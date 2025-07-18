# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["APIKeyCreateParams"]


class APIKeyCreateParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    name: Required[str]
    """Name of the API Key."""

    description: str
    """Description of the API Key."""

    expires_at: str
    """Expiration date of the API Key in ISO 8601 format."""
