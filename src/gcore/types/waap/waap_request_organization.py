# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["WaapRequestOrganization"]


class WaapRequestOrganization(BaseModel):
    name: str
    """Organization name"""

    subnet: str
    """Network range"""
