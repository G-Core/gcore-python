# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AppUpdateParams", "Secrets"]


class AppUpdateParams(TypedDict, total=False):
    binary: int
    """Binary ID"""

    comment: str
    """App description"""

    debug: bool
    """Switch on logging for 30 minutes (switched off by default)"""

    env: Dict[str, str]
    """Environment variables"""

    log: Optional[Literal["kafka", "none"]]
    """Logging channel (by default - kafka, which allows exploring logs with API)"""

    name: str
    """App name"""

    rsp_headers: Dict[str, str]
    """Extra headers to add to the response"""

    secrets: Dict[str, Secrets]
    """Application secrets"""

    status: int
    """
    Status code:
    0 - draft (inactive)
    1 - enabled
    2 - disabled
    3 - hourly call limit exceeded
    4 - daily call limit exceeded
    5 - suspended
    """

    stores: Dict[str, int]
    """KV stores for the app"""

    template: int
    """Template ID"""


class Secrets(TypedDict, total=False):
    """Application secret short description"""

    id: Required[int]
    """The unique identifier of the secret."""
