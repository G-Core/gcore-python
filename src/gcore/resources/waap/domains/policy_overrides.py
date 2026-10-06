# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
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
from ....types.waap.domains import (
    policy_override_list_params,
    policy_override_create_params,
    policy_override_update_params,
    policy_override_list_owasp_top_threats_targets_params,
)
from ....types.waap.domains.waap_policy_override import WaapPolicyOverride
from ....types.waap.domains.waap_owasp_top_threats_target import WaapOwaspTopThreatsTarget

__all__ = ["PolicyOverridesResource", "AsyncPolicyOverridesResource"]


class PolicyOverridesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PolicyOverridesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return PolicyOverridesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PolicyOverridesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return PolicyOverridesResourceWithStreamingResponse(self)

    def create(
        self,
        domain_id: int,
        *,
        enabled: bool,
        name: str,
        target_ids: Iterable[int],
        target_type: Literal["detector", "rule"],
        conditions: Iterable[policy_override_create_params.Condition] | Omit = omit,
        description: Optional[str] | Omit = omit,
        request_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapPolicyOverride:
        """
        Create a policy override

        Args:
          domain_id: The domain ID

          enabled: Whether the override is active

          name: The policy override's display name

          target_ids: The detectors or rules this override suppresses

          target_type: Whether `target_ids` are detector IDs or rule IDs

          conditions: The conditions required for the override to apply. An override may have up to 5
              conditions; all must pass for the override to apply. Without conditions the
              override applies to every request on the owning domain that hits a linked
              target.

          description: An optional note explaining the override

          request_id: The ID of the request that prompted this override, if created from Event
              Details. Preserves a snapshot of that request for audit purposes; has no effect
              on override behavior and is not returned by this API.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            path_template("/waap/v1/domains/{domain_id}/default-rule-overrides", domain_id=domain_id),
            body=maybe_transform(
                {
                    "enabled": enabled,
                    "name": name,
                    "target_ids": target_ids,
                    "target_type": target_type,
                    "conditions": conditions,
                    "description": description,
                    "request_id": request_id,
                },
                policy_override_create_params.PolicyOverrideCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapPolicyOverride,
        )

    def update(
        self,
        policy_override_id: int,
        *,
        domain_id: int,
        conditions: Optional[Iterable[policy_override_update_params.Condition]] | Omit = omit,
        description: Optional[str] | Omit = omit,
        enabled: Optional[bool] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapPolicyOverride:
        """
        Update a policy override

        Args:
          domain_id: The domain ID

          policy_override_id: Policy override ID

          conditions: The conditions required for the override to apply. An override may have up to 5
              conditions; all must pass for the override to apply. Without conditions the
              override applies to every request on the owning domain that hits a linked
              target.

          description: An optional note explaining the override

          enabled: Whether the override is active

          name: The policy override's display name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            path_template(
                "/waap/v1/domains/{domain_id}/default-rule-overrides/{policy_override_id}",
                domain_id=domain_id,
                policy_override_id=policy_override_id,
            ),
            body=maybe_transform(
                {
                    "conditions": conditions,
                    "description": description,
                    "enabled": enabled,
                    "name": name,
                },
                policy_override_update_params.PolicyOverrideUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapPolicyOverride,
        )

    def list(
        self,
        domain_id: int,
        *,
        enabled: Optional[bool] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        ordering: Optional[
            Literal[
                "id",
                "name",
                "target_type",
                "enabled",
                "stale",
                "created_at",
                "updated_at",
                "-id",
                "-name",
                "-target_type",
                "-enabled",
                "-stale",
                "-created_at",
                "-updated_at",
            ]
        ]
        | Omit = omit,
        search: Optional[str] | Omit = omit,
        target_type: Optional[Literal["detector", "rule"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[WaapPolicyOverride]:
        """
        Retrieve policy overrides

        Args:
          domain_id: The domain ID

          enabled: Filter by enabled state.

          limit: Number of items to return

          offset: Number of items to skip

          ordering: Determine the field used to order results.

          search: Search policy override names and descriptions.

          target_type: Filter by linked target type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            path_template("/waap/v1/domains/{domain_id}/default-rule-overrides", domain_id=domain_id),
            page=SyncOffsetPage[WaapPolicyOverride],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "enabled": enabled,
                        "limit": limit,
                        "offset": offset,
                        "ordering": ordering,
                        "search": search,
                        "target_type": target_type,
                    },
                    policy_override_list_params.PolicyOverrideListParams,
                ),
            ),
            model=WaapPolicyOverride,
        )

    def delete(
        self,
        policy_override_id: int,
        *,
        domain_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a policy override

        Args:
          domain_id: The domain ID

          policy_override_id: Policy override ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/waap/v1/domains/{domain_id}/default-rule-overrides/{policy_override_id}",
                domain_id=domain_id,
                policy_override_id=policy_override_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        policy_override_id: int,
        *,
        domain_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapPolicyOverride:
        """
        Retrieve a policy override

        Args:
          domain_id: The domain ID

          policy_override_id: Policy override ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template(
                "/waap/v1/domains/{domain_id}/default-rule-overrides/{policy_override_id}",
                domain_id=domain_id,
                policy_override_id=policy_override_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapPolicyOverride,
        )

    def list_owasp_top_threats_targets(
        self,
        domain_id: int,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[WaapOwaspTopThreatsTarget]:
        """
        List OWASP Top Threats targets selectable as a policy override target

        Args:
          domain_id: The domain ID

          limit: Number of items to return

          offset: Number of items to skip

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            path_template(
                "/waap/v1/domains/{domain_id}/policy-override-targets/owasp-top-threats", domain_id=domain_id
            ),
            page=SyncOffsetPage[WaapOwaspTopThreatsTarget],
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
                    policy_override_list_owasp_top_threats_targets_params.PolicyOverrideListOwaspTopThreatsTargetsParams,
                ),
            ),
            model=WaapOwaspTopThreatsTarget,
        )


class AsyncPolicyOverridesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPolicyOverridesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPolicyOverridesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPolicyOverridesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncPolicyOverridesResourceWithStreamingResponse(self)

    async def create(
        self,
        domain_id: int,
        *,
        enabled: bool,
        name: str,
        target_ids: Iterable[int],
        target_type: Literal["detector", "rule"],
        conditions: Iterable[policy_override_create_params.Condition] | Omit = omit,
        description: Optional[str] | Omit = omit,
        request_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapPolicyOverride:
        """
        Create a policy override

        Args:
          domain_id: The domain ID

          enabled: Whether the override is active

          name: The policy override's display name

          target_ids: The detectors or rules this override suppresses

          target_type: Whether `target_ids` are detector IDs or rule IDs

          conditions: The conditions required for the override to apply. An override may have up to 5
              conditions; all must pass for the override to apply. Without conditions the
              override applies to every request on the owning domain that hits a linked
              target.

          description: An optional note explaining the override

          request_id: The ID of the request that prompted this override, if created from Event
              Details. Preserves a snapshot of that request for audit purposes; has no effect
              on override behavior and is not returned by this API.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            path_template("/waap/v1/domains/{domain_id}/default-rule-overrides", domain_id=domain_id),
            body=await async_maybe_transform(
                {
                    "enabled": enabled,
                    "name": name,
                    "target_ids": target_ids,
                    "target_type": target_type,
                    "conditions": conditions,
                    "description": description,
                    "request_id": request_id,
                },
                policy_override_create_params.PolicyOverrideCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapPolicyOverride,
        )

    async def update(
        self,
        policy_override_id: int,
        *,
        domain_id: int,
        conditions: Optional[Iterable[policy_override_update_params.Condition]] | Omit = omit,
        description: Optional[str] | Omit = omit,
        enabled: Optional[bool] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapPolicyOverride:
        """
        Update a policy override

        Args:
          domain_id: The domain ID

          policy_override_id: Policy override ID

          conditions: The conditions required for the override to apply. An override may have up to 5
              conditions; all must pass for the override to apply. Without conditions the
              override applies to every request on the owning domain that hits a linked
              target.

          description: An optional note explaining the override

          enabled: Whether the override is active

          name: The policy override's display name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            path_template(
                "/waap/v1/domains/{domain_id}/default-rule-overrides/{policy_override_id}",
                domain_id=domain_id,
                policy_override_id=policy_override_id,
            ),
            body=await async_maybe_transform(
                {
                    "conditions": conditions,
                    "description": description,
                    "enabled": enabled,
                    "name": name,
                },
                policy_override_update_params.PolicyOverrideUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapPolicyOverride,
        )

    def list(
        self,
        domain_id: int,
        *,
        enabled: Optional[bool] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        ordering: Optional[
            Literal[
                "id",
                "name",
                "target_type",
                "enabled",
                "stale",
                "created_at",
                "updated_at",
                "-id",
                "-name",
                "-target_type",
                "-enabled",
                "-stale",
                "-created_at",
                "-updated_at",
            ]
        ]
        | Omit = omit,
        search: Optional[str] | Omit = omit,
        target_type: Optional[Literal["detector", "rule"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[WaapPolicyOverride, AsyncOffsetPage[WaapPolicyOverride]]:
        """
        Retrieve policy overrides

        Args:
          domain_id: The domain ID

          enabled: Filter by enabled state.

          limit: Number of items to return

          offset: Number of items to skip

          ordering: Determine the field used to order results.

          search: Search policy override names and descriptions.

          target_type: Filter by linked target type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            path_template("/waap/v1/domains/{domain_id}/default-rule-overrides", domain_id=domain_id),
            page=AsyncOffsetPage[WaapPolicyOverride],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "enabled": enabled,
                        "limit": limit,
                        "offset": offset,
                        "ordering": ordering,
                        "search": search,
                        "target_type": target_type,
                    },
                    policy_override_list_params.PolicyOverrideListParams,
                ),
            ),
            model=WaapPolicyOverride,
        )

    async def delete(
        self,
        policy_override_id: int,
        *,
        domain_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a policy override

        Args:
          domain_id: The domain ID

          policy_override_id: Policy override ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/waap/v1/domains/{domain_id}/default-rule-overrides/{policy_override_id}",
                domain_id=domain_id,
                policy_override_id=policy_override_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        policy_override_id: int,
        *,
        domain_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapPolicyOverride:
        """
        Retrieve a policy override

        Args:
          domain_id: The domain ID

          policy_override_id: Policy override ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template(
                "/waap/v1/domains/{domain_id}/default-rule-overrides/{policy_override_id}",
                domain_id=domain_id,
                policy_override_id=policy_override_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapPolicyOverride,
        )

    def list_owasp_top_threats_targets(
        self,
        domain_id: int,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[WaapOwaspTopThreatsTarget, AsyncOffsetPage[WaapOwaspTopThreatsTarget]]:
        """
        List OWASP Top Threats targets selectable as a policy override target

        Args:
          domain_id: The domain ID

          limit: Number of items to return

          offset: Number of items to skip

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            path_template(
                "/waap/v1/domains/{domain_id}/policy-override-targets/owasp-top-threats", domain_id=domain_id
            ),
            page=AsyncOffsetPage[WaapOwaspTopThreatsTarget],
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
                    policy_override_list_owasp_top_threats_targets_params.PolicyOverrideListOwaspTopThreatsTargetsParams,
                ),
            ),
            model=WaapOwaspTopThreatsTarget,
        )


class PolicyOverridesResourceWithRawResponse:
    def __init__(self, policy_overrides: PolicyOverridesResource) -> None:
        self._policy_overrides = policy_overrides

        self.create = to_raw_response_wrapper(
            policy_overrides.create,
        )
        self.update = to_raw_response_wrapper(
            policy_overrides.update,
        )
        self.list = to_raw_response_wrapper(
            policy_overrides.list,
        )
        self.delete = to_raw_response_wrapper(
            policy_overrides.delete,
        )
        self.get = to_raw_response_wrapper(
            policy_overrides.get,
        )
        self.list_owasp_top_threats_targets = to_raw_response_wrapper(
            policy_overrides.list_owasp_top_threats_targets,
        )


class AsyncPolicyOverridesResourceWithRawResponse:
    def __init__(self, policy_overrides: AsyncPolicyOverridesResource) -> None:
        self._policy_overrides = policy_overrides

        self.create = async_to_raw_response_wrapper(
            policy_overrides.create,
        )
        self.update = async_to_raw_response_wrapper(
            policy_overrides.update,
        )
        self.list = async_to_raw_response_wrapper(
            policy_overrides.list,
        )
        self.delete = async_to_raw_response_wrapper(
            policy_overrides.delete,
        )
        self.get = async_to_raw_response_wrapper(
            policy_overrides.get,
        )
        self.list_owasp_top_threats_targets = async_to_raw_response_wrapper(
            policy_overrides.list_owasp_top_threats_targets,
        )


class PolicyOverridesResourceWithStreamingResponse:
    def __init__(self, policy_overrides: PolicyOverridesResource) -> None:
        self._policy_overrides = policy_overrides

        self.create = to_streamed_response_wrapper(
            policy_overrides.create,
        )
        self.update = to_streamed_response_wrapper(
            policy_overrides.update,
        )
        self.list = to_streamed_response_wrapper(
            policy_overrides.list,
        )
        self.delete = to_streamed_response_wrapper(
            policy_overrides.delete,
        )
        self.get = to_streamed_response_wrapper(
            policy_overrides.get,
        )
        self.list_owasp_top_threats_targets = to_streamed_response_wrapper(
            policy_overrides.list_owasp_top_threats_targets,
        )


class AsyncPolicyOverridesResourceWithStreamingResponse:
    def __init__(self, policy_overrides: AsyncPolicyOverridesResource) -> None:
        self._policy_overrides = policy_overrides

        self.create = async_to_streamed_response_wrapper(
            policy_overrides.create,
        )
        self.update = async_to_streamed_response_wrapper(
            policy_overrides.update,
        )
        self.list = async_to_streamed_response_wrapper(
            policy_overrides.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            policy_overrides.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            policy_overrides.get,
        )
        self.list_owasp_top_threats_targets = async_to_streamed_response_wrapper(
            policy_overrides.list_owasp_top_threats_targets,
        )
