# Custom code. This file is not generated and is preserved across codegen runs.
# It isolates hand-written *_and_poll convenience methods from generated code to
# eliminate merge conflicts.

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Iterable, Optional, cast

import httpx

from ....._types import NOT_GIVEN, Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit
from .....types.cloud.inference import deployment_create_params, deployment_update_params
from .....types.cloud.inference.inference_deployment import InferenceDeployment

if TYPE_CHECKING:
    from ....._client import Gcore, AsyncGcore


class DeploymentsResourceCustomMixin:
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
        containers: Iterable[deployment_create_params.Container],
        flavor_name: str,
        image: str,
        listening_port: int,
        name: str,
        api_keys: SequenceNotStr[str] | Omit = omit,
        auth_enabled: bool | Omit = omit,
        command: Optional[SequenceNotStr[str]] | Omit = omit,
        credentials_name: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        envs: Dict[str, str] | Omit = omit,
        ingress_opts: Optional[deployment_create_params.IngressOpts] | Omit = omit,
        logging: Optional[deployment_create_params.Logging] | Omit = omit,
        probes: Optional[deployment_create_params.Probes] | Omit = omit,
        api_timeout: Optional[int] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> InferenceDeployment:
        response = self.create(
            project_id=project_id,
            containers=containers,
            flavor_name=flavor_name,
            image=image,
            listening_port=listening_port,
            name=name,
            api_keys=api_keys,
            auth_enabled=auth_enabled,
            command=command,
            credentials_name=credentials_name,
            description=description,
            envs=envs,
            ingress_opts=ingress_opts,
            logging=logging,
            probes=probes,
            api_timeout=api_timeout,
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
            or not task.created_resources.inference_instances
            or len(task.created_resources.inference_instances) != 1
        ):
            raise ValueError("Expected exactly one resource to be created in a task")
        return cast(
            InferenceDeployment,
            self.get(
                deployment_name=task.created_resources.inference_instances[0],
                project_id=project_id,
                extra_headers=extra_headers,
                timeout=timeout,
            ),
        )

    def update_and_poll(
        self,
        deployment_name: str,
        *,
        project_id: int | None = None,
        api_keys: Optional[SequenceNotStr[str]] | Omit = omit,
        auth_enabled: bool | Omit = omit,
        command: Optional[SequenceNotStr[str]] | Omit = omit,
        containers: Optional[Iterable[deployment_update_params.Container]] | Omit = omit,
        credentials_name: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        envs: Optional[Dict[str, str]] | Omit = omit,
        flavor_name: str | Omit = omit,
        image: Optional[str] | Omit = omit,
        ingress_opts: Optional[deployment_update_params.IngressOpts] | Omit = omit,
        listening_port: Optional[int] | Omit = omit,
        logging: Optional[deployment_update_params.Logging] | Omit = omit,
        probes: Optional[deployment_update_params.Probes] | Omit = omit,
        api_timeout: Optional[int] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> InferenceDeployment:
        """
        Update inference deployment and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.update(
            deployment_name=deployment_name,
            project_id=project_id,
            api_keys=api_keys,
            auth_enabled=auth_enabled,
            command=command,
            containers=containers,
            credentials_name=credentials_name,
            description=description,
            envs=envs,
            flavor_name=flavor_name,
            image=image,
            ingress_opts=ingress_opts,
            listening_port=listening_port,
            logging=logging,
            probes=probes,
            api_timeout=api_timeout,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks or len(response.tasks) < 1:
            raise ValueError("Expected at least one task to be created")
        self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        return cast(
            InferenceDeployment,
            self.get(
                deployment_name=deployment_name,
                project_id=project_id,
                extra_headers=extra_headers,
                timeout=timeout,
            ),
        )

    def delete_and_poll(
        self,
        deployment_name: str,
        *,
        project_id: int | None = None,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> None:
        """
        Delete inference deployment and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.delete(
            deployment_name=deployment_name,
            project_id=project_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks or len(response.tasks) < 1:
            raise ValueError("Expected at least one task to be created")
        self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )


class AsyncDeploymentsResourceCustomMixin:
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
        containers: Iterable[deployment_create_params.Container],
        flavor_name: str,
        image: str,
        listening_port: int,
        name: str,
        api_keys: SequenceNotStr[str] | Omit = omit,
        auth_enabled: bool | Omit = omit,
        command: Optional[SequenceNotStr[str]] | Omit = omit,
        credentials_name: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        envs: Dict[str, str] | Omit = omit,
        ingress_opts: Optional[deployment_create_params.IngressOpts] | Omit = omit,
        logging: Optional[deployment_create_params.Logging] | Omit = omit,
        probes: Optional[deployment_create_params.Probes] | Omit = omit,
        api_timeout: Optional[int] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> InferenceDeployment:
        response = await self.create(
            project_id=project_id,
            containers=containers,
            flavor_name=flavor_name,
            image=image,
            listening_port=listening_port,
            name=name,
            api_keys=api_keys,
            auth_enabled=auth_enabled,
            command=command,
            credentials_name=credentials_name,
            description=description,
            envs=envs,
            ingress_opts=ingress_opts,
            logging=logging,
            probes=probes,
            api_timeout=api_timeout,
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
            or not task.created_resources.inference_instances
            or len(task.created_resources.inference_instances) != 1
        ):
            raise ValueError("Expected exactly one resource to be created in a task")
        return cast(
            InferenceDeployment,
            await self.get(
                deployment_name=task.created_resources.inference_instances[0],
                project_id=project_id,
                extra_headers=extra_headers,
                timeout=timeout,
            ),
        )

    async def update_and_poll(
        self,
        deployment_name: str,
        *,
        project_id: int | None = None,
        api_keys: Optional[SequenceNotStr[str]] | Omit = omit,
        auth_enabled: bool | Omit = omit,
        command: Optional[SequenceNotStr[str]] | Omit = omit,
        containers: Optional[Iterable[deployment_update_params.Container]] | Omit = omit,
        credentials_name: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        envs: Optional[Dict[str, str]] | Omit = omit,
        flavor_name: str | Omit = omit,
        image: Optional[str] | Omit = omit,
        ingress_opts: Optional[deployment_update_params.IngressOpts] | Omit = omit,
        listening_port: Optional[int] | Omit = omit,
        logging: Optional[deployment_update_params.Logging] | Omit = omit,
        probes: Optional[deployment_update_params.Probes] | Omit = omit,
        api_timeout: Optional[int] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> InferenceDeployment:
        """
        Update inference deployment and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.update(
            deployment_name=deployment_name,
            project_id=project_id,
            api_keys=api_keys,
            auth_enabled=auth_enabled,
            command=command,
            containers=containers,
            credentials_name=credentials_name,
            description=description,
            envs=envs,
            flavor_name=flavor_name,
            image=image,
            ingress_opts=ingress_opts,
            listening_port=listening_port,
            logging=logging,
            probes=probes,
            api_timeout=api_timeout,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks or len(response.tasks) < 1:
            raise ValueError("Expected at least one task to be created")
        await self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        return cast(
            InferenceDeployment,
            await self.get(
                deployment_name=deployment_name,
                project_id=project_id,
                extra_headers=extra_headers,
                timeout=timeout,
            ),
        )

    async def delete_and_poll(
        self,
        deployment_name: str,
        *,
        project_id: int | None = None,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> None:
        """
        Delete inference deployment and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.delete(
            deployment_name=deployment_name,
            project_id=project_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks or len(response.tasks) < 1:
            raise ValueError("Expected at least one task to be created")
        await self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
