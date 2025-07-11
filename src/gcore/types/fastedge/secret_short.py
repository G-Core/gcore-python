# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SecretShort"]


class SecretShort(BaseModel):
    name: str
    """The unique name of the secret."""

    id: Optional[int] = None
    """The unique identifier of the secret."""

    app_count: Optional[int] = None
    """The number of applications that use this secret."""

    comment: Optional[str] = None
    """A description or comment about the secret."""
