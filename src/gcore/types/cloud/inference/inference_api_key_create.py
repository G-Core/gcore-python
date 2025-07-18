# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["InferenceAPIKeyCreate"]


class InferenceAPIKeyCreate(BaseModel):
    created_at: str
    """Timestamp when the API Key was created."""

    deployment_names: List[str]
    """List of inference deployment names to which this API Key has been attached."""

    description: Optional[str] = None
    """Description of the API Key."""

    expires_at: Optional[str] = None
    """Timestamp when the API Key will expire."""

    name: str
    """API Key name."""

    secret: str
    """The actual API Key secret."""
