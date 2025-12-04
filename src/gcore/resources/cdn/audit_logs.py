# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.cdn import audit_log_list_params
from ...pagination import SyncOffsetPage, AsyncOffsetPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.cdn.cdn_audit_log_entry import CdnAuditLogEntry

__all__ = ["AuditLogsResource", "AsyncAuditLogsResource"]


class AuditLogsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuditLogsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AuditLogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuditLogsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AuditLogsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        client_id: int | Omit = omit,
        limit: int | Omit = omit,
        max_requested_at: str | Omit = omit,
        method: str | Omit = omit,
        min_requested_at: str | Omit = omit,
        offset: int | Omit = omit,
        path: str | Omit = omit,
        remote_ip_address: str | Omit = omit,
        status_code: int | Omit = omit,
        token_id: int | Omit = omit,
        user_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[CdnAuditLogEntry]:
        """
        Get information about all CDN activity logs records.

        Args:
          client_id: Client ID.

          limit: Maximum number of items in response.

          max_requested_at: End of the requested time period (ISO 8601/RFC 3339 format, UTC.)

              You can specify a date with a time separated by a space, or just a date.

              Examples:

              - &`max_requested_at`=2021-05-05 12:00:00
              - &`max_requested_at`=2021-05-05

          method: HTTP method type of requests.

              Use upper case only.

              Example:

              - ?method=DELETE

          min_requested_at: Beginning of the requested time period (ISO 8601/RFC 3339 format, UTC.)

              You can specify a date with a time separated by a space, or just a date.

              Examples:

              - &`min_requested_at`=2021-05-05 12:00:00
              - &`min_requested_at`=2021-05-05

          offset: Offset relative to the beginning of activity logs.

          path: Exact URL path.

          remote_ip_address: Exact IP address from which requests are sent.

          status_code: Status code returned in the response.

              Specify the first numbers of a status code to get requests for a group of status
              codes.

              To filter the activity logs by 4xx codes, use:

              - &`status_code`=4 -

          token_id: Permanent API token ID. Requests made with this token should be displayed.

          user_id: User ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/cdn/activity_log/requests",
            page=SyncOffsetPage[CdnAuditLogEntry],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "client_id": client_id,
                        "limit": limit,
                        "max_requested_at": max_requested_at,
                        "method": method,
                        "min_requested_at": min_requested_at,
                        "offset": offset,
                        "path": path,
                        "remote_ip_address": remote_ip_address,
                        "status_code": status_code,
                        "token_id": token_id,
                        "user_id": user_id,
                    },
                    audit_log_list_params.AuditLogListParams,
                ),
            ),
            model=CdnAuditLogEntry,
        )

    def get(
        self,
        log_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CdnAuditLogEntry:
        """
        Get information about CDN activity logs record.

        Args:
          log_id: Activity logs record ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/cdn/activity_log/requests/{log_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CdnAuditLogEntry,
        )


class AsyncAuditLogsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAuditLogsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAuditLogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuditLogsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncAuditLogsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        client_id: int | Omit = omit,
        limit: int | Omit = omit,
        max_requested_at: str | Omit = omit,
        method: str | Omit = omit,
        min_requested_at: str | Omit = omit,
        offset: int | Omit = omit,
        path: str | Omit = omit,
        remote_ip_address: str | Omit = omit,
        status_code: int | Omit = omit,
        token_id: int | Omit = omit,
        user_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CdnAuditLogEntry, AsyncOffsetPage[CdnAuditLogEntry]]:
        """
        Get information about all CDN activity logs records.

        Args:
          client_id: Client ID.

          limit: Maximum number of items in response.

          max_requested_at: End of the requested time period (ISO 8601/RFC 3339 format, UTC.)

              You can specify a date with a time separated by a space, or just a date.

              Examples:

              - &`max_requested_at`=2021-05-05 12:00:00
              - &`max_requested_at`=2021-05-05

          method: HTTP method type of requests.

              Use upper case only.

              Example:

              - ?method=DELETE

          min_requested_at: Beginning of the requested time period (ISO 8601/RFC 3339 format, UTC.)

              You can specify a date with a time separated by a space, or just a date.

              Examples:

              - &`min_requested_at`=2021-05-05 12:00:00
              - &`min_requested_at`=2021-05-05

          offset: Offset relative to the beginning of activity logs.

          path: Exact URL path.

          remote_ip_address: Exact IP address from which requests are sent.

          status_code: Status code returned in the response.

              Specify the first numbers of a status code to get requests for a group of status
              codes.

              To filter the activity logs by 4xx codes, use:

              - &`status_code`=4 -

          token_id: Permanent API token ID. Requests made with this token should be displayed.

          user_id: User ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/cdn/activity_log/requests",
            page=AsyncOffsetPage[CdnAuditLogEntry],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "client_id": client_id,
                        "limit": limit,
                        "max_requested_at": max_requested_at,
                        "method": method,
                        "min_requested_at": min_requested_at,
                        "offset": offset,
                        "path": path,
                        "remote_ip_address": remote_ip_address,
                        "status_code": status_code,
                        "token_id": token_id,
                        "user_id": user_id,
                    },
                    audit_log_list_params.AuditLogListParams,
                ),
            ),
            model=CdnAuditLogEntry,
        )

    async def get(
        self,
        log_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CdnAuditLogEntry:
        """
        Get information about CDN activity logs record.

        Args:
          log_id: Activity logs record ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/cdn/activity_log/requests/{log_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CdnAuditLogEntry,
        )


class AuditLogsResourceWithRawResponse:
    def __init__(self, audit_logs: AuditLogsResource) -> None:
        self._audit_logs = audit_logs

        self.list = to_raw_response_wrapper(
            audit_logs.list,
        )
        self.get = to_raw_response_wrapper(
            audit_logs.get,
        )


class AsyncAuditLogsResourceWithRawResponse:
    def __init__(self, audit_logs: AsyncAuditLogsResource) -> None:
        self._audit_logs = audit_logs

        self.list = async_to_raw_response_wrapper(
            audit_logs.list,
        )
        self.get = async_to_raw_response_wrapper(
            audit_logs.get,
        )


class AuditLogsResourceWithStreamingResponse:
    def __init__(self, audit_logs: AuditLogsResource) -> None:
        self._audit_logs = audit_logs

        self.list = to_streamed_response_wrapper(
            audit_logs.list,
        )
        self.get = to_streamed_response_wrapper(
            audit_logs.get,
        )


class AsyncAuditLogsResourceWithStreamingResponse:
    def __init__(self, audit_logs: AsyncAuditLogsResource) -> None:
        self._audit_logs = audit_logs

        self.list = async_to_streamed_response_wrapper(
            audit_logs.list,
        )
        self.get = async_to_streamed_response_wrapper(
            audit_logs.get,
        )
