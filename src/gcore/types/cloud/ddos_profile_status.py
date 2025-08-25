# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["DDOSProfileStatus"]


class DDOSProfileStatus(BaseModel):
    error_description: str
    """Detailed error message describing any issues with the profile operation"""

    status: str
    """Current operational status of the DDoS protection profile"""
