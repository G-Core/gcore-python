# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

from ...._types import SequenceNotStr
from ..price_port_spec_param import PricePortSpecParam
from ..price_volume_spec_param import PriceVolumeSpecParam
from ..price_port_reference_param import PricePortReferenceParam
from ..price_volume_reference_param import PriceVolumeReferenceParam

__all__ = [
    "InstancePreviewParams",
    "InstancePricePreviewReferenceBodySerializer",
    "InstancePricePreviewReferenceBodySerializerInterface",
    "InstancePricePreviewWorkflowBodySerializer",
    "InstancePricePreviewWorkflowBodySerializerBootVolume",
    "InstancePricePreviewWorkflowBodySerializerDataVolume",
    "InstancePricePreviewWorkflowBodySerializerInterface",
]


class InstancePricePreviewReferenceBodySerializer(TypedDict, total=False):
    project_id: int
    """Project ID."""

    flavor_name: Required[str]
    """Flavor of the server."""

    region_id: Required[int]
    """Region of the server."""

    boot_volume_id: str
    """Existing boot volume. Omit it to price the server without a boot volume."""

    data_volume_ids: SequenceNotStr[str]
    """Existing data volumes."""

    interfaces: Iterable[InstancePricePreviewReferenceBodySerializerInterface]
    """Ports in NIC order.

    An entry with `port_id` is an existing port, any other entry is a new one. Omit
    it to price the server without ports.
    """


InstancePricePreviewReferenceBodySerializerInterface: TypeAlias = Union[PricePortReferenceParam, PricePortSpecParam]


class InstancePricePreviewWorkflowBodySerializer(TypedDict, total=False):
    project_id: int
    """Project ID."""

    flavor_name: Required[str]
    """Flavor of the server."""

    region_id: Required[int]
    """Region of the server."""

    boot_volume: InstancePricePreviewWorkflowBodySerializerBootVolume
    """An entry with `volume_id` is an existing volume, any other entry is a new one.

    Omit it to price the server without a boot volume.
    """

    data_volumes: Iterable[InstancePricePreviewWorkflowBodySerializerDataVolume]
    """An entry with `volume_id` is an existing volume, any other entry is a new one."""

    interfaces: Iterable[InstancePricePreviewWorkflowBodySerializerInterface]
    """Ports in NIC order.

    An entry with `port_id` is an existing port, any other entry is a new one. Omit
    it to price the server without ports.
    """


InstancePricePreviewWorkflowBodySerializerBootVolume: TypeAlias = Union[PriceVolumeReferenceParam, PriceVolumeSpecParam]

InstancePricePreviewWorkflowBodySerializerDataVolume: TypeAlias = Union[PriceVolumeReferenceParam, PriceVolumeSpecParam]

InstancePricePreviewWorkflowBodySerializerInterface: TypeAlias = Union[PricePortReferenceParam, PricePortSpecParam]

InstancePreviewParams: TypeAlias = Union[
    InstancePricePreviewReferenceBodySerializer, InstancePricePreviewWorkflowBodySerializer
]
