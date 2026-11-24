# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ...types.cloud import placement_group_list_params, placement_group_create_params, placement_group_delete_params
from ..._base_client import AsyncPaginator, make_request_options
from .placement_groups_custom import PlacementGroupsResourceCustomMixin, AsyncPlacementGroupsResourceCustomMixin
from ...types.cloud.task_id_list import TaskIDList
from ...types.cloud.placement_group import PlacementGroup
from ...types.cloud.placement_group_delete_response import PlacementGroupDeleteResponse

__all__ = ["PlacementGroupsResource", "AsyncPlacementGroupsResource"]


class PlacementGroupsResource(PlacementGroupsResourceCustomMixin, SyncAPIResource):
    """
    Placement groups set an affinity or anti-affinity policy for virtual machines, in any region of the project.
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
        name: str,
        policy: Literal["affinity", "anti-affinity", "soft-affinity", "soft-anti-affinity"],
        region_id: int,
        dry_run: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Create an affinity, anti-affinity, soft-affinity or soft-anti-affinity placement
        group. Returns the ID of the task performing the creation.

        The name and the policy cannot change after the create. To add an instance to
        the group, send `placement_group_id` when you create or update the instance.

        With `?dry_run=true` the request runs every check and changes nothing. The
        response holds an empty `tasks` array. A failed check returns the same error as
        the real create.

        Args:
          project_id: Project ID.

          name: Placement group name. A name starting with `k8s-` is rejected with 400
              `validation-error`. The prefix is reserved for the groups that managed
              Kubernetes creates.

          policy: Placement policy: affinity, anti-affinity, soft-affinity, or soft-anti-affinity.

          region_id: Region to create the placement group in.

          dry_run: Run every check of the real request and change nothing. The response has the
              status code and the schema of the real call, and an empty list of tasks. With
              `false`, the default, the request does the operation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        return self._post(
            path_template("/cloud/v1/projects/{project_id}/placement_groups", project_id=project_id),
            body=maybe_transform(
                {
                    "name": name,
                    "policy": policy,
                    "region_id": region_id,
                },
                placement_group_create_params.PlacementGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"dry_run": dry_run}, placement_group_create_params.PlacementGroupCreateParams),
            ),
            cast_to=TaskIDList,
        )

    def list(
        self,
        *,
        project_id: int | None = None,
        ids: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        managed: bool | Omit = omit,
        managed_by: Literal["system"] | Omit = omit,
        member_ids: SequenceNotStr[str] | Omit = omit,
        name: placement_group_list_params.Name | Omit = omit,
        offset: int | Omit = omit,
        order_by: Literal[
            "created_at.asc",
            "created_at.desc",
            "name.asc",
            "name.desc",
            "region_id.asc",
            "region_id.desc",
            "updated_at.asc",
            "updated_at.desc",
        ]
        | Omit = omit,
        policies: List[Literal["affinity", "anti-affinity", "soft-affinity", "soft-anti-affinity"]] | Omit = omit,
        region_ids: Iterable[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[PlacementGroup]:
        """List a project's placement groups across all regions.

        Groups created for a
        managed service such as Kubernetes are returned with a `managed_by` object and
        are read-only.

        Args:
          project_id: Project ID.

          ids: Filter by one or more placement group IDs (exact match).

          limit: Maximum number of items to return.

          managed: Filter placement groups that a service operates (true) or not (false).

          managed_by: Filter by the type of the managing service.

          member_ids: Filter to placement groups containing any of these instance UUIDs.

          name: Operator-based name filter, e.g. `name[contains]=web`, `name[prefix]=prod-`.
              Case-insensitive.

          offset: Number of items to skip from the start of the result.

          order_by: Sort field and direction.

          policies: Filter by one or more placement policies.

          region_ids: Filter by one or more region IDs. Omit to list across all regions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        return self._get_api_list(
            path_template("/cloud/v1/projects/{project_id}/placement_groups", project_id=project_id),
            page=SyncOffsetPage[PlacementGroup],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ids": ids,
                        "limit": limit,
                        "managed": managed,
                        "managed_by": managed_by,
                        "member_ids": member_ids,
                        "name": name,
                        "offset": offset,
                        "order_by": order_by,
                        "policies": policies,
                        "region_ids": region_ids,
                    },
                    placement_group_list_params.PlacementGroupListParams,
                ),
            ),
            model=PlacementGroup,
        )

    def delete(
        self,
        placement_group_id: str,
        *,
        project_id: int | None = None,
        dry_run: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlacementGroupDeleteResponse:
        """
        Returns the ID of the task performing the deletion.

        A group created for a managed service such as Kubernetes (non-null `managed_by`)
        is platform-owned and cannot be deleted. Members are not deleted, only
        ungrouped. The delete removes no other resource, and no resource is attached to
        a group. So `resources_to_delete` holds only the group, and
        `resources_to_preserve` is empty.

        With `?dry_run=true` the request runs every check and changes nothing. The
        response holds an empty `tasks` array. A failed check returns the same error as
        the real delete.

        Args:
          project_id: Project ID.

          placement_group_id: Placement group ID.

          dry_run: Run every check of the real request and change nothing. The response has the
              status code and the schema of the real call, and an empty list of tasks. With
              `false`, the default, the request does the operation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not placement_group_id:
            raise ValueError(f"Expected a non-empty value for `placement_group_id` but received {placement_group_id!r}")
        return self._delete(
            path_template(
                "/cloud/v1/projects/{project_id}/placement_groups/{placement_group_id}",
                project_id=project_id,
                placement_group_id=placement_group_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"dry_run": dry_run}, placement_group_delete_params.PlacementGroupDeleteParams),
            ),
            cast_to=PlacementGroupDeleteResponse,
        )

    def get(
        self,
        placement_group_id: str,
        *,
        project_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlacementGroup:
        """
        Returns a single placement group by ID; the region is resolved from the ID, so
        it is not part of the path.

        Args:
          project_id: Project ID.

          placement_group_id: Placement group ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not placement_group_id:
            raise ValueError(f"Expected a non-empty value for `placement_group_id` but received {placement_group_id!r}")
        return self._get(
            path_template(
                "/cloud/v1/projects/{project_id}/placement_groups/{placement_group_id}",
                project_id=project_id,
                placement_group_id=placement_group_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlacementGroup,
        )


class AsyncPlacementGroupsResource(AsyncPlacementGroupsResourceCustomMixin, AsyncAPIResource):
    """
    Placement groups set an affinity or anti-affinity policy for virtual machines, in any region of the project.
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
        name: str,
        policy: Literal["affinity", "anti-affinity", "soft-affinity", "soft-anti-affinity"],
        region_id: int,
        dry_run: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Create an affinity, anti-affinity, soft-affinity or soft-anti-affinity placement
        group. Returns the ID of the task performing the creation.

        The name and the policy cannot change after the create. To add an instance to
        the group, send `placement_group_id` when you create or update the instance.

        With `?dry_run=true` the request runs every check and changes nothing. The
        response holds an empty `tasks` array. A failed check returns the same error as
        the real create.

        Args:
          project_id: Project ID.

          name: Placement group name. A name starting with `k8s-` is rejected with 400
              `validation-error`. The prefix is reserved for the groups that managed
              Kubernetes creates.

          policy: Placement policy: affinity, anti-affinity, soft-affinity, or soft-anti-affinity.

          region_id: Region to create the placement group in.

          dry_run: Run every check of the real request and change nothing. The response has the
              status code and the schema of the real call, and an empty list of tasks. With
              `false`, the default, the request does the operation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        return await self._post(
            path_template("/cloud/v1/projects/{project_id}/placement_groups", project_id=project_id),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "policy": policy,
                    "region_id": region_id,
                },
                placement_group_create_params.PlacementGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"dry_run": dry_run}, placement_group_create_params.PlacementGroupCreateParams
                ),
            ),
            cast_to=TaskIDList,
        )

    def list(
        self,
        *,
        project_id: int | None = None,
        ids: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        managed: bool | Omit = omit,
        managed_by: Literal["system"] | Omit = omit,
        member_ids: SequenceNotStr[str] | Omit = omit,
        name: placement_group_list_params.Name | Omit = omit,
        offset: int | Omit = omit,
        order_by: Literal[
            "created_at.asc",
            "created_at.desc",
            "name.asc",
            "name.desc",
            "region_id.asc",
            "region_id.desc",
            "updated_at.asc",
            "updated_at.desc",
        ]
        | Omit = omit,
        policies: List[Literal["affinity", "anti-affinity", "soft-affinity", "soft-anti-affinity"]] | Omit = omit,
        region_ids: Iterable[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PlacementGroup, AsyncOffsetPage[PlacementGroup]]:
        """List a project's placement groups across all regions.

        Groups created for a
        managed service such as Kubernetes are returned with a `managed_by` object and
        are read-only.

        Args:
          project_id: Project ID.

          ids: Filter by one or more placement group IDs (exact match).

          limit: Maximum number of items to return.

          managed: Filter placement groups that a service operates (true) or not (false).

          managed_by: Filter by the type of the managing service.

          member_ids: Filter to placement groups containing any of these instance UUIDs.

          name: Operator-based name filter, e.g. `name[contains]=web`, `name[prefix]=prod-`.
              Case-insensitive.

          offset: Number of items to skip from the start of the result.

          order_by: Sort field and direction.

          policies: Filter by one or more placement policies.

          region_ids: Filter by one or more region IDs. Omit to list across all regions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        return self._get_api_list(
            path_template("/cloud/v1/projects/{project_id}/placement_groups", project_id=project_id),
            page=AsyncOffsetPage[PlacementGroup],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ids": ids,
                        "limit": limit,
                        "managed": managed,
                        "managed_by": managed_by,
                        "member_ids": member_ids,
                        "name": name,
                        "offset": offset,
                        "order_by": order_by,
                        "policies": policies,
                        "region_ids": region_ids,
                    },
                    placement_group_list_params.PlacementGroupListParams,
                ),
            ),
            model=PlacementGroup,
        )

    async def delete(
        self,
        placement_group_id: str,
        *,
        project_id: int | None = None,
        dry_run: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlacementGroupDeleteResponse:
        """
        Returns the ID of the task performing the deletion.

        A group created for a managed service such as Kubernetes (non-null `managed_by`)
        is platform-owned and cannot be deleted. Members are not deleted, only
        ungrouped. The delete removes no other resource, and no resource is attached to
        a group. So `resources_to_delete` holds only the group, and
        `resources_to_preserve` is empty.

        With `?dry_run=true` the request runs every check and changes nothing. The
        response holds an empty `tasks` array. A failed check returns the same error as
        the real delete.

        Args:
          project_id: Project ID.

          placement_group_id: Placement group ID.

          dry_run: Run every check of the real request and change nothing. The response has the
              status code and the schema of the real call, and an empty list of tasks. With
              `false`, the default, the request does the operation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not placement_group_id:
            raise ValueError(f"Expected a non-empty value for `placement_group_id` but received {placement_group_id!r}")
        return await self._delete(
            path_template(
                "/cloud/v1/projects/{project_id}/placement_groups/{placement_group_id}",
                project_id=project_id,
                placement_group_id=placement_group_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"dry_run": dry_run}, placement_group_delete_params.PlacementGroupDeleteParams
                ),
            ),
            cast_to=PlacementGroupDeleteResponse,
        )

    async def get(
        self,
        placement_group_id: str,
        *,
        project_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlacementGroup:
        """
        Returns a single placement group by ID; the region is resolved from the ID, so
        it is not part of the path.

        Args:
          project_id: Project ID.

          placement_group_id: Placement group ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not placement_group_id:
            raise ValueError(f"Expected a non-empty value for `placement_group_id` but received {placement_group_id!r}")
        return await self._get(
            path_template(
                "/cloud/v1/projects/{project_id}/placement_groups/{placement_group_id}",
                project_id=project_id,
                placement_group_id=placement_group_id,
            ),
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
