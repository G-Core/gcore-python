# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["WaapIPInfo", "Whois"]


class Whois(BaseModel):
    abuse_mail: Optional[str] = None
    """The abuse mail"""

    cidr: Optional[int] = None
    """The CIDR"""

    country: Optional[str] = None
    """The country"""

    net_description: Optional[str] = None
    """The network description"""

    net_name: Optional[str] = None
    """The network name"""

    net_range: Optional[str] = None
    """The network range"""

    net_type: Optional[str] = None
    """The network type"""

    org_id: Optional[str] = None
    """The organization ID"""

    org_name: Optional[str] = None
    """The organization name"""

    owner_type: Optional[str] = None
    """The owner type"""

    rir: Optional[str] = None
    """The RIR"""

    state: Optional[str] = None
    """The state"""


class WaapIPInfo(BaseModel):
    risk_score: Literal["NO_RISK", "LOW", "MEDIUM", "HIGH", "EXTREME", "NOT_ENOUGH_DATA"]
    """The risk score of the IP address"""

    tags: List[str]
    """The tags associated with the IP address that affect the risk score"""

    whois: Whois
    """The WHOIS information for the IP address"""
