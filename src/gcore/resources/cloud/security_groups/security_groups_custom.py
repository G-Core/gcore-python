# Custom code. This file is not generated and is preserved across codegen runs.
# It isolates hand-written *_and_poll convenience methods from generated code to
# eliminate merge conflicts.

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Iterable, Optional, cast

import httpx

from ...._types import NOT_GIVEN, Body, Omit, Query, Headers, NotGiven, omit
from ....types.cloud import (
    security_group_create_params,
    security_group_update_params,
)
from ....types.cloud.security_group import SecurityGroup
from ....types.cloud.tag_update_map_param import TagUpdateMapParam

if TYPE_CHECKING:
    from ...._client import Gcore, AsyncGcore


class SecurityGroupsResourceCustomMixin:
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
        name: str,
        description: str | Omit = omit,
        rules: Iterable[security_group_create_params.Rule] | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> SecurityGroup:
        """
        Create security group and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.create(
            project_id=project_id,
            region_id=region_id,
            name=name,
            description=description,
            rules=rules,
            tags=tags,
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
        if task.created_resources is None or task.created_resources.security_groups is None:
            raise ValueError("Task completed but created_resources or security_groups is missing")
        security_group_id = task.created_resources.security_groups[0]
        return cast(
            SecurityGroup,
            self.get(
                group_id=security_group_id,
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
        group_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        description: str | Omit = omit,
        name: str | Omit = omit,
        rules: Iterable[security_group_update_params.Rule] | Omit = omit,
        tags: Optional[TagUpdateMapParam] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> SecurityGroup:
        """
        Update security group and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.update(
            group_id=group_id,
            project_id=project_id,
            region_id=region_id,
            description=description,
            name=name,
            rules=rules,
            tags=tags,
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
            SecurityGroup,
            self.get(
                group_id=group_id,
                project_id=project_id,
                region_id=region_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
        )


class AsyncSecurityGroupsResourceCustomMixin:
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
        name: str,
        description: str | Omit = omit,
        rules: Iterable[security_group_create_params.Rule] | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> SecurityGroup:
        """
        Create security group and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.create(
            project_id=project_id,
            region_id=region_id,
            name=name,
            description=description,
            rules=rules,
            tags=tags,
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
        if task.created_resources is None or task.created_resources.security_groups is None:
            raise ValueError("Task completed but created_resources or security_groups is missing")
        security_group_id = task.created_resources.security_groups[0]
        return cast(
            SecurityGroup,
            await self.get(
                group_id=security_group_id,
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
        group_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        description: str | Omit = omit,
        name: str | Omit = omit,
        rules: Iterable[security_group_update_params.Rule] | Omit = omit,
        tags: Optional[TagUpdateMapParam] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> SecurityGroup:
        """
        Update security group and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.update(
            group_id=group_id,
            project_id=project_id,
            region_id=region_id,
            description=description,
            name=name,
            rules=rules,
            tags=tags,
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
            SecurityGroup,
            await self.get(
                group_id=group_id,
                project_id=project_id,
                region_id=region_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
        )
