# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["FlavorListSuitableParams"]


class FlavorListSuitableParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2Favailable_flavors/post/parameters/0/schema'
    "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}/available_flavors'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2Favailable_flavors/post/parameters/1/schema'
    "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}/available_flavors'].post.parameters[1].schema"
    """

    include_prices: bool
    """
    '#/paths/%2Fcloud%2Fv1%2Fbminstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2Favailable_flavors/post/parameters/2'
    "$.paths['/cloud/v1/bminstances/{project_id}/{region_id}/available_flavors'].post.parameters[2]"
    """

    apptemplate_id: str
    """
    '#/components/schemas/AvailableBaremetalFlavorsRequestSchema/properties/apptemplate_id'
    "$.components.schemas.AvailableBaremetalFlavorsRequestSchema.properties.apptemplate_id"
    """

    image_id: str
    """
    '#/components/schemas/AvailableBaremetalFlavorsRequestSchema/properties/image_id'
    "$.components.schemas.AvailableBaremetalFlavorsRequestSchema.properties.image_id"
    """
