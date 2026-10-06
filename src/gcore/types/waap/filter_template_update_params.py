# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

__all__ = ["FilterTemplateUpdateParams"]


class FilterTemplateUpdateParams(TypedDict, total=False):
    filter_config: Optional[Dict[str, object]]
    """Arbitrary JSON object storing the frontend filter state"""

    name: Optional[str]
    """Human-readable template name"""
