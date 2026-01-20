# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional

import httpx

from .rules import (
    RulesResource,
    AsyncRulesResource,
    RulesResourceWithRawResponse,
    AsyncRulesResourceWithRawResponse,
    RulesResourceWithStreamingResponse,
    AsyncRulesResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ....types.cloud import (
    security_group_copy_params,
    security_group_list_params,
    security_group_create_params,
    security_group_update_params,
)
from ...._base_client import AsyncPaginator, make_request_options
from ....types.cloud.task_id_list import TaskIDList
from ....types.cloud.security_group import SecurityGroup
from ....types.cloud.tag_update_map_param import TagUpdateMapParam

__all__ = ["SecurityGroupsResource", "AsyncSecurityGroupsResource"]


class SecurityGroupsResource(SyncAPIResource):
    @cached_property
    def rules(self) -> RulesResource:
        return RulesResource(self._client)

    @cached_property
    def with_raw_response(self) -> SecurityGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return SecurityGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SecurityGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return SecurityGroupsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        description: str | Omit = omit,
        rules: Iterable[security_group_create_params.Rule] | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """Creates a new security group with the specified configuration.

        If no egress
        rules are provided, default set of egress rules will be applied If rules are
        explicitly set to empty, no rules will be created.

        Args:
          project_id: Project ID

          region_id: Region ID

          name: Security group name

          description: Security group description

          rules: Security group rules

          tags: Key-value tags to associate with the resource. A tag is a key-value pair that
              can be associated with a resource, enabling efficient filtering and grouping for
              better organization and management. Both tag keys and values have a maximum
              length of 255 characters. Some tags are read-only and cannot be modified by the
              user. Tags are also integrated with cost reports, allowing cost data to be
              filtered based on tag keys or values.

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
            f"/cloud/v2/security_groups/{project_id}/{region_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "rules": rules,
                    "tags": tags,
                },
                security_group_create_params.SecurityGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def update(
        self,
        group_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        description: str | Omit = omit,
        name: str | Omit = omit,
        rules: Iterable[security_group_update_params.Rule] | Omit = omit,
        tags: Optional[TagUpdateMapParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Updates the specified security group with the provided changes.

        **Behavior:**

        - Simple fields (name, description) will be updated if provided
        - Undefined fields will remain unchanged
        - If no change is detected for a specific field compared to the current security
          group state, that field will be skipped
        - If no changes are detected at all across all fields, no task will be created
          and an empty task list will be returned

        **Important - Security Group Rules:**

        - Rules must be specified completely as the desired final state
        - The system compares the provided rules against the current state
        - Rules that exist in the request but not in the current state will be added
        - Rules that exist in the current state but not in the request will be removed
        - To keep existing rules, they must be included in the request alongside any new
          rules

        Args:
          project_id: Project ID

          region_id: Region ID

          group_id: Security group ID

          description: Security group description

          name: Name

          rules: Security group rules

          tags: Update key-value tags using JSON Merge Patch semantics (RFC 7386). Provide
              key-value pairs to add or update tags. Set tag values to `null` to remove tags.
              Unspecified tags remain unchanged. Read-only tags are always preserved and
              cannot be modified.

              **Examples:**

              - **Add/update tags:**
                `{'tags': {'environment': 'production', 'team': 'backend'}}` adds new tags or
                updates existing ones.
              - **Delete tags:** `{'tags': {'old_tag': null}}` removes specific tags.
              - **Remove all tags:** `{'tags': null}` removes all user-managed tags (read-only
                tags are preserved).
              - **Partial update:** `{'tags': {'environment': 'staging'}}` only updates
                specified tags.
              - **Mixed operations:**
                `{'tags': {'environment': 'production', 'cost_center': 'engineering', 'deprecated_tag': null}}`
                adds/updates 'environment' and 'cost_center' while removing 'deprecated_tag',
                preserving other existing tags.
              - **Replace all:** first delete existing tags with null values, then add new
                ones in the same request.

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
        return self._patch(
            f"/cloud/v2/security_groups/{project_id}/{region_id}/{group_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "rules": rules,
                    "tags": tags,
                },
                security_group_update_params.SecurityGroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def list(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        limit: int | Omit = omit,
        name: str | Omit = omit,
        offset: int | Omit = omit,
        tag_key: SequenceNotStr[str] | Omit = omit,
        tag_key_value: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[SecurityGroup]:
        """
        List all security groups in the specified project and region.

        Args:
          project_id: Project ID

          region_id: Region ID

          limit: Limit of items on a single page

          name: Optional. Filter by name. Must be specified a full name of the security group.

          offset: Offset in results list

          tag_key: Optional. Filter by tag keys. ?`tag_key`=key1&`tag_key`=key2

          tag_key_value: Optional. Filter by tag key-value pairs.

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
            f"/cloud/v1/securitygroups/{project_id}/{region_id}",
            page=SyncOffsetPage[SecurityGroup],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "tag_key": tag_key,
                        "tag_key_value": tag_key_value,
                    },
                    security_group_list_params.SecurityGroupListParams,
                ),
            ),
            model=SecurityGroup,
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
    ) -> None:
        """
        Delete a specific security group and all its associated rules.

        Args:
          project_id: Project ID

          region_id: Region ID

          group_id: Group ID

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/cloud/v1/securitygroups/{project_id}/{region_id}/{group_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def copy(
        self,
        group_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SecurityGroup:
        """
        Create a deep copy of an existing security group.

        Args:
          project_id: Project ID

          region_id: Region ID

          group_id: Group ID

          name: Name.

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
        return self._post(
            f"/cloud/v1/securitygroups/{project_id}/{region_id}/{group_id}/copy",
            body=maybe_transform({"name": name}, security_group_copy_params.SecurityGroupCopyParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecurityGroup,
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
    ) -> SecurityGroup:
        """
        Get detailed information about a specific security group.

        Args:
          project_id: Project ID

          region_id: Region ID

          group_id: Group ID

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
            f"/cloud/v1/securitygroups/{project_id}/{region_id}/{group_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecurityGroup,
        )

    def revert_to_default(
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
    ) -> SecurityGroup:
        """
        Revert a security group to its previous state.

        Args:
          project_id: Project ID

          region_id: Region ID

          group_id: Group ID

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
        return self._post(
            f"/cloud/v1/securitygroups/{project_id}/{region_id}/{group_id}/revert",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecurityGroup,
        )

    def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        description: str | Omit = omit,
        rules: Iterable[security_group_create_params.Rule] | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> SecurityGroup:
        """
        Create security group and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.create(
            project_id=project_id,
            region_id=region_id,
            name=name,
            description=description,
            rules=rules,
            tags=tags,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks:
            raise ValueError("Expected at least one task to be created")
        task = self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        if task.created_resources is None or task.created_resources.security_groups is None:
            raise ValueError("Task completed but created_resources or security_groups is missing")
        security_group_id = task.created_resources.security_groups[0]
        return self.get(
            group_id=security_group_id,
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )

    def update_and_poll(
        self,
        group_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        description: str | Omit = omit,
        name: str | Omit = omit,
        rules: Iterable[security_group_update_params.Rule] | Omit = omit,
        tags: Optional[TagUpdateMapParam] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> SecurityGroup:
        """
        Update security group and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.update(
            group_id=group_id,
            project_id=project_id,
            region_id=region_id,
            description=description,
            name=name,
            rules=rules,
            tags=tags,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if response.tasks:
            self._client.cloud.tasks.poll(
                task_id=response.tasks[0],
                extra_headers=extra_headers,
                polling_interval_seconds=polling_interval_seconds,
                polling_timeout_seconds=polling_timeout_seconds,
            )
        return self.get(
            group_id=group_id,
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )


class AsyncSecurityGroupsResource(AsyncAPIResource):
    @cached_property
    def rules(self) -> AsyncRulesResource:
        return AsyncRulesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSecurityGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSecurityGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSecurityGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncSecurityGroupsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        description: str | Omit = omit,
        rules: Iterable[security_group_create_params.Rule] | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """Creates a new security group with the specified configuration.

        If no egress
        rules are provided, default set of egress rules will be applied If rules are
        explicitly set to empty, no rules will be created.

        Args:
          project_id: Project ID

          region_id: Region ID

          name: Security group name

          description: Security group description

          rules: Security group rules

          tags: Key-value tags to associate with the resource. A tag is a key-value pair that
              can be associated with a resource, enabling efficient filtering and grouping for
              better organization and management. Both tag keys and values have a maximum
              length of 255 characters. Some tags are read-only and cannot be modified by the
              user. Tags are also integrated with cost reports, allowing cost data to be
              filtered based on tag keys or values.

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
            f"/cloud/v2/security_groups/{project_id}/{region_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "rules": rules,
                    "tags": tags,
                },
                security_group_create_params.SecurityGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def update(
        self,
        group_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        description: str | Omit = omit,
        name: str | Omit = omit,
        rules: Iterable[security_group_update_params.Rule] | Omit = omit,
        tags: Optional[TagUpdateMapParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Updates the specified security group with the provided changes.

        **Behavior:**

        - Simple fields (name, description) will be updated if provided
        - Undefined fields will remain unchanged
        - If no change is detected for a specific field compared to the current security
          group state, that field will be skipped
        - If no changes are detected at all across all fields, no task will be created
          and an empty task list will be returned

        **Important - Security Group Rules:**

        - Rules must be specified completely as the desired final state
        - The system compares the provided rules against the current state
        - Rules that exist in the request but not in the current state will be added
        - Rules that exist in the current state but not in the request will be removed
        - To keep existing rules, they must be included in the request alongside any new
          rules

        Args:
          project_id: Project ID

          region_id: Region ID

          group_id: Security group ID

          description: Security group description

          name: Name

          rules: Security group rules

          tags: Update key-value tags using JSON Merge Patch semantics (RFC 7386). Provide
              key-value pairs to add or update tags. Set tag values to `null` to remove tags.
              Unspecified tags remain unchanged. Read-only tags are always preserved and
              cannot be modified.

              **Examples:**

              - **Add/update tags:**
                `{'tags': {'environment': 'production', 'team': 'backend'}}` adds new tags or
                updates existing ones.
              - **Delete tags:** `{'tags': {'old_tag': null}}` removes specific tags.
              - **Remove all tags:** `{'tags': null}` removes all user-managed tags (read-only
                tags are preserved).
              - **Partial update:** `{'tags': {'environment': 'staging'}}` only updates
                specified tags.
              - **Mixed operations:**
                `{'tags': {'environment': 'production', 'cost_center': 'engineering', 'deprecated_tag': null}}`
                adds/updates 'environment' and 'cost_center' while removing 'deprecated_tag',
                preserving other existing tags.
              - **Replace all:** first delete existing tags with null values, then add new
                ones in the same request.

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
        return await self._patch(
            f"/cloud/v2/security_groups/{project_id}/{region_id}/{group_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "rules": rules,
                    "tags": tags,
                },
                security_group_update_params.SecurityGroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def list(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        limit: int | Omit = omit,
        name: str | Omit = omit,
        offset: int | Omit = omit,
        tag_key: SequenceNotStr[str] | Omit = omit,
        tag_key_value: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[SecurityGroup, AsyncOffsetPage[SecurityGroup]]:
        """
        List all security groups in the specified project and region.

        Args:
          project_id: Project ID

          region_id: Region ID

          limit: Limit of items on a single page

          name: Optional. Filter by name. Must be specified a full name of the security group.

          offset: Offset in results list

          tag_key: Optional. Filter by tag keys. ?`tag_key`=key1&`tag_key`=key2

          tag_key_value: Optional. Filter by tag key-value pairs.

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
            f"/cloud/v1/securitygroups/{project_id}/{region_id}",
            page=AsyncOffsetPage[SecurityGroup],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "tag_key": tag_key,
                        "tag_key_value": tag_key_value,
                    },
                    security_group_list_params.SecurityGroupListParams,
                ),
            ),
            model=SecurityGroup,
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
    ) -> None:
        """
        Delete a specific security group and all its associated rules.

        Args:
          project_id: Project ID

          region_id: Region ID

          group_id: Group ID

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/cloud/v1/securitygroups/{project_id}/{region_id}/{group_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def copy(
        self,
        group_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SecurityGroup:
        """
        Create a deep copy of an existing security group.

        Args:
          project_id: Project ID

          region_id: Region ID

          group_id: Group ID

          name: Name.

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
        return await self._post(
            f"/cloud/v1/securitygroups/{project_id}/{region_id}/{group_id}/copy",
            body=await async_maybe_transform({"name": name}, security_group_copy_params.SecurityGroupCopyParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecurityGroup,
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
    ) -> SecurityGroup:
        """
        Get detailed information about a specific security group.

        Args:
          project_id: Project ID

          region_id: Region ID

          group_id: Group ID

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
            f"/cloud/v1/securitygroups/{project_id}/{region_id}/{group_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecurityGroup,
        )

    async def revert_to_default(
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
    ) -> SecurityGroup:
        """
        Revert a security group to its previous state.

        Args:
          project_id: Project ID

          region_id: Region ID

          group_id: Group ID

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
        return await self._post(
            f"/cloud/v1/securitygroups/{project_id}/{region_id}/{group_id}/revert",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecurityGroup,
        )

    async def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        description: str | Omit = omit,
        rules: Iterable[security_group_create_params.Rule] | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> SecurityGroup:
        """
        Create security group and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.create(
            project_id=project_id,
            region_id=region_id,
            name=name,
            description=description,
            rules=rules,
            tags=tags,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks:
            raise ValueError("Expected at least one task to be created")
        task = await self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        if task.created_resources is None or task.created_resources.security_groups is None:
            raise ValueError("Task completed but created_resources or security_groups is missing")
        security_group_id = task.created_resources.security_groups[0]
        return await self.get(
            group_id=security_group_id,
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )

    async def update_and_poll(
        self,
        group_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        description: str | Omit = omit,
        name: str | Omit = omit,
        rules: Iterable[security_group_update_params.Rule] | Omit = omit,
        tags: Optional[TagUpdateMapParam] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> SecurityGroup:
        """
        Update security group and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.update(
            group_id=group_id,
            project_id=project_id,
            region_id=region_id,
            description=description,
            name=name,
            rules=rules,
            tags=tags,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if response.tasks:
            await self._client.cloud.tasks.poll(
                task_id=response.tasks[0],
                extra_headers=extra_headers,
                polling_interval_seconds=polling_interval_seconds,
                polling_timeout_seconds=polling_timeout_seconds,
            )
        return await self.get(
            group_id=group_id,
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )


class SecurityGroupsResourceWithRawResponse:
    def __init__(self, security_groups: SecurityGroupsResource) -> None:
        self._security_groups = security_groups

        self.create = to_raw_response_wrapper(
            security_groups.create,
        )
        self.update = to_raw_response_wrapper(
            security_groups.update,
        )
        self.list = to_raw_response_wrapper(
            security_groups.list,
        )
        self.delete = to_raw_response_wrapper(
            security_groups.delete,
        )
        self.copy = to_raw_response_wrapper(
            security_groups.copy,
        )
        self.get = to_raw_response_wrapper(
            security_groups.get,
        )
        self.revert_to_default = to_raw_response_wrapper(
            security_groups.revert_to_default,
        )
        self.create_and_poll = to_raw_response_wrapper(
            security_groups.create_and_poll,
        )
        self.update_and_poll = to_raw_response_wrapper(
            security_groups.update_and_poll,
        )

    @cached_property
    def rules(self) -> RulesResourceWithRawResponse:
        return RulesResourceWithRawResponse(self._security_groups.rules)


class AsyncSecurityGroupsResourceWithRawResponse:
    def __init__(self, security_groups: AsyncSecurityGroupsResource) -> None:
        self._security_groups = security_groups

        self.create = async_to_raw_response_wrapper(
            security_groups.create,
        )
        self.update = async_to_raw_response_wrapper(
            security_groups.update,
        )
        self.list = async_to_raw_response_wrapper(
            security_groups.list,
        )
        self.delete = async_to_raw_response_wrapper(
            security_groups.delete,
        )
        self.copy = async_to_raw_response_wrapper(
            security_groups.copy,
        )
        self.get = async_to_raw_response_wrapper(
            security_groups.get,
        )
        self.revert_to_default = async_to_raw_response_wrapper(
            security_groups.revert_to_default,
        )
        self.create_and_poll = async_to_raw_response_wrapper(
            security_groups.create_and_poll,
        )
        self.update_and_poll = async_to_raw_response_wrapper(
            security_groups.update_and_poll,
        )

    @cached_property
    def rules(self) -> AsyncRulesResourceWithRawResponse:
        return AsyncRulesResourceWithRawResponse(self._security_groups.rules)


class SecurityGroupsResourceWithStreamingResponse:
    def __init__(self, security_groups: SecurityGroupsResource) -> None:
        self._security_groups = security_groups

        self.create = to_streamed_response_wrapper(
            security_groups.create,
        )
        self.update = to_streamed_response_wrapper(
            security_groups.update,
        )
        self.list = to_streamed_response_wrapper(
            security_groups.list,
        )
        self.delete = to_streamed_response_wrapper(
            security_groups.delete,
        )
        self.copy = to_streamed_response_wrapper(
            security_groups.copy,
        )
        self.get = to_streamed_response_wrapper(
            security_groups.get,
        )
        self.revert_to_default = to_streamed_response_wrapper(
            security_groups.revert_to_default,
        )
        self.create_and_poll = to_streamed_response_wrapper(
            security_groups.create_and_poll,
        )
        self.update_and_poll = to_streamed_response_wrapper(
            security_groups.update_and_poll,
        )

    @cached_property
    def rules(self) -> RulesResourceWithStreamingResponse:
        return RulesResourceWithStreamingResponse(self._security_groups.rules)


class AsyncSecurityGroupsResourceWithStreamingResponse:
    def __init__(self, security_groups: AsyncSecurityGroupsResource) -> None:
        self._security_groups = security_groups

        self.create = async_to_streamed_response_wrapper(
            security_groups.create,
        )
        self.update = async_to_streamed_response_wrapper(
            security_groups.update,
        )
        self.list = async_to_streamed_response_wrapper(
            security_groups.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            security_groups.delete,
        )
        self.copy = async_to_streamed_response_wrapper(
            security_groups.copy,
        )
        self.get = async_to_streamed_response_wrapper(
            security_groups.get,
        )
        self.revert_to_default = async_to_streamed_response_wrapper(
            security_groups.revert_to_default,
        )
        self.create_and_poll = async_to_streamed_response_wrapper(
            security_groups.create_and_poll,
        )
        self.update_and_poll = async_to_streamed_response_wrapper(
            security_groups.update_and_poll,
        )

    @cached_property
    def rules(self) -> AsyncRulesResourceWithStreamingResponse:
        return AsyncRulesResourceWithStreamingResponse(self._security_groups.rules)
