# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DirectoryCreateParams"]


class DirectoryCreateParams(TypedDict, total=False):
    name: Required[str]
    """Title of the directory."""

    parent_id: int
    """ID of a parent directory. "null" if it's in the root."""
