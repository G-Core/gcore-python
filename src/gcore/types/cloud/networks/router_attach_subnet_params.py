# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RouterAttachSubnetParams"]


class RouterAttachSubnetParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Frouters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Brouter_id%7D%2Fattach/post/parameters/0/schema'
    "$.paths['/cloud/v1/routers/{project_id}/{region_id}/{router_id}/attach'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Frouters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Brouter_id%7D%2Fattach/post/parameters/1/schema'
    "$.paths['/cloud/v1/routers/{project_id}/{region_id}/{router_id}/attach'].post.parameters[1].schema"
    """

    subnet_id: Required[str]
    """
    '#/components/schemas/SubnetIdSerializer/properties/subnet_id'
    "$.components.schemas.SubnetIdSerializer.properties.subnet_id"
    """
