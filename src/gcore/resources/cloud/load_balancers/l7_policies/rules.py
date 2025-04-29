# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.cloud.l7_rule import L7Rule
from .....types.cloud.l7_rule_list import L7RuleList
from .....types.cloud.task_id_list import TaskIDList
from .....types.cloud.load_balancers.l7_policies import rule_create_params, rule_replace_params

__all__ = ["RulesResource", "AsyncRulesResource"]


class RulesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return RulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
        """
        return RulesResourceWithStreamingResponse(self)

    def create(
        self,
        l7policy_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        compare_type: Literal["CONTAINS", "ENDS_WITH", "EQUAL_TO", "REGEX", "STARTS_WITH"],
        type: Literal[
            "COOKIE",
            "FILE_TYPE",
            "HEADER",
            "HOST_NAME",
            "PATH",
            "SSL_CONN_HAS_CERT",
            "SSL_DN_FIELD",
            "SSL_VERIFY_RESULT",
        ],
        value: str,
        invert: bool | NotGiven = NOT_GIVEN,
        key: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Create load balancer L7 rule

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D%2Frules/post/parameters/0/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D%2Frules/post/parameters/1/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules'].post.parameters[1].schema"

          l7policy_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D%2Frules/post/parameters/2/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules'].post.parameters[2].schema"

          compare_type: '#/components/schemas/CreateL7RuleSchema/properties/compare_type'
              "$.components.schemas.CreateL7RuleSchema.properties.compare_type"

          type: '#/components/schemas/CreateL7RuleSchema/properties/type'
              "$.components.schemas.CreateL7RuleSchema.properties.type"

          value: '#/components/schemas/CreateL7RuleSchema/properties/value'
              "$.components.schemas.CreateL7RuleSchema.properties.value"

          invert: '#/components/schemas/CreateL7RuleSchema/properties/invert'
              "$.components.schemas.CreateL7RuleSchema.properties.invert"

          key: '#/components/schemas/CreateL7RuleSchema/properties/key'
              "$.components.schemas.CreateL7RuleSchema.properties.key"

          tags: '#/components/schemas/CreateL7RuleSchema/properties/tags'
              "$.components.schemas.CreateL7RuleSchema.properties.tags"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not l7policy_id:
            raise ValueError(f"Expected a non-empty value for `l7policy_id` but received {l7policy_id!r}")
        return self._post(
            f"/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules",
            body=maybe_transform(
                {
                    "compare_type": compare_type,
                    "type": type,
                    "value": value,
                    "invert": invert,
                    "key": key,
                    "tags": tags,
                },
                rule_create_params.RuleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def list(
        self,
        l7policy_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> L7RuleList:
        """
        List load balancer L7 policy rules

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D%2Frules/get/parameters/0/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D%2Frules/get/parameters/1/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules'].get.parameters[1].schema"

          l7policy_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D%2Frules/get/parameters/2/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules'].get.parameters[2].schema"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not l7policy_id:
            raise ValueError(f"Expected a non-empty value for `l7policy_id` but received {l7policy_id!r}")
        return self._get(
            f"/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=L7RuleList,
        )

    def delete(
        self,
        l7rule_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        l7policy_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Delete load balancer L7 rule

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D%2Frules%2F%7Bl7rule_id%7D/delete/parameters/0/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules/{l7rule_id}']['delete'].parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D%2Frules%2F%7Bl7rule_id%7D/delete/parameters/1/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules/{l7rule_id}']['delete'].parameters[1].schema"

          l7policy_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D%2Frules%2F%7Bl7rule_id%7D/delete/parameters/2/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules/{l7rule_id}']['delete'].parameters[2].schema"

          l7rule_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D%2Frules%2F%7Bl7rule_id%7D/delete/parameters/3/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules/{l7rule_id}']['delete'].parameters[3].schema"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not l7policy_id:
            raise ValueError(f"Expected a non-empty value for `l7policy_id` but received {l7policy_id!r}")
        if not l7rule_id:
            raise ValueError(f"Expected a non-empty value for `l7rule_id` but received {l7rule_id!r}")
        return self._delete(
            f"/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules/{l7rule_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def get(
        self,
        l7rule_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        l7policy_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> L7Rule:
        """
        Get load balancer L7 rule

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D%2Frules%2F%7Bl7rule_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules/{l7rule_id}'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D%2Frules%2F%7Bl7rule_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules/{l7rule_id}'].get.parameters[1].schema"

          l7policy_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D%2Frules%2F%7Bl7rule_id%7D/get/parameters/2/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules/{l7rule_id}'].get.parameters[2].schema"

          l7rule_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D%2Frules%2F%7Bl7rule_id%7D/get/parameters/3/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules/{l7rule_id}'].get.parameters[3].schema"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not l7policy_id:
            raise ValueError(f"Expected a non-empty value for `l7policy_id` but received {l7policy_id!r}")
        if not l7rule_id:
            raise ValueError(f"Expected a non-empty value for `l7rule_id` but received {l7rule_id!r}")
        return self._get(
            f"/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules/{l7rule_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=L7Rule,
        )

    def replace(
        self,
        l7rule_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        l7policy_id: str,
        compare_type: Literal["CONTAINS", "ENDS_WITH", "EQUAL_TO", "REGEX", "STARTS_WITH"] | NotGiven = NOT_GIVEN,
        invert: bool | NotGiven = NOT_GIVEN,
        key: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        type: Literal[
            "COOKIE",
            "FILE_TYPE",
            "HEADER",
            "HOST_NAME",
            "PATH",
            "SSL_CONN_HAS_CERT",
            "SSL_DN_FIELD",
            "SSL_VERIFY_RESULT",
        ]
        | NotGiven = NOT_GIVEN,
        value: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Replace load balancer L7 rule properties

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D%2Frules%2F%7Bl7rule_id%7D/put/parameters/0/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules/{l7rule_id}'].put.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D%2Frules%2F%7Bl7rule_id%7D/put/parameters/1/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules/{l7rule_id}'].put.parameters[1].schema"

          l7policy_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D%2Frules%2F%7Bl7rule_id%7D/put/parameters/2/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules/{l7rule_id}'].put.parameters[2].schema"

          l7rule_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D%2Frules%2F%7Bl7rule_id%7D/put/parameters/3/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules/{l7rule_id}'].put.parameters[3].schema"

          compare_type: '#/components/schemas/UpdateL7RuleSchema/properties/compare_type'
              "$.components.schemas.UpdateL7RuleSchema.properties.compare_type"

          invert: '#/components/schemas/UpdateL7RuleSchema/properties/invert'
              "$.components.schemas.UpdateL7RuleSchema.properties.invert"

          key: '#/components/schemas/UpdateL7RuleSchema/properties/key'
              "$.components.schemas.UpdateL7RuleSchema.properties.key"

          tags: '#/components/schemas/UpdateL7RuleSchema/properties/tags'
              "$.components.schemas.UpdateL7RuleSchema.properties.tags"

          type: '#/components/schemas/UpdateL7RuleSchema/properties/type'
              "$.components.schemas.UpdateL7RuleSchema.properties.type"

          value: '#/components/schemas/UpdateL7RuleSchema/properties/value'
              "$.components.schemas.UpdateL7RuleSchema.properties.value"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not l7policy_id:
            raise ValueError(f"Expected a non-empty value for `l7policy_id` but received {l7policy_id!r}")
        if not l7rule_id:
            raise ValueError(f"Expected a non-empty value for `l7rule_id` but received {l7rule_id!r}")
        return self._put(
            f"/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules/{l7rule_id}",
            body=maybe_transform(
                {
                    "compare_type": compare_type,
                    "invert": invert,
                    "key": key,
                    "tags": tags,
                    "type": type,
                    "value": value,
                },
                rule_replace_params.RuleReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )


class AsyncRulesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
        """
        return AsyncRulesResourceWithStreamingResponse(self)

    async def create(
        self,
        l7policy_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        compare_type: Literal["CONTAINS", "ENDS_WITH", "EQUAL_TO", "REGEX", "STARTS_WITH"],
        type: Literal[
            "COOKIE",
            "FILE_TYPE",
            "HEADER",
            "HOST_NAME",
            "PATH",
            "SSL_CONN_HAS_CERT",
            "SSL_DN_FIELD",
            "SSL_VERIFY_RESULT",
        ],
        value: str,
        invert: bool | NotGiven = NOT_GIVEN,
        key: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Create load balancer L7 rule

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D%2Frules/post/parameters/0/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D%2Frules/post/parameters/1/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules'].post.parameters[1].schema"

          l7policy_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D%2Frules/post/parameters/2/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules'].post.parameters[2].schema"

          compare_type: '#/components/schemas/CreateL7RuleSchema/properties/compare_type'
              "$.components.schemas.CreateL7RuleSchema.properties.compare_type"

          type: '#/components/schemas/CreateL7RuleSchema/properties/type'
              "$.components.schemas.CreateL7RuleSchema.properties.type"

          value: '#/components/schemas/CreateL7RuleSchema/properties/value'
              "$.components.schemas.CreateL7RuleSchema.properties.value"

          invert: '#/components/schemas/CreateL7RuleSchema/properties/invert'
              "$.components.schemas.CreateL7RuleSchema.properties.invert"

          key: '#/components/schemas/CreateL7RuleSchema/properties/key'
              "$.components.schemas.CreateL7RuleSchema.properties.key"

          tags: '#/components/schemas/CreateL7RuleSchema/properties/tags'
              "$.components.schemas.CreateL7RuleSchema.properties.tags"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not l7policy_id:
            raise ValueError(f"Expected a non-empty value for `l7policy_id` but received {l7policy_id!r}")
        return await self._post(
            f"/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules",
            body=await async_maybe_transform(
                {
                    "compare_type": compare_type,
                    "type": type,
                    "value": value,
                    "invert": invert,
                    "key": key,
                    "tags": tags,
                },
                rule_create_params.RuleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def list(
        self,
        l7policy_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> L7RuleList:
        """
        List load balancer L7 policy rules

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D%2Frules/get/parameters/0/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D%2Frules/get/parameters/1/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules'].get.parameters[1].schema"

          l7policy_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D%2Frules/get/parameters/2/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules'].get.parameters[2].schema"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not l7policy_id:
            raise ValueError(f"Expected a non-empty value for `l7policy_id` but received {l7policy_id!r}")
        return await self._get(
            f"/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=L7RuleList,
        )

    async def delete(
        self,
        l7rule_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        l7policy_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Delete load balancer L7 rule

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D%2Frules%2F%7Bl7rule_id%7D/delete/parameters/0/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules/{l7rule_id}']['delete'].parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D%2Frules%2F%7Bl7rule_id%7D/delete/parameters/1/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules/{l7rule_id}']['delete'].parameters[1].schema"

          l7policy_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D%2Frules%2F%7Bl7rule_id%7D/delete/parameters/2/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules/{l7rule_id}']['delete'].parameters[2].schema"

          l7rule_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D%2Frules%2F%7Bl7rule_id%7D/delete/parameters/3/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules/{l7rule_id}']['delete'].parameters[3].schema"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not l7policy_id:
            raise ValueError(f"Expected a non-empty value for `l7policy_id` but received {l7policy_id!r}")
        if not l7rule_id:
            raise ValueError(f"Expected a non-empty value for `l7rule_id` but received {l7rule_id!r}")
        return await self._delete(
            f"/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules/{l7rule_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def get(
        self,
        l7rule_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        l7policy_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> L7Rule:
        """
        Get load balancer L7 rule

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D%2Frules%2F%7Bl7rule_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules/{l7rule_id}'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D%2Frules%2F%7Bl7rule_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules/{l7rule_id}'].get.parameters[1].schema"

          l7policy_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D%2Frules%2F%7Bl7rule_id%7D/get/parameters/2/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules/{l7rule_id}'].get.parameters[2].schema"

          l7rule_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D%2Frules%2F%7Bl7rule_id%7D/get/parameters/3/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules/{l7rule_id}'].get.parameters[3].schema"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not l7policy_id:
            raise ValueError(f"Expected a non-empty value for `l7policy_id` but received {l7policy_id!r}")
        if not l7rule_id:
            raise ValueError(f"Expected a non-empty value for `l7rule_id` but received {l7rule_id!r}")
        return await self._get(
            f"/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules/{l7rule_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=L7Rule,
        )

    async def replace(
        self,
        l7rule_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        l7policy_id: str,
        compare_type: Literal["CONTAINS", "ENDS_WITH", "EQUAL_TO", "REGEX", "STARTS_WITH"] | NotGiven = NOT_GIVEN,
        invert: bool | NotGiven = NOT_GIVEN,
        key: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        type: Literal[
            "COOKIE",
            "FILE_TYPE",
            "HEADER",
            "HOST_NAME",
            "PATH",
            "SSL_CONN_HAS_CERT",
            "SSL_DN_FIELD",
            "SSL_VERIFY_RESULT",
        ]
        | NotGiven = NOT_GIVEN,
        value: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Replace load balancer L7 rule properties

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D%2Frules%2F%7Bl7rule_id%7D/put/parameters/0/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules/{l7rule_id}'].put.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D%2Frules%2F%7Bl7rule_id%7D/put/parameters/1/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules/{l7rule_id}'].put.parameters[1].schema"

          l7policy_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D%2Frules%2F%7Bl7rule_id%7D/put/parameters/2/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules/{l7rule_id}'].put.parameters[2].schema"

          l7rule_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D%2Frules%2F%7Bl7rule_id%7D/put/parameters/3/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules/{l7rule_id}'].put.parameters[3].schema"

          compare_type: '#/components/schemas/UpdateL7RuleSchema/properties/compare_type'
              "$.components.schemas.UpdateL7RuleSchema.properties.compare_type"

          invert: '#/components/schemas/UpdateL7RuleSchema/properties/invert'
              "$.components.schemas.UpdateL7RuleSchema.properties.invert"

          key: '#/components/schemas/UpdateL7RuleSchema/properties/key'
              "$.components.schemas.UpdateL7RuleSchema.properties.key"

          tags: '#/components/schemas/UpdateL7RuleSchema/properties/tags'
              "$.components.schemas.UpdateL7RuleSchema.properties.tags"

          type: '#/components/schemas/UpdateL7RuleSchema/properties/type'
              "$.components.schemas.UpdateL7RuleSchema.properties.type"

          value: '#/components/schemas/UpdateL7RuleSchema/properties/value'
              "$.components.schemas.UpdateL7RuleSchema.properties.value"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not l7policy_id:
            raise ValueError(f"Expected a non-empty value for `l7policy_id` but received {l7policy_id!r}")
        if not l7rule_id:
            raise ValueError(f"Expected a non-empty value for `l7rule_id` but received {l7rule_id!r}")
        return await self._put(
            f"/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules/{l7rule_id}",
            body=await async_maybe_transform(
                {
                    "compare_type": compare_type,
                    "invert": invert,
                    "key": key,
                    "tags": tags,
                    "type": type,
                    "value": value,
                },
                rule_replace_params.RuleReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )


class RulesResourceWithRawResponse:
    def __init__(self, rules: RulesResource) -> None:
        self._rules = rules

        self.create = to_raw_response_wrapper(
            rules.create,
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
