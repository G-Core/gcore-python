# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "FileShareCreateParams",
    "CreateStandardFileShareSerializer",
    "CreateStandardFileShareSerializerNetwork",
    "CreateStandardFileShareSerializerAccess",
    "CreateVastFileShareSerializer",
]


class CreateStandardFileShareSerializer(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    name: Required[str]
    """File share name"""

    network: Required[CreateStandardFileShareSerializerNetwork]
    """File share network configuration"""

    protocol: Required[Literal["NFS"]]
    """File share protocol"""

    size: Required[int]
    """File share size"""

    access: Iterable[CreateStandardFileShareSerializerAccess]
    """Access Rules"""

    tags: Dict[str, str]
    """Key-value tags to associate with the resource.

    A tag is a key-value pair that can be associated with a resource, enabling
    efficient filtering and grouping for better organization and management. Some
    tags are read-only and cannot be modified by the user. Tags are also integrated
    with cost reports, allowing cost data to be filtered based on tag keys or
    values.
    """

    volume_type: Literal["default_share_type"]
    """File share volume type"""


class CreateStandardFileShareSerializerNetwork(TypedDict, total=False):
    network_id: Required[str]
    """Network ID."""

    subnet_id: str
    """Subnetwork ID.

    If the subnet is not selected, it will be selected automatically.
    """


class CreateStandardFileShareSerializerAccess(TypedDict, total=False):
    access_mode: Required[Literal["ro", "rw"]]
    """Access mode"""

    ip_address: Required[str]
    """Source IP or network"""


class CreateVastFileShareSerializer(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    name: Required[str]
    """File share name"""

    protocol: Required[Literal["NFS"]]
    """File share protocol"""

    size: Required[int]
    """File share size"""

    volume_type: Required[Literal["vast_share_type"]]
    """File share volume type"""

    tags: Dict[str, str]
    """Key-value tags to associate with the resource.

    A tag is a key-value pair that can be associated with a resource, enabling
    efficient filtering and grouping for better organization and management. Some
    tags are read-only and cannot be modified by the user. Tags are also integrated
    with cost reports, allowing cost data to be filtered based on tag keys or
    values.
    """


FileShareCreateParams: TypeAlias = Union[CreateStandardFileShareSerializer, CreateVastFileShareSerializer]
