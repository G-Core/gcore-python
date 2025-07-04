# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["UserInvite"]


class UserInvite(BaseModel):
    status: Optional[str] = None
    """Status of the invitation."""

    user_id: Optional[int] = None
    """Invited user ID."""
