# Custom code. This file is not generated and is preserved across codegen runs.
# It isolates hand-written *_and_poll convenience methods from generated code to
# eliminate merge conflicts.

from __future__ import annotations

from typing import TYPE_CHECKING, Any, cast

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .....types.cloud.gpu_baremetal.clusters.gpu_baremetal_cluster_server import GPUBaremetalClusterServer

if TYPE_CHECKING:
    from ....._client import Gcore, AsyncGcore


class ServersResourceCustomMixin:
    if TYPE_CHECKING:
        # Provided by the concrete generated resource class this mixin is
        # combined with; declared here so client-derived locals keep their
        # real types and other resource methods resolve via __getattr__.
        _client: Gcore

        def __getattr__(self, name: str) -> Any: ...

    def delete_and_poll(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        cluster_id: str,
        delete_floatings: bool | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a bare metal GPU server from cluster and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.delete(
            instance_id=instance_id,
            project_id=project_id,
            region_id=region_id,
            cluster_id=cluster_id,
            delete_floatings=delete_floatings,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks or len(response.tasks) < 1:
            raise ValueError("Expected at least one task to be created")
        self._client.cloud.tasks.poll(
            response.tasks[0],
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )

    def replace_and_poll(
        self,
        server_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        cluster_id: str,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GPUBaremetalClusterServer:
        """
        Replace a bare metal GPU cluster server and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.replace(
            server_id=server_id,
            project_id=project_id,
            region_id=region_id,
            cluster_id=cluster_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks or len(response.tasks) < 1:
            raise ValueError("Expected at least one task to be created")
        task = self._client.cloud.tasks.poll(
            response.tasks[0],
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        if not task.created_resources or not task.created_resources.instances:
            raise ValueError("No server was created")
        new_server_id = task.created_resources.instances[0]
        servers = self.list(
            cluster_id=cluster_id,
            project_id=project_id,
            region_id=region_id,
            uuids=[new_server_id],
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )
        if not servers.results or len(servers.results) != 1:
            raise ValueError(f"Server {new_server_id} not found")
        return cast(GPUBaremetalClusterServer, servers.results[0])

    def rebuild_and_poll(
        self,
        server_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        cluster_id: str,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GPUBaremetalClusterServer:
        """
        Rebuild a bare metal GPU cluster server and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.rebuild(
            server_id=server_id,
            project_id=project_id,
            region_id=region_id,
            cluster_id=cluster_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks or len(response.tasks) < 1:
            raise ValueError("Expected at least one task to be created")
        self._client.cloud.tasks.poll(
            response.tasks[0],
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        servers = self.list(
            cluster_id=cluster_id,
            project_id=project_id,
            region_id=region_id,
            uuids=[server_id],
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )
        if not servers.results or len(servers.results) != 1:
            raise ValueError(f"Server {server_id} not found")
        return cast(GPUBaremetalClusterServer, servers.results[0])


class AsyncServersResourceCustomMixin:
    if TYPE_CHECKING:
        # Provided by the concrete generated resource class this mixin is
        # combined with; declared here so client-derived locals keep their
        # real types and other resource methods resolve via __getattr__.
        _client: AsyncGcore

        def __getattr__(self, name: str) -> Any: ...

    async def delete_and_poll(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        cluster_id: str,
        delete_floatings: bool | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a bare metal GPU server from cluster and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.delete(
            instance_id=instance_id,
            project_id=project_id,
            region_id=region_id,
            cluster_id=cluster_id,
            delete_floatings=delete_floatings,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks or len(response.tasks) < 1:
            raise ValueError("Expected at least one task to be created")
        await self._client.cloud.tasks.poll(
            response.tasks[0],
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )

    async def replace_and_poll(
        self,
        server_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        cluster_id: str,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GPUBaremetalClusterServer:
        """
        Replace a bare metal GPU cluster server and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.replace(
            server_id=server_id,
            project_id=project_id,
            region_id=region_id,
            cluster_id=cluster_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks or len(response.tasks) < 1:
            raise ValueError("Expected at least one task to be created")
        task = await self._client.cloud.tasks.poll(
            response.tasks[0],
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        if not task.created_resources or not task.created_resources.instances:
            raise ValueError("No server was created")
        new_server_id = task.created_resources.instances[0]
        servers = await self.list(
            cluster_id=cluster_id,
            project_id=project_id,
            region_id=region_id,
            uuids=[new_server_id],
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )
        if not servers.results or len(servers.results) != 1:
            raise ValueError(f"Server {new_server_id} not found")
        return cast(GPUBaremetalClusterServer, servers.results[0])

    async def rebuild_and_poll(
        self,
        server_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        cluster_id: str,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GPUBaremetalClusterServer:
        """
        Rebuild a bare metal GPU cluster server and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.rebuild(
            server_id=server_id,
            project_id=project_id,
            region_id=region_id,
            cluster_id=cluster_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks or len(response.tasks) < 1:
            raise ValueError("Expected at least one task to be created")
        await self._client.cloud.tasks.poll(
            response.tasks[0],
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        servers = await self.list(
            cluster_id=cluster_id,
            project_id=project_id,
            region_id=region_id,
            uuids=[server_id],
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )
        if not servers.results or len(servers.results) != 1:
            raise ValueError(f"Server {server_id} not found")
        return cast(GPUBaremetalClusterServer, servers.results[0])
