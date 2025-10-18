# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.cloud import placement_group_create_params
from ..._base_client import make_request_options
from ...types.cloud.task_id_list import TaskIDList
from ...types.cloud.placement_group import PlacementGroup
from ...types.cloud.placement_group_list import PlacementGroupList

__all__ = ["PlacementGroupsResource", "AsyncPlacementGroupsResource"]


class PlacementGroupsResource(SyncAPIResource):
    """
    Placement Groups allow you to specific a policy that determines whether Virtual Machines will be hosted on the same physical server or on different ones.
    """

    @cached_property
    def with_raw_response(self) -> PlacementGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return PlacementGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PlacementGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return PlacementGroupsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        policy: Literal["affinity", "anti-affinity", "soft-anti-affinity"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlacementGroup:
        """
        Create an affinity or anti-affinity or soft-anti-affinity placement group

        Args:
          name: The name of the server group.

          policy: The server group policy.

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
            f"/cloud/v1/servergroups/{project_id}/{region_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "policy": policy,
                },
                placement_group_create_params.PlacementGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlacementGroup,
        )

    def list(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlacementGroupList:
        """
        List placement groups

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
        return self._get(
            f"/cloud/v1/servergroups/{project_id}/{region_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlacementGroupList,
        )

    def delete(
        self,
        group_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Delete placement group

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
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return self._delete(
            f"/cloud/v1/servergroups/{project_id}/{region_id}/{group_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def get(
        self,
        group_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlacementGroup:
        """
        Get placement group

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
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return self._get(
            f"/cloud/v1/servergroups/{project_id}/{region_id}/{group_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlacementGroup,
        )


class AsyncPlacementGroupsResource(AsyncAPIResource):
    """
    Placement Groups allow you to specific a policy that determines whether Virtual Machines will be hosted on the same physical server or on different ones.
    """

    @cached_property
    def with_raw_response(self) -> AsyncPlacementGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPlacementGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPlacementGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncPlacementGroupsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        policy: Literal["affinity", "anti-affinity", "soft-anti-affinity"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlacementGroup:
        """
        Create an affinity or anti-affinity or soft-anti-affinity placement group

        Args:
          name: The name of the server group.

          policy: The server group policy.

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
            f"/cloud/v1/servergroups/{project_id}/{region_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "policy": policy,
                },
                placement_group_create_params.PlacementGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlacementGroup,
        )

    async def list(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlacementGroupList:
        """
        List placement groups

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
        return await self._get(
            f"/cloud/v1/servergroups/{project_id}/{region_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlacementGroupList,
        )

    async def delete(
        self,
        group_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Delete placement group

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
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return await self._delete(
            f"/cloud/v1/servergroups/{project_id}/{region_id}/{group_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def get(
        self,
        group_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlacementGroup:
        """
        Get placement group

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
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return await self._get(
            f"/cloud/v1/servergroups/{project_id}/{region_id}/{group_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlacementGroup,
        )


class PlacementGroupsResourceWithRawResponse:
    def __init__(self, placement_groups: PlacementGroupsResource) -> None:
        self._placement_groups = placement_groups

        self.create = to_raw_response_wrapper(
            placement_groups.create,
        )
        self.list = to_raw_response_wrapper(
            placement_groups.list,
        )
        self.delete = to_raw_response_wrapper(
            placement_groups.delete,
        )
        self.get = to_raw_response_wrapper(
            placement_groups.get,
        )


class AsyncPlacementGroupsResourceWithRawResponse:
    def __init__(self, placement_groups: AsyncPlacementGroupsResource) -> None:
        self._placement_groups = placement_groups

        self.create = async_to_raw_response_wrapper(
            placement_groups.create,
        )
        self.list = async_to_raw_response_wrapper(
            placement_groups.list,
        )
        self.delete = async_to_raw_response_wrapper(
            placement_groups.delete,
        )
        self.get = async_to_raw_response_wrapper(
            placement_groups.get,
        )


class PlacementGroupsResourceWithStreamingResponse:
    def __init__(self, placement_groups: PlacementGroupsResource) -> None:
        self._placement_groups = placement_groups

        self.create = to_streamed_response_wrapper(
            placement_groups.create,
        )
        self.list = to_streamed_response_wrapper(
            placement_groups.list,
        )
        self.delete = to_streamed_response_wrapper(
            placement_groups.delete,
        )
        self.get = to_streamed_response_wrapper(
            placement_groups.get,
        )


class AsyncPlacementGroupsResourceWithStreamingResponse:
    def __init__(self, placement_groups: AsyncPlacementGroupsResource) -> None:
        self._placement_groups = placement_groups

        self.create = async_to_streamed_response_wrapper(
            placement_groups.create,
        )
        self.list = async_to_streamed_response_wrapper(
            placement_groups.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            placement_groups.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            placement_groups.get,
        )
