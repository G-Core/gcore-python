# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["LogListParams"]


class LogListParams(TypedDict, total=False):
    from_: Required[Annotated[str, PropertyInfo(alias="from")]]
    """
    Start date and time of the requested time period (ISO 8601/RFC 3339 format,
    UTC.)

    Difference between "from" and "to" cannot exceed 6 hours.

    Examples:

    - &from=2021-06-14T00:00:00Z
    - &from=2021-06-14T00:00:00.000Z
    """

    to: Required[str]
    """End date and time of the requested time period (ISO 8601/RFC 3339 format, UTC.)

    Difference between "from" and "to" cannot exceed 6 hours.

    Examples:

    - &to=2021-06-15T00:00:00Z
    - &to=2021-06-15T00:00:00.000Z
    """

    cache_status_eq: Annotated[str, PropertyInfo(alias="cache_status__eq")]
    """Caching status.

    Possible values: 'MISS', 'BYPASS', 'EXPIRED', 'STALE', 'PENDING', 'UPDATING',
    'REVALIDATED', 'HIT', '-'.
    """

    cache_status_in: Annotated[str, PropertyInfo(alias="cache_status__in")]
    """List of caching statuses.

    Possible values: 'MISS', 'BYPASS', 'EXPIRED', 'STALE', 'PENDING', 'UPDATING',
    'REVALIDATED', 'HIT', '-'. Values should be separated by a comma.
    """

    cache_status_ne: Annotated[str, PropertyInfo(alias="cache_status__ne")]
    """Caching status not equal to the specified value.

    Possible values: 'MISS', 'BYPASS', 'EXPIRED', 'STALE', 'PENDING', 'UPDATING',
    'REVALIDATED', 'HIT', '-'.
    """

    cache_status_not_in: Annotated[str, PropertyInfo(alias="cache_status__not_in")]
    """List of caching statuses not equal to the specified values.

    Possible values: 'MISS', 'BYPASS', 'EXPIRED', 'STALE', 'PENDING', 'UPDATING',
    'REVALIDATED', 'HIT', '-'. Values should be separated by a comma.
    """

    client_ip_eq: Annotated[str, PropertyInfo(alias="client_ip__eq")]
    """IP address of the client who sent the request."""

    client_ip_in: Annotated[str, PropertyInfo(alias="client_ip__in")]
    """List of IP addresses of the clients who sent the request."""

    client_ip_ne: Annotated[str, PropertyInfo(alias="client_ip__ne")]
    """IP address of the client who did not send the request."""

    client_ip_not_in: Annotated[str, PropertyInfo(alias="client_ip__not_in")]
    """List of IP addresses of the clients who did not send the request."""

    cname_contains: Annotated[str, PropertyInfo(alias="cname__contains")]
    """Part of the custom domain of the requested CDN resource.

    Minimum length is 3 characters.
    """

    cname_eq: Annotated[str, PropertyInfo(alias="cname__eq")]
    """Custom domain of the requested CDN resource."""

    cname_in: Annotated[str, PropertyInfo(alias="cname__in")]
    """List of custom domains of the requested CDN resource.

    Values should be separated by a comma.
    """

    cname_ne: Annotated[str, PropertyInfo(alias="cname__ne")]
    """Custom domain of the requested CDN resource not equal to the specified value."""

    cname_not_in: Annotated[str, PropertyInfo(alias="cname__not_in")]
    """
    List of custom domains of the requested CDN resource not equal to the specified
    values. Values should be separated by a comma.
    """

    datacenter_eq: Annotated[str, PropertyInfo(alias="datacenter__eq")]
    """Data center where request was processed."""

    datacenter_in: Annotated[str, PropertyInfo(alias="datacenter__in")]
    """List of data centers where request was processed.

    Values should be separated by a comma.
    """

    datacenter_ne: Annotated[str, PropertyInfo(alias="datacenter__ne")]
    """Data center where request was not processed."""

    datacenter_not_in: Annotated[str, PropertyInfo(alias="datacenter__not_in")]
    """List of data centers where request was not processed.

    Values should be separated by a comma.
    """

    fields: str
    """A comma-separated list of returned fields.

    Supported fields are presented in the responses section.

    Example:

    - &fields=timestamp,path,status
    """

    limit: int
    """Maximum number of log records in the response."""

    method_eq: Annotated[str, PropertyInfo(alias="method__eq")]
    """Request HTTP method.

    Possible values: 'CONNECT', 'DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH', 'POST',
    'PUT', 'TRACE'.
    """

    method_in: Annotated[str, PropertyInfo(alias="method__in")]
    """Request HTTP method.

    Possible values: 'CONNECT', 'DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH', 'POST',
    'PUT', 'TRACE'. Values should be separated by a comma.
    """

    method_ne: Annotated[str, PropertyInfo(alias="method__ne")]
    """Request HTTP method.

    Possible values: 'CONNECT', 'DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH', 'POST',
    'PUT', 'TRACE'.
    """

    method_not_in: Annotated[str, PropertyInfo(alias="method__not_in")]
    """Request HTTP method.

    Possible values: 'CONNECT', 'DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH', 'POST',
    'PUT', 'TRACE'. Values should be separated by a comma.
    """

    offset: int
    """
    Number of log records to skip starting from the beginning of the requested
    period.
    """

    ordering: str
    """Sorting rules.

    Possible values:

    - **method** - Request HTTP method.
    - **`client_ip`** - IP address of the client who sent the request.
    - **status** - Status code in the response.
    - **size** - Response size in bytes.
    - **cname** - Custom domain of the requested resource.
    - **`resource_id`** - ID of the requested CDN resource.
    - **`cache_status`** - Caching status.
    - **datacenter** - Data center where request was processed.
    - **timestamp** - Date and time when the request was made.

    Parameter may have multiple values separated by a comma.

    By default, ascending sorting is applied. To sort in descending order, add '-'
    prefix.

    Example:

    - &ordering=-timestamp,status
    """

    resource_id_eq: Annotated[int, PropertyInfo(alias="resource_id__eq")]
    """ID of the requested CDN resource equal to the specified value."""

    resource_id_gt: Annotated[int, PropertyInfo(alias="resource_id__gt")]
    """ID of the requested CDN resource greater than the specified value."""

    resource_id_gte: Annotated[int, PropertyInfo(alias="resource_id__gte")]
    """ID of the requested CDN resource greater than or equal to the specified value."""

    resource_id_in: Annotated[str, PropertyInfo(alias="resource_id__in")]
    """List of IDs of the requested CDN resource.

    Values should be separated by a comma.
    """

    resource_id_lt: Annotated[int, PropertyInfo(alias="resource_id__lt")]
    """ID of the requested CDN resource less than the specified value."""

    resource_id_lte: Annotated[int, PropertyInfo(alias="resource_id__lte")]
    """ID of the requested CDN resource less than or equal to the specified value."""

    resource_id_ne: Annotated[int, PropertyInfo(alias="resource_id__ne")]
    """ID of the requested CDN resource not equal to the specified value."""

    resource_id_not_in: Annotated[str, PropertyInfo(alias="resource_id__not_in")]
    """List of IDs of the requested CDN resource not equal to the specified values.

    Values should be separated by a comma.
    """

    size_eq: Annotated[int, PropertyInfo(alias="size__eq")]
    """Response size in bytes equal to the specified value."""

    size_gt: Annotated[int, PropertyInfo(alias="size__gt")]
    """Response size in bytes greater than the specified value."""

    size_gte: Annotated[int, PropertyInfo(alias="size__gte")]
    """Response size in bytes greater than or equal to the specified value."""

    size_in: Annotated[str, PropertyInfo(alias="size__in")]
    """List of response sizes in bytes. Values should be separated by a comma."""

    size_lt: Annotated[int, PropertyInfo(alias="size__lt")]
    """Response size in bytes less than the specified value."""

    size_lte: Annotated[int, PropertyInfo(alias="size__lte")]
    """Response size in bytes less than or equal to the specified value."""

    size_ne: Annotated[int, PropertyInfo(alias="size__ne")]
    """Response size in bytes not equal to the specified value."""

    size_not_in: Annotated[str, PropertyInfo(alias="size__not_in")]
    """List of response sizes in bytes not equal to the specified values.

    Values should be separated by
    """

    status_eq: Annotated[int, PropertyInfo(alias="status__eq")]
    """Status code in the response equal to the specified value."""

    status_gt: Annotated[int, PropertyInfo(alias="status__gt")]
    """Status code in the response greater than the specified value."""

    status_gte: Annotated[int, PropertyInfo(alias="status__gte")]
    """Status code in the response greater than or equal to the specified value."""

    status_in: Annotated[str, PropertyInfo(alias="status__in")]
    """List of status codes in the response. Values should be separated by a comma."""

    status_lt: Annotated[int, PropertyInfo(alias="status__lt")]
    """Status code in the response less than the specified value."""

    status_lte: Annotated[int, PropertyInfo(alias="status__lte")]
    """Status code in the response less than or equal to the specified value."""

    status_ne: Annotated[int, PropertyInfo(alias="status__ne")]
    """Status code in the response not equal to the specified value."""

    status_not_in: Annotated[str, PropertyInfo(alias="status__not_in")]
    """List of status codes not in the response.

    Values should be separated by a comma.
    """
