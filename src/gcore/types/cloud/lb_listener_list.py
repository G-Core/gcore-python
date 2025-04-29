# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .lb_listener import LbListener

__all__ = ["LbListenerList"]


class LbListenerList(BaseModel):
    count: int
    """
    '#/components/schemas/LbListenerSerializerList/properties/count'
    "$.components.schemas.LbListenerSerializerList.properties.count"
    """

    results: List[LbListener]
    """
    '#/components/schemas/LbListenerSerializerList/properties/results'
    "$.components.schemas.LbListenerSerializerList.properties.results"
    """
