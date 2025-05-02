# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["Tag"]


class Tag(BaseModel):
    key: str
    """Tag key. The maximum size for a key is 255 bytes."""

    read_only: bool
    """If true, the tag is read-only and cannot be modified by the user"""

    value: str
    """Tag value. The maximum size for a value is 1024 bytes."""
