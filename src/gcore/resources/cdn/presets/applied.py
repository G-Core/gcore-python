# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast

import httpx

from ...._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.cdn.presets import applied_apply_params
from ....types.cdn.presets.applied_preset import AppliedPreset
from ....types.cdn.presets.applied_preset_fields import AppliedPresetFields
from ....types.cdn.presets.applied_apply_response import AppliedApplyResponse

__all__ = ["AppliedResource", "AsyncAppliedResource"]


class AppliedResource(SyncAPIResource):
    """
    Applied presets represent the association between a preset and a CDN resource or rule. Use them to apply a preset to an object, list the objects a preset is applied to, unapply it, and inspect which object fields a preset manages.
    """

    @cached_property
    def with_raw_response(self) -> AppliedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AppliedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AppliedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AppliedResourceWithStreamingResponse(self)

    def apply(
        self,
        preset_id: int,
        *,
        object_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppliedApplyResponse:
        """
        Apply the preset to an object (CDN resource or rule, according to the preset
        `object_type`).

        The preset settings are applied to the object, and the options included in the
        preset can no longer be edited on the object until the preset is unapplied.

        Args:
          object_id: ID of the object (CDN resource or rule, according to the preset `object_type`)
              to apply the preset to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            path_template("/cdn/presets/{preset_id}/applied", preset_id=preset_id),
            body=maybe_transform({"object_id": object_id}, applied_apply_params.AppliedApplyParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppliedApplyResponse,
        )

    def get_objects(
        self,
        preset_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppliedPreset:
        """
        Get the list of objects the preset is currently applied to.

        Non-staff users only see objects that belong to their account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            AppliedPreset,
            self._get(
                path_template("/cdn/presets/{preset_id}/applied", preset_id=preset_id),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, AppliedPreset),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def get_resource_preset(
        self,
        resource_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppliedPresetFields:
        """
        Get the preset applied to a CDN resource and the list of resource fields managed
        by the preset.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/cdn/resources/{resource_id}/preset", resource_id=resource_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppliedPresetFields,
        )

    def get_rule_preset(
        self,
        rule_id: int,
        *,
        resource_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppliedPresetFields:
        """
        Get the preset applied to a rule and the list of rule fields managed by the
        preset.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template(
                "/cdn/resources/{resource_id}/rules/{rule_id}/preset", resource_id=resource_id, rule_id=rule_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppliedPresetFields,
        )

    def unapply(
        self,
        object_id: int,
        *,
        preset_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Unapply the preset from the object.

        The options managed by the preset are
        removed from the object.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/cdn/presets/{preset_id}/applied/{object_id}", preset_id=preset_id, object_id=object_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAppliedResource(AsyncAPIResource):
    """
    Applied presets represent the association between a preset and a CDN resource or rule. Use them to apply a preset to an object, list the objects a preset is applied to, unapply it, and inspect which object fields a preset manages.
    """

    @cached_property
    def with_raw_response(self) -> AsyncAppliedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAppliedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAppliedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncAppliedResourceWithStreamingResponse(self)

    async def apply(
        self,
        preset_id: int,
        *,
        object_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppliedApplyResponse:
        """
        Apply the preset to an object (CDN resource or rule, according to the preset
        `object_type`).

        The preset settings are applied to the object, and the options included in the
        preset can no longer be edited on the object until the preset is unapplied.

        Args:
          object_id: ID of the object (CDN resource or rule, according to the preset `object_type`)
              to apply the preset to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            path_template("/cdn/presets/{preset_id}/applied", preset_id=preset_id),
            body=await async_maybe_transform({"object_id": object_id}, applied_apply_params.AppliedApplyParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppliedApplyResponse,
        )

    async def get_objects(
        self,
        preset_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppliedPreset:
        """
        Get the list of objects the preset is currently applied to.

        Non-staff users only see objects that belong to their account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            AppliedPreset,
            await self._get(
                path_template("/cdn/presets/{preset_id}/applied", preset_id=preset_id),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, AppliedPreset),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def get_resource_preset(
        self,
        resource_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppliedPresetFields:
        """
        Get the preset applied to a CDN resource and the list of resource fields managed
        by the preset.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/cdn/resources/{resource_id}/preset", resource_id=resource_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppliedPresetFields,
        )

    async def get_rule_preset(
        self,
        rule_id: int,
        *,
        resource_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppliedPresetFields:
        """
        Get the preset applied to a rule and the list of rule fields managed by the
        preset.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template(
                "/cdn/resources/{resource_id}/rules/{rule_id}/preset", resource_id=resource_id, rule_id=rule_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppliedPresetFields,
        )

    async def unapply(
        self,
        object_id: int,
        *,
        preset_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Unapply the preset from the object.

        The options managed by the preset are
        removed from the object.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/cdn/presets/{preset_id}/applied/{object_id}", preset_id=preset_id, object_id=object_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AppliedResourceWithRawResponse:
    def __init__(self, applied: AppliedResource) -> None:
        self._applied = applied

        self.apply = to_raw_response_wrapper(
            applied.apply,
        )
        self.get_objects = to_raw_response_wrapper(
            applied.get_objects,
        )
        self.get_resource_preset = to_raw_response_wrapper(
            applied.get_resource_preset,
        )
        self.get_rule_preset = to_raw_response_wrapper(
            applied.get_rule_preset,
        )
        self.unapply = to_raw_response_wrapper(
            applied.unapply,
        )


class AsyncAppliedResourceWithRawResponse:
    def __init__(self, applied: AsyncAppliedResource) -> None:
        self._applied = applied

        self.apply = async_to_raw_response_wrapper(
            applied.apply,
        )
        self.get_objects = async_to_raw_response_wrapper(
            applied.get_objects,
        )
        self.get_resource_preset = async_to_raw_response_wrapper(
            applied.get_resource_preset,
        )
        self.get_rule_preset = async_to_raw_response_wrapper(
            applied.get_rule_preset,
        )
        self.unapply = async_to_raw_response_wrapper(
            applied.unapply,
        )


class AppliedResourceWithStreamingResponse:
    def __init__(self, applied: AppliedResource) -> None:
        self._applied = applied

        self.apply = to_streamed_response_wrapper(
            applied.apply,
        )
        self.get_objects = to_streamed_response_wrapper(
            applied.get_objects,
        )
        self.get_resource_preset = to_streamed_response_wrapper(
            applied.get_resource_preset,
        )
        self.get_rule_preset = to_streamed_response_wrapper(
            applied.get_rule_preset,
        )
        self.unapply = to_streamed_response_wrapper(
            applied.unapply,
        )


class AsyncAppliedResourceWithStreamingResponse:
    def __init__(self, applied: AsyncAppliedResource) -> None:
        self._applied = applied

        self.apply = async_to_streamed_response_wrapper(
            applied.apply,
        )
        self.get_objects = async_to_streamed_response_wrapper(
            applied.get_objects,
        )
        self.get_resource_preset = async_to_streamed_response_wrapper(
            applied.get_resource_preset,
        )
        self.get_rule_preset = async_to_streamed_response_wrapper(
            applied.get_rule_preset,
        )
        self.unapply = async_to_streamed_response_wrapper(
            applied.unapply,
        )
