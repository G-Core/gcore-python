# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AppUpdateParams", "Secrets", "Stores"]


class AppUpdateParams(TypedDict, total=False):
    binary: int
    """ID of the WebAssembly binary to deploy"""

    comment: str
    """Optional human-readable description of the application's purpose"""

    debug: bool
    """Enable verbose debug logging for 30 minutes.

    Automatically expires to prevent performance impact.
    """

    env: Dict[str, str]
    """Environment variables"""

    log: Optional[Literal["kafka", "none"]]
    """Logging channel.

    Use 'kafka' to enable log collection (queryable via API), or 'none' to disable
    logging.
    """

    name: str
    """Unique application name (alphanumeric, hyphens allowed)"""

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
    5 - suspended
    """

    stores: Dict[str, Stores]
    """Application edge stores"""

    template: int
    """Template ID"""


class Secrets(TypedDict, total=False):
    """Application secret short description"""

    id: Required[int]
    """The unique identifier of the secret."""


class Stores(TypedDict, total=False):
    """Application stores"""

    id: Required[int]
    """The identifier of the store"""
