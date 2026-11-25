# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.cloud.pricing import port_preview_params
from ....types.cloud.port_price import PortPrice
from ....types.cloud.ip_assignment_request_param import IPAssignmentRequestParam

__all__ = ["PortsResource", "AsyncPortsResource"]


class PortsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PortsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return PortsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PortsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return PortsResourceWithStreamingResponse(self)

    def preview(
        self,
        *,
        project_id: int | None = None,
        region_id: int,
        ip_assignments: Iterable[IPAssignmentRequestParam] | Omit = omit,
        network_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortPrice:
        """Get the price of a port before you create it.

        Send the same body that you send
        to create a port. The API reads only the fields that change the price.

        Args:
          project_id: Project ID.

          region_id: Region ID where the port is created

          ip_assignments: IP addresses to assign. All subnets must belong to the same network. Repeat a
              subnet to get several addresses from it. Omit the field to get one address from
              an IPv4 subnet.

          network_id: Network to create the port in. When omitted, it is the network of the subnets in
              `ip_assignments`, or the region's public network if `ip_assignments` is omitted.
              Every subnet in `ip_assignments` must belong to it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        return self._post(
            path_template("/cloud/v1/projects/{project_id}/pricing/ports", project_id=project_id),
            body=maybe_transform(
                {
                    "region_id": region_id,
                    "ip_assignments": ip_assignments,
                    "network_id": network_id,
                },
                port_preview_params.PortPreviewParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortPrice,
        )


class AsyncPortsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPortsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPortsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPortsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncPortsResourceWithStreamingResponse(self)

    async def preview(
        self,
        *,
        project_id: int | None = None,
        region_id: int,
        ip_assignments: Iterable[IPAssignmentRequestParam] | Omit = omit,
        network_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortPrice:
        """Get the price of a port before you create it.

        Send the same body that you send
        to create a port. The API reads only the fields that change the price.

        Args:
          project_id: Project ID.

          region_id: Region ID where the port is created

          ip_assignments: IP addresses to assign. All subnets must belong to the same network. Repeat a
              subnet to get several addresses from it. Omit the field to get one address from
              an IPv4 subnet.

          network_id: Network to create the port in. When omitted, it is the network of the subnets in
              `ip_assignments`, or the region's public network if `ip_assignments` is omitted.
              Every subnet in `ip_assignments` must belong to it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        return await self._post(
            path_template("/cloud/v1/projects/{project_id}/pricing/ports", project_id=project_id),
            body=await async_maybe_transform(
                {
                    "region_id": region_id,
                    "ip_assignments": ip_assignments,
                    "network_id": network_id,
                },
                port_preview_params.PortPreviewParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortPrice,
        )


class PortsResourceWithRawResponse:
    def __init__(self, ports: PortsResource) -> None:
        self._ports = ports

        self.preview = to_raw_response_wrapper(
            ports.preview,
        )


class AsyncPortsResourceWithRawResponse:
    def __init__(self, ports: AsyncPortsResource) -> None:
        self._ports = ports

        self.preview = async_to_raw_response_wrapper(
            ports.preview,
        )


class PortsResourceWithStreamingResponse:
    def __init__(self, ports: PortsResource) -> None:
        self._ports = ports

        self.preview = to_streamed_response_wrapper(
            ports.preview,
        )


class AsyncPortsResourceWithStreamingResponse:
    def __init__(self, ports: AsyncPortsResource) -> None:
        self._ports = ports

        self.preview = async_to_streamed_response_wrapper(
            ports.preview,
        )
