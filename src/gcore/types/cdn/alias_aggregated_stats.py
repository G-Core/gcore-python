# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AliasAggregatedStats", "Metrics"]


class Metrics(BaseModel):
    """Statistics parameters."""

    alias_usage: Optional[int] = None
    """Number of aliases in use."""


class AliasAggregatedStats(BaseModel):
    api_1_example: Optional[object] = FieldInfo(alias="1 (example)", default=None)
    """CDN resource ID for which statistics data is shown."""

    api_12_example: Optional[object] = FieldInfo(alias="12 (example)", default=None)
    """Client ID for which statistics data is shown."""

    client: Optional[object] = None
    """Client IDs by which statistics data is grouped."""

    metrics: Optional[Metrics] = None
    """Statistics parameters."""

    resource: Optional[object] = None
    """Resources IDs by which statistics data is grouped."""
