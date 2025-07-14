# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["InferenceModel"]


class InferenceModel(BaseModel):
    id: str
    """Model ID."""

    category: Optional[str] = None
    """Category of the model."""

    default_flavor_name: Optional[str] = None
    """Default flavor for the model."""

    description: str
    """Description of the model."""

    developer: Optional[str] = None
    """Developer of the model."""

    documentation_page: Optional[str] = None
    """Path to the documentation page."""

    eula_url: Optional[str] = None
    """URL to the EULA text."""

    example_curl_request: Optional[str] = None
    """Example curl request to the model."""

    has_eula: bool
    """Whether the model has an EULA."""

    image_registry_id: Optional[str] = None
    """Image registry of the model."""

    image_url: str
    """Image URL of the model."""

    inference_backend: Optional[str] = None
    """Describing underlying inference engine."""

    inference_frontend: Optional[str] = None
    """Describing model frontend type."""

    api_model_id: Optional[str] = FieldInfo(alias="model_id", default=None)
    """Model name to perform inference call."""

    name: str
    """Name of the model."""

    openai_compatibility: Optional[str] = None
    """OpenAI compatibility level."""

    port: int
    """Port on which the model runs."""

    version: Optional[str] = None
    """Version of the model."""
