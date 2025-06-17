# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.waap.waap_advanced_rule_descriptor_list import WaapAdvancedRuleDescriptorList

__all__ = ["AdvancedRulesResource", "AsyncAdvancedRulesResource"]


class AdvancedRulesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AdvancedRulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AdvancedRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AdvancedRulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AdvancedRulesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WaapAdvancedRuleDescriptorList:
        """Retrieve an advanced rules descriptor"""
        return self._get(
            "/waap/v1/advanced-rules/descriptor",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapAdvancedRuleDescriptorList,
        )


class AsyncAdvancedRulesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAdvancedRulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAdvancedRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAdvancedRulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncAdvancedRulesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WaapAdvancedRuleDescriptorList:
        """Retrieve an advanced rules descriptor"""
        return await self._get(
            "/waap/v1/advanced-rules/descriptor",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapAdvancedRuleDescriptorList,
        )


class AdvancedRulesResourceWithRawResponse:
    def __init__(self, advanced_rules: AdvancedRulesResource) -> None:
        self._advanced_rules = advanced_rules

        self.list = to_raw_response_wrapper(
            advanced_rules.list,
        )


class AsyncAdvancedRulesResourceWithRawResponse:
    def __init__(self, advanced_rules: AsyncAdvancedRulesResource) -> None:
        self._advanced_rules = advanced_rules

        self.list = async_to_raw_response_wrapper(
            advanced_rules.list,
        )


class AdvancedRulesResourceWithStreamingResponse:
    def __init__(self, advanced_rules: AdvancedRulesResource) -> None:
        self._advanced_rules = advanced_rules

        self.list = to_streamed_response_wrapper(
            advanced_rules.list,
        )


class AsyncAdvancedRulesResourceWithStreamingResponse:
    def __init__(self, advanced_rules: AsyncAdvancedRulesResource) -> None:
        self._advanced_rules = advanced_rules

        self.list = async_to_streamed_response_wrapper(
            advanced_rules.list,
        )
