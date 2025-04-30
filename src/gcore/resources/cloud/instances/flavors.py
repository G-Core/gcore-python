# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

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
from ...._base_client import make_request_options
from ....types.cloud.instances import flavor_list_params, flavor_list_suitable_params, flavor_list_for_resize_params
from ....types.cloud.instances.instance_flavor_list import InstanceFlavorList

__all__ = ["FlavorsResource", "AsyncFlavorsResource"]


class FlavorsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FlavorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return FlavorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FlavorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
        """
        return FlavorsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        disabled: bool | NotGiven = NOT_GIVEN,
        exclude_linux: bool | NotGiven = NOT_GIVEN,
        exclude_windows: bool | NotGiven = NOT_GIVEN,
        include_prices: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InstanceFlavorList:
        """Retrieve a list of flavors.

        When the include_prices query parameter is
        specified, the list shows prices. A client in trial mode gets all price values
        as 0. If you get Pricing Error contact the support

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fflavors%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/flavors/{project_id}/{region_id}'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fflavors%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v1/flavors/{project_id}/{region_id}'].get.parameters[1].schema"

          disabled: '#/paths/%2Fcloud%2Fv1%2Fflavors%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/2'
              "$.paths['/cloud/v1/flavors/{project_id}/{region_id}'].get.parameters[2]"

          exclude_linux: '#/paths/%2Fcloud%2Fv1%2Fflavors%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/3'
              "$.paths['/cloud/v1/flavors/{project_id}/{region_id}'].get.parameters[3]"

          exclude_windows: '#/paths/%2Fcloud%2Fv1%2Fflavors%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/4'
              "$.paths['/cloud/v1/flavors/{project_id}/{region_id}'].get.parameters[4]"

          include_prices: '#/paths/%2Fcloud%2Fv1%2Fflavors%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/5'
              "$.paths['/cloud/v1/flavors/{project_id}/{region_id}'].get.parameters[5]"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return self._get(
            f"/cloud/v1/flavors/{project_id}/{region_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "disabled": disabled,
                        "exclude_linux": exclude_linux,
                        "exclude_windows": exclude_windows,
                        "include_prices": include_prices,
                    },
                    flavor_list_params.FlavorListParams,
                ),
            ),
            cast_to=InstanceFlavorList,
        )

    def list_for_resize(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        include_prices: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InstanceFlavorList:
        """
        List suitable flavors for instance resize

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Favailable_flavors/get/parameters/0/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/available_flavors'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Favailable_flavors/get/parameters/1/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/available_flavors'].get.parameters[1].schema"

          instance_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Favailable_flavors/get/parameters/2/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/available_flavors'].get.parameters[2].schema"

          include_prices: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Favailable_flavors/get/parameters/3'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/available_flavors'].get.parameters[3]"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return self._get(
            f"/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/available_flavors",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"include_prices": include_prices}, flavor_list_for_resize_params.FlavorListForResizeParams
                ),
            ),
            cast_to=InstanceFlavorList,
        )

    def list_suitable(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        volumes: Iterable[flavor_list_suitable_params.Volume],
        include_prices: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InstanceFlavorList:
        """
        List suitable flavors for instance creation

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2Favailable_flavors/post/parameters/0/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/available_flavors'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2Favailable_flavors/post/parameters/1/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/available_flavors'].post.parameters[1].schema"

          volumes: '#/components/schemas/CreateInstanceVolumeListSchema/properties/volumes'
              "$.components.schemas.CreateInstanceVolumeListSchema.properties.volumes"

          include_prices: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2Favailable_flavors/post/parameters/2'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/available_flavors'].post.parameters[2]"

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
            f"/cloud/v1/instances/{project_id}/{region_id}/available_flavors",
            body=maybe_transform({"volumes": volumes}, flavor_list_suitable_params.FlavorListSuitableParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"include_prices": include_prices}, flavor_list_suitable_params.FlavorListSuitableParams
                ),
            ),
            cast_to=InstanceFlavorList,
        )


class AsyncFlavorsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFlavorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFlavorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFlavorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
        """
        return AsyncFlavorsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        disabled: bool | NotGiven = NOT_GIVEN,
        exclude_linux: bool | NotGiven = NOT_GIVEN,
        exclude_windows: bool | NotGiven = NOT_GIVEN,
        include_prices: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InstanceFlavorList:
        """Retrieve a list of flavors.

        When the include_prices query parameter is
        specified, the list shows prices. A client in trial mode gets all price values
        as 0. If you get Pricing Error contact the support

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fflavors%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/flavors/{project_id}/{region_id}'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fflavors%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v1/flavors/{project_id}/{region_id}'].get.parameters[1].schema"

          disabled: '#/paths/%2Fcloud%2Fv1%2Fflavors%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/2'
              "$.paths['/cloud/v1/flavors/{project_id}/{region_id}'].get.parameters[2]"

          exclude_linux: '#/paths/%2Fcloud%2Fv1%2Fflavors%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/3'
              "$.paths['/cloud/v1/flavors/{project_id}/{region_id}'].get.parameters[3]"

          exclude_windows: '#/paths/%2Fcloud%2Fv1%2Fflavors%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/4'
              "$.paths['/cloud/v1/flavors/{project_id}/{region_id}'].get.parameters[4]"

          include_prices: '#/paths/%2Fcloud%2Fv1%2Fflavors%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/5'
              "$.paths['/cloud/v1/flavors/{project_id}/{region_id}'].get.parameters[5]"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return await self._get(
            f"/cloud/v1/flavors/{project_id}/{region_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "disabled": disabled,
                        "exclude_linux": exclude_linux,
                        "exclude_windows": exclude_windows,
                        "include_prices": include_prices,
                    },
                    flavor_list_params.FlavorListParams,
                ),
            ),
            cast_to=InstanceFlavorList,
        )

    async def list_for_resize(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        include_prices: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InstanceFlavorList:
        """
        List suitable flavors for instance resize

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Favailable_flavors/get/parameters/0/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/available_flavors'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Favailable_flavors/get/parameters/1/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/available_flavors'].get.parameters[1].schema"

          instance_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Favailable_flavors/get/parameters/2/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/available_flavors'].get.parameters[2].schema"

          include_prices: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Favailable_flavors/get/parameters/3'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/available_flavors'].get.parameters[3]"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return await self._get(
            f"/cloud/v1/instances/{project_id}/{region_id}/{instance_id}/available_flavors",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"include_prices": include_prices}, flavor_list_for_resize_params.FlavorListForResizeParams
                ),
            ),
            cast_to=InstanceFlavorList,
        )

    async def list_suitable(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        volumes: Iterable[flavor_list_suitable_params.Volume],
        include_prices: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InstanceFlavorList:
        """
        List suitable flavors for instance creation

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2Favailable_flavors/post/parameters/0/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/available_flavors'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2Favailable_flavors/post/parameters/1/schema'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/available_flavors'].post.parameters[1].schema"

          volumes: '#/components/schemas/CreateInstanceVolumeListSchema/properties/volumes'
              "$.components.schemas.CreateInstanceVolumeListSchema.properties.volumes"

          include_prices: '#/paths/%2Fcloud%2Fv1%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2Favailable_flavors/post/parameters/2'
              "$.paths['/cloud/v1/instances/{project_id}/{region_id}/available_flavors'].post.parameters[2]"

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
            f"/cloud/v1/instances/{project_id}/{region_id}/available_flavors",
            body=await async_maybe_transform(
                {"volumes": volumes}, flavor_list_suitable_params.FlavorListSuitableParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"include_prices": include_prices}, flavor_list_suitable_params.FlavorListSuitableParams
                ),
            ),
            cast_to=InstanceFlavorList,
        )


class FlavorsResourceWithRawResponse:
    def __init__(self, flavors: FlavorsResource) -> None:
        self._flavors = flavors

        self.list = to_raw_response_wrapper(
            flavors.list,
        )
        self.list_for_resize = to_raw_response_wrapper(
            flavors.list_for_resize,
        )
        self.list_suitable = to_raw_response_wrapper(
            flavors.list_suitable,
        )


class AsyncFlavorsResourceWithRawResponse:
    def __init__(self, flavors: AsyncFlavorsResource) -> None:
        self._flavors = flavors

        self.list = async_to_raw_response_wrapper(
            flavors.list,
        )
        self.list_for_resize = async_to_raw_response_wrapper(
            flavors.list_for_resize,
        )
        self.list_suitable = async_to_raw_response_wrapper(
            flavors.list_suitable,
        )


class FlavorsResourceWithStreamingResponse:
    def __init__(self, flavors: FlavorsResource) -> None:
        self._flavors = flavors

        self.list = to_streamed_response_wrapper(
            flavors.list,
        )
        self.list_for_resize = to_streamed_response_wrapper(
            flavors.list_for_resize,
        )
        self.list_suitable = to_streamed_response_wrapper(
            flavors.list_suitable,
        )


class AsyncFlavorsResourceWithStreamingResponse:
    def __init__(self, flavors: AsyncFlavorsResource) -> None:
        self._flavors = flavors

        self.list = async_to_streamed_response_wrapper(
            flavors.list,
        )
        self.list_for_resize = async_to_streamed_response_wrapper(
            flavors.list_for_resize,
        )
        self.list_suitable = async_to_streamed_response_wrapper(
            flavors.list_suitable,
        )
