# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ConsoleGetParams"]


class ConsoleGetParams(TypedDict, total=False):
    project_id: int
    """Project ID."""

    console_type: Literal["novnc", "spice"]
    """Console type that you expect.

    If you omit it, you get the first available type in this order: `novnc`,
    `spice`.
    """
