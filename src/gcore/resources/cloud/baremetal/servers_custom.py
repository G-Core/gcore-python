# Custom code. This file is not generated and is preserved across codegen runs.
# It isolates hand-written *_and_poll convenience methods from generated code to
# eliminate merge conflicts.

from __future__ import annotations

import time
from typing import TYPE_CHECKING, Any, Dict, List, Iterable, Optional, Sequence, cast
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import is_given
from ....types.cloud.task import Task
from ....types.cloud.baremetal import server_create_params, server_update_params
from ....types.cloud.tag_update_map_param import TagUpdateMapParam
from ....types.cloud.baremetal.baremetal_server import BaremetalServer
from ....types.cloud.baremetal_regional.baremetal_regional_server import BaremetalRegionalServer

if TYPE_CHECKING:
    from ...._client import Gcore, AsyncGcore

# the values that the API reads as true in a boolean query parameter
_TRUE_QUERY_VALUES = {"1", "on", "t", "true", "y", "yes"}


def _is_true(value: object) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, int):
        return value != 0
    if isinstance(value, str):
        return value.strip().lower() in _TRUE_QUERY_VALUES
    if isinstance(value, (list, tuple)):
        return any(_is_true(item) for item in cast("Sequence[object]", value))
    return False


def _reject_dry_run(client: Gcore | AsyncGcore, extra_query: Query | None) -> None:
    """Raise before any request when the client or `extra_query` asks for a dry run."""
    query = {**client.default_query, **(extra_query or {})}
    if _is_true(query.get("dry_run")):
        raise ValueError(
            "The *_and_poll helpers do not support a dry run, because a dry run starts no task. "
            "Call the method without `_and_poll` and pass `dry_run=True`."
        )


def _require_tasks(task_ids: List[str]) -> List[str]:
    if not task_ids:
        raise ValueError("Expected at least one task to be created")
    return task_ids


def _created_server_id(tasks: List[Task]) -> str:
    """Return the one bare metal server ID that the finished create tasks report."""
    server_ids: List[str] = []
    for task in tasks:
        created = task.created_resources.instances if task.created_resources else None
        for server_id in created or []:
            if server_id and server_id not in server_ids:
                server_ids.append(server_id)
    if not server_ids:
        raise ValueError("The create tasks finished, but no task reports a server in `created_resources.instances`")
    if len(server_ids) > 1:
        raise ValueError(
            f"Expected one created bare metal server, but the tasks report {len(server_ids)}: {server_ids}"
        )
    return server_ids[0]


class _TaskBudget:
    """One polling timeout for all tasks of a call, so that two tasks do not wait twice as long."""

    def __init__(
        self, client: Gcore | AsyncGcore, polling_interval_seconds: int | Omit, polling_timeout_seconds: int | Omit
    ) -> None:
        interval = (
            polling_interval_seconds
            if is_given(polling_interval_seconds)
            else cast(int, client.polling_interval_seconds)
        )
        self._interval = max(1, interval)
        self._timeout = polling_timeout_seconds
        total = (
            polling_timeout_seconds if is_given(polling_timeout_seconds) else cast(int, client.polling_timeout_seconds)
        )
        self._deadline = time.monotonic() + total
        self._first = True

    def next_timeout(self, task_id: str) -> int | Omit:
        """Return the polling timeout of the next task: the time that is left of the budget."""
        if self._first:
            # the first task gets the timeout as given, so that tasks.poll checks it as usual
            self._first = False
            return self._timeout
        remaining = int(self._deadline - time.monotonic())
        # tasks.poll needs a timeout longer than its interval
        if remaining <= self._interval:
            raise TimeoutError(f"Timed out waiting for task {task_id}")
        return remaining


class ServersResourceCustomMixin:
    if TYPE_CHECKING:
        # Provided by the concrete generated resource class this mixin is
        # combined with; declared here so client-derived locals keep their
        # real types and other resource methods resolve via __getattr__.
        _client: Gcore

        def __getattr__(self, name: str) -> Any: ...

    def _wait_for_tasks(
        self,
        task_ids: List[str],
        *,
        polling_interval_seconds: int | Omit,
        polling_timeout_seconds: int | Omit,
        extra_headers: Headers | None,
        timeout: float | httpx.Timeout | None | NotGiven,
    ) -> List[Task]:
        task_ids = _require_tasks(task_ids)
        budget = _TaskBudget(self._client, polling_interval_seconds, polling_timeout_seconds)
        return [
            self._client.cloud.tasks.poll(
                task_id=task_id,
                extra_headers=extra_headers,
                polling_interval_seconds=polling_interval_seconds,
                polling_timeout_seconds=budget.next_timeout(task_id),
                # tasks.poll passes the timeout on to tasks.get, which takes every timeout type
                timeout=cast("float | NotGiven", timeout),
            )
            for task_id in task_ids
        ]

    def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        flavor_name: str,
        image_id: str,
        interfaces: Iterable[server_create_params.Interface],
        region_id: int,
        name: str | Omit = omit,
        password: str | Omit = omit,
        ssh_key_id: str | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        user_data: str | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BaremetalServer:
        """
        Create a bare metal server, wait for every task to finish, and return the new server.

        The helper reads the server ID from `created_resources.instances` of the tasks and calls `get` once.
        The polling timeout covers all tasks together.

        The helper does not support a dry run. Call `create` with `dry_run=True` instead.
        `extra_body` goes only to the create request.
        """
        _reject_dry_run(self._client, extra_query)
        response = self.create(
            project_id=project_id,
            flavor_name=flavor_name,
            image_id=image_id,
            interfaces=interfaces,
            region_id=region_id,
            name=name,
            password=password,
            ssh_key_id=ssh_key_id,
            tags=tags,
            user_data=user_data,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        tasks = self._wait_for_tasks(
            response.tasks,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
            extra_headers=extra_headers,
            timeout=timeout,
        )
        return cast(
            BaremetalServer,
            self.get(
                _created_server_id(tasks),
                project_id=project_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                timeout=timeout,
            ),
        )

    def update_and_poll(
        self,
        server_id: str,
        *,
        project_id: int | None = None,
        interfaces: Iterable[server_update_params.Interface] | Omit = omit,
        name: str | Omit = omit,
        tags: Optional[TagUpdateMapParam] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BaremetalServer:
        """
        Update a bare metal server, wait for every task to finish, and return the server.

        The helper waits for the tasks, not for the global read to show every change. So the returned server can
        show old data for a few seconds after the tasks finish.

        The helper does not support a dry run. Call `update` with `dry_run=True` instead.
        `extra_body` goes only to the update request.
        """
        _reject_dry_run(self._client, extra_query)
        response = self.update(
            server_id=server_id,
            project_id=project_id,
            interfaces=interfaces,
            name=name,
            tags=tags,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        self._wait_for_tasks(
            response.tasks,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
            extra_headers=extra_headers,
            timeout=timeout,
        )
        return cast(
            BaremetalServer,
            self.get(
                server_id,
                project_id=project_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                timeout=timeout,
            ),
        )

    def action_and_poll(
        self,
        server_id: str,
        *,
        project_id: int | None = None,
        action: Literal["reboot", "reboot_hard", "start", "stop"],
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BaremetalServer:
        """
        Run a power action on a bare metal server, wait for every task to finish, and return the server.

        The helper waits for the tasks, not for the global read to show every change. So the returned server can
        show old data, such as the old status, for a few seconds after the tasks finish.

        The helper does not support a dry run. Call `action` with `dry_run=True` instead.
        `extra_body` goes only to the action request.
        """
        _reject_dry_run(self._client, extra_query)
        response = self.action(
            server_id=server_id,
            project_id=project_id,
            action=action,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        self._wait_for_tasks(
            response.tasks,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
            extra_headers=extra_headers,
            timeout=timeout,
        )
        return cast(
            BaremetalServer,
            self.get(
                server_id,
                project_id=project_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                timeout=timeout,
            ),
        )

    def delete_and_poll(
        self,
        server_id: str,
        *,
        project_id: int | None = None,
        all_floating_ips: bool | Omit = omit,
        all_ports: bool | Omit = omit,
        floating_ip_ids: SequenceNotStr[str] | Omit = omit,
        port_ids: SequenceNotStr[str] | Omit = omit,
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
        Delete a bare metal server and wait for every task to finish.

        By default the delete keeps the ports and floating IPs of the server. Name the ones to delete with
        `port_ids` and `floating_ip_ids`, or pass `all_ports` and `all_floating_ips`.

        The helper does not support a dry run. Call `delete` with `dry_run=True` instead.
        """
        _reject_dry_run(self._client, extra_query)
        response = self.delete(
            server_id=server_id,
            project_id=project_id,
            all_floating_ips=all_floating_ips,
            all_ports=all_ports,
            floating_ip_ids=floating_ip_ids,
            port_ids=port_ids,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        self._wait_for_tasks(
            response.tasks,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
            extra_headers=extra_headers,
            timeout=timeout,
        )

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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> BaremetalRegionalServer:
        """
        Rebuild a bare metal server and wait for it to be ready. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.

        The helper reads the result through the temporary regional client, so it returns the legacy `BaremetalRegionalServer` model.
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
            timeout=timeout,
        )
        if not response.tasks:
            raise ValueError("Expected at least one task to be created")
        self._client.cloud.tasks.poll(
            response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        servers = self._client.cloud.baremetal_regional.servers.list(
            project_id=project_id,
            region_id=region_id,
            uuid=server_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if len(servers.results) != 1:
            raise ValueError(f"Server {server_id} not found")
        return servers.results[0]


class AsyncServersResourceCustomMixin:
    if TYPE_CHECKING:
        # Provided by the concrete generated resource class this mixin is
        # combined with; declared here so client-derived locals keep their
        # real types and other resource methods resolve via __getattr__.
        _client: AsyncGcore

        def __getattr__(self, name: str) -> Any: ...

    async def _wait_for_tasks(
        self,
        task_ids: List[str],
        *,
        polling_interval_seconds: int | Omit,
        polling_timeout_seconds: int | Omit,
        extra_headers: Headers | None,
        timeout: float | httpx.Timeout | None | NotGiven,
    ) -> List[Task]:
        task_ids = _require_tasks(task_ids)
        budget = _TaskBudget(self._client, polling_interval_seconds, polling_timeout_seconds)
        return [
            await self._client.cloud.tasks.poll(
                task_id=task_id,
                extra_headers=extra_headers,
                polling_interval_seconds=polling_interval_seconds,
                polling_timeout_seconds=budget.next_timeout(task_id),
                # tasks.poll passes the timeout on to tasks.get, which takes every timeout type
                timeout=cast("float | NotGiven", timeout),
            )
            for task_id in task_ids
        ]

    async def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        flavor_name: str,
        image_id: str,
        interfaces: Iterable[server_create_params.Interface],
        region_id: int,
        name: str | Omit = omit,
        password: str | Omit = omit,
        ssh_key_id: str | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        user_data: str | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BaremetalServer:
        """
        Create a bare metal server, wait for every task to finish, and return the new server.

        The helper reads the server ID from `created_resources.instances` of the tasks and calls `get` once.
        The polling timeout covers all tasks together.

        The helper does not support a dry run. Call `create` with `dry_run=True` instead.
        `extra_body` goes only to the create request.
        """
        _reject_dry_run(self._client, extra_query)
        response = await self.create(
            project_id=project_id,
            flavor_name=flavor_name,
            image_id=image_id,
            interfaces=interfaces,
            region_id=region_id,
            name=name,
            password=password,
            ssh_key_id=ssh_key_id,
            tags=tags,
            user_data=user_data,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        tasks = await self._wait_for_tasks(
            response.tasks,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
            extra_headers=extra_headers,
            timeout=timeout,
        )
        return cast(
            BaremetalServer,
            await self.get(
                _created_server_id(tasks),
                project_id=project_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                timeout=timeout,
            ),
        )

    async def update_and_poll(
        self,
        server_id: str,
        *,
        project_id: int | None = None,
        interfaces: Iterable[server_update_params.Interface] | Omit = omit,
        name: str | Omit = omit,
        tags: Optional[TagUpdateMapParam] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BaremetalServer:
        """
        Update a bare metal server, wait for every task to finish, and return the server.

        The helper waits for the tasks, not for the global read to show every change. So the returned server can
        show old data for a few seconds after the tasks finish.

        The helper does not support a dry run. Call `update` with `dry_run=True` instead.
        `extra_body` goes only to the update request.
        """
        _reject_dry_run(self._client, extra_query)
        response = await self.update(
            server_id=server_id,
            project_id=project_id,
            interfaces=interfaces,
            name=name,
            tags=tags,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        await self._wait_for_tasks(
            response.tasks,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
            extra_headers=extra_headers,
            timeout=timeout,
        )
        return cast(
            BaremetalServer,
            await self.get(
                server_id,
                project_id=project_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                timeout=timeout,
            ),
        )

    async def action_and_poll(
        self,
        server_id: str,
        *,
        project_id: int | None = None,
        action: Literal["reboot", "reboot_hard", "start", "stop"],
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BaremetalServer:
        """
        Run a power action on a bare metal server, wait for every task to finish, and return the server.

        The helper waits for the tasks, not for the global read to show every change. So the returned server can
        show old data, such as the old status, for a few seconds after the tasks finish.

        The helper does not support a dry run. Call `action` with `dry_run=True` instead.
        `extra_body` goes only to the action request.
        """
        _reject_dry_run(self._client, extra_query)
        response = await self.action(
            server_id=server_id,
            project_id=project_id,
            action=action,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        await self._wait_for_tasks(
            response.tasks,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
            extra_headers=extra_headers,
            timeout=timeout,
        )
        return cast(
            BaremetalServer,
            await self.get(
                server_id,
                project_id=project_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                timeout=timeout,
            ),
        )

    async def delete_and_poll(
        self,
        server_id: str,
        *,
        project_id: int | None = None,
        all_floating_ips: bool | Omit = omit,
        all_ports: bool | Omit = omit,
        floating_ip_ids: SequenceNotStr[str] | Omit = omit,
        port_ids: SequenceNotStr[str] | Omit = omit,
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
        Delete a bare metal server and wait for every task to finish.

        By default the delete keeps the ports and floating IPs of the server. Name the ones to delete with
        `port_ids` and `floating_ip_ids`, or pass `all_ports` and `all_floating_ips`.

        The helper does not support a dry run. Call `delete` with `dry_run=True` instead.
        """
        _reject_dry_run(self._client, extra_query)
        response = await self.delete(
            server_id=server_id,
            project_id=project_id,
            all_floating_ips=all_floating_ips,
            all_ports=all_ports,
            floating_ip_ids=floating_ip_ids,
            port_ids=port_ids,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        await self._wait_for_tasks(
            response.tasks,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
            extra_headers=extra_headers,
            timeout=timeout,
        )

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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> BaremetalRegionalServer:
        """
        Rebuild a bare metal server and wait for it to be ready. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.

        The helper reads the result through the temporary regional client, so it returns the legacy `BaremetalRegionalServer` model.
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
            timeout=timeout,
        )
        if not response.tasks:
            raise ValueError("Expected at least one task to be created")
        await self._client.cloud.tasks.poll(
            response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        servers = await self._client.cloud.baremetal_regional.servers.list(
            project_id=project_id,
            region_id=region_id,
            uuid=server_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if len(servers.results) != 1:
            raise ValueError(f"Server {server_id} not found")
        return servers.results[0]
