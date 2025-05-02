# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RegistryCredentialCreateParams"]


class RegistryCredentialCreateParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    name: Required[str]
    """Registry credential name."""

    password: Required[str]
    """Registry password."""

    registry_url: Required[str]
    """Registry URL."""

    username: Required[str]
    """Registry username."""
