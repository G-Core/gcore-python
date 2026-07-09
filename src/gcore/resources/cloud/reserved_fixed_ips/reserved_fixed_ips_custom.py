# Custom code. This file is not generated and is preserved across codegen runs.
# It isolates hand-written *_and_poll convenience methods from generated code to
# eliminate merge conflicts.

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, cast
from typing_extensions import Literal, overload

import httpx

from ...._types import NOT_GIVEN, Body, Omit, Query, Headers, NotGiven, omit
from ...._utils import required_args
from ....types.cloud import (
    InterfaceIPFamily,
)
from ....types.cloud.task_id_list import TaskIDList
from ....types.cloud.reserved_fixed_ip import ReservedFixedIP
from ....types.cloud.interface_ip_family import InterfaceIPFamily

if TYPE_CHECKING:
    from ...._client import Gcore, AsyncGcore


class ReservedFixedIPsResourceCustomMixin:
    if TYPE_CHECKING:
        # Provided by the concrete generated resource class this mixin is
        # combined with; declared here so client-derived locals keep their
        # real types and other resource methods resolve via __getattr__.
        _client: Gcore

        def __getattr__(self, name: str) -> Any: ...

    @overload
    def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        type: Literal["external"],
        ip_family: Optional[InterfaceIPFamily] | Omit = omit,
        is_vip: bool | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> ReservedFixedIP:
        """
        Create a new reserved fixed IP with the specified configuration and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.

        Args:
          type: Must be 'external'

          ip_family: Which subnets should be selected: IPv4, IPv6 or use dual stack.

          is_vip: If reserved fixed IP is a VIP

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        subnet_id: str,
        type: Literal["subnet"],
        is_vip: bool | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> ReservedFixedIP:
        """
        Create a new reserved fixed IP with the specified configuration and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.

        Args:
          subnet_id: Reserved fixed IP will be allocated in this subnet

          type: Must be 'subnet'.

          is_vip: If reserved fixed IP is a VIP

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        network_id: str,
        type: Literal["any_subnet"],
        ip_family: Optional[InterfaceIPFamily] | Omit = omit,
        is_vip: bool | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> ReservedFixedIP:
        """
        Create a new reserved fixed IP with the specified configuration and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.

        Args:
          network_id: Reserved fixed IP will be allocated in a subnet of this network

          type: Must be '`any_subnet`'.

          ip_family: Which subnets should be selected: IPv4, IPv6 or use dual stack.

          is_vip: If reserved fixed IP is a VIP

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        ip_address: str,
        network_id: str,
        type: Literal["ip_address"],
        is_vip: bool | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> ReservedFixedIP:
        """
        Create a new reserved fixed IP with the specified configuration and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.

        Args:
          ip_address: Reserved fixed IP will be allocated the given IP address

          network_id: Reserved fixed IP will be allocated in a subnet of this network

          type: Must be '`ip_address`'.

          is_vip: If reserved fixed IP is a VIP

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        port_id: str,
        type: Literal["port"],
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> ReservedFixedIP:
        """
        Create a new reserved fixed IP with the specified configuration and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.

        Args:
          port_id: Port ID to make a reserved fixed IP (for example, `vip_port_id` of the Load
              Balancer entity).

          type: Must be 'port'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["type"],
        ["subnet_id", "type"],
        ["network_id", "type"],
        ["ip_address", "network_id", "type"],
        ["port_id", "type"],
    )
    def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        type: Literal["external"] | Literal["subnet"] | Literal["any_subnet"] | Literal["ip_address"] | Literal["port"],
        ip_family: Optional[InterfaceIPFamily] | Omit = omit,
        is_vip: bool | Omit = omit,
        subnet_id: str | Omit = omit,
        network_id: str | Omit = omit,
        ip_address: str | Omit = omit,
        port_id: str | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> ReservedFixedIP:
        """
        Create a new reserved fixed IP with the specified configuration and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response: TaskIDList = self.create(  # type: ignore
            project_id=project_id,
            region_id=region_id,
            type=type,
            ip_family=ip_family,
            is_vip=is_vip,
            subnet_id=subnet_id,
            network_id=network_id,
            ip_address=ip_address,
            port_id=port_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks:  # type: ignore
            raise ValueError("Expected at least one task to be created")
        task = self._client.cloud.tasks.poll(
            task_id=response.tasks[0],  # type: ignore
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        if (
            task.created_resources is None
            or task.created_resources.ports is None
            or len(task.created_resources.ports) != 1
        ):
            raise ValueError("Task completed but created_resources or ports is missing or invalid")
        created_port_id = task.created_resources.ports[0]
        return cast(
            ReservedFixedIP,
            self.get(
                port_id=created_port_id,
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
        port_id: str,
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
        Delete a specific reserved fixed IP and all its associated resources and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.delete(
            port_id=port_id,
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


class AsyncReservedFixedIPsResourceCustomMixin:
    if TYPE_CHECKING:
        # Provided by the concrete generated resource class this mixin is
        # combined with; declared here so client-derived locals keep their
        # real types and other resource methods resolve via __getattr__.
        _client: AsyncGcore

        def __getattr__(self, name: str) -> Any: ...

    @overload
    async def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        type: Literal["external"],
        ip_family: Optional[InterfaceIPFamily] | Omit = omit,
        is_vip: bool | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> ReservedFixedIP:
        """
        Create a new reserved fixed IP with the specified configuration and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.

        Args:
          type: Must be 'external'

          ip_family: Which subnets should be selected: IPv4, IPv6 or use dual stack.

          is_vip: If reserved fixed IP is a VIP

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        subnet_id: str,
        type: Literal["subnet"],
        is_vip: bool | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> ReservedFixedIP:
        """
        Create a new reserved fixed IP with the specified configuration and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.

        Args:
          subnet_id: Reserved fixed IP will be allocated in this subnet

          type: Must be 'subnet'.

          is_vip: If reserved fixed IP is a VIP

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        network_id: str,
        type: Literal["any_subnet"],
        ip_family: Optional[InterfaceIPFamily] | Omit = omit,
        is_vip: bool | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> ReservedFixedIP:
        """
        Create a new reserved fixed IP with the specified configuration and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.

        Args:
          network_id: Reserved fixed IP will be allocated in a subnet of this network

          type: Must be '`any_subnet`'.

          ip_family: Which subnets should be selected: IPv4, IPv6 or use dual stack.

          is_vip: If reserved fixed IP is a VIP

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        ip_address: str,
        network_id: str,
        type: Literal["ip_address"],
        is_vip: bool | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> ReservedFixedIP:
        """
        Create a new reserved fixed IP with the specified configuration and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.

        Args:
          ip_address: Reserved fixed IP will be allocated the given IP address

          network_id: Reserved fixed IP will be allocated in a subnet of this network

          type: Must be '`ip_address`'.

          is_vip: If reserved fixed IP is a VIP

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        port_id: str,
        type: Literal["port"],
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> ReservedFixedIP:
        """
        Create a new reserved fixed IP with the specified configuration and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.

        Args:
          port_id: Port ID to make a reserved fixed IP (for example, `vip_port_id` of the Load
              Balancer entity).

          type: Must be 'port'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["type"],
        ["subnet_id", "type"],
        ["network_id", "type"],
        ["ip_address", "network_id", "type"],
        ["port_id", "type"],
    )
    async def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        type: Literal["external"] | Literal["subnet"] | Literal["any_subnet"] | Literal["ip_address"] | Literal["port"],
        ip_family: Optional[InterfaceIPFamily] | Omit = omit,
        is_vip: bool | Omit = omit,
        subnet_id: str | Omit = omit,
        network_id: str | Omit = omit,
        ip_address: str | Omit = omit,
        port_id: str | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> ReservedFixedIP:
        """
        Create a new reserved fixed IP with the specified configuration and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response: TaskIDList = await self.create(  # type: ignore
            project_id=project_id,
            region_id=region_id,
            type=type,
            ip_family=ip_family,
            is_vip=is_vip,
            subnet_id=subnet_id,
            network_id=network_id,
            ip_address=ip_address,
            port_id=port_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks:  # type: ignore
            raise ValueError("Expected at least one task to be created")
        task = await self._client.cloud.tasks.poll(
            task_id=response.tasks[0],  # type: ignore
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        if (
            task.created_resources is None
            or task.created_resources.ports is None
            or len(task.created_resources.ports) != 1
        ):
            raise ValueError("Task completed but created_resources or ports is missing or invalid")
        created_port_id = task.created_resources.ports[0]
        return cast(
            ReservedFixedIP,
            await self.get(
                port_id=created_port_id,
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
        port_id: str,
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
        Delete a specific reserved fixed IP and all its associated resources and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.delete(
            port_id=port_id,
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
