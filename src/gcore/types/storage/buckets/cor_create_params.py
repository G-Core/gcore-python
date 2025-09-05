# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["CorCreateParams"]


class CorCreateParams(TypedDict, total=False):
    storage_id: Required[int]

    allowed_origins: Annotated[SequenceNotStr[str], PropertyInfo(alias="allowedOrigins")]
    """List of allowed origins for CORS requests"""
