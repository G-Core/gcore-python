# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import Body, Query, Headers, NotGiven, not_given
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.cloud.reserved_fixed_ips.vip.candidate_port_list import CandidatePortList

__all__ = ["CandidatePortsResource", "AsyncCandidatePortsResource"]


class CandidatePortsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CandidatePortsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return CandidatePortsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CandidatePortsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return CandidatePortsResourceWithStreamingResponse(self)

    def list(
        self,
        port_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CandidatePortList:
        """
        List all instance ports that are available for connecting to a VIP.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not port_id:
            raise ValueError(f"Expected a non-empty value for `port_id` but received {port_id!r}")
        return self._get(
            f"/cloud/v1/reserved_fixed_ips/{project_id}/{region_id}/{port_id}/available_devices",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CandidatePortList,
        )


class AsyncCandidatePortsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCandidatePortsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCandidatePortsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCandidatePortsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncCandidatePortsResourceWithStreamingResponse(self)

    async def list(
        self,
        port_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CandidatePortList:
        """
        List all instance ports that are available for connecting to a VIP.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not port_id:
            raise ValueError(f"Expected a non-empty value for `port_id` but received {port_id!r}")
        return await self._get(
            f"/cloud/v1/reserved_fixed_ips/{project_id}/{region_id}/{port_id}/available_devices",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CandidatePortList,
        )


class CandidatePortsResourceWithRawResponse:
    def __init__(self, candidate_ports: CandidatePortsResource) -> None:
        self._candidate_ports = candidate_ports

        self.list = to_raw_response_wrapper(
            candidate_ports.list,
        )


class AsyncCandidatePortsResourceWithRawResponse:
    def __init__(self, candidate_ports: AsyncCandidatePortsResource) -> None:
        self._candidate_ports = candidate_ports

        self.list = async_to_raw_response_wrapper(
            candidate_ports.list,
        )


class CandidatePortsResourceWithStreamingResponse:
    def __init__(self, candidate_ports: CandidatePortsResource) -> None:
        self._candidate_ports = candidate_ports

        self.list = to_streamed_response_wrapper(
            candidate_ports.list,
        )


class AsyncCandidatePortsResourceWithStreamingResponse:
    def __init__(self, candidate_ports: AsyncCandidatePortsResource) -> None:
        self._candidate_ports = candidate_ports

        self.list = async_to_streamed_response_wrapper(
            candidate_ports.list,
        )
