# Custom code. This file is not generated and is preserved across codegen runs.
# It isolates hand-written *_and_poll convenience methods from generated code to
# eliminate merge conflicts.

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Iterable, Optional, cast
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ....types.cloud import instance_create_params, instance_update_params
from ....types.cloud.instance import Instance
from ....types.cloud.tag_update_map_param import TagUpdateMapParam

if TYPE_CHECKING:
    from ...._client import Gcore, AsyncGcore

_Action = Literal["reboot", "reboot_hard", "resume", "start", "stop", "suspend"]


class InstancesResourceCustomMixin:
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
        boot_volume_id: str,
        flavor_name: str,
        interfaces: Iterable[instance_create_params.Interface],
        region_id: int,
        data_volume_ids: SequenceNotStr[str] | Omit = omit,
        name: str | Omit = omit,
        password: str | Omit = omit,
        placement_group_id: str | Omit = omit,
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
    ) -> Instance:
        """
        Create an instance, wait for the task to finish, and return the new instance. The helper waits only for the first task. To wait for other tasks, use the `tasks.poll` method.

        After the task, the helper gets the instance once and returns it.
        """
        response = self.create(
            project_id=project_id,
            boot_volume_id=boot_volume_id,
            flavor_name=flavor_name,
            interfaces=interfaces,
            region_id=region_id,
            data_volume_ids=data_volume_ids,
            name=name,
            password=password,
            placement_group_id=placement_group_id,
            ssh_key_id=ssh_key_id,
            tags=tags,
            user_data=user_data,
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
        if task.created_resources is None or not task.created_resources.instances:
            raise ValueError("Task completed but created_resources or instances is missing")
        new_instance_id = task.created_resources.instances[0]

        return cast(
            Instance,
            self.get(
                instance_id=new_instance_id,
                project_id=project_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                timeout=timeout,
            ),
        )

    def update_and_poll(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        data_volume_ids: SequenceNotStr[str] | Omit = omit,
        flavor_name: str | Omit = omit,
        interfaces: Iterable[instance_update_params.Interface] | Omit = omit,
        name: str | Omit = omit,
        placement_group_id: Optional[str] | Omit = omit,
        tags: Optional[TagUpdateMapParam] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Instance:
        """
        Update an instance, wait for the task to finish, and return the instance. The helper waits only for the first task. To wait for other tasks, use the `tasks.poll` method.

        If the API creates no task, the helper returns the instance at once.

        After the task, the helper gets the instance once and returns it.
        """
        response = self.update(
            instance_id=instance_id,
            project_id=project_id,
            data_volume_ids=data_volume_ids,
            flavor_name=flavor_name,
            interfaces=interfaces,
            name=name,
            placement_group_id=placement_group_id,
            tags=tags,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )

        def get() -> Instance:
            return cast(
                Instance,
                self.get(
                    instance_id=instance_id,
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

    def action_and_poll(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        action: _Action,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Instance:
        """
        Run a power action on an instance, wait for the task to finish, and return the instance. The helper waits only for the first task. To wait for other tasks, use the `tasks.poll` method.

        After the task, the helper gets the instance once and returns it.
        """
        response = self.action(
            instance_id=instance_id,
            project_id=project_id,
            action=action,
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

        def get() -> Instance:
            return cast(
                Instance,
                self.get(
                    instance_id=instance_id,
                    project_id=project_id,
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    timeout=timeout,
                ),
            )

        return get()

    def delete_and_poll(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        all_floating_ips: bool | Omit = omit,
        all_ports: bool | Omit = omit,
        all_volumes: bool | Omit = omit,
        floating_ip_ids: SequenceNotStr[str] | Omit = omit,
        port_ids: SequenceNotStr[str] | Omit = omit,
        volume_ids: SequenceNotStr[str] | Omit = omit,
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
        Delete an instance and wait for the task to finish. The helper waits only for the first task. To wait for other tasks, use the `tasks.poll` method.
        """
        response = self.delete(
            instance_id=instance_id,
            project_id=project_id,
            all_floating_ips=all_floating_ips,
            all_ports=all_ports,
            all_volumes=all_volumes,
            floating_ip_ids=floating_ip_ids,
            port_ids=port_ids,
            volume_ids=volume_ids,
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

    def rebuild_and_poll(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        image_id: str | Omit = omit,
        ssh_key_name: Optional[str] | Omit = omit,
        user_data: str | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Instance:
        """
        Rebuild the instance and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.rebuild(
            instance_id=instance_id,
            project_id=project_id,
            region_id=region_id,
            image_id=image_id,
            ssh_key_name=ssh_key_name,
            user_data=user_data,
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
            Instance,
            self.get(
                instance_id=instance_id,
                project_id=project_id,
                extra_headers=extra_headers,
            ),
        )


class AsyncInstancesResourceCustomMixin:
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
        boot_volume_id: str,
        flavor_name: str,
        interfaces: Iterable[instance_create_params.Interface],
        region_id: int,
        data_volume_ids: SequenceNotStr[str] | Omit = omit,
        name: str | Omit = omit,
        password: str | Omit = omit,
        placement_group_id: str | Omit = omit,
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
    ) -> Instance:
        """
        Create an instance, wait for the task to finish, and return the new instance. The helper waits only for the first task. To wait for other tasks, use the `tasks.poll` method.

        After the task, the helper gets the instance once and returns it.
        """
        response = await self.create(
            project_id=project_id,
            boot_volume_id=boot_volume_id,
            flavor_name=flavor_name,
            interfaces=interfaces,
            region_id=region_id,
            data_volume_ids=data_volume_ids,
            name=name,
            password=password,
            placement_group_id=placement_group_id,
            ssh_key_id=ssh_key_id,
            tags=tags,
            user_data=user_data,
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
        if task.created_resources is None or not task.created_resources.instances:
            raise ValueError("Task completed but created_resources or instances is missing")
        new_instance_id = task.created_resources.instances[0]

        return cast(
            Instance,
            await self.get(
                instance_id=new_instance_id,
                project_id=project_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                timeout=timeout,
            ),
        )

    async def update_and_poll(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        data_volume_ids: SequenceNotStr[str] | Omit = omit,
        flavor_name: str | Omit = omit,
        interfaces: Iterable[instance_update_params.Interface] | Omit = omit,
        name: str | Omit = omit,
        placement_group_id: Optional[str] | Omit = omit,
        tags: Optional[TagUpdateMapParam] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Instance:
        """
        Update an instance, wait for the task to finish, and return the instance. The helper waits only for the first task. To wait for other tasks, use the `tasks.poll` method.

        If the API creates no task, the helper returns the instance at once.

        After the task, the helper gets the instance once and returns it.
        """
        response = await self.update(
            instance_id=instance_id,
            project_id=project_id,
            data_volume_ids=data_volume_ids,
            flavor_name=flavor_name,
            interfaces=interfaces,
            name=name,
            placement_group_id=placement_group_id,
            tags=tags,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )

        async def get() -> Instance:
            return cast(
                Instance,
                await self.get(
                    instance_id=instance_id,
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

    async def action_and_poll(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        action: _Action,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Instance:
        """
        Run a power action on an instance, wait for the task to finish, and return the instance. The helper waits only for the first task. To wait for other tasks, use the `tasks.poll` method.

        After the task, the helper gets the instance once and returns it.
        """
        response = await self.action(
            instance_id=instance_id,
            project_id=project_id,
            action=action,
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

        async def get() -> Instance:
            return cast(
                Instance,
                await self.get(
                    instance_id=instance_id,
                    project_id=project_id,
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    timeout=timeout,
                ),
            )

        return await get()

    async def delete_and_poll(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        all_floating_ips: bool | Omit = omit,
        all_ports: bool | Omit = omit,
        all_volumes: bool | Omit = omit,
        floating_ip_ids: SequenceNotStr[str] | Omit = omit,
        port_ids: SequenceNotStr[str] | Omit = omit,
        volume_ids: SequenceNotStr[str] | Omit = omit,
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
        Delete an instance and wait for the task to finish. The helper waits only for the first task. To wait for other tasks, use the `tasks.poll` method.
        """
        response = await self.delete(
            instance_id=instance_id,
            project_id=project_id,
            all_floating_ips=all_floating_ips,
            all_ports=all_ports,
            all_volumes=all_volumes,
            floating_ip_ids=floating_ip_ids,
            port_ids=port_ids,
            volume_ids=volume_ids,
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

    async def rebuild_and_poll(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        image_id: str | Omit = omit,
        ssh_key_name: Optional[str] | Omit = omit,
        user_data: str | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Instance:
        """
        Rebuild the instance and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.rebuild(
            instance_id=instance_id,
            project_id=project_id,
            region_id=region_id,
            image_id=image_id,
            ssh_key_name=ssh_key_name,
            user_data=user_data,
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
            Instance,
            await self.get(
                instance_id=instance_id,
                project_id=project_id,
                extra_headers=extra_headers,
            ),
        )
