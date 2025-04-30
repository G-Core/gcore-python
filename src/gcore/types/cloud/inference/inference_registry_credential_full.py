# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["InferenceRegistryCredentialFull"]


class InferenceRegistryCredentialFull(BaseModel):
    name: str
    """
    '#/components/schemas/InferenceRegistryCredentialOutFullSerializer/properties/name'
    "$.components.schemas.InferenceRegistryCredentialOutFullSerializer.properties.name"
    """

    password: str
    """
    '#/components/schemas/InferenceRegistryCredentialOutFullSerializer/properties/password'
    "$.components.schemas.InferenceRegistryCredentialOutFullSerializer.properties.password"
    """

    project_id: int
    """
    '#/components/schemas/InferenceRegistryCredentialOutFullSerializer/properties/project_id'
    "$.components.schemas.InferenceRegistryCredentialOutFullSerializer.properties.project_id"
    """

    registry_url: str
    """
    '#/components/schemas/InferenceRegistryCredentialOutFullSerializer/properties/registry_url'
    "$.components.schemas.InferenceRegistryCredentialOutFullSerializer.properties.registry_url"
    """

    username: str
    """
    '#/components/schemas/InferenceRegistryCredentialOutFullSerializer/properties/username'
    "$.components.schemas.InferenceRegistryCredentialOutFullSerializer.properties.username"
    """
