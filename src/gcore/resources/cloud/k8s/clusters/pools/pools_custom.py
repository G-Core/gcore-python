# Custom code. This file is not generated and is preserved across codegen runs.
# It isolates hand-written *_and_poll convenience methods from generated code to
# eliminate merge conflicts.

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional, cast
from typing_extensions import Literal

import httpx

from ......_types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ......types.cloud.k8s.clusters.k8s_cluster_pool import K8SClusterPool

if TYPE_CHECKING:
    from ......_client import Gcore, AsyncGcore


class PoolsResourceCustomMixin:
    if TYPE_CHECKING:
        # Provided by the concrete generated resource class this mixin is
        # combined with; declared here so client-derived locals keep their
        # real types and other resource methods resolve via __getattr__.
        _client: Gcore

        def __getattr__(self, name: str) -> Any: ...

    def create_and_poll(
        self,
        cluster_name: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        flavor_id: str,
        min_node_count: int,
        name: str,
        auto_healing_enabled: Optional[bool] | Omit = omit,
        boot_volume_size: Optional[int] | Omit = omit,
        boot_volume_type: Optional[Literal["cold", "ssd_hiiops", "ssd_local", "ssd_lowlatency", "standard", "ultra"]]
        | Omit = omit,
        crio_config: Optional[Dict[str, str]] | Omit = omit,
        is_public_ipv4: Optional[bool] | Omit = omit,
        kubelet_config: Optional[Dict[str, str]] | Omit = omit,
        labels: Optional[Dict[str, str]] | Omit = omit,
        max_node_count: Optional[int] | Omit = omit,
        servergroup_policy: Optional[Literal["affinity", "anti-affinity", "soft-anti-affinity"]] | Omit = omit,
        taints: Optional[Dict[str, str]] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> K8SClusterPool:
        """
        Create a k8s cluster pool and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.create(
            cluster_name=cluster_name,
            project_id=project_id,
            region_id=region_id,
            flavor_id=flavor_id,
            min_node_count=min_node_count,
            name=name,
            auto_healing_enabled=auto_healing_enabled,
            boot_volume_size=boot_volume_size,
            boot_volume_type=boot_volume_type,
            crio_config=crio_config,
            is_public_ipv4=is_public_ipv4,
            kubelet_config=kubelet_config,
            labels=labels,
            max_node_count=max_node_count,
            servergroup_policy=servergroup_policy,
            taints=taints,
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
        if not task.created_resources or not task.created_resources.k8s_pools:
            raise ValueError("No k8s cluster pool was created")
        # K8s pool `get` is keyed on pool name (not UUID), and the name is
        # unique within a cluster, so reuse the name passed to `create`.
        return cast(
            K8SClusterPool,
            self.get(
                pool_name=name,
                project_id=project_id,
                region_id=region_id,
                cluster_name=cluster_name,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
        )

    def resize_and_poll(
        self,
        pool_name: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        cluster_name: str,
        node_count: int,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> K8SClusterPool:
        """
        Resize a k8s cluster pool and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.resize(
            pool_name=pool_name,
            project_id=project_id,
            region_id=region_id,
            cluster_name=cluster_name,
            node_count=node_count,
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
            extra_query=extra_query,
            extra_body=extra_body,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        return cast(
            K8SClusterPool,
            self.get(
                pool_name=pool_name,
                project_id=project_id,
                region_id=region_id,
                cluster_name=cluster_name,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
        )

    def delete_and_poll(
        self,
        pool_name: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        cluster_name: str,
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
        Delete a k8s cluster pool and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.delete(
            pool_name=pool_name,
            project_id=project_id,
            region_id=region_id,
            cluster_name=cluster_name,
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
            extra_query=extra_query,
            extra_body=extra_body,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )


class AsyncPoolsResourceCustomMixin:
    if TYPE_CHECKING:
        # Provided by the concrete generated resource class this mixin is
        # combined with; declared here so client-derived locals keep their
        # real types and other resource methods resolve via __getattr__.
        _client: AsyncGcore

        def __getattr__(self, name: str) -> Any: ...

    async def create_and_poll(
        self,
        cluster_name: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        flavor_id: str,
        min_node_count: int,
        name: str,
        auto_healing_enabled: Optional[bool] | Omit = omit,
        boot_volume_size: Optional[int] | Omit = omit,
        boot_volume_type: Optional[Literal["cold", "ssd_hiiops", "ssd_local", "ssd_lowlatency", "standard", "ultra"]]
        | Omit = omit,
        crio_config: Optional[Dict[str, str]] | Omit = omit,
        is_public_ipv4: Optional[bool] | Omit = omit,
        kubelet_config: Optional[Dict[str, str]] | Omit = omit,
        labels: Optional[Dict[str, str]] | Omit = omit,
        max_node_count: Optional[int] | Omit = omit,
        servergroup_policy: Optional[Literal["affinity", "anti-affinity", "soft-anti-affinity"]] | Omit = omit,
        taints: Optional[Dict[str, str]] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> K8SClusterPool:
        """
        Create a k8s cluster pool and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.create(
            cluster_name=cluster_name,
            project_id=project_id,
            region_id=region_id,
            flavor_id=flavor_id,
            min_node_count=min_node_count,
            name=name,
            auto_healing_enabled=auto_healing_enabled,
            boot_volume_size=boot_volume_size,
            boot_volume_type=boot_volume_type,
            crio_config=crio_config,
            is_public_ipv4=is_public_ipv4,
            kubelet_config=kubelet_config,
            labels=labels,
            max_node_count=max_node_count,
            servergroup_policy=servergroup_policy,
            taints=taints,
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
        if not task.created_resources or not task.created_resources.k8s_pools:
            raise ValueError("No k8s cluster pool was created")
        # K8s pool `get` is keyed on pool name (not UUID), and the name is
        # unique within a cluster, so reuse the name passed to `create`.
        return cast(
            K8SClusterPool,
            await self.get(
                pool_name=name,
                project_id=project_id,
                region_id=region_id,
                cluster_name=cluster_name,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
        )

    async def resize_and_poll(
        self,
        pool_name: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        cluster_name: str,
        node_count: int,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> K8SClusterPool:
        """
        Resize a k8s cluster pool and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.resize(
            pool_name=pool_name,
            project_id=project_id,
            region_id=region_id,
            cluster_name=cluster_name,
            node_count=node_count,
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
            extra_query=extra_query,
            extra_body=extra_body,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        return cast(
            K8SClusterPool,
            await self.get(
                pool_name=pool_name,
                project_id=project_id,
                region_id=region_id,
                cluster_name=cluster_name,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
        )

    async def delete_and_poll(
        self,
        pool_name: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        cluster_name: str,
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
        Delete a k8s cluster pool and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.delete(
            pool_name=pool_name,
            project_id=project_id,
            region_id=region_id,
            cluster_name=cluster_name,
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
            extra_query=extra_query,
            extra_body=extra_body,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
