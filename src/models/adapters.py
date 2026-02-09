"""
Unified Model Factory - Single entry point for all LLM providers.
Supports: 
- OpenAI: GPT-5.2
- Anthropic: Claude 4.5
- Vertex AI MaaS: Gemini 3 Pro, Llama 4
- Vertex AI Endpoint: MedGemma 27B

All calls are automatically logged for research transparency using a LoggedInvoker wrapper.
"""

import os
import time
from typing import Any, Literal
import json
import subprocess
from dataclasses import dataclass
from langchain_core.messages import BaseMessage, SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from langchain_google_vertexai.model_garden import ChatAnthropicVertex
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.runnables import RunnableLambda
from google.cloud import aiplatform
from google.api_core import exceptions as google_exceptions
import copy
import hashlib

from ..logging import get_logger
from ..utils.json_utils import extract_json_from_text
from .continuation import ContinuationProxy

# Retry configuration for transient API errors
RETRY_MAX_ATTEMPTS = 3
RETRY_BACKOFF_BASE = 15.0  # seconds
RETRY_STATUS_CODES = {401, 429, 500, 502, 503, 504}


def _is_retryable_error(error: Exception) -> bool:
    """Check if an error is transient and should be retried."""
    # Check for specific Google API exceptions if available
    if google_exceptions:
        if isinstance(error, (google_exceptions.ServiceUnavailable, 
                              google_exceptions.DeadlineExceeded, 
                              google_exceptions.ResourceExhausted,
                              google_exceptions.Aborted,
                              google_exceptions.InternalServerError)):
            return True

    error_str = str(error)
    
    # Check for status_code attribute (common in HTTP errors)
    if hasattr(error, "status_code"):
        if error.status_code in RETRY_STATUS_CODES:
            return True
            
    # Check for HTTP status codes in error message
    for code in RETRY_STATUS_CODES:
        if f"code: {code}" in error_str or f"code:{code}" in error_str:
            return True
            
    # Check for common transient error patterns
    if "UNAUTHENTICATED" in error_str or "UNAVAILABLE" in error_str:
        return True
    if "rate limit" in error_str.lower() or "quota" in error_str.lower() or "resource exhausted" in error_str.lower():
        return True
        
    # Check for JSON parsing errors (common with flaky backends receiving malformed HTTP responses)
    if isinstance(error, json.JSONDecodeError):
        return True
    if "Extra data" in error_str or "Expecting value" in error_str:
        return True
        
    return False


def _retry_with_backoff(func, *args, logger=None, agent_name=None, **kwargs):
    """Execute a function with exponential backoff retry on transient errors."""
    last_error = None
    for attempt in range(RETRY_MAX_ATTEMPTS):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            last_error = e
            if not _is_retryable_error(e) or attempt == RETRY_MAX_ATTEMPTS - 1:
                if attempt == RETRY_MAX_ATTEMPTS - 1 and logger:
                     agent_context = f"[{agent_name}] " if agent_name else ""
                     logger.log_error(f"{agent_context}Max retries ({RETRY_MAX_ATTEMPTS}) exhausted for transient error. Succeeded: False. Last error: {str(e)[:500]}")
                raise
            wait_time = RETRY_BACKOFF_BASE * (2 ** attempt)
            if logger:
                agent_context = f"[{agent_name}] " if agent_name else ""
                logger.log_error(f"{agent_context}Transient error (attempt {attempt + 1}/{RETRY_MAX_ATTEMPTS}), retrying in {wait_time}s: {str(e)[:200]}")
            time.sleep(wait_time)
    raise last_error  # Should not reach here


ModelProvider = Literal[
    "openai",                   # GPT models via OpenAI API
    "anthropic",                # Claude via Anthropic API
    "google_genai",             # Gemini, Llama via Vertex AI MaaS / GenAI
    "anthropic_vertex",         # Claude via Vertex AI (Anthropic)
    "vertex_endpoint_openai",   # MedGemma via Vertex AI Endpoint (OpenAI Protocol)
    "vertexai",                 # Vertex AI (for generic MaaS if needed)
    "vertex_openapi",           # Vertex AI OpenAPI
    "huggingface_endpoint",     # Hugging Face Inference Endpoints
]


@dataclass
class ModelAdapterConfig:
    """Configuration for a specific model."""
    provider: ModelProvider
    model_name: str
    display_name: str
    api_key_env: str = ""
    project_id_env: str = "GOOGLE_CLOUD_PROJECT"
    location_env: str = "GOOGLE_CLOUD_LOCATION"
    # Override location for preview models (e.g., "global")
    location_override: str = ""
    endpoint_id_env: str = ""  # For Vertex Endpoints
    temperature: float = 0.2
    max_tokens: int = 8192
    is_medical_specialized: bool = False

    # Capability & Research Flags
    supports_json_schema: bool = True
    requires_global_location: bool = False
    allow_heuristic_recovery: bool = False
    max_images: int = 10  # Default limit for multimodal models
    max_continuations: int = 1 # Default number of auto-continuations for truncated responses

    # Generation Parameters
    frequency_penalty: float | None = None
    presence_penalty: float | None = None

    # Reasoning / Thinking Configurations
    reasoning_effort: str = "none"         # OpenAI: low, medium, high, none
    thinking_level: str = ""               # Gemini: LOW, MEDIUM, HIGH
    budget_tokens: int = 0                 # Claude: Number of tokens for thinking
    use_vertex_api: bool = True            # Whether to use Vertex AI API (vs generic Google GenAI)
    endpoint_url: str = ""                 # Explicit Endpoint URL (e.g. for Hugging Face)


# Supported models registry
SUPPORTED_MODELS = {
    # --- OpenAI ---
    "gpt-5.2": ModelAdapterConfig(
        provider="openai",
        model_name="gpt-5.2-2025-12-11",
        display_name="GPT-5.2",
        api_key_env="OPENAI_API_KEY",
        reasoning_effort="none",  # Default for GPT-5.2
        max_images=3,
    ),

    # --- Vertex AI MaaS (Gemini / GenAI) ---
    "gemini-3-pro": ModelAdapterConfig(
        provider="google_genai",
        model_name="gemini-3-pro-preview",
        display_name="Gemini 3 Pro",
        location_override="global",
        requires_global_location=True,
        max_images=3,
        thinking_level="high",  # Default for Gemini 3 Pro
    ),

    # --- Anthropic ---
    "claude-4.5-opus": ModelAdapterConfig(
        provider="anthropic",
        model_name="claude-opus-4-5-20251101",
        display_name="Claude 4.5 Opus",
        api_key_env="ANTHROPIC_API_KEY",
        max_images=3,
        temperature=1, # must be 1 for Claude 4.5 with thinking
    ),

    "llama-4": ModelAdapterConfig(
        provider="vertex_openapi",  # Uses OpenAI-compatible API on Vertex
        model_name="meta/llama-4-maverick-17b-128e-instruct-maas",
        location_override="us-east5",  # Llama 4 ONLY available in us-east5
        display_name="Llama 4 Maverick",
        max_images=3,
    ),

    # --- Hugging Face Endpoints ---
    "medgemma-27b": ModelAdapterConfig(
        provider="huggingface_endpoint",
        model_name="google/medgemma-27b-it",
        endpoint_url="https://vw6dpmkurd9rzaqh.us-east-1.aws.endpoints.huggingface.cloud",
        display_name="MedGemma 27B",
        api_key_env="HUGGINGFACEHUB_API_TOKEN",
        is_medical_specialized=True,
        max_images=3, # Multimodal support
    ),
}


class LoggedRunner:
    """
    Wrapper for structured output runnables that adds logging.
    """

    def __init__(self, runner, outer, pydantic_schema=None):
        self.runner = runner
        self.outer = outer
        self.pydantic_schema = pydantic_schema

    def invoke(self, messages: list[BaseMessage], **kwargs):
        t0 = time.time()
        # Define a safe invoker that handles JSON 'Extra data' errors properly
        # This needs to be INSIDE the retry loop so that a recoverable JSON error
        # isn't treated as a transient failure that triggers retries.
        def safe_invoke(*args, **kwargs):
            try:
                return self.runner.invoke(*args, **kwargs)
            except Exception as e:
                # --- Robust Recovery for "Extra data" JSON errors ---
                # Common with reasoning models (Llama, etc.) that append text after JSON.
                # Extract underlying JSON error if wrapped (e.g. by LangChain)
                json_err = e
                if not isinstance(json_err, json.JSONDecodeError) and hasattr(e, "args") and len(e.args) > 0:
                    if isinstance(e.args[0], json.JSONDecodeError):
                        json_err = e.args[0]
                    elif hasattr(e, "cause") and isinstance(e.cause, json.JSONDecodeError): # Python 3.11+ or custom wrappers
                        json_err = e.cause

                if isinstance(json_err, json.JSONDecodeError) and json_err.msg.startswith("Extra data"):
                    try:
                        # The parser found valid JSON up to .pos, but there was extra data.
                        # We can simply truncate at .pos to get the valid JSON.
                        raw_text = json_err.doc
                        valid_json_str = raw_text[:json_err.pos]
                        
                        parsed_obj = json.loads(valid_json_str)
                        
                        # CRITICAL: Check if the "recovered" JSON is actually an API error response
                        # e.g. {"code": 400, "message": "...", "type": "BadRequestError"}
                        if isinstance(parsed_obj, dict) and (
                            "error" in parsed_obj or 
                            (parsed_obj.get("code", 0) >= 400 and "message" in parsed_obj) or
                            "BadRequestError" in parsed_obj.get("type", "")
                        ):
                             error_msg = f"API Error captured as output: {parsed_obj}"
                             self.outer.logger.log_error(error_msg)
                             raise Exception(error_msg)

                        # Reconstruct the expected structure (Parsed vs Raw)
                        # If include_raw=True, LangChain returns {"parsed": ..., "raw": ...}
                        # We emulate this for downstream compatibility.
                        
                        log_msg = f"Recovered from JSON 'Extra data' error. Truncated {len(raw_text) - len(valid_json_str)} excess chars."
                        self.outer.logger.log_recovery(log_msg, original_error=json_err)
                        
                        return {
                            "parsed": parsed_obj,
                            "raw": AIMessage(content=raw_text)
                        }
                    except Exception as rec_e:
                        # If recovery fails, log and re-raise the NEW exception (rec_e) which contains the true cause (e.g. API Error)
                        self.outer.logger.log_error(f"Failed to recover from JSON extra data: {rec_e}")
                        raise rec_e
                
                # If not a recoverable JSON error, re-raise to let retry logic handle it (if transient)
                raise e

        try:
            result = _retry_with_backoff(safe_invoke, messages, logger=self.outer.logger, agent_name=self.outer.agent_name, **kwargs)
        except Exception as e:
            # Extract system and user prompts properly for error logging
            sys_prompt = next((m.content for m in reversed(messages) if isinstance(m, SystemMessage)), "")
            usr_prompt = next((m.content for m in reversed(messages) if isinstance(m, HumanMessage)), "")

            # Provide context on runner failure
            self.outer.logger.log_llm_call(
                model_name=f"{self.outer.config.provider}/{self.outer.config.model_name} (failed)",
                temperature=self.outer.config.temperature,
                max_tokens=self.outer.config.max_tokens,
                system_prompt=sys_prompt,
                user_prompt=usr_prompt,
                response_text=str(e),
                agent_name=self.outer.agent_name,
                task_description="structured_output_failure",
                latency_ms=(time.time() - t0) * 1000,
                full_messages=messages,
                prompt_tokens=0, completion_tokens=0
            )
            raise e

        latency_ms = (time.time() - t0) * 1000

        # Unwrap 'include_raw=True' result first
        raw_msg = None
        prompt_tokens = 0
        completion_tokens = 0
        reasoning_tokens = 0

        if isinstance(result, dict) and "parsed" in result and "raw" in result:
            raw_msg = result["raw"]
            result = result["parsed"]

            # Extract tokens from raw message usage_metadata
            if hasattr(raw_msg, "usage_metadata") and raw_msg.usage_metadata:
                usage = raw_msg.usage_metadata
                prompt_tokens = usage.get("input_tokens", 0)
                completion_tokens = usage.get("output_tokens", 0)

                # Check for reasoning tokens
                completion_details = usage.get("completion_tokens_details") or {}
                if isinstance(completion_details, dict):
                    reasoning_tokens = completion_details.get("reasoning_tokens", 0)

                # Check for Gemini specific fields
                if isinstance(usage, dict):
                    reasoning_tokens = reasoning_tokens or usage.get("thoughts_token_count", 0)
                    total_tokens = usage.get("total_token_count", 0)
                    input_tokens_meta = usage.get("prompt_token_count", 0)
                else:
                    reasoning_tokens = reasoning_tokens or getattr(usage, "thoughts_token_count", 0)
                    total_tokens = getattr(usage, "total_token_count", 0)
                    input_tokens_meta = getattr(usage, "prompt_token_count", 0)

                # Correct completion_tokens for billing
                if total_tokens > 0 and input_tokens_meta > 0:
                    billable_output = total_tokens - input_tokens_meta
                    if billable_output > completion_tokens:
                        completion_tokens = billable_output

        # If result is still a string (common in json_mode without pydantic parsing), parse it
        if isinstance(result, str):
            def fix_json_callback(bad_json: str) -> str:
                """Helper to ask LLM to fix malformed JSON."""
                prompt = (
                    "You are a helpful assistant that extracts and fixes JSON.\n"
                    "The following text contains an intended JSON object or array but may be malformed...\n"
                    f"INPUT:\n{bad_json}\n\nOUTPUT:"
                )
                try:
                    fix_messages = [HumanMessage(content=prompt)]
                    resp = self.outer.model.invoke(fix_messages, temperature=self.outer.config.temperature)
                    return resp.content
                except Exception:
                    return ""
            result = extract_json_from_text(result, fix_callback=fix_json_callback)

        # Handle tool-call result wrapped as dictionary (Llama 4 behavior)
        if isinstance(result, dict) and result.get("type") == "function" and "name" in result and "parameters" in result:
            result = result["parameters"]

        # Handle double-wrapped structure: {"type": "json", "content": {...}}
        if isinstance(result, dict) and result.get("type") == "json" and "content" in result:
            content = result["content"]
            if isinstance(content, str):
                result = extract_json_from_text(content)
            else:
                result = content

        # Handle case where LLM wraps everything in a single key (e.g. "analysis_results", "output", etc)
        # but only if the root doesn't already contain required keys from the schema
        if isinstance(result, dict) and self.pydantic_schema:
            required_keys = {k for k, v in self.pydantic_schema.model_fields.items() if v.is_required()}

            # Check if required keys are missing at root
            if not any(k in result for k in required_keys):
                # Try single-key wrapper unwrap
                if len(result) == 1:
                    wrapper_key = list(result.keys())[0]
                    if isinstance(result[wrapper_key], dict):
                        result = result[wrapper_key]

                # If still missing keys, do a recursive search (if allowed)
                if self.outer.config.allow_heuristic_recovery and isinstance(result, dict) and not any(k in result for k in required_keys):
                    def find_schema_match(obj: dict, required: set) -> dict | None:
                        """Recursively search for a dict containing required keys."""
                        if any(k in obj for k in required):
                            return obj
                        for v in obj.values():
                            if isinstance(v, dict):
                                match = find_schema_match(v, required)
                                if match:
                                    return match
                        return None

                    match = find_schema_match(result, required_keys)
                    if match:
                        result = match

        # Finally, perform Pydantic Validation if requested
        if self.pydantic_schema:
            if result is None:
                # Attempt to retrieve raw content and debug info
                raw_content = ""
                tool_calls = []
                invalid_tool_calls = []
                
                if raw_msg:
                    raw_content = getattr(raw_msg, 'content', "")
                    tool_calls = getattr(raw_msg, 'tool_calls', [])
                    invalid_tool_calls = getattr(raw_msg, 'invalid_tool_calls', [])
                
                error_context = f"Raw response content: '{raw_content}'"
                if tool_calls:
                    error_context += f", Tool Calls: {tool_calls}"
                if invalid_tool_calls:
                    error_context += f", Invalid Tool Calls: {invalid_tool_calls}"
                    
                error_msg = f"Structured output returned None (failed to parse JSON from model response). {error_context}"
                self.outer.logger.log_error(error_msg)
                
                # Check for invalid tool calls specifically
                if invalid_tool_calls:
                     for itc in invalid_tool_calls:
                         if 'error' in itc:
                              self.outer.logger.log_error(f"Tool call error: {itc['error']}")
                
                # Try a final fallback extraction if we have raw content
                if raw_content and isinstance(raw_content, str):
                    try:
                        fallback_json = extract_json_from_text(raw_content)
                        if fallback_json:
                            self.outer.logger.log_recovery(f"Recovered JSON from raw text after parser failure.")
                            result = self.pydantic_schema.model_validate(fallback_json)
                    except Exception as fallback_e:
                        self.outer.logger.log_error(f"Fallback JSON validation failed: {fallback_e}")


                if result is None:
                    raise ValueError(error_msg)

            # Check if result is still a string after extraction attempts
            if isinstance(result, str):
                raise ValueError(f"Failed to parse JSON from model response: {result}")

            if isinstance(result, dict):
                try:
                    result = self.pydantic_schema.model_validate(result)
                except Exception as e:
                    self.outer.logger.log_error(f"Pydantic Validation failed. Input Type: {type(result)}. Input (partial): {str(result)[:500]}")
                    self.outer.logger.log_llm_call(
                        model_name=f"{self.outer.config.provider}/{self.outer.config.model_name} (validation_error)",
                        temperature=self.outer.config.temperature,
                        max_tokens=self.outer.config.max_tokens,
                        system_prompt="",
                        user_prompt="",
                        response_text=f"Validation Failed: {e}. Raw: {result}",
                        agent_name=self.outer.agent_name,
                        task_description="structured_output_validation_error",
                        latency_ms=latency_ms,
                        prompt_tokens=prompt_tokens, completion_tokens=completion_tokens
                    )
                    raise ValueError(f"Pydantic Validation Failed: {e}") from e

        # Prepare parsed_json for logging
        parsed_json_obj = None
        if hasattr(result, "model_dump"):
            parsed_json_obj = result.model_dump()
        elif hasattr(result, "dict"):
             parsed_json_obj = result.dict()
        elif isinstance(result, (dict, list)):
            parsed_json_obj = result

        # Determine response_text (prefer raw output)
        if raw_msg and hasattr(raw_msg, 'content'):
            if isinstance(raw_msg.content, list):
                # Join content blocks if it's a list (multimodal/multiblock)
                response_text = ""
                for block in raw_msg.content:
                    if isinstance(block, dict):
                        response_text += block.get("text", str(block))
                    else:
                        response_text += str(block)
            else:
                response_text = raw_msg.content
        elif isinstance(result, str) and not self.pydantic_schema:
             response_text = result
        else:
             # Fallback to serialized result
             if hasattr(result, "model_dump_json"):
                 response_text = result.model_dump_json()
             elif isinstance(result, (dict, list)):
                 response_text = json.dumps(result)
             elif result is None and raw_msg:
                 # Fallback to raw content if result is None (parsing failed)
                 content = getattr(raw_msg, 'content', str(raw_msg))
                 if isinstance(content, list):
                     response_text = " ".join(str(b) for b in content)
                 else:
                     response_text = str(content)
             else:
                 response_text = str(result)

        system_prompt = next((m.content for m in reversed(messages) if isinstance(m, SystemMessage)), "")
        user_prompt = next((m.content for m in reversed(messages) if isinstance(m, HumanMessage)), "")

        self.outer.logger.log_llm_call(
            model_name=f"{self.outer.config.provider}/{self.outer.config.model_name} (structured)",
            temperature=self.outer.config.temperature,
            max_tokens=self.outer.config.max_tokens,
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            response_text=response_text,
            agent_name=self.outer.agent_name,
            task_description="structured_output",
            latency_ms=latency_ms,
            full_messages=messages,
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
            reasoning_tokens=reasoning_tokens,
            parsed_json=parsed_json_obj,
        )
        return result


class LoggedInvoker:
    """
    Wrapper that adds research logging (metrics, prompts, latency) to any model.
    """

    def __init__(self, model, config: ModelAdapterConfig, agent_name: str = ""):
        self.model = model
        self.config = config
        self.agent_name = agent_name
        self.logger = get_logger()

    def invoke(self, messages: list[BaseMessage], task_description: str = "", **kwargs) -> AIMessage:
        t0 = time.time()

        # Invoke the underlying LangChain model with retry for transient errors
        resp = _retry_with_backoff(self.model.invoke, messages, logger=self.logger, agent_name=self.agent_name, **kwargs)
        
        # Normalize response content: Convert list (multimodal chunks) to string for downstream compatibility
        if isinstance(resp.content, list):
            joined_text = ""
            for block in resp.content:
                if isinstance(block, dict) and "text" in block:
                    joined_text += block["text"]
                elif isinstance(block, str):
                    joined_text += block
                # Ignore non-text blocks (like tool calls or media if any, though usually 'text' covers content)
            
            # Replace list content with normalized string
            # We modify the AIMessage object in place
            resp.content = joined_text

        latency_ms = (time.time() - t0) * 1000

        # Extract tokens/usage if present
        prompt_tokens = 0
        completion_tokens = 0

        meta = getattr(resp, "response_metadata", {}) or {}
        usage = meta.get("token_usage") or meta.get("usage") or {}

        prompt_tokens = usage.get("prompt_tokens") or usage.get("input_tokens") or 0
        completion_tokens = usage.get("completion_tokens") or usage.get("output_tokens") or 0

        # Check for reasoning tokens (OpenAI: completion_tokens_details.reasoning_tokens)
        reasoning_tokens = 0
        completion_details = usage.get("completion_tokens_details") or {}
        if isinstance(completion_details, dict):
            reasoning_tokens = completion_details.get("reasoning_tokens", 0)

        # In LangChain Google GenAI/VertexAI, usage_metadata might be in response_metadata
        # Check 'usage_metadata' dict in meta which is sometimes passed through
        usage_meta_raw = meta.get("usage_metadata")
        if usage_meta_raw:
            # It could be a dict or object
            if isinstance(usage_meta_raw, dict):
                reasoning_tokens = reasoning_tokens or usage_meta_raw.get("thoughts_token_count", 0)
                total_tokens = usage_meta_raw.get("total_token_count", 0)
                input_tokens_meta = usage_meta_raw.get("prompt_token_count", 0)
            else:
                reasoning_tokens = reasoning_tokens or getattr(usage_meta_raw, "thoughts_token_count", 0)
                total_tokens = getattr(usage_meta_raw, "total_token_count", 0)
                input_tokens_meta = getattr(usage_meta_raw, "prompt_token_count", 0)

            # Correct completion_tokens for billing if total implies separate thoughts
            # (Gemini total_token_count is the authority for billing)
            if total_tokens > 0 and input_tokens_meta > 0:
                billable_output = total_tokens - input_tokens_meta
                if billable_output > completion_tokens:
                    completion_tokens = billable_output

        system_prompt = next((m.content for m in reversed(messages) if isinstance(m, SystemMessage)), "")
        user_prompt = next((m.content for m in reversed(messages) if isinstance(m, HumanMessage)), "")

        self.logger.log_llm_call(
            model_name=f"{self.config.provider}/{self.config.model_name}",
            temperature=self.config.temperature,
            max_tokens=self.config.max_tokens,
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            response_text=resp.content,
            agent_name=self.agent_name,
            task_description=task_description,
            latency_ms=latency_ms,
            full_messages=messages,
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
            reasoning_tokens=reasoning_tokens,
        )
        return resp

    def with_structured_output(self, schema: Any, method: str = "json_mode") -> Any:
        """
        Wraps structured output. LangChain's .with_structured_output returns a Runnable.
        We wrap that runnable to log the execution.
        """
        if not self.config.supports_json_schema:
            raise NotImplementedError(f"Structured output not supported for {self.config.model_name}")

        # Vertex AI requires strict JSON schema (no additionalProperties). Convert Pydantic to sanitized dict.
        # Deep copy to prevent mutation of the original schema
        target_schema = copy.deepcopy(schema)
        
        if isinstance(schema, type) and issubclass(schema, BaseMessage):
            # It's a message type, unlikely for structured output but possible
            pass
        elif hasattr(schema, "model_json_schema"):
            # It is a Pydantic model (v2)
            schema_dict = schema.model_json_schema()
            target_schema = self._sanitize_schema(copy.deepcopy(schema_dict))
        elif isinstance(schema, dict):
            target_schema = self._sanitize_schema(copy.deepcopy(schema))

        # Pass sanitized dict for Vertex/Google providers (except OpenAI-compatible ones).
        if ("google" in self.config.provider or "vertex" in self.config.provider) and "openai" not in self.config.provider:
            # Default to json_schema for Google models if json_mode is requested
            target_method = "json_schema" if method == "json_mode" else method
            runner = self.model.with_structured_output(target_schema, method=target_method, include_raw=True)
        elif self.config.provider == "openai":
            # For OpenAI, explicit function_calling is often safer/more stable than json_mode for complex schemas
            target_method = "function_calling" if method == "json_mode" else method
            runner = self.model.with_structured_output(schema, method=target_method, include_raw=True)
        elif self.config.provider == "huggingface_endpoint":            
            # Use PydanticOutputParser to generate prompt instructions
            parser = PydanticOutputParser(pydantic_object=schema)
            format_instructions = parser.get_format_instructions()
            
            def prompt_augmentation(input_val):
                messages = list(input_val) if isinstance(input_val, list) else [input_val]
                # Inject instructions. Prefer SystemMessage if supported, else append to last HumanMessage.
                # For vLLM/OpenAI-compat, SystemMessage is standard.
                # We place it at the END to ensure it's not forgotten (recency bias)
                messages.append(SystemMessage(content=f"\nIMPORTANT: You must output a valid JSON object matching the schema below.\n{format_instructions}\nDo not include any markdown formatting like ```json."))
                return messages
                
            def _prune_null_objects(obj):
                """Recursively replace dicts with all-None values with None."""
                if isinstance(obj, dict):
                    # Recurse first
                    cleaned = {k: _prune_null_objects(v) for k, v in obj.items()}
                    # If all values are None, return None (unless empty dict is valid, but usually signifies missing data in this context)
                    if cleaned and all(v is None for v in cleaned.values()):
                        return None
                    return cleaned
                elif isinstance(obj, list):
                    return [_prune_null_objects(x) for x in obj]
                return obj

            def parsing_step(raw_msg):
                 try:
                     # Try generic extraction first which handles markdown code blocks
                     text = raw_msg.content if hasattr(raw_msg, "content") else str(raw_msg)
                     
                     json_obj = extract_json_from_text(text)
                     if json_obj is not None:
                         # Prune "empty" objects (e.g. {low: null, high: null}) that cause validation errors in strict schemas
                         json_obj = _prune_null_objects(json_obj)
                         
                         # Valid JSON extracted, validate with Pydantic
                         parsed = schema.model_validate(json_obj)
                         return {"raw": raw_msg, "parsed": parsed}
                     
                     # Fallback to default parser if extraction returned None (unlikely if valid)
                     parsed = parser.invoke(raw_msg)
                     return {"raw": raw_msg, "parsed": parsed}
                 except Exception:
                     # Return None for parsed to trigger LoggedRunner's fallback/error handling
                     return {"raw": raw_msg, "parsed": None}

            # Chain: specialized prompt -> raw model -> parser wrapper
            runner = RunnableLambda(prompt_augmentation) | self.model | RunnableLambda(parsing_step)

        else:
            # For other OpenAI-compatible (and fallback), pass as is
            runner = self.model.with_structured_output(schema, method=method, include_raw=True)

        # We need to wrap the runner's invoke to capture the log
        # The runner returns a Pydantic object (or dict), not AIMessage.
        # We'll log the serialized result.

        # Pass the original schema if it was a Pydantic class to allow reconstruction
        pydantic_class = schema if (isinstance(schema, type) and hasattr(schema, "model_validate")) else None

        return LoggedRunner(runner, self, pydantic_schema=pydantic_class)

    def _sanitize_schema(self, schema: dict, is_root: bool = True) -> dict:
        """Recursively remove 'additionalProperties' from schema for Vertex AI compatibility."""
        if not isinstance(schema, dict):
            return schema

        # Handle validation incompatible fields for Vertex AI
        schema.pop("additionalProperties", None)

        # Ensure 'title' exists at ROOT LEVEL ONLY (required by Claude on Vertex AI for tool/function calling)
        if is_root and "title" not in schema:
            desc = schema.get("description")
            if isinstance(desc, str) and desc:
                # Truncate to avoid limit but keep somewhat readable
                schema["title"] = desc[:20].replace(" ", "") + "_" + hashlib.md5(desc.encode()).hexdigest()[:6]
            else:
                # Generate a deterministic hash based on content to ensure consistency
                schema_str = json.dumps(schema, sort_keys=True)
                schema["title"] = "Schema_" + hashlib.md5(schema_str.encode()).hexdigest()[:8]

        # Handle 'anyOf' (usually Optional[T] -> [T, null])
        if "anyOf" in schema:
            options = schema.pop("anyOf")
            for opt in options:
                # Find the first non-null option
                if isinstance(opt, dict) and opt.get("type") != "null":
                    schema.update(opt)
                    break

        for key, value in schema.items():
            if isinstance(value, dict):
                # Nested schemas are not root
                self._sanitize_schema(value, is_root=False)
            elif isinstance(value, list):
                for item in value:
                    self._sanitize_schema(item, is_root=False)
        return schema

    def __getattr__(self, name: str) -> Any:
        return getattr(self.model, name)


def _make_model(config: ModelAdapterConfig) -> Any:
    provider = config.provider

    # Common kwargs
    kwargs = {
        "temperature": config.temperature,
        "max_tokens": config.max_tokens,
    }

    if config.frequency_penalty is not None:
        kwargs["frequency_penalty"] = config.frequency_penalty
    if config.presence_penalty is not None:
        kwargs["presence_penalty"] = config.presence_penalty

    if provider == "openai":
        # Pass "reasoning_effort" if specified (only for O1/GPT-5 models)
        if config.reasoning_effort and config.reasoning_effort != "none":
            kwargs["reasoning_effort"] = config.reasoning_effort

        return ChatOpenAI(
            model=config.model_name,
            api_key=os.getenv(config.api_key_env),
            **kwargs
        )

    if provider == "google_genai":
        project_id = os.getenv(config.project_id_env)
        location = "global" if config.requires_global_location else (config.location_override or os.getenv(config.location_env, "us-central1"))

        # Use explicit configuration for Vertex AI vs Google GenAI
        use_vertex = config.use_vertex_api

        # Pass thinking_level if specified
        extra_args = {}
        if config.thinking_level:
            extra_args["thinking_level"] = config.thinking_level

        return ChatGoogleGenerativeAI(
            model=config.model_name,
            project=project_id,
            location=location,
            vertexai=use_vertex,
            **kwargs,        # temp, max_tokens
            **extra_args
        )

    if provider == "vertex_openapi":
        # For models like Llama that use OpenAPI-compatible endpoints on Vertex AI
        # Global: https://aiplatform.googleapis.com/v1/projects/{PROJECT}/locations/global/endpoints/openapi
        # Regional: https://{REGION}-aiplatform.googleapis.com/v1/projects/{PROJECT}/locations/{REGION}/endpoints/openapi
        project_id = os.getenv(config.project_id_env)
        location = config.location_override or "global"

        # Get access token for authentication
        token = subprocess.check_output(["gcloud", "auth", "print-access-token"]).decode().strip()

        # Use region-specific hostname for non-global locations
        if location == "global":
            hostname = "aiplatform.googleapis.com"
        else:
            hostname = f"{location}-aiplatform.googleapis.com"

        base_url = f"https://{hostname}/v1/projects/{project_id}/locations/{location}/endpoints/openapi"

        return ChatOpenAI(
            model=config.model_name,
            base_url=base_url,
            api_key=token,  # Use GCP access token as API key
            **kwargs
        )

    if provider == "vertex_endpoint_openai":
        # For Customer-Managed Endpoints (vLLM/TGI) that expose OpenAI protocol
        # URL: https://{REGION}-aiplatform.googleapis.com/v1beta1/projects/{PROJECT}/locations/{REGION}/endpoints/{ENDPOINT_ID}
        project_id = os.getenv(config.project_id_env)
        location = os.getenv(config.location_env, "us-central1")
        if config.location_override:
            location = config.location_override

        endpoint_id = os.getenv(config.endpoint_id_env)
        if not endpoint_id:
            raise ValueError(f"Endpoint ID not found in env for {config.model_name} ({config.endpoint_id_env})")

        # Resolve Endpoint Hostname (Dedicated vs Shared)
        hostname = f"{location}-aiplatform.googleapis.com"
        try:
            aiplatform.init(project=project_id, location=location)
            ep = aiplatform.Endpoint(endpoint_id)

            # Accessing gca_resource triggers the API call to get details
            resource = ep.gca_resource

            if getattr(resource, "dedicated_endpoint_enabled", False):
                dedicated_dns = getattr(resource, "dedicated_endpoint_dns", None)
                if dedicated_dns:
                    hostname = dedicated_dns
                else:
                    # Should not happen if enabled
                    raise ValueError(f"Endpoint {endpoint_id} has dedicated_endpoint_enabled=True but no dedicated_endpoint_dns found.")

        except Exception as e:
            # If it was a ValueError we just raised, re-raise it
            if isinstance(e, ValueError):
                raise
            # Fallback to default shared hostname on connection/permission errors.
            pass

        # Get access token
        try:
            token = subprocess.check_output(["gcloud", "auth", "print-access-token"]).decode().strip()
        except Exception as e:
            raise RuntimeError(f"Failed to get gcloud token: {e}")

        base_url = f"https://{hostname}/v1beta1/projects/{project_id}/locations/{location}/endpoints/{endpoint_id}"

        return ChatOpenAI(
            model=config.model_name,
            base_url=base_url,
            api_key=token,
            **kwargs
        )

    if provider == "anthropic":
        # Direct Anthropic API
        # Handle thinking/reasoning params
        if config.budget_tokens > 0:
            kwargs["thinking"] = {
                 "type": "enabled",
                 "budget_tokens": config.budget_tokens
            }

        return ChatAnthropic(
            model=config.model_name,
            api_key=os.getenv(config.api_key_env),
            **kwargs 
        )

    if provider == "anthropic_vertex":
        project_id = os.getenv(config.project_id_env)
        location = "global" if config.requires_global_location else os.getenv(config.location_env, "us-central1")

        # Add thinking budget if specified
        if config.budget_tokens > 0:
            # Standard Anthropic / Vertex Anthropic structure
            if "model_kwargs" not in kwargs: kwargs["model_kwargs"] = {}
            kwargs["model_kwargs"]["thinking"] = {
                "type": "enabled",
                "budget_tokens": config.budget_tokens
            }

        return ChatAnthropicVertex(
            model_name=config.model_name,
            project=project_id,
            location=location,
            **kwargs
        )

    if provider == "vertexai":
        # Generic Vertex
        project_id = os.getenv(config.project_id_env)
        location = os.getenv(config.location_env, "us-central1")

        # Use explicit configuration for Vertex AI vs Google GenAI
        use_vertex = config.use_vertex_api

        extra_args = {}
        if config.thinking_level:
            extra_args["thinking_level"] = config.thinking_level

        return ChatGoogleGenerativeAI(
            model=config.model_name,
            project=project_id,
            location=location,
            vertexai=use_vertex,
            **kwargs,
            **extra_args
        )

    if provider == "huggingface_endpoint":
        # Hugging Face Inference Endpoint (vLLM / OpenAI Compatible)
        api_token = os.getenv(config.api_key_env)
        if not api_token:
            raise ValueError(f"API Token not found in env for {config.model_name} ({config.api_key_env})")
        
        # Ensure endpoint_url ends with /v1
        base_url = config.endpoint_url.rstrip("/")
        if not base_url.endswith("/v1"):
            base_url += "/v1"

        return ChatOpenAI(
            model=config.model_name,
            base_url=base_url,
            api_key=api_token,
            temperature=config.temperature,
            max_tokens=config.max_tokens,
            # Pass other kwargs if allowed by vLLM (frequency_penalty etc support varies)
        )

    raise ValueError(f"Unsupported provider: {provider}")


def create_model(model_key: str, agent_name: str = "") -> LoggedInvoker:
    """
    Factory function to create a model instance with logging.
    """
    if model_key not in SUPPORTED_MODELS:
        raise ValueError(f"Unknown model key: {model_key}")
    cfg = SUPPORTED_MODELS[model_key]

    # Pre-flight environment check (e.g. enforcing global location)
    if cfg.requires_global_location:
        os.environ["GOOGLE_CLOUD_LOCATION"] = "global"

    raw_model = _make_model(cfg)

    # Wrap model with auto-continuation logic
    continuation_model = ContinuationProxy(
        raw_model,
        max_continuations=cfg.max_continuations,
        agent_name=agent_name
    )

    return LoggedInvoker(continuation_model, cfg, agent_name=agent_name)
