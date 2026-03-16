# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "ClusterActionParams",
    "StartGPUClusterSerializer",
    "StopGPUClusterSerializer",
    "SoftRebootGPUClusterSerializer",
    "HardRebootGPUClusterSerializer",
    "ResizeVirtualGPUClusterSerializer",
]


class StartGPUClusterSerializer(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    action: Required[Literal["start"]]
    """Action name"""


class StopGPUClusterSerializer(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    action: Required[Literal["stop"]]
    """Action name"""


class SoftRebootGPUClusterSerializer(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    action: Required[Literal["soft_reboot"]]
    """Action name"""


class HardRebootGPUClusterSerializer(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    action: Required[Literal["hard_reboot"]]
    """Action name"""


class ResizeVirtualGPUClusterSerializer(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    action: Required[Literal["resize"]]
    """Action name"""

    servers_count: Required[int]
    """Requested servers count"""


ClusterActionParams: TypeAlias = Union[
    StartGPUClusterSerializer,
    StopGPUClusterSerializer,
    SoftRebootGPUClusterSerializer,
    HardRebootGPUClusterSerializer,
    ResizeVirtualGPUClusterSerializer,
]
