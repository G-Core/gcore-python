from __future__ import annotations

import time
from typing import TYPE_CHECKING, Any, Union, Iterator, Sequence, cast
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import is_given
from ...types.cloud.task import Task
from ...types.cloud.placement_group import PlacementGroup

if TYPE_CHECKING:
    from ..._client import Gcore, AsyncGcore

_Policy = Literal["affinity", "anti-affinity", "soft-affinity", "soft-anti-affinity"]
_Timeout = Union[float, httpx.Timeout, None, NotGiven]


def _is_true(value: object) -> bool:
    if isinstance(value, (list, tuple)):
        return any(_is_true(item) for item in cast("Sequence[object]", value))
    return str(value).strip().lower() in {"1", "on", "t", "true", "y", "yes"}


def _reject_dry_run(client: Gcore | AsyncGcore, extra_query: Query | None) -> None:
    """Raise before any request when the client or request asks for a dry run."""
    query = {**client.default_query, **(extra_query or {})}
    if _is_true(query.get("dry_run")):
        raise ValueError("Polling helpers do not support dry_run; use create or delete with dry_run=True.")


def _created_group_id(tasks: Sequence[Task]) -> str:
    ids: set[str] = set()
    for task in tasks:
        if task.created_resources is not None:
            ids.update(group_id for group_id in (task.created_resources.servergroups or []) if group_id)
    if not ids:
        raise ValueError("Expected a placement group ID in created_resources.servergroups, got none")
    if len(ids) > 1:
        raise ValueError("Expected one placement group ID in created_resources.servergroups, got multiple IDs")
    return ids.pop()


class _Polling:
    def __init__(self, client: Gcore | AsyncGcore, interval: int | Omit, timeout: int | Omit) -> None:
        self.interval = max(1, interval if is_given(interval) else cast(int, client.polling_interval_seconds))
        self.timeout = timeout if is_given(timeout) else cast(int, client.polling_timeout_seconds)

    def task_timeouts(self, task_ids: Sequence[str]) -> Iterator[tuple[str, int]]:
        """Yield each task with its remaining share of the polling timeout."""
        if not task_ids:
            raise ValueError("Expected at least one placement group task")
        deadline = time.monotonic() + self.timeout
        for index, task_id in enumerate(task_ids):
            remaining = int(deadline - time.monotonic()) if index else self.timeout
            if index and remaining <= self.interval:
                raise TimeoutError(f"Timed out waiting for task {task_id}")
            yield task_id, remaining


class PlacementGroupsResourceCustomMixin:
    if TYPE_CHECKING:
        _client: Gcore

        def __getattr__(self, name: str) -> Any: ...

    def _poll_placement_group_tasks(
        self,
        task_ids: Sequence[str],
        polling: _Polling,
        extra_headers: Headers | None,
        timeout: _Timeout,
    ) -> list[Task]:
        return [
            self._client.cloud.tasks.poll(
                task_id,
                polling_interval_seconds=polling.interval,
                polling_timeout_seconds=task_timeout,
                extra_headers=extra_headers,
                timeout=cast("float | NotGiven", timeout),
            )
            for task_id, task_timeout in polling.task_timeouts(task_ids)
        ]

    def create_and_poll(
        self,
        *,
        name: str,
        policy: _Policy,
        region_id: int,
        project_id: int | None = None,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: _Timeout = not_given,
    ) -> PlacementGroup:
        """Create a placement group and wait for all tasks within one polling budget.

        Create and the final GET use the client's ordinary retry policy. The
        finished tasks must report exactly one distinct placement group ID in
        `created_resources.servergroups`. After all tasks finish, the helper
        performs one GET and returns its result or propagates its error.

        This helper does not support dry runs. Use `create` with
        `dry_run=True` instead.
        """
        _reject_dry_run(self._client, extra_query)
        response = self.create(
            name=name,
            policy=policy,
            region_id=region_id,
            project_id=project_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        polling = _Polling(self._client, polling_interval_seconds, polling_timeout_seconds)
        group_id = _created_group_id(self._poll_placement_group_tasks(response.tasks, polling, extra_headers, timeout))
        return cast(
            PlacementGroup,
            self.get(
                group_id,
                project_id=project_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                timeout=timeout,
            ),
        )

    def delete_and_poll(
        self,
        placement_group_id: str,
        *,
        project_id: int | None = None,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: _Timeout = not_given,
    ) -> None:
        """Delete a placement group and wait for all tasks within one polling budget.

        This helper does not support dry runs. Use `delete` with
        `dry_run=True` instead.
        """
        _reject_dry_run(self._client, extra_query)
        response = self._client.cloud.placement_groups.delete(
            placement_group_id,
            project_id=project_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        polling = _Polling(self._client, polling_interval_seconds, polling_timeout_seconds)
        self._poll_placement_group_tasks(response.tasks, polling, extra_headers, timeout)


class AsyncPlacementGroupsResourceCustomMixin:
    if TYPE_CHECKING:
        _client: AsyncGcore

        def __getattr__(self, name: str) -> Any: ...

    async def _poll_placement_group_tasks(
        self,
        task_ids: Sequence[str],
        polling: _Polling,
        extra_headers: Headers | None,
        timeout: _Timeout,
    ) -> list[Task]:
        return [
            await self._client.cloud.tasks.poll(
                task_id,
                polling_interval_seconds=polling.interval,
                polling_timeout_seconds=task_timeout,
                extra_headers=extra_headers,
                timeout=cast("float | NotGiven", timeout),
            )
            for task_id, task_timeout in polling.task_timeouts(task_ids)
        ]

    async def create_and_poll(
        self,
        *,
        name: str,
        policy: _Policy,
        region_id: int,
        project_id: int | None = None,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: _Timeout = not_given,
    ) -> PlacementGroup:
        """Create a placement group and wait for all tasks within one polling budget.

        Create and the final GET use the client's ordinary retry policy. The
        finished tasks must report exactly one distinct placement group ID in
        `created_resources.servergroups`. After all tasks finish, the helper
        performs one GET and returns its result or propagates its error.

        This helper does not support dry runs. Use `create` with
        `dry_run=True` instead.
        """
        _reject_dry_run(self._client, extra_query)
        response = await self.create(
            name=name,
            policy=policy,
            region_id=region_id,
            project_id=project_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        polling = _Polling(self._client, polling_interval_seconds, polling_timeout_seconds)
        group_id = _created_group_id(
            await self._poll_placement_group_tasks(response.tasks, polling, extra_headers, timeout)
        )
        return cast(
            PlacementGroup,
            await self.get(
                group_id,
                project_id=project_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                timeout=timeout,
            ),
        )

    async def delete_and_poll(
        self,
        placement_group_id: str,
        *,
        project_id: int | None = None,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: _Timeout = not_given,
    ) -> None:
        """Delete a placement group and wait for all tasks within one polling budget.

        This helper does not support dry runs. Use `delete` with
        `dry_run=True` instead.
        """
        _reject_dry_run(self._client, extra_query)
        response = await self._client.cloud.placement_groups.delete(
            placement_group_id,
            project_id=project_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        polling = _Polling(self._client, polling_interval_seconds, polling_timeout_seconds)
        await self._poll_placement_group_tasks(response.tasks, polling, extra_headers, timeout)
