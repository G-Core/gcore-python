# Custom code. This file is not generated and is preserved across codegen runs.
# It isolates hand-written *_and_poll convenience methods from generated code to
# eliminate merge conflicts.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given

if TYPE_CHECKING:
    from ....._client import Gcore, AsyncGcore


class ServersResourceCustomMixin:
    if TYPE_CHECKING:
        # Provided by the concrete generated resource class this mixin is
        # combined with; declared here so client-derived locals keep their
        # real types and other resource methods resolve via __getattr__.
        _client: Gcore

        def __getattr__(self, name: str) -> Any: ...

    def delete_and_poll(
        self,
        server_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        cluster_id: str,
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
        Delete a server from a virtual GPU cluster and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.delete(
            server_id=server_id,
            project_id=project_id,
            region_id=region_id,
            cluster_id=cluster_id,
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


class AsyncServersResourceCustomMixin:
    if TYPE_CHECKING:
        # Provided by the concrete generated resource class this mixin is
        # combined with; declared here so client-derived locals keep their
        # real types and other resource methods resolve via __getattr__.
        _client: AsyncGcore

        def __getattr__(self, name: str) -> Any: ...

    async def delete_and_poll(
        self,
        server_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        cluster_id: str,
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
        Delete a server from a virtual GPU cluster and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.delete(
            server_id=server_id,
            project_id=project_id,
            region_id=region_id,
            cluster_id=cluster_id,
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
