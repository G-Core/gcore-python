# Custom code. This file is not generated and is preserved across codegen runs.
# It isolates hand-written *_and_poll convenience methods from generated code to
# eliminate merge conflicts.

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Iterable, Optional, cast
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...types.cloud import port_create_params, port_update_params
from ...types.cloud.port import Port
from ...types.cloud.floating_ip import FloatingIP
from ...types.cloud.tag_update_map_param import TagUpdateMapParam

if TYPE_CHECKING:
    from ..._client import Gcore, AsyncGcore


class PortsResourceCustomMixin:
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
        region_id: int,
        allowed_address_pairs: Iterable[port_create_params.AllowedAddressPair] | Omit = omit,
        ip_assignments: Iterable[port_create_params.IPAssignment] | Omit = omit,
        network_id: str | Omit = omit,
        port_security_enabled: bool | Omit = omit,
        security_group_ids: SequenceNotStr[str] | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Port:
        """
        Create a port, wait for the task to finish, and return the new port. The helper waits only for the first task. To wait for other tasks, use the `tasks.poll` method.
        """
        response = self.create(
            project_id=project_id,
            region_id=region_id,
            allowed_address_pairs=allowed_address_pairs,
            ip_assignments=ip_assignments,
            network_id=network_id,
            port_security_enabled=port_security_enabled,
            security_group_ids=security_group_ids,
            tags=tags,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks:
            raise ValueError("Expected at least one task to be created")
        task = self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        if task.created_resources is None or not task.created_resources.ports:
            raise ValueError("Task completed but created_resources or ports is missing")
        new_port_id = task.created_resources.ports[0]
        return cast(
            Port,
            self.get(
                port_id=new_port_id,
                project_id=project_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                timeout=timeout,
            ),
        )

    def update_and_poll(
        self,
        port_id: str,
        *,
        project_id: int | None = None,
        allowed_address_pairs: Iterable[port_update_params.AllowedAddressPair] | Omit = omit,
        ip_assignments: Iterable[port_update_params.IPAssignment] | Omit = omit,
        port_security_enabled: bool | Omit = omit,
        security_group_ids: SequenceNotStr[str] | Omit = omit,
        tags: Optional[TagUpdateMapParam] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Port:
        """
        Update a port, wait for the task to finish, and return the port. The helper waits only for the first task. To wait for other tasks, use the `tasks.poll` method.

        If nothing changes, the API creates no task, and the helper returns the port at once.

        After the task, the helper gets the port once and returns it.
        """
        response = self.update(
            port_id=port_id,
            project_id=project_id,
            allowed_address_pairs=allowed_address_pairs,
            ip_assignments=ip_assignments,
            port_security_enabled=port_security_enabled,
            security_group_ids=security_group_ids,
            tags=tags,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )

        def get() -> Port:
            return cast(
                Port,
                self.get(
                    port_id=port_id,
                    project_id=project_id,
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    timeout=timeout,
                ),
            )

        if not response.tasks:
            return get()
        self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        return get()

    def delete_and_poll(
        self,
        port_id: str,
        *,
        project_id: int | None = None,
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
        Delete a port and wait for the task to finish. The helper waits only for the first task. To wait for other tasks, use the `tasks.poll` method.
        """
        response = self.delete(
            port_id=port_id,
            project_id=project_id,
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

    def convert_and_poll(
        self,
        port_id: str,
        *,
        project_id: int | None = None,
        target_type: Literal["floating_ip"],
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FloatingIP:
        """
        Convert a port to a floating IP, wait for the task to finish, and return the new floating IP. The task deletes the port, so the port ID is not valid after the call.

        Floating IPs have no global view route, so the helper gets the floating IP with `floating_ips.get` in the region of the task.
        """
        response = self.convert(
            port_id=port_id,
            project_id=project_id,
            target_type=target_type,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks:
            raise ValueError("Expected at least one task to be created")
        task = self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        if task.created_resources is None or not task.created_resources.floatingips:
            raise ValueError("Task completed but created_resources or floatingips is missing")
        if task.region_id is None:
            raise ValueError(f"Task {task.id} has no region ID")
        # the region comes from the task, not from the client, because the port route has no region
        return self._client.cloud.floating_ips.get(
            floating_ip_id=task.created_resources.floatingips[0],
            project_id=project_id,
            region_id=task.region_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )


class AsyncPortsResourceCustomMixin:
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
        region_id: int,
        allowed_address_pairs: Iterable[port_create_params.AllowedAddressPair] | Omit = omit,
        ip_assignments: Iterable[port_create_params.IPAssignment] | Omit = omit,
        network_id: str | Omit = omit,
        port_security_enabled: bool | Omit = omit,
        security_group_ids: SequenceNotStr[str] | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Port:
        """
        Create a port, wait for the task to finish, and return the new port. The helper waits only for the first task. To wait for other tasks, use the `tasks.poll` method.
        """
        response = await self.create(
            project_id=project_id,
            region_id=region_id,
            allowed_address_pairs=allowed_address_pairs,
            ip_assignments=ip_assignments,
            network_id=network_id,
            port_security_enabled=port_security_enabled,
            security_group_ids=security_group_ids,
            tags=tags,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks:
            raise ValueError("Expected at least one task to be created")
        task = await self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        if task.created_resources is None or not task.created_resources.ports:
            raise ValueError("Task completed but created_resources or ports is missing")
        new_port_id = task.created_resources.ports[0]

        return cast(
            Port,
            await self.get(
                port_id=new_port_id,
                project_id=project_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                timeout=timeout,
            ),
        )

    async def update_and_poll(
        self,
        port_id: str,
        *,
        project_id: int | None = None,
        allowed_address_pairs: Iterable[port_update_params.AllowedAddressPair] | Omit = omit,
        ip_assignments: Iterable[port_update_params.IPAssignment] | Omit = omit,
        port_security_enabled: bool | Omit = omit,
        security_group_ids: SequenceNotStr[str] | Omit = omit,
        tags: Optional[TagUpdateMapParam] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Port:
        """
        Update a port, wait for the task to finish, and return the port. The helper waits only for the first task. To wait for other tasks, use the `tasks.poll` method.

        If nothing changes, the API creates no task, and the helper returns the port at once.

        After the task, the helper gets the port once and returns it.
        """
        response = await self.update(
            port_id=port_id,
            project_id=project_id,
            allowed_address_pairs=allowed_address_pairs,
            ip_assignments=ip_assignments,
            port_security_enabled=port_security_enabled,
            security_group_ids=security_group_ids,
            tags=tags,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )

        async def get() -> Port:
            return cast(
                Port,
                await self.get(
                    port_id=port_id,
                    project_id=project_id,
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    timeout=timeout,
                ),
            )

        if not response.tasks:
            return await get()
        await self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        return await get()

    async def delete_and_poll(
        self,
        port_id: str,
        *,
        project_id: int | None = None,
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
        Delete a port and wait for the task to finish. The helper waits only for the first task. To wait for other tasks, use the `tasks.poll` method.
        """
        response = await self.delete(
            port_id=port_id,
            project_id=project_id,
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

    async def convert_and_poll(
        self,
        port_id: str,
        *,
        project_id: int | None = None,
        target_type: Literal["floating_ip"],
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FloatingIP:
        """
        Convert a port to a floating IP, wait for the task to finish, and return the new floating IP. The task deletes the port, so the port ID is not valid after the call.

        Floating IPs have no global view route, so the helper gets the floating IP with `floating_ips.get` in the region of the task.
        """
        response = await self.convert(
            port_id=port_id,
            project_id=project_id,
            target_type=target_type,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks:
            raise ValueError("Expected at least one task to be created")
        task = await self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        if task.created_resources is None or not task.created_resources.floatingips:
            raise ValueError("Task completed but created_resources or floatingips is missing")
        if task.region_id is None:
            raise ValueError(f"Task {task.id} has no region ID")
        # the region comes from the task, not from the client, because the port route has no region
        return await self._client.cloud.floating_ips.get(
            floating_ip_id=task.created_resources.floatingips[0],
            project_id=project_id,
            region_id=task.region_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
