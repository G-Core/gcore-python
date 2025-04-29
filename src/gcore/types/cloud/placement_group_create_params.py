# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PlacementGroupCreateParams"]


class PlacementGroupCreateParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fservergroups%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
    "$.paths['/cloud/v1/servergroups/{project_id}/{region_id}'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fservergroups%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
    "$.paths['/cloud/v1/servergroups/{project_id}/{region_id}'].post.parameters[1].schema"
    """

    name: Required[str]
    """
    '#/components/schemas/CreateServerGroupSerializer/properties/name'
    "$.components.schemas.CreateServerGroupSerializer.properties.name"
    """

    policy: Required[Literal["affinity", "anti-affinity", "soft-anti-affinity"]]
    """
    '#/components/schemas/CreateServerGroupSerializer/properties/policy'
    "$.components.schemas.CreateServerGroupSerializer.properties.policy"
    """
