# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["WaapRequestDetails", "CommonTag", "Network", "NetworkOrganization", "PatternMatchedTag", "UserAgent"]


class CommonTag(BaseModel):
    """Common tag details"""

    description: str
    """Tag description information"""

    display_name: str
    """The tag's display name"""

    tag: str
    """Tag name"""


class NetworkOrganization(BaseModel):
    """Organization details"""

    name: str
    """Organization name"""

    subnet: str
    """Network range"""


class Network(BaseModel):
    """Network details"""

    client_ip: str
    """Client IP"""

    country: str
    """Country code"""

    organization: NetworkOrganization
    """Organization details"""


class PatternMatchedTag(BaseModel):
    """Pattern matched tag details"""

    description: str
    """Tag description information"""

    display_name: str
    """The tag's display name"""

    execution_phase: str
    """
    The phase in which the tag was triggered: access -> Request, `header_filter` ->
    `response_header`, `body_filter` -> `response_body`
    """

    field: str
    """The entity to which the variable that triggered the tag belong to.

    For example: `request_headers`, uri, cookies etc.
    """

    field_name: str
    """The name of the variable which holds the value that triggered the tag"""

    pattern_name: str
    """The name of the detected regexp pattern"""

    pattern_value: str
    """The pattern which triggered the tag"""

    tag: str
    """Tag name"""


class UserAgent(BaseModel):
    """User agent"""

    base_browser: str
    """User agent browser"""

    base_browser_version: str
    """User agent browser version"""

    client: str
    """Client from User agent header"""

    client_type: str
    """User agent client type"""

    client_version: str
    """User agent client version"""

    cpu: str
    """User agent cpu"""

    device: str
    """User agent device"""

    device_type: str
    """User agent device type"""

    full_string: str
    """User agent"""

    os: str
    """User agent os"""

    rendering_engine: str
    """User agent engine"""


class WaapRequestDetails(BaseModel):
    """Request's details used when displaying a single request."""

    id: str
    """Request ID"""

    action: str
    """Request action"""

    common_tags: List[CommonTag]
    """List of common tags"""

    content_type: str
    """Content type of request"""

    domain: str
    """Domain name"""

    http_status_code: int
    """Status code for http request"""

    http_version: str
    """HTTP version of request"""

    incident_id: str
    """ID of challenge that was generated"""

    method: str
    """Request method"""

    network: Network
    """Network details"""

    path: str
    """Request path"""

    pattern_matched_tags: List[PatternMatchedTag]
    """List of shield tags"""

    query_string: str
    """The query string of the request"""

    reference_id: str
    """Reference ID to identify user sanction"""

    request_headers: Dict[str, object]
    """HTTP request headers"""

    request_time: datetime
    """The time of the request"""

    request_type: str
    """The type of the request that generated an event"""

    requested_domain: str
    """The real domain name"""

    response_time: str
    """Time took to process all request"""

    result: Literal["passed", "blocked", "suppressed", ""]
    """The result of a request"""

    rule_id: str
    """ID of the triggered rule"""

    rule_name: str
    """Name of the triggered rule"""

    scheme: str
    """The HTTP scheme of the request that generated an event"""

    session_request_count: str
    """The number requests in session"""

    traffic_types: List[str]
    """List of traffic types"""

    user_agent: UserAgent
    """User agent"""
