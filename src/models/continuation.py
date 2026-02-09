from typing import Any, Optional

from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.runnables import Runnable, RunnableConfig, RunnableBinding
from langchain_core.runnables import RunnableSequence
from ..logging import get_logger
from ..config import config as app_config

class ContinuationProxy(Runnable):
    """
    A proxy around a ChatModel that handles truncated responses (finish_reason='length')
    by automatically requesting continuation and concatenating the results.
    
    This effectively gives the illusion of a larger context window or longer generation capability
    to downstream components (like structural parsers).
    """
    
    def __init__(self, model: Runnable, max_continuations: int = None, logger = None, agent_name: str = ""):
        self.model = model
        # Use config defaults if not specified
        cont_cfg = app_config.continuation
        self.max_continuations = max_continuations if max_continuations is not None else cont_cfg.max_continuations
        self.logger = logger or get_logger()
        self.agent_name = agent_name
        
        # Loop detection thresholds from config
        self.ttr_threshold = cont_cfg.ttr_threshold
        self.ngram_duplication_threshold = cont_cfg.ngram_duplication_threshold
        self.ngram_size = cont_cfg.ngram_size
        self.tail_chars = cont_cfg.tail_chars

    def _is_likely_looping_pre_continuation(self, text: str) -> tuple[bool, str]:
        """
        Lightweight check BEFORE attempting continuation.
        Returns (is_looping, reason_string).
        """
        if len(text) < self.tail_chars:
            return False, ""  # Not enough data to judge
        
        tail = text[-self.tail_chars:]
        tokens = tail.split()  # Simple whitespace tokenization
        
        if len(tokens) < self.ngram_size:
            return False, ""
        
        # 1. Type-Token Ratio (TTR) Check
        ttr = len(set(tokens)) / len(tokens)
        if ttr < self.ttr_threshold:
            return True, f"TTR={ttr:.2f} < {self.ttr_threshold} (low vocabulary diversity)"
        
        # 2. Rep-N (N-gram Duplication) Check
        ngrams = [tuple(tokens[i:i+self.ngram_size]) for i in range(len(tokens) - self.ngram_size + 1)]
        if ngrams:
            unique_ratio = len(set(ngrams)) / len(ngrams)
            if unique_ratio < (1 - self.ngram_duplication_threshold):
                return True, f"Ngram unique ratio={unique_ratio:.2f} (>{self.ngram_duplication_threshold*100:.0f}% duplicates)"
        
        return False, ""

    def invoke(self, input: Any, config: Optional[RunnableConfig] = None, **kwargs: Any) -> Any:
        # Initial invocation
        response = self.model.invoke(input, config=config, **kwargs)
        
        # Only handle continuation for AIMessages (chat models)
        if not isinstance(response, AIMessage):
            return response
            
        # Check for truncation
        attempts = 0
        current_response = response
        
        while attempts < self.max_continuations:
            # Detect truncation from metadata
            meta = current_response.response_metadata or {}
            finish_reason = meta.get("finish_reason")
            
            # Check Vertex/Gemini nested candidates structure if top-level missing
            if not finish_reason:
                usage_meta = meta.get("usage_metadata")
                if not finish_reason and meta.get("candidates"):
                     # Vertex AI often puts it in candidates[0]
                     finish_reason = meta["candidates"][0].get("finish_reason")
            
            # OpenAI/Vertex Standard: 'length' or 'MAX_TOKENS'
            is_truncated = finish_reason in ("length", "MAX_TOKENS")
            
            if not is_truncated:
                break
                
            attempts += 1
            agent_context = f"[{self.agent_name}] " if self.agent_name else ""
            
            # PRE-CONTINUATION LOOP CHECK
            # Before requesting continuation, check if the current response is already looping
            is_looping, loop_reason = self._is_likely_looping_pre_continuation(response.content)
            if is_looping:
                if self.logger:
                    self.logger.log_warning(f"{agent_context}Pre-continuation loop detected: {loop_reason}. Aborting continuation.")
                # Truncate repeating tail and return what we have
                response.content = self._truncate_loop(response.content)
                break
            
            if self.logger:
                 self.logger.log_error(f"{agent_context}Response truncated (reason={finish_reason}). Attempting continuation {attempts}/{self.max_continuations}...")
            
            # Prepare continuation prompt
            # We append the previous AI response (so far) and a user prompt to continue
            # Note: 'input' is usually a list of messages. We shouldn't modify the original list.
            messages = list(input) if isinstance(input, list) else [input]
            
            # If we are in a loop, 'messages' needs to include what we've generated so far
            # 'current_response' contains the chunk.
            # But wait, we need to append to the FULL conversation history.
            
            # We need to construct a new message history for the continuation call
            # 1. Original messages
            # 2. The AI's PARTIAL response (as a message)
            # 3. User's instruction to continue
            
            # For the first continuation, 'response' is the partial.
            # For subsequent, 'response' accumulates content, but we need the *last chunk* for the model?
            # Actually, standard pattern:
            # messages + [AIMessage(content=response.content), HumanMessage(content="Continue...")]
            
            # BUT: 'response' object is accumulating content? No, 'response' is the initial object.
            # We need to be careful about accumulating content vs messages.
            
            # Let's accumulate content in 'combined_content'
            # And for the prompt, we pass the *full accumulated text so far*? 
            # OR just the last chunk?
            # Most models work best if you just append the last partial message and say "Continue".
            
            # CORRECT LOGIC:
            # We have 'response' which holds the ACCUMULATED message so far (we will update it).
            # But we need to prompt the model.
            
            # On attempt 1:
            # input messages + [AIMessage(content=original_chunk)] + [HumanMessage("Continue")]
            
            # On attempt 2:
            # input messages + [AIMessage(content=original_chunk)] + [HumanMessage("Continue")] + [AIMessage(content=chunk2)] + [HumanMessage("Continue")]
            # This grows the context window fast.
            
            # PREFERRED LOGIC for recent models (Llama 3/4):
            # Just extend the conversation.
            
            # We need to track the *extension* messages separately
            # We can't modify 'input' directly if it's reused elsewhere, but here it's fine.
            
            # Let's clone input for safety
            param_messages = list(input) if isinstance(input, list) else [input]
            
            # We need to append ALL previous chunks to the history correctly
            # But 'response' (the variable) should be the *merged* result at the end.
            
            # Let's track chunks
            # We need the last received chunk to append to history
            last_chunk = current_response
            
            # Append last chunk to history
            # Note: We strip metadata/id to avoid confusion, just content
            param_messages.append(AIMessage(content=last_chunk.content))
            
            # Append continuation instruction
            param_messages.append(HumanMessage(content="Your previous response was truncated. Please continue exactly where you left off."))
            
            # Invoke again
            next_chunk = self.model.invoke(param_messages, config=config, **kwargs)
            
            if not isinstance(next_chunk, AIMessage):
                # Should not happen for chat models
                break
                
            # Merge content
            response.content += next_chunk.content

            # Check for loop in the tail of accumulated content
            if self._detect_loop(response.content):
                if self.logger:
                    self.logger.log_error("Loop detected in LLM response. Aborting continuation.")
                # Strip the repeating tail to keep the response clean
                response.content = self._truncate_loop(response.content)
                break
            
            # Update usage metadata if possible (sum tokens)
            self._merge_usage(response, next_chunk)
            
            # Update current response pointer for next loop check
            current_response = next_chunk
            
            # We break loop if next_chunk is not truncated (checked at top of loop)
            # But we need to update 'input' for next iteration? 
            # Actually, we reconstructed 'param_messages' from 'input' (original) + all previous chunks?
            # No, my logic above only added the *last* chunk to 'input'. 
            # If we loop twice, we need:
            # Input + Chunk1 + Prompt + Chunk2 + Prompt
            # My logic:
            # Loop 1: param = Input + Chunk1 + Prompt -> Chunk2
            # Loop 2: need Input + Chunk1 + Prompt + Chunk2 + Prompt
            
            # So we need to maintain a running list of 'extension_messages'
            # OR just update 'input' variable (reassigned local var)
            input = param_messages # Now input includes Chunk1 + Prompt
            # Next loop will append Chunk2 + Prompt
            
        if self.logger and attempts >= self.max_continuations:
             agent_context = f"[{self.agent_name}] " if self.agent_name else ""
             self.logger.log_error(f"{agent_context}Max continuations ({self.max_continuations}) exhausted. Response may be incomplete.")

        return response

    def _detect_loop(self, text: str, min_repeat_len: int = 20, repetitions: int = 3) -> bool:
        """ Detects if the end of the text is repeating the same block. """
        if not text:
            return False
            
        # Clean trailing whitespace for more accurate tail detection
        clean_text = text.rstrip()
        if len(clean_text) < min_repeat_len * repetitions:
            return False
            
        # Check trailing substrings of various lengths
        # We start from min_repeat_len up to len/repetitions
        for length in range(min_repeat_len, (len(clean_text) // repetitions) + 1):
            tail = clean_text[-length:]
            count = 1
            for i in range(1, repetitions):
                start = -length * (i + 1)
                end = -length * i
                if clean_text[start:end] == tail:
                    count += 1
                else:
                    break
            if count >= repetitions:
                return True
        return False

    def _truncate_loop(self, text: str) -> str:
        """ Truncates the repeating tail of a looping response. """
        # Find the repeat block
        for length in range(20, len(text) // 2):
            tail = text[-length:]
            if text[-(length*2):-length] == tail:
                # Found repeat, keep only one copy and strip the rest
                base = text[:-length]
                # Recursively clean if there's more
                while base.endswith(tail):
                    base = base[:-length]
                return base + tail
        return text

    def _merge_usage(self, target: AIMessage, source: AIMessage):
        """Merge token usage from source into target."""
        t_meta = target.response_metadata or {}
        s_meta = source.response_metadata or {}
        
        t_usage = t_meta.get("token_usage") or t_meta.get("usage") or {}
        s_usage = s_meta.get("token_usage") or s_meta.get("usage") or {}
        
        if not t_usage or not s_usage:
            return
            
        # Sum known fields
        for key in ["completion_tokens", "prompt_tokens", "total_tokens", "output_tokens", "input_tokens"]:
            if key in s_usage and key in t_usage:
                t_usage[key] += s_usage[key]
                
        # Update target
        if "token_usage" in t_meta:
            t_meta["token_usage"] = t_usage
        if "usage" in t_meta:
            t_meta["usage"] = t_usage
            
        target.response_metadata = t_meta

    def bind(self, **kwargs: Any) -> Runnable:
        """
        Bind arguments to the model. 
        Returns a new ContinuationProxy wrapping the BOUND model.
        This allows the proxy to persist through .bind() calls (used by with_structured_output).
        """
        return ContinuationProxy(self.model.bind(**kwargs), self.max_continuations, self.logger, self.agent_name)

    def with_structured_output(self, schema: Any, **kwargs: Any) -> Runnable:
        """
        Pass through to the underlying model's with_structured_output, 
        but ensure the Proxy remains in the chain if possible.
        
        Problem: outer.with_structured_output(schema) returns a new RunnableSequence (Model | Parser).
        The 'Model' in that sequence is 'self.model', NOT 'self' (Proxt).
        
        We need to intercept this.
        """
        # Let the inner model create the chain (handling prompts, binding tools, etc)
        chain = self.model.with_structured_output(schema, **kwargs)
        
        # DEBUG: Print chain structure
        # print(f"DEBUG: ContinuationProxy chain type: {type(chain)}")
        # if hasattr(chain, "steps"):
        #     print(f"DEBUG: Chain steps: {chain.steps}")
        # elif isinstance(chain, RunnableBinding):
        #     print(f"DEBUG: Chain bound: {chain.bound}")
        
        if hasattr(chain, "steps"):
            # It's a RunnableSequence [BoundModel, Parser] or [RunnableParallel, Parser]
            steps = list(chain.steps)
            
            # Step 0 is usually the model interaction. 
            # With include_raw=True, it's often a dict (RunnableParallel): {'raw': BoundModel}
            first_step = steps[0]
            
            if isinstance(first_step, dict):
                # Update the 'raw' component if it exists
                if "raw" in first_step:
                     first_step["raw"] = ContinuationProxy(first_step["raw"], self.max_continuations, self.logger, self.agent_name)
                else:
                    # Fallback: wrap all values? Or assume single value?
                    # Generally 'raw' is the key used by include_raw=True
                    # Let's try to wrap all values that look like runnables
                    for k, v in first_step.items():
                        if hasattr(v, "invoke"): # basic check
                             first_step[k] = ContinuationProxy(v, self.max_continuations, self.logger, self.agent_name)
                
                # Reassign modified dict
                steps[0] = first_step
                return RunnableSequence(*steps)
                
            else:
                # It's a direct Runnable (e.g. RunnableBinding)
                steps[0] = ContinuationProxy(steps[0], self.max_continuations, self.logger, self.agent_name)
                return RunnableSequence(*steps)
            
        elif isinstance(chain, RunnableBinding):
            # It might be just the bound model (if include_raw=True sometimes?)
            # Just wrap it
            return ContinuationProxy(chain, self.max_continuations, self.logger, self.agent_name)
            
        else:
            # Fallback: If structure is unknown, we can't safely inject the proxy.
            # But we can log a warning.
            # Or just return chain (no continuation for this case).
            return chain

    def __getattr__(self, name: str) -> Any:
        # Delegate unknown attributes to the underlying model
        # This allows access to 'temperature', 'max_tokens', etc.
        return getattr(self.model, name)
