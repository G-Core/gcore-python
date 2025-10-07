# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ...._base_client import AsyncPaginator, make_request_options
from ....types.waap.domains import (
    custom_rule_list_params,
    custom_rule_create_params,
    custom_rule_update_params,
    custom_rule_delete_multiple_params,
)
from ....types.waap.domains.waap_custom_rule import WaapCustomRule

__all__ = ["CustomRulesResource", "AsyncCustomRulesResource"]


class CustomRulesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CustomRulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return CustomRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomRulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return CustomRulesResourceWithStreamingResponse(self)

    def create(
        self,
        domain_id: int,
        *,
        action: custom_rule_create_params.Action,
        conditions: Iterable[custom_rule_create_params.Condition],
        enabled: bool,
        name: str,
        description: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapCustomRule:
        """
        Create a custom rule

        Args:
          domain_id: The domain ID

          action: The action that the rule takes when triggered. Only one action can be set per
              rule.

          conditions: The conditions required for the WAAP engine to trigger the rule. Rules may have
              between 1 and 5 conditions. All conditions must pass for the rule to trigger

          enabled: Whether or not the rule is enabled

          name: The name assigned to the rule

          description: The description assigned to the rule

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/waap/v1/domains/{domain_id}/custom-rules",
            body=maybe_transform(
                {
                    "action": action,
                    "conditions": conditions,
                    "enabled": enabled,
                    "name": name,
                    "description": description,
                },
                custom_rule_create_params.CustomRuleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapCustomRule,
        )

    def update(
        self,
        rule_id: int,
        *,
        domain_id: int,
        action: Optional[custom_rule_update_params.Action] | Omit = omit,
        conditions: Optional[Iterable[custom_rule_update_params.Condition]] | Omit = omit,
        description: Optional[str] | Omit = omit,
        enabled: Optional[bool] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Only properties present in the request will be updated

        Args:
          domain_id: The domain ID

          rule_id: The custom rule ID

          action: The action that a WAAP rule takes when triggered.

          conditions: The conditions required for the WAAP engine to trigger the rule. Rules may have
              between 1 and 5 conditions. All conditions must pass for the rule to trigger

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
            f"/waap/v1/domains/{domain_id}/custom-rules/{rule_id}",
            body=maybe_transform(
                {
                    "action": action,
                    "conditions": conditions,
                    "description": description,
                    "enabled": enabled,
                    "name": name,
                },
                custom_rule_update_params.CustomRuleUpdateParams,
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
        action: Literal["allow", "block", "captcha", "handshake", "monitor", "tag"] | Omit = omit,
        description: str | Omit = omit,
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
    ) -> SyncOffsetPage[WaapCustomRule]:
        """
        Extracts a list of custom rules assigned to a domain, offering filter, ordering,
        and pagination capabilities

        Args:
          domain_id: The domain ID

          action: Filter to refine results by specific actions

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
            f"/waap/v1/domains/{domain_id}/custom-rules",
            page=SyncOffsetPage[WaapCustomRule],
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
                    custom_rule_list_params.CustomRuleListParams,
                ),
            ),
            model=WaapCustomRule,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a custom rule

        Args:
          domain_id: The domain ID

          rule_id: The custom rule ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/waap/v1/domains/{domain_id}/custom-rules/{rule_id}",
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            f"/waap/v1/domains/{domain_id}/custom-rules/bulk_delete",
            body=maybe_transform(
                {"rule_ids": rule_ids}, custom_rule_delete_multiple_params.CustomRuleDeleteMultipleParams
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapCustomRule:
        """
        Extracts a specific custom rule assigned to a domain

        Args:
          domain_id: The domain ID

          rule_id: The custom rule ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/waap/v1/domains/{domain_id}/custom-rules/{rule_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapCustomRule,
        )

    def toggle(
        self,
        action: Literal["enable", "disable"],
        *,
        domain_id: int,
        rule_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Toggle a custom rule

        Args:
          domain_id: The domain ID

          rule_id: The custom rule ID

          action: Enable or disable a custom rule

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not action:
            raise ValueError(f"Expected a non-empty value for `action` but received {action!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            f"/waap/v1/domains/{domain_id}/custom-rules/{rule_id}/{action}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncCustomRulesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCustomRulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCustomRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomRulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncCustomRulesResourceWithStreamingResponse(self)

    async def create(
        self,
        domain_id: int,
        *,
        action: custom_rule_create_params.Action,
        conditions: Iterable[custom_rule_create_params.Condition],
        enabled: bool,
        name: str,
        description: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapCustomRule:
        """
        Create a custom rule

        Args:
          domain_id: The domain ID

          action: The action that the rule takes when triggered. Only one action can be set per
              rule.

          conditions: The conditions required for the WAAP engine to trigger the rule. Rules may have
              between 1 and 5 conditions. All conditions must pass for the rule to trigger

          enabled: Whether or not the rule is enabled

          name: The name assigned to the rule

          description: The description assigned to the rule

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/waap/v1/domains/{domain_id}/custom-rules",
            body=await async_maybe_transform(
                {
                    "action": action,
                    "conditions": conditions,
                    "enabled": enabled,
                    "name": name,
                    "description": description,
                },
                custom_rule_create_params.CustomRuleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapCustomRule,
        )

    async def update(
        self,
        rule_id: int,
        *,
        domain_id: int,
        action: Optional[custom_rule_update_params.Action] | Omit = omit,
        conditions: Optional[Iterable[custom_rule_update_params.Condition]] | Omit = omit,
        description: Optional[str] | Omit = omit,
        enabled: Optional[bool] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Only properties present in the request will be updated

        Args:
          domain_id: The domain ID

          rule_id: The custom rule ID

          action: The action that a WAAP rule takes when triggered.

          conditions: The conditions required for the WAAP engine to trigger the rule. Rules may have
              between 1 and 5 conditions. All conditions must pass for the rule to trigger

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
            f"/waap/v1/domains/{domain_id}/custom-rules/{rule_id}",
            body=await async_maybe_transform(
                {
                    "action": action,
                    "conditions": conditions,
                    "description": description,
                    "enabled": enabled,
                    "name": name,
                },
                custom_rule_update_params.CustomRuleUpdateParams,
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
        action: Literal["allow", "block", "captcha", "handshake", "monitor", "tag"] | Omit = omit,
        description: str | Omit = omit,
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
    ) -> AsyncPaginator[WaapCustomRule, AsyncOffsetPage[WaapCustomRule]]:
        """
        Extracts a list of custom rules assigned to a domain, offering filter, ordering,
        and pagination capabilities

        Args:
          domain_id: The domain ID

          action: Filter to refine results by specific actions

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
            f"/waap/v1/domains/{domain_id}/custom-rules",
            page=AsyncOffsetPage[WaapCustomRule],
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
                    custom_rule_list_params.CustomRuleListParams,
                ),
            ),
            model=WaapCustomRule,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a custom rule

        Args:
          domain_id: The domain ID

          rule_id: The custom rule ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/waap/v1/domains/{domain_id}/custom-rules/{rule_id}",
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            f"/waap/v1/domains/{domain_id}/custom-rules/bulk_delete",
            body=await async_maybe_transform(
                {"rule_ids": rule_ids}, custom_rule_delete_multiple_params.CustomRuleDeleteMultipleParams
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapCustomRule:
        """
        Extracts a specific custom rule assigned to a domain

        Args:
          domain_id: The domain ID

          rule_id: The custom rule ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/waap/v1/domains/{domain_id}/custom-rules/{rule_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapCustomRule,
        )

    async def toggle(
        self,
        action: Literal["enable", "disable"],
        *,
        domain_id: int,
        rule_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Toggle a custom rule

        Args:
          domain_id: The domain ID

          rule_id: The custom rule ID

          action: Enable or disable a custom rule

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not action:
            raise ValueError(f"Expected a non-empty value for `action` but received {action!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            f"/waap/v1/domains/{domain_id}/custom-rules/{rule_id}/{action}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class CustomRulesResourceWithRawResponse:
    def __init__(self, custom_rules: CustomRulesResource) -> None:
        self._custom_rules = custom_rules

        self.create = to_raw_response_wrapper(
            custom_rules.create,
        )
        self.update = to_raw_response_wrapper(
            custom_rules.update,
        )
        self.list = to_raw_response_wrapper(
            custom_rules.list,
        )
        self.delete = to_raw_response_wrapper(
            custom_rules.delete,
        )
        self.delete_multiple = to_raw_response_wrapper(
            custom_rules.delete_multiple,
        )
        self.get = to_raw_response_wrapper(
            custom_rules.get,
        )
        self.toggle = to_raw_response_wrapper(
            custom_rules.toggle,
        )


class AsyncCustomRulesResourceWithRawResponse:
    def __init__(self, custom_rules: AsyncCustomRulesResource) -> None:
        self._custom_rules = custom_rules

        self.create = async_to_raw_response_wrapper(
            custom_rules.create,
        )
        self.update = async_to_raw_response_wrapper(
            custom_rules.update,
        )
        self.list = async_to_raw_response_wrapper(
            custom_rules.list,
        )
        self.delete = async_to_raw_response_wrapper(
            custom_rules.delete,
        )
        self.delete_multiple = async_to_raw_response_wrapper(
            custom_rules.delete_multiple,
        )
        self.get = async_to_raw_response_wrapper(
            custom_rules.get,
        )
        self.toggle = async_to_raw_response_wrapper(
            custom_rules.toggle,
        )


class CustomRulesResourceWithStreamingResponse:
    def __init__(self, custom_rules: CustomRulesResource) -> None:
        self._custom_rules = custom_rules

        self.create = to_streamed_response_wrapper(
            custom_rules.create,
        )
        self.update = to_streamed_response_wrapper(
            custom_rules.update,
        )
        self.list = to_streamed_response_wrapper(
            custom_rules.list,
        )
        self.delete = to_streamed_response_wrapper(
            custom_rules.delete,
        )
        self.delete_multiple = to_streamed_response_wrapper(
            custom_rules.delete_multiple,
        )
        self.get = to_streamed_response_wrapper(
            custom_rules.get,
        )
        self.toggle = to_streamed_response_wrapper(
            custom_rules.toggle,
        )


class AsyncCustomRulesResourceWithStreamingResponse:
    def __init__(self, custom_rules: AsyncCustomRulesResource) -> None:
        self._custom_rules = custom_rules

        self.create = async_to_streamed_response_wrapper(
            custom_rules.create,
        )
        self.update = async_to_streamed_response_wrapper(
            custom_rules.update,
        )
        self.list = async_to_streamed_response_wrapper(
            custom_rules.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            custom_rules.delete,
        )
        self.delete_multiple = async_to_streamed_response_wrapper(
            custom_rules.delete_multiple,
        )
        self.get = async_to_streamed_response_wrapper(
            custom_rules.get,
        )
        self.toggle = async_to_streamed_response_wrapper(
            custom_rules.toggle,
        )
