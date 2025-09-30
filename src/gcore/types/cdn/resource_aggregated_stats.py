# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ResourceAggregatedStats"]


class ResourceAggregatedStats(BaseModel):
    api_1_example: Optional[object] = FieldInfo(alias="1 (example)", default=None)
    """CDN resource ID for which statistics data is shown."""

    api_95_percentile: Optional[int] = FieldInfo(alias="95_percentile", default=None)
    """95 percentile bandwidth value"""

    backblaze_bytes: Optional[int] = None
    """Traffic in bytes from Backblaze origin."""

    cache_hit_traffic_ratio: Optional[int] = None
    """Formula: 1 - `upstream_bytes` / `sent_bytes`.

    We deduct the non-cached traffic from the total traffic amount
    """

    cis_example: Optional[object] = FieldInfo(alias="cis (example)", default=None)
    """Region by which statistics data is grouped."""

    max_bandwidth: Optional[int] = None
    """Maximum bandwidth"""

    metrics: Optional[object] = None
    """Statistics parameters."""

    min_bandwidth: Optional[int] = None
    """Minimum bandwidth"""

    region: Optional[object] = None
    """Regions by which statistics data is grouped."""

    requests: Optional[int] = None
    """Number of requests to edge servers."""

    resource: Optional[object] = None
    """Resources IDs by which statistics data is grouped."""

    response_types: Optional[object] = None
    """Statistics by content type.

    It returns a number of responses for content with different MIME types.
    """

    responses_2xx: Optional[int] = None
    """Number of 2xx response codes."""

    responses_3xx: Optional[int] = None
    """Number of 3xx response codes."""

    responses_4xx: Optional[int] = None
    """Number of 4xx response codes."""

    responses_5xx: Optional[int] = None
    """Number of 5xx response codes."""

    responses_hit: Optional[int] = None
    """Number of responses with the header Cache: HIT."""

    responses_miss: Optional[int] = None
    """Number of responses with the header Cache: MISS."""

    sent_bytes: Optional[int] = None
    """Traffic in bytes from CDN servers to clients."""

    total_bytes: Optional[int] = None
    """Upstream bytes and `sent_bytes` combined."""

    upstream_bytes: Optional[int] = None
    """Traffic in bytes from the upstream to CDN servers."""
