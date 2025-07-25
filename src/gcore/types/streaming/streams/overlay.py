# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["Overlay"]


class Overlay(BaseModel):
    id: int
    """ID of the overlay"""

    created_at: str
    """Datetime of creation in ISO 8601"""

    stream_id: int
    """ID of a stream to which it is attached"""

    updated_at: str
    """Datetime of last update in ISO 8601"""

    url: str
    """Valid http/https URL to an HTML page/widget"""

    height: Optional[int] = None
    """Height of the widget"""

    stretch: Optional[bool] = None
    """Switch of auto scaling the widget.

    Must not be used as "true" simultaneously with the coordinate installation
    method (w, h, x, y).
    """

    width: Optional[int] = None
    """Width of the widget"""

    x: Optional[int] = None
    """Coordinate of left upper corner"""

    y: Optional[int] = None
    """Coordinate of left upper corner"""
