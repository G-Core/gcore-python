# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .ddos_profile_field import DDOSProfileField
from .ddos_profile_status import DDOSProfileStatus
from .ddos_profile_template import DDOSProfileTemplate
from .ddos_profile_option_list import DDOSProfileOptionList

__all__ = ["DDOSProfile", "Protocol"]


class Protocol(BaseModel):
    port: str
    """Network port number for which protocols are configured"""

    protocols: List[str]
    """List of network protocols enabled on the specified port"""


class DDOSProfile(BaseModel):
    id: int
    """Unique identifier for the DDoS protection profile"""

    fields: List[DDOSProfileField]
    """List of configured field values for the protection profile"""

    options: DDOSProfileOptionList
    """Configuration options controlling profile activation and BGP routing"""

    profile_template: Optional[DDOSProfileTemplate] = None
    """Complete template configuration data used for this profile"""

    profile_template_description: Optional[str] = None
    """Detailed description of the protection template used for this profile"""

    protocols: Optional[List[Protocol]] = None
    """List of network protocols and ports configured for protection"""

    site: Optional[str] = None
    """Geographic site identifier where the protection is deployed"""

    status: Optional[DDOSProfileStatus] = None
    """Current operational status and any error information for the profile"""
