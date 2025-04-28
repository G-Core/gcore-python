# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

import httpx

from .routers import (
    RoutersResource,
    AsyncRoutersResource,
    RoutersResourceWithRawResponse,
    AsyncRoutersResourceWithRawResponse,
    RoutersResourceWithStreamingResponse,
    AsyncRoutersResourceWithStreamingResponse,
)
from .subnets import (
    SubnetsResource,
    AsyncSubnetsResource,
    SubnetsResourceWithRawResponse,
    AsyncSubnetsResourceWithRawResponse,
    SubnetsResourceWithStreamingResponse,
    AsyncSubnetsResourceWithStreamingResponse,
)
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
from ....types.cloud import network_list_params, network_create_params, network_update_params
from ...._base_client import AsyncPaginator, make_request_options
from ....types.cloud.network import Network
from ....types.cloud.task_id_list import TaskIDList

__all__ = ["NetworksResource", "AsyncNetworksResource"]


class NetworksResource(SyncAPIResource):
    @cached_property
    def subnets(self) -> SubnetsResource:
        return SubnetsResource(self._client)

    @cached_property
    def routers(self) -> RoutersResource:
        return RoutersResource(self._client)

    @cached_property
    def with_raw_response(self) -> NetworksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return NetworksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NetworksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
        """
        return NetworksResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        create_router: bool | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        type: Literal["vlan", "vxlan"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Create network

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fnetworks%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
              "$.paths['/cloud/v1/networks/{project_id}/{region_id}'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fnetworks%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
              "$.paths['/cloud/v1/networks/{project_id}/{region_id}'].post.parameters[1].schema"

          name: '#/components/schemas/CreateNetworkSerializer/properties/name'
              "$.components.schemas.CreateNetworkSerializer.properties.name"

          create_router: '#/components/schemas/CreateNetworkSerializer/properties/create_router'
              "$.components.schemas.CreateNetworkSerializer.properties.create_router"

          metadata: '#/components/schemas/CreateNetworkSerializer/properties/metadata/anyOf/0'
              "$.components.schemas.CreateNetworkSerializer.properties.metadata.anyOf[0]"

          type: '#/components/schemas/CreateNetworkSerializer/properties/type'
              "$.components.schemas.CreateNetworkSerializer.properties.type"

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
            f"/cloud/v1/networks/{project_id}/{region_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "create_router": create_router,
                    "metadata": metadata,
                    "type": type,
                },
                network_create_params.NetworkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def update(
        self,
        network_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Network:
        """
        Change network name

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fnetworks%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bnetwork_id%7D/patch/parameters/0/schema'
              "$.paths['/cloud/v1/networks/{project_id}/{region_id}/{network_id}'].patch.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fnetworks%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bnetwork_id%7D/patch/parameters/1/schema'
              "$.paths['/cloud/v1/networks/{project_id}/{region_id}/{network_id}'].patch.parameters[1].schema"

          network_id: '#/paths/%2Fcloud%2Fv1%2Fnetworks%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bnetwork_id%7D/patch/parameters/2/schema'
              "$.paths['/cloud/v1/networks/{project_id}/{region_id}/{network_id}'].patch.parameters[2].schema"

          name: '#/components/schemas/NameSerializerPydantic/properties/name'
              "$.components.schemas.NameSerializerPydantic.properties.name"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not network_id:
            raise ValueError(f"Expected a non-empty value for `network_id` but received {network_id!r}")
        return self._patch(
            f"/cloud/v1/networks/{project_id}/{region_id}/{network_id}",
            body=maybe_transform({"name": name}, network_update_params.NetworkUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Network,
        )

    def list(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        limit: int | NotGiven = NOT_GIVEN,
        metadata_k: str | NotGiven = NOT_GIVEN,
        metadata_kv: str | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        order_by: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[Network]:
        """
        List networks

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fnetworks%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/networks/{project_id}/{region_id}'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fnetworks%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v1/networks/{project_id}/{region_id}'].get.parameters[1].schema"

          limit: '#/paths/%2Fcloud%2Fv1%2Fnetworks%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/2'
              "$.paths['/cloud/v1/networks/{project_id}/{region_id}'].get.parameters[2]"

          metadata_k: '#/paths/%2Fcloud%2Fv1%2Fnetworks%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/3'
              "$.paths['/cloud/v1/networks/{project_id}/{region_id}'].get.parameters[3]"

          metadata_kv: '#/paths/%2Fcloud%2Fv1%2Fnetworks%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/4'
              "$.paths['/cloud/v1/networks/{project_id}/{region_id}'].get.parameters[4]"

          offset: '#/paths/%2Fcloud%2Fv1%2Fnetworks%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/5'
              "$.paths['/cloud/v1/networks/{project_id}/{region_id}'].get.parameters[5]"

          order_by: '#/paths/%2Fcloud%2Fv1%2Fnetworks%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/6'
              "$.paths['/cloud/v1/networks/{project_id}/{region_id}'].get.parameters[6]"

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
            f"/cloud/v1/networks/{project_id}/{region_id}",
            page=SyncOffsetPage[Network],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "metadata_k": metadata_k,
                        "metadata_kv": metadata_kv,
                        "offset": offset,
                        "order_by": order_by,
                    },
                    network_list_params.NetworkListParams,
                ),
            ),
            model=Network,
        )

    def delete(
        self,
        network_id: str,
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
        Delete network

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fnetworks%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bnetwork_id%7D/delete/parameters/0/schema'
              "$.paths['/cloud/v1/networks/{project_id}/{region_id}/{network_id}']['delete'].parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fnetworks%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bnetwork_id%7D/delete/parameters/1/schema'
              "$.paths['/cloud/v1/networks/{project_id}/{region_id}/{network_id}']['delete'].parameters[1].schema"

          network_id: '#/paths/%2Fcloud%2Fv1%2Fnetworks%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bnetwork_id%7D/delete/parameters/2/schema'
              "$.paths['/cloud/v1/networks/{project_id}/{region_id}/{network_id}']['delete'].parameters[2].schema"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not network_id:
            raise ValueError(f"Expected a non-empty value for `network_id` but received {network_id!r}")
        return self._delete(
            f"/cloud/v1/networks/{project_id}/{region_id}/{network_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def get(
        self,
        network_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Network:
        """
        Get network

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fnetworks%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bnetwork_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/networks/{project_id}/{region_id}/{network_id}'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fnetworks%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bnetwork_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v1/networks/{project_id}/{region_id}/{network_id}'].get.parameters[1].schema"

          network_id: '#/paths/%2Fcloud%2Fv1%2Fnetworks%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bnetwork_id%7D/get/parameters/2/schema'
              "$.paths['/cloud/v1/networks/{project_id}/{region_id}/{network_id}'].get.parameters[2].schema"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not network_id:
            raise ValueError(f"Expected a non-empty value for `network_id` but received {network_id!r}")
        return self._get(
            f"/cloud/v1/networks/{project_id}/{region_id}/{network_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Network,
        )


class AsyncNetworksResource(AsyncAPIResource):
    @cached_property
    def subnets(self) -> AsyncSubnetsResource:
        return AsyncSubnetsResource(self._client)

    @cached_property
    def routers(self) -> AsyncRoutersResource:
        return AsyncRoutersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncNetworksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNetworksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNetworksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
        """
        return AsyncNetworksResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        create_router: bool | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        type: Literal["vlan", "vxlan"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Create network

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fnetworks%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
              "$.paths['/cloud/v1/networks/{project_id}/{region_id}'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fnetworks%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
              "$.paths['/cloud/v1/networks/{project_id}/{region_id}'].post.parameters[1].schema"

          name: '#/components/schemas/CreateNetworkSerializer/properties/name'
              "$.components.schemas.CreateNetworkSerializer.properties.name"

          create_router: '#/components/schemas/CreateNetworkSerializer/properties/create_router'
              "$.components.schemas.CreateNetworkSerializer.properties.create_router"

          metadata: '#/components/schemas/CreateNetworkSerializer/properties/metadata/anyOf/0'
              "$.components.schemas.CreateNetworkSerializer.properties.metadata.anyOf[0]"

          type: '#/components/schemas/CreateNetworkSerializer/properties/type'
              "$.components.schemas.CreateNetworkSerializer.properties.type"

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
            f"/cloud/v1/networks/{project_id}/{region_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "create_router": create_router,
                    "metadata": metadata,
                    "type": type,
                },
                network_create_params.NetworkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def update(
        self,
        network_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Network:
        """
        Change network name

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fnetworks%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bnetwork_id%7D/patch/parameters/0/schema'
              "$.paths['/cloud/v1/networks/{project_id}/{region_id}/{network_id}'].patch.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fnetworks%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bnetwork_id%7D/patch/parameters/1/schema'
              "$.paths['/cloud/v1/networks/{project_id}/{region_id}/{network_id}'].patch.parameters[1].schema"

          network_id: '#/paths/%2Fcloud%2Fv1%2Fnetworks%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bnetwork_id%7D/patch/parameters/2/schema'
              "$.paths['/cloud/v1/networks/{project_id}/{region_id}/{network_id}'].patch.parameters[2].schema"

          name: '#/components/schemas/NameSerializerPydantic/properties/name'
              "$.components.schemas.NameSerializerPydantic.properties.name"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not network_id:
            raise ValueError(f"Expected a non-empty value for `network_id` but received {network_id!r}")
        return await self._patch(
            f"/cloud/v1/networks/{project_id}/{region_id}/{network_id}",
            body=await async_maybe_transform({"name": name}, network_update_params.NetworkUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Network,
        )

    def list(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        limit: int | NotGiven = NOT_GIVEN,
        metadata_k: str | NotGiven = NOT_GIVEN,
        metadata_kv: str | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        order_by: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Network, AsyncOffsetPage[Network]]:
        """
        List networks

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fnetworks%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/networks/{project_id}/{region_id}'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fnetworks%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v1/networks/{project_id}/{region_id}'].get.parameters[1].schema"

          limit: '#/paths/%2Fcloud%2Fv1%2Fnetworks%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/2'
              "$.paths['/cloud/v1/networks/{project_id}/{region_id}'].get.parameters[2]"

          metadata_k: '#/paths/%2Fcloud%2Fv1%2Fnetworks%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/3'
              "$.paths['/cloud/v1/networks/{project_id}/{region_id}'].get.parameters[3]"

          metadata_kv: '#/paths/%2Fcloud%2Fv1%2Fnetworks%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/4'
              "$.paths['/cloud/v1/networks/{project_id}/{region_id}'].get.parameters[4]"

          offset: '#/paths/%2Fcloud%2Fv1%2Fnetworks%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/5'
              "$.paths['/cloud/v1/networks/{project_id}/{region_id}'].get.parameters[5]"

          order_by: '#/paths/%2Fcloud%2Fv1%2Fnetworks%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/6'
              "$.paths['/cloud/v1/networks/{project_id}/{region_id}'].get.parameters[6]"

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
            f"/cloud/v1/networks/{project_id}/{region_id}",
            page=AsyncOffsetPage[Network],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "metadata_k": metadata_k,
                        "metadata_kv": metadata_kv,
                        "offset": offset,
                        "order_by": order_by,
                    },
                    network_list_params.NetworkListParams,
                ),
            ),
            model=Network,
        )

    async def delete(
        self,
        network_id: str,
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
        Delete network

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fnetworks%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bnetwork_id%7D/delete/parameters/0/schema'
              "$.paths['/cloud/v1/networks/{project_id}/{region_id}/{network_id}']['delete'].parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fnetworks%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bnetwork_id%7D/delete/parameters/1/schema'
              "$.paths['/cloud/v1/networks/{project_id}/{region_id}/{network_id}']['delete'].parameters[1].schema"

          network_id: '#/paths/%2Fcloud%2Fv1%2Fnetworks%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bnetwork_id%7D/delete/parameters/2/schema'
              "$.paths['/cloud/v1/networks/{project_id}/{region_id}/{network_id}']['delete'].parameters[2].schema"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not network_id:
            raise ValueError(f"Expected a non-empty value for `network_id` but received {network_id!r}")
        return await self._delete(
            f"/cloud/v1/networks/{project_id}/{region_id}/{network_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def get(
        self,
        network_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Network:
        """
        Get network

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fnetworks%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bnetwork_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/networks/{project_id}/{region_id}/{network_id}'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fnetworks%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bnetwork_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v1/networks/{project_id}/{region_id}/{network_id}'].get.parameters[1].schema"

          network_id: '#/paths/%2Fcloud%2Fv1%2Fnetworks%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bnetwork_id%7D/get/parameters/2/schema'
              "$.paths['/cloud/v1/networks/{project_id}/{region_id}/{network_id}'].get.parameters[2].schema"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not network_id:
            raise ValueError(f"Expected a non-empty value for `network_id` but received {network_id!r}")
        return await self._get(
            f"/cloud/v1/networks/{project_id}/{region_id}/{network_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Network,
        )


class NetworksResourceWithRawResponse:
    def __init__(self, networks: NetworksResource) -> None:
        self._networks = networks

        self.create = to_raw_response_wrapper(
            networks.create,
        )
        self.update = to_raw_response_wrapper(
            networks.update,
        )
        self.list = to_raw_response_wrapper(
            networks.list,
        )
        self.delete = to_raw_response_wrapper(
            networks.delete,
        )
        self.get = to_raw_response_wrapper(
            networks.get,
        )

    @cached_property
    def subnets(self) -> SubnetsResourceWithRawResponse:
        return SubnetsResourceWithRawResponse(self._networks.subnets)

    @cached_property
    def routers(self) -> RoutersResourceWithRawResponse:
        return RoutersResourceWithRawResponse(self._networks.routers)


class AsyncNetworksResourceWithRawResponse:
    def __init__(self, networks: AsyncNetworksResource) -> None:
        self._networks = networks

        self.create = async_to_raw_response_wrapper(
            networks.create,
        )
        self.update = async_to_raw_response_wrapper(
            networks.update,
        )
        self.list = async_to_raw_response_wrapper(
            networks.list,
        )
        self.delete = async_to_raw_response_wrapper(
            networks.delete,
        )
        self.get = async_to_raw_response_wrapper(
            networks.get,
        )

    @cached_property
    def subnets(self) -> AsyncSubnetsResourceWithRawResponse:
        return AsyncSubnetsResourceWithRawResponse(self._networks.subnets)

    @cached_property
    def routers(self) -> AsyncRoutersResourceWithRawResponse:
        return AsyncRoutersResourceWithRawResponse(self._networks.routers)


class NetworksResourceWithStreamingResponse:
    def __init__(self, networks: NetworksResource) -> None:
        self._networks = networks

        self.create = to_streamed_response_wrapper(
            networks.create,
        )
        self.update = to_streamed_response_wrapper(
            networks.update,
        )
        self.list = to_streamed_response_wrapper(
            networks.list,
        )
        self.delete = to_streamed_response_wrapper(
            networks.delete,
        )
        self.get = to_streamed_response_wrapper(
            networks.get,
        )

    @cached_property
    def subnets(self) -> SubnetsResourceWithStreamingResponse:
        return SubnetsResourceWithStreamingResponse(self._networks.subnets)

    @cached_property
    def routers(self) -> RoutersResourceWithStreamingResponse:
        return RoutersResourceWithStreamingResponse(self._networks.routers)


class AsyncNetworksResourceWithStreamingResponse:
    def __init__(self, networks: AsyncNetworksResource) -> None:
        self._networks = networks

        self.create = async_to_streamed_response_wrapper(
            networks.create,
        )
        self.update = async_to_streamed_response_wrapper(
            networks.update,
        )
        self.list = async_to_streamed_response_wrapper(
            networks.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            networks.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            networks.get,
        )

    @cached_property
    def subnets(self) -> AsyncSubnetsResourceWithStreamingResponse:
        return AsyncSubnetsResourceWithStreamingResponse(self._networks.subnets)

    @cached_property
    def routers(self) -> AsyncRoutersResourceWithStreamingResponse:
        return AsyncRoutersResourceWithStreamingResponse(self._networks.routers)
