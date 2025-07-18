# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["APIKeyUpdateParams"]


class APIKeyUpdateParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    description: Optional[str]
    """Description of the API Key."""
