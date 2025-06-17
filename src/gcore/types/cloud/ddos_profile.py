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

    protocols: List[str]


class DDOSProfile(BaseModel):
    id: int
    """DDoS protection profile ID"""

    profile_template: Optional[DDOSProfileTemplate] = None
    """Template data"""

    fields: Optional[List[DDOSProfileField]] = None

    options: Optional[DDOSProfileOptionList] = None

    profile_template_description: Optional[str] = None
    """DDoS profile template description"""

    protocols: Optional[List[Protocol]] = None
    """List of protocols"""

    site: Optional[str] = None

    status: Optional[DDOSProfileStatus] = None
