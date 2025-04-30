# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RegistryCredentialCreateParams"]


class RegistryCredentialCreateParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fregistry_credentials/post/parameters/0/schema'
    "$.paths['/cloud/v3/inference/{project_id}/registry_credentials'].post.parameters[0].schema"
    """

    name: Required[str]
    """
    '#/components/schemas/InferenceRegistryCredentialInSerializer/properties/name'
    "$.components.schemas.InferenceRegistryCredentialInSerializer.properties.name"
    """

    password: Required[str]
    """
    '#/components/schemas/InferenceRegistryCredentialInSerializer/properties/password'
    "$.components.schemas.InferenceRegistryCredentialInSerializer.properties.password"
    """

    registry_url: Required[str]
    """
    '#/components/schemas/InferenceRegistryCredentialInSerializer/properties/registry_url'
    "$.components.schemas.InferenceRegistryCredentialInSerializer.properties.registry_url"
    """

    username: Required[str]
    """
    '#/components/schemas/InferenceRegistryCredentialInSerializer/properties/username'
    "$.components.schemas.InferenceRegistryCredentialInSerializer.properties.username"
    """
