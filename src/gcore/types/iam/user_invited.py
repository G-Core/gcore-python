# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["UserInvited"]


class UserInvited(BaseModel):
    status: str
    """Status of the invitation."""

    user_id: int
    """Invited user ID."""
