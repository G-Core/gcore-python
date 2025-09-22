# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
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
from ....types.waap.domains import advanced_rule_list_params, advanced_rule_create_params, advanced_rule_update_params
from ....types.waap.domains.waap_advanced_rule import WaapAdvancedRule

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

    def create(
        self,
        domain_id: int,
        *,
        action: advanced_rule_create_params.Action,
        enabled: bool,
        name: str,
        source: str,
        description: str | Omit = omit,
        phase: Optional[Literal["access", "header_filter", "body_filter"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapAdvancedRule:
        """
        Create an advanced rule

        Args:
          domain_id: The domain ID

          action: The action that the rule takes when triggered. Only one action can be set per
              rule.

          enabled: Whether or not the rule is enabled

          name: The name assigned to the rule

          source: A CEL syntax expression that contains the rule's conditions. Allowed objects
              are: request, whois, session, response, tags, `user_defined_tags`, `user_agent`,
              `client_data`.

              More info can be found here:
              https://gcore.com/docs/waap/waap-rules/advanced-rules

          description: The description assigned to the rule

          phase: The WAAP request/response phase for applying the rule. Default is "access".

              The "access" phase is responsible for modifying the request before it is sent to
              the origin server.

              The "`header_filter`" phase is responsible for modifying the HTTP headers of a
              response before they are sent back to the client.

              The "`body_filter`" phase is responsible for modifying the body of a response
              before it is sent back to the client.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/waap/v1/domains/{domain_id}/advanced-rules",
            body=maybe_transform(
                {
                    "action": action,
                    "enabled": enabled,
                    "name": name,
                    "source": source,
                    "description": description,
                    "phase": phase,
                },
                advanced_rule_create_params.AdvancedRuleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapAdvancedRule,
        )

    def update(
        self,
        rule_id: int,
        *,
        domain_id: int,
        action: Optional[advanced_rule_update_params.Action] | Omit = omit,
        description: Optional[str] | Omit = omit,
        enabled: Optional[bool] | Omit = omit,
        name: Optional[str] | Omit = omit,
        phase: Optional[Literal["access", "header_filter", "body_filter"]] | Omit = omit,
        source: Optional[str] | Omit = omit,
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

          rule_id: The advanced rule ID

          action: The action that a WAAP rule takes when triggered.

          description: The description assigned to the rule

          enabled: Whether or not the rule is enabled

          name: The name assigned to the rule

          phase: The WAAP request/response phase for applying the rule.

              The "access" phase is responsible for modifying the request before it is sent to
              the origin server.

              The "`header_filter`" phase is responsible for modifying the HTTP headers of a
              response before they are sent back to the client.

              The "`body_filter`" phase is responsible for modifying the body of a response
              before it is sent back to the client.

          source: A CEL syntax expression that contains the rule's conditions. Allowed objects
              are: request, whois, session, response, tags, `user_defined_tags`, `user_agent`,
              `client_data`.

              More info can be found here:
              https://gcore.com/docs/waap/waap-rules/advanced-rules

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            f"/waap/v1/domains/{domain_id}/advanced-rules/{rule_id}",
            body=maybe_transform(
                {
                    "action": action,
                    "description": description,
                    "enabled": enabled,
                    "name": name,
                    "phase": phase,
                    "source": source,
                },
                advanced_rule_update_params.AdvancedRuleUpdateParams,
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
                "id",
                "name",
                "description",
                "enabled",
                "action",
                "phase",
                "-id",
                "-name",
                "-description",
                "-enabled",
                "-action",
                "-phase",
            ]
        ]
        | Omit = omit,
        phase: Literal["access", "header_filter", "body_filter"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[WaapAdvancedRule]:
        """
        Retrieve a list of advanced rules assigned to a domain, offering filter,
        ordering, and pagination capabilities

        Args:
          domain_id: The domain ID

          action: Filter to refine results by specific actions

          description: Filter rules based on their description. Supports '\\**' as a wildcard character.

          enabled: Filter rules based on their active status

          limit: Number of items to return

          name: Filter rules based on their name. Supports '\\**' as a wildcard character.

          offset: Number of items to skip

          ordering: Determine the field to order results by

          phase: Filter rules based on the WAAP request/response phase for applying the rule.

              The "access" phase is responsible for modifying the request before it is sent to
              the origin server.

              The "`header_filter`" phase is responsible for modifying the HTTP headers of a
              response before they are sent back to the client.

              The "`body_filter`" phase is responsible for modifying the body of a response
              before it is sent back to the client.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            f"/waap/v1/domains/{domain_id}/advanced-rules",
            page=SyncOffsetPage[WaapAdvancedRule],
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
                        "phase": phase,
                    },
                    advanced_rule_list_params.AdvancedRuleListParams,
                ),
            ),
            model=WaapAdvancedRule,
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
        Delete an advanced rule

        Args:
          domain_id: The domain ID

          rule_id: The advanced rule ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/waap/v1/domains/{domain_id}/advanced-rules/{rule_id}",
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
    ) -> WaapAdvancedRule:
        """
        Retrieve a specific advanced rule assigned to a domain

        Args:
          domain_id: The domain ID

          rule_id: The advanced rule ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/waap/v1/domains/{domain_id}/advanced-rules/{rule_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapAdvancedRule,
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
        Toggle an advanced rule

        Args:
          domain_id: The domain ID

          rule_id: The advanced rule ID

          action: Enable or disable an advanced rule

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not action:
            raise ValueError(f"Expected a non-empty value for `action` but received {action!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            f"/waap/v1/domains/{domain_id}/advanced-rules/{rule_id}/{action}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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

    async def create(
        self,
        domain_id: int,
        *,
        action: advanced_rule_create_params.Action,
        enabled: bool,
        name: str,
        source: str,
        description: str | Omit = omit,
        phase: Optional[Literal["access", "header_filter", "body_filter"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapAdvancedRule:
        """
        Create an advanced rule

        Args:
          domain_id: The domain ID

          action: The action that the rule takes when triggered. Only one action can be set per
              rule.

          enabled: Whether or not the rule is enabled

          name: The name assigned to the rule

          source: A CEL syntax expression that contains the rule's conditions. Allowed objects
              are: request, whois, session, response, tags, `user_defined_tags`, `user_agent`,
              `client_data`.

              More info can be found here:
              https://gcore.com/docs/waap/waap-rules/advanced-rules

          description: The description assigned to the rule

          phase: The WAAP request/response phase for applying the rule. Default is "access".

              The "access" phase is responsible for modifying the request before it is sent to
              the origin server.

              The "`header_filter`" phase is responsible for modifying the HTTP headers of a
              response before they are sent back to the client.

              The "`body_filter`" phase is responsible for modifying the body of a response
              before it is sent back to the client.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/waap/v1/domains/{domain_id}/advanced-rules",
            body=await async_maybe_transform(
                {
                    "action": action,
                    "enabled": enabled,
                    "name": name,
                    "source": source,
                    "description": description,
                    "phase": phase,
                },
                advanced_rule_create_params.AdvancedRuleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapAdvancedRule,
        )

    async def update(
        self,
        rule_id: int,
        *,
        domain_id: int,
        action: Optional[advanced_rule_update_params.Action] | Omit = omit,
        description: Optional[str] | Omit = omit,
        enabled: Optional[bool] | Omit = omit,
        name: Optional[str] | Omit = omit,
        phase: Optional[Literal["access", "header_filter", "body_filter"]] | Omit = omit,
        source: Optional[str] | Omit = omit,
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

          rule_id: The advanced rule ID

          action: The action that a WAAP rule takes when triggered.

          description: The description assigned to the rule

          enabled: Whether or not the rule is enabled

          name: The name assigned to the rule

          phase: The WAAP request/response phase for applying the rule.

              The "access" phase is responsible for modifying the request before it is sent to
              the origin server.

              The "`header_filter`" phase is responsible for modifying the HTTP headers of a
              response before they are sent back to the client.

              The "`body_filter`" phase is responsible for modifying the body of a response
              before it is sent back to the client.

          source: A CEL syntax expression that contains the rule's conditions. Allowed objects
              are: request, whois, session, response, tags, `user_defined_tags`, `user_agent`,
              `client_data`.

              More info can be found here:
              https://gcore.com/docs/waap/waap-rules/advanced-rules

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            f"/waap/v1/domains/{domain_id}/advanced-rules/{rule_id}",
            body=await async_maybe_transform(
                {
                    "action": action,
                    "description": description,
                    "enabled": enabled,
                    "name": name,
                    "phase": phase,
                    "source": source,
                },
                advanced_rule_update_params.AdvancedRuleUpdateParams,
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
                "id",
                "name",
                "description",
                "enabled",
                "action",
                "phase",
                "-id",
                "-name",
                "-description",
                "-enabled",
                "-action",
                "-phase",
            ]
        ]
        | Omit = omit,
        phase: Literal["access", "header_filter", "body_filter"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[WaapAdvancedRule, AsyncOffsetPage[WaapAdvancedRule]]:
        """
        Retrieve a list of advanced rules assigned to a domain, offering filter,
        ordering, and pagination capabilities

        Args:
          domain_id: The domain ID

          action: Filter to refine results by specific actions

          description: Filter rules based on their description. Supports '\\**' as a wildcard character.

          enabled: Filter rules based on their active status

          limit: Number of items to return

          name: Filter rules based on their name. Supports '\\**' as a wildcard character.

          offset: Number of items to skip

          ordering: Determine the field to order results by

          phase: Filter rules based on the WAAP request/response phase for applying the rule.

              The "access" phase is responsible for modifying the request before it is sent to
              the origin server.

              The "`header_filter`" phase is responsible for modifying the HTTP headers of a
              response before they are sent back to the client.

              The "`body_filter`" phase is responsible for modifying the body of a response
              before it is sent back to the client.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            f"/waap/v1/domains/{domain_id}/advanced-rules",
            page=AsyncOffsetPage[WaapAdvancedRule],
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
                        "phase": phase,
                    },
                    advanced_rule_list_params.AdvancedRuleListParams,
                ),
            ),
            model=WaapAdvancedRule,
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
        Delete an advanced rule

        Args:
          domain_id: The domain ID

          rule_id: The advanced rule ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/waap/v1/domains/{domain_id}/advanced-rules/{rule_id}",
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
    ) -> WaapAdvancedRule:
        """
        Retrieve a specific advanced rule assigned to a domain

        Args:
          domain_id: The domain ID

          rule_id: The advanced rule ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/waap/v1/domains/{domain_id}/advanced-rules/{rule_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapAdvancedRule,
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
        Toggle an advanced rule

        Args:
          domain_id: The domain ID

          rule_id: The advanced rule ID

          action: Enable or disable an advanced rule

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not action:
            raise ValueError(f"Expected a non-empty value for `action` but received {action!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            f"/waap/v1/domains/{domain_id}/advanced-rules/{rule_id}/{action}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AdvancedRulesResourceWithRawResponse:
    def __init__(self, advanced_rules: AdvancedRulesResource) -> None:
        self._advanced_rules = advanced_rules

        self.create = to_raw_response_wrapper(
            advanced_rules.create,
        )
        self.update = to_raw_response_wrapper(
            advanced_rules.update,
        )
        self.list = to_raw_response_wrapper(
            advanced_rules.list,
        )
        self.delete = to_raw_response_wrapper(
            advanced_rules.delete,
        )
        self.get = to_raw_response_wrapper(
            advanced_rules.get,
        )
        self.toggle = to_raw_response_wrapper(
            advanced_rules.toggle,
        )


class AsyncAdvancedRulesResourceWithRawResponse:
    def __init__(self, advanced_rules: AsyncAdvancedRulesResource) -> None:
        self._advanced_rules = advanced_rules

        self.create = async_to_raw_response_wrapper(
            advanced_rules.create,
        )
        self.update = async_to_raw_response_wrapper(
            advanced_rules.update,
        )
        self.list = async_to_raw_response_wrapper(
            advanced_rules.list,
        )
        self.delete = async_to_raw_response_wrapper(
            advanced_rules.delete,
        )
        self.get = async_to_raw_response_wrapper(
            advanced_rules.get,
        )
        self.toggle = async_to_raw_response_wrapper(
            advanced_rules.toggle,
        )


class AdvancedRulesResourceWithStreamingResponse:
    def __init__(self, advanced_rules: AdvancedRulesResource) -> None:
        self._advanced_rules = advanced_rules

        self.create = to_streamed_response_wrapper(
            advanced_rules.create,
        )
        self.update = to_streamed_response_wrapper(
            advanced_rules.update,
        )
        self.list = to_streamed_response_wrapper(
            advanced_rules.list,
        )
        self.delete = to_streamed_response_wrapper(
            advanced_rules.delete,
        )
        self.get = to_streamed_response_wrapper(
            advanced_rules.get,
        )
        self.toggle = to_streamed_response_wrapper(
            advanced_rules.toggle,
        )


class AsyncAdvancedRulesResourceWithStreamingResponse:
    def __init__(self, advanced_rules: AsyncAdvancedRulesResource) -> None:
        self._advanced_rules = advanced_rules

        self.create = async_to_streamed_response_wrapper(
            advanced_rules.create,
        )
        self.update = async_to_streamed_response_wrapper(
            advanced_rules.update,
        )
        self.list = async_to_streamed_response_wrapper(
            advanced_rules.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            advanced_rules.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            advanced_rules.get,
        )
        self.toggle = async_to_streamed_response_wrapper(
            advanced_rules.toggle,
        )
