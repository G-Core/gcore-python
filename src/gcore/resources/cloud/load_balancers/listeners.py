# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ...._types import NOT_GIVEN, Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ....types.cloud.task_id_list import TaskIDList
from ....types.cloud.load_balancers import (
    listener_get_params,
    listener_list_params,
    listener_create_params,
    listener_delete_params,
    listener_update_params,
)
from ....types.cloud.lb_listener_protocol import LbListenerProtocol
from ....types.cloud.load_balancer_listener_list import LoadBalancerListenerList
from ....types.cloud.load_balancer_listener_detail import LoadBalancerListenerDetail

__all__ = ["ListenersResource", "AsyncListenersResource"]


class ListenersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ListenersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return ListenersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ListenersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return ListenersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        load_balancer_id: str,
        name: str,
        protocol: LbListenerProtocol,
        protocol_port: int,
        allowed_cidrs: Optional[SequenceNotStr[str]] | Omit = omit,
        connection_limit: int | Omit = omit,
        default_pool_id: str | Omit = omit,
        insert_x_forwarded: bool | Omit = omit,
        secret_id: str | Omit = omit,
        sni_secret_id: SequenceNotStr[str] | Omit = omit,
        timeout_client_data: Optional[int] | Omit = omit,
        timeout_member_connect: Optional[int] | Omit = omit,
        timeout_member_data: Optional[int] | Omit = omit,
        user_list: Iterable[listener_create_params.UserList] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Create load balancer listener

        Args:
          project_id: Project ID

          region_id: Region ID

          load_balancer_id: ID of already existent Load Balancer.

          name: Load balancer listener name

          protocol: Load balancer listener protocol

          protocol_port: Protocol port

          allowed_cidrs: Network CIDRs from which service will be accessible

          connection_limit: Limit of the simultaneous connections. If -1 is provided, it is translated to
              the default value 100000.

          default_pool_id: ID of already existent Load Balancer Pool to attach listener to.

          insert_x_forwarded: Add headers X-Forwarded-For, X-Forwarded-Port, X-Forwarded-Proto to requests.
              Only used with HTTP or `TERMINATED_HTTPS` protocols.

          secret_id: ID of the secret where PKCS12 file is stored for `TERMINATED_HTTPS` or
              PROMETHEUS listener

          sni_secret_id: List of secrets IDs containing PKCS12 format certificate/key bundles for
              `TERMINATED_HTTPS` or PROMETHEUS listeners

          timeout_client_data: Frontend client inactivity timeout in milliseconds

          timeout_member_connect: Backend member connection timeout in milliseconds

          timeout_member_data: Backend member inactivity timeout in milliseconds

          user_list: Load balancer listener list of username and encrypted password items

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
                    "load_balancer_id": load_balancer_id,
                    "name": name,
                    "protocol": protocol,
                    "protocol_port": protocol_port,
                    "allowed_cidrs": allowed_cidrs,
                    "connection_limit": connection_limit,
                    "default_pool_id": default_pool_id,
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
        allowed_cidrs: Optional[SequenceNotStr[str]] | Omit = omit,
        connection_limit: int | Omit = omit,
        name: str | Omit = omit,
        secret_id: Optional[str] | Omit = omit,
        sni_secret_id: Optional[SequenceNotStr[str]] | Omit = omit,
        timeout_client_data: Optional[int] | Omit = omit,
        timeout_member_connect: Optional[int] | Omit = omit,
        timeout_member_data: Optional[int] | Omit = omit,
        user_list: Optional[Iterable[listener_update_params.UserList]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Update load balancer listener

        Args:
          project_id: Project ID

          region_id: Region ID

          listener_id: Listener ID

          allowed_cidrs: Network CIDRs from which service will be accessible

          connection_limit: Limit of simultaneous connections. If -1 is provided, it is translated to the
              default value 100000.

          name: Load balancer listener name

          secret_id: ID of the secret where PKCS12 file is stored for `TERMINATED_HTTPS` or
              PROMETHEUS load balancer

          sni_secret_id: List of secret's ID containing PKCS12 format certificate/key bundfles for
              `TERMINATED_HTTPS` or PROMETHEUS listeners

          timeout_client_data: Frontend client inactivity timeout in milliseconds

          timeout_member_connect: Backend member connection timeout in milliseconds

          timeout_member_data: Backend member inactivity timeout in milliseconds

          user_list: Load balancer listener users list

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
        load_balancer_id: str | Omit = omit,
        show_stats: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoadBalancerListenerList:
        """
        List load balancer listeners

        Args:
          project_id: Project ID

          region_id: Region ID

          load_balancer_id: Load Balancer ID

          show_stats: Show stats

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
                        "load_balancer_id": load_balancer_id,
                        "show_stats": show_stats,
                    },
                    listener_list_params.ListenerListParams,
                ),
            ),
            cast_to=LoadBalancerListenerList,
        )

    def delete(
        self,
        listener_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        delete_default_pool: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Delete load balancer listener

        Args:
          project_id: Project ID

          region_id: Region ID

          listener_id: Listener ID

          delete_default_pool: Delete default pool attached directly to the listener.

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
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"delete_default_pool": delete_default_pool}, listener_delete_params.ListenerDeleteParams
                ),
            ),
            cast_to=TaskIDList,
        )

    def get(
        self,
        listener_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        show_stats: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoadBalancerListenerDetail:
        """
        Get load balancer listener

        Args:
          project_id: Project ID

          region_id: Region ID

          listener_id: Listener ID

          show_stats: Show stats

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
            cast_to=LoadBalancerListenerDetail,
        )

    def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        load_balancer_id: str,
        name: str,
        protocol: LbListenerProtocol,
        protocol_port: int,
        allowed_cidrs: Optional[SequenceNotStr[str]] | Omit = omit,
        connection_limit: int | Omit = omit,
        insert_x_forwarded: bool | Omit = omit,
        secret_id: str | Omit = omit,
        sni_secret_id: SequenceNotStr[str] | Omit = omit,
        timeout_client_data: Optional[int] | Omit = omit,
        timeout_member_connect: Optional[int] | Omit = omit,
        timeout_member_data: Optional[int] | Omit = omit,
        user_list: Iterable[listener_create_params.UserList] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LoadBalancerListenerDetail:
        response = self.create(
            project_id=project_id,
            region_id=region_id,
            load_balancer_id=load_balancer_id,
            name=name,
            protocol=protocol,
            protocol_port=protocol_port,
            allowed_cidrs=allowed_cidrs,
            connection_limit=connection_limit,
            insert_x_forwarded=insert_x_forwarded,
            secret_id=secret_id,
            sni_secret_id=sni_secret_id,
            timeout_client_data=timeout_client_data,
            timeout_member_connect=timeout_member_connect,
            timeout_member_data=timeout_member_data,
            user_list=user_list,
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
            polling_timeout_seconds=polling_timeout_seconds,
        )
        if (
            not task.created_resources
            or not task.created_resources.listeners
            or len(task.created_resources.listeners) != 1
        ):
            raise ValueError(f"Expected exactly one resource to be created in a task")
        return self.get(
            listener_id=task.created_resources.listeners[0],
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
            timeout=timeout,
        )

    def delete_and_poll(
        self,
        listener_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> None:
        """
        Delete listener and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.delete(
            listener_id=listener_id,
            project_id=project_id,
            region_id=region_id,
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
            polling_timeout_seconds=polling_timeout_seconds,
        )

    def update_and_poll(
        self,
        listener_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        allowed_cidrs: Optional[SequenceNotStr[str]] | Omit = omit,
        connection_limit: int | Omit = omit,
        name: str | Omit = omit,
        secret_id: Optional[str] | Omit = omit,
        sni_secret_id: Optional[SequenceNotStr[str]] | Omit = omit,
        timeout_client_data: Optional[int] | Omit = omit,
        timeout_member_connect: Optional[int] | Omit = omit,
        timeout_member_data: Optional[int] | Omit = omit,
        user_list: Optional[Iterable[listener_update_params.UserList]] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LoadBalancerListenerDetail:
        """
        Update listener and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.update(
            listener_id=listener_id,
            project_id=project_id,
            region_id=region_id,
            allowed_cidrs=allowed_cidrs,
            connection_limit=connection_limit,
            name=name,
            secret_id=secret_id,
            sni_secret_id=sni_secret_id,
            timeout_client_data=timeout_client_data,
            timeout_member_connect=timeout_member_connect,
            timeout_member_data=timeout_member_data,
            user_list=user_list,
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
            polling_timeout_seconds=polling_timeout_seconds,
        )
        return self.get(
            listener_id=listener_id,
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
            timeout=timeout,
        )


class AsyncListenersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncListenersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncListenersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncListenersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncListenersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        load_balancer_id: str,
        name: str,
        protocol: LbListenerProtocol,
        protocol_port: int,
        allowed_cidrs: Optional[SequenceNotStr[str]] | Omit = omit,
        connection_limit: int | Omit = omit,
        default_pool_id: str | Omit = omit,
        insert_x_forwarded: bool | Omit = omit,
        secret_id: str | Omit = omit,
        sni_secret_id: SequenceNotStr[str] | Omit = omit,
        timeout_client_data: Optional[int] | Omit = omit,
        timeout_member_connect: Optional[int] | Omit = omit,
        timeout_member_data: Optional[int] | Omit = omit,
        user_list: Iterable[listener_create_params.UserList] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Create load balancer listener

        Args:
          project_id: Project ID

          region_id: Region ID

          load_balancer_id: ID of already existent Load Balancer.

          name: Load balancer listener name

          protocol: Load balancer listener protocol

          protocol_port: Protocol port

          allowed_cidrs: Network CIDRs from which service will be accessible

          connection_limit: Limit of the simultaneous connections. If -1 is provided, it is translated to
              the default value 100000.

          default_pool_id: ID of already existent Load Balancer Pool to attach listener to.

          insert_x_forwarded: Add headers X-Forwarded-For, X-Forwarded-Port, X-Forwarded-Proto to requests.
              Only used with HTTP or `TERMINATED_HTTPS` protocols.

          secret_id: ID of the secret where PKCS12 file is stored for `TERMINATED_HTTPS` or
              PROMETHEUS listener

          sni_secret_id: List of secrets IDs containing PKCS12 format certificate/key bundles for
              `TERMINATED_HTTPS` or PROMETHEUS listeners

          timeout_client_data: Frontend client inactivity timeout in milliseconds

          timeout_member_connect: Backend member connection timeout in milliseconds

          timeout_member_data: Backend member inactivity timeout in milliseconds

          user_list: Load balancer listener list of username and encrypted password items

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
                    "load_balancer_id": load_balancer_id,
                    "name": name,
                    "protocol": protocol,
                    "protocol_port": protocol_port,
                    "allowed_cidrs": allowed_cidrs,
                    "connection_limit": connection_limit,
                    "default_pool_id": default_pool_id,
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
        allowed_cidrs: Optional[SequenceNotStr[str]] | Omit = omit,
        connection_limit: int | Omit = omit,
        name: str | Omit = omit,
        secret_id: Optional[str] | Omit = omit,
        sni_secret_id: Optional[SequenceNotStr[str]] | Omit = omit,
        timeout_client_data: Optional[int] | Omit = omit,
        timeout_member_connect: Optional[int] | Omit = omit,
        timeout_member_data: Optional[int] | Omit = omit,
        user_list: Optional[Iterable[listener_update_params.UserList]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Update load balancer listener

        Args:
          project_id: Project ID

          region_id: Region ID

          listener_id: Listener ID

          allowed_cidrs: Network CIDRs from which service will be accessible

          connection_limit: Limit of simultaneous connections. If -1 is provided, it is translated to the
              default value 100000.

          name: Load balancer listener name

          secret_id: ID of the secret where PKCS12 file is stored for `TERMINATED_HTTPS` or
              PROMETHEUS load balancer

          sni_secret_id: List of secret's ID containing PKCS12 format certificate/key bundfles for
              `TERMINATED_HTTPS` or PROMETHEUS listeners

          timeout_client_data: Frontend client inactivity timeout in milliseconds

          timeout_member_connect: Backend member connection timeout in milliseconds

          timeout_member_data: Backend member inactivity timeout in milliseconds

          user_list: Load balancer listener users list

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
        load_balancer_id: str | Omit = omit,
        show_stats: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoadBalancerListenerList:
        """
        List load balancer listeners

        Args:
          project_id: Project ID

          region_id: Region ID

          load_balancer_id: Load Balancer ID

          show_stats: Show stats

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
                        "load_balancer_id": load_balancer_id,
                        "show_stats": show_stats,
                    },
                    listener_list_params.ListenerListParams,
                ),
            ),
            cast_to=LoadBalancerListenerList,
        )

    async def delete(
        self,
        listener_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        delete_default_pool: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Delete load balancer listener

        Args:
          project_id: Project ID

          region_id: Region ID

          listener_id: Listener ID

          delete_default_pool: Delete default pool attached directly to the listener.

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
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"delete_default_pool": delete_default_pool}, listener_delete_params.ListenerDeleteParams
                ),
            ),
            cast_to=TaskIDList,
        )

    async def get(
        self,
        listener_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        show_stats: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoadBalancerListenerDetail:
        """
        Get load balancer listener

        Args:
          project_id: Project ID

          region_id: Region ID

          listener_id: Listener ID

          show_stats: Show stats

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
            cast_to=LoadBalancerListenerDetail,
        )

    async def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        load_balancer_id: str,
        name: str,
        protocol: LbListenerProtocol,
        protocol_port: int,
        allowed_cidrs: Optional[SequenceNotStr[str]] | Omit = omit,
        connection_limit: int | Omit = omit,
        insert_x_forwarded: bool | Omit = omit,
        secret_id: str | Omit = omit,
        sni_secret_id: SequenceNotStr[str] | Omit = omit,
        timeout_client_data: Optional[int] | Omit = omit,
        timeout_member_connect: Optional[int] | Omit = omit,
        timeout_member_data: Optional[int] | Omit = omit,
        user_list: Iterable[listener_create_params.UserList] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LoadBalancerListenerDetail:
        response = await self.create(
            project_id=project_id,
            region_id=region_id,
            load_balancer_id=load_balancer_id,
            name=name,
            protocol=protocol,
            protocol_port=protocol_port,
            allowed_cidrs=allowed_cidrs,
            connection_limit=connection_limit,
            insert_x_forwarded=insert_x_forwarded,
            secret_id=secret_id,
            sni_secret_id=sni_secret_id,
            timeout_client_data=timeout_client_data,
            timeout_member_connect=timeout_member_connect,
            timeout_member_data=timeout_member_data,
            user_list=user_list,
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
            polling_timeout_seconds=polling_timeout_seconds,
        )
        if (
            not task.created_resources
            or not task.created_resources.listeners
            or len(task.created_resources.listeners) != 1
        ):
            raise ValueError(f"Expected exactly one resource to be created in a task")
        return await self.get(
            listener_id=task.created_resources.listeners[0],
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
            timeout=timeout,
        )

    async def delete_and_poll(
        self,
        listener_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> None:
        """
        Delete listener and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.delete(
            listener_id=listener_id,
            project_id=project_id,
            region_id=region_id,
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
            polling_timeout_seconds=polling_timeout_seconds,
        )

    async def update_and_poll(
        self,
        listener_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        allowed_cidrs: Optional[SequenceNotStr[str]] | Omit = omit,
        connection_limit: int | Omit = omit,
        name: str | Omit = omit,
        secret_id: Optional[str] | Omit = omit,
        sni_secret_id: Optional[SequenceNotStr[str]] | Omit = omit,
        timeout_client_data: Optional[int] | Omit = omit,
        timeout_member_connect: Optional[int] | Omit = omit,
        timeout_member_data: Optional[int] | Omit = omit,
        user_list: Optional[Iterable[listener_update_params.UserList]] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LoadBalancerListenerDetail:
        """
        Update listener and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.update(
            listener_id=listener_id,
            project_id=project_id,
            region_id=region_id,
            allowed_cidrs=allowed_cidrs,
            connection_limit=connection_limit,
            name=name,
            secret_id=secret_id,
            sni_secret_id=sni_secret_id,
            timeout_client_data=timeout_client_data,
            timeout_member_connect=timeout_member_connect,
            timeout_member_data=timeout_member_data,
            user_list=user_list,
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
            polling_timeout_seconds=polling_timeout_seconds,
        )
        return await self.get(
            listener_id=listener_id,
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
            timeout=timeout,
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
        self.create_and_poll = to_raw_response_wrapper(
            listeners.create_and_poll,
        )
        self.delete_and_poll = to_raw_response_wrapper(
            listeners.delete_and_poll,
        )
        self.update_and_poll = to_raw_response_wrapper(
            listeners.update_and_poll,
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
        self.create_and_poll = async_to_raw_response_wrapper(
            listeners.create_and_poll,
        )
        self.delete_and_poll = async_to_raw_response_wrapper(
            listeners.delete_and_poll,
        )
        self.update_and_poll = async_to_raw_response_wrapper(
            listeners.update_and_poll,
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
        self.create_and_poll = to_streamed_response_wrapper(
            listeners.create_and_poll,
        )
        self.delete_and_poll = to_streamed_response_wrapper(
            listeners.delete_and_poll,
        )
        self.update_and_poll = to_streamed_response_wrapper(
            listeners.update_and_poll,
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
        self.create_and_poll = async_to_streamed_response_wrapper(
            listeners.create_and_poll,
        )
        self.delete_and_poll = async_to_streamed_response_wrapper(
            listeners.delete_and_poll,
        )
        self.update_and_poll = async_to_streamed_response_wrapper(
            listeners.update_and_poll,
        )
