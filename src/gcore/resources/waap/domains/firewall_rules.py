# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

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
from ....types.waap import WaapCustomerRuleState
from ...._base_client import AsyncPaginator, make_request_options
from ....types.waap.domains import (
    firewall_rule_list_params,
    firewall_rule_create_params,
    firewall_rule_update_params,
    firewall_rule_delete_multiple_params,
)
from ....types.waap.waap_firewall_rule import WaapFirewallRule
from ....types.waap.waap_customer_rule_state import WaapCustomerRuleState

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

    def create(
        self,
        domain_id: int,
        *,
        action: firewall_rule_create_params.Action,
        conditions: Iterable[firewall_rule_create_params.Condition],
        enabled: bool,
        name: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WaapFirewallRule:
        """
        Create a firewall rule

        Args:
          domain_id: The domain ID

          action: The action that a firewall rule takes when triggered

          conditions: The condition required for the WAAP engine to trigger the rule.

          enabled: Whether or not the rule is enabled

          name: The name assigned to the rule

          description: The description assigned to the rule

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/waap/v1/domains/{domain_id}/firewall-rules",
            body=maybe_transform(
                {
                    "action": action,
                    "conditions": conditions,
                    "enabled": enabled,
                    "name": name,
                    "description": description,
                },
                firewall_rule_create_params.FirewallRuleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapFirewallRule,
        )

    def update(
        self,
        rule_id: int,
        *,
        domain_id: int,
        action: Optional[firewall_rule_update_params.Action] | NotGiven = NOT_GIVEN,
        conditions: Optional[Iterable[firewall_rule_update_params.Condition]] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        enabled: Optional[bool] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Only properties present in the request will be updated

        Args:
          domain_id: The domain ID

          rule_id: The firewall rule ID

          action: The action that a firewall rule takes when triggered

          conditions: The condition required for the WAAP engine to trigger the rule.

          description: The description assigned to the rule

          enabled: Whether or not the rule is enabled

          name: The name assigned to the rule

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            f"/waap/v1/domains/{domain_id}/firewall-rules/{rule_id}",
            body=maybe_transform(
                {
                    "action": action,
                    "conditions": conditions,
                    "description": description,
                    "enabled": enabled,
                    "name": name,
                },
                firewall_rule_update_params.FirewallRuleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        domain_id: int,
        *,
        action: Literal["allow", "block"] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        ordering: Optional[
            Literal[
                "id", "name", "description", "enabled", "action", "-id", "-name", "-description", "-enabled", "-action"
            ]
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[WaapFirewallRule]:
        """
        Extracts a list of firewall rules assigned to a domain, offering filter,
        ordering, and pagination capabilities

        Args:
          domain_id: The domain ID

          action: Filter to refine results by specific firewall actions

          description: Filter rules based on their description. Supports '\\**' as a wildcard character.

          enabled: Filter rules based on their active status

          limit: Number of items to return

          name: Filter rules based on their name. Supports '\\**' as a wildcard character.

          offset: Number of items to skip

          ordering: Determine the field to order results by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            f"/waap/v1/domains/{domain_id}/firewall-rules",
            page=SyncOffsetPage[WaapFirewallRule],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "action": action,
                        "description": description,
                        "enabled": enabled,
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "ordering": ordering,
                    },
                    firewall_rule_list_params.FirewallRuleListParams,
                ),
            ),
            model=WaapFirewallRule,
        )

    def delete(
        self,
        rule_id: int,
        *,
        domain_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a firewall rule

        Args:
          domain_id: The domain ID

          rule_id: The firewall rule ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/waap/v1/domains/{domain_id}/firewall-rules/{rule_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def delete_multiple(
        self,
        domain_id: int,
        *,
        rule_ids: Iterable[int],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete multiple WAAP rules

        Args:
          domain_id: The domain ID

          rule_ids: The IDs of the rules to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/waap/v1/domains/{domain_id}/firewall-rules/bulk_delete",
            body=maybe_transform(
                {"rule_ids": rule_ids}, firewall_rule_delete_multiple_params.FirewallRuleDeleteMultipleParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        rule_id: int,
        *,
        domain_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WaapFirewallRule:
        """
        Extracts a specific firewall rule assigned to a domain

        Args:
          domain_id: The domain ID

          rule_id: The firewall rule ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/waap/v1/domains/{domain_id}/firewall-rules/{rule_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapFirewallRule,
        )

    def toggle(
        self,
        action: WaapCustomerRuleState,
        *,
        domain_id: int,
        rule_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Toggle a firewall rule

        Args:
          domain_id: The domain ID

          rule_id: The firewall rule ID

          action: Enable or disable a firewall rule

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not action:
            raise ValueError(f"Expected a non-empty value for `action` but received {action!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            f"/waap/v1/domains/{domain_id}/firewall-rules/{rule_id}/{action}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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

    async def create(
        self,
        domain_id: int,
        *,
        action: firewall_rule_create_params.Action,
        conditions: Iterable[firewall_rule_create_params.Condition],
        enabled: bool,
        name: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WaapFirewallRule:
        """
        Create a firewall rule

        Args:
          domain_id: The domain ID

          action: The action that a firewall rule takes when triggered

          conditions: The condition required for the WAAP engine to trigger the rule.

          enabled: Whether or not the rule is enabled

          name: The name assigned to the rule

          description: The description assigned to the rule

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/waap/v1/domains/{domain_id}/firewall-rules",
            body=await async_maybe_transform(
                {
                    "action": action,
                    "conditions": conditions,
                    "enabled": enabled,
                    "name": name,
                    "description": description,
                },
                firewall_rule_create_params.FirewallRuleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapFirewallRule,
        )

    async def update(
        self,
        rule_id: int,
        *,
        domain_id: int,
        action: Optional[firewall_rule_update_params.Action] | NotGiven = NOT_GIVEN,
        conditions: Optional[Iterable[firewall_rule_update_params.Condition]] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        enabled: Optional[bool] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Only properties present in the request will be updated

        Args:
          domain_id: The domain ID

          rule_id: The firewall rule ID

          action: The action that a firewall rule takes when triggered

          conditions: The condition required for the WAAP engine to trigger the rule.

          description: The description assigned to the rule

          enabled: Whether or not the rule is enabled

          name: The name assigned to the rule

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            f"/waap/v1/domains/{domain_id}/firewall-rules/{rule_id}",
            body=await async_maybe_transform(
                {
                    "action": action,
                    "conditions": conditions,
                    "description": description,
                    "enabled": enabled,
                    "name": name,
                },
                firewall_rule_update_params.FirewallRuleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        domain_id: int,
        *,
        action: Literal["allow", "block"] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        ordering: Optional[
            Literal[
                "id", "name", "description", "enabled", "action", "-id", "-name", "-description", "-enabled", "-action"
            ]
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[WaapFirewallRule, AsyncOffsetPage[WaapFirewallRule]]:
        """
        Extracts a list of firewall rules assigned to a domain, offering filter,
        ordering, and pagination capabilities

        Args:
          domain_id: The domain ID

          action: Filter to refine results by specific firewall actions

          description: Filter rules based on their description. Supports '\\**' as a wildcard character.

          enabled: Filter rules based on their active status

          limit: Number of items to return

          name: Filter rules based on their name. Supports '\\**' as a wildcard character.

          offset: Number of items to skip

          ordering: Determine the field to order results by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            f"/waap/v1/domains/{domain_id}/firewall-rules",
            page=AsyncOffsetPage[WaapFirewallRule],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "action": action,
                        "description": description,
                        "enabled": enabled,
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "ordering": ordering,
                    },
                    firewall_rule_list_params.FirewallRuleListParams,
                ),
            ),
            model=WaapFirewallRule,
        )

    async def delete(
        self,
        rule_id: int,
        *,
        domain_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a firewall rule

        Args:
          domain_id: The domain ID

          rule_id: The firewall rule ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/waap/v1/domains/{domain_id}/firewall-rules/{rule_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def delete_multiple(
        self,
        domain_id: int,
        *,
        rule_ids: Iterable[int],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete multiple WAAP rules

        Args:
          domain_id: The domain ID

          rule_ids: The IDs of the rules to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/waap/v1/domains/{domain_id}/firewall-rules/bulk_delete",
            body=await async_maybe_transform(
                {"rule_ids": rule_ids}, firewall_rule_delete_multiple_params.FirewallRuleDeleteMultipleParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        rule_id: int,
        *,
        domain_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WaapFirewallRule:
        """
        Extracts a specific firewall rule assigned to a domain

        Args:
          domain_id: The domain ID

          rule_id: The firewall rule ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/waap/v1/domains/{domain_id}/firewall-rules/{rule_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapFirewallRule,
        )

    async def toggle(
        self,
        action: WaapCustomerRuleState,
        *,
        domain_id: int,
        rule_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Toggle a firewall rule

        Args:
          domain_id: The domain ID

          rule_id: The firewall rule ID

          action: Enable or disable a firewall rule

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not action:
            raise ValueError(f"Expected a non-empty value for `action` but received {action!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            f"/waap/v1/domains/{domain_id}/firewall-rules/{rule_id}/{action}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class FirewallRulesResourceWithRawResponse:
    def __init__(self, firewall_rules: FirewallRulesResource) -> None:
        self._firewall_rules = firewall_rules

        self.create = to_raw_response_wrapper(
            firewall_rules.create,
        )
        self.update = to_raw_response_wrapper(
            firewall_rules.update,
        )
        self.list = to_raw_response_wrapper(
            firewall_rules.list,
        )
        self.delete = to_raw_response_wrapper(
            firewall_rules.delete,
        )
        self.delete_multiple = to_raw_response_wrapper(
            firewall_rules.delete_multiple,
        )
        self.get = to_raw_response_wrapper(
            firewall_rules.get,
        )
        self.toggle = to_raw_response_wrapper(
            firewall_rules.toggle,
        )


class AsyncFirewallRulesResourceWithRawResponse:
    def __init__(self, firewall_rules: AsyncFirewallRulesResource) -> None:
        self._firewall_rules = firewall_rules

        self.create = async_to_raw_response_wrapper(
            firewall_rules.create,
        )
        self.update = async_to_raw_response_wrapper(
            firewall_rules.update,
        )
        self.list = async_to_raw_response_wrapper(
            firewall_rules.list,
        )
        self.delete = async_to_raw_response_wrapper(
            firewall_rules.delete,
        )
        self.delete_multiple = async_to_raw_response_wrapper(
            firewall_rules.delete_multiple,
        )
        self.get = async_to_raw_response_wrapper(
            firewall_rules.get,
        )
        self.toggle = async_to_raw_response_wrapper(
            firewall_rules.toggle,
        )


class FirewallRulesResourceWithStreamingResponse:
    def __init__(self, firewall_rules: FirewallRulesResource) -> None:
        self._firewall_rules = firewall_rules

        self.create = to_streamed_response_wrapper(
            firewall_rules.create,
        )
        self.update = to_streamed_response_wrapper(
            firewall_rules.update,
        )
        self.list = to_streamed_response_wrapper(
            firewall_rules.list,
        )
        self.delete = to_streamed_response_wrapper(
            firewall_rules.delete,
        )
        self.delete_multiple = to_streamed_response_wrapper(
            firewall_rules.delete_multiple,
        )
        self.get = to_streamed_response_wrapper(
            firewall_rules.get,
        )
        self.toggle = to_streamed_response_wrapper(
            firewall_rules.toggle,
        )


class AsyncFirewallRulesResourceWithStreamingResponse:
    def __init__(self, firewall_rules: AsyncFirewallRulesResource) -> None:
        self._firewall_rules = firewall_rules

        self.create = async_to_streamed_response_wrapper(
            firewall_rules.create,
        )
        self.update = async_to_streamed_response_wrapper(
            firewall_rules.update,
        )
        self.list = async_to_streamed_response_wrapper(
            firewall_rules.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            firewall_rules.delete,
        )
        self.delete_multiple = async_to_streamed_response_wrapper(
            firewall_rules.delete_multiple,
        )
        self.get = async_to_streamed_response_wrapper(
            firewall_rules.get,
        )
        self.toggle = async_to_streamed_response_wrapper(
            firewall_rules.toggle,
        )
