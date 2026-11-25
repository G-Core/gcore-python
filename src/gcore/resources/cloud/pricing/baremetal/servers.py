# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.cloud.server_price import ServerPrice
from .....types.cloud.pricing.baremetal import server_preview_params

__all__ = ["ServersResource", "AsyncServersResource"]


class ServersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ServersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return ServersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ServersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return ServersResourceWithStreamingResponse(self)

    def get(
        self,
        server_id: str,
        *,
        project_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServerPrice:
        """Get the price of an existing bare metal server.

        The price covers the flavor, the
        external IP addresses and the floating IPs.

        Args:
          project_id: Project ID.

          server_id: Bare metal server ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not server_id:
            raise ValueError(f"Expected a non-empty value for `server_id` but received {server_id!r}")
        return self._get(
            path_template(
                "/cloud/v1/projects/{project_id}/pricing/baremetal/servers/{server_id}",
                project_id=project_id,
                server_id=server_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServerPrice,
        )

    def preview(
        self,
        *,
        project_id: int | None = None,
        flavor_name: str,
        region_id: int,
        interfaces: Iterable[server_preview_params.Interface] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServerPrice:
        """Get the price of a bare metal server before you create it.

        Send the same body
        that you send to create a bare metal server. The API reads only the fields that
        change the price. The price includes the flavor, the ports and the floating IPs.
        It also includes the existing ports and floating IPs that you attach.

        Args:
          project_id: Project ID.

          flavor_name: Flavor of the server.

          region_id: Region of the server.

          interfaces: Ports in NIC order. An entry with `port_id` is an existing port, any other entry
              is a new one. Omit it to price the server without ports.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        return self._post(
            path_template("/cloud/v1/projects/{project_id}/pricing/baremetal/servers", project_id=project_id),
            body=maybe_transform(
                {
                    "flavor_name": flavor_name,
                    "region_id": region_id,
                    "interfaces": interfaces,
                },
                server_preview_params.ServerPreviewParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServerPrice,
        )


class AsyncServersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncServersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncServersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncServersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncServersResourceWithStreamingResponse(self)

    async def get(
        self,
        server_id: str,
        *,
        project_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServerPrice:
        """Get the price of an existing bare metal server.

        The price covers the flavor, the
        external IP addresses and the floating IPs.

        Args:
          project_id: Project ID.

          server_id: Bare metal server ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not server_id:
            raise ValueError(f"Expected a non-empty value for `server_id` but received {server_id!r}")
        return await self._get(
            path_template(
                "/cloud/v1/projects/{project_id}/pricing/baremetal/servers/{server_id}",
                project_id=project_id,
                server_id=server_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServerPrice,
        )

    async def preview(
        self,
        *,
        project_id: int | None = None,
        flavor_name: str,
        region_id: int,
        interfaces: Iterable[server_preview_params.Interface] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ServerPrice:
        """Get the price of a bare metal server before you create it.

        Send the same body
        that you send to create a bare metal server. The API reads only the fields that
        change the price. The price includes the flavor, the ports and the floating IPs.
        It also includes the existing ports and floating IPs that you attach.

        Args:
          project_id: Project ID.

          flavor_name: Flavor of the server.

          region_id: Region of the server.

          interfaces: Ports in NIC order. An entry with `port_id` is an existing port, any other entry
              is a new one. Omit it to price the server without ports.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        return await self._post(
            path_template("/cloud/v1/projects/{project_id}/pricing/baremetal/servers", project_id=project_id),
            body=await async_maybe_transform(
                {
                    "flavor_name": flavor_name,
                    "region_id": region_id,
                    "interfaces": interfaces,
                },
                server_preview_params.ServerPreviewParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServerPrice,
        )


class ServersResourceWithRawResponse:
    def __init__(self, servers: ServersResource) -> None:
        self._servers = servers

        self.get = to_raw_response_wrapper(
            servers.get,
        )
        self.preview = to_raw_response_wrapper(
            servers.preview,
        )


class AsyncServersResourceWithRawResponse:
    def __init__(self, servers: AsyncServersResource) -> None:
        self._servers = servers

        self.get = async_to_raw_response_wrapper(
            servers.get,
        )
        self.preview = async_to_raw_response_wrapper(
            servers.preview,
        )


class ServersResourceWithStreamingResponse:
    def __init__(self, servers: ServersResource) -> None:
        self._servers = servers

        self.get = to_streamed_response_wrapper(
            servers.get,
        )
        self.preview = to_streamed_response_wrapper(
            servers.preview,
        )


class AsyncServersResourceWithStreamingResponse:
    def __init__(self, servers: AsyncServersResource) -> None:
        self._servers = servers

        self.get = async_to_streamed_response_wrapper(
            servers.get,
        )
        self.preview = async_to_streamed_response_wrapper(
            servers.preview,
        )
