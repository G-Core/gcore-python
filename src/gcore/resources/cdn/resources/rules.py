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
from ...._base_client import make_request_options
from ....types.cdn.resources import rule_create_params, rule_update_params, rule_replace_params
from ....types.cdn.resources.cdn_resource_rule import CdnResourceRule
from ....types.cdn.resources.rule_list_response import RuleListResponse

__all__ = ["RulesResource", "AsyncRulesResource"]


class RulesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return RulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return RulesResourceWithStreamingResponse(self)

    def create(
        self,
        resource_id: int,
        *,
        name: str,
        rule: str,
        rule_type: int,
        active: bool | Omit = omit,
        options: rule_create_params.Options | Omit = omit,
        origin_group: Optional[int] | Omit = omit,
        override_origin_protocol: Optional[Literal["HTTPS", "HTTP", "MATCH"]] | Omit = omit,
        weight: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CdnResourceRule:
        """
        Create rule

        Args:
          name: Rule name.

          rule: Path to the file or folder for which the rule will be applied.

              The rule is applied if the requested URI matches the rule path.

              We add a leading forward slash to any rule path. Specify a path without a
              forward slash.

          rule_type: Rule type.

              Possible values:

              - **Type 0** - Regular expression. Must start with '^/' or '/'.
              - **Type 1** - Regular expression. Note that for this rule type we automatically
                add / to each rule pattern before your regular expression. This type is
                **legacy**, please use Type 0.

          active: Enables or disables a rule.

              Possible values:

              - **true** - Rule is active, rule settings are applied.
              - **false** - Rule is inactive, rule settings are not applied.

          options: List of options that can be configured for the rule.

              In case of `null` value the option is not added to the rule. Option inherits its
              value from the CDN resource settings.

          origin_group: ID of the origin group to which the rule is applied.

              If the origin group is not specified, the rule is applied to the origin group
              that the CDN resource is associated with.

          override_origin_protocol: Sets a protocol other than the one specified in the CDN resource settings to
              connect to the origin.

              Possible values:

              - **HTTPS** - CDN servers connect to origin via HTTPS protocol.
              - **HTTP** - CDN servers connect to origin via HTTP protocol.
              - **MATCH** - Connection protocol is chosen automatically; in this case, content
                on origin source should be available for the CDN both through HTTP and HTTPS
                protocols.
              - **null** - `originProtocol` setting is inherited from the CDN resource
                settings.

          weight: Rule execution order: from lowest (1) to highest.

              If requested URI matches multiple rules, the one higher in the order of the
              rules will be applied.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/cdn/resources/{resource_id}/rules",
            body=maybe_transform(
                {
                    "name": name,
                    "rule": rule,
                    "rule_type": rule_type,
                    "active": active,
                    "options": options,
                    "origin_group": origin_group,
                    "override_origin_protocol": override_origin_protocol,
                    "weight": weight,
                },
                rule_create_params.RuleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CdnResourceRule,
        )

    def update(
        self,
        rule_id: int,
        *,
        resource_id: int,
        active: bool | Omit = omit,
        name: str | Omit = omit,
        options: rule_update_params.Options | Omit = omit,
        origin_group: Optional[int] | Omit = omit,
        override_origin_protocol: Optional[Literal["HTTPS", "HTTP", "MATCH"]] | Omit = omit,
        rule: str | Omit = omit,
        rule_type: int | Omit = omit,
        weight: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CdnResourceRule:
        """
        Change rule

        Args:
          active: Enables or disables a rule.

              Possible values:

              - **true** - Rule is active, rule settings are applied.
              - **false** - Rule is inactive, rule settings are not applied.

          name: Rule name.

          options: List of options that can be configured for the rule.

              In case of `null` value the option is not added to the rule. Option inherits its
              value from the CDN resource settings.

          origin_group: ID of the origin group to which the rule is applied.

              If the origin group is not specified, the rule is applied to the origin group
              that the CDN resource is associated with.

          override_origin_protocol: Sets a protocol other than the one specified in the CDN resource settings to
              connect to the origin.

              Possible values:

              - **HTTPS** - CDN servers connect to origin via HTTPS protocol.
              - **HTTP** - CDN servers connect to origin via HTTP protocol.
              - **MATCH** - Connection protocol is chosen automatically; in this case, content
                on origin source should be available for the CDN both through HTTP and HTTPS
                protocols.
              - **null** - `originProtocol` setting is inherited from the CDN resource
                settings.

          rule: Path to the file or folder for which the rule will be applied.

              The rule is applied if the requested URI matches the rule path.

              We add a leading forward slash to any rule path. Specify a path without a
              forward slash.

          rule_type: Rule type.

              Possible values:

              - **Type 0** - Regular expression. Must start with '^/' or '/'.
              - **Type 1** - Regular expression. Note that for this rule type we automatically
                add / to each rule pattern before your regular expression. This type is
                **legacy**, please use Type 0.

          weight: Rule execution order: from lowest (1) to highest.

              If requested URI matches multiple rules, the one higher in the order of the
              rules will be applied.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/cdn/resources/{resource_id}/rules/{rule_id}",
            body=maybe_transform(
                {
                    "active": active,
                    "name": name,
                    "options": options,
                    "origin_group": origin_group,
                    "override_origin_protocol": override_origin_protocol,
                    "rule": rule,
                    "rule_type": rule_type,
                    "weight": weight,
                },
                rule_update_params.RuleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CdnResourceRule,
        )

    def list(
        self,
        resource_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleListResponse:
        """
        Get rules list

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/cdn/resources/{resource_id}/rules",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RuleListResponse,
        )

    def delete(
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
    ) -> None:
        """
        Delete the rule from the system permanently.

        Notes:

        - **Deactivation Requirement**: Set the `active` attribute to `false` before
          deletion.
        - **Irreversibility**: This action is irreversible. Once deleted, the rule
          cannot be recovered.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/cdn/resources/{resource_id}/rules/{rule_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
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
    ) -> CdnResourceRule:
        """
        Get rule details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/cdn/resources/{resource_id}/rules/{rule_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CdnResourceRule,
        )

    def replace(
        self,
        rule_id: int,
        *,
        resource_id: int,
        rule: str,
        rule_type: int,
        active: bool | Omit = omit,
        name: str | Omit = omit,
        options: rule_replace_params.Options | Omit = omit,
        origin_group: Optional[int] | Omit = omit,
        override_origin_protocol: Optional[Literal["HTTPS", "HTTP", "MATCH"]] | Omit = omit,
        weight: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CdnResourceRule:
        """
        Change rule

        Args:
          rule: Path to the file or folder for which the rule will be applied.

              The rule is applied if the requested URI matches the rule path.

              We add a leading forward slash to any rule path. Specify a path without a
              forward slash.

          rule_type: Rule type.

              Possible values:

              - **Type 0** - Regular expression. Must start with '^/' or '/'.
              - **Type 1** - Regular expression. Note that for this rule type we automatically
                add / to each rule pattern before your regular expression. This type is
                **legacy**, please use Type 0.

          active: Enables or disables a rule.

              Possible values:

              - **true** - Rule is active, rule settings are applied.
              - **false** - Rule is inactive, rule settings are not applied.

          name: Rule name.

          options: List of options that can be configured for the rule.

              In case of `null` value the option is not added to the rule. Option inherits its
              value from the CDN resource settings.

          origin_group: ID of the origin group to which the rule is applied.

              If the origin group is not specified, the rule is applied to the origin group
              that the CDN resource is associated with.

          override_origin_protocol: Sets a protocol other than the one specified in the CDN resource settings to
              connect to the origin.

              Possible values:

              - **HTTPS** - CDN servers connect to origin via HTTPS protocol.
              - **HTTP** - CDN servers connect to origin via HTTP protocol.
              - **MATCH** - Connection protocol is chosen automatically; in this case, content
                on origin source should be available for the CDN both through HTTP and HTTPS
                protocols.
              - **null** - `originProtocol` setting is inherited from the CDN resource
                settings.

          weight: Rule execution order: from lowest (1) to highest.

              If requested URI matches multiple rules, the one higher in the order of the
              rules will be applied.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/cdn/resources/{resource_id}/rules/{rule_id}",
            body=maybe_transform(
                {
                    "rule": rule,
                    "rule_type": rule_type,
                    "active": active,
                    "name": name,
                    "options": options,
                    "origin_group": origin_group,
                    "override_origin_protocol": override_origin_protocol,
                    "weight": weight,
                },
                rule_replace_params.RuleReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CdnResourceRule,
        )


class AsyncRulesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncRulesResourceWithStreamingResponse(self)

    async def create(
        self,
        resource_id: int,
        *,
        name: str,
        rule: str,
        rule_type: int,
        active: bool | Omit = omit,
        options: rule_create_params.Options | Omit = omit,
        origin_group: Optional[int] | Omit = omit,
        override_origin_protocol: Optional[Literal["HTTPS", "HTTP", "MATCH"]] | Omit = omit,
        weight: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CdnResourceRule:
        """
        Create rule

        Args:
          name: Rule name.

          rule: Path to the file or folder for which the rule will be applied.

              The rule is applied if the requested URI matches the rule path.

              We add a leading forward slash to any rule path. Specify a path without a
              forward slash.

          rule_type: Rule type.

              Possible values:

              - **Type 0** - Regular expression. Must start with '^/' or '/'.
              - **Type 1** - Regular expression. Note that for this rule type we automatically
                add / to each rule pattern before your regular expression. This type is
                **legacy**, please use Type 0.

          active: Enables or disables a rule.

              Possible values:

              - **true** - Rule is active, rule settings are applied.
              - **false** - Rule is inactive, rule settings are not applied.

          options: List of options that can be configured for the rule.

              In case of `null` value the option is not added to the rule. Option inherits its
              value from the CDN resource settings.

          origin_group: ID of the origin group to which the rule is applied.

              If the origin group is not specified, the rule is applied to the origin group
              that the CDN resource is associated with.

          override_origin_protocol: Sets a protocol other than the one specified in the CDN resource settings to
              connect to the origin.

              Possible values:

              - **HTTPS** - CDN servers connect to origin via HTTPS protocol.
              - **HTTP** - CDN servers connect to origin via HTTP protocol.
              - **MATCH** - Connection protocol is chosen automatically; in this case, content
                on origin source should be available for the CDN both through HTTP and HTTPS
                protocols.
              - **null** - `originProtocol` setting is inherited from the CDN resource
                settings.

          weight: Rule execution order: from lowest (1) to highest.

              If requested URI matches multiple rules, the one higher in the order of the
              rules will be applied.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/cdn/resources/{resource_id}/rules",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "rule": rule,
                    "rule_type": rule_type,
                    "active": active,
                    "options": options,
                    "origin_group": origin_group,
                    "override_origin_protocol": override_origin_protocol,
                    "weight": weight,
                },
                rule_create_params.RuleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CdnResourceRule,
        )

    async def update(
        self,
        rule_id: int,
        *,
        resource_id: int,
        active: bool | Omit = omit,
        name: str | Omit = omit,
        options: rule_update_params.Options | Omit = omit,
        origin_group: Optional[int] | Omit = omit,
        override_origin_protocol: Optional[Literal["HTTPS", "HTTP", "MATCH"]] | Omit = omit,
        rule: str | Omit = omit,
        rule_type: int | Omit = omit,
        weight: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CdnResourceRule:
        """
        Change rule

        Args:
          active: Enables or disables a rule.

              Possible values:

              - **true** - Rule is active, rule settings are applied.
              - **false** - Rule is inactive, rule settings are not applied.

          name: Rule name.

          options: List of options that can be configured for the rule.

              In case of `null` value the option is not added to the rule. Option inherits its
              value from the CDN resource settings.

          origin_group: ID of the origin group to which the rule is applied.

              If the origin group is not specified, the rule is applied to the origin group
              that the CDN resource is associated with.

          override_origin_protocol: Sets a protocol other than the one specified in the CDN resource settings to
              connect to the origin.

              Possible values:

              - **HTTPS** - CDN servers connect to origin via HTTPS protocol.
              - **HTTP** - CDN servers connect to origin via HTTP protocol.
              - **MATCH** - Connection protocol is chosen automatically; in this case, content
                on origin source should be available for the CDN both through HTTP and HTTPS
                protocols.
              - **null** - `originProtocol` setting is inherited from the CDN resource
                settings.

          rule: Path to the file or folder for which the rule will be applied.

              The rule is applied if the requested URI matches the rule path.

              We add a leading forward slash to any rule path. Specify a path without a
              forward slash.

          rule_type: Rule type.

              Possible values:

              - **Type 0** - Regular expression. Must start with '^/' or '/'.
              - **Type 1** - Regular expression. Note that for this rule type we automatically
                add / to each rule pattern before your regular expression. This type is
                **legacy**, please use Type 0.

          weight: Rule execution order: from lowest (1) to highest.

              If requested URI matches multiple rules, the one higher in the order of the
              rules will be applied.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/cdn/resources/{resource_id}/rules/{rule_id}",
            body=await async_maybe_transform(
                {
                    "active": active,
                    "name": name,
                    "options": options,
                    "origin_group": origin_group,
                    "override_origin_protocol": override_origin_protocol,
                    "rule": rule,
                    "rule_type": rule_type,
                    "weight": weight,
                },
                rule_update_params.RuleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CdnResourceRule,
        )

    async def list(
        self,
        resource_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleListResponse:
        """
        Get rules list

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/cdn/resources/{resource_id}/rules",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RuleListResponse,
        )

    async def delete(
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
    ) -> None:
        """
        Delete the rule from the system permanently.

        Notes:

        - **Deactivation Requirement**: Set the `active` attribute to `false` before
          deletion.
        - **Irreversibility**: This action is irreversible. Once deleted, the rule
          cannot be recovered.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/cdn/resources/{resource_id}/rules/{rule_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
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
    ) -> CdnResourceRule:
        """
        Get rule details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/cdn/resources/{resource_id}/rules/{rule_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CdnResourceRule,
        )

    async def replace(
        self,
        rule_id: int,
        *,
        resource_id: int,
        rule: str,
        rule_type: int,
        active: bool | Omit = omit,
        name: str | Omit = omit,
        options: rule_replace_params.Options | Omit = omit,
        origin_group: Optional[int] | Omit = omit,
        override_origin_protocol: Optional[Literal["HTTPS", "HTTP", "MATCH"]] | Omit = omit,
        weight: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CdnResourceRule:
        """
        Change rule

        Args:
          rule: Path to the file or folder for which the rule will be applied.

              The rule is applied if the requested URI matches the rule path.

              We add a leading forward slash to any rule path. Specify a path without a
              forward slash.

          rule_type: Rule type.

              Possible values:

              - **Type 0** - Regular expression. Must start with '^/' or '/'.
              - **Type 1** - Regular expression. Note that for this rule type we automatically
                add / to each rule pattern before your regular expression. This type is
                **legacy**, please use Type 0.

          active: Enables or disables a rule.

              Possible values:

              - **true** - Rule is active, rule settings are applied.
              - **false** - Rule is inactive, rule settings are not applied.

          name: Rule name.

          options: List of options that can be configured for the rule.

              In case of `null` value the option is not added to the rule. Option inherits its
              value from the CDN resource settings.

          origin_group: ID of the origin group to which the rule is applied.

              If the origin group is not specified, the rule is applied to the origin group
              that the CDN resource is associated with.

          override_origin_protocol: Sets a protocol other than the one specified in the CDN resource settings to
              connect to the origin.

              Possible values:

              - **HTTPS** - CDN servers connect to origin via HTTPS protocol.
              - **HTTP** - CDN servers connect to origin via HTTP protocol.
              - **MATCH** - Connection protocol is chosen automatically; in this case, content
                on origin source should be available for the CDN both through HTTP and HTTPS
                protocols.
              - **null** - `originProtocol` setting is inherited from the CDN resource
                settings.

          weight: Rule execution order: from lowest (1) to highest.

              If requested URI matches multiple rules, the one higher in the order of the
              rules will be applied.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/cdn/resources/{resource_id}/rules/{rule_id}",
            body=await async_maybe_transform(
                {
                    "rule": rule,
                    "rule_type": rule_type,
                    "active": active,
                    "name": name,
                    "options": options,
                    "origin_group": origin_group,
                    "override_origin_protocol": override_origin_protocol,
                    "weight": weight,
                },
                rule_replace_params.RuleReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CdnResourceRule,
        )


class RulesResourceWithRawResponse:
    def __init__(self, rules: RulesResource) -> None:
        self._rules = rules

        self.create = to_raw_response_wrapper(
            rules.create,
        )
        self.update = to_raw_response_wrapper(
            rules.update,
        )
        self.list = to_raw_response_wrapper(
            rules.list,
        )
        self.delete = to_raw_response_wrapper(
            rules.delete,
        )
        self.get = to_raw_response_wrapper(
            rules.get,
        )
        self.replace = to_raw_response_wrapper(
            rules.replace,
        )


class AsyncRulesResourceWithRawResponse:
    def __init__(self, rules: AsyncRulesResource) -> None:
        self._rules = rules

        self.create = async_to_raw_response_wrapper(
            rules.create,
        )
        self.update = async_to_raw_response_wrapper(
            rules.update,
        )
        self.list = async_to_raw_response_wrapper(
            rules.list,
        )
        self.delete = async_to_raw_response_wrapper(
            rules.delete,
        )
        self.get = async_to_raw_response_wrapper(
            rules.get,
        )
        self.replace = async_to_raw_response_wrapper(
            rules.replace,
        )


class RulesResourceWithStreamingResponse:
    def __init__(self, rules: RulesResource) -> None:
        self._rules = rules

        self.create = to_streamed_response_wrapper(
            rules.create,
        )
        self.update = to_streamed_response_wrapper(
            rules.update,
        )
        self.list = to_streamed_response_wrapper(
            rules.list,
        )
        self.delete = to_streamed_response_wrapper(
            rules.delete,
        )
        self.get = to_streamed_response_wrapper(
            rules.get,
        )
        self.replace = to_streamed_response_wrapper(
            rules.replace,
        )


class AsyncRulesResourceWithStreamingResponse:
    def __init__(self, rules: AsyncRulesResource) -> None:
        self._rules = rules

        self.create = async_to_streamed_response_wrapper(
            rules.create,
        )
        self.update = async_to_streamed_response_wrapper(
            rules.update,
        )
        self.list = async_to_streamed_response_wrapper(
            rules.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            rules.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            rules.get,
        )
        self.replace = async_to_streamed_response_wrapper(
            rules.replace,
        )
