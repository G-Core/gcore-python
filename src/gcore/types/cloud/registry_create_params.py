# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RegistryCreateParams"]


class RegistryCreateParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fregistries%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
    "$.paths['/cloud/v1/registries/{project_id}/{region_id}'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fregistries%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
    "$.paths['/cloud/v1/registries/{project_id}/{region_id}'].post.parameters[1].schema"
    """

    name: Required[str]
    """
    '#/components/schemas/RegistryCreateSerializer/properties/name'
    "$.components.schemas.RegistryCreateSerializer.properties.name"
    """

    storage_limit: int
    """
    '#/components/schemas/RegistryCreateSerializer/properties/storage_limit'
    "$.components.schemas.RegistryCreateSerializer.properties.storage_limit"
    """
