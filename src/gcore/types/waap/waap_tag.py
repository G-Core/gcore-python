# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["WaapTag"]


class WaapTag(BaseModel):
    description: str
    """A tag's human readable description"""

    name: str
    """The name of a tag that should be used in a WAAP rule condition"""

    readable_name: str
    """The display name of the tag"""
