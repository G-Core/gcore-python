# Custom code. This file is not generated and is preserved across codegen runs.
# It isolates hand-written *_and_poll convenience methods from generated code to
# eliminate merge conflicts.

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterable, Optional, cast

import httpx

from ....._types import NOT_GIVEN, Body, Omit, Query, Headers, NotGiven, omit
from .....types.cloud import LbAlgorithm, LbPoolProtocol
from .....types.cloud.lb_algorithm import LbAlgorithm
from .....types.cloud.load_balancers import pool_create_params, pool_update_params
from .....types.cloud.lb_pool_protocol import LbPoolProtocol
from .....types.cloud.load_balancer_pool import LoadBalancerPool

if TYPE_CHECKING:
    from ....._client import Gcore, AsyncGcore


class PoolsResourceCustomMixin:
    if TYPE_CHECKING:
        # Provided by the concrete generated resource class this mixin is
        # combined with; declared here so client-derived locals keep their
        # real types and other resource methods resolve via __getattr__.
        _client: Gcore

        def __getattr__(self, name: str) -> Any: ...

    def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        lb_algorithm: LbAlgorithm,
        name: str,
        protocol: LbPoolProtocol,
        ca_secret_id: Optional[str] | Omit = omit,
        crl_secret_id: Optional[str] | Omit = omit,
        healthmonitor: Optional[pool_create_params.Healthmonitor] | Omit = omit,
        listener_id: Optional[str] | Omit = omit,
        load_balancer_id: Optional[str] | Omit = omit,
        members: Iterable[pool_create_params.Member] | Omit = omit,
        secret_id: Optional[str] | Omit = omit,
        session_persistence: Optional[pool_create_params.SessionPersistence] | Omit = omit,
        timeout_client_data: Optional[int] | Omit = omit,
        timeout_member_connect: Optional[int] | Omit = omit,
        timeout_member_data: Optional[int] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
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
            load_balancer_id=load_balancer_id,
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
            raise ValueError("Expected exactly one task to be created")
        task = self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        if not task.created_resources or not task.created_resources.pools or len(task.created_resources.pools) != 1:
            raise ValueError("Expected exactly one resource to be created in a task")
        return cast(
            LoadBalancerPool,
            self.get(
                pool_id=task.created_resources.pools[0],
                project_id=project_id,
                region_id=region_id,
                extra_headers=extra_headers,
                timeout=timeout,
            ),
        )

    def delete_and_poll(
        self,
        pool_id: str,
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
            polling_timeout_seconds=polling_timeout_seconds,
        )

    def update_and_poll(
        self,
        pool_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        ca_secret_id: Optional[str] | Omit = omit,
        crl_secret_id: Optional[str] | Omit = omit,
        healthmonitor: Optional[pool_update_params.Healthmonitor] | Omit = omit,
        lb_algorithm: LbAlgorithm | Omit = omit,
        members: Optional[Iterable[pool_update_params.Member]] | Omit = omit,
        name: str | Omit = omit,
        protocol: LbPoolProtocol | Omit = omit,
        secret_id: Optional[str] | Omit = omit,
        session_persistence: Optional[pool_update_params.SessionPersistence] | Omit = omit,
        timeout_client_data: Optional[int] | Omit = omit,
        timeout_member_connect: Optional[int] | Omit = omit,
        timeout_member_data: Optional[int] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
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
            polling_timeout_seconds=polling_timeout_seconds,
        )
        return cast(
            LoadBalancerPool,
            self.get(
                pool_id=pool_id,
                project_id=project_id,
                region_id=region_id,
                extra_headers=extra_headers,
                timeout=timeout,
            ),
        )


class AsyncPoolsResourceCustomMixin:
    if TYPE_CHECKING:
        # Provided by the concrete generated resource class this mixin is
        # combined with; declared here so client-derived locals keep their
        # real types and other resource methods resolve via __getattr__.
        _client: AsyncGcore

        def __getattr__(self, name: str) -> Any: ...

    async def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        lb_algorithm: LbAlgorithm,
        name: str,
        protocol: LbPoolProtocol,
        ca_secret_id: Optional[str] | Omit = omit,
        crl_secret_id: Optional[str] | Omit = omit,
        healthmonitor: Optional[pool_create_params.Healthmonitor] | Omit = omit,
        listener_id: Optional[str] | Omit = omit,
        load_balancer_id: Optional[str] | Omit = omit,
        members: Iterable[pool_create_params.Member] | Omit = omit,
        secret_id: Optional[str] | Omit = omit,
        session_persistence: Optional[pool_create_params.SessionPersistence] | Omit = omit,
        timeout_client_data: Optional[int] | Omit = omit,
        timeout_member_connect: Optional[int] | Omit = omit,
        timeout_member_data: Optional[int] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
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
            load_balancer_id=load_balancer_id,
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
            raise ValueError("Expected exactly one task to be created")
        task = await self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        if not task.created_resources or not task.created_resources.pools or len(task.created_resources.pools) != 1:
            raise ValueError("Expected exactly one resource to be created in a task")
        return cast(
            LoadBalancerPool,
            await self.get(
                pool_id=task.created_resources.pools[0],
                project_id=project_id,
                region_id=region_id,
                extra_headers=extra_headers,
                timeout=timeout,
            ),
        )

    async def delete_and_poll(
        self,
        pool_id: str,
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
            polling_timeout_seconds=polling_timeout_seconds,
        )

    async def update_and_poll(
        self,
        pool_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        ca_secret_id: Optional[str] | Omit = omit,
        crl_secret_id: Optional[str] | Omit = omit,
        healthmonitor: Optional[pool_update_params.Healthmonitor] | Omit = omit,
        lb_algorithm: LbAlgorithm | Omit = omit,
        members: Optional[Iterable[pool_update_params.Member]] | Omit = omit,
        name: str | Omit = omit,
        protocol: LbPoolProtocol | Omit = omit,
        secret_id: Optional[str] | Omit = omit,
        session_persistence: Optional[pool_update_params.SessionPersistence] | Omit = omit,
        timeout_client_data: Optional[int] | Omit = omit,
        timeout_member_connect: Optional[int] | Omit = omit,
        timeout_member_data: Optional[int] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
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
            polling_timeout_seconds=polling_timeout_seconds,
        )
        return cast(
            LoadBalancerPool,
            await self.get(
                pool_id=pool_id,
                project_id=project_id,
                region_id=region_id,
                extra_headers=extra_headers,
                timeout=timeout,
            ),
        )
