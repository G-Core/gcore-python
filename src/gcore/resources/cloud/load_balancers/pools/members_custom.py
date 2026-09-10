# Custom code. This file is not generated and is preserved across codegen runs.
# It isolates hand-written *_and_poll convenience methods from generated code to
# eliminate merge conflicts.

from __future__ import annotations

from typing import TYPE_CHECKING, Any, List, Iterable, Optional, cast

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .....types.cloud.member import Member
from .....types.cloud.load_balancers.pools import member_replace_params

if TYPE_CHECKING:
    from ....._client import Gcore, AsyncGcore


class MembersResourceCustomMixin:
    if TYPE_CHECKING:
        # Provided by the concrete generated resource class this mixin is
        # combined with; declared here so client-derived locals keep their
        # real types and other resource methods resolve via __getattr__.
        _client: Gcore

        def __getattr__(self, name: str) -> Any: ...

    def create_and_poll(
        self,
        pool_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        address: str,
        protocol_port: int,
        admin_state_up: bool | Omit = omit,
        backup: bool | Omit = omit,
        instance_id: Optional[str] | Omit = omit,
        monitor_address: Optional[str] | Omit = omit,
        monitor_port: Optional[int] | Omit = omit,
        subnet_id: Optional[str] | Omit = omit,
        weight: int | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Member:
        """
        Create pool member and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.create(
            pool_id=pool_id,
            project_id=project_id,
            region_id=region_id,
            address=address,
            protocol_port=protocol_port,
            admin_state_up=admin_state_up,
            backup=backup,
            instance_id=instance_id,
            monitor_address=monitor_address,
            monitor_port=monitor_port,
            subnet_id=subnet_id,
            weight=weight,
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
        if not task.created_resources or not task.created_resources.members or len(task.created_resources.members) != 1:
            raise ValueError("Expected exactly one resource to be created in a task")
        return cast(
            Member,
            self.get(
                member_id=task.created_resources.members[0],
                project_id=project_id,
                region_id=region_id,
                pool_id=pool_id,
                extra_headers=extra_headers,
                timeout=timeout,
            ),
        )

    def update_and_poll(
        self,
        member_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        pool_id: str,
        admin_state_up: bool | Omit = omit,
        backup: bool | Omit = omit,
        monitor_address: Optional[str] | Omit = omit,
        monitor_port: Optional[int] | Omit = omit,
        weight: int | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Member:
        """
        Update pool member and poll for the result. A request that changes nothing creates no task, in which case the member is returned as-is. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.update(
            member_id=member_id,
            project_id=project_id,
            region_id=region_id,
            pool_id=pool_id,
            admin_state_up=admin_state_up,
            backup=backup,
            monitor_address=monitor_address,
            monitor_port=monitor_port,
            weight=weight,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if response.tasks:
            self._client.cloud.tasks.poll(
                task_id=response.tasks[0],
                extra_headers=extra_headers,
                polling_interval_seconds=polling_interval_seconds,
                polling_timeout_seconds=polling_timeout_seconds,
            )
        return cast(
            Member,
            self.get(
                member_id=member_id,
                project_id=project_id,
                region_id=region_id,
                pool_id=pool_id,
                extra_headers=extra_headers,
                timeout=timeout,
            ),
        )

    def replace_and_poll(
        self,
        pool_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        body: Iterable[member_replace_params.Body] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> List[Member]:
        """
        Replace the pool's entire member list, poll for the result and return the resulting members.

        The API handles a replace as a single pool patch: it returns one task when the member set
        changes and an empty task list when the requested set already matches (members are matched
        by address and port), so no task is a completed no-op rather than an error.
        """
        response = self.replace(
            pool_id=pool_id,
            project_id=project_id,
            region_id=region_id,
            body=body,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        # `self.replace` resolves through the mixin's __getattr__, so pin the element type.
        for task_id in cast(List[str], response.tasks or []):
            self._client.cloud.tasks.poll(
                task_id=task_id,
                extra_headers=extra_headers,
                polling_interval_seconds=polling_interval_seconds,
                polling_timeout_seconds=polling_timeout_seconds,
            )
        page = self.list(
            pool_id=pool_id,
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
            timeout=timeout,
        )
        return list(page.results)

    def delete_and_poll(
        self,
        member_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        pool_id: str,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> None:
        """
        Delete pool member and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.delete(
            member_id=member_id,
            project_id=project_id,
            region_id=region_id,
            pool_id=pool_id,
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


class AsyncMembersResourceCustomMixin:
    if TYPE_CHECKING:
        # Provided by the concrete generated resource class this mixin is
        # combined with; declared here so client-derived locals keep their
        # real types and other resource methods resolve via __getattr__.
        _client: AsyncGcore

        def __getattr__(self, name: str) -> Any: ...

    async def create_and_poll(
        self,
        pool_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        address: str,
        protocol_port: int,
        admin_state_up: bool | Omit = omit,
        backup: bool | Omit = omit,
        instance_id: Optional[str] | Omit = omit,
        monitor_address: Optional[str] | Omit = omit,
        monitor_port: Optional[int] | Omit = omit,
        subnet_id: Optional[str] | Omit = omit,
        weight: int | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Member:
        """
        Create pool member and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.create(
            pool_id=pool_id,
            project_id=project_id,
            region_id=region_id,
            address=address,
            protocol_port=protocol_port,
            admin_state_up=admin_state_up,
            backup=backup,
            instance_id=instance_id,
            monitor_address=monitor_address,
            monitor_port=monitor_port,
            subnet_id=subnet_id,
            weight=weight,
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
        if not task.created_resources or not task.created_resources.members or len(task.created_resources.members) != 1:
            raise ValueError("Expected exactly one resource to be created in a task")
        return cast(
            Member,
            await self.get(
                member_id=task.created_resources.members[0],
                project_id=project_id,
                region_id=region_id,
                pool_id=pool_id,
                extra_headers=extra_headers,
                timeout=timeout,
            ),
        )

    async def update_and_poll(
        self,
        member_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        pool_id: str,
        admin_state_up: bool | Omit = omit,
        backup: bool | Omit = omit,
        monitor_address: Optional[str] | Omit = omit,
        monitor_port: Optional[int] | Omit = omit,
        weight: int | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Member:
        """
        Update pool member and poll for the result. A request that changes nothing creates no task, in which case the member is returned as-is. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.update(
            member_id=member_id,
            project_id=project_id,
            region_id=region_id,
            pool_id=pool_id,
            admin_state_up=admin_state_up,
            backup=backup,
            monitor_address=monitor_address,
            monitor_port=monitor_port,
            weight=weight,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if response.tasks:
            await self._client.cloud.tasks.poll(
                task_id=response.tasks[0],
                extra_headers=extra_headers,
                polling_interval_seconds=polling_interval_seconds,
                polling_timeout_seconds=polling_timeout_seconds,
            )
        return cast(
            Member,
            await self.get(
                member_id=member_id,
                project_id=project_id,
                region_id=region_id,
                pool_id=pool_id,
                extra_headers=extra_headers,
                timeout=timeout,
            ),
        )

    async def replace_and_poll(
        self,
        pool_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        body: Iterable[member_replace_params.Body] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> List[Member]:
        """
        Replace the pool's entire member list, poll for the result and return the resulting members.

        The API handles a replace as a single pool patch: it returns one task when the member set
        changes and an empty task list when the requested set already matches (members are matched
        by address and port), so no task is a completed no-op rather than an error.
        """
        response = await self.replace(
            pool_id=pool_id,
            project_id=project_id,
            region_id=region_id,
            body=body,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        # `self.replace` resolves through the mixin's __getattr__, so pin the element type.
        for task_id in cast(List[str], response.tasks or []):
            await self._client.cloud.tasks.poll(
                task_id=task_id,
                extra_headers=extra_headers,
                polling_interval_seconds=polling_interval_seconds,
                polling_timeout_seconds=polling_timeout_seconds,
            )
        page = await self.list(
            pool_id=pool_id,
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
            timeout=timeout,
        )
        return list(page.results)

    async def delete_and_poll(
        self,
        member_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        pool_id: str,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> None:
        """
        Delete pool member and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.delete(
            member_id=member_id,
            project_id=project_id,
            region_id=region_id,
            pool_id=pool_id,
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
