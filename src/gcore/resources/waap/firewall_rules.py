# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncOffsetPage, AsyncOffsetPage
from ...types.waap import firewall_rule_list_params
from ..._base_client import AsyncPaginator, make_request_options
from ...types.waap.waap_account_firewall_rule import WaapAccountFirewallRule

__all__ = ["FirewallRulesResource", "AsyncFirewallRulesResource"]


class FirewallRulesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FirewallRulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return FirewallRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FirewallRulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return FirewallRulesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        action: Literal["allow", "block"] | Omit = omit,
        description: str | Omit = omit,
        domain_ids: Iterable[int] | Omit = omit,
        enabled: bool | Omit = omit,
        limit: int | Omit = omit,
        name: str | Omit = omit,
        offset: int | Omit = omit,
        ordering: Optional[
            Literal[
                "id", "name", "description", "enabled", "action", "-id", "-name", "-description", "-enabled", "-action"
            ]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[WaapAccountFirewallRule]:
        """
        Returns all firewall rules across all domains belonging to the authenticated
        account. Supports filtering, ordering, and pagination.

        Args:
          action: Filter by action type

          description: Filter rules by description (supports wildcards)

          domain_ids: Filter by domain IDs (can specify multiple)

          enabled: Filter by enabled status

          limit: Number of items to return

          name: Filter rules by name (supports wildcards)

          offset: Number of items to skip

          ordering: Order results by field (prefix with - for descending)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/waap/v2/firewall-rules",
            page=SyncOffsetPage[WaapAccountFirewallRule],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "action": action,
                        "description": description,
                        "domain_ids": domain_ids,
                        "enabled": enabled,
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "ordering": ordering,
                    },
                    firewall_rule_list_params.FirewallRuleListParams,
                ),
            ),
            model=WaapAccountFirewallRule,
        )


class AsyncFirewallRulesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFirewallRulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFirewallRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFirewallRulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncFirewallRulesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        action: Literal["allow", "block"] | Omit = omit,
        description: str | Omit = omit,
        domain_ids: Iterable[int] | Omit = omit,
        enabled: bool | Omit = omit,
        limit: int | Omit = omit,
        name: str | Omit = omit,
        offset: int | Omit = omit,
        ordering: Optional[
            Literal[
                "id", "name", "description", "enabled", "action", "-id", "-name", "-description", "-enabled", "-action"
            ]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[WaapAccountFirewallRule, AsyncOffsetPage[WaapAccountFirewallRule]]:
        """
        Returns all firewall rules across all domains belonging to the authenticated
        account. Supports filtering, ordering, and pagination.

        Args:
          action: Filter by action type

          description: Filter rules by description (supports wildcards)

          domain_ids: Filter by domain IDs (can specify multiple)

          enabled: Filter by enabled status

          limit: Number of items to return

          name: Filter rules by name (supports wildcards)

          offset: Number of items to skip

          ordering: Order results by field (prefix with - for descending)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/waap/v2/firewall-rules",
            page=AsyncOffsetPage[WaapAccountFirewallRule],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "action": action,
                        "description": description,
                        "domain_ids": domain_ids,
                        "enabled": enabled,
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "ordering": ordering,
                    },
                    firewall_rule_list_params.FirewallRuleListParams,
                ),
            ),
            model=WaapAccountFirewallRule,
        )


class FirewallRulesResourceWithRawResponse:
    def __init__(self, firewall_rules: FirewallRulesResource) -> None:
        self._firewall_rules = firewall_rules

        self.list = to_raw_response_wrapper(
            firewall_rules.list,
        )


class AsyncFirewallRulesResourceWithRawResponse:
    def __init__(self, firewall_rules: AsyncFirewallRulesResource) -> None:
        self._firewall_rules = firewall_rules

        self.list = async_to_raw_response_wrapper(
            firewall_rules.list,
        )


class FirewallRulesResourceWithStreamingResponse:
    def __init__(self, firewall_rules: FirewallRulesResource) -> None:
        self._firewall_rules = firewall_rules

        self.list = to_streamed_response_wrapper(
            firewall_rules.list,
        )


class AsyncFirewallRulesResourceWithStreamingResponse:
    def __init__(self, firewall_rules: AsyncFirewallRulesResource) -> None:
        self._firewall_rules = firewall_rules

        self.list = async_to_streamed_response_wrapper(
            firewall_rules.list,
        )
