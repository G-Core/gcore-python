# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.cloud import LbListenerProtocol
from ...._base_client import make_request_options
from ....types.cloud.lb_listener import LbListener
from ....types.cloud.task_id_list import TaskIDList
from ....types.cloud.load_balancers import (
    listener_get_params,
    listener_list_params,
    listener_create_params,
    listener_update_params,
)
from ....types.cloud.lb_listener_list import LbListenerList
from ....types.cloud.lb_listener_protocol import LbListenerProtocol

__all__ = ["ListenersResource", "AsyncListenersResource"]


class ListenersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ListenersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return ListenersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ListenersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
        """
        return ListenersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        loadbalancer_id: str,
        name: str,
        protocol: LbListenerProtocol,
        protocol_port: int,
        allowed_cidrs: Optional[List[str]] | NotGiven = NOT_GIVEN,
        connection_limit: int | NotGiven = NOT_GIVEN,
        insert_x_forwarded: bool | NotGiven = NOT_GIVEN,
        secret_id: str | NotGiven = NOT_GIVEN,
        sni_secret_id: List[str] | NotGiven = NOT_GIVEN,
        timeout_client_data: Optional[int] | NotGiven = NOT_GIVEN,
        timeout_member_connect: Optional[int] | NotGiven = NOT_GIVEN,
        timeout_member_data: Optional[int] | NotGiven = NOT_GIVEN,
        user_list: Iterable[listener_create_params.UserList] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Create load balancer listener

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Flblisteners%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
              "$.paths['/cloud/v1/lblisteners/{project_id}/{region_id}'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Flblisteners%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
              "$.paths['/cloud/v1/lblisteners/{project_id}/{region_id}'].post.parameters[1].schema"

          loadbalancer_id: '#/components/schemas/CreateLbListenerSerializer/properties/loadbalancer_id'
              "$.components.schemas.CreateLbListenerSerializer.properties.loadbalancer_id"

          name: '#/components/schemas/CreateLbListenerSerializer/properties/name'
              "$.components.schemas.CreateLbListenerSerializer.properties.name"

          protocol: '#/components/schemas/CreateLbListenerSerializer/properties/protocol'
              "$.components.schemas.CreateLbListenerSerializer.properties.protocol"

          protocol_port: '#/components/schemas/CreateLbListenerSerializer/properties/protocol_port'
              "$.components.schemas.CreateLbListenerSerializer.properties.protocol_port"

          allowed_cidrs: '#/components/schemas/CreateLbListenerSerializer/properties/allowed_cidrs/anyOf/0'
              "$.components.schemas.CreateLbListenerSerializer.properties.allowed_cidrs.anyOf[0]"

          connection_limit: '#/components/schemas/CreateLbListenerSerializer/properties/connection_limit'
              "$.components.schemas.CreateLbListenerSerializer.properties.connection_limit"

          insert_x_forwarded: '#/components/schemas/CreateLbListenerSerializer/properties/insert_x_forwarded'
              "$.components.schemas.CreateLbListenerSerializer.properties.insert_x_forwarded"

          secret_id: '#/components/schemas/CreateLbListenerSerializer/properties/secret_id/anyOf/0'
              "$.components.schemas.CreateLbListenerSerializer.properties.secret_id.anyOf[0]"

          sni_secret_id: '#/components/schemas/CreateLbListenerSerializer/properties/sni_secret_id'
              "$.components.schemas.CreateLbListenerSerializer.properties.sni_secret_id"

          timeout_client_data: '#/components/schemas/CreateLbListenerSerializer/properties/timeout_client_data/anyOf/0'
              "$.components.schemas.CreateLbListenerSerializer.properties.timeout_client_data.anyOf[0]"

          timeout_member_connect: '#/components/schemas/CreateLbListenerSerializer/properties/timeout_member_connect/anyOf/0'
              "$.components.schemas.CreateLbListenerSerializer.properties.timeout_member_connect.anyOf[0]"

          timeout_member_data: '#/components/schemas/CreateLbListenerSerializer/properties/timeout_member_data/anyOf/0'
              "$.components.schemas.CreateLbListenerSerializer.properties.timeout_member_data.anyOf[0]"

          user_list: '#/components/schemas/CreateLbListenerSerializer/properties/user_list'
              "$.components.schemas.CreateLbListenerSerializer.properties.user_list"

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
            f"/cloud/v1/lblisteners/{project_id}/{region_id}",
            body=maybe_transform(
                {
                    "loadbalancer_id": loadbalancer_id,
                    "name": name,
                    "protocol": protocol,
                    "protocol_port": protocol_port,
                    "allowed_cidrs": allowed_cidrs,
                    "connection_limit": connection_limit,
                    "insert_x_forwarded": insert_x_forwarded,
                    "secret_id": secret_id,
                    "sni_secret_id": sni_secret_id,
                    "timeout_client_data": timeout_client_data,
                    "timeout_member_connect": timeout_member_connect,
                    "timeout_member_data": timeout_member_data,
                    "user_list": user_list,
                },
                listener_create_params.ListenerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def update(
        self,
        listener_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        allowed_cidrs: Optional[List[str]] | NotGiven = NOT_GIVEN,
        connection_limit: int | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        secret_id: Optional[str] | NotGiven = NOT_GIVEN,
        sni_secret_id: Optional[List[str]] | NotGiven = NOT_GIVEN,
        timeout_client_data: Optional[int] | NotGiven = NOT_GIVEN,
        timeout_member_connect: Optional[int] | NotGiven = NOT_GIVEN,
        timeout_member_data: Optional[int] | NotGiven = NOT_GIVEN,
        user_list: Optional[Iterable[listener_update_params.UserList]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Update listener

        Args:
          project_id: '#/paths/%2Fcloud%2Fv2%2Flblisteners%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Blistener_id%7D/patch/parameters/0/schema'
              "$.paths['/cloud/v2/lblisteners/{project_id}/{region_id}/{listener_id}'].patch.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv2%2Flblisteners%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Blistener_id%7D/patch/parameters/1/schema'
              "$.paths['/cloud/v2/lblisteners/{project_id}/{region_id}/{listener_id}'].patch.parameters[1].schema"

          listener_id: '#/paths/%2Fcloud%2Fv2%2Flblisteners%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Blistener_id%7D/patch/parameters/2/schema'
              "$.paths['/cloud/v2/lblisteners/{project_id}/{region_id}/{listener_id}'].patch.parameters[2].schema"

          allowed_cidrs: '#/components/schemas/PatchLbListenerSerializer/properties/allowed_cidrs/anyOf/0'
              "$.components.schemas.PatchLbListenerSerializer.properties.allowed_cidrs.anyOf[0]"

          connection_limit: '#/components/schemas/PatchLbListenerSerializer/properties/connection_limit'
              "$.components.schemas.PatchLbListenerSerializer.properties.connection_limit"

          name: '#/components/schemas/PatchLbListenerSerializer/properties/name'
              "$.components.schemas.PatchLbListenerSerializer.properties.name"

          secret_id: '#/components/schemas/PatchLbListenerSerializer/properties/secret_id/anyOf/0'
              "$.components.schemas.PatchLbListenerSerializer.properties.secret_id.anyOf[0]"

          sni_secret_id: '#/components/schemas/PatchLbListenerSerializer/properties/sni_secret_id/anyOf/0'
              "$.components.schemas.PatchLbListenerSerializer.properties.sni_secret_id.anyOf[0]"

          timeout_client_data: '#/components/schemas/PatchLbListenerSerializer/properties/timeout_client_data/anyOf/0'
              "$.components.schemas.PatchLbListenerSerializer.properties.timeout_client_data.anyOf[0]"

          timeout_member_connect: '#/components/schemas/PatchLbListenerSerializer/properties/timeout_member_connect/anyOf/0'
              "$.components.schemas.PatchLbListenerSerializer.properties.timeout_member_connect.anyOf[0]"

          timeout_member_data: '#/components/schemas/PatchLbListenerSerializer/properties/timeout_member_data/anyOf/0'
              "$.components.schemas.PatchLbListenerSerializer.properties.timeout_member_data.anyOf[0]"

          user_list: '#/components/schemas/PatchLbListenerSerializer/properties/user_list/anyOf/0'
              "$.components.schemas.PatchLbListenerSerializer.properties.user_list.anyOf[0]"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not listener_id:
            raise ValueError(f"Expected a non-empty value for `listener_id` but received {listener_id!r}")
        return self._patch(
            f"/cloud/v2/lblisteners/{project_id}/{region_id}/{listener_id}",
            body=maybe_transform(
                {
                    "allowed_cidrs": allowed_cidrs,
                    "connection_limit": connection_limit,
                    "name": name,
                    "secret_id": secret_id,
                    "sni_secret_id": sni_secret_id,
                    "timeout_client_data": timeout_client_data,
                    "timeout_member_connect": timeout_member_connect,
                    "timeout_member_data": timeout_member_data,
                    "user_list": user_list,
                },
                listener_update_params.ListenerUpdateParams,
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
        loadbalancer_id: str | NotGiven = NOT_GIVEN,
        show_stats: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LbListenerList:
        """
        List load balancer listeners

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Flblisteners%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/lblisteners/{project_id}/{region_id}'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Flblisteners%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v1/lblisteners/{project_id}/{region_id}'].get.parameters[1].schema"

          loadbalancer_id: '#/paths/%2Fcloud%2Fv1%2Flblisteners%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/2'
              "$.paths['/cloud/v1/lblisteners/{project_id}/{region_id}'].get.parameters[2]"

          show_stats: '#/paths/%2Fcloud%2Fv1%2Flblisteners%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/3'
              "$.paths['/cloud/v1/lblisteners/{project_id}/{region_id}'].get.parameters[3]"

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
            f"/cloud/v1/lblisteners/{project_id}/{region_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "loadbalancer_id": loadbalancer_id,
                        "show_stats": show_stats,
                    },
                    listener_list_params.ListenerListParams,
                ),
            ),
            cast_to=LbListenerList,
        )

    def delete(
        self,
        listener_id: str,
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
        Delete load balancer listener

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Flblisteners%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Blistener_id%7D/delete/parameters/0/schema'
              "$.paths['/cloud/v1/lblisteners/{project_id}/{region_id}/{listener_id}']['delete'].parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Flblisteners%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Blistener_id%7D/delete/parameters/1/schema'
              "$.paths['/cloud/v1/lblisteners/{project_id}/{region_id}/{listener_id}']['delete'].parameters[1].schema"

          listener_id: '#/paths/%2Fcloud%2Fv1%2Flblisteners%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Blistener_id%7D/delete/parameters/2/schema'
              "$.paths['/cloud/v1/lblisteners/{project_id}/{region_id}/{listener_id}']['delete'].parameters[2].schema"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not listener_id:
            raise ValueError(f"Expected a non-empty value for `listener_id` but received {listener_id!r}")
        return self._delete(
            f"/cloud/v1/lblisteners/{project_id}/{region_id}/{listener_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def get(
        self,
        listener_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        show_stats: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LbListener:
        """
        Get listener

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Flblisteners%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Blistener_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/lblisteners/{project_id}/{region_id}/{listener_id}'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Flblisteners%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Blistener_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v1/lblisteners/{project_id}/{region_id}/{listener_id}'].get.parameters[1].schema"

          listener_id: '#/paths/%2Fcloud%2Fv1%2Flblisteners%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Blistener_id%7D/get/parameters/2/schema'
              "$.paths['/cloud/v1/lblisteners/{project_id}/{region_id}/{listener_id}'].get.parameters[2].schema"

          show_stats: '#/paths/%2Fcloud%2Fv1%2Flblisteners%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Blistener_id%7D/get/parameters/3'
              "$.paths['/cloud/v1/lblisteners/{project_id}/{region_id}/{listener_id}'].get.parameters[3]"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not listener_id:
            raise ValueError(f"Expected a non-empty value for `listener_id` but received {listener_id!r}")
        return self._get(
            f"/cloud/v1/lblisteners/{project_id}/{region_id}/{listener_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"show_stats": show_stats}, listener_get_params.ListenerGetParams),
            ),
            cast_to=LbListener,
        )


class AsyncListenersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncListenersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncListenersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncListenersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
        """
        return AsyncListenersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        loadbalancer_id: str,
        name: str,
        protocol: LbListenerProtocol,
        protocol_port: int,
        allowed_cidrs: Optional[List[str]] | NotGiven = NOT_GIVEN,
        connection_limit: int | NotGiven = NOT_GIVEN,
        insert_x_forwarded: bool | NotGiven = NOT_GIVEN,
        secret_id: str | NotGiven = NOT_GIVEN,
        sni_secret_id: List[str] | NotGiven = NOT_GIVEN,
        timeout_client_data: Optional[int] | NotGiven = NOT_GIVEN,
        timeout_member_connect: Optional[int] | NotGiven = NOT_GIVEN,
        timeout_member_data: Optional[int] | NotGiven = NOT_GIVEN,
        user_list: Iterable[listener_create_params.UserList] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Create load balancer listener

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Flblisteners%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
              "$.paths['/cloud/v1/lblisteners/{project_id}/{region_id}'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Flblisteners%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
              "$.paths['/cloud/v1/lblisteners/{project_id}/{region_id}'].post.parameters[1].schema"

          loadbalancer_id: '#/components/schemas/CreateLbListenerSerializer/properties/loadbalancer_id'
              "$.components.schemas.CreateLbListenerSerializer.properties.loadbalancer_id"

          name: '#/components/schemas/CreateLbListenerSerializer/properties/name'
              "$.components.schemas.CreateLbListenerSerializer.properties.name"

          protocol: '#/components/schemas/CreateLbListenerSerializer/properties/protocol'
              "$.components.schemas.CreateLbListenerSerializer.properties.protocol"

          protocol_port: '#/components/schemas/CreateLbListenerSerializer/properties/protocol_port'
              "$.components.schemas.CreateLbListenerSerializer.properties.protocol_port"

          allowed_cidrs: '#/components/schemas/CreateLbListenerSerializer/properties/allowed_cidrs/anyOf/0'
              "$.components.schemas.CreateLbListenerSerializer.properties.allowed_cidrs.anyOf[0]"

          connection_limit: '#/components/schemas/CreateLbListenerSerializer/properties/connection_limit'
              "$.components.schemas.CreateLbListenerSerializer.properties.connection_limit"

          insert_x_forwarded: '#/components/schemas/CreateLbListenerSerializer/properties/insert_x_forwarded'
              "$.components.schemas.CreateLbListenerSerializer.properties.insert_x_forwarded"

          secret_id: '#/components/schemas/CreateLbListenerSerializer/properties/secret_id/anyOf/0'
              "$.components.schemas.CreateLbListenerSerializer.properties.secret_id.anyOf[0]"

          sni_secret_id: '#/components/schemas/CreateLbListenerSerializer/properties/sni_secret_id'
              "$.components.schemas.CreateLbListenerSerializer.properties.sni_secret_id"

          timeout_client_data: '#/components/schemas/CreateLbListenerSerializer/properties/timeout_client_data/anyOf/0'
              "$.components.schemas.CreateLbListenerSerializer.properties.timeout_client_data.anyOf[0]"

          timeout_member_connect: '#/components/schemas/CreateLbListenerSerializer/properties/timeout_member_connect/anyOf/0'
              "$.components.schemas.CreateLbListenerSerializer.properties.timeout_member_connect.anyOf[0]"

          timeout_member_data: '#/components/schemas/CreateLbListenerSerializer/properties/timeout_member_data/anyOf/0'
              "$.components.schemas.CreateLbListenerSerializer.properties.timeout_member_data.anyOf[0]"

          user_list: '#/components/schemas/CreateLbListenerSerializer/properties/user_list'
              "$.components.schemas.CreateLbListenerSerializer.properties.user_list"

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
            f"/cloud/v1/lblisteners/{project_id}/{region_id}",
            body=await async_maybe_transform(
                {
                    "loadbalancer_id": loadbalancer_id,
                    "name": name,
                    "protocol": protocol,
                    "protocol_port": protocol_port,
                    "allowed_cidrs": allowed_cidrs,
                    "connection_limit": connection_limit,
                    "insert_x_forwarded": insert_x_forwarded,
                    "secret_id": secret_id,
                    "sni_secret_id": sni_secret_id,
                    "timeout_client_data": timeout_client_data,
                    "timeout_member_connect": timeout_member_connect,
                    "timeout_member_data": timeout_member_data,
                    "user_list": user_list,
                },
                listener_create_params.ListenerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def update(
        self,
        listener_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        allowed_cidrs: Optional[List[str]] | NotGiven = NOT_GIVEN,
        connection_limit: int | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        secret_id: Optional[str] | NotGiven = NOT_GIVEN,
        sni_secret_id: Optional[List[str]] | NotGiven = NOT_GIVEN,
        timeout_client_data: Optional[int] | NotGiven = NOT_GIVEN,
        timeout_member_connect: Optional[int] | NotGiven = NOT_GIVEN,
        timeout_member_data: Optional[int] | NotGiven = NOT_GIVEN,
        user_list: Optional[Iterable[listener_update_params.UserList]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Update listener

        Args:
          project_id: '#/paths/%2Fcloud%2Fv2%2Flblisteners%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Blistener_id%7D/patch/parameters/0/schema'
              "$.paths['/cloud/v2/lblisteners/{project_id}/{region_id}/{listener_id}'].patch.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv2%2Flblisteners%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Blistener_id%7D/patch/parameters/1/schema'
              "$.paths['/cloud/v2/lblisteners/{project_id}/{region_id}/{listener_id}'].patch.parameters[1].schema"

          listener_id: '#/paths/%2Fcloud%2Fv2%2Flblisteners%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Blistener_id%7D/patch/parameters/2/schema'
              "$.paths['/cloud/v2/lblisteners/{project_id}/{region_id}/{listener_id}'].patch.parameters[2].schema"

          allowed_cidrs: '#/components/schemas/PatchLbListenerSerializer/properties/allowed_cidrs/anyOf/0'
              "$.components.schemas.PatchLbListenerSerializer.properties.allowed_cidrs.anyOf[0]"

          connection_limit: '#/components/schemas/PatchLbListenerSerializer/properties/connection_limit'
              "$.components.schemas.PatchLbListenerSerializer.properties.connection_limit"

          name: '#/components/schemas/PatchLbListenerSerializer/properties/name'
              "$.components.schemas.PatchLbListenerSerializer.properties.name"

          secret_id: '#/components/schemas/PatchLbListenerSerializer/properties/secret_id/anyOf/0'
              "$.components.schemas.PatchLbListenerSerializer.properties.secret_id.anyOf[0]"

          sni_secret_id: '#/components/schemas/PatchLbListenerSerializer/properties/sni_secret_id/anyOf/0'
              "$.components.schemas.PatchLbListenerSerializer.properties.sni_secret_id.anyOf[0]"

          timeout_client_data: '#/components/schemas/PatchLbListenerSerializer/properties/timeout_client_data/anyOf/0'
              "$.components.schemas.PatchLbListenerSerializer.properties.timeout_client_data.anyOf[0]"

          timeout_member_connect: '#/components/schemas/PatchLbListenerSerializer/properties/timeout_member_connect/anyOf/0'
              "$.components.schemas.PatchLbListenerSerializer.properties.timeout_member_connect.anyOf[0]"

          timeout_member_data: '#/components/schemas/PatchLbListenerSerializer/properties/timeout_member_data/anyOf/0'
              "$.components.schemas.PatchLbListenerSerializer.properties.timeout_member_data.anyOf[0]"

          user_list: '#/components/schemas/PatchLbListenerSerializer/properties/user_list/anyOf/0'
              "$.components.schemas.PatchLbListenerSerializer.properties.user_list.anyOf[0]"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not listener_id:
            raise ValueError(f"Expected a non-empty value for `listener_id` but received {listener_id!r}")
        return await self._patch(
            f"/cloud/v2/lblisteners/{project_id}/{region_id}/{listener_id}",
            body=await async_maybe_transform(
                {
                    "allowed_cidrs": allowed_cidrs,
                    "connection_limit": connection_limit,
                    "name": name,
                    "secret_id": secret_id,
                    "sni_secret_id": sni_secret_id,
                    "timeout_client_data": timeout_client_data,
                    "timeout_member_connect": timeout_member_connect,
                    "timeout_member_data": timeout_member_data,
                    "user_list": user_list,
                },
                listener_update_params.ListenerUpdateParams,
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
        loadbalancer_id: str | NotGiven = NOT_GIVEN,
        show_stats: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LbListenerList:
        """
        List load balancer listeners

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Flblisteners%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/lblisteners/{project_id}/{region_id}'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Flblisteners%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v1/lblisteners/{project_id}/{region_id}'].get.parameters[1].schema"

          loadbalancer_id: '#/paths/%2Fcloud%2Fv1%2Flblisteners%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/2'
              "$.paths['/cloud/v1/lblisteners/{project_id}/{region_id}'].get.parameters[2]"

          show_stats: '#/paths/%2Fcloud%2Fv1%2Flblisteners%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/3'
              "$.paths['/cloud/v1/lblisteners/{project_id}/{region_id}'].get.parameters[3]"

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
            f"/cloud/v1/lblisteners/{project_id}/{region_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "loadbalancer_id": loadbalancer_id,
                        "show_stats": show_stats,
                    },
                    listener_list_params.ListenerListParams,
                ),
            ),
            cast_to=LbListenerList,
        )

    async def delete(
        self,
        listener_id: str,
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
        Delete load balancer listener

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Flblisteners%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Blistener_id%7D/delete/parameters/0/schema'
              "$.paths['/cloud/v1/lblisteners/{project_id}/{region_id}/{listener_id}']['delete'].parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Flblisteners%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Blistener_id%7D/delete/parameters/1/schema'
              "$.paths['/cloud/v1/lblisteners/{project_id}/{region_id}/{listener_id}']['delete'].parameters[1].schema"

          listener_id: '#/paths/%2Fcloud%2Fv1%2Flblisteners%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Blistener_id%7D/delete/parameters/2/schema'
              "$.paths['/cloud/v1/lblisteners/{project_id}/{region_id}/{listener_id}']['delete'].parameters[2].schema"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not listener_id:
            raise ValueError(f"Expected a non-empty value for `listener_id` but received {listener_id!r}")
        return await self._delete(
            f"/cloud/v1/lblisteners/{project_id}/{region_id}/{listener_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def get(
        self,
        listener_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        show_stats: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LbListener:
        """
        Get listener

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Flblisteners%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Blistener_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/lblisteners/{project_id}/{region_id}/{listener_id}'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Flblisteners%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Blistener_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v1/lblisteners/{project_id}/{region_id}/{listener_id}'].get.parameters[1].schema"

          listener_id: '#/paths/%2Fcloud%2Fv1%2Flblisteners%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Blistener_id%7D/get/parameters/2/schema'
              "$.paths['/cloud/v1/lblisteners/{project_id}/{region_id}/{listener_id}'].get.parameters[2].schema"

          show_stats: '#/paths/%2Fcloud%2Fv1%2Flblisteners%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Blistener_id%7D/get/parameters/3'
              "$.paths['/cloud/v1/lblisteners/{project_id}/{region_id}/{listener_id}'].get.parameters[3]"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not listener_id:
            raise ValueError(f"Expected a non-empty value for `listener_id` but received {listener_id!r}")
        return await self._get(
            f"/cloud/v1/lblisteners/{project_id}/{region_id}/{listener_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"show_stats": show_stats}, listener_get_params.ListenerGetParams),
            ),
            cast_to=LbListener,
        )


class ListenersResourceWithRawResponse:
    def __init__(self, listeners: ListenersResource) -> None:
        self._listeners = listeners

        self.create = to_raw_response_wrapper(
            listeners.create,
        )
        self.update = to_raw_response_wrapper(
            listeners.update,
        )
        self.list = to_raw_response_wrapper(
            listeners.list,
        )
        self.delete = to_raw_response_wrapper(
            listeners.delete,
        )
        self.get = to_raw_response_wrapper(
            listeners.get,
        )


class AsyncListenersResourceWithRawResponse:
    def __init__(self, listeners: AsyncListenersResource) -> None:
        self._listeners = listeners

        self.create = async_to_raw_response_wrapper(
            listeners.create,
        )
        self.update = async_to_raw_response_wrapper(
            listeners.update,
        )
        self.list = async_to_raw_response_wrapper(
            listeners.list,
        )
        self.delete = async_to_raw_response_wrapper(
            listeners.delete,
        )
        self.get = async_to_raw_response_wrapper(
            listeners.get,
        )


class ListenersResourceWithStreamingResponse:
    def __init__(self, listeners: ListenersResource) -> None:
        self._listeners = listeners

        self.create = to_streamed_response_wrapper(
            listeners.create,
        )
        self.update = to_streamed_response_wrapper(
            listeners.update,
        )
        self.list = to_streamed_response_wrapper(
            listeners.list,
        )
        self.delete = to_streamed_response_wrapper(
            listeners.delete,
        )
        self.get = to_streamed_response_wrapper(
            listeners.get,
        )


class AsyncListenersResourceWithStreamingResponse:
    def __init__(self, listeners: AsyncListenersResource) -> None:
        self._listeners = listeners

        self.create = async_to_streamed_response_wrapper(
            listeners.create,
        )
        self.update = async_to_streamed_response_wrapper(
            listeners.update,
        )
        self.list = async_to_streamed_response_wrapper(
            listeners.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            listeners.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            listeners.get,
        )
