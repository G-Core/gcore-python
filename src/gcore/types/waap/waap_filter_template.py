# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from ..._models import BaseModel

__all__ = ["WaapFilterTemplate"]


class WaapFilterTemplate(BaseModel):
    """Response body for a single filter template."""

    id: int
    """The ID of the filter template"""

    filter_config: Dict[str, object]
    """Arbitrary JSON object storing the frontend filter state"""

    name: str
    """Human-readable template name"""
