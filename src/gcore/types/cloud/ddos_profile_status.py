# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["DDOSProfileStatus"]


class DDOSProfileStatus(BaseModel):
    error_description: str
    """Description of the error, if it exists"""

    status: str
    """Profile status"""
