# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PlacementGroupDeleteParams"]


class PlacementGroupDeleteParams(TypedDict, total=False):
    project_id: int
    """Project ID."""

    dry_run: bool
    """Run every check of the real request and change nothing.

    The response has the status code and the schema of the real call, and an empty
    list of tasks. With `false`, the default, the request does the operation.
    """
