# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from .members import (
    MembersResource,
    AsyncMembersResource,
    MembersResourceWithRawResponse,
    AsyncMembersResourceWithRawResponse,
    MembersResourceWithStreamingResponse,
    AsyncMembersResourceWithStreamingResponse,
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
from .....types.cloud import LbAlgorithm, LbPoolProtocol
from .health_monitors import (
    HealthMonitorsResource,
    AsyncHealthMonitorsResource,
    HealthMonitorsResourceWithRawResponse,
    AsyncHealthMonitorsResourceWithRawResponse,
    HealthMonitorsResourceWithStreamingResponse,
    AsyncHealthMonitorsResourceWithStreamingResponse,
)
from ....._base_client import make_request_options
from .....types.cloud.lb_algorithm import LbAlgorithm
from .....types.cloud.task_id_list import TaskIDList
from .....types.cloud.load_balancers import pool_list_params, pool_create_params, pool_update_params
from .....types.cloud.lb_pool_protocol import LbPoolProtocol
from .....types.cloud.load_balancer_pool import LoadBalancerPool
from .....types.cloud.load_balancer_pool_list import LoadBalancerPoolList

__all__ = ["PoolsResource", "AsyncPoolsResource"]


class PoolsResource(SyncAPIResource):
    @cached_property
    def health_monitors(self) -> HealthMonitorsResource:
        return HealthMonitorsResource(self._client)

    @cached_property
    def members(self) -> MembersResource:
        return MembersResource(self._client)

    @cached_property
    def with_raw_response(self) -> PoolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return PoolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PoolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return PoolsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        lb_algorithm: LbAlgorithm,
        name: str,
        protocol: LbPoolProtocol,
        ca_secret_id: Optional[str] | NotGiven = NOT_GIVEN,
        crl_secret_id: Optional[str] | NotGiven = NOT_GIVEN,
        healthmonitor: Optional[pool_create_params.Healthmonitor] | NotGiven = NOT_GIVEN,
        listener_id: Optional[str] | NotGiven = NOT_GIVEN,
        loadbalancer_id: Optional[str] | NotGiven = NOT_GIVEN,
        members: Optional[Iterable[pool_create_params.Member]] | NotGiven = NOT_GIVEN,
        secret_id: Optional[str] | NotGiven = NOT_GIVEN,
        session_persistence: Optional[pool_create_params.SessionPersistence] | NotGiven = NOT_GIVEN,
        timeout_client_data: Optional[int] | NotGiven = NOT_GIVEN,
        timeout_member_connect: Optional[int] | NotGiven = NOT_GIVEN,
        timeout_member_data: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Create load balancer pool

        Args:
          project_id: Project ID

          region_id: Region ID

          lb_algorithm: Load balancer algorithm

          name: Pool name

          protocol: Protocol

          ca_secret_id: Secret ID of CA certificate bundle

          crl_secret_id: Secret ID of CA revocation list file

          healthmonitor: Health monitor details

          listener_id: Listener ID

          loadbalancer_id: Loadbalancer ID

          members: Pool members

          secret_id: Secret ID for TLS client authentication to the member servers

          session_persistence: Session persistence details

          timeout_client_data: Frontend client inactivity timeout in milliseconds

          timeout_member_connect: Backend member connection timeout in milliseconds

          timeout_member_data: Backend member inactivity timeout in milliseconds

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
            f"/cloud/v1/lbpools/{project_id}/{region_id}",
            body=maybe_transform(
                {
                    "lb_algorithm": lb_algorithm,
                    "name": name,
                    "protocol": protocol,
                    "ca_secret_id": ca_secret_id,
                    "crl_secret_id": crl_secret_id,
                    "healthmonitor": healthmonitor,
                    "listener_id": listener_id,
                    "loadbalancer_id": loadbalancer_id,
                    "members": members,
                    "secret_id": secret_id,
                    "session_persistence": session_persistence,
                    "timeout_client_data": timeout_client_data,
                    "timeout_member_connect": timeout_member_connect,
                    "timeout_member_data": timeout_member_data,
                },
                pool_create_params.PoolCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def update(
        self,
        pool_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        ca_secret_id: Optional[str] | NotGiven = NOT_GIVEN,
        crl_secret_id: Optional[str] | NotGiven = NOT_GIVEN,
        healthmonitor: Optional[pool_update_params.Healthmonitor] | NotGiven = NOT_GIVEN,
        lb_algorithm: LbAlgorithm | NotGiven = NOT_GIVEN,
        members: Optional[Iterable[pool_update_params.Member]] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        protocol: LbPoolProtocol | NotGiven = NOT_GIVEN,
        secret_id: Optional[str] | NotGiven = NOT_GIVEN,
        session_persistence: Optional[pool_update_params.SessionPersistence] | NotGiven = NOT_GIVEN,
        timeout_client_data: Optional[int] | NotGiven = NOT_GIVEN,
        timeout_member_connect: Optional[int] | NotGiven = NOT_GIVEN,
        timeout_member_data: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Changes provided here will overwrite existing load balancer pool settings.
        Undefined fields will be kept as is. Complex objects need to be specified fully,
        they will be overwritten.

        Args:
          project_id: Project ID

          region_id: Region ID

          pool_id: Pool ID

          ca_secret_id: Secret ID of CA certificate bundle

          crl_secret_id: Secret ID of CA revocation list file

          healthmonitor: New pool health monitor settings

          lb_algorithm: New load balancer pool algorithm of how to distribute requests

          members: New sequence of load balancer pool members. If members are the same (by
              address + port), they will be kept as is without recreation and downtime.

          name: New pool name

          protocol: New communication protocol

          secret_id: Secret ID for TLS client authentication to the member servers

          session_persistence: New session persistence settings

          timeout_client_data: Frontend client inactivity timeout in milliseconds

          timeout_member_connect: Backend member connection timeout in milliseconds

          timeout_member_data: Backend member inactivity timeout in milliseconds

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not pool_id:
            raise ValueError(f"Expected a non-empty value for `pool_id` but received {pool_id!r}")
        return self._patch(
            f"/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}",
            body=maybe_transform(
                {
                    "ca_secret_id": ca_secret_id,
                    "crl_secret_id": crl_secret_id,
                    "healthmonitor": healthmonitor,
                    "lb_algorithm": lb_algorithm,
                    "members": members,
                    "name": name,
                    "protocol": protocol,
                    "secret_id": secret_id,
                    "session_persistence": session_persistence,
                    "timeout_client_data": timeout_client_data,
                    "timeout_member_connect": timeout_member_connect,
                    "timeout_member_data": timeout_member_data,
                },
                pool_update_params.PoolUpdateParams,
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
        details: bool | NotGiven = NOT_GIVEN,
        listener_id: str | NotGiven = NOT_GIVEN,
        loadbalancer_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoadBalancerPoolList:
        """
        List load balancer pools

        Args:
          project_id: Project ID

          region_id: Region ID

          details: Show members and Health Monitor details

          listener_id: Listener ID

          loadbalancer_id: Load Balancer ID

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
            f"/cloud/v1/lbpools/{project_id}/{region_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "details": details,
                        "listener_id": listener_id,
                        "loadbalancer_id": loadbalancer_id,
                    },
                    pool_list_params.PoolListParams,
                ),
            ),
            cast_to=LoadBalancerPoolList,
        )

    def delete(
        self,
        pool_id: str,
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
        Delete load balancer pool

        Args:
          project_id: Project ID

          region_id: Region ID

          pool_id: Pool ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not pool_id:
            raise ValueError(f"Expected a non-empty value for `pool_id` but received {pool_id!r}")
        return self._delete(
            f"/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def get(
        self,
        pool_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoadBalancerPool:
        """
        Get load balancer pool

        Args:
          project_id: Project ID

          region_id: Region ID

          pool_id: Pool ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not pool_id:
            raise ValueError(f"Expected a non-empty value for `pool_id` but received {pool_id!r}")
        return self._get(
            f"/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoadBalancerPool,
        )

    def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        lb_algorithm: LbAlgorithm,
        name: str,
        protocol: LbPoolProtocol,
        ca_secret_id: Optional[str] | NotGiven = NOT_GIVEN,
        crl_secret_id: Optional[str] | NotGiven = NOT_GIVEN,
        healthmonitor: Optional[pool_create_params.Healthmonitor] | NotGiven = NOT_GIVEN,
        listener_id: Optional[str] | NotGiven = NOT_GIVEN,
        loadbalancer_id: Optional[str] | NotGiven = NOT_GIVEN,
        members: Optional[Iterable[pool_create_params.Member]] | NotGiven = NOT_GIVEN,
        secret_id: Optional[str] | NotGiven = NOT_GIVEN,
        session_persistence: Optional[pool_create_params.SessionPersistence] | NotGiven = NOT_GIVEN,
        timeout_client_data: Optional[int] | NotGiven = NOT_GIVEN,
        timeout_member_connect: Optional[int] | NotGiven = NOT_GIVEN,
        timeout_member_data: Optional[int] | NotGiven = NOT_GIVEN,
        polling_interval_seconds: int | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LoadBalancerPool:
        response = self.create(
            project_id=project_id,
            region_id=region_id,
            lb_algorithm=lb_algorithm,
            name=name,
            protocol=protocol,
            ca_secret_id=ca_secret_id,
            crl_secret_id=crl_secret_id,
            healthmonitor=healthmonitor,
            listener_id=listener_id,
            loadbalancer_id=loadbalancer_id,
            members=members,
            secret_id=secret_id,
            session_persistence=session_persistence,
            timeout_client_data=timeout_client_data,
            timeout_member_connect=timeout_member_connect,
            timeout_member_data=timeout_member_data,
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
        if not task.created_resources or not task.created_resources.pools or len(task.created_resources.pools) != 1:
            raise ValueError(f"Expected exactly one resource to be created in a task")
        return self.get(
            pool_id=task.created_resources.pools[0],
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
            timeout=timeout,
        )

    def delete_and_poll(
        self,
        pool_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        polling_interval_seconds: int | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> None:
        """
        Delete pool and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.delete(
            pool_id=pool_id,
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
        )

    def update_and_poll(
        self,
        pool_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        ca_secret_id: Optional[str] | NotGiven = NOT_GIVEN,
        crl_secret_id: Optional[str] | NotGiven = NOT_GIVEN,
        healthmonitor: Optional[pool_update_params.Healthmonitor] | NotGiven = NOT_GIVEN,
        lb_algorithm: LbAlgorithm | NotGiven = NOT_GIVEN,
        members: Optional[Iterable[pool_update_params.Member]] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        protocol: LbPoolProtocol | NotGiven = NOT_GIVEN,
        secret_id: Optional[str] | NotGiven = NOT_GIVEN,
        session_persistence: Optional[pool_update_params.SessionPersistence] | NotGiven = NOT_GIVEN,
        timeout_client_data: Optional[int] | NotGiven = NOT_GIVEN,
        timeout_member_connect: Optional[int] | NotGiven = NOT_GIVEN,
        timeout_member_data: Optional[int] | NotGiven = NOT_GIVEN,
        polling_interval_seconds: int | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LoadBalancerPool:
        """
        Update pool and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.update(
            pool_id=pool_id,
            project_id=project_id,
            region_id=region_id,
            ca_secret_id=ca_secret_id,
            crl_secret_id=crl_secret_id,
            healthmonitor=healthmonitor,
            lb_algorithm=lb_algorithm,
            members=members,
            name=name,
            protocol=protocol,
            secret_id=secret_id,
            session_persistence=session_persistence,
            timeout_client_data=timeout_client_data,
            timeout_member_connect=timeout_member_connect,
            timeout_member_data=timeout_member_data,
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
            pool_id=pool_id,
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
            timeout=timeout,
        )


class AsyncPoolsResource(AsyncAPIResource):
    @cached_property
    def health_monitors(self) -> AsyncHealthMonitorsResource:
        return AsyncHealthMonitorsResource(self._client)

    @cached_property
    def members(self) -> AsyncMembersResource:
        return AsyncMembersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPoolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPoolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPoolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncPoolsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        lb_algorithm: LbAlgorithm,
        name: str,
        protocol: LbPoolProtocol,
        ca_secret_id: Optional[str] | NotGiven = NOT_GIVEN,
        crl_secret_id: Optional[str] | NotGiven = NOT_GIVEN,
        healthmonitor: Optional[pool_create_params.Healthmonitor] | NotGiven = NOT_GIVEN,
        listener_id: Optional[str] | NotGiven = NOT_GIVEN,
        loadbalancer_id: Optional[str] | NotGiven = NOT_GIVEN,
        members: Optional[Iterable[pool_create_params.Member]] | NotGiven = NOT_GIVEN,
        secret_id: Optional[str] | NotGiven = NOT_GIVEN,
        session_persistence: Optional[pool_create_params.SessionPersistence] | NotGiven = NOT_GIVEN,
        timeout_client_data: Optional[int] | NotGiven = NOT_GIVEN,
        timeout_member_connect: Optional[int] | NotGiven = NOT_GIVEN,
        timeout_member_data: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Create load balancer pool

        Args:
          project_id: Project ID

          region_id: Region ID

          lb_algorithm: Load balancer algorithm

          name: Pool name

          protocol: Protocol

          ca_secret_id: Secret ID of CA certificate bundle

          crl_secret_id: Secret ID of CA revocation list file

          healthmonitor: Health monitor details

          listener_id: Listener ID

          loadbalancer_id: Loadbalancer ID

          members: Pool members

          secret_id: Secret ID for TLS client authentication to the member servers

          session_persistence: Session persistence details

          timeout_client_data: Frontend client inactivity timeout in milliseconds

          timeout_member_connect: Backend member connection timeout in milliseconds

          timeout_member_data: Backend member inactivity timeout in milliseconds

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
            f"/cloud/v1/lbpools/{project_id}/{region_id}",
            body=await async_maybe_transform(
                {
                    "lb_algorithm": lb_algorithm,
                    "name": name,
                    "protocol": protocol,
                    "ca_secret_id": ca_secret_id,
                    "crl_secret_id": crl_secret_id,
                    "healthmonitor": healthmonitor,
                    "listener_id": listener_id,
                    "loadbalancer_id": loadbalancer_id,
                    "members": members,
                    "secret_id": secret_id,
                    "session_persistence": session_persistence,
                    "timeout_client_data": timeout_client_data,
                    "timeout_member_connect": timeout_member_connect,
                    "timeout_member_data": timeout_member_data,
                },
                pool_create_params.PoolCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def update(
        self,
        pool_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        ca_secret_id: Optional[str] | NotGiven = NOT_GIVEN,
        crl_secret_id: Optional[str] | NotGiven = NOT_GIVEN,
        healthmonitor: Optional[pool_update_params.Healthmonitor] | NotGiven = NOT_GIVEN,
        lb_algorithm: LbAlgorithm | NotGiven = NOT_GIVEN,
        members: Optional[Iterable[pool_update_params.Member]] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        protocol: LbPoolProtocol | NotGiven = NOT_GIVEN,
        secret_id: Optional[str] | NotGiven = NOT_GIVEN,
        session_persistence: Optional[pool_update_params.SessionPersistence] | NotGiven = NOT_GIVEN,
        timeout_client_data: Optional[int] | NotGiven = NOT_GIVEN,
        timeout_member_connect: Optional[int] | NotGiven = NOT_GIVEN,
        timeout_member_data: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Changes provided here will overwrite existing load balancer pool settings.
        Undefined fields will be kept as is. Complex objects need to be specified fully,
        they will be overwritten.

        Args:
          project_id: Project ID

          region_id: Region ID

          pool_id: Pool ID

          ca_secret_id: Secret ID of CA certificate bundle

          crl_secret_id: Secret ID of CA revocation list file

          healthmonitor: New pool health monitor settings

          lb_algorithm: New load balancer pool algorithm of how to distribute requests

          members: New sequence of load balancer pool members. If members are the same (by
              address + port), they will be kept as is without recreation and downtime.

          name: New pool name

          protocol: New communication protocol

          secret_id: Secret ID for TLS client authentication to the member servers

          session_persistence: New session persistence settings

          timeout_client_data: Frontend client inactivity timeout in milliseconds

          timeout_member_connect: Backend member connection timeout in milliseconds

          timeout_member_data: Backend member inactivity timeout in milliseconds

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not pool_id:
            raise ValueError(f"Expected a non-empty value for `pool_id` but received {pool_id!r}")
        return await self._patch(
            f"/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}",
            body=await async_maybe_transform(
                {
                    "ca_secret_id": ca_secret_id,
                    "crl_secret_id": crl_secret_id,
                    "healthmonitor": healthmonitor,
                    "lb_algorithm": lb_algorithm,
                    "members": members,
                    "name": name,
                    "protocol": protocol,
                    "secret_id": secret_id,
                    "session_persistence": session_persistence,
                    "timeout_client_data": timeout_client_data,
                    "timeout_member_connect": timeout_member_connect,
                    "timeout_member_data": timeout_member_data,
                },
                pool_update_params.PoolUpdateParams,
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
        details: bool | NotGiven = NOT_GIVEN,
        listener_id: str | NotGiven = NOT_GIVEN,
        loadbalancer_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoadBalancerPoolList:
        """
        List load balancer pools

        Args:
          project_id: Project ID

          region_id: Region ID

          details: Show members and Health Monitor details

          listener_id: Listener ID

          loadbalancer_id: Load Balancer ID

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
            f"/cloud/v1/lbpools/{project_id}/{region_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "details": details,
                        "listener_id": listener_id,
                        "loadbalancer_id": loadbalancer_id,
                    },
                    pool_list_params.PoolListParams,
                ),
            ),
            cast_to=LoadBalancerPoolList,
        )

    async def delete(
        self,
        pool_id: str,
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
        Delete load balancer pool

        Args:
          project_id: Project ID

          region_id: Region ID

          pool_id: Pool ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not pool_id:
            raise ValueError(f"Expected a non-empty value for `pool_id` but received {pool_id!r}")
        return await self._delete(
            f"/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def get(
        self,
        pool_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoadBalancerPool:
        """
        Get load balancer pool

        Args:
          project_id: Project ID

          region_id: Region ID

          pool_id: Pool ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not pool_id:
            raise ValueError(f"Expected a non-empty value for `pool_id` but received {pool_id!r}")
        return await self._get(
            f"/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoadBalancerPool,
        )

    async def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        lb_algorithm: LbAlgorithm,
        name: str,
        protocol: LbPoolProtocol,
        ca_secret_id: Optional[str] | NotGiven = NOT_GIVEN,
        crl_secret_id: Optional[str] | NotGiven = NOT_GIVEN,
        healthmonitor: Optional[pool_create_params.Healthmonitor] | NotGiven = NOT_GIVEN,
        listener_id: Optional[str] | NotGiven = NOT_GIVEN,
        loadbalancer_id: Optional[str] | NotGiven = NOT_GIVEN,
        members: Optional[Iterable[pool_create_params.Member]] | NotGiven = NOT_GIVEN,
        secret_id: Optional[str] | NotGiven = NOT_GIVEN,
        session_persistence: Optional[pool_create_params.SessionPersistence] | NotGiven = NOT_GIVEN,
        timeout_client_data: Optional[int] | NotGiven = NOT_GIVEN,
        timeout_member_connect: Optional[int] | NotGiven = NOT_GIVEN,
        timeout_member_data: Optional[int] | NotGiven = NOT_GIVEN,
        polling_interval_seconds: int | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LoadBalancerPool:
        response = await self.create(
            project_id=project_id,
            region_id=region_id,
            lb_algorithm=lb_algorithm,
            name=name,
            protocol=protocol,
            ca_secret_id=ca_secret_id,
            crl_secret_id=crl_secret_id,
            healthmonitor=healthmonitor,
            listener_id=listener_id,
            loadbalancer_id=loadbalancer_id,
            members=members,
            secret_id=secret_id,
            session_persistence=session_persistence,
            timeout_client_data=timeout_client_data,
            timeout_member_connect=timeout_member_connect,
            timeout_member_data=timeout_member_data,
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
        if not task.created_resources or not task.created_resources.pools or len(task.created_resources.pools) != 1:
            raise ValueError(f"Expected exactly one resource to be created in a task")
        return await self.get(
            pool_id=task.created_resources.pools[0],
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
            timeout=timeout,
        )

    async def delete_and_poll(
        self,
        pool_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        polling_interval_seconds: int | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> None:
        """
        Delete pool and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.delete(
            pool_id=pool_id,
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
        )

    async def update_and_poll(
        self,
        pool_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        ca_secret_id: Optional[str] | NotGiven = NOT_GIVEN,
        crl_secret_id: Optional[str] | NotGiven = NOT_GIVEN,
        healthmonitor: Optional[pool_update_params.Healthmonitor] | NotGiven = NOT_GIVEN,
        lb_algorithm: LbAlgorithm | NotGiven = NOT_GIVEN,
        members: Optional[Iterable[pool_update_params.Member]] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        protocol: LbPoolProtocol | NotGiven = NOT_GIVEN,
        secret_id: Optional[str] | NotGiven = NOT_GIVEN,
        session_persistence: Optional[pool_update_params.SessionPersistence] | NotGiven = NOT_GIVEN,
        timeout_client_data: Optional[int] | NotGiven = NOT_GIVEN,
        timeout_member_connect: Optional[int] | NotGiven = NOT_GIVEN,
        timeout_member_data: Optional[int] | NotGiven = NOT_GIVEN,
        polling_interval_seconds: int | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LoadBalancerPool:
        """
        Update pool and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.update(
            pool_id=pool_id,
            project_id=project_id,
            region_id=region_id,
            ca_secret_id=ca_secret_id,
            crl_secret_id=crl_secret_id,
            healthmonitor=healthmonitor,
            lb_algorithm=lb_algorithm,
            members=members,
            name=name,
            protocol=protocol,
            secret_id=secret_id,
            session_persistence=session_persistence,
            timeout_client_data=timeout_client_data,
            timeout_member_connect=timeout_member_connect,
            timeout_member_data=timeout_member_data,
            timeout=timeout,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )
        if not response.tasks:
            raise ValueError("Expected at least one task to be created")
        await self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
        )
        return await self.get(
            pool_id=pool_id,
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
            timeout=timeout,
        )


class PoolsResourceWithRawResponse:
    def __init__(self, pools: PoolsResource) -> None:
        self._pools = pools

        self.create = to_raw_response_wrapper(
            pools.create,
        )
        self.update = to_raw_response_wrapper(
            pools.update,
        )
        self.list = to_raw_response_wrapper(
            pools.list,
        )
        self.delete = to_raw_response_wrapper(
            pools.delete,
        )
        self.get = to_raw_response_wrapper(
            pools.get,
        )

    @cached_property
    def health_monitors(self) -> HealthMonitorsResourceWithRawResponse:
        return HealthMonitorsResourceWithRawResponse(self._pools.health_monitors)

    @cached_property
    def members(self) -> MembersResourceWithRawResponse:
        return MembersResourceWithRawResponse(self._pools.members)


class AsyncPoolsResourceWithRawResponse:
    def __init__(self, pools: AsyncPoolsResource) -> None:
        self._pools = pools

        self.create = async_to_raw_response_wrapper(
            pools.create,
        )
        self.update = async_to_raw_response_wrapper(
            pools.update,
        )
        self.list = async_to_raw_response_wrapper(
            pools.list,
        )
        self.delete = async_to_raw_response_wrapper(
            pools.delete,
        )
        self.get = async_to_raw_response_wrapper(
            pools.get,
        )

    @cached_property
    def health_monitors(self) -> AsyncHealthMonitorsResourceWithRawResponse:
        return AsyncHealthMonitorsResourceWithRawResponse(self._pools.health_monitors)

    @cached_property
    def members(self) -> AsyncMembersResourceWithRawResponse:
        return AsyncMembersResourceWithRawResponse(self._pools.members)


class PoolsResourceWithStreamingResponse:
    def __init__(self, pools: PoolsResource) -> None:
        self._pools = pools

        self.create = to_streamed_response_wrapper(
            pools.create,
        )
        self.update = to_streamed_response_wrapper(
            pools.update,
        )
        self.list = to_streamed_response_wrapper(
            pools.list,
        )
        self.delete = to_streamed_response_wrapper(
            pools.delete,
        )
        self.get = to_streamed_response_wrapper(
            pools.get,
        )

    @cached_property
    def health_monitors(self) -> HealthMonitorsResourceWithStreamingResponse:
        return HealthMonitorsResourceWithStreamingResponse(self._pools.health_monitors)

    @cached_property
    def members(self) -> MembersResourceWithStreamingResponse:
        return MembersResourceWithStreamingResponse(self._pools.members)


class AsyncPoolsResourceWithStreamingResponse:
    def __init__(self, pools: AsyncPoolsResource) -> None:
        self._pools = pools

        self.create = async_to_streamed_response_wrapper(
            pools.create,
        )
        self.update = async_to_streamed_response_wrapper(
            pools.update,
        )
        self.list = async_to_streamed_response_wrapper(
            pools.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            pools.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            pools.get,
        )

    @cached_property
    def health_monitors(self) -> AsyncHealthMonitorsResourceWithStreamingResponse:
        return AsyncHealthMonitorsResourceWithStreamingResponse(self._pools.health_monitors)

    @cached_property
    def members(self) -> AsyncMembersResourceWithStreamingResponse:
        return AsyncMembersResourceWithStreamingResponse(self._pools.members)
