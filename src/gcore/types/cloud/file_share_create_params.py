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
    "CreateVastFileShareSerializerShareSettings",
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
    """File share size in GiB"""

    access: Iterable[CreateStandardFileShareSerializerAccess]
    """Access Rules"""

    tags: Dict[str, str]
    """Key-value tags to associate with the resource.

    A tag is a key-value pair that can be associated with a resource, enabling
    efficient filtering and grouping for better organization and management. Both
    tag keys and values have a maximum length of 255 characters. Some tags are
    read-only and cannot be modified by the user. Tags are also integrated with cost
    reports, allowing cost data to be filtered based on tag keys or values.
    """

    type_name: Literal["standard"]
    """Standard file share type"""

    volume_type: Literal["default_share_type"]
    """Deprecated. Use `type_name` instead."""


class CreateStandardFileShareSerializerNetwork(TypedDict, total=False):
    """File share network configuration"""

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
    """File share size in GiB"""

    share_settings: CreateVastFileShareSerializerShareSettings
    """Configuration settings for the share"""

    tags: Dict[str, str]
    """Key-value tags to associate with the resource.

    A tag is a key-value pair that can be associated with a resource, enabling
    efficient filtering and grouping for better organization and management. Both
    tag keys and values have a maximum length of 255 characters. Some tags are
    read-only and cannot be modified by the user. Tags are also integrated with cost
    reports, allowing cost data to be filtered based on tag keys or values.
    """

    type_name: Literal["vast"]
    """Vast file share type"""

    volume_type: Literal["vast_share_type"]
    """Deprecated. Use `type_name` instead."""


class CreateVastFileShareSerializerShareSettings(TypedDict, total=False):
    """Configuration settings for the share"""

    allowed_characters: Literal["LCD", "NPL"]
    """Determines which characters are allowed in file names. Choose between:

    - Lowest Common Denominator (LCD), allows only characters allowed by all VAST
      Cluster-supported protocols
    - Native Protocol Limit (NPL), imposes no limitation beyond that of the client
      protocol.
    """

    path_length: Literal["LCD", "NPL"]
    """Affects the maximum limit of file path component name length. Choose between:

    - Lowest Common Denominator (LCD), imposes the lowest common denominator file
      length limit of all VAST Cluster-supported protocols. With this (default)
      option, the limitation on the length of a single component of the path is 255
      characters
    - Native Protocol Limit (NPL), imposes no limitation beyond that of the client
      protocol.
    """

    root_squash: bool
    """Enables or disables root squash for NFS clients.

    - If `true` (default), root squash is enabled: the root user is mapped to nobody
      for all file and folder management operations on the export.
    - If `false`, root squash is disabled: the NFS client `root` user retains root
      privileges. Use this option if you trust the root user not to perform
      operations that will corrupt data.
    """


FileShareCreateParams: TypeAlias = Union[CreateStandardFileShareSerializer, CreateVastFileShareSerializer]
