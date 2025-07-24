# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["DirectoryUpdateParams"]


class DirectoryUpdateParams(TypedDict, total=False):
    name: str
    """Title of the directory. Omit this if you don't want to change."""

    parent_id: int
    """ID of a parent directory.

    "null" if it's in the root. Omit this if you don't want to change.
    """
