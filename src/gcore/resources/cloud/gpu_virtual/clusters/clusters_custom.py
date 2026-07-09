# Custom code. This file is not generated and is preserved across codegen runs.
# It isolates hand-written *_and_poll convenience methods from generated code to
# eliminate merge conflicts.

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, cast
from typing_extensions import Literal, overload

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ....._utils import path_template, required_args, maybe_transform, async_maybe_transform
from ....._base_client import make_request_options
from .....types.cloud.gpu_virtual import (
    cluster_action_params,
    cluster_create_params,
)
from .....types.cloud.task_id_list import TaskIDList
from .....types.cloud.gpu_virtual.gpu_virtual_cluster import GPUVirtualCluster

if TYPE_CHECKING:
    from ....._client import Gcore, AsyncGcore


class ClustersResourceCustomMixin:
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
        name: str,
        servers_count: int,
        servers_settings: cluster_create_params.ServersSettings,
        tags: Dict[str, str] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GPUVirtualCluster:
        """
        Create a virtual GPU cluster and wait for it to be ready.
        """
        response = self.create(
            project_id=project_id,
            region_id=region_id,
            flavor=flavor,
            name=name,
            servers_count=servers_count,
            servers_settings=servers_settings,
            tags=tags,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks or len(response.tasks) != 1:
            raise ValueError("Expected exactly one task to be created")
        task = self._client.cloud.tasks.poll(
            response.tasks[0],
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        if not task.created_resources or not task.created_resources.clusters:
            raise ValueError("No cluster was created")
        cluster_id = task.created_resources.clusters[0]
        return cast(
            GPUVirtualCluster,
            self.get(
                cluster_id=cluster_id,
                project_id=project_id,
                region_id=region_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
        )

    def delete_and_poll(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        all_floating_ips: bool | Omit = omit,
        all_reserved_fixed_ips: bool | Omit = omit,
        all_volumes: bool | Omit = omit,
        floating_ip_ids: SequenceNotStr[str] | Omit = omit,
        reserved_fixed_ip_ids: SequenceNotStr[str] | Omit = omit,
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
        Delete a virtual GPU cluster and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.delete(
            cluster_id=cluster_id,
            project_id=project_id,
            region_id=region_id,
            all_floating_ips=all_floating_ips,
            all_reserved_fixed_ips=all_reserved_fixed_ips,
            all_volumes=all_volumes,
            floating_ip_ids=floating_ip_ids,
            reserved_fixed_ip_ids=reserved_fixed_ip_ids,
            volume_ids=volume_ids,
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

    @overload
    def action_and_poll(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["start"],
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GPUVirtualCluster:
        """Perform an action on a virtual GPU cluster and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method."""
        ...

    @overload
    def action_and_poll(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["stop"],
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GPUVirtualCluster:
        """Perform an action on a virtual GPU cluster and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method."""
        ...

    @overload
    def action_and_poll(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["soft_reboot"],
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GPUVirtualCluster:
        """Perform an action on a virtual GPU cluster and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method."""
        ...

    @overload
    def action_and_poll(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["hard_reboot"],
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GPUVirtualCluster:
        """Perform an action on a virtual GPU cluster and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method."""
        ...

    @overload
    def action_and_poll(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["resize"],
        servers_count: int,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GPUVirtualCluster:
        """Perform an action on a virtual GPU cluster and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method."""
        ...

    @required_args(["action"], ["action", "servers_count"])
    def action_and_poll(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["start"]
        | Literal["stop"]
        | Literal["soft_reboot"]
        | Literal["hard_reboot"]
        | Literal["resize"],
        servers_count: int | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GPUVirtualCluster:
        """
        Perform an action on a virtual GPU cluster and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not cluster_id:
            raise ValueError(f"Expected a non-empty value for `cluster_id` but received {cluster_id!r}")
        response = self._post(
            path_template(
                "/cloud/v3/gpu/virtual/{project_id}/{region_id}/clusters/{cluster_id}/action",
                project_id=project_id,
                region_id=region_id,
                cluster_id=cluster_id,
            ),
            body=maybe_transform(
                {
                    "action": action,
                    "servers_count": servers_count,
                },
                cluster_action_params.ClusterActionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )
        if not response.tasks:
            raise ValueError("Expected at least one task to be created")
        self._client.cloud.tasks.poll(
            response.tasks[0],
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        return cast(
            GPUVirtualCluster,
            self.get(
                cluster_id=cluster_id,
                project_id=project_id,
                region_id=region_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
        )


class AsyncClustersResourceCustomMixin:
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
        name: str,
        servers_count: int,
        servers_settings: cluster_create_params.ServersSettings,
        tags: Dict[str, str] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GPUVirtualCluster:
        """
        Create a virtual GPU cluster and wait for it to be ready.
        """
        response = await self.create(
            project_id=project_id,
            region_id=region_id,
            flavor=flavor,
            name=name,
            servers_count=servers_count,
            servers_settings=servers_settings,
            tags=tags,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks or len(response.tasks) != 1:
            raise ValueError("Expected exactly one task to be created")
        task = await self._client.cloud.tasks.poll(
            response.tasks[0],
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        if not task.created_resources or not task.created_resources.clusters:
            raise ValueError("No cluster was created")
        cluster_id = task.created_resources.clusters[0]
        return cast(
            GPUVirtualCluster,
            await self.get(
                cluster_id=cluster_id,
                project_id=project_id,
                region_id=region_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
        )

    async def delete_and_poll(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        all_floating_ips: bool | Omit = omit,
        all_reserved_fixed_ips: bool | Omit = omit,
        all_volumes: bool | Omit = omit,
        floating_ip_ids: SequenceNotStr[str] | Omit = omit,
        reserved_fixed_ip_ids: SequenceNotStr[str] | Omit = omit,
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
        Delete a virtual GPU cluster and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.delete(
            cluster_id=cluster_id,
            project_id=project_id,
            region_id=region_id,
            all_floating_ips=all_floating_ips,
            all_reserved_fixed_ips=all_reserved_fixed_ips,
            all_volumes=all_volumes,
            floating_ip_ids=floating_ip_ids,
            reserved_fixed_ip_ids=reserved_fixed_ip_ids,
            volume_ids=volume_ids,
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

    @overload
    async def action_and_poll(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["start"],
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GPUVirtualCluster:
        """Perform an action on a virtual GPU cluster and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method."""
        ...

    @overload
    async def action_and_poll(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["stop"],
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GPUVirtualCluster:
        """Perform an action on a virtual GPU cluster and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method."""
        ...

    @overload
    async def action_and_poll(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["soft_reboot"],
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GPUVirtualCluster:
        """Perform an action on a virtual GPU cluster and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method."""
        ...

    @overload
    async def action_and_poll(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["hard_reboot"],
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GPUVirtualCluster:
        """Perform an action on a virtual GPU cluster and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method."""
        ...

    @overload
    async def action_and_poll(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["resize"],
        servers_count: int,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GPUVirtualCluster:
        """Perform an action on a virtual GPU cluster and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method."""
        ...

    @required_args(["action"], ["action", "servers_count"])
    async def action_and_poll(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["start"]
        | Literal["stop"]
        | Literal["soft_reboot"]
        | Literal["hard_reboot"]
        | Literal["resize"],
        servers_count: int | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GPUVirtualCluster:
        """
        Perform an action on a virtual GPU cluster and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not cluster_id:
            raise ValueError(f"Expected a non-empty value for `cluster_id` but received {cluster_id!r}")
        response = await self._post(
            path_template(
                "/cloud/v3/gpu/virtual/{project_id}/{region_id}/clusters/{cluster_id}/action",
                project_id=project_id,
                region_id=region_id,
                cluster_id=cluster_id,
            ),
            body=await async_maybe_transform(
                {
                    "action": action,
                    "servers_count": servers_count,
                },
                cluster_action_params.ClusterActionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )
        if not response.tasks:
            raise ValueError("Expected at least one task to be created")
        await self._client.cloud.tasks.poll(
            response.tasks[0],
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        return cast(
            GPUVirtualCluster,
            await self.get(
                cluster_id=cluster_id,
                project_id=project_id,
                region_id=region_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
        )
