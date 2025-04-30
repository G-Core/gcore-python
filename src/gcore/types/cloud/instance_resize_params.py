# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["InstanceResizeParams"]


class InstanceResizeParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fchangeflavor/post/parameters/0/schema'
    "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/changeflavor'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Fchangeflavor/post/parameters/1/schema'
    "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/changeflavor'].post.parameters[1].schema"
    """

    flavor_id: Required[str]
    """
    '#/components/schemas/FlavorIdSchema/properties/flavor_id'
    "$.components.schemas.FlavorIdSchema.properties.flavor_id"
    """
