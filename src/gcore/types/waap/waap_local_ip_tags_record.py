# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["WaapLocalIPTagsRecord", "Domain"]


class Domain(BaseModel):
    id: int
    """The unique identifier for the domain"""

    name: str
    """The domain name"""


class WaapLocalIPTagsRecord(BaseModel):
    date: int
    """The timestamp of the last request from the IP to the domain"""

    domain: Domain

    global_tags: List[str]
    """The tags associated with the IP globally"""

    ip: str
    """The IP address"""

    local_tags: List[str]
    """The tags associated with the IP in the context of the domain"""
