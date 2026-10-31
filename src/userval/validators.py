"""Username validation helpers."""

MAX_LENGTH = 32


def validate_username(username):
    """Return the cleaned username or raise ValueError if it is invalid.

    Rules:
    - must be a string
    - must not be empty or whitespace-only
    - surrounding whitespace is stripped
    - must be at most MAX_LENGTH characters
    """
    if username is None:
        raise ValueError("username is required")
    if not isinstance(username, str):
        raise ValueError("username must be a string")
    cleaned = username.strip()
    if not cleaned:
        raise ValueError("username must not be empty")
    if len(cleaned) > MAX_LENGTH:
        raise ValueError("username too long")
    return cleaned
