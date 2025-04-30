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
    """
    '#/paths/%2Fcloud%2Fv1%2Ffile_shares%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
    "$.paths['/cloud/v1/file_shares/{project_id}/{region_id}'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Ffile_shares%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
    "$.paths['/cloud/v1/file_shares/{project_id}/{region_id}'].post.parameters[1].schema"
    """

    name: Required[str]
    """
    '#/components/schemas/CreateStandardFileShareSerializer/properties/name'
    "$.components.schemas.CreateStandardFileShareSerializer.properties.name"
    """

    network: Required[CreateStandardFileShareSerializerNetwork]
    """
    '#/components/schemas/CreateStandardFileShareSerializer/properties/network'
    "$.components.schemas.CreateStandardFileShareSerializer.properties.network"
    """

    protocol: Required[Literal["NFS"]]
    """
    '#/components/schemas/CreateStandardFileShareSerializer/properties/protocol'
    "$.components.schemas.CreateStandardFileShareSerializer.properties.protocol"
    """

    size: Required[int]
    """
    '#/components/schemas/CreateStandardFileShareSerializer/properties/size'
    "$.components.schemas.CreateStandardFileShareSerializer.properties.size"
    """

    access: Iterable[CreateStandardFileShareSerializerAccess]
    """
    '#/components/schemas/CreateStandardFileShareSerializer/properties/access'
    "$.components.schemas.CreateStandardFileShareSerializer.properties.access"
    """

    tags: Dict[str, str]
    """
    '#/components/schemas/CreateStandardFileShareSerializer/properties/tags'
    "$.components.schemas.CreateStandardFileShareSerializer.properties.tags"
    """

    volume_type: Literal["default_share_type"]
    """
    '#/components/schemas/CreateStandardFileShareSerializer/properties/volume_type'
    "$.components.schemas.CreateStandardFileShareSerializer.properties.volume_type"
    """


class CreateStandardFileShareSerializerNetwork(TypedDict, total=False):
    network_id: Required[str]
    """
    '#/components/schemas/FileShareNetworkSerializer/properties/network_id'
    "$.components.schemas.FileShareNetworkSerializer.properties.network_id"
    """

    subnet_id: str
    """
    '#/components/schemas/FileShareNetworkSerializer/properties/subnet_id'
    "$.components.schemas.FileShareNetworkSerializer.properties.subnet_id"
    """


class CreateStandardFileShareSerializerAccess(TypedDict, total=False):
    access_mode: Required[Literal["ro", "rw"]]
    """
    '#/components/schemas/CreateAccessRuleSerializer/properties/access_mode'
    "$.components.schemas.CreateAccessRuleSerializer.properties.access_mode"
    """

    ip_address: Required[str]
    """
    '#/components/schemas/CreateAccessRuleSerializer/properties/ip_address/anyOf/0'
    "$.components.schemas.CreateAccessRuleSerializer.properties.ip_address.anyOf[0]"
    """


class CreateVastFileShareSerializer(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Ffile_shares%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
    "$.paths['/cloud/v1/file_shares/{project_id}/{region_id}'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Ffile_shares%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
    "$.paths['/cloud/v1/file_shares/{project_id}/{region_id}'].post.parameters[1].schema"
    """

    name: Required[str]
    """
    '#/components/schemas/CreateVastFileShareSerializer/properties/name'
    "$.components.schemas.CreateVastFileShareSerializer.properties.name"
    """

    protocol: Required[Literal["NFS"]]
    """
    '#/components/schemas/CreateVastFileShareSerializer/properties/protocol'
    "$.components.schemas.CreateVastFileShareSerializer.properties.protocol"
    """

    size: Required[int]
    """
    '#/components/schemas/CreateVastFileShareSerializer/properties/size'
    "$.components.schemas.CreateVastFileShareSerializer.properties.size"
    """

    volume_type: Required[Literal["vast_share_type"]]
    """
    '#/components/schemas/CreateVastFileShareSerializer/properties/volume_type'
    "$.components.schemas.CreateVastFileShareSerializer.properties.volume_type"
    """

    tags: Dict[str, str]
    """
    '#/components/schemas/CreateVastFileShareSerializer/properties/tags'
    "$.components.schemas.CreateVastFileShareSerializer.properties.tags"
    """


FileShareCreateParams: TypeAlias = Union[CreateStandardFileShareSerializer, CreateVastFileShareSerializer]
