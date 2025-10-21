# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ...types.cdn import log_list_params, log_download_params
from ...pagination import SyncOffsetPageCdnLogs, AsyncOffsetPageCdnLogs
from ..._base_client import AsyncPaginator, make_request_options
from ...types.cdn.cdn_log_entry import Data

__all__ = ["LogsResource", "AsyncLogsResource"]


class LogsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LogsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return LogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LogsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return LogsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        from_: str,
        to: str,
        cache_status_eq: str | Omit = omit,
        cache_status_in: str | Omit = omit,
        cache_status_ne: str | Omit = omit,
        cache_status_not_in: str | Omit = omit,
        client_ip_eq: str | Omit = omit,
        client_ip_in: str | Omit = omit,
        client_ip_ne: str | Omit = omit,
        client_ip_not_in: str | Omit = omit,
        cname_contains: str | Omit = omit,
        cname_eq: str | Omit = omit,
        cname_in: str | Omit = omit,
        cname_ne: str | Omit = omit,
        cname_not_in: str | Omit = omit,
        datacenter_eq: str | Omit = omit,
        datacenter_in: str | Omit = omit,
        datacenter_ne: str | Omit = omit,
        datacenter_not_in: str | Omit = omit,
        fields: str | Omit = omit,
        limit: int | Omit = omit,
        method_eq: str | Omit = omit,
        method_in: str | Omit = omit,
        method_ne: str | Omit = omit,
        method_not_in: str | Omit = omit,
        offset: int | Omit = omit,
        ordering: str | Omit = omit,
        resource_id_eq: int | Omit = omit,
        resource_id_gt: int | Omit = omit,
        resource_id_gte: int | Omit = omit,
        resource_id_in: str | Omit = omit,
        resource_id_lt: int | Omit = omit,
        resource_id_lte: int | Omit = omit,
        resource_id_ne: int | Omit = omit,
        resource_id_not_in: str | Omit = omit,
        size_eq: int | Omit = omit,
        size_gt: int | Omit = omit,
        size_gte: int | Omit = omit,
        size_in: str | Omit = omit,
        size_lt: int | Omit = omit,
        size_lte: int | Omit = omit,
        size_ne: int | Omit = omit,
        size_not_in: str | Omit = omit,
        status_eq: int | Omit = omit,
        status_gt: int | Omit = omit,
        status_gte: int | Omit = omit,
        status_in: str | Omit = omit,
        status_lt: int | Omit = omit,
        status_lte: int | Omit = omit,
        status_ne: int | Omit = omit,
        status_not_in: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPageCdnLogs[Data]:
        """
        Get CDN logs for up to 3 days starting today.

        You can filter logs using query parameters by client IP, CDN resource, date,
        path and etc.

        To filter the CDN logs by 2xx status codes, use:

        - &`status__gte`=200&`status__lt`=300

        Args:
          from_: Start date and time of the requested time period (ISO 8601/RFC 3339 format,
              UTC.)

              Difference between "from" and "to" cannot exceed 6 hours.

              Examples:

              - &from=2021-06-14T00:00:00Z
              - &from=2021-06-14T00:00:00.000Z

          to: End date and time of the requested time period (ISO 8601/RFC 3339 format, UTC.)

              Difference between "from" and "to" cannot exceed 6 hours.

              Examples:

              - &to=2021-06-15T00:00:00Z
              - &to=2021-06-15T00:00:00.000Z

          cache_status_eq: Caching status. Possible values: 'MISS', 'BYPASS', 'EXPIRED', 'STALE',
              'PENDING', 'UPDATING', 'REVALIDATED', 'HIT', '-'.

          cache_status_in: List of caching statuses. Possible values: 'MISS', 'BYPASS', 'EXPIRED', 'STALE',
              'PENDING', 'UPDATING', 'REVALIDATED', 'HIT', '-'. Values should be separated by
              a comma.

          cache_status_ne: Caching status not equal to the specified value. Possible values: 'MISS',
              'BYPASS', 'EXPIRED', 'STALE', 'PENDING', 'UPDATING', 'REVALIDATED', 'HIT', '-'.

          cache_status_not_in:
              List of caching statuses not equal to the specified values. Possible values:
              'MISS', 'BYPASS', 'EXPIRED', 'STALE', 'PENDING', 'UPDATING', 'REVALIDATED',
              'HIT', '-'. Values should be separated by a comma.

          client_ip_eq: IP address of the client who sent the request.

          client_ip_in: List of IP addresses of the clients who sent the request.

          client_ip_ne: IP address of the client who did not send the request.

          client_ip_not_in: List of IP addresses of the clients who did not send the request.

          cname_contains: Part of the custom domain of the requested CDN resource. Minimum length is 3
              characters.

          cname_eq: Custom domain of the requested CDN resource.

          cname_in: List of custom domains of the requested CDN resource. Values should be separated
              by a comma.

          cname_ne: Custom domain of the requested CDN resource not equal to the specified value.

          cname_not_in: List of custom domains of the requested CDN resource not equal to the specified
              values. Values should be separated by a comma.

          datacenter_eq: Data center where request was processed.

          datacenter_in: List of data centers where request was processed. Values should be separated by
              a comma.

          datacenter_ne: Data center where request was not processed.

          datacenter_not_in: List of data centers where request was not processed. Values should be separated
              by a comma.

          fields: A comma-separated list of returned fields.

              Supported fields are presented in the responses section.

              Example:

              - &fields=timestamp,path,status

          limit: Maximum number of log records in the response.

          method_eq: Request HTTP method. Possible values: 'CONNECT', 'DELETE', 'GET', 'HEAD',
              'OPTIONS', 'PATCH', 'POST', 'PUT', 'TRACE'.

          method_in: Request HTTP method. Possible values: 'CONNECT', 'DELETE', 'GET', 'HEAD',
              'OPTIONS', 'PATCH', 'POST', 'PUT', 'TRACE'. Values should be separated by a
              comma.

          method_ne: Request HTTP method. Possible values: 'CONNECT', 'DELETE', 'GET', 'HEAD',
              'OPTIONS', 'PATCH', 'POST', 'PUT', 'TRACE'.

          method_not_in: Request HTTP method. Possible values: 'CONNECT', 'DELETE', 'GET', 'HEAD',
              'OPTIONS', 'PATCH', 'POST', 'PUT', 'TRACE'. Values should be separated by a
              comma.

          offset: Number of log records to skip starting from the beginning of the requested
              period.

          ordering: Sorting rules.

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

          resource_id_eq: ID of the requested CDN resource equal to the specified value.

          resource_id_gt: ID of the requested CDN resource greater than the specified value.

          resource_id_gte: ID of the requested CDN resource greater than or equal to the specified value.

          resource_id_in: List of IDs of the requested CDN resource. Values should be separated by a
              comma.

          resource_id_lt: ID of the requested CDN resource less than the specified value.

          resource_id_lte: ID of the requested CDN resource less than or equal to the specified value.

          resource_id_ne: ID of the requested CDN resource not equal to the specified value.

          resource_id_not_in: List of IDs of the requested CDN resource not equal to the specified values.
              Values should be separated by a comma.

          size_eq: Response size in bytes equal to the specified value.

          size_gt: Response size in bytes greater than the specified value.

          size_gte: Response size in bytes greater than or equal to the specified value.

          size_in: List of response sizes in bytes. Values should be separated by a comma.

          size_lt: Response size in bytes less than the specified value.

          size_lte: Response size in bytes less than or equal to the specified value.

          size_ne: Response size in bytes not equal to the specified value.

          size_not_in: List of response sizes in bytes not equal to the specified values. Values should
              be separated by

          status_eq: Status code in the response equal to the specified value.

          status_gt: Status code in the response greater than the specified value.

          status_gte: Status code in the response greater than or equal to the specified value.

          status_in: List of status codes in the response. Values should be separated by a comma.

          status_lt: Status code in the response less than the specified value.

          status_lte: Status code in the response less than or equal to the specified value.

          status_ne: Status code in the response not equal to the specified value.

          status_not_in: List of status codes not in the response. Values should be separated by a comma.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/cdn/advanced/v1/logs",
            page=SyncOffsetPageCdnLogs[Data],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                        "cache_status_eq": cache_status_eq,
                        "cache_status_in": cache_status_in,
                        "cache_status_ne": cache_status_ne,
                        "cache_status_not_in": cache_status_not_in,
                        "client_ip_eq": client_ip_eq,
                        "client_ip_in": client_ip_in,
                        "client_ip_ne": client_ip_ne,
                        "client_ip_not_in": client_ip_not_in,
                        "cname_contains": cname_contains,
                        "cname_eq": cname_eq,
                        "cname_in": cname_in,
                        "cname_ne": cname_ne,
                        "cname_not_in": cname_not_in,
                        "datacenter_eq": datacenter_eq,
                        "datacenter_in": datacenter_in,
                        "datacenter_ne": datacenter_ne,
                        "datacenter_not_in": datacenter_not_in,
                        "fields": fields,
                        "limit": limit,
                        "method_eq": method_eq,
                        "method_in": method_in,
                        "method_ne": method_ne,
                        "method_not_in": method_not_in,
                        "offset": offset,
                        "ordering": ordering,
                        "resource_id_eq": resource_id_eq,
                        "resource_id_gt": resource_id_gt,
                        "resource_id_gte": resource_id_gte,
                        "resource_id_in": resource_id_in,
                        "resource_id_lt": resource_id_lt,
                        "resource_id_lte": resource_id_lte,
                        "resource_id_ne": resource_id_ne,
                        "resource_id_not_in": resource_id_not_in,
                        "size_eq": size_eq,
                        "size_gt": size_gt,
                        "size_gte": size_gte,
                        "size_in": size_in,
                        "size_lt": size_lt,
                        "size_lte": size_lte,
                        "size_ne": size_ne,
                        "size_not_in": size_not_in,
                        "status_eq": status_eq,
                        "status_gt": status_gt,
                        "status_gte": status_gte,
                        "status_in": status_in,
                        "status_lt": status_lt,
                        "status_lte": status_lte,
                        "status_ne": status_ne,
                        "status_not_in": status_not_in,
                    },
                    log_list_params.LogListParams,
                ),
            ),
            model=Data,
        )

    def download(
        self,
        *,
        format: str,
        from_: str,
        to: str,
        cache_status_eq: str | Omit = omit,
        cache_status_in: str | Omit = omit,
        cache_status_ne: str | Omit = omit,
        cache_status_not_in: str | Omit = omit,
        client_ip_eq: str | Omit = omit,
        client_ip_in: str | Omit = omit,
        client_ip_ne: str | Omit = omit,
        client_ip_not_in: str | Omit = omit,
        cname_contains: str | Omit = omit,
        cname_eq: str | Omit = omit,
        cname_in: str | Omit = omit,
        cname_ne: str | Omit = omit,
        cname_not_in: str | Omit = omit,
        datacenter_eq: str | Omit = omit,
        datacenter_in: str | Omit = omit,
        datacenter_ne: str | Omit = omit,
        datacenter_not_in: str | Omit = omit,
        fields: str | Omit = omit,
        limit: int | Omit = omit,
        method_eq: str | Omit = omit,
        method_in: str | Omit = omit,
        method_ne: str | Omit = omit,
        method_not_in: str | Omit = omit,
        offset: int | Omit = omit,
        resource_id_eq: int | Omit = omit,
        resource_id_gt: int | Omit = omit,
        resource_id_gte: int | Omit = omit,
        resource_id_in: str | Omit = omit,
        resource_id_lt: int | Omit = omit,
        resource_id_lte: int | Omit = omit,
        resource_id_ne: int | Omit = omit,
        resource_id_not_in: str | Omit = omit,
        size_eq: int | Omit = omit,
        size_gt: int | Omit = omit,
        size_gte: int | Omit = omit,
        size_in: str | Omit = omit,
        size_lt: int | Omit = omit,
        size_lte: int | Omit = omit,
        size_ne: int | Omit = omit,
        size_not_in: str | Omit = omit,
        sort: str | Omit = omit,
        status_eq: int | Omit = omit,
        status_gt: int | Omit = omit,
        status_gte: int | Omit = omit,
        status_in: str | Omit = omit,
        status_lt: int | Omit = omit,
        status_lte: int | Omit = omit,
        status_ne: int | Omit = omit,
        status_not_in: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Download CDN logs for up to 3 days starting today.

        You can filter logs using query params by client IP, CDN resource, date, path
        and etc.

        Args:
          format: Output format.

              Possible values:

              - csv
              - tsv

          from_: Start date and time of the requested time period (ISO 8601/RFC 3339 format,
              UTC.)

              Difference between "from" and "to" cannot exceed 6 hours.

              Examples:

              - &from=2021-06-14T00:00:00Z
              - &from=2021-06-14T00:00:00.000Z

          to: End date and time of the requested time period (ISO 8601/RFC 3339 format, UTC.)

              Difference between "from" and "to" cannot exceed 6 hours.

              Examples:

              - &to=2021-06-15T00:00:00Z
              - &to=2021-06-15T00:00:00.000Z

          cache_status_eq: Caching status. Possible values: 'MISS', 'BYPASS', 'EXPIRED', 'STALE',
              'PENDING', 'UPDATING', 'REVALIDATED', 'HIT', '-'.

          cache_status_in: List of caching statuses. Possible values: 'MISS', 'BYPASS', 'EXPIRED', 'STALE',
              'PENDING', 'UPDATING', 'REVALIDATED', 'HIT', '-'. Values should be separated by
              a comma.

          cache_status_ne: Caching status not equal to the specified value. Possible values: 'MISS',
              'BYPASS', 'EXPIRED', 'STALE', 'PENDING', 'UPDATING', 'REVALIDATED', 'HIT', '-'.

          cache_status_not_in:
              List of caching statuses not equal to the specified values. Possible values:
              'MISS', 'BYPASS', 'EXPIRED', 'STALE', 'PENDING', 'UPDATING', 'REVALIDATED',
              'HIT', '-'. Values should be separated by a comma.

          client_ip_eq: IP address of the client who sent the request.

          client_ip_in: List of IP addresses of the clients who sent the request.

          client_ip_ne: IP address of the client who did not send the request.

          client_ip_not_in: List of IP addresses of the clients who did not send the request.

          cname_contains: Part of the custom domain of the requested CDN resource. Minimum length is 3
              characters.

          cname_eq: Custom domain of the requested CDN resource.

          cname_in: List of custom domains of the requested CDN resource. Values should be separated
              by a comma.

          cname_ne: Custom domain of the requested CDN resource not equal to the specified value.

          cname_not_in: List of custom domains of the requested CDN resource not equal to the specified
              values. Values should be separated by a comma.

          datacenter_eq: Data center where request was processed.

          datacenter_in: List of data centers where request was processed. Values should be separated by
              a comma.

          datacenter_ne: Data center where request was not processed.

          datacenter_not_in: List of data centers where request was not processed. Values should be separated
              by a comma.

          fields: A comma-separated list of returned fields.

              Supported fields are presented in the responses section.

              Example:

              - &fields=timestamp,path,status

          limit: Maximum number of log records in the response.

          method_eq: Request HTTP method. Possible values: 'CONNECT', 'DELETE', 'GET', 'HEAD',
              'OPTIONS', 'PATCH', 'POST', 'PUT', 'TRACE'.

          method_in: Request HTTP method. Possible values: 'CONNECT', 'DELETE', 'GET', 'HEAD',
              'OPTIONS', 'PATCH', 'POST', 'PUT', 'TRACE'. Values should be separated by a
              comma.

          method_ne: Request HTTP method. Possible values: 'CONNECT', 'DELETE', 'GET', 'HEAD',
              'OPTIONS', 'PATCH', 'POST', 'PUT', 'TRACE'.

          method_not_in: Request HTTP method. Possible values: 'CONNECT', 'DELETE', 'GET', 'HEAD',
              'OPTIONS', 'PATCH', 'POST', 'PUT', 'TRACE'. Values should be separated by a
              comma.

          offset: Number of log records to skip starting from the beginning of the requested
              period.

          resource_id_eq: ID of the requested CDN resource equal to the specified value.

          resource_id_gt: ID of the requested CDN resource greater than the specified value.

          resource_id_gte: ID of the requested CDN resource greater than or equal to the specified value.

          resource_id_in: List of IDs of the requested CDN resource. Values should be separated by a
              comma.

          resource_id_lt: ID of the requested CDN resource less than the specified value.

          resource_id_lte: ID of the requested CDN resource less than or equal to the specified value.

          resource_id_ne: ID of the requested CDN resource not equal to the specified value.

          resource_id_not_in: List of IDs of the requested CDN resource not equal to the specified values.
              Values should be separated by a comma.

          size_eq: Response size in bytes equal to the specified value.

          size_gt: Response size in bytes greater than the specified value.

          size_gte: Response size in bytes greater than or equal to the specified value.

          size_in: List of response sizes in bytes. Values should be separated by a comma.

          size_lt: Response size in bytes less than the specified value.

          size_lte: Response size in bytes less than or equal to the specified value.

          size_ne: Response size in bytes not equal to the specified value.

          size_not_in: List of response sizes in bytes not equal to the specified values. Values should
              be separated by

          sort: Sorting rules.

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

              May include multiple values separated by a comma.

              Example:

              - &sort=-timestamp,status

          status_eq: Status code in the response equal to the specified value.

          status_gt: Status code in the response greater than the specified value.

          status_gte: Status code in the response greater than or equal to the specified value.

          status_in: List of status codes in the response. Values should be separated by a comma.

          status_lt: Status code in the response less than the specified value.

          status_lte: Status code in the response less than or equal to the specified value.

          status_ne: Status code in the response not equal to the specified value.

          status_not_in: List of status codes not in the response. Values should be separated by a comma.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/zip", **(extra_headers or {})}
        return self._get(
            "/cdn/advanced/v1/logs/download",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "format": format,
                        "from_": from_,
                        "to": to,
                        "cache_status_eq": cache_status_eq,
                        "cache_status_in": cache_status_in,
                        "cache_status_ne": cache_status_ne,
                        "cache_status_not_in": cache_status_not_in,
                        "client_ip_eq": client_ip_eq,
                        "client_ip_in": client_ip_in,
                        "client_ip_ne": client_ip_ne,
                        "client_ip_not_in": client_ip_not_in,
                        "cname_contains": cname_contains,
                        "cname_eq": cname_eq,
                        "cname_in": cname_in,
                        "cname_ne": cname_ne,
                        "cname_not_in": cname_not_in,
                        "datacenter_eq": datacenter_eq,
                        "datacenter_in": datacenter_in,
                        "datacenter_ne": datacenter_ne,
                        "datacenter_not_in": datacenter_not_in,
                        "fields": fields,
                        "limit": limit,
                        "method_eq": method_eq,
                        "method_in": method_in,
                        "method_ne": method_ne,
                        "method_not_in": method_not_in,
                        "offset": offset,
                        "resource_id_eq": resource_id_eq,
                        "resource_id_gt": resource_id_gt,
                        "resource_id_gte": resource_id_gte,
                        "resource_id_in": resource_id_in,
                        "resource_id_lt": resource_id_lt,
                        "resource_id_lte": resource_id_lte,
                        "resource_id_ne": resource_id_ne,
                        "resource_id_not_in": resource_id_not_in,
                        "size_eq": size_eq,
                        "size_gt": size_gt,
                        "size_gte": size_gte,
                        "size_in": size_in,
                        "size_lt": size_lt,
                        "size_lte": size_lte,
                        "size_ne": size_ne,
                        "size_not_in": size_not_in,
                        "sort": sort,
                        "status_eq": status_eq,
                        "status_gt": status_gt,
                        "status_gte": status_gte,
                        "status_in": status_in,
                        "status_lt": status_lt,
                        "status_lte": status_lte,
                        "status_ne": status_ne,
                        "status_not_in": status_not_in,
                    },
                    log_download_params.LogDownloadParams,
                ),
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncLogsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLogsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLogsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncLogsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        from_: str,
        to: str,
        cache_status_eq: str | Omit = omit,
        cache_status_in: str | Omit = omit,
        cache_status_ne: str | Omit = omit,
        cache_status_not_in: str | Omit = omit,
        client_ip_eq: str | Omit = omit,
        client_ip_in: str | Omit = omit,
        client_ip_ne: str | Omit = omit,
        client_ip_not_in: str | Omit = omit,
        cname_contains: str | Omit = omit,
        cname_eq: str | Omit = omit,
        cname_in: str | Omit = omit,
        cname_ne: str | Omit = omit,
        cname_not_in: str | Omit = omit,
        datacenter_eq: str | Omit = omit,
        datacenter_in: str | Omit = omit,
        datacenter_ne: str | Omit = omit,
        datacenter_not_in: str | Omit = omit,
        fields: str | Omit = omit,
        limit: int | Omit = omit,
        method_eq: str | Omit = omit,
        method_in: str | Omit = omit,
        method_ne: str | Omit = omit,
        method_not_in: str | Omit = omit,
        offset: int | Omit = omit,
        ordering: str | Omit = omit,
        resource_id_eq: int | Omit = omit,
        resource_id_gt: int | Omit = omit,
        resource_id_gte: int | Omit = omit,
        resource_id_in: str | Omit = omit,
        resource_id_lt: int | Omit = omit,
        resource_id_lte: int | Omit = omit,
        resource_id_ne: int | Omit = omit,
        resource_id_not_in: str | Omit = omit,
        size_eq: int | Omit = omit,
        size_gt: int | Omit = omit,
        size_gte: int | Omit = omit,
        size_in: str | Omit = omit,
        size_lt: int | Omit = omit,
        size_lte: int | Omit = omit,
        size_ne: int | Omit = omit,
        size_not_in: str | Omit = omit,
        status_eq: int | Omit = omit,
        status_gt: int | Omit = omit,
        status_gte: int | Omit = omit,
        status_in: str | Omit = omit,
        status_lt: int | Omit = omit,
        status_lte: int | Omit = omit,
        status_ne: int | Omit = omit,
        status_not_in: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Data, AsyncOffsetPageCdnLogs[Data]]:
        """
        Get CDN logs for up to 3 days starting today.

        You can filter logs using query parameters by client IP, CDN resource, date,
        path and etc.

        To filter the CDN logs by 2xx status codes, use:

        - &`status__gte`=200&`status__lt`=300

        Args:
          from_: Start date and time of the requested time period (ISO 8601/RFC 3339 format,
              UTC.)

              Difference between "from" and "to" cannot exceed 6 hours.

              Examples:

              - &from=2021-06-14T00:00:00Z
              - &from=2021-06-14T00:00:00.000Z

          to: End date and time of the requested time period (ISO 8601/RFC 3339 format, UTC.)

              Difference between "from" and "to" cannot exceed 6 hours.

              Examples:

              - &to=2021-06-15T00:00:00Z
              - &to=2021-06-15T00:00:00.000Z

          cache_status_eq: Caching status. Possible values: 'MISS', 'BYPASS', 'EXPIRED', 'STALE',
              'PENDING', 'UPDATING', 'REVALIDATED', 'HIT', '-'.

          cache_status_in: List of caching statuses. Possible values: 'MISS', 'BYPASS', 'EXPIRED', 'STALE',
              'PENDING', 'UPDATING', 'REVALIDATED', 'HIT', '-'. Values should be separated by
              a comma.

          cache_status_ne: Caching status not equal to the specified value. Possible values: 'MISS',
              'BYPASS', 'EXPIRED', 'STALE', 'PENDING', 'UPDATING', 'REVALIDATED', 'HIT', '-'.

          cache_status_not_in:
              List of caching statuses not equal to the specified values. Possible values:
              'MISS', 'BYPASS', 'EXPIRED', 'STALE', 'PENDING', 'UPDATING', 'REVALIDATED',
              'HIT', '-'. Values should be separated by a comma.

          client_ip_eq: IP address of the client who sent the request.

          client_ip_in: List of IP addresses of the clients who sent the request.

          client_ip_ne: IP address of the client who did not send the request.

          client_ip_not_in: List of IP addresses of the clients who did not send the request.

          cname_contains: Part of the custom domain of the requested CDN resource. Minimum length is 3
              characters.

          cname_eq: Custom domain of the requested CDN resource.

          cname_in: List of custom domains of the requested CDN resource. Values should be separated
              by a comma.

          cname_ne: Custom domain of the requested CDN resource not equal to the specified value.

          cname_not_in: List of custom domains of the requested CDN resource not equal to the specified
              values. Values should be separated by a comma.

          datacenter_eq: Data center where request was processed.

          datacenter_in: List of data centers where request was processed. Values should be separated by
              a comma.

          datacenter_ne: Data center where request was not processed.

          datacenter_not_in: List of data centers where request was not processed. Values should be separated
              by a comma.

          fields: A comma-separated list of returned fields.

              Supported fields are presented in the responses section.

              Example:

              - &fields=timestamp,path,status

          limit: Maximum number of log records in the response.

          method_eq: Request HTTP method. Possible values: 'CONNECT', 'DELETE', 'GET', 'HEAD',
              'OPTIONS', 'PATCH', 'POST', 'PUT', 'TRACE'.

          method_in: Request HTTP method. Possible values: 'CONNECT', 'DELETE', 'GET', 'HEAD',
              'OPTIONS', 'PATCH', 'POST', 'PUT', 'TRACE'. Values should be separated by a
              comma.

          method_ne: Request HTTP method. Possible values: 'CONNECT', 'DELETE', 'GET', 'HEAD',
              'OPTIONS', 'PATCH', 'POST', 'PUT', 'TRACE'.

          method_not_in: Request HTTP method. Possible values: 'CONNECT', 'DELETE', 'GET', 'HEAD',
              'OPTIONS', 'PATCH', 'POST', 'PUT', 'TRACE'. Values should be separated by a
              comma.

          offset: Number of log records to skip starting from the beginning of the requested
              period.

          ordering: Sorting rules.

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

          resource_id_eq: ID of the requested CDN resource equal to the specified value.

          resource_id_gt: ID of the requested CDN resource greater than the specified value.

          resource_id_gte: ID of the requested CDN resource greater than or equal to the specified value.

          resource_id_in: List of IDs of the requested CDN resource. Values should be separated by a
              comma.

          resource_id_lt: ID of the requested CDN resource less than the specified value.

          resource_id_lte: ID of the requested CDN resource less than or equal to the specified value.

          resource_id_ne: ID of the requested CDN resource not equal to the specified value.

          resource_id_not_in: List of IDs of the requested CDN resource not equal to the specified values.
              Values should be separated by a comma.

          size_eq: Response size in bytes equal to the specified value.

          size_gt: Response size in bytes greater than the specified value.

          size_gte: Response size in bytes greater than or equal to the specified value.

          size_in: List of response sizes in bytes. Values should be separated by a comma.

          size_lt: Response size in bytes less than the specified value.

          size_lte: Response size in bytes less than or equal to the specified value.

          size_ne: Response size in bytes not equal to the specified value.

          size_not_in: List of response sizes in bytes not equal to the specified values. Values should
              be separated by

          status_eq: Status code in the response equal to the specified value.

          status_gt: Status code in the response greater than the specified value.

          status_gte: Status code in the response greater than or equal to the specified value.

          status_in: List of status codes in the response. Values should be separated by a comma.

          status_lt: Status code in the response less than the specified value.

          status_lte: Status code in the response less than or equal to the specified value.

          status_ne: Status code in the response not equal to the specified value.

          status_not_in: List of status codes not in the response. Values should be separated by a comma.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/cdn/advanced/v1/logs",
            page=AsyncOffsetPageCdnLogs[Data],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                        "cache_status_eq": cache_status_eq,
                        "cache_status_in": cache_status_in,
                        "cache_status_ne": cache_status_ne,
                        "cache_status_not_in": cache_status_not_in,
                        "client_ip_eq": client_ip_eq,
                        "client_ip_in": client_ip_in,
                        "client_ip_ne": client_ip_ne,
                        "client_ip_not_in": client_ip_not_in,
                        "cname_contains": cname_contains,
                        "cname_eq": cname_eq,
                        "cname_in": cname_in,
                        "cname_ne": cname_ne,
                        "cname_not_in": cname_not_in,
                        "datacenter_eq": datacenter_eq,
                        "datacenter_in": datacenter_in,
                        "datacenter_ne": datacenter_ne,
                        "datacenter_not_in": datacenter_not_in,
                        "fields": fields,
                        "limit": limit,
                        "method_eq": method_eq,
                        "method_in": method_in,
                        "method_ne": method_ne,
                        "method_not_in": method_not_in,
                        "offset": offset,
                        "ordering": ordering,
                        "resource_id_eq": resource_id_eq,
                        "resource_id_gt": resource_id_gt,
                        "resource_id_gte": resource_id_gte,
                        "resource_id_in": resource_id_in,
                        "resource_id_lt": resource_id_lt,
                        "resource_id_lte": resource_id_lte,
                        "resource_id_ne": resource_id_ne,
                        "resource_id_not_in": resource_id_not_in,
                        "size_eq": size_eq,
                        "size_gt": size_gt,
                        "size_gte": size_gte,
                        "size_in": size_in,
                        "size_lt": size_lt,
                        "size_lte": size_lte,
                        "size_ne": size_ne,
                        "size_not_in": size_not_in,
                        "status_eq": status_eq,
                        "status_gt": status_gt,
                        "status_gte": status_gte,
                        "status_in": status_in,
                        "status_lt": status_lt,
                        "status_lte": status_lte,
                        "status_ne": status_ne,
                        "status_not_in": status_not_in,
                    },
                    log_list_params.LogListParams,
                ),
            ),
            model=Data,
        )

    async def download(
        self,
        *,
        format: str,
        from_: str,
        to: str,
        cache_status_eq: str | Omit = omit,
        cache_status_in: str | Omit = omit,
        cache_status_ne: str | Omit = omit,
        cache_status_not_in: str | Omit = omit,
        client_ip_eq: str | Omit = omit,
        client_ip_in: str | Omit = omit,
        client_ip_ne: str | Omit = omit,
        client_ip_not_in: str | Omit = omit,
        cname_contains: str | Omit = omit,
        cname_eq: str | Omit = omit,
        cname_in: str | Omit = omit,
        cname_ne: str | Omit = omit,
        cname_not_in: str | Omit = omit,
        datacenter_eq: str | Omit = omit,
        datacenter_in: str | Omit = omit,
        datacenter_ne: str | Omit = omit,
        datacenter_not_in: str | Omit = omit,
        fields: str | Omit = omit,
        limit: int | Omit = omit,
        method_eq: str | Omit = omit,
        method_in: str | Omit = omit,
        method_ne: str | Omit = omit,
        method_not_in: str | Omit = omit,
        offset: int | Omit = omit,
        resource_id_eq: int | Omit = omit,
        resource_id_gt: int | Omit = omit,
        resource_id_gte: int | Omit = omit,
        resource_id_in: str | Omit = omit,
        resource_id_lt: int | Omit = omit,
        resource_id_lte: int | Omit = omit,
        resource_id_ne: int | Omit = omit,
        resource_id_not_in: str | Omit = omit,
        size_eq: int | Omit = omit,
        size_gt: int | Omit = omit,
        size_gte: int | Omit = omit,
        size_in: str | Omit = omit,
        size_lt: int | Omit = omit,
        size_lte: int | Omit = omit,
        size_ne: int | Omit = omit,
        size_not_in: str | Omit = omit,
        sort: str | Omit = omit,
        status_eq: int | Omit = omit,
        status_gt: int | Omit = omit,
        status_gte: int | Omit = omit,
        status_in: str | Omit = omit,
        status_lt: int | Omit = omit,
        status_lte: int | Omit = omit,
        status_ne: int | Omit = omit,
        status_not_in: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Download CDN logs for up to 3 days starting today.

        You can filter logs using query params by client IP, CDN resource, date, path
        and etc.

        Args:
          format: Output format.

              Possible values:

              - csv
              - tsv

          from_: Start date and time of the requested time period (ISO 8601/RFC 3339 format,
              UTC.)

              Difference between "from" and "to" cannot exceed 6 hours.

              Examples:

              - &from=2021-06-14T00:00:00Z
              - &from=2021-06-14T00:00:00.000Z

          to: End date and time of the requested time period (ISO 8601/RFC 3339 format, UTC.)

              Difference between "from" and "to" cannot exceed 6 hours.

              Examples:

              - &to=2021-06-15T00:00:00Z
              - &to=2021-06-15T00:00:00.000Z

          cache_status_eq: Caching status. Possible values: 'MISS', 'BYPASS', 'EXPIRED', 'STALE',
              'PENDING', 'UPDATING', 'REVALIDATED', 'HIT', '-'.

          cache_status_in: List of caching statuses. Possible values: 'MISS', 'BYPASS', 'EXPIRED', 'STALE',
              'PENDING', 'UPDATING', 'REVALIDATED', 'HIT', '-'. Values should be separated by
              a comma.

          cache_status_ne: Caching status not equal to the specified value. Possible values: 'MISS',
              'BYPASS', 'EXPIRED', 'STALE', 'PENDING', 'UPDATING', 'REVALIDATED', 'HIT', '-'.

          cache_status_not_in:
              List of caching statuses not equal to the specified values. Possible values:
              'MISS', 'BYPASS', 'EXPIRED', 'STALE', 'PENDING', 'UPDATING', 'REVALIDATED',
              'HIT', '-'. Values should be separated by a comma.

          client_ip_eq: IP address of the client who sent the request.

          client_ip_in: List of IP addresses of the clients who sent the request.

          client_ip_ne: IP address of the client who did not send the request.

          client_ip_not_in: List of IP addresses of the clients who did not send the request.

          cname_contains: Part of the custom domain of the requested CDN resource. Minimum length is 3
              characters.

          cname_eq: Custom domain of the requested CDN resource.

          cname_in: List of custom domains of the requested CDN resource. Values should be separated
              by a comma.

          cname_ne: Custom domain of the requested CDN resource not equal to the specified value.

          cname_not_in: List of custom domains of the requested CDN resource not equal to the specified
              values. Values should be separated by a comma.

          datacenter_eq: Data center where request was processed.

          datacenter_in: List of data centers where request was processed. Values should be separated by
              a comma.

          datacenter_ne: Data center where request was not processed.

          datacenter_not_in: List of data centers where request was not processed. Values should be separated
              by a comma.

          fields: A comma-separated list of returned fields.

              Supported fields are presented in the responses section.

              Example:

              - &fields=timestamp,path,status

          limit: Maximum number of log records in the response.

          method_eq: Request HTTP method. Possible values: 'CONNECT', 'DELETE', 'GET', 'HEAD',
              'OPTIONS', 'PATCH', 'POST', 'PUT', 'TRACE'.

          method_in: Request HTTP method. Possible values: 'CONNECT', 'DELETE', 'GET', 'HEAD',
              'OPTIONS', 'PATCH', 'POST', 'PUT', 'TRACE'. Values should be separated by a
              comma.

          method_ne: Request HTTP method. Possible values: 'CONNECT', 'DELETE', 'GET', 'HEAD',
              'OPTIONS', 'PATCH', 'POST', 'PUT', 'TRACE'.

          method_not_in: Request HTTP method. Possible values: 'CONNECT', 'DELETE', 'GET', 'HEAD',
              'OPTIONS', 'PATCH', 'POST', 'PUT', 'TRACE'. Values should be separated by a
              comma.

          offset: Number of log records to skip starting from the beginning of the requested
              period.

          resource_id_eq: ID of the requested CDN resource equal to the specified value.

          resource_id_gt: ID of the requested CDN resource greater than the specified value.

          resource_id_gte: ID of the requested CDN resource greater than or equal to the specified value.

          resource_id_in: List of IDs of the requested CDN resource. Values should be separated by a
              comma.

          resource_id_lt: ID of the requested CDN resource less than the specified value.

          resource_id_lte: ID of the requested CDN resource less than or equal to the specified value.

          resource_id_ne: ID of the requested CDN resource not equal to the specified value.

          resource_id_not_in: List of IDs of the requested CDN resource not equal to the specified values.
              Values should be separated by a comma.

          size_eq: Response size in bytes equal to the specified value.

          size_gt: Response size in bytes greater than the specified value.

          size_gte: Response size in bytes greater than or equal to the specified value.

          size_in: List of response sizes in bytes. Values should be separated by a comma.

          size_lt: Response size in bytes less than the specified value.

          size_lte: Response size in bytes less than or equal to the specified value.

          size_ne: Response size in bytes not equal to the specified value.

          size_not_in: List of response sizes in bytes not equal to the specified values. Values should
              be separated by

          sort: Sorting rules.

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

              May include multiple values separated by a comma.

              Example:

              - &sort=-timestamp,status

          status_eq: Status code in the response equal to the specified value.

          status_gt: Status code in the response greater than the specified value.

          status_gte: Status code in the response greater than or equal to the specified value.

          status_in: List of status codes in the response. Values should be separated by a comma.

          status_lt: Status code in the response less than the specified value.

          status_lte: Status code in the response less than or equal to the specified value.

          status_ne: Status code in the response not equal to the specified value.

          status_not_in: List of status codes not in the response. Values should be separated by a comma.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/zip", **(extra_headers or {})}
        return await self._get(
            "/cdn/advanced/v1/logs/download",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "format": format,
                        "from_": from_,
                        "to": to,
                        "cache_status_eq": cache_status_eq,
                        "cache_status_in": cache_status_in,
                        "cache_status_ne": cache_status_ne,
                        "cache_status_not_in": cache_status_not_in,
                        "client_ip_eq": client_ip_eq,
                        "client_ip_in": client_ip_in,
                        "client_ip_ne": client_ip_ne,
                        "client_ip_not_in": client_ip_not_in,
                        "cname_contains": cname_contains,
                        "cname_eq": cname_eq,
                        "cname_in": cname_in,
                        "cname_ne": cname_ne,
                        "cname_not_in": cname_not_in,
                        "datacenter_eq": datacenter_eq,
                        "datacenter_in": datacenter_in,
                        "datacenter_ne": datacenter_ne,
                        "datacenter_not_in": datacenter_not_in,
                        "fields": fields,
                        "limit": limit,
                        "method_eq": method_eq,
                        "method_in": method_in,
                        "method_ne": method_ne,
                        "method_not_in": method_not_in,
                        "offset": offset,
                        "resource_id_eq": resource_id_eq,
                        "resource_id_gt": resource_id_gt,
                        "resource_id_gte": resource_id_gte,
                        "resource_id_in": resource_id_in,
                        "resource_id_lt": resource_id_lt,
                        "resource_id_lte": resource_id_lte,
                        "resource_id_ne": resource_id_ne,
                        "resource_id_not_in": resource_id_not_in,
                        "size_eq": size_eq,
                        "size_gt": size_gt,
                        "size_gte": size_gte,
                        "size_in": size_in,
                        "size_lt": size_lt,
                        "size_lte": size_lte,
                        "size_ne": size_ne,
                        "size_not_in": size_not_in,
                        "sort": sort,
                        "status_eq": status_eq,
                        "status_gt": status_gt,
                        "status_gte": status_gte,
                        "status_in": status_in,
                        "status_lt": status_lt,
                        "status_lte": status_lte,
                        "status_ne": status_ne,
                        "status_not_in": status_not_in,
                    },
                    log_download_params.LogDownloadParams,
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class LogsResourceWithRawResponse:
    def __init__(self, logs: LogsResource) -> None:
        self._logs = logs

        self.list = to_raw_response_wrapper(
            logs.list,
        )
        self.download = to_custom_raw_response_wrapper(
            logs.download,
            BinaryAPIResponse,
        )


class AsyncLogsResourceWithRawResponse:
    def __init__(self, logs: AsyncLogsResource) -> None:
        self._logs = logs

        self.list = async_to_raw_response_wrapper(
            logs.list,
        )
        self.download = async_to_custom_raw_response_wrapper(
            logs.download,
            AsyncBinaryAPIResponse,
        )


class LogsResourceWithStreamingResponse:
    def __init__(self, logs: LogsResource) -> None:
        self._logs = logs

        self.list = to_streamed_response_wrapper(
            logs.list,
        )
        self.download = to_custom_streamed_response_wrapper(
            logs.download,
            StreamedBinaryAPIResponse,
        )


class AsyncLogsResourceWithStreamingResponse:
    def __init__(self, logs: AsyncLogsResource) -> None:
        self._logs = logs

        self.list = async_to_streamed_response_wrapper(
            logs.list,
        )
        self.download = async_to_custom_streamed_response_wrapper(
            logs.download,
            AsyncStreamedBinaryAPIResponse,
        )
