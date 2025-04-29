# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from .rules import (
    RulesResource,
    AsyncRulesResource,
    RulesResourceWithRawResponse,
    AsyncRulesResourceWithRawResponse,
    RulesResourceWithStreamingResponse,
    AsyncRulesResourceWithStreamingResponse,
)
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
from .....types.cloud.l7_policy import L7Policy
from .....types.cloud.task_id_list import TaskIDList
from .....types.cloud.l7_policy_list import L7PolicyList
from .....types.cloud.load_balancers import l7_policy_create_params, l7_policy_replace_params

__all__ = ["L7PoliciesResource", "AsyncL7PoliciesResource"]


class L7PoliciesResource(SyncAPIResource):
    @cached_property
    def rules(self) -> RulesResource:
        return RulesResource(self._client)

    @cached_property
    def with_raw_response(self) -> L7PoliciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return L7PoliciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> L7PoliciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
        """
        return L7PoliciesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["REDIRECT_PREFIX", "REDIRECT_TO_POOL", "REDIRECT_TO_URL", "REJECT"],
        listener_id: str,
        name: str | NotGiven = NOT_GIVEN,
        position: int | NotGiven = NOT_GIVEN,
        redirect_http_code: int | NotGiven = NOT_GIVEN,
        redirect_pool_id: str | NotGiven = NOT_GIVEN,
        redirect_prefix: str | NotGiven = NOT_GIVEN,
        redirect_url: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Create load balancer L7 policy

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}'].post.parameters[1].schema"

          action: '#/components/schemas/CreateL7PolicySchema/properties/action'
              "$.components.schemas.CreateL7PolicySchema.properties.action"

          listener_id: '#/components/schemas/CreateL7PolicySchema/properties/listener_id'
              "$.components.schemas.CreateL7PolicySchema.properties.listener_id"

          name: '#/components/schemas/CreateL7PolicySchema/properties/name'
              "$.components.schemas.CreateL7PolicySchema.properties.name"

          position: '#/components/schemas/CreateL7PolicySchema/properties/position'
              "$.components.schemas.CreateL7PolicySchema.properties.position"

          redirect_http_code: '#/components/schemas/CreateL7PolicySchema/properties/redirect_http_code'
              "$.components.schemas.CreateL7PolicySchema.properties.redirect_http_code"

          redirect_pool_id: '#/components/schemas/CreateL7PolicySchema/properties/redirect_pool_id'
              "$.components.schemas.CreateL7PolicySchema.properties.redirect_pool_id"

          redirect_prefix: '#/components/schemas/CreateL7PolicySchema/properties/redirect_prefix'
              "$.components.schemas.CreateL7PolicySchema.properties.redirect_prefix"

          redirect_url: '#/components/schemas/CreateL7PolicySchema/properties/redirect_url'
              "$.components.schemas.CreateL7PolicySchema.properties.redirect_url"

          tags: '#/components/schemas/CreateL7PolicySchema/properties/tags'
              "$.components.schemas.CreateL7PolicySchema.properties.tags"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return self._post(
            f"/cloud/v1/l7policies/{project_id}/{region_id}",
            body=maybe_transform(
                {
                    "action": action,
                    "listener_id": listener_id,
                    "name": name,
                    "position": position,
                    "redirect_http_code": redirect_http_code,
                    "redirect_pool_id": redirect_pool_id,
                    "redirect_prefix": redirect_prefix,
                    "redirect_url": redirect_url,
                    "tags": tags,
                },
                l7_policy_create_params.L7PolicyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def list(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> L7PolicyList:
        """
        List load balancer L7 policies

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}'].get.parameters[1].schema"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return self._get(
            f"/cloud/v1/l7policies/{project_id}/{region_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=L7PolicyList,
        )

    def delete(
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
    ) -> TaskIDList:
        """
        Delete load balancer L7 policy

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D/delete/parameters/0/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}']['delete'].parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D/delete/parameters/1/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}']['delete'].parameters[1].schema"

          l7policy_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D/delete/parameters/2/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}']['delete'].parameters[2].schema"

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
        return self._delete(
            f"/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def get(
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
    ) -> L7Policy:
        """
        Get load balancer L7 policy

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}'].get.parameters[1].schema"

          l7policy_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D/get/parameters/2/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}'].get.parameters[2].schema"

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
            f"/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=L7Policy,
        )

    def replace(
        self,
        l7policy_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["REDIRECT_PREFIX", "REDIRECT_TO_POOL", "REDIRECT_TO_URL", "REJECT"],
        name: str | NotGiven = NOT_GIVEN,
        position: int | NotGiven = NOT_GIVEN,
        redirect_http_code: int | NotGiven = NOT_GIVEN,
        redirect_pool_id: str | NotGiven = NOT_GIVEN,
        redirect_prefix: str | NotGiven = NOT_GIVEN,
        redirect_url: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Replace load balancer L7 policy properties

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D/put/parameters/0/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}'].put.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D/put/parameters/1/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}'].put.parameters[1].schema"

          l7policy_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D/put/parameters/2/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}'].put.parameters[2].schema"

          action: '#/components/schemas/UpdateL7PolicySchema/properties/action'
              "$.components.schemas.UpdateL7PolicySchema.properties.action"

          name: '#/components/schemas/UpdateL7PolicySchema/properties/name'
              "$.components.schemas.UpdateL7PolicySchema.properties.name"

          position: '#/components/schemas/UpdateL7PolicySchema/properties/position'
              "$.components.schemas.UpdateL7PolicySchema.properties.position"

          redirect_http_code: '#/components/schemas/UpdateL7PolicySchema/properties/redirect_http_code'
              "$.components.schemas.UpdateL7PolicySchema.properties.redirect_http_code"

          redirect_pool_id: '#/components/schemas/UpdateL7PolicySchema/properties/redirect_pool_id'
              "$.components.schemas.UpdateL7PolicySchema.properties.redirect_pool_id"

          redirect_prefix: '#/components/schemas/UpdateL7PolicySchema/properties/redirect_prefix'
              "$.components.schemas.UpdateL7PolicySchema.properties.redirect_prefix"

          redirect_url: '#/components/schemas/UpdateL7PolicySchema/properties/redirect_url'
              "$.components.schemas.UpdateL7PolicySchema.properties.redirect_url"

          tags: '#/components/schemas/UpdateL7PolicySchema/properties/tags'
              "$.components.schemas.UpdateL7PolicySchema.properties.tags"

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
        return self._put(
            f"/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}",
            body=maybe_transform(
                {
                    "action": action,
                    "name": name,
                    "position": position,
                    "redirect_http_code": redirect_http_code,
                    "redirect_pool_id": redirect_pool_id,
                    "redirect_prefix": redirect_prefix,
                    "redirect_url": redirect_url,
                    "tags": tags,
                },
                l7_policy_replace_params.L7PolicyReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )


class AsyncL7PoliciesResource(AsyncAPIResource):
    @cached_property
    def rules(self) -> AsyncRulesResource:
        return AsyncRulesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncL7PoliciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncL7PoliciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncL7PoliciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
        """
        return AsyncL7PoliciesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["REDIRECT_PREFIX", "REDIRECT_TO_POOL", "REDIRECT_TO_URL", "REJECT"],
        listener_id: str,
        name: str | NotGiven = NOT_GIVEN,
        position: int | NotGiven = NOT_GIVEN,
        redirect_http_code: int | NotGiven = NOT_GIVEN,
        redirect_pool_id: str | NotGiven = NOT_GIVEN,
        redirect_prefix: str | NotGiven = NOT_GIVEN,
        redirect_url: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Create load balancer L7 policy

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}'].post.parameters[1].schema"

          action: '#/components/schemas/CreateL7PolicySchema/properties/action'
              "$.components.schemas.CreateL7PolicySchema.properties.action"

          listener_id: '#/components/schemas/CreateL7PolicySchema/properties/listener_id'
              "$.components.schemas.CreateL7PolicySchema.properties.listener_id"

          name: '#/components/schemas/CreateL7PolicySchema/properties/name'
              "$.components.schemas.CreateL7PolicySchema.properties.name"

          position: '#/components/schemas/CreateL7PolicySchema/properties/position'
              "$.components.schemas.CreateL7PolicySchema.properties.position"

          redirect_http_code: '#/components/schemas/CreateL7PolicySchema/properties/redirect_http_code'
              "$.components.schemas.CreateL7PolicySchema.properties.redirect_http_code"

          redirect_pool_id: '#/components/schemas/CreateL7PolicySchema/properties/redirect_pool_id'
              "$.components.schemas.CreateL7PolicySchema.properties.redirect_pool_id"

          redirect_prefix: '#/components/schemas/CreateL7PolicySchema/properties/redirect_prefix'
              "$.components.schemas.CreateL7PolicySchema.properties.redirect_prefix"

          redirect_url: '#/components/schemas/CreateL7PolicySchema/properties/redirect_url'
              "$.components.schemas.CreateL7PolicySchema.properties.redirect_url"

          tags: '#/components/schemas/CreateL7PolicySchema/properties/tags'
              "$.components.schemas.CreateL7PolicySchema.properties.tags"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return await self._post(
            f"/cloud/v1/l7policies/{project_id}/{region_id}",
            body=await async_maybe_transform(
                {
                    "action": action,
                    "listener_id": listener_id,
                    "name": name,
                    "position": position,
                    "redirect_http_code": redirect_http_code,
                    "redirect_pool_id": redirect_pool_id,
                    "redirect_prefix": redirect_prefix,
                    "redirect_url": redirect_url,
                    "tags": tags,
                },
                l7_policy_create_params.L7PolicyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def list(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> L7PolicyList:
        """
        List load balancer L7 policies

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}'].get.parameters[1].schema"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return await self._get(
            f"/cloud/v1/l7policies/{project_id}/{region_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=L7PolicyList,
        )

    async def delete(
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
    ) -> TaskIDList:
        """
        Delete load balancer L7 policy

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D/delete/parameters/0/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}']['delete'].parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D/delete/parameters/1/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}']['delete'].parameters[1].schema"

          l7policy_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D/delete/parameters/2/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}']['delete'].parameters[2].schema"

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
        return await self._delete(
            f"/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def get(
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
    ) -> L7Policy:
        """
        Get load balancer L7 policy

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}'].get.parameters[1].schema"

          l7policy_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D/get/parameters/2/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}'].get.parameters[2].schema"

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
            f"/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=L7Policy,
        )

    async def replace(
        self,
        l7policy_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["REDIRECT_PREFIX", "REDIRECT_TO_POOL", "REDIRECT_TO_URL", "REJECT"],
        name: str | NotGiven = NOT_GIVEN,
        position: int | NotGiven = NOT_GIVEN,
        redirect_http_code: int | NotGiven = NOT_GIVEN,
        redirect_pool_id: str | NotGiven = NOT_GIVEN,
        redirect_prefix: str | NotGiven = NOT_GIVEN,
        redirect_url: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Replace load balancer L7 policy properties

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D/put/parameters/0/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}'].put.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D/put/parameters/1/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}'].put.parameters[1].schema"

          l7policy_id: '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D/put/parameters/2/schema'
              "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}'].put.parameters[2].schema"

          action: '#/components/schemas/UpdateL7PolicySchema/properties/action'
              "$.components.schemas.UpdateL7PolicySchema.properties.action"

          name: '#/components/schemas/UpdateL7PolicySchema/properties/name'
              "$.components.schemas.UpdateL7PolicySchema.properties.name"

          position: '#/components/schemas/UpdateL7PolicySchema/properties/position'
              "$.components.schemas.UpdateL7PolicySchema.properties.position"

          redirect_http_code: '#/components/schemas/UpdateL7PolicySchema/properties/redirect_http_code'
              "$.components.schemas.UpdateL7PolicySchema.properties.redirect_http_code"

          redirect_pool_id: '#/components/schemas/UpdateL7PolicySchema/properties/redirect_pool_id'
              "$.components.schemas.UpdateL7PolicySchema.properties.redirect_pool_id"

          redirect_prefix: '#/components/schemas/UpdateL7PolicySchema/properties/redirect_prefix'
              "$.components.schemas.UpdateL7PolicySchema.properties.redirect_prefix"

          redirect_url: '#/components/schemas/UpdateL7PolicySchema/properties/redirect_url'
              "$.components.schemas.UpdateL7PolicySchema.properties.redirect_url"

          tags: '#/components/schemas/UpdateL7PolicySchema/properties/tags'
              "$.components.schemas.UpdateL7PolicySchema.properties.tags"

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
        return await self._put(
            f"/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}",
            body=await async_maybe_transform(
                {
                    "action": action,
                    "name": name,
                    "position": position,
                    "redirect_http_code": redirect_http_code,
                    "redirect_pool_id": redirect_pool_id,
                    "redirect_prefix": redirect_prefix,
                    "redirect_url": redirect_url,
                    "tags": tags,
                },
                l7_policy_replace_params.L7PolicyReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )


class L7PoliciesResourceWithRawResponse:
    def __init__(self, l7_policies: L7PoliciesResource) -> None:
        self._l7_policies = l7_policies

        self.create = to_raw_response_wrapper(
            l7_policies.create,
        )
        self.list = to_raw_response_wrapper(
            l7_policies.list,
        )
        self.delete = to_raw_response_wrapper(
            l7_policies.delete,
        )
        self.get = to_raw_response_wrapper(
            l7_policies.get,
        )
        self.replace = to_raw_response_wrapper(
            l7_policies.replace,
        )

    @cached_property
    def rules(self) -> RulesResourceWithRawResponse:
        return RulesResourceWithRawResponse(self._l7_policies.rules)


class AsyncL7PoliciesResourceWithRawResponse:
    def __init__(self, l7_policies: AsyncL7PoliciesResource) -> None:
        self._l7_policies = l7_policies

        self.create = async_to_raw_response_wrapper(
            l7_policies.create,
        )
        self.list = async_to_raw_response_wrapper(
            l7_policies.list,
        )
        self.delete = async_to_raw_response_wrapper(
            l7_policies.delete,
        )
        self.get = async_to_raw_response_wrapper(
            l7_policies.get,
        )
        self.replace = async_to_raw_response_wrapper(
            l7_policies.replace,
        )

    @cached_property
    def rules(self) -> AsyncRulesResourceWithRawResponse:
        return AsyncRulesResourceWithRawResponse(self._l7_policies.rules)


class L7PoliciesResourceWithStreamingResponse:
    def __init__(self, l7_policies: L7PoliciesResource) -> None:
        self._l7_policies = l7_policies

        self.create = to_streamed_response_wrapper(
            l7_policies.create,
        )
        self.list = to_streamed_response_wrapper(
            l7_policies.list,
        )
        self.delete = to_streamed_response_wrapper(
            l7_policies.delete,
        )
        self.get = to_streamed_response_wrapper(
            l7_policies.get,
        )
        self.replace = to_streamed_response_wrapper(
            l7_policies.replace,
        )

    @cached_property
    def rules(self) -> RulesResourceWithStreamingResponse:
        return RulesResourceWithStreamingResponse(self._l7_policies.rules)


class AsyncL7PoliciesResourceWithStreamingResponse:
    def __init__(self, l7_policies: AsyncL7PoliciesResource) -> None:
        self._l7_policies = l7_policies

        self.create = async_to_streamed_response_wrapper(
            l7_policies.create,
        )
        self.list = async_to_streamed_response_wrapper(
            l7_policies.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            l7_policies.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            l7_policies.get,
        )
        self.replace = async_to_streamed_response_wrapper(
            l7_policies.replace,
        )

    @cached_property
    def rules(self) -> AsyncRulesResourceWithStreamingResponse:
        return AsyncRulesResourceWithStreamingResponse(self._l7_policies.rules)
