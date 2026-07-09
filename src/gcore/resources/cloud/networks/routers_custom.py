# Custom code. This file is not generated and is preserved across codegen runs.
# It isolates hand-written *_and_poll convenience methods from generated code to
# eliminate merge conflicts.

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterable, cast

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....types.cloud.networks import (
    router_update_params,
)
from ....types.cloud.networks.router import Router

if TYPE_CHECKING:
    from ...._client import Gcore, AsyncGcore


class RoutersResourceCustomMixin:
    if TYPE_CHECKING:
        # Provided by the concrete generated resource class this mixin is
        # combined with; declared here so client-derived locals keep their
        # real types and other resource methods resolve via __getattr__.
        _client: Gcore

        def __getattr__(self, name: str) -> Any: ...

    def update_and_poll(
        self,
        router_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        external_gateway_info: router_update_params.ExternalGatewayInfo | Omit = omit,
        name: str | Omit = omit,
        routes: Iterable[router_update_params.Route] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Router:
        """
        Update router and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.update(
            router_id=router_id,
            project_id=project_id,
            region_id=region_id,
            external_gateway_info=external_gateway_info,
            name=name,
            routes=routes,
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
            Router,
            self.get(
                router_id=router_id,
                project_id=project_id,
                region_id=region_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
        )


class AsyncRoutersResourceCustomMixin:
    if TYPE_CHECKING:
        # Provided by the concrete generated resource class this mixin is
        # combined with; declared here so client-derived locals keep their
        # real types and other resource methods resolve via __getattr__.
        _client: AsyncGcore

        def __getattr__(self, name: str) -> Any: ...

    async def update_and_poll(
        self,
        router_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        external_gateway_info: router_update_params.ExternalGatewayInfo | Omit = omit,
        name: str | Omit = omit,
        routes: Iterable[router_update_params.Route] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Router:
        """
        Update router and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.update(
            router_id=router_id,
            project_id=project_id,
            region_id=region_id,
            external_gateway_info=external_gateway_info,
            name=name,
            routes=routes,
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
            Router,
            await self.get(
                router_id=router_id,
                project_id=project_id,
                region_id=region_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
        )
