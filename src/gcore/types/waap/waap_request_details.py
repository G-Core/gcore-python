# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel
from .waap_common_tag import WaapCommonTag
from .waap_network_details import WaapNetworkDetails
from .waap_user_agent_details import WaapUserAgentDetails
from .waap_pattern_matched_tag import WaapPatternMatchedTag

__all__ = ["WaapRequestDetails"]


class WaapRequestDetails(BaseModel):
    id: str
    """Request ID"""

    action: str
    """Request action"""

    common_tags: List[WaapCommonTag]
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

    network: WaapNetworkDetails
    """Network details"""

    path: str
    """Request path"""

    pattern_matched_tags: List[WaapPatternMatchedTag]
    """List of shield tags"""

    query_string: str
    """The query string of the request"""

    reference_id: str
    """Reference ID to identify user sanction"""

    request_headers: object
    """HTTP request headers"""

    request_time: str
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

    user_agent: WaapUserAgentDetails
    """User agent details"""
