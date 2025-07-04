# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional

import httpx

from .rules import (
    RulesResource,
    AsyncRulesResource,
    RulesResourceWithRawResponse,
    AsyncRulesResourceWithRawResponse,
    RulesResourceWithStreamingResponse,
    AsyncRulesResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
        security_group: security_group_create_params.SecurityGroup,
        instances: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecurityGroup:
        """
        Create a new security group with the specified configuration.

        Args:
          security_group: Security group

          instances: List of instances

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
            f"/cloud/v1/securitygroups/{project_id}/{region_id}",
            body=maybe_transform(
                {
                    "security_group": security_group,
                    "instances": instances,
                },
                security_group_create_params.SecurityGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecurityGroup,
        )

    def update(
        self,
        group_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        changed_rules: Iterable[security_group_update_params.ChangedRule] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        tags: Optional[TagUpdateMapParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecurityGroup:
        """
        Update the configuration of an existing security group.

        Args:
          changed_rules: List of rules to create or delete

          name: Name

          tags: Update key-value tags using JSON Merge Patch semantics (RFC 7386). Provide
              key-value pairs to add or update tags. Set tag values to `null` to remove tags.
              Unspecified tags remain unchanged. Read-only tags are always preserved and
              cannot be modified. **Examples:**

              - **Add/update tags:**
                `{'tags': {'environment': 'production', 'team': 'backend'}}` adds new tags or
                updates existing ones.
              - **Delete tags:** `{'tags': {'`old_tag`': null}}` removes specific tags.
              - **Remove all tags:** `{'tags': null}` removes all user-managed tags (read-only
                tags are preserved).
              - **Partial update:** `{'tags': {'environment': 'staging'}}` only updates
                specified tags.
              - **Mixed operations:**
                `{'tags': {'environment': 'production', '`cost_center`': 'engineering', '`deprecated_tag`': null}}`
                adds/updates 'environment' and '`cost_center`' while removing
                '`deprecated_tag`', preserving other existing tags.
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
            f"/cloud/v1/securitygroups/{project_id}/{region_id}/{group_id}",
            body=maybe_transform(
                {
                    "changed_rules": changed_rules,
                    "name": name,
                    "tags": tags,
                },
                security_group_update_params.SecurityGroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecurityGroup,
        )

    def list(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        tag_key: List[str] | NotGiven = NOT_GIVEN,
        tag_key_value: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[SecurityGroup]:
        """
        List all security groups in the specified project and region.

        Args:
          limit: Limit the number of returned security groups

          offset: Offset value is used to exclude the first set of records from the result

          tag_key: Filter by tag keys.

          tag_key_value: Filter by tag key-value pairs. Must be a valid JSON string.

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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a specific security group and all its associated rules.

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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecurityGroup:
        """
        Create a deep copy of an existing security group.

        Args:
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecurityGroup:
        """
        Get detailed information about a specific security group.

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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecurityGroup:
        """
        Revert a security group to its previous state.

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
        return self._post(
            f"/cloud/v1/securitygroups/{project_id}/{region_id}/{group_id}/revert",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecurityGroup,
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
        security_group: security_group_create_params.SecurityGroup,
        instances: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecurityGroup:
        """
        Create a new security group with the specified configuration.

        Args:
          security_group: Security group

          instances: List of instances

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
            f"/cloud/v1/securitygroups/{project_id}/{region_id}",
            body=await async_maybe_transform(
                {
                    "security_group": security_group,
                    "instances": instances,
                },
                security_group_create_params.SecurityGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecurityGroup,
        )

    async def update(
        self,
        group_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        changed_rules: Iterable[security_group_update_params.ChangedRule] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        tags: Optional[TagUpdateMapParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecurityGroup:
        """
        Update the configuration of an existing security group.

        Args:
          changed_rules: List of rules to create or delete

          name: Name

          tags: Update key-value tags using JSON Merge Patch semantics (RFC 7386). Provide
              key-value pairs to add or update tags. Set tag values to `null` to remove tags.
              Unspecified tags remain unchanged. Read-only tags are always preserved and
              cannot be modified. **Examples:**

              - **Add/update tags:**
                `{'tags': {'environment': 'production', 'team': 'backend'}}` adds new tags or
                updates existing ones.
              - **Delete tags:** `{'tags': {'`old_tag`': null}}` removes specific tags.
              - **Remove all tags:** `{'tags': null}` removes all user-managed tags (read-only
                tags are preserved).
              - **Partial update:** `{'tags': {'environment': 'staging'}}` only updates
                specified tags.
              - **Mixed operations:**
                `{'tags': {'environment': 'production', '`cost_center`': 'engineering', '`deprecated_tag`': null}}`
                adds/updates 'environment' and '`cost_center`' while removing
                '`deprecated_tag`', preserving other existing tags.
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
            f"/cloud/v1/securitygroups/{project_id}/{region_id}/{group_id}",
            body=await async_maybe_transform(
                {
                    "changed_rules": changed_rules,
                    "name": name,
                    "tags": tags,
                },
                security_group_update_params.SecurityGroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecurityGroup,
        )

    def list(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        tag_key: List[str] | NotGiven = NOT_GIVEN,
        tag_key_value: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[SecurityGroup, AsyncOffsetPage[SecurityGroup]]:
        """
        List all security groups in the specified project and region.

        Args:
          limit: Limit the number of returned security groups

          offset: Offset value is used to exclude the first set of records from the result

          tag_key: Filter by tag keys.

          tag_key_value: Filter by tag key-value pairs. Must be a valid JSON string.

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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a specific security group and all its associated rules.

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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecurityGroup:
        """
        Create a deep copy of an existing security group.

        Args:
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecurityGroup:
        """
        Get detailed information about a specific security group.

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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecurityGroup:
        """
        Revert a security group to its previous state.

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
        return await self._post(
            f"/cloud/v1/securitygroups/{project_id}/{region_id}/{group_id}/revert",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecurityGroup,
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

    @cached_property
    def rules(self) -> AsyncRulesResourceWithStreamingResponse:
        return AsyncRulesResourceWithStreamingResponse(self._security_groups.rules)
