# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["UserCreateParams"]


class UserCreateParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fregistries%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bregistry_id%7D%2Fusers/post/parameters/0/schema'
    "$.paths['/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fregistries%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bregistry_id%7D%2Fusers/post/parameters/1/schema'
    "$.paths['/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/users'].post.parameters[1].schema"
    """

    duration: Required[int]
    """
    '#/components/schemas/RegistryUserCreateSerializer/properties/duration'
    "$.components.schemas.RegistryUserCreateSerializer.properties.duration"
    """

    name: Required[str]
    """
    '#/components/schemas/RegistryUserCreateSerializer/properties/name'
    "$.components.schemas.RegistryUserCreateSerializer.properties.name"
    """

    read_only: bool
    """
    '#/components/schemas/RegistryUserCreateSerializer/properties/read_only'
    "$.components.schemas.RegistryUserCreateSerializer.properties.read_only"
    """

    secret: str
    """
    '#/components/schemas/RegistryUserCreateSerializer/properties/secret'
    "$.components.schemas.RegistryUserCreateSerializer.properties.secret"
    """
