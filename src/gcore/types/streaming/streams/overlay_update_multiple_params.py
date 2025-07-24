# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["OverlayUpdateMultipleParams", "Body"]


class OverlayUpdateMultipleParams(TypedDict, total=False):
    body: Iterable[Body]


class Body(TypedDict, total=False):
    id: Required[int]
    """ID of the overlay"""

    height: int
    """Height of the widget"""

    stretch: bool
    """Switch of auto scaling the widget.

    Must not be used as "true" simultaneously with the coordinate installation
    method (w, h, x, y).
    """

    url: str
    """Valid http/https URL to an HTML page/widget"""

    width: int
    """Width of the widget"""

    x: int
    """Coordinate of left upper corner"""

    y: int
    """Coordinate of left upper corner"""
