# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .tag_update_list_param import TagUpdateListParam

__all__ = ["NetworkCreateParams"]


class NetworkCreateParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fnetworks%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
    "$.paths['/cloud/v1/networks/{project_id}/{region_id}'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fnetworks%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
    "$.paths['/cloud/v1/networks/{project_id}/{region_id}'].post.parameters[1].schema"
    """

    name: Required[str]
    """
    '#/components/schemas/CreateNetworkSerializer/properties/name'
    "$.components.schemas.CreateNetworkSerializer.properties.name"
    """

    create_router: bool
    """
    '#/components/schemas/CreateNetworkSerializer/properties/create_router'
    "$.components.schemas.CreateNetworkSerializer.properties.create_router"
    """

    tags: TagUpdateListParam
    """
    '#/components/schemas/CreateNetworkSerializer/properties/tags'
    "$.components.schemas.CreateNetworkSerializer.properties.tags"
    """

    type: Literal["vlan", "vxlan"]
    """
    '#/components/schemas/CreateNetworkSerializer/properties/type'
    "$.components.schemas.CreateNetworkSerializer.properties.type"
    """
