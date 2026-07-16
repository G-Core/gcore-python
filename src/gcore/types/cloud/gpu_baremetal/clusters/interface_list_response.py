# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from ...network_interface import NetworkInterface
from ...instance_interface import InstanceInterface

__all__ = ["InterfaceListResponse"]

InterfaceListResponse: TypeAlias = Union[NetworkInterface, InstanceInterface]
