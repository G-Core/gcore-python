# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncOffsetPageFastedgeAppLogs, AsyncOffsetPageFastedgeAppLogs
from ...._base_client import AsyncPaginator, make_request_options
from ....types.fastedge.apps import log_list_params
from ....types.fastedge.apps.log import Log

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
        id: int,
        *,
        client_ip: str | Omit = omit,
        edge: str | Omit = omit,
        from_: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        search: str | Omit = omit,
        sort: Literal["desc", "asc"] | Omit = omit,
        to: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPageFastedgeAppLogs[Log]:
        """
        List logs for the app

        Args:
          client_ip: Search by client IP

          edge: Edge name

          from_: Reporting period start time, RFC3339 format. Default 1 hour ago.

          limit: Limit for pagination

          offset: Offset for pagination

          search: Search string

          sort: Sort order (default desc)

          to: Reporting period end time, RFC3339 format. Default current time in UTC.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            f"/fastedge/v1/apps/{id}/logs",
            page=SyncOffsetPageFastedgeAppLogs[Log],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "client_ip": client_ip,
                        "edge": edge,
                        "from_": from_,
                        "limit": limit,
                        "offset": offset,
                        "search": search,
                        "sort": sort,
                        "to": to,
                    },
                    log_list_params.LogListParams,
                ),
            ),
            model=Log,
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
        id: int,
        *,
        client_ip: str | Omit = omit,
        edge: str | Omit = omit,
        from_: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        search: str | Omit = omit,
        sort: Literal["desc", "asc"] | Omit = omit,
        to: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Log, AsyncOffsetPageFastedgeAppLogs[Log]]:
        """
        List logs for the app

        Args:
          client_ip: Search by client IP

          edge: Edge name

          from_: Reporting period start time, RFC3339 format. Default 1 hour ago.

          limit: Limit for pagination

          offset: Offset for pagination

          search: Search string

          sort: Sort order (default desc)

          to: Reporting period end time, RFC3339 format. Default current time in UTC.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            f"/fastedge/v1/apps/{id}/logs",
            page=AsyncOffsetPageFastedgeAppLogs[Log],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "client_ip": client_ip,
                        "edge": edge,
                        "from_": from_,
                        "limit": limit,
                        "offset": offset,
                        "search": search,
                        "sort": sort,
                        "to": to,
                    },
                    log_list_params.LogListParams,
                ),
            ),
            model=Log,
        )


class LogsResourceWithRawResponse:
    def __init__(self, logs: LogsResource) -> None:
        self._logs = logs

        self.list = to_raw_response_wrapper(
            logs.list,
        )


class AsyncLogsResourceWithRawResponse:
    def __init__(self, logs: AsyncLogsResource) -> None:
        self._logs = logs

        self.list = async_to_raw_response_wrapper(
            logs.list,
        )


class LogsResourceWithStreamingResponse:
    def __init__(self, logs: LogsResource) -> None:
        self._logs = logs

        self.list = to_streamed_response_wrapper(
            logs.list,
        )


class AsyncLogsResourceWithStreamingResponse:
    def __init__(self, logs: AsyncLogsResource) -> None:
        self._logs = logs

        self.list = async_to_streamed_response_wrapper(
            logs.list,
        )
