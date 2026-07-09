# Custom code. This file is not generated and is preserved across codegen runs.
# It isolates hand-written *_and_poll convenience methods from generated code to
# eliminate merge conflicts.

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Iterable, Optional, cast
from typing_extensions import Literal, overload

import httpx

from ...._types import NOT_GIVEN, Body, Omit, Query, Headers, NotGiven, omit
from ...._utils import required_args, maybe_transform, async_maybe_transform
from ....types.cloud import (
    instance_action_params,
    instance_create_params,
)
from ...._base_client import make_request_options
from ....types.cloud.instance import Instance
from ....types.cloud.task_id_list import TaskIDList

if TYPE_CHECKING:
    from ...._client import Gcore, AsyncGcore


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
        region_id: int | None = None,
        flavor: str,
        interfaces: Iterable[instance_create_params.Interface],
        volumes: Iterable[instance_create_params.Volume],
        allow_app_ports: bool | Omit = omit,
        configuration: Optional[Dict[str, object]] | Omit = omit,
        name: str | Omit = omit,
        name_template: str | Omit = omit,
        password: str | Omit = omit,
        security_groups: Iterable[instance_create_params.SecurityGroup] | Omit = omit,
        servergroup_id: str | Omit = omit,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Instance:
        """Create one or many instances or basic VMs and poll for the result."""
        response = self.create(
            project_id=project_id,
            region_id=region_id,
            flavor=flavor,
            interfaces=interfaces,
            volumes=volumes,
            allow_app_ports=allow_app_ports,
            configuration=configuration,
            name_template=name_template,
            name=name,
            password=password,
            security_groups=security_groups,
            servergroup_id=servergroup_id,
            ssh_key_name=ssh_key_name,
            tags=tags,
            user_data=user_data,
            username=username,
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
            or not task.created_resources.instances
            or len(task.created_resources.instances) != 1
        ):
            raise ValueError("Expected exactly one resource to be created in a task")
        return cast(
            Instance,
            self.get(
                instance_id=task.created_resources.instances[0],
                project_id=project_id,
                region_id=region_id,
                extra_headers=extra_headers,
            ),
        )

    def delete_and_poll(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        delete_floatings: bool | Omit = omit,
        floatings: str | Omit = omit,
        reserved_fixed_ips: str | Omit = omit,
        volumes: str | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete instance and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.delete(
            instance_id=instance_id,
            project_id=project_id,
            region_id=region_id,
            delete_floatings=delete_floatings,
            floatings=floatings,
            reserved_fixed_ips=reserved_fixed_ips,
            volumes=volumes,
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

    @overload
    def action_and_poll(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["start"],
        activate_profile: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Instance:
        """
        The action can be one of: start, stop, reboot, powercycle, suspend or resume.
        Suspend and resume are not available for bare metal instances.

        Args:
          action: Instance action name

          activate_profile: Used on start instance to activate Advanced DDoS profile

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def action_and_poll(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["reboot", "reboot_hard", "resume", "stop", "suspend"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Instance:
        """
        The action can be one of: start, stop, reboot, powercycle, suspend or resume.
        Suspend and resume are not available for bare metal instances.

        Args:
          action: Instance action name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["action"])
    def action_and_poll(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["start", "reboot", "reboot_hard", "resume", "stop", "suspend"],
        activate_profile: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Instance:
        """
        Perform the action on the instance and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        response = self._post(
            f"/cloud/v2/instances/{project_id}/{region_id}/{instance_id}/action",
            body=maybe_transform(
                {
                    "action": action,
                    "activate_profile": activate_profile,
                },
                instance_action_params.InstanceActionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )
        if not response.tasks:
            raise ValueError("Expected at least one task to be created")
        self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
        )
        return cast(
            Instance,
            self.get(
                instance_id=instance_id,
                project_id=project_id,
                region_id=region_id,
                extra_headers=extra_headers,
            ),
        )

    def add_to_placement_group_and_poll(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        servergroup_id: str,
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
        Put instance into the server group and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.add_to_placement_group(
            instance_id=instance_id,
            project_id=project_id,
            region_id=region_id,
            servergroup_id=servergroup_id,
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
                region_id=region_id,
                extra_headers=extra_headers,
            ),
        )

    def remove_from_placement_group_and_poll(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
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
        Remove instance from the server group and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.remove_from_placement_group(
            instance_id=instance_id,
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
        return cast(
            Instance,
            self.get(
                instance_id=instance_id,
                project_id=project_id,
                region_id=region_id,
                extra_headers=extra_headers,
            ),
        )

    def resize_and_poll(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        flavor_id: str,
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
        Change flavor of the instance and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.resize(
            instance_id=instance_id,
            project_id=project_id,
            region_id=region_id,
            flavor_id=flavor_id,
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
                region_id=region_id,
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
        region_id: int | None = None,
        flavor: str,
        interfaces: Iterable[instance_create_params.Interface],
        volumes: Iterable[instance_create_params.Volume],
        allow_app_ports: bool | Omit = omit,
        configuration: Optional[Dict[str, object]] | Omit = omit,
        name: str | Omit = omit,
        name_template: str | Omit = omit,
        password: str | Omit = omit,
        security_groups: Iterable[instance_create_params.SecurityGroup] | Omit = omit,
        servergroup_id: str | Omit = omit,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Instance:
        """Create one or many instances or basic VMs and poll for the result."""
        response = await self.create(
            project_id=project_id,
            region_id=region_id,
            flavor=flavor,
            interfaces=interfaces,
            volumes=volumes,
            allow_app_ports=allow_app_ports,
            configuration=configuration,
            name_template=name_template,
            name=name,
            password=password,
            security_groups=security_groups,
            servergroup_id=servergroup_id,
            ssh_key_name=ssh_key_name,
            tags=tags,
            user_data=user_data,
            username=username,
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
            or not task.created_resources.instances
            or len(task.created_resources.instances) != 1
        ):
            raise ValueError("Expected exactly one resource to be created in a task")
        return cast(
            Instance,
            await self.get(
                instance_id=task.created_resources.instances[0],
                project_id=project_id,
                region_id=region_id,
                extra_headers=extra_headers,
            ),
        )

    async def delete_and_poll(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        delete_floatings: bool | Omit = omit,
        floatings: str | Omit = omit,
        reserved_fixed_ips: str | Omit = omit,
        volumes: str | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete instance and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.delete(
            instance_id=instance_id,
            project_id=project_id,
            region_id=region_id,
            delete_floatings=delete_floatings,
            floatings=floatings,
            reserved_fixed_ips=reserved_fixed_ips,
            volumes=volumes,
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

    @overload
    async def action_and_poll(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["start"],
        activate_profile: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Instance:
        """
        The action can be one of: start, stop, reboot, powercycle, suspend or resume.
        Suspend and resume are not available for bare metal instances.

        Args:
          action: Instance action name

          activate_profile: Used on start instance to activate Advanced DDoS profile

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def action_and_poll(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["reboot", "reboot_hard", "resume", "stop", "suspend"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Instance:
        """
        The action can be one of: start, stop, reboot, powercycle, suspend or resume.
        Suspend and resume are not available for bare metal instances.

        Args:
          action: Instance action name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["action"])
    async def action_and_poll(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["start", "reboot", "reboot_hard", "resume", "stop", "suspend"],
        activate_profile: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Instance:
        """
        Perform the action on the instance and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        response = await self._post(
            f"/cloud/v2/instances/{project_id}/{region_id}/{instance_id}/action",
            body=await async_maybe_transform(
                {
                    "action": action,
                    "activate_profile": activate_profile,
                },
                instance_action_params.InstanceActionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )
        if not response.tasks:
            raise ValueError("Expected at least one task to be created")
        await self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
        )
        return cast(
            Instance,
            await self.get(
                instance_id=instance_id,
                project_id=project_id,
                region_id=region_id,
                extra_headers=extra_headers,
            ),
        )

    async def add_to_placement_group_and_poll(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        servergroup_id: str,
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
        Put instance into the server group and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.add_to_placement_group(
            instance_id=instance_id,
            project_id=project_id,
            region_id=region_id,
            servergroup_id=servergroup_id,
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
                region_id=region_id,
                extra_headers=extra_headers,
            ),
        )

    async def remove_from_placement_group_and_poll(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
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
        Remove instance from the server group and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.remove_from_placement_group(
            instance_id=instance_id,
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
        return cast(
            Instance,
            await self.get(
                instance_id=instance_id,
                project_id=project_id,
                region_id=region_id,
                extra_headers=extra_headers,
            ),
        )

    async def resize_and_poll(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        flavor_id: str,
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
        Change flavor of the instance and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.resize(
            instance_id=instance_id,
            project_id=project_id,
            region_id=region_id,
            flavor_id=flavor_id,
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
                region_id=region_id,
                extra_headers=extra_headers,
            ),
        )
