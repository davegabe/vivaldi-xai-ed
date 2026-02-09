import re
import json
from typing import Union, Optional, Match, Callable
import json_repair

def _escape_unescaped_backslashes(text: str) -> str:
    """
    Double all backslashes not followed by a valid escape (n, t, r, b, f, a, ", ', \\, /, u, U) and not already escaped.
    """
    # Only double a single backslash not followed by a valid escape
    # Do not double if already escaped (i.e., \\)
    # Use negative lookbehind to avoid already escaped
    valid_escapes = "ntbrfa\"'\\/uU"
    pattern = r"(?<!\\)\\(?![{}])".format(valid_escapes)
    return re.sub(pattern, r"\\\\", text)


# --- Unicode escape fixer ---
def _fix_incomplete_unicode_escapes(text: str) -> str:
    r"""
    Pads incomplete unicode escapes (e.g., \\uF, \\uFF) to valid 4-digit escapes (\\u0F00, \\uFF00) and decodes to unicode if possible.
    """
    def pad_unicode(match: Match[str]) -> str:
        """Pad incomplete unicode escape sequence to valid 4-digit hex.
        
        Args:
            match: Regex match object containing captured unicode digits

        Returns:
            Converted unicode character or padded escape sequence
        """
        digits = match.group(1)
        if len(digits) == 1:
            padded = digits.rjust(2, '0') + '00'  # e.g., F -> 0F00
        elif len(digits) == 2:
            padded = digits + '00'  # e.g., FF -> FF00
        elif len(digits) == 3:
            padded = digits + '0'   # e.g., FFF -> FFF0
        else:
            padded = digits
        try:
            codepoint = int(padded, 16)
            char = chr(codepoint)
            return char
        except Exception:
            return f"\\u{padded}"
    # Replace \u followed by 1-3 hex digits not followed by another hex digit
    return re.sub(r"\\u([0-9a-fA-F]{1,3})(?![0-9a-fA-F])", pad_unicode, text)



def extract_json_from_text(text: str, fix_callback: Optional[Callable[[str], str]] = None) -> Optional[Union[dict, list]]:
    """
    Extract and parse JSON from text that may contain markdown or other content,
    using the json-repair library. Applies unicode and backslash pre-processing.
    """
    # Pre-process: fix incomplete unicode escapes
    text = _fix_incomplete_unicode_escapes(text)
    # Pre-process: escape unescaped backslashes (for other cases)
    text = _escape_unescaped_backslashes(text)

    repair_exceptions = (json.JSONDecodeError, TypeError, ValueError, AttributeError, IndexError, KeyError)

    # Strategy 1: Extract JSON from markdown code blocks
    code_block_match = re.search(
        r"```(?:json)?\s*([\s\S]*?)\s*```", text, re.DOTALL)
    if code_block_match:
        json_str_candidate = code_block_match.group(1).strip()
        if json_str_candidate:
            try:
                result = json_repair.repair_json(json_str_candidate, return_objects=True)
                if isinstance(result, tuple):
                    result = result[0]
                if isinstance(result, (dict, list)):
                    return result
                return None
            except repair_exceptions:
                pass

    # Strategy 2: Try to parse the entire text as JSON (after stripping)
    stripped_text = text.strip()
    if stripped_text.startswith(("{", "[")) and stripped_text.endswith(("}", "]")):
        try:
            result = json_repair.repair_json(stripped_text, return_objects=True)
            if isinstance(result, tuple):
                result = result[0]
            if isinstance(result, (dict, list)):
                return result
            return None
        except repair_exceptions:
            pass

    # Strategy 3: Look for embedded JSON-like structures using regex
    potential_json_matches = []
    # Try to extract the largest JSON object/array from the start
    for start in [m.start() for m in re.finditer(r'[\[{]', text)]:
        for end in range(len(text), start + 1, -1):
            candidate = text[start:end].strip()
            if len(candidate) < 2:
                continue
            if not ((candidate.startswith('{') and candidate.count('{') >= candidate.count('}')) or (candidate.startswith('[') and candidate.count('[') >= candidate.count(']'))):
                continue
            # Try to repair and parse
            try:
                repaired_obj = json_repair.repair_json(candidate, return_objects=True)
                if isinstance(repaired_obj, tuple):
                    repaired_obj = repaired_obj[0]
                if isinstance(repaired_obj, (dict, list)):
                    return repaired_obj
            except repair_exceptions:
                continue
            except Exception:
                continue
                
    # Fallback to previous regex-based extraction for other cases
    for pattern_str in [
        r"(\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\})",
        r"(\[[^\[\]]*(?:\[[^\[\]]*\][^\[\]]*)*\])",
        r"(\{[\s\S]*?\})(?=\s*(?:$|\n\n|```|[,\}\]]))",
        r"(\[[\s\S]*?\])(?=\s*(?:$|\n\n|```|[,\}\]]))"
    ]:
        try:
            for match in re.finditer(pattern_str, text):
                potential_json_matches.append(match.group(1))
        except re.error:
            pass

    if not potential_json_matches:
        for pattern_str in [r"(\{[\s\S]*?\})", r"(\[[\s\S]*?\])"]:
            try:
                for match in re.finditer(pattern_str, text):
                    potential_json_matches.append(match.group(1))
            except re.error:
                pass

    potential_json_matches = list(set(potential_json_matches))
    potential_json_matches.sort(key=len, reverse=True)

    for candidate in potential_json_matches:
        candidate_stripped = candidate.strip()
        if len(candidate_stripped) < 2 or \
           not ((candidate_stripped.startswith("{") and candidate_stripped.endswith("}")) or \
                (candidate_stripped.startswith("[") and candidate_stripped.endswith("]"))):
            if candidate_stripped not in ["{}", "[]"]:
                continue
        try:
            repaired_obj = json_repair.repair_json(candidate_stripped, return_objects=True)
            if isinstance(repaired_obj, tuple):
                repaired_obj = repaired_obj[0]
            if isinstance(repaired_obj, (dict, list)):
                return repaired_obj
            return None
        except repair_exceptions:
            continue
        except Exception:
            continue

    # Final fallback: use provided fix_callback (e.g., LLM)
    if fix_callback:
        try:
            fixed_text = fix_callback(text)
            if fixed_text and isinstance(fixed_text, str):
                # Recurse without callback to prevent infinite loops
                return extract_json_from_text(fixed_text, fix_callback=None)
        except Exception:
            pass

    return None
