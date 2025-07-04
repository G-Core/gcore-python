# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["InferenceRegistryCredentials"]


class InferenceRegistryCredentials(BaseModel):
    name: str
    """Registry credential name."""

    project_id: int
    """Project ID to which the inference registry credentials belongs."""

    registry_url: str
    """Registry URL."""

    username: str
    """Registry username."""
