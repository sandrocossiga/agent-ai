"""Guard utilities for input sanitization.

This module contains helper functions for cleaning and validating
user inputs before they are processed by the agent. Proper
sanitization is essential to defend against prompt injection and
other attacks in agentic systems.
"""
import re
from typing import Optional


def sanitize(text: Optional[str]) -> str:
    """Sanitize incoming user text.

    This function removes potentially dangerous patterns such as
    newline characters, certain special tokens, and control
    sequences. It also collapses multiple whitespace characters
    into a single space.

    Args:
        text: The raw input string to sanitize. If `None` is
            provided, an empty string is returned.

    Returns:
        A sanitized string safe for processing.
    """
    if not text:
        return ""

    # Remove common prompt injection patterns
    injection_patterns = [
        r"\n",  # newline characters
        r"<\|endof.*?\|>",  # special stop sequences
        r"(?i)system:\s*",  # system role instructions
        r"(?i)assistant:\s*",
    ]
    cleaned = text
    for pattern in injection_patterns:
        cleaned = re.sub(pattern, " ", cleaned)

    # Collapse multiple whitespace into a single space
    cleaned = re.sub(r"\s+", " ", cleaned).strip()

    # Truncate input to a reasonable length to avoid runaway prompts
    max_length = 1024
    if len(cleaned) > max_length:
        cleaned = cleaned[:max_length]

    return cleaned
