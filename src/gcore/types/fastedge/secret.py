# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["Secret", "SecretSlot"]


class SecretSlot(BaseModel):
    slot: int
    """Secret slot ID."""

    checksum: Optional[str] = None
    """A checksum of the secret value for integrity verification."""


class Secret(BaseModel):
    app_count: Optional[int] = None
    """The number of applications that use this secret."""

    comment: Optional[str] = None
    """A description or comment about the secret."""

    name: Optional[str] = None
    """The unique name of the secret."""

    secret_slots: Optional[List[SecretSlot]] = None
    """A list of secret slots associated with this secret."""
