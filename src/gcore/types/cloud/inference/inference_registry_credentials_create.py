# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["InferenceRegistryCredentialsCreate"]


class InferenceRegistryCredentialsCreate(BaseModel):
    name: str
    """Registry credential name."""

    password: str
    """Registry password."""

    project_id: int
    """Project ID to which the inference registry credentials belongs."""

    registry_url: str
    """Registry URL."""

    username: str
    """Registry username."""
