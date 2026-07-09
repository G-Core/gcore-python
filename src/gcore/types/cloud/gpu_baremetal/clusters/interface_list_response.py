# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import TypeAlias

from ....._models import BaseModel
from ...network_interface import NetworkInterface
from ...instance_interface import InstanceInterface

__all__ = ["InterfaceListResponse", "Result"]

Result: TypeAlias = Union[NetworkInterface, InstanceInterface]


class InterfaceListResponse(BaseModel):
    count: int
    """Number of objects"""

    results: List[Result]
    """Objects"""
