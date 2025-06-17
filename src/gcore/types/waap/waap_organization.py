# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["WaapOrganization"]


class WaapOrganization(BaseModel):
    id: int
    """The ID of an organization"""

    name: str
    """The name of an organization"""
