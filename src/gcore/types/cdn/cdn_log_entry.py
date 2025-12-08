# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["CdnLogEntry", "Data", "Meta"]


class Data(BaseModel):
    cache_status: Optional[str] = None
    """Cache status: HIT, MISS, etc."""

    client_ip: Optional[str] = None
    """IP address from that the request was received."""

    cname: Optional[str] = None
    """CDN resource custom domain."""

    datacenter: Optional[str] = None
    """Data center where the request was processed."""

    method: Optional[str] = None
    """HTTP method used in the request."""

    path: Optional[str] = None
    """Path requested."""

    referer: Optional[str] = None
    """Value of 'Referer' header."""

    resource_id: Optional[int] = None
    """CDN resource ID."""

    sent_http_content_type: Optional[str] = None
    """
    Value of the Content-Type HTTP header, indicating the MIME type of the resource
    being transmitted.
    """

    size: Optional[int] = None
    """Response size in bytes."""

    status: Optional[int] = None
    """HTTP status code."""

    tcpinfo_rtt: Optional[int] = None
    """
    Time required to transmit a complete TCP segment: from the first bit to the
    last.
    """

    timestamp: Optional[int] = None
    """Log timestamp."""

    user_agent: Optional[str] = None
    """Value of 'User-Agent' header."""


class Meta(BaseModel):
    """Contains meta-information."""

    count: Optional[int] = None
    """Total number of records which match given parameters."""


class CdnLogEntry(BaseModel):
    data: Optional[List[Data]] = None
    """Contains requested logs."""

    meta: Optional[Meta] = None
    """Contains meta-information."""
