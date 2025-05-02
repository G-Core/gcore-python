# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["AccessRule"]


class AccessRule(BaseModel):
    id: str
    """Access Rule ID"""

    access_level: Literal["ro", "rw"]
    """Access mode"""

    access_to: str
    """Source IP or network"""

    state: Literal["active", "applying", "denying", "error", "new", "queued_to_apply", "queued_to_deny"]
    """Access Rule state"""
