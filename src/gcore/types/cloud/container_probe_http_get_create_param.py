# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["ContainerProbeHTTPGetCreateParam"]


class ContainerProbeHTTPGetCreateParam(TypedDict, total=False):
    port: Required[int]
    """Port number the probe should connect to."""

    headers: Dict[str, str]
    """HTTP headers to be sent with the request."""

    host: Optional[str]
    """Host name to send HTTP request to."""

    path: str
    """The endpoint to send the HTTP request to."""

    schema: str
    """Schema to use for the HTTP request."""
