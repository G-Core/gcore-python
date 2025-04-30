# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RegistryCredentialReplaceParams"]


class RegistryCredentialReplaceParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fregistry_credentials%2F%7Bcredential_name%7D/put/parameters/0/schema'
    "$.paths['/cloud/v3/inference/{project_id}/registry_credentials/{credential_name}'].put.parameters[0].schema"
    """

    password: Required[str]
    """
    '#/components/schemas/InferenceRegistryCredentialInUpdateSerializer/properties/password'
    "$.components.schemas.InferenceRegistryCredentialInUpdateSerializer.properties.password"
    """

    registry_url: Required[str]
    """
    '#/components/schemas/InferenceRegistryCredentialInUpdateSerializer/properties/registry_url'
    "$.components.schemas.InferenceRegistryCredentialInUpdateSerializer.properties.registry_url"
    """

    username: Required[str]
    """
    '#/components/schemas/InferenceRegistryCredentialInUpdateSerializer/properties/username'
    "$.components.schemas.InferenceRegistryCredentialInUpdateSerializer.properties.username"
    """
