# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional

from ..._models import BaseModel

__all__ = ["AliasDeleteMultipleResponse", "Removed"]


class Removed(BaseModel):
    id: Optional[int] = None

    cname: Optional[str] = None


class AliasDeleteMultipleResponse(BaseModel):
    not_found: Optional[List[Union[int, str]]] = None
    """Requested IDs or hostnames that did not match an alias."""

    removed: Optional[List[Removed]] = None
    """Aliases deleted by this request."""
