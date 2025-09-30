# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ShieldAggregatedStats"]


class ShieldAggregatedStats(BaseModel):
    api_1_example: Optional[object] = FieldInfo(alias="1 (example)", default=None)
    """CDN resource ID for which statistics data is shown."""

    metrics: Optional[object] = None
    """Statistics parameters."""

    resource: Optional[object] = None
    """Resources IDs by which statistics data is grouped."""

    shield_usage: Optional[str] = None
    """Number of CDN resources that used origin shielding."""
