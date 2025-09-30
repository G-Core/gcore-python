# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["MetricListParams", "FilterBy"]


class MetricListParams(TypedDict, total=False):
    from_: Required[Annotated[str, PropertyInfo(alias="from")]]
    """Beginning period to fetch metrics (ISO 8601/RFC 3339 format, UTC.)

    Examples:

    - 2021-06-14T00:00:00Z
    - 2021-06-14T00:00:00.000Z

    The total number of points, which is determined as the difference between "from"
    and "to" divided by "granularity", cannot exceed 1440. Exception: "speed"
    metrics are limited to 72 points.
    """

    metrics: Required[SequenceNotStr[str]]
    """Possible values:

    - **`edge_bandwidth`** - Bandwidth from client to CDN (bit/s.)
    - **`edge_requests`** - Number of requests per interval (requests/s.)
    - **`edge_requests_total`** - Total number of requests per interval.
    - **`edge_status_1xx`** - Number of 1xx status codes from edge.
    - **`edge_status_200`** - Number of 200 status codes from edge.
    - **`edge_status_204`** - Number of 204 status codes from edge.
    - **`edge_status_206`** - Number of 206 status codes from edge.
    - **`edge_status_2xx`** - Number of 2xx status codes from edge.
    - **`edge_status_301`** - Number of 301 status codes from edge.
    - **`edge_status_302`** - Number of 302 status codes from edge.
    - **`edge_status_304`** - Number of 304 status codes from edge.
    - **`edge_status_3xx`** - Number of 3xx status codes from edge.
    - **`edge_status_400`** - Number of 400 status codes from edge.
    - **`edge_status_401`** - Number of 401 status codes from edge.
    - **`edge_status_403`** - Number of 403 status codes from edge.
    - **`edge_status_404`** - Number of 404 status codes from edge.
    - **`edge_status_416`** - Number of 416 status codes from edge.
    - **`edge_status_429`** - Number of 429 status codes from edge.
    - **`edge_status_4xx`** - Number of 4xx status codes from edge.
    - **`edge_status_500`** - Number of 500 status codes from edge.
    - **`edge_status_501`** - Number of 501 status codes from edge.
    - **`edge_status_502`** - Number of 502 status codes from edge.
    - **`edge_status_503`** - Number of 503 status codes from edge.
    - **`edge_status_504`** - Number of 504 status codes from edge.
    - **`edge_status_505`** - Number of 505 status codes from edge.
    - **`edge_status_5xx`** - Number of 5xx status codes from edge.
    - **`edge_hit_ratio`** - Percent of cache hits (0.0 - 1.0).
    - **`edge_hit_bytes`** - Number of bytes sent back when cache hits.
    - **`origin_bandwidth`** - Bandwidth from CDN to Origin (bit/s.)
    - **`origin_requests`** - Number of requests per interval (requests/s.)
    - **`origin_status_1xx`** - Number of 1xx status from origin.
    - **`origin_status_200`** - Number of 200 status from origin.
    - **`origin_status_204`** - Number of 204 status from origin.
    - **`origin_status_206`** - Number of 206 status from origin.
    - **`origin_status_2xx`** - Number of 2xx status from origin.
    - **`origin_status_301`** - Number of 301 status from origin.
    - **`origin_status_302`** - Number of 302 status from origin.
    - **`origin_status_304`** - Number of 304 status from origin.
    - **`origin_status_3xx`** - Number of 3xx status from origin.
    - **`origin_status_400`** - Number of 400 status from origin.
    - **`origin_status_401`** - Number of 401 status from origin.
    - **`origin_status_403`** - Number of 403 status from origin.
    - **`origin_status_404`** - Number of 404 status from origin.
    - **`origin_status_416`** - Number of 416 status from origin.
    - **`origin_status_429`** - Number of 426 status from origin.
    - **`origin_status_4xx`** - Number of 4xx status from origin.
    - **`origin_status_500`** - Number of 500 status from origin.
    - **`origin_status_501`** - Number of 501 status from origin.
    - **`origin_status_502`** - Number of 502 status from origin.
    - **`origin_status_503`** - Number of 503 status from origin.
    - **`origin_status_504`** - Number of 504 status from origin.
    - **`origin_status_505`** - Number of 505 status from origin.
    - **`origin_status_5xx`** - Number of 5xx status from origin.
    - **`edge_download_speed`** - Download speed from edge in KB/s (includes only
      requests that status was in the range [200, 300].)
    - **`origin_download_speed`** - Download speed from origin in KB/s (includes
      only requests that status was in the range [200, 300].)
    """

    to: Required[str]
    """Specifies ending period to fetch metrics (ISO 8601/RFC 3339 format, UTC)

    Examples:

    - 2021-06-15T00:00:00Z
    - 2021-06-15T00:00:00.000Z

    The total number of points, which is determined as the difference between "from"
    and "to" divided by "granularity", cannot exceed 1440. Exception: "speed"
    metrics are limited to 72 points.
    """

    filter_by: Iterable[FilterBy]
    """Each item represents one filter statement."""

    granularity: str
    """Duration of the time blocks into which the data is divided.

    The value must correspond to the ISO 8601 period format.

    Examples:

    - P1D
    - PT5M

    Notes:

    - The total number of points, which is determined as the difference between
      "from" and "to" divided by "granularity", cannot exceed 1440. Exception:
      "speed" metrics are limited to 72 points.
    - For "speed" metrics the value must be a multiple of 5.
    """

    group_by: SequenceNotStr[str]
    """Output data grouping.

    Possible values:

    - **resource** - Data is grouped by CDN resource.
    - **cname** - Data is grouped by common names.
    - **region** – Data is grouped by regions (continents.) Available for "speed"
      metrics only.
    - **isp** - Data is grouped by ISP names. Available for "speed" metrics only.
    """


class FilterBy(TypedDict, total=False):
    field: Required[str]
    """Defines the parameters by that data can be filtered.

    Possible values:

    - **resource** - Data is filtered by CDN resource ID.
    - **cname** - Data is filtered by common name.
    - **region** - Data is filtered by region (continent.) Available for "speed"
      metrics only.
    - **isp** - Data is filtered by ISP name. Available for "speed" metrics only.
    """

    op: Required[str]
    """Comparison operator to be applied.

    Possible values:

    - **in** - 'IN' operator.
    - **`not_in`** - 'NOT IN' operator.
    - **gt** - '>' operator.
    - **gte** - '>=' operator.
    - **lt** - '<' operator.
    - **lte** - '<=' operator.
    - **eq** - '==' operator.
    - **ne** - '!=' operator.
    - **like** - 'LIKE' operator.
    - **`not_like`** - 'NOT LIKE' operator.
    """

    values: Required[SequenceNotStr[Union[float, str]]]
    """Contains one or more values to be compared against."""
