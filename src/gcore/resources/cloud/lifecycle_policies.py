# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.cloud import (
    lifecycle_policy_create_params,
    lifecycle_policy_update_params,
    lifecycle_policy_add_volumes_params,
    lifecycle_policy_add_schedules_params,
    lifecycle_policy_remove_volumes_params,
    lifecycle_policy_remove_schedules_params,
    lifecycle_policy_estimate_max_usage_params,
)
from ..._base_client import make_request_options
from ...types.cloud.lifecycle_policy import LifecyclePolicy
from ...types.cloud.lifecycle_policy_list_response import LifecyclePolicyListResponse
from ...types.cloud.lifecycle_policy_estimate_max_usage_response import LifecyclePolicyEstimateMaxUsageResponse

__all__ = ["LifecyclePoliciesResource", "AsyncLifecyclePoliciesResource"]


class LifecyclePoliciesResource(SyncAPIResource):
    """
    Snapshot schedule policies describe when volume snapshots are taken and which volumes they cover. Volume membership is owned by the policy: attach and detach are policy-side operations, so a volume can join or leave a policy without being recreated.
    """

    @cached_property
    def with_raw_response(self) -> LifecyclePoliciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return LifecyclePoliciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LifecyclePoliciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return LifecyclePoliciesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["volume_snapshot"],
        name: str,
        schedules: Iterable[lifecycle_policy_create_params.Schedule] | Omit = omit,
        status: Literal["active", "paused"] | Omit = omit,
        volume_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LifecyclePolicy:
        """
        Create a new snapshot policy with the specified configuration.

        Args:
          project_id: Project ID

          region_id: Region ID

          action: Action that the policy will perform.

          name: Name of the lifecycle policy.

          schedules: List of schedules associated with the policy.

          status: Current status of the lifecycle policy.

          volume_ids: List of volume IDs.

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
                "/cloud/v1/lifecycle_policy/{project_id}/{region_id}", project_id=project_id, region_id=region_id
            ),
            body=maybe_transform(
                {
                    "action": action,
                    "name": name,
                    "schedules": schedules,
                    "status": status,
                    "volume_ids": volume_ids,
                },
                lifecycle_policy_create_params.LifecyclePolicyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LifecyclePolicy,
        )

    def update(
        self,
        policy_id: int,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str | Omit = omit,
        status: Literal["active", "paused"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LifecyclePolicy:
        """
        Update the configuration of an existing snapshot policy.

        Args:
          project_id: Project ID

          region_id: Region ID

          policy_id: Lifecycle policy ID.

          name: Name of the lifecycle policy.

          status: Status of the lifecycle policy.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return self._patch(
            path_template(
                "/cloud/v1/lifecycle_policy/{project_id}/{region_id}/{policy_id}",
                project_id=project_id,
                region_id=region_id,
                policy_id=policy_id,
            ),
            body=maybe_transform(
                {
                    "name": name,
                    "status": status,
                },
                lifecycle_policy_update_params.LifecyclePolicyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LifecyclePolicy,
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
    ) -> LifecyclePolicyListResponse:
        """
        List all snapshot policies in the specified project and region.

        Args:
          project_id: Project ID

          region_id: Region ID

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
            path_template(
                "/cloud/v1/lifecycle_policy/{project_id}/{region_id}", project_id=project_id, region_id=region_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LifecyclePolicyListResponse,
        )

    def delete(
        self,
        policy_id: int,
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
        Delete a specific snapshot policy and all its associated schedules.

        Args:
          project_id: Project ID

          region_id: Region ID

          policy_id: Lifecycle policy ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/cloud/v1/lifecycle_policy/{project_id}/{region_id}/{policy_id}",
                project_id=project_id,
                region_id=region_id,
                policy_id=policy_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def add_schedules(
        self,
        policy_id: int,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        schedules: Iterable[lifecycle_policy_add_schedules_params.Schedule],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LifecyclePolicy:
        """
        Add new schedules to an existing snapshot policy.

        Args:
          project_id: Project ID

          region_id: Region ID

          policy_id: Lifecycle policy ID.

          schedules: List of schedules associated with the policy.

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
                "/cloud/v1/lifecycle_policy/{project_id}/{region_id}/{policy_id}/add_schedules",
                project_id=project_id,
                region_id=region_id,
                policy_id=policy_id,
            ),
            body=maybe_transform(
                {"schedules": schedules}, lifecycle_policy_add_schedules_params.LifecyclePolicyAddSchedulesParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LifecyclePolicy,
        )

    def add_volumes(
        self,
        policy_id: int,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        volume_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LifecyclePolicy:
        """
        Add volumes to an existing snapshot policy.

        Args:
          project_id: Project ID

          region_id: Region ID

          policy_id: Lifecycle policy ID.

          volume_ids: List of volume IDs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return self._put(
            path_template(
                "/cloud/v1/lifecycle_policy/{project_id}/{region_id}/{policy_id}/add_volumes_to_policy",
                project_id=project_id,
                region_id=region_id,
                policy_id=policy_id,
            ),
            body=maybe_transform(
                {"volume_ids": volume_ids}, lifecycle_policy_add_volumes_params.LifecyclePolicyAddVolumesParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LifecyclePolicy,
        )

    def estimate_max_usage(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["volume_snapshot"],
        name: str,
        schedules: Iterable[lifecycle_policy_estimate_max_usage_params.Schedule] | Omit = omit,
        status: Literal["active", "paused"] | Omit = omit,
        volume_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LifecyclePolicyEstimateMaxUsageResponse:
        """
        Calculate the maximum resource usage if all snapshots are created by the policy.

        Args:
          project_id: Project ID

          region_id: Region ID

          action: Action that the policy will perform.

          name: Name of the lifecycle policy.

          schedules: List of schedules associated with the policy.

          status: Current status of the lifecycle policy.

          volume_ids: List of volume IDs.

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
                "/cloud/v1/lifecycle_policy/{project_id}/{region_id}/estimate_max_policy_usage",
                project_id=project_id,
                region_id=region_id,
            ),
            body=maybe_transform(
                {
                    "action": action,
                    "name": name,
                    "schedules": schedules,
                    "status": status,
                    "volume_ids": volume_ids,
                },
                lifecycle_policy_estimate_max_usage_params.LifecyclePolicyEstimateMaxUsageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LifecyclePolicyEstimateMaxUsageResponse,
        )

    def get(
        self,
        policy_id: int,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LifecyclePolicy:
        """
        Get detailed information about a specific snapshot policy.

        Args:
          project_id: Project ID

          region_id: Region ID

          policy_id: Lifecycle policy ID.

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
            path_template(
                "/cloud/v1/lifecycle_policy/{project_id}/{region_id}/{policy_id}",
                project_id=project_id,
                region_id=region_id,
                policy_id=policy_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LifecyclePolicy,
        )

    def remove_schedules(
        self,
        policy_id: int,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        schedule_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LifecyclePolicy:
        """
        Remove schedules from an existing snapshot policy.

        Args:
          project_id: Project ID

          region_id: Region ID

          policy_id: Lifecycle policy ID.

          schedule_ids: List of schedule IDs.

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
                "/cloud/v1/lifecycle_policy/{project_id}/{region_id}/{policy_id}/remove_schedules",
                project_id=project_id,
                region_id=region_id,
                policy_id=policy_id,
            ),
            body=maybe_transform(
                {"schedule_ids": schedule_ids},
                lifecycle_policy_remove_schedules_params.LifecyclePolicyRemoveSchedulesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LifecyclePolicy,
        )

    def remove_volumes(
        self,
        policy_id: int,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        volume_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LifecyclePolicy:
        """
        Remove volumes from an existing snapshot policy.

        Args:
          project_id: Project ID

          region_id: Region ID

          policy_id: Lifecycle policy ID.

          volume_ids: List of volume IDs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return self._put(
            path_template(
                "/cloud/v1/lifecycle_policy/{project_id}/{region_id}/{policy_id}/remove_volumes_from_policy",
                project_id=project_id,
                region_id=region_id,
                policy_id=policy_id,
            ),
            body=maybe_transform(
                {"volume_ids": volume_ids}, lifecycle_policy_remove_volumes_params.LifecyclePolicyRemoveVolumesParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LifecyclePolicy,
        )


class AsyncLifecyclePoliciesResource(AsyncAPIResource):
    """
    Snapshot schedule policies describe when volume snapshots are taken and which volumes they cover. Volume membership is owned by the policy: attach and detach are policy-side operations, so a volume can join or leave a policy without being recreated.
    """

    @cached_property
    def with_raw_response(self) -> AsyncLifecyclePoliciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLifecyclePoliciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLifecyclePoliciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncLifecyclePoliciesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["volume_snapshot"],
        name: str,
        schedules: Iterable[lifecycle_policy_create_params.Schedule] | Omit = omit,
        status: Literal["active", "paused"] | Omit = omit,
        volume_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LifecyclePolicy:
        """
        Create a new snapshot policy with the specified configuration.

        Args:
          project_id: Project ID

          region_id: Region ID

          action: Action that the policy will perform.

          name: Name of the lifecycle policy.

          schedules: List of schedules associated with the policy.

          status: Current status of the lifecycle policy.

          volume_ids: List of volume IDs.

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
                "/cloud/v1/lifecycle_policy/{project_id}/{region_id}", project_id=project_id, region_id=region_id
            ),
            body=await async_maybe_transform(
                {
                    "action": action,
                    "name": name,
                    "schedules": schedules,
                    "status": status,
                    "volume_ids": volume_ids,
                },
                lifecycle_policy_create_params.LifecyclePolicyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LifecyclePolicy,
        )

    async def update(
        self,
        policy_id: int,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str | Omit = omit,
        status: Literal["active", "paused"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LifecyclePolicy:
        """
        Update the configuration of an existing snapshot policy.

        Args:
          project_id: Project ID

          region_id: Region ID

          policy_id: Lifecycle policy ID.

          name: Name of the lifecycle policy.

          status: Status of the lifecycle policy.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return await self._patch(
            path_template(
                "/cloud/v1/lifecycle_policy/{project_id}/{region_id}/{policy_id}",
                project_id=project_id,
                region_id=region_id,
                policy_id=policy_id,
            ),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "status": status,
                },
                lifecycle_policy_update_params.LifecyclePolicyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LifecyclePolicy,
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
    ) -> LifecyclePolicyListResponse:
        """
        List all snapshot policies in the specified project and region.

        Args:
          project_id: Project ID

          region_id: Region ID

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
            path_template(
                "/cloud/v1/lifecycle_policy/{project_id}/{region_id}", project_id=project_id, region_id=region_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LifecyclePolicyListResponse,
        )

    async def delete(
        self,
        policy_id: int,
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
        Delete a specific snapshot policy and all its associated schedules.

        Args:
          project_id: Project ID

          region_id: Region ID

          policy_id: Lifecycle policy ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/cloud/v1/lifecycle_policy/{project_id}/{region_id}/{policy_id}",
                project_id=project_id,
                region_id=region_id,
                policy_id=policy_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def add_schedules(
        self,
        policy_id: int,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        schedules: Iterable[lifecycle_policy_add_schedules_params.Schedule],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LifecyclePolicy:
        """
        Add new schedules to an existing snapshot policy.

        Args:
          project_id: Project ID

          region_id: Region ID

          policy_id: Lifecycle policy ID.

          schedules: List of schedules associated with the policy.

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
                "/cloud/v1/lifecycle_policy/{project_id}/{region_id}/{policy_id}/add_schedules",
                project_id=project_id,
                region_id=region_id,
                policy_id=policy_id,
            ),
            body=await async_maybe_transform(
                {"schedules": schedules}, lifecycle_policy_add_schedules_params.LifecyclePolicyAddSchedulesParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LifecyclePolicy,
        )

    async def add_volumes(
        self,
        policy_id: int,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        volume_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LifecyclePolicy:
        """
        Add volumes to an existing snapshot policy.

        Args:
          project_id: Project ID

          region_id: Region ID

          policy_id: Lifecycle policy ID.

          volume_ids: List of volume IDs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return await self._put(
            path_template(
                "/cloud/v1/lifecycle_policy/{project_id}/{region_id}/{policy_id}/add_volumes_to_policy",
                project_id=project_id,
                region_id=region_id,
                policy_id=policy_id,
            ),
            body=await async_maybe_transform(
                {"volume_ids": volume_ids}, lifecycle_policy_add_volumes_params.LifecyclePolicyAddVolumesParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LifecyclePolicy,
        )

    async def estimate_max_usage(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["volume_snapshot"],
        name: str,
        schedules: Iterable[lifecycle_policy_estimate_max_usage_params.Schedule] | Omit = omit,
        status: Literal["active", "paused"] | Omit = omit,
        volume_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LifecyclePolicyEstimateMaxUsageResponse:
        """
        Calculate the maximum resource usage if all snapshots are created by the policy.

        Args:
          project_id: Project ID

          region_id: Region ID

          action: Action that the policy will perform.

          name: Name of the lifecycle policy.

          schedules: List of schedules associated with the policy.

          status: Current status of the lifecycle policy.

          volume_ids: List of volume IDs.

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
                "/cloud/v1/lifecycle_policy/{project_id}/{region_id}/estimate_max_policy_usage",
                project_id=project_id,
                region_id=region_id,
            ),
            body=await async_maybe_transform(
                {
                    "action": action,
                    "name": name,
                    "schedules": schedules,
                    "status": status,
                    "volume_ids": volume_ids,
                },
                lifecycle_policy_estimate_max_usage_params.LifecyclePolicyEstimateMaxUsageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LifecyclePolicyEstimateMaxUsageResponse,
        )

    async def get(
        self,
        policy_id: int,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LifecyclePolicy:
        """
        Get detailed information about a specific snapshot policy.

        Args:
          project_id: Project ID

          region_id: Region ID

          policy_id: Lifecycle policy ID.

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
            path_template(
                "/cloud/v1/lifecycle_policy/{project_id}/{region_id}/{policy_id}",
                project_id=project_id,
                region_id=region_id,
                policy_id=policy_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LifecyclePolicy,
        )

    async def remove_schedules(
        self,
        policy_id: int,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        schedule_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LifecyclePolicy:
        """
        Remove schedules from an existing snapshot policy.

        Args:
          project_id: Project ID

          region_id: Region ID

          policy_id: Lifecycle policy ID.

          schedule_ids: List of schedule IDs.

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
                "/cloud/v1/lifecycle_policy/{project_id}/{region_id}/{policy_id}/remove_schedules",
                project_id=project_id,
                region_id=region_id,
                policy_id=policy_id,
            ),
            body=await async_maybe_transform(
                {"schedule_ids": schedule_ids},
                lifecycle_policy_remove_schedules_params.LifecyclePolicyRemoveSchedulesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LifecyclePolicy,
        )

    async def remove_volumes(
        self,
        policy_id: int,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        volume_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LifecyclePolicy:
        """
        Remove volumes from an existing snapshot policy.

        Args:
          project_id: Project ID

          region_id: Region ID

          policy_id: Lifecycle policy ID.

          volume_ids: List of volume IDs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return await self._put(
            path_template(
                "/cloud/v1/lifecycle_policy/{project_id}/{region_id}/{policy_id}/remove_volumes_from_policy",
                project_id=project_id,
                region_id=region_id,
                policy_id=policy_id,
            ),
            body=await async_maybe_transform(
                {"volume_ids": volume_ids}, lifecycle_policy_remove_volumes_params.LifecyclePolicyRemoveVolumesParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LifecyclePolicy,
        )


class LifecyclePoliciesResourceWithRawResponse:
    def __init__(self, lifecycle_policies: LifecyclePoliciesResource) -> None:
        self._lifecycle_policies = lifecycle_policies

        self.create = to_raw_response_wrapper(
            lifecycle_policies.create,
        )
        self.update = to_raw_response_wrapper(
            lifecycle_policies.update,
        )
        self.list = to_raw_response_wrapper(
            lifecycle_policies.list,
        )
        self.delete = to_raw_response_wrapper(
            lifecycle_policies.delete,
        )
        self.add_schedules = to_raw_response_wrapper(
            lifecycle_policies.add_schedules,
        )
        self.add_volumes = to_raw_response_wrapper(
            lifecycle_policies.add_volumes,
        )
        self.estimate_max_usage = to_raw_response_wrapper(
            lifecycle_policies.estimate_max_usage,
        )
        self.get = to_raw_response_wrapper(
            lifecycle_policies.get,
        )
        self.remove_schedules = to_raw_response_wrapper(
            lifecycle_policies.remove_schedules,
        )
        self.remove_volumes = to_raw_response_wrapper(
            lifecycle_policies.remove_volumes,
        )


class AsyncLifecyclePoliciesResourceWithRawResponse:
    def __init__(self, lifecycle_policies: AsyncLifecyclePoliciesResource) -> None:
        self._lifecycle_policies = lifecycle_policies

        self.create = async_to_raw_response_wrapper(
            lifecycle_policies.create,
        )
        self.update = async_to_raw_response_wrapper(
            lifecycle_policies.update,
        )
        self.list = async_to_raw_response_wrapper(
            lifecycle_policies.list,
        )
        self.delete = async_to_raw_response_wrapper(
            lifecycle_policies.delete,
        )
        self.add_schedules = async_to_raw_response_wrapper(
            lifecycle_policies.add_schedules,
        )
        self.add_volumes = async_to_raw_response_wrapper(
            lifecycle_policies.add_volumes,
        )
        self.estimate_max_usage = async_to_raw_response_wrapper(
            lifecycle_policies.estimate_max_usage,
        )
        self.get = async_to_raw_response_wrapper(
            lifecycle_policies.get,
        )
        self.remove_schedules = async_to_raw_response_wrapper(
            lifecycle_policies.remove_schedules,
        )
        self.remove_volumes = async_to_raw_response_wrapper(
            lifecycle_policies.remove_volumes,
        )


class LifecyclePoliciesResourceWithStreamingResponse:
    def __init__(self, lifecycle_policies: LifecyclePoliciesResource) -> None:
        self._lifecycle_policies = lifecycle_policies

        self.create = to_streamed_response_wrapper(
            lifecycle_policies.create,
        )
        self.update = to_streamed_response_wrapper(
            lifecycle_policies.update,
        )
        self.list = to_streamed_response_wrapper(
            lifecycle_policies.list,
        )
        self.delete = to_streamed_response_wrapper(
            lifecycle_policies.delete,
        )
        self.add_schedules = to_streamed_response_wrapper(
            lifecycle_policies.add_schedules,
        )
        self.add_volumes = to_streamed_response_wrapper(
            lifecycle_policies.add_volumes,
        )
        self.estimate_max_usage = to_streamed_response_wrapper(
            lifecycle_policies.estimate_max_usage,
        )
        self.get = to_streamed_response_wrapper(
            lifecycle_policies.get,
        )
        self.remove_schedules = to_streamed_response_wrapper(
            lifecycle_policies.remove_schedules,
        )
        self.remove_volumes = to_streamed_response_wrapper(
            lifecycle_policies.remove_volumes,
        )


class AsyncLifecyclePoliciesResourceWithStreamingResponse:
    def __init__(self, lifecycle_policies: AsyncLifecyclePoliciesResource) -> None:
        self._lifecycle_policies = lifecycle_policies

        self.create = async_to_streamed_response_wrapper(
            lifecycle_policies.create,
        )
        self.update = async_to_streamed_response_wrapper(
            lifecycle_policies.update,
        )
        self.list = async_to_streamed_response_wrapper(
            lifecycle_policies.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            lifecycle_policies.delete,
        )
        self.add_schedules = async_to_streamed_response_wrapper(
            lifecycle_policies.add_schedules,
        )
        self.add_volumes = async_to_streamed_response_wrapper(
            lifecycle_policies.add_volumes,
        )
        self.estimate_max_usage = async_to_streamed_response_wrapper(
            lifecycle_policies.estimate_max_usage,
        )
        self.get = async_to_streamed_response_wrapper(
            lifecycle_policies.get,
        )
        self.remove_schedules = async_to_streamed_response_wrapper(
            lifecycle_policies.remove_schedules,
        )
        self.remove_volumes = async_to_streamed_response_wrapper(
            lifecycle_policies.remove_volumes,
        )
