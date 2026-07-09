# Custom code. This file is not generated and is preserved across codegen runs.
# It isolates hand-written *_and_poll convenience methods from generated code to
# eliminate merge conflicts.

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterable, Optional, cast
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit
from ....types.cloud import LbListenerProtocol
from ....types.cloud.load_balancers import (
    listener_create_params,
    listener_update_params,
)
from ....types.cloud.lb_listener_protocol import LbListenerProtocol
from ....types.cloud.load_balancer_listener_detail import LoadBalancerListenerDetail

if TYPE_CHECKING:
    from ...._client import Gcore, AsyncGcore


class ListenersResourceCustomMixin:
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
        load_balancer_id: str,
        name: str,
        protocol: LbListenerProtocol,
        protocol_port: int,
        allowed_cidrs: Optional[SequenceNotStr[str]] | Omit = omit,
        connection_limit: int | Omit = omit,
        insert_x_forwarded: bool | Omit = omit,
        secret_id: Literal[""] | Omit = omit,
        sni_secret_id: SequenceNotStr[str] | Omit = omit,
        timeout_client_data: Optional[int] | Omit = omit,
        timeout_member_connect: Optional[int] | Omit = omit,
        timeout_member_data: Optional[int] | Omit = omit,
        user_list: Iterable[listener_create_params.UserList] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LoadBalancerListenerDetail:
        response = self.create(
            project_id=project_id,
            region_id=region_id,
            load_balancer_id=load_balancer_id,
            name=name,
            protocol=protocol,
            protocol_port=protocol_port,
            allowed_cidrs=allowed_cidrs,
            connection_limit=connection_limit,
            insert_x_forwarded=insert_x_forwarded,
            secret_id=secret_id,
            sni_secret_id=sni_secret_id,
            timeout_client_data=timeout_client_data,
            timeout_member_connect=timeout_member_connect,
            timeout_member_data=timeout_member_data,
            user_list=user_list,
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
            or not task.created_resources.listeners
            or len(task.created_resources.listeners) != 1
        ):
            raise ValueError("Expected exactly one resource to be created in a task")
        return cast(
            LoadBalancerListenerDetail,
            self.get(
                listener_id=task.created_resources.listeners[0],
                project_id=project_id,
                region_id=region_id,
                extra_headers=extra_headers,
                timeout=timeout,
            ),
        )

    def delete_and_poll(
        self,
        listener_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
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
        Delete listener and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.delete(
            listener_id=listener_id,
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

    def update_and_poll(
        self,
        listener_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        allowed_cidrs: Optional[SequenceNotStr[str]] | Omit = omit,
        connection_limit: int | Omit = omit,
        name: str | Omit = omit,
        secret_id: Optional[str] | Omit = omit,
        sni_secret_id: Optional[SequenceNotStr[str]] | Omit = omit,
        timeout_client_data: Optional[int] | Omit = omit,
        timeout_member_connect: Optional[int] | Omit = omit,
        timeout_member_data: Optional[int] | Omit = omit,
        user_list: Optional[Iterable[listener_update_params.UserList]] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LoadBalancerListenerDetail:
        """
        Update listener and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.update(
            listener_id=listener_id,
            project_id=project_id,
            region_id=region_id,
            allowed_cidrs=allowed_cidrs,
            connection_limit=connection_limit,
            name=name,
            secret_id=secret_id,
            sni_secret_id=sni_secret_id,
            timeout_client_data=timeout_client_data,
            timeout_member_connect=timeout_member_connect,
            timeout_member_data=timeout_member_data,
            user_list=user_list,
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
            LoadBalancerListenerDetail,
            self.get(
                listener_id=listener_id,
                project_id=project_id,
                region_id=region_id,
                extra_headers=extra_headers,
                timeout=timeout,
            ),
        )


class AsyncListenersResourceCustomMixin:
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
        load_balancer_id: str,
        name: str,
        protocol: LbListenerProtocol,
        protocol_port: int,
        allowed_cidrs: Optional[SequenceNotStr[str]] | Omit = omit,
        connection_limit: int | Omit = omit,
        insert_x_forwarded: bool | Omit = omit,
        secret_id: Literal[""] | Omit = omit,
        sni_secret_id: SequenceNotStr[str] | Omit = omit,
        timeout_client_data: Optional[int] | Omit = omit,
        timeout_member_connect: Optional[int] | Omit = omit,
        timeout_member_data: Optional[int] | Omit = omit,
        user_list: Iterable[listener_create_params.UserList] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LoadBalancerListenerDetail:
        response = await self.create(
            project_id=project_id,
            region_id=region_id,
            load_balancer_id=load_balancer_id,
            name=name,
            protocol=protocol,
            protocol_port=protocol_port,
            allowed_cidrs=allowed_cidrs,
            connection_limit=connection_limit,
            insert_x_forwarded=insert_x_forwarded,
            secret_id=secret_id,
            sni_secret_id=sni_secret_id,
            timeout_client_data=timeout_client_data,
            timeout_member_connect=timeout_member_connect,
            timeout_member_data=timeout_member_data,
            user_list=user_list,
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
            or not task.created_resources.listeners
            or len(task.created_resources.listeners) != 1
        ):
            raise ValueError("Expected exactly one resource to be created in a task")
        return cast(
            LoadBalancerListenerDetail,
            await self.get(
                listener_id=task.created_resources.listeners[0],
                project_id=project_id,
                region_id=region_id,
                extra_headers=extra_headers,
                timeout=timeout,
            ),
        )

    async def delete_and_poll(
        self,
        listener_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
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
        Delete listener and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.delete(
            listener_id=listener_id,
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

    async def update_and_poll(
        self,
        listener_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        allowed_cidrs: Optional[SequenceNotStr[str]] | Omit = omit,
        connection_limit: int | Omit = omit,
        name: str | Omit = omit,
        secret_id: Optional[str] | Omit = omit,
        sni_secret_id: Optional[SequenceNotStr[str]] | Omit = omit,
        timeout_client_data: Optional[int] | Omit = omit,
        timeout_member_connect: Optional[int] | Omit = omit,
        timeout_member_data: Optional[int] | Omit = omit,
        user_list: Optional[Iterable[listener_update_params.UserList]] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LoadBalancerListenerDetail:
        """
        Update listener and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.update(
            listener_id=listener_id,
            project_id=project_id,
            region_id=region_id,
            allowed_cidrs=allowed_cidrs,
            connection_limit=connection_limit,
            name=name,
            secret_id=secret_id,
            sni_secret_id=sni_secret_id,
            timeout_client_data=timeout_client_data,
            timeout_member_connect=timeout_member_connect,
            timeout_member_data=timeout_member_data,
            user_list=user_list,
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
            LoadBalancerListenerDetail,
            await self.get(
                listener_id=listener_id,
                project_id=project_id,
                region_id=region_id,
                extra_headers=extra_headers,
                timeout=timeout,
            ),
        )
