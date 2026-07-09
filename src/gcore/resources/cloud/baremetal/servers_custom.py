# Custom code. This file is not generated and is preserved across codegen runs.
# It isolates hand-written *_and_poll convenience methods from generated code to
# eliminate merge conflicts.

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Iterable, Optional, cast

from ...._types import Body, Omit, Query, Headers, omit
from ....types.cloud.baremetal import (
    server_create_params,
)
from ....types.cloud.baremetal.baremetal_server import BaremetalServer

if TYPE_CHECKING:
    from ...._client import Gcore, AsyncGcore


class ServersResourceCustomMixin:
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
        flavor: str,
        interfaces: Iterable[server_create_params.Interface],
        app_config: Optional[Dict[str, object]] | Omit = omit,
        apptemplate_id: str | Omit = omit,
        ddos_profile: server_create_params.DDOSProfile | Omit = omit,
        image_id: str | Omit = omit,
        name: str | Omit = omit,
        name_template: str | Omit = omit,
        password: str | Omit = omit,
        ssh_key_name: Optional[str] | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        user_data: str | Omit = omit,
        username: str | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> BaremetalServer:
        """
        Create a bare metal server and wait for it to be ready.
        """
        response = self.create(
            project_id=project_id,
            region_id=region_id,
            flavor=flavor,
            interfaces=interfaces,
            app_config=app_config,
            apptemplate_id=apptemplate_id,
            ddos_profile=ddos_profile,
            image_id=image_id,
            name=name,
            name_template=name_template,
            password=password,
            ssh_key_name=ssh_key_name,
            tags=tags,
            user_data=user_data,
            username=username,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )
        if not response.tasks or len(response.tasks) != 1:
            raise ValueError("Expected exactly one task to be created")
        task = self._client.cloud.tasks.poll(
            response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        if not task.created_resources or not task.created_resources.instances:
            raise ValueError("No server was created")
        server_id = task.created_resources.instances[0]
        servers = self.list(
            project_id=project_id,
            region_id=region_id,
            uuid=server_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )
        if len(servers.results) != 1:
            raise ValueError(f"Server {server_id} not found")
        return cast(BaremetalServer, servers.results[0])

    def rebuild_and_poll(
        self,
        server_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        image_id: str | Omit = omit,
        user_data: str | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> BaremetalServer:
        """
        Rebuild a bare metal server and wait for it to be ready. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.rebuild(
            server_id=server_id,
            project_id=project_id,
            region_id=region_id,
            image_id=image_id,
            user_data=user_data,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )
        if not response.tasks:
            raise ValueError("Expected at least one task to be created")
        self._client.cloud.tasks.poll(
            response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        servers = self.list(
            project_id=project_id,
            region_id=region_id,
            uuid=server_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )
        if len(servers.results) != 1:
            raise ValueError(f"Server {server_id} not found")
        return cast(BaremetalServer, servers.results[0])


class AsyncServersResourceCustomMixin:
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
        flavor: str,
        interfaces: Iterable[server_create_params.Interface],
        app_config: Optional[Dict[str, object]] | Omit = omit,
        apptemplate_id: str | Omit = omit,
        ddos_profile: server_create_params.DDOSProfile | Omit = omit,
        image_id: str | Omit = omit,
        name: str | Omit = omit,
        name_template: str | Omit = omit,
        password: str | Omit = omit,
        ssh_key_name: Optional[str] | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        user_data: str | Omit = omit,
        username: str | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> BaremetalServer:
        """
        Create a bare metal server and wait for it to be ready.
        """
        response = await self.create(
            project_id=project_id,
            region_id=region_id,
            flavor=flavor,
            interfaces=interfaces,
            app_config=app_config,
            apptemplate_id=apptemplate_id,
            ddos_profile=ddos_profile,
            image_id=image_id,
            name=name,
            name_template=name_template,
            password=password,
            ssh_key_name=ssh_key_name,
            tags=tags,
            user_data=user_data,
            username=username,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )
        if not response.tasks or len(response.tasks) != 1:
            raise ValueError("Expected exactly one task to be created")
        task = await self._client.cloud.tasks.poll(
            response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        if not task.created_resources or not task.created_resources.instances:
            raise ValueError("No server was created")
        server_id = task.created_resources.instances[0]
        servers = await self.list(
            project_id=project_id,
            region_id=region_id,
            uuid=server_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )
        if len(servers.results) != 1:
            raise ValueError(f"Server {server_id} not found")
        return cast(BaremetalServer, servers.results[0])

    async def rebuild_and_poll(
        self,
        server_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        image_id: str | Omit = omit,
        user_data: str | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> BaremetalServer:
        """
        Rebuild a bare metal server and wait for it to be ready. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.rebuild(
            server_id=server_id,
            project_id=project_id,
            region_id=region_id,
            image_id=image_id,
            user_data=user_data,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )
        if not response.tasks:
            raise ValueError("Expected at least one task to be created")
        await self._client.cloud.tasks.poll(
            response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        servers = await self.list(
            project_id=project_id,
            region_id=region_id,
            uuid=server_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )
        if len(servers.results) != 1:
            raise ValueError(f"Server {server_id} not found")
        return cast(BaremetalServer, servers.results[0])
