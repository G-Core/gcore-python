# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .lb_session_persistence_type import LbSessionPersistenceType

__all__ = ["SessionPersistence"]


class SessionPersistence(BaseModel):
    cookie_name: Optional[str] = None
    """Should be set if app cookie or http cookie is used. Null otherwise."""

    persistence_granularity: Optional[str] = None
    """Subnet mask if `source_ip` is used. For UDP ports only, null otherwise."""

    persistence_timeout: Optional[int] = None
    """Session persistence timeout. For UDP ports only, null otherwise."""

    type: LbSessionPersistenceType
    """Session persistence type"""
