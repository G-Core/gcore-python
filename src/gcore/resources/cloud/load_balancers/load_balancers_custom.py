# Custom code. This file is not generated and is preserved across codegen runs.
# It isolates hand-written *_and_poll convenience methods from generated code to
# eliminate merge conflicts.

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Iterable, cast

import httpx

from ...._types import NOT_GIVEN, Body, Omit, Query, Headers, NotGiven, omit
from ....types.cloud import (
    InterfaceIPFamily,
    LoadBalancerMemberConnectivity,
    load_balancer_create_params,
)
from ....types.cloud.load_balancer import LoadBalancer
from ....types.cloud.interface_ip_family import InterfaceIPFamily
from ....types.cloud.load_balancer_member_connectivity import LoadBalancerMemberConnectivity

if TYPE_CHECKING:
    from ...._client import Gcore, AsyncGcore


class LoadBalancersResourceCustomMixin:
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
        flavor: str | Omit = omit,
        floating_ip: load_balancer_create_params.FloatingIP | Omit = omit,
        listeners: Iterable[load_balancer_create_params.Listener] | Omit = omit,
        logging: load_balancer_create_params.Logging | Omit = omit,
        name: str,
        preferred_connectivity: LoadBalancerMemberConnectivity | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        vip_ip_family: InterfaceIPFamily | Omit = omit,
        vip_network_id: str | Omit = omit,
        vip_port_id: str | Omit = omit,
        vip_subnet_id: str | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LoadBalancer:
        response = self.create(
            project_id=project_id,
            region_id=region_id,
            flavor=flavor,
            floating_ip=floating_ip,
            listeners=listeners,
            logging=logging,
            name=name,
            preferred_connectivity=preferred_connectivity,
            tags=tags,
            vip_ip_family=vip_ip_family,
            vip_network_id=vip_network_id,
            vip_port_id=vip_port_id,
            vip_subnet_id=vip_subnet_id,
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
        if (
            not task.created_resources
            or not task.created_resources.loadbalancers
            or len(task.created_resources.loadbalancers) != 1
        ):
            raise ValueError("Expected exactly one resource to be created in a task")
        return cast(
            LoadBalancer,
            self.get(
                load_balancer_id=task.created_resources.loadbalancers[0],
                project_id=project_id,
                region_id=region_id,
                extra_headers=extra_headers,
                timeout=timeout,
            ),
        )

    def delete_and_poll(
        self,
        load_balancer_id: str,
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
        Delete load balancer and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.delete(
            load_balancer_id=load_balancer_id,
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

    def failover_and_poll(
        self,
        load_balancer_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        force: bool | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LoadBalancer:
        """
        Failover load balancer and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.failover(
            load_balancer_id=load_balancer_id,
            project_id=project_id,
            region_id=region_id,
            force=force,
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
            LoadBalancer,
            self.get(
                load_balancer_id=load_balancer_id,
                project_id=project_id,
                region_id=region_id,
                extra_headers=extra_headers,
                timeout=timeout,
            ),
        )

    def resize_and_poll(
        self,
        load_balancer_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        flavor: str,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LoadBalancer:
        """
        Resize load balancer and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.resize(
            load_balancer_id=load_balancer_id,
            project_id=project_id,
            region_id=region_id,
            flavor=flavor,
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
            LoadBalancer,
            self.get(
                load_balancer_id=load_balancer_id,
                project_id=project_id,
                region_id=region_id,
                extra_headers=extra_headers,
                timeout=timeout,
            ),
        )


class AsyncLoadBalancersResourceCustomMixin:
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
        flavor: str | Omit = omit,
        floating_ip: load_balancer_create_params.FloatingIP | Omit = omit,
        listeners: Iterable[load_balancer_create_params.Listener] | Omit = omit,
        logging: load_balancer_create_params.Logging | Omit = omit,
        name: str,
        preferred_connectivity: LoadBalancerMemberConnectivity | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        vip_ip_family: InterfaceIPFamily | Omit = omit,
        vip_network_id: str | Omit = omit,
        vip_port_id: str | Omit = omit,
        vip_subnet_id: str | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LoadBalancer:
        response = await self.create(
            project_id=project_id,
            region_id=region_id,
            flavor=flavor,
            floating_ip=floating_ip,
            listeners=listeners,
            logging=logging,
            name=name,
            preferred_connectivity=preferred_connectivity,
            tags=tags,
            vip_ip_family=vip_ip_family,
            vip_network_id=vip_network_id,
            vip_port_id=vip_port_id,
            vip_subnet_id=vip_subnet_id,
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
        if (
            not task.created_resources
            or not task.created_resources.loadbalancers
            or len(task.created_resources.loadbalancers) != 1
        ):
            raise ValueError("Expected exactly one resource to be created in a task")
        return cast(
            LoadBalancer,
            await self.get(
                load_balancer_id=task.created_resources.loadbalancers[0],
                project_id=project_id,
                region_id=region_id,
                extra_headers=extra_headers,
                timeout=timeout,
            ),
        )

    async def delete_and_poll(
        self,
        load_balancer_id: str,
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
        Delete load balancer and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.delete(
            load_balancer_id=load_balancer_id,
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

    async def failover_and_poll(
        self,
        load_balancer_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        force: bool | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LoadBalancer:
        """
        Failover load balancer and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.failover(
            load_balancer_id=load_balancer_id,
            project_id=project_id,
            region_id=region_id,
            force=force,
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
        return cast(
            LoadBalancer,
            await self.get(
                load_balancer_id=load_balancer_id,
                project_id=project_id,
                region_id=region_id,
                extra_headers=extra_headers,
                timeout=timeout,
            ),
        )

    async def resize_and_poll(
        self,
        load_balancer_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        flavor: str,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LoadBalancer:
        """
        Resize load balancer and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.resize(
            load_balancer_id=load_balancer_id,
            project_id=project_id,
            region_id=region_id,
            flavor=flavor,
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
        return cast(
            LoadBalancer,
            await self.get(
                load_balancer_id=load_balancer_id,
                project_id=project_id,
                region_id=region_id,
                extra_headers=extra_headers,
                timeout=timeout,
            ),
        )
