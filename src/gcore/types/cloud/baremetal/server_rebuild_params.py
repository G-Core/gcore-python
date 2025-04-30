# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ServerRebuildParams"]


class ServerRebuildParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bserver_id%7D%2Frebuild/post/parameters/0/schema'
    "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}/{server_id}/rebuild'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bserver_id%7D%2Frebuild/post/parameters/1/schema'
    "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}/{server_id}/rebuild'].post.parameters[1].schema"
    """

    image_id: str
    """
    '#/components/schemas/RebuildBaremetalSchema/properties/image_id'
    "$.components.schemas.RebuildBaremetalSchema.properties.image_id"
    """

    user_data: str
    """
    '#/components/schemas/RebuildBaremetalSchema/properties/user_data'
    "$.components.schemas.RebuildBaremetalSchema.properties.user_data"
    """
