# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SecretDeleteParams"]


class SecretDeleteParams(TypedDict, total=False):
    force: bool
    """When true, deletes secret even if used by applications. Defaults to false."""
