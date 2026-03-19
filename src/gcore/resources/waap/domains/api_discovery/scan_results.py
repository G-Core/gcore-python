# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import path_template, maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .....pagination import SyncOffsetPage, AsyncOffsetPage
from ....._base_client import AsyncPaginator, make_request_options
from .....types.waap.domains.api_discovery import scan_result_list_params
from .....types.waap.domains.api_discovery.waap_api_scan_result import WaapAPIScanResult

__all__ = ["ScanResultsResource", "AsyncScanResultsResource"]


class ScanResultsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ScanResultsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return ScanResultsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScanResultsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return ScanResultsResourceWithStreamingResponse(self)

    def list(
        self,
        domain_id: int,
        *,
        limit: int | Omit = omit,
        message: Optional[str] | Omit = omit,
        offset: int | Omit = omit,
        ordering: Literal[
            "id",
            "type",
            "start_time",
            "end_time",
            "status",
            "message",
            "-id",
            "-type",
            "-start_time",
            "-end_time",
            "-status",
            "-message",
        ]
        | Omit = omit,
        status: Optional[Literal["SUCCESS", "FAILURE", "IN_PROGRESS"]] | Omit = omit,
        type: Optional[Literal["TRAFFIC_SCAN", "API_DESCRIPTION_FILE_SCAN"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[WaapAPIScanResult]:
        """
        Get Scan Results

        Args:
          domain_id: The domain ID

          limit: Number of items to return

          message: Filter by the message of the scan. Supports '\\**' as a wildcard character

          offset: Number of items to skip

          ordering: Sort the response by given field.

          status: Filter by the status of the scan

          type: Filter by the path of the scan type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            path_template("/waap/v1/domains/{domain_id}/api-discovery/scan-results", domain_id=domain_id),
            page=SyncOffsetPage[WaapAPIScanResult],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "message": message,
                        "offset": offset,
                        "ordering": ordering,
                        "status": status,
                        "type": type,
                    },
                    scan_result_list_params.ScanResultListParams,
                ),
            ),
            model=WaapAPIScanResult,
        )

    def get(
        self,
        scan_id: str,
        *,
        domain_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapAPIScanResult:
        """
        Get Scan Result

        Args:
          domain_id: The domain ID

          scan_id: The scan ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not scan_id:
            raise ValueError(f"Expected a non-empty value for `scan_id` but received {scan_id!r}")
        return self._get(
            path_template(
                "/waap/v1/domains/{domain_id}/api-discovery/scan-results/{scan_id}",
                domain_id=domain_id,
                scan_id=scan_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapAPIScanResult,
        )


class AsyncScanResultsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncScanResultsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncScanResultsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScanResultsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncScanResultsResourceWithStreamingResponse(self)

    def list(
        self,
        domain_id: int,
        *,
        limit: int | Omit = omit,
        message: Optional[str] | Omit = omit,
        offset: int | Omit = omit,
        ordering: Literal[
            "id",
            "type",
            "start_time",
            "end_time",
            "status",
            "message",
            "-id",
            "-type",
            "-start_time",
            "-end_time",
            "-status",
            "-message",
        ]
        | Omit = omit,
        status: Optional[Literal["SUCCESS", "FAILURE", "IN_PROGRESS"]] | Omit = omit,
        type: Optional[Literal["TRAFFIC_SCAN", "API_DESCRIPTION_FILE_SCAN"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[WaapAPIScanResult, AsyncOffsetPage[WaapAPIScanResult]]:
        """
        Get Scan Results

        Args:
          domain_id: The domain ID

          limit: Number of items to return

          message: Filter by the message of the scan. Supports '\\**' as a wildcard character

          offset: Number of items to skip

          ordering: Sort the response by given field.

          status: Filter by the status of the scan

          type: Filter by the path of the scan type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            path_template("/waap/v1/domains/{domain_id}/api-discovery/scan-results", domain_id=domain_id),
            page=AsyncOffsetPage[WaapAPIScanResult],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "message": message,
                        "offset": offset,
                        "ordering": ordering,
                        "status": status,
                        "type": type,
                    },
                    scan_result_list_params.ScanResultListParams,
                ),
            ),
            model=WaapAPIScanResult,
        )

    async def get(
        self,
        scan_id: str,
        *,
        domain_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapAPIScanResult:
        """
        Get Scan Result

        Args:
          domain_id: The domain ID

          scan_id: The scan ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not scan_id:
            raise ValueError(f"Expected a non-empty value for `scan_id` but received {scan_id!r}")
        return await self._get(
            path_template(
                "/waap/v1/domains/{domain_id}/api-discovery/scan-results/{scan_id}",
                domain_id=domain_id,
                scan_id=scan_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapAPIScanResult,
        )


class ScanResultsResourceWithRawResponse:
    def __init__(self, scan_results: ScanResultsResource) -> None:
        self._scan_results = scan_results

        self.list = to_raw_response_wrapper(
            scan_results.list,
        )
        self.get = to_raw_response_wrapper(
            scan_results.get,
        )


class AsyncScanResultsResourceWithRawResponse:
    def __init__(self, scan_results: AsyncScanResultsResource) -> None:
        self._scan_results = scan_results

        self.list = async_to_raw_response_wrapper(
            scan_results.list,
        )
        self.get = async_to_raw_response_wrapper(
            scan_results.get,
        )


class ScanResultsResourceWithStreamingResponse:
    def __init__(self, scan_results: ScanResultsResource) -> None:
        self._scan_results = scan_results

        self.list = to_streamed_response_wrapper(
            scan_results.list,
        )
        self.get = to_streamed_response_wrapper(
            scan_results.get,
        )


class AsyncScanResultsResourceWithStreamingResponse:
    def __init__(self, scan_results: AsyncScanResultsResource) -> None:
        self._scan_results = scan_results

        self.list = async_to_streamed_response_wrapper(
            scan_results.list,
        )
        self.get = async_to_streamed_response_wrapper(
            scan_results.get,
        )
