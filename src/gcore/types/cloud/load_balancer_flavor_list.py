# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import TypeAlias

from ..._models import BaseModel
from .load_balancer_flavor_detail import LoadBalancerFlavorDetail

__all__ = ["LoadBalancerFlavorList", "Result", "ResultLbFlavorSerializer"]


class ResultLbFlavorSerializer(BaseModel):
    flavor_id: str
    """Flavor ID is the same as name"""

    flavor_name: str
    """Flavor name"""

    ram: int
    """RAM size in MiB"""

    vcpus: int
    """Virtual CPU count. For bare metal flavors, it's a physical CPU count"""


Result: TypeAlias = Union[ResultLbFlavorSerializer, LoadBalancerFlavorDetail]


class LoadBalancerFlavorList(BaseModel):
    count: int
    """Number of objects"""

    results: List[Result]
    """Objects"""
