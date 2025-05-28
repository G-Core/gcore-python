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
from .....types.cloud.task_id_list import TaskIDList
from .....types.cloud.load_balancer_l7_rule import LoadBalancerL7Rule
from .....types.cloud.load_balancer_l7_rule_list import LoadBalancerL7RuleList
from .....types.cloud.load_balancers.l7_policies import rule_create_params, rule_replace_params

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
          compare_type: The comparison type for the L7 rule

          type: The L7 rule type

          value: The value to use for the comparison. For example, the file type to compare

          invert: When true the logic of the rule is inverted. For example, with invert true,
              'equal to' would become 'not equal to'. Default is false.

          key: The key to use for the comparison. For example, the name of the cookie to
              evaluate.

          tags: A list of simple strings assigned to the l7 rule

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
    ) -> LoadBalancerL7RuleList:
        """
        List load balancer L7 policy rules

        Args:
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
            cast_to=LoadBalancerL7RuleList,
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
    ) -> LoadBalancerL7Rule:
        """
        Get load balancer L7 rule

        Args:
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
            cast_to=LoadBalancerL7Rule,
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
          compare_type: The comparison type for the L7 rule

          invert: When true the logic of the rule is inverted. For example, with invert true,
              'equal to' would become 'not equal to'. Default is false.

          key: The key to use for the comparison. For example, the name of the cookie to
              evaluate.

          tags: A list of simple strings assigned to the l7 rule

          type: The L7 rule type

          value: The value to use for the comparison. For example, the file type to compare

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

    def create_and_poll(
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
        polling_interval_seconds: int | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LoadBalancerL7Rule:
        response = self.create(
            l7policy_id=l7policy_id,
            project_id=project_id,
            region_id=region_id,
            compare_type=compare_type,
            type=type,
            value=value,
            invert=invert,
            key=key,
            tags=tags,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks or len(response.tasks) != 1:
            raise ValueError(f"Expected exactly one task to be created")
        task = self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
        )
        if not task.created_resources or not task.created_resources.l7rules or len(task.created_resources.l7rules) != 1:
            raise ValueError(f"Expected exactly one resource to be created in a task")
        return self.get(
            l7rule_id=task.created_resources.l7rules[0],
            project_id=project_id,
            region_id=region_id,
            l7policy_id=l7policy_id,
            extra_headers=extra_headers,
            timeout=timeout,
        )

    def delete_and_poll(
        self,
        l7rule_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        l7policy_id: str,
        polling_interval_seconds: int | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> None:
        """
        Delete L7 rule and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.delete(
            l7rule_id=l7rule_id,
            project_id=project_id,
            region_id=region_id,
            l7policy_id=l7policy_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks:
            raise ValueError("Expected at least one task to be created")
        self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
        )

    def replace_and_poll(
        self,
        l7rule_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        l7policy_id: str,
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
        polling_interval_seconds: int | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LoadBalancerL7Rule:
        """
        Replace L7 rule and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.replace(
            l7rule_id=l7rule_id,
            project_id=project_id,
            region_id=region_id,
            l7policy_id=l7policy_id,
            compare_type=compare_type,
            type=type,
            value=value,
            invert=invert,
            key=key,
            tags=tags,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks:
            raise ValueError("Expected at least one task to be created")
        self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
        )
        return self.get(
            l7rule_id=l7rule_id,
            project_id=project_id,
            region_id=region_id,
            l7policy_id=l7policy_id,
            extra_headers=extra_headers,
            timeout=timeout,
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
          compare_type: The comparison type for the L7 rule

          type: The L7 rule type

          value: The value to use for the comparison. For example, the file type to compare

          invert: When true the logic of the rule is inverted. For example, with invert true,
              'equal to' would become 'not equal to'. Default is false.

          key: The key to use for the comparison. For example, the name of the cookie to
              evaluate.

          tags: A list of simple strings assigned to the l7 rule

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
    ) -> LoadBalancerL7RuleList:
        """
        List load balancer L7 policy rules

        Args:
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
            cast_to=LoadBalancerL7RuleList,
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
    ) -> LoadBalancerL7Rule:
        """
        Get load balancer L7 rule

        Args:
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
            cast_to=LoadBalancerL7Rule,
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
          compare_type: The comparison type for the L7 rule

          invert: When true the logic of the rule is inverted. For example, with invert true,
              'equal to' would become 'not equal to'. Default is false.

          key: The key to use for the comparison. For example, the name of the cookie to
              evaluate.

          tags: A list of simple strings assigned to the l7 rule

          type: The L7 rule type

          value: The value to use for the comparison. For example, the file type to compare

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

    async def create_and_poll(
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
        polling_interval_seconds: int | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LoadBalancerL7Rule:
        response = await self.create(
            l7policy_id=l7policy_id,
            project_id=project_id,
            region_id=region_id,
            compare_type=compare_type,
            type=type,
            value=value,
            invert=invert,
            key=key,
            tags=tags,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks or len(response.tasks) != 1:
            raise ValueError(f"Expected exactly one task to be created")
        task = await self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
        )
        if not task.created_resources or not task.created_resources.l7rules or len(task.created_resources.l7rules) != 1:
            raise ValueError(f"Expected exactly one resource to be created in a task")
        return await self.get(
            l7rule_id=task.created_resources.l7rules[0],
            project_id=project_id,
            region_id=region_id,
            l7policy_id=l7policy_id,
            extra_headers=extra_headers,
            timeout=timeout,
        )

    async def delete_and_poll(
        self,
        l7rule_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        l7policy_id: str,
        polling_interval_seconds: int | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> None:
        """
        Delete L7 rule and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.delete(
            l7rule_id=l7rule_id,
            project_id=project_id,
            region_id=region_id,
            l7policy_id=l7policy_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks:
            raise ValueError("Expected at least one task to be created")
        await self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
        )

    async def replace_and_poll(
        self,
        l7rule_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        l7policy_id: str,
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
        polling_interval_seconds: int | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LoadBalancerL7Rule:
        """
        Replace L7 rule and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.replace(
            l7rule_id=l7rule_id,
            project_id=project_id,
            region_id=region_id,
            l7policy_id=l7policy_id,
            compare_type=compare_type,
            type=type,
            value=value,
            invert=invert,
            key=key,
            tags=tags,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks:
            raise ValueError("Expected at least one task to be created")
        await self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
        )
        return await self.get(
            l7rule_id=l7rule_id,
            project_id=project_id,
            region_id=region_id,
            l7policy_id=l7policy_id,
            extra_headers=extra_headers,
            timeout=timeout,
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
