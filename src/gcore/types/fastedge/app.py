# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["App", "Secrets"]


class Secrets(BaseModel):
    id: int
    """The unique identifier of the secret."""

    comment: Optional[str] = None
    """A description or comment about the secret."""

    name: Optional[str] = None
    """The unique name of the secret."""


class App(BaseModel):
    api_type: Optional[str] = None
    """Wasm API type"""

    binary: Optional[int] = None
    """Binary ID"""

    comment: Optional[str] = None
    """App description"""

    debug_until: Optional[datetime] = None
    """When debugging finishes"""

    env: Optional[Dict[str, str]] = None
    """Environment variables"""

    log: Optional[Literal["kafka", "none"]] = None
    """Logging channel (by default - kafka, which allows exploring logs with API)"""

    name: Optional[str] = None
    """App name"""

    networks: Optional[List[str]] = None
    """Networks"""

    plan: Optional[str] = None
    """Plan name"""

    plan_id: Optional[int] = None
    """Plan ID"""

    rsp_headers: Optional[Dict[str, str]] = None
    """Extra headers to add to the response"""

    secrets: Optional[Dict[str, Secrets]] = None
    """Application secrets"""

    status: Optional[int] = None
    """
    Status code:
    0 - draft (inactive)
    1 - enabled
    2 - disabled
    3 - hourly call limit exceeded
    4 - daily call limit exceeded
    5 - suspended
    """

    stores: Optional[Dict[str, int]] = None
    """KV stores for the app"""

    template: Optional[int] = None
    """Template ID"""

    template_name: Optional[str] = None
    """Template name"""

    url: Optional[str] = None
    """App URL"""
