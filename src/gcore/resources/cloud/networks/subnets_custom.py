# Custom code. This file is not generated and is preserved across codegen runs.
# It isolates hand-written *_and_poll convenience methods from generated code to
# eliminate merge conflicts.

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Iterable, Optional, cast

import httpx

from ...._types import NOT_GIVEN, Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit
from ....types.cloud import IPVersion
from ....types.cloud.subnet import Subnet
from ....types.cloud.networks import subnet_create_params
from ....types.cloud.ip_version import IPVersion

if TYPE_CHECKING:
    from ...._client import Gcore, AsyncGcore


class SubnetsResourceCustomMixin:
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
        cidr: str,
        name: str,
        network_id: str,
        connect_to_network_router: bool | Omit = omit,
        dns_nameservers: Optional[SequenceNotStr[str]] | Omit = omit,
        enable_dhcp: bool | Omit = omit,
        gateway_ip: Optional[str] | Omit = omit,
        host_routes: Optional[Iterable[subnet_create_params.HostRoute]] | Omit = omit,
        ip_version: IPVersion | Omit = omit,
        router_id_to_connect: Optional[str] | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Subnet:
        """Create subnet and poll for the result."""
        response = self.create(
            project_id=project_id,
            region_id=region_id,
            cidr=cidr,
            name=name,
            network_id=network_id,
            connect_to_network_router=connect_to_network_router,
            dns_nameservers=dns_nameservers,
            enable_dhcp=enable_dhcp,
            gateway_ip=gateway_ip,
            host_routes=host_routes,
            ip_version=ip_version,
            router_id_to_connect=router_id_to_connect,
            tags=tags,
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
        if not task.created_resources or not task.created_resources.subnets or len(task.created_resources.subnets) != 1:
            raise ValueError("Expected exactly one resource to be created in a task")
        return cast(
            Subnet,
            self.get(
                subnet_id=task.created_resources.subnets[0],
                project_id=project_id,
                region_id=region_id,
                extra_headers=extra_headers,
            ),
        )


class AsyncSubnetsResourceCustomMixin:
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
        cidr: str,
        name: str,
        network_id: str,
        connect_to_network_router: bool | Omit = omit,
        dns_nameservers: Optional[SequenceNotStr[str]] | Omit = omit,
        enable_dhcp: bool | Omit = omit,
        gateway_ip: Optional[str] | Omit = omit,
        host_routes: Optional[Iterable[subnet_create_params.HostRoute]] | Omit = omit,
        ip_version: IPVersion | Omit = omit,
        router_id_to_connect: Optional[str] | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Subnet:
        """Create subnet and poll for the result."""
        response = await self.create(
            project_id=project_id,
            region_id=region_id,
            cidr=cidr,
            name=name,
            network_id=network_id,
            connect_to_network_router=connect_to_network_router,
            dns_nameservers=dns_nameservers,
            enable_dhcp=enable_dhcp,
            gateway_ip=gateway_ip,
            host_routes=host_routes,
            ip_version=ip_version,
            router_id_to_connect=router_id_to_connect,
            tags=tags,
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
        if not task.created_resources or not task.created_resources.subnets or len(task.created_resources.subnets) != 1:
            raise ValueError("Expected exactly one resource to be created in a task")
        return cast(
            Subnet,
            await self.get(
                subnet_id=task.created_resources.subnets[0],
                project_id=project_id,
                region_id=region_id,
                extra_headers=extra_headers,
            ),
        )
