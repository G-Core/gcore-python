# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["FilterTemplateCreateParams"]


class FilterTemplateCreateParams(TypedDict, total=False):
    filter_config: Required[Dict[str, object]]
    """Arbitrary JSON object storing the frontend filter state"""

    name: Required[str]
    """Human-readable template name"""
