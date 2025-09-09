# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncOffsetPage, AsyncOffsetPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.cloud.networks import (
    router_list_params,
    router_create_params,
    router_update_params,
    router_attach_subnet_params,
    router_detach_subnet_params,
)
from ....types.cloud.task_id_list import TaskIDList
from ....types.cloud.networks.router import Router

__all__ = ["RoutersResource", "AsyncRoutersResource"]


class RoutersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RoutersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return RoutersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RoutersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return RoutersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        external_gateway_info: Optional[router_create_params.ExternalGatewayInfo] | NotGiven = NOT_GIVEN,
        interfaces: Optional[Iterable[router_create_params.Interface]] | NotGiven = NOT_GIVEN,
        routes: Optional[Iterable[router_create_params.Route]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Create a new router with the specified configuration.

        Args:
          name: name of router

          external_gateway_info

          interfaces: List of interfaces to attach to router immediately after creation.

          routes: List of custom routes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return self._post(
            f"/cloud/v1/routers/{project_id}/{region_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "external_gateway_info": external_gateway_info,
                    "interfaces": interfaces,
                    "routes": routes,
                },
                router_create_params.RouterCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def update(
        self,
        router_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        external_gateway_info: Optional[router_update_params.ExternalGatewayInfo] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        routes: Optional[Iterable[router_update_params.Route]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Router:
        """
        Update the configuration of an existing router.

        Args:
          external_gateway_info: New external gateway.

          name: New name of router

          routes: List of custom routes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not router_id:
            raise ValueError(f"Expected a non-empty value for `router_id` but received {router_id!r}")
        return self._patch(
            f"/cloud/v1/routers/{project_id}/{region_id}/{router_id}",
            body=maybe_transform(
                {
                    "external_gateway_info": external_gateway_info,
                    "name": name,
                    "routes": routes,
                },
                router_update_params.RouterUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Router,
        )

    def list(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[Router]:
        """
        List all routers in the specified project and region.

        Args:
          limit: Limit the number of returned routers

          offset: Offset value is used to exclude the first set of records from the result

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return self._get_api_list(
            f"/cloud/v1/routers/{project_id}/{region_id}",
            page=SyncOffsetPage[Router],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    router_list_params.RouterListParams,
                ),
            ),
            model=Router,
        )

    def delete(
        self,
        router_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Delete a specific router and all its associated resources.

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
        if not router_id:
            raise ValueError(f"Expected a non-empty value for `router_id` but received {router_id!r}")
        return self._delete(
            f"/cloud/v1/routers/{project_id}/{region_id}/{router_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def attach_subnet(
        self,
        router_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        subnet_id: str,
        ip_address: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Router:
        """
        Attach a subnet to an existing router.

        Args:
          project_id: Project ID

          region_id: Region ID

          router_id: Router ID

          subnet_id: Subnet ID on which router interface will be created

          ip_address: IP address to assign for router's interface, if not specified, address will be
              selected automatically

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not router_id:
            raise ValueError(f"Expected a non-empty value for `router_id` but received {router_id!r}")
        return self._post(
            f"/cloud/v1/routers/{project_id}/{region_id}/{router_id}/attach",
            body=maybe_transform(
                {
                    "subnet_id": subnet_id,
                    "ip_address": ip_address,
                },
                router_attach_subnet_params.RouterAttachSubnetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Router,
        )

    def detach_subnet(
        self,
        router_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        subnet_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Router:
        """
        Detach a subnet from an existing router.

        Args:
          subnet_id: Target IP is identified by it's subnet

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not router_id:
            raise ValueError(f"Expected a non-empty value for `router_id` but received {router_id!r}")
        return self._post(
            f"/cloud/v1/routers/{project_id}/{region_id}/{router_id}/detach",
            body=maybe_transform({"subnet_id": subnet_id}, router_detach_subnet_params.RouterDetachSubnetParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Router,
        )

    def get(
        self,
        router_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Router:
        """
        Get detailed information about a specific router.

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
        if not router_id:
            raise ValueError(f"Expected a non-empty value for `router_id` but received {router_id!r}")
        return self._get(
            f"/cloud/v1/routers/{project_id}/{region_id}/{router_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Router,
        )


class AsyncRoutersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRoutersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRoutersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRoutersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncRoutersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        external_gateway_info: Optional[router_create_params.ExternalGatewayInfo] | NotGiven = NOT_GIVEN,
        interfaces: Optional[Iterable[router_create_params.Interface]] | NotGiven = NOT_GIVEN,
        routes: Optional[Iterable[router_create_params.Route]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Create a new router with the specified configuration.

        Args:
          name: name of router

          external_gateway_info

          interfaces: List of interfaces to attach to router immediately after creation.

          routes: List of custom routes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return await self._post(
            f"/cloud/v1/routers/{project_id}/{region_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "external_gateway_info": external_gateway_info,
                    "interfaces": interfaces,
                    "routes": routes,
                },
                router_create_params.RouterCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def update(
        self,
        router_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        external_gateway_info: Optional[router_update_params.ExternalGatewayInfo] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        routes: Optional[Iterable[router_update_params.Route]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Router:
        """
        Update the configuration of an existing router.

        Args:
          external_gateway_info: New external gateway.

          name: New name of router

          routes: List of custom routes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not router_id:
            raise ValueError(f"Expected a non-empty value for `router_id` but received {router_id!r}")
        return await self._patch(
            f"/cloud/v1/routers/{project_id}/{region_id}/{router_id}",
            body=await async_maybe_transform(
                {
                    "external_gateway_info": external_gateway_info,
                    "name": name,
                    "routes": routes,
                },
                router_update_params.RouterUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Router,
        )

    def list(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Router, AsyncOffsetPage[Router]]:
        """
        List all routers in the specified project and region.

        Args:
          limit: Limit the number of returned routers

          offset: Offset value is used to exclude the first set of records from the result

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return self._get_api_list(
            f"/cloud/v1/routers/{project_id}/{region_id}",
            page=AsyncOffsetPage[Router],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    router_list_params.RouterListParams,
                ),
            ),
            model=Router,
        )

    async def delete(
        self,
        router_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Delete a specific router and all its associated resources.

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
        if not router_id:
            raise ValueError(f"Expected a non-empty value for `router_id` but received {router_id!r}")
        return await self._delete(
            f"/cloud/v1/routers/{project_id}/{region_id}/{router_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def attach_subnet(
        self,
        router_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        subnet_id: str,
        ip_address: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Router:
        """
        Attach a subnet to an existing router.

        Args:
          project_id: Project ID

          region_id: Region ID

          router_id: Router ID

          subnet_id: Subnet ID on which router interface will be created

          ip_address: IP address to assign for router's interface, if not specified, address will be
              selected automatically

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not router_id:
            raise ValueError(f"Expected a non-empty value for `router_id` but received {router_id!r}")
        return await self._post(
            f"/cloud/v1/routers/{project_id}/{region_id}/{router_id}/attach",
            body=await async_maybe_transform(
                {
                    "subnet_id": subnet_id,
                    "ip_address": ip_address,
                },
                router_attach_subnet_params.RouterAttachSubnetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Router,
        )

    async def detach_subnet(
        self,
        router_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        subnet_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Router:
        """
        Detach a subnet from an existing router.

        Args:
          subnet_id: Target IP is identified by it's subnet

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not router_id:
            raise ValueError(f"Expected a non-empty value for `router_id` but received {router_id!r}")
        return await self._post(
            f"/cloud/v1/routers/{project_id}/{region_id}/{router_id}/detach",
            body=await async_maybe_transform(
                {"subnet_id": subnet_id}, router_detach_subnet_params.RouterDetachSubnetParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Router,
        )

    async def get(
        self,
        router_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Router:
        """
        Get detailed information about a specific router.

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
        if not router_id:
            raise ValueError(f"Expected a non-empty value for `router_id` but received {router_id!r}")
        return await self._get(
            f"/cloud/v1/routers/{project_id}/{region_id}/{router_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Router,
        )


class RoutersResourceWithRawResponse:
    def __init__(self, routers: RoutersResource) -> None:
        self._routers = routers

        self.create = to_raw_response_wrapper(
            routers.create,
        )
        self.update = to_raw_response_wrapper(
            routers.update,
        )
        self.list = to_raw_response_wrapper(
            routers.list,
        )
        self.delete = to_raw_response_wrapper(
            routers.delete,
        )
        self.attach_subnet = to_raw_response_wrapper(
            routers.attach_subnet,
        )
        self.detach_subnet = to_raw_response_wrapper(
            routers.detach_subnet,
        )
        self.get = to_raw_response_wrapper(
            routers.get,
        )


class AsyncRoutersResourceWithRawResponse:
    def __init__(self, routers: AsyncRoutersResource) -> None:
        self._routers = routers

        self.create = async_to_raw_response_wrapper(
            routers.create,
        )
        self.update = async_to_raw_response_wrapper(
            routers.update,
        )
        self.list = async_to_raw_response_wrapper(
            routers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            routers.delete,
        )
        self.attach_subnet = async_to_raw_response_wrapper(
            routers.attach_subnet,
        )
        self.detach_subnet = async_to_raw_response_wrapper(
            routers.detach_subnet,
        )
        self.get = async_to_raw_response_wrapper(
            routers.get,
        )


class RoutersResourceWithStreamingResponse:
    def __init__(self, routers: RoutersResource) -> None:
        self._routers = routers

        self.create = to_streamed_response_wrapper(
            routers.create,
        )
        self.update = to_streamed_response_wrapper(
            routers.update,
        )
        self.list = to_streamed_response_wrapper(
            routers.list,
        )
        self.delete = to_streamed_response_wrapper(
            routers.delete,
        )
        self.attach_subnet = to_streamed_response_wrapper(
            routers.attach_subnet,
        )
        self.detach_subnet = to_streamed_response_wrapper(
            routers.detach_subnet,
        )
        self.get = to_streamed_response_wrapper(
            routers.get,
        )


class AsyncRoutersResourceWithStreamingResponse:
    def __init__(self, routers: AsyncRoutersResource) -> None:
        self._routers = routers

        self.create = async_to_streamed_response_wrapper(
            routers.create,
        )
        self.update = async_to_streamed_response_wrapper(
            routers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            routers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            routers.delete,
        )
        self.attach_subnet = async_to_streamed_response_wrapper(
            routers.attach_subnet,
        )
        self.detach_subnet = async_to_streamed_response_wrapper(
            routers.detach_subnet,
        )
        self.get = async_to_streamed_response_wrapper(
            routers.get,
        )
