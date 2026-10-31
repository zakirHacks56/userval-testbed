"""userval: tiny username validation package (test bed for the OSS agent)."""

from .validators import MAX_LENGTH, validate_username

__all__ = ["MAX_LENGTH", "validate_username"]
