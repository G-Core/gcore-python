# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["LogsAggregatedStats"]


class LogsAggregatedStats(BaseModel):
    api_1_example: Optional[object] = FieldInfo(alias="1 (example)", default=None)
    """CDN resource ID for which statistics data is shown."""

    metrics: Optional[object] = None
    """Statistics parameters."""

    raw_logs_usage: Optional[str] = None
    """Number of resources that used Logs uploader."""

    resource: Optional[object] = None
    """Resources IDs by which statistics data is grouped.."""
