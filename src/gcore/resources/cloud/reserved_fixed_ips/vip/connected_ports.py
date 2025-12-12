# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.cloud.reserved_fixed_ips.vip import connected_port_add_params, connected_port_replace_params
from .....types.cloud.reserved_fixed_ips.vip.connected_port_list import ConnectedPortList

__all__ = ["ConnectedPortsResource", "AsyncConnectedPortsResource"]


class ConnectedPortsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConnectedPortsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return ConnectedPortsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConnectedPortsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return ConnectedPortsResourceWithStreamingResponse(self)

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
    ) -> ConnectedPortList:
        """
        List all instance ports that share a VIP.

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
            f"/cloud/v1/reserved_fixed_ips/{project_id}/{region_id}/{port_id}/connected_devices",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectedPortList,
        )

    def add(
        self,
        port_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        port_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectedPortList:
        """
        Add instance ports to share a VIP.

        Args:
          port_ids: List of port IDs that will share one VIP

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
        return self._patch(
            f"/cloud/v1/reserved_fixed_ips/{project_id}/{region_id}/{port_id}/connected_devices",
            body=maybe_transform({"port_ids": port_ids}, connected_port_add_params.ConnectedPortAddParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectedPortList,
        )

    def replace(
        self,
        port_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        port_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectedPortList:
        """
        Replace the list of instance ports that share a VIP.

        Args:
          port_ids: List of port IDs that will share one VIP

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
        return self._put(
            f"/cloud/v1/reserved_fixed_ips/{project_id}/{region_id}/{port_id}/connected_devices",
            body=maybe_transform({"port_ids": port_ids}, connected_port_replace_params.ConnectedPortReplaceParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectedPortList,
        )


class AsyncConnectedPortsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConnectedPortsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConnectedPortsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConnectedPortsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncConnectedPortsResourceWithStreamingResponse(self)

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
    ) -> ConnectedPortList:
        """
        List all instance ports that share a VIP.

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
            f"/cloud/v1/reserved_fixed_ips/{project_id}/{region_id}/{port_id}/connected_devices",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectedPortList,
        )

    async def add(
        self,
        port_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        port_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectedPortList:
        """
        Add instance ports to share a VIP.

        Args:
          port_ids: List of port IDs that will share one VIP

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
        return await self._patch(
            f"/cloud/v1/reserved_fixed_ips/{project_id}/{region_id}/{port_id}/connected_devices",
            body=await async_maybe_transform({"port_ids": port_ids}, connected_port_add_params.ConnectedPortAddParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectedPortList,
        )

    async def replace(
        self,
        port_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        port_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectedPortList:
        """
        Replace the list of instance ports that share a VIP.

        Args:
          port_ids: List of port IDs that will share one VIP

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
        return await self._put(
            f"/cloud/v1/reserved_fixed_ips/{project_id}/{region_id}/{port_id}/connected_devices",
            body=await async_maybe_transform(
                {"port_ids": port_ids}, connected_port_replace_params.ConnectedPortReplaceParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectedPortList,
        )


class ConnectedPortsResourceWithRawResponse:
    def __init__(self, connected_ports: ConnectedPortsResource) -> None:
        self._connected_ports = connected_ports

        self.list = to_raw_response_wrapper(
            connected_ports.list,
        )
        self.add = to_raw_response_wrapper(
            connected_ports.add,
        )
        self.replace = to_raw_response_wrapper(
            connected_ports.replace,
        )


class AsyncConnectedPortsResourceWithRawResponse:
    def __init__(self, connected_ports: AsyncConnectedPortsResource) -> None:
        self._connected_ports = connected_ports

        self.list = async_to_raw_response_wrapper(
            connected_ports.list,
        )
        self.add = async_to_raw_response_wrapper(
            connected_ports.add,
        )
        self.replace = async_to_raw_response_wrapper(
            connected_ports.replace,
        )


class ConnectedPortsResourceWithStreamingResponse:
    def __init__(self, connected_ports: ConnectedPortsResource) -> None:
        self._connected_ports = connected_ports

        self.list = to_streamed_response_wrapper(
            connected_ports.list,
        )
        self.add = to_streamed_response_wrapper(
            connected_ports.add,
        )
        self.replace = to_streamed_response_wrapper(
            connected_ports.replace,
        )


class AsyncConnectedPortsResourceWithStreamingResponse:
    def __init__(self, connected_ports: AsyncConnectedPortsResource) -> None:
        self._connected_ports = connected_ports

        self.list = async_to_streamed_response_wrapper(
            connected_ports.list,
        )
        self.add = async_to_streamed_response_wrapper(
            connected_ports.add,
        )
        self.replace = async_to_streamed_response_wrapper(
            connected_ports.replace,
        )
