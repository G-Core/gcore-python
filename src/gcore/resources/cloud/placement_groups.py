# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncOffsetPage, AsyncOffsetPage
from ...types.cloud import placement_group_list_params, placement_group_create_params
from ..._base_client import AsyncPaginator, make_request_options
from ...types.cloud.task_id_list import TaskIDList
from ...types.cloud.placement_group import PlacementGroup

__all__ = ["PlacementGroupsResource", "AsyncPlacementGroupsResource"]


class PlacementGroupsResource(SyncAPIResource):
    """
    Placement groups enforce affinity or anti-affinity policies that control whether virtual machines are hosted on the same or different physical servers.
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

    @typing_extensions.deprecated("deprecated")
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
        Use
        [POST /v1/projects/{`project_id`}/`placement_groups`](#operation/GlobalPlacementGroupListView.post)
        instead. This route is deprecated. Later, we will remove it. We will tell you in
        advance.

        Create an affinity or anti-affinity or soft-anti-affinity placement group

        Args:
          project_id: Project ID

          region_id: Region ID

          name: The name of the placement group.

          policy: The placement group policy.

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
            path_template(
                "/cloud/v1/servergroups/{project_id}/{region_id}", project_id=project_id, region_id=region_id
            ),
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

    @typing_extensions.deprecated("deprecated")
    def list(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[PlacementGroup]:
        """
        Use
        [GET /v1/projects/{`project_id`}/`placement_groups`](#operation/GlobalPlacementGroupListView.get)
        instead. This route is deprecated. Later, we will remove it. We will tell you in
        advance.

        List all placement groups in the specified project and region.

        Args:
          project_id: Project ID

          region_id: Region ID

          limit: Optional. Limit the number of returned items

          offset: Optional. Offset value is used to exclude the first set of records from the
              result

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
            path_template(
                "/cloud/v1/servergroups/{project_id}/{region_id}", project_id=project_id, region_id=region_id
            ),
            page=SyncOffsetPage[PlacementGroup],
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
                    placement_group_list_params.PlacementGroupListParams,
                ),
            ),
            model=PlacementGroup,
        )

    @typing_extensions.deprecated("deprecated")
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
        Use
        [DELETE /v1/projects/{`project_id`}/`placement_groups`/{`placement_group_id`}](#operation/GlobalPlacementGroupDetailView.delete)
        instead. This route is deprecated. Later, we will remove it. We will tell you in
        advance.

        Delete a placement group by its ID.

        Args:
          project_id: Project ID

          region_id: Region ID

          group_id: The ID of the placement group.

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
            path_template(
                "/cloud/v1/servergroups/{project_id}/{region_id}/{group_id}",
                project_id=project_id,
                region_id=region_id,
                group_id=group_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    @typing_extensions.deprecated("deprecated")
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
        Use
        [GET /v1/projects/{`project_id`}/`placement_groups`/{`placement_group_id`}](#operation/GlobalPlacementGroupDetailView.get)
        instead. This route is deprecated. Later, we will remove it. We will tell you in
        advance.

        Retrieve a single placement group by its ID.

        Args:
          project_id: Project ID

          region_id: Region ID

          group_id: The ID of the placement group.

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
            path_template(
                "/cloud/v1/servergroups/{project_id}/{region_id}/{group_id}",
                project_id=project_id,
                region_id=region_id,
                group_id=group_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlacementGroup,
        )


class AsyncPlacementGroupsResource(AsyncAPIResource):
    """
    Placement groups enforce affinity or anti-affinity policies that control whether virtual machines are hosted on the same or different physical servers.
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

    @typing_extensions.deprecated("deprecated")
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
        Use
        [POST /v1/projects/{`project_id`}/`placement_groups`](#operation/GlobalPlacementGroupListView.post)
        instead. This route is deprecated. Later, we will remove it. We will tell you in
        advance.

        Create an affinity or anti-affinity or soft-anti-affinity placement group

        Args:
          project_id: Project ID

          region_id: Region ID

          name: The name of the placement group.

          policy: The placement group policy.

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
            path_template(
                "/cloud/v1/servergroups/{project_id}/{region_id}", project_id=project_id, region_id=region_id
            ),
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

    @typing_extensions.deprecated("deprecated")
    def list(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PlacementGroup, AsyncOffsetPage[PlacementGroup]]:
        """
        Use
        [GET /v1/projects/{`project_id`}/`placement_groups`](#operation/GlobalPlacementGroupListView.get)
        instead. This route is deprecated. Later, we will remove it. We will tell you in
        advance.

        List all placement groups in the specified project and region.

        Args:
          project_id: Project ID

          region_id: Region ID

          limit: Optional. Limit the number of returned items

          offset: Optional. Offset value is used to exclude the first set of records from the
              result

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
            path_template(
                "/cloud/v1/servergroups/{project_id}/{region_id}", project_id=project_id, region_id=region_id
            ),
            page=AsyncOffsetPage[PlacementGroup],
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
                    placement_group_list_params.PlacementGroupListParams,
                ),
            ),
            model=PlacementGroup,
        )

    @typing_extensions.deprecated("deprecated")
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
        Use
        [DELETE /v1/projects/{`project_id`}/`placement_groups`/{`placement_group_id`}](#operation/GlobalPlacementGroupDetailView.delete)
        instead. This route is deprecated. Later, we will remove it. We will tell you in
        advance.

        Delete a placement group by its ID.

        Args:
          project_id: Project ID

          region_id: Region ID

          group_id: The ID of the placement group.

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
            path_template(
                "/cloud/v1/servergroups/{project_id}/{region_id}/{group_id}",
                project_id=project_id,
                region_id=region_id,
                group_id=group_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    @typing_extensions.deprecated("deprecated")
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
        Use
        [GET /v1/projects/{`project_id`}/`placement_groups`/{`placement_group_id`}](#operation/GlobalPlacementGroupDetailView.get)
        instead. This route is deprecated. Later, we will remove it. We will tell you in
        advance.

        Retrieve a single placement group by its ID.

        Args:
          project_id: Project ID

          region_id: Region ID

          group_id: The ID of the placement group.

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
            path_template(
                "/cloud/v1/servergroups/{project_id}/{region_id}/{group_id}",
                project_id=project_id,
                region_id=region_id,
                group_id=group_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlacementGroup,
        )


class PlacementGroupsResourceWithRawResponse:
    def __init__(self, placement_groups: PlacementGroupsResource) -> None:
        self._placement_groups = placement_groups

        self.create = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                placement_groups.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                placement_groups.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                placement_groups.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                placement_groups.get,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncPlacementGroupsResourceWithRawResponse:
    def __init__(self, placement_groups: AsyncPlacementGroupsResource) -> None:
        self._placement_groups = placement_groups

        self.create = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                placement_groups.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                placement_groups.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                placement_groups.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                placement_groups.get,  # pyright: ignore[reportDeprecated],
            )
        )


class PlacementGroupsResourceWithStreamingResponse:
    def __init__(self, placement_groups: PlacementGroupsResource) -> None:
        self._placement_groups = placement_groups

        self.create = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                placement_groups.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                placement_groups.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                placement_groups.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                placement_groups.get,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncPlacementGroupsResourceWithStreamingResponse:
    def __init__(self, placement_groups: AsyncPlacementGroupsResource) -> None:
        self._placement_groups = placement_groups

        self.create = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                placement_groups.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                placement_groups.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                placement_groups.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                placement_groups.get,  # pyright: ignore[reportDeprecated],
            )
        )
