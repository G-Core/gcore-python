# Custom code. This file is not generated and is preserved across codegen runs.
# It isolates hand-written *_and_poll convenience methods from generated code to
# eliminate merge conflicts.

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Iterable, Optional, cast

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .....types.cloud.k8s import (
    cluster_create_params,
    cluster_update_params,
)
from .....types.cloud.k8s.k8s_cluster import K8SCluster

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
        keypair: str,
        name: str,
        pools: Iterable[cluster_create_params.Pool],
        version: str,
        add_ons: cluster_create_params.AddOns | Omit = omit,
        authentication: Optional[cluster_create_params.Authentication] | Omit = omit,
        autoscaler_config: Optional[Dict[str, str]] | Omit = omit,
        cni: Optional[cluster_create_params.Cni] | Omit = omit,
        csi: cluster_create_params.Csi | Omit = omit,
        ddos_profile: Optional[cluster_create_params.DDOSProfile] | Omit = omit,
        fixed_network: Optional[str] | Omit = omit,
        fixed_subnet: Optional[str] | Omit = omit,
        is_ipv6: Optional[bool] | Omit = omit,
        logging: Optional[cluster_create_params.Logging] | Omit = omit,
        pods_ip_pool: Optional[str] | Omit = omit,
        pods_ipv6_pool: Optional[str] | Omit = omit,
        services_ip_pool: Optional[str] | Omit = omit,
        services_ipv6_pool: Optional[str] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> K8SCluster:
        """
        Create a k8s cluster and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.create(
            project_id=project_id,
            region_id=region_id,
            keypair=keypair,
            name=name,
            pools=pools,
            version=version,
            add_ons=add_ons,
            authentication=authentication,
            autoscaler_config=autoscaler_config,
            cni=cni,
            csi=csi,
            ddos_profile=ddos_profile,
            fixed_network=fixed_network,
            fixed_subnet=fixed_subnet,
            is_ipv6=is_ipv6,
            logging=logging,
            pods_ip_pool=pods_ip_pool,
            pods_ipv6_pool=pods_ipv6_pool,
            services_ip_pool=services_ip_pool,
            services_ipv6_pool=services_ipv6_pool,
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
        if not task.created_resources or not task.created_resources.k8s_clusters:
            raise ValueError("No k8s cluster was created")
        # K8s cluster `get` is keyed on cluster name (not UUID), and the name is
        # unique per region, so reuse the name passed to `create`.
        return cast(
            K8SCluster,
            self.get(
                cluster_name=name,
                project_id=project_id,
                region_id=region_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
        )

    def update_and_poll(
        self,
        cluster_name: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        add_ons: cluster_update_params.AddOns | Omit = omit,
        authentication: Optional[cluster_update_params.Authentication] | Omit = omit,
        autoscaler_config: Optional[Dict[str, str]] | Omit = omit,
        cni: Optional[cluster_update_params.Cni] | Omit = omit,
        ddos_profile: Optional[cluster_update_params.DDOSProfile] | Omit = omit,
        logging: Optional[cluster_update_params.Logging] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> K8SCluster:
        """
        Update a k8s cluster and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.update(
            cluster_name=cluster_name,
            project_id=project_id,
            region_id=region_id,
            add_ons=add_ons,
            authentication=authentication,
            autoscaler_config=autoscaler_config,
            cni=cni,
            ddos_profile=ddos_profile,
            logging=logging,
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
            K8SCluster,
            self.get(
                cluster_name=cluster_name,
                project_id=project_id,
                region_id=region_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
        )

    def upgrade_and_poll(
        self,
        cluster_name: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        version: str,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> K8SCluster:
        """
        Upgrade a k8s cluster and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.upgrade(
            cluster_name=cluster_name,
            project_id=project_id,
            region_id=region_id,
            version=version,
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
            K8SCluster,
            self.get(
                cluster_name=cluster_name,
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
        cluster_name: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        volumes: str | Omit = omit,
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
        Delete a k8s cluster and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.delete(
            cluster_name=cluster_name,
            project_id=project_id,
            region_id=region_id,
            volumes=volumes,
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
        keypair: str,
        name: str,
        pools: Iterable[cluster_create_params.Pool],
        version: str,
        add_ons: cluster_create_params.AddOns | Omit = omit,
        authentication: Optional[cluster_create_params.Authentication] | Omit = omit,
        autoscaler_config: Optional[Dict[str, str]] | Omit = omit,
        cni: Optional[cluster_create_params.Cni] | Omit = omit,
        csi: cluster_create_params.Csi | Omit = omit,
        ddos_profile: Optional[cluster_create_params.DDOSProfile] | Omit = omit,
        fixed_network: Optional[str] | Omit = omit,
        fixed_subnet: Optional[str] | Omit = omit,
        is_ipv6: Optional[bool] | Omit = omit,
        logging: Optional[cluster_create_params.Logging] | Omit = omit,
        pods_ip_pool: Optional[str] | Omit = omit,
        pods_ipv6_pool: Optional[str] | Omit = omit,
        services_ip_pool: Optional[str] | Omit = omit,
        services_ipv6_pool: Optional[str] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> K8SCluster:
        """
        Create a k8s cluster and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.create(
            project_id=project_id,
            region_id=region_id,
            keypair=keypair,
            name=name,
            pools=pools,
            version=version,
            add_ons=add_ons,
            authentication=authentication,
            autoscaler_config=autoscaler_config,
            cni=cni,
            csi=csi,
            ddos_profile=ddos_profile,
            fixed_network=fixed_network,
            fixed_subnet=fixed_subnet,
            is_ipv6=is_ipv6,
            logging=logging,
            pods_ip_pool=pods_ip_pool,
            pods_ipv6_pool=pods_ipv6_pool,
            services_ip_pool=services_ip_pool,
            services_ipv6_pool=services_ipv6_pool,
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
        if not task.created_resources or not task.created_resources.k8s_clusters:
            raise ValueError("No k8s cluster was created")
        # K8s cluster `get` is keyed on cluster name (not UUID), and the name is
        # unique per region, so reuse the name passed to `create`.
        return cast(
            K8SCluster,
            await self.get(
                cluster_name=name,
                project_id=project_id,
                region_id=region_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
        )

    async def update_and_poll(
        self,
        cluster_name: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        add_ons: cluster_update_params.AddOns | Omit = omit,
        authentication: Optional[cluster_update_params.Authentication] | Omit = omit,
        autoscaler_config: Optional[Dict[str, str]] | Omit = omit,
        cni: Optional[cluster_update_params.Cni] | Omit = omit,
        ddos_profile: Optional[cluster_update_params.DDOSProfile] | Omit = omit,
        logging: Optional[cluster_update_params.Logging] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> K8SCluster:
        """
        Update a k8s cluster and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.update(
            cluster_name=cluster_name,
            project_id=project_id,
            region_id=region_id,
            add_ons=add_ons,
            authentication=authentication,
            autoscaler_config=autoscaler_config,
            cni=cni,
            ddos_profile=ddos_profile,
            logging=logging,
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
            K8SCluster,
            await self.get(
                cluster_name=cluster_name,
                project_id=project_id,
                region_id=region_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
        )

    async def upgrade_and_poll(
        self,
        cluster_name: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        version: str,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> K8SCluster:
        """
        Upgrade a k8s cluster and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.upgrade(
            cluster_name=cluster_name,
            project_id=project_id,
            region_id=region_id,
            version=version,
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
            K8SCluster,
            await self.get(
                cluster_name=cluster_name,
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
        cluster_name: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        volumes: str | Omit = omit,
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
        Delete a k8s cluster and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.delete(
            cluster_name=cluster_name,
            project_id=project_id,
            region_id=region_id,
            volumes=volumes,
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
