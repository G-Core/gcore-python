# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["InferenceRegistryCredential"]


class InferenceRegistryCredential(BaseModel):
    name: str
    """
    '#/components/schemas/InferenceRegistryCredentialOutSerializer/properties/name'
    "$.components.schemas.InferenceRegistryCredentialOutSerializer.properties.name"
    """

    project_id: int
    """
    '#/components/schemas/InferenceRegistryCredentialOutSerializer/properties/project_id'
    "$.components.schemas.InferenceRegistryCredentialOutSerializer.properties.project_id"
    """

    registry_url: str
    """
    '#/components/schemas/InferenceRegistryCredentialOutSerializer/properties/registry_url'
    "$.components.schemas.InferenceRegistryCredentialOutSerializer.properties.registry_url"
    """

    username: str
    """
    '#/components/schemas/InferenceRegistryCredentialOutSerializer/properties/username'
    "$.components.schemas.InferenceRegistryCredentialOutSerializer.properties.username"
    """
