# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["QuotaItem"]


class QuotaItem(BaseModel):
    allowed: int
    """The maximum allowed number of this resource"""

    current: int
    """The current number of this resource"""
