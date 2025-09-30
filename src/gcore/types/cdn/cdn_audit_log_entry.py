# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["CdnAuditLogEntry", "Action"]


class Action(BaseModel):
    action_type: Optional[str] = None
    """Type of change.

    Possible values:

    - **D** - Object is deleted.
    - **C** - Object is created.
    - **U** - Object is updated.
    """

    state_after_request: Optional[object] = None
    """JSON representation of object after the request."""

    state_before_request: Optional[object] = None
    """JSON representation of object before the request."""


class CdnAuditLogEntry(BaseModel):
    id: Optional[int] = None
    """Activity logs record ID."""

    actions: Optional[List[Action]] = None
    """State of a requested object before and after the request."""

    client_id: Optional[int] = None
    """ID of the client who made the request."""

    data: Optional[object] = None
    """Request body."""

    host: Optional[str] = None
    """Host from which the request was made."""

    method: Optional[str] = None
    """Request HTTP method."""

    path: Optional[str] = None
    """Request URL."""

    query_params: Optional[str] = None
    """Request parameters."""

    remote_ip_address: Optional[str] = None
    """IP address from which the request was made."""

    requested_at: Optional[str] = None
    """Date and time when the request was made."""

    status_code: Optional[int] = None
    """Status code that is returned in the response."""

    token_id: Optional[int] = None
    """Permanent API token ID with which the request was made."""

    user_id: Optional[int] = None
    """ID of the user who made the request."""
