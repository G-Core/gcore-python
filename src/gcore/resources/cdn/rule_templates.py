# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.cdn import rule_template_create_params, rule_template_update_params, rule_template_replace_params
from ..._base_client import make_request_options
from ...types.cdn.rule_template import RuleTemplate
from ...types.cdn.rule_template_list import RuleTemplateList

__all__ = ["RuleTemplatesResource", "AsyncRuleTemplatesResource"]


class RuleTemplatesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RuleTemplatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return RuleTemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RuleTemplatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return RuleTemplatesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        rule: str,
        rule_type: int,
        name: str | Omit = omit,
        options: rule_template_create_params.Options | Omit = omit,
        override_origin_protocol: Optional[Literal["HTTPS", "HTTP", "MATCH"]] | Omit = omit,
        weight: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleTemplate:
        """
        Create rule template

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

          name: Rule template name.

          options: List of options that can be configured for the rule.

              In case of `null` value the option is not added to the rule. Option inherits its
              value from the CDN resource settings.

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
            "/cdn/resources/rule_templates",
            body=maybe_transform(
                {
                    "rule": rule,
                    "rule_type": rule_type,
                    "name": name,
                    "options": options,
                    "override_origin_protocol": override_origin_protocol,
                    "weight": weight,
                },
                rule_template_create_params.RuleTemplateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RuleTemplate,
        )

    def update(
        self,
        rule_template_id: int,
        *,
        name: str | Omit = omit,
        options: rule_template_update_params.Options | Omit = omit,
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
    ) -> RuleTemplate:
        """
        Change rule template

        Args:
          name: Rule template name.

          options: List of options that can be configured for the rule.

              In case of `null` value the option is not added to the rule. Option inherits its
              value from the CDN resource settings.

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
            f"/cdn/resources/rule_templates/{rule_template_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "options": options,
                    "override_origin_protocol": override_origin_protocol,
                    "rule": rule,
                    "rule_type": rule_type,
                    "weight": weight,
                },
                rule_template_update_params.RuleTemplateUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RuleTemplate,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleTemplateList:
        """Get rule templates list"""
        return self._get(
            "/cdn/resources/rule_templates",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RuleTemplateList,
        )

    def delete(
        self,
        rule_template_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete rule template

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/cdn/resources/rule_templates/{rule_template_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        rule_template_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleTemplate:
        """
        Get rule template details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/cdn/resources/rule_templates/{rule_template_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RuleTemplate,
        )

    def replace(
        self,
        rule_template_id: int,
        *,
        rule: str,
        rule_type: int,
        name: str | Omit = omit,
        options: rule_template_replace_params.Options | Omit = omit,
        override_origin_protocol: Optional[Literal["HTTPS", "HTTP", "MATCH"]] | Omit = omit,
        weight: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleTemplate:
        """
        Change rule template

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

          name: Rule template name.

          options: List of options that can be configured for the rule.

              In case of `null` value the option is not added to the rule. Option inherits its
              value from the CDN resource settings.

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
            f"/cdn/resources/rule_templates/{rule_template_id}",
            body=maybe_transform(
                {
                    "rule": rule,
                    "rule_type": rule_type,
                    "name": name,
                    "options": options,
                    "override_origin_protocol": override_origin_protocol,
                    "weight": weight,
                },
                rule_template_replace_params.RuleTemplateReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RuleTemplate,
        )


class AsyncRuleTemplatesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRuleTemplatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRuleTemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRuleTemplatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncRuleTemplatesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        rule: str,
        rule_type: int,
        name: str | Omit = omit,
        options: rule_template_create_params.Options | Omit = omit,
        override_origin_protocol: Optional[Literal["HTTPS", "HTTP", "MATCH"]] | Omit = omit,
        weight: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleTemplate:
        """
        Create rule template

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

          name: Rule template name.

          options: List of options that can be configured for the rule.

              In case of `null` value the option is not added to the rule. Option inherits its
              value from the CDN resource settings.

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
            "/cdn/resources/rule_templates",
            body=await async_maybe_transform(
                {
                    "rule": rule,
                    "rule_type": rule_type,
                    "name": name,
                    "options": options,
                    "override_origin_protocol": override_origin_protocol,
                    "weight": weight,
                },
                rule_template_create_params.RuleTemplateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RuleTemplate,
        )

    async def update(
        self,
        rule_template_id: int,
        *,
        name: str | Omit = omit,
        options: rule_template_update_params.Options | Omit = omit,
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
    ) -> RuleTemplate:
        """
        Change rule template

        Args:
          name: Rule template name.

          options: List of options that can be configured for the rule.

              In case of `null` value the option is not added to the rule. Option inherits its
              value from the CDN resource settings.

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
            f"/cdn/resources/rule_templates/{rule_template_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "options": options,
                    "override_origin_protocol": override_origin_protocol,
                    "rule": rule,
                    "rule_type": rule_type,
                    "weight": weight,
                },
                rule_template_update_params.RuleTemplateUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RuleTemplate,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleTemplateList:
        """Get rule templates list"""
        return await self._get(
            "/cdn/resources/rule_templates",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RuleTemplateList,
        )

    async def delete(
        self,
        rule_template_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete rule template

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/cdn/resources/rule_templates/{rule_template_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        rule_template_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleTemplate:
        """
        Get rule template details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/cdn/resources/rule_templates/{rule_template_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RuleTemplate,
        )

    async def replace(
        self,
        rule_template_id: int,
        *,
        rule: str,
        rule_type: int,
        name: str | Omit = omit,
        options: rule_template_replace_params.Options | Omit = omit,
        override_origin_protocol: Optional[Literal["HTTPS", "HTTP", "MATCH"]] | Omit = omit,
        weight: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleTemplate:
        """
        Change rule template

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

          name: Rule template name.

          options: List of options that can be configured for the rule.

              In case of `null` value the option is not added to the rule. Option inherits its
              value from the CDN resource settings.

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
            f"/cdn/resources/rule_templates/{rule_template_id}",
            body=await async_maybe_transform(
                {
                    "rule": rule,
                    "rule_type": rule_type,
                    "name": name,
                    "options": options,
                    "override_origin_protocol": override_origin_protocol,
                    "weight": weight,
                },
                rule_template_replace_params.RuleTemplateReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RuleTemplate,
        )


class RuleTemplatesResourceWithRawResponse:
    def __init__(self, rule_templates: RuleTemplatesResource) -> None:
        self._rule_templates = rule_templates

        self.create = to_raw_response_wrapper(
            rule_templates.create,
        )
        self.update = to_raw_response_wrapper(
            rule_templates.update,
        )
        self.list = to_raw_response_wrapper(
            rule_templates.list,
        )
        self.delete = to_raw_response_wrapper(
            rule_templates.delete,
        )
        self.get = to_raw_response_wrapper(
            rule_templates.get,
        )
        self.replace = to_raw_response_wrapper(
            rule_templates.replace,
        )


class AsyncRuleTemplatesResourceWithRawResponse:
    def __init__(self, rule_templates: AsyncRuleTemplatesResource) -> None:
        self._rule_templates = rule_templates

        self.create = async_to_raw_response_wrapper(
            rule_templates.create,
        )
        self.update = async_to_raw_response_wrapper(
            rule_templates.update,
        )
        self.list = async_to_raw_response_wrapper(
            rule_templates.list,
        )
        self.delete = async_to_raw_response_wrapper(
            rule_templates.delete,
        )
        self.get = async_to_raw_response_wrapper(
            rule_templates.get,
        )
        self.replace = async_to_raw_response_wrapper(
            rule_templates.replace,
        )


class RuleTemplatesResourceWithStreamingResponse:
    def __init__(self, rule_templates: RuleTemplatesResource) -> None:
        self._rule_templates = rule_templates

        self.create = to_streamed_response_wrapper(
            rule_templates.create,
        )
        self.update = to_streamed_response_wrapper(
            rule_templates.update,
        )
        self.list = to_streamed_response_wrapper(
            rule_templates.list,
        )
        self.delete = to_streamed_response_wrapper(
            rule_templates.delete,
        )
        self.get = to_streamed_response_wrapper(
            rule_templates.get,
        )
        self.replace = to_streamed_response_wrapper(
            rule_templates.replace,
        )


class AsyncRuleTemplatesResourceWithStreamingResponse:
    def __init__(self, rule_templates: AsyncRuleTemplatesResource) -> None:
        self._rule_templates = rule_templates

        self.create = async_to_streamed_response_wrapper(
            rule_templates.create,
        )
        self.update = async_to_streamed_response_wrapper(
            rule_templates.update,
        )
        self.list = async_to_streamed_response_wrapper(
            rule_templates.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            rule_templates.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            rule_templates.get,
        )
        self.replace = async_to_streamed_response_wrapper(
            rule_templates.replace,
        )
