# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["WaapRequestSummary"]


class WaapRequestSummary(BaseModel):
    """Request summary used when displaying a list of requests"""

    id: str
    """Request's unique id"""

    action: str
    """Action of the triggered rule"""

    client_ip: str
    """Client's IP address."""

    country: str
    """Country code"""

    decision: Literal["passed", "allowed", "monitored", "blocked", ""]
    """The decision made for processing the request through the WAAP."""

    domain: str
    """Domain name"""

    domain_id: int
    """Domain ID"""

    method: str
    """HTTP method"""

    optional_action: Literal["captcha", "challenge", ""]
    """An optional action that may be applied in addition to the primary decision."""

    organization: str
    """Organization"""

    path: str
    """Request path"""

    reference_id: str
    """The reference ID to a sanction that was given to a user."""

    request_time: int
    """The UNIX timestamp in ms of the date a set of traffic counters was recorded"""

    result: Literal["passed", "blocked", "suppressed", ""]

    rule_id: str
    """The ID of the triggered rule."""

    rule_name: str
    """Name of the triggered rule"""

    status_code: int
    """Status code for http request"""

    traffic_types: str
    """Comma separated list of traffic types."""

    user_agent: str
    """User agent"""

    user_agent_client: str
    """Client from parsed User agent header"""
