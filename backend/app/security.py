# security.py

BLOCKED_PATTERNS = [
    "ignore previous instructions",
    "ignore all previous instructions",
    "system prompt",
    "developer message",
    "api key",
    "reveal your prompt",
    "forget previous instructions",
    "bypass security",
    "pretend to be",
    "act as another ai"
]

def check_prompt(prompt: str):

    prompt = prompt.lower()

    for pattern in BLOCKED_PATTERNS:
        if pattern in prompt:
            return False, pattern

    return True, None