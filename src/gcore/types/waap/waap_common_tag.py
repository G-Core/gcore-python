# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["WaapCommonTag"]


class WaapCommonTag(BaseModel):
    description: str
    """Tag description information"""

    display_name: str
    """The tag's display name"""

    tag: str
    """Tag name"""
