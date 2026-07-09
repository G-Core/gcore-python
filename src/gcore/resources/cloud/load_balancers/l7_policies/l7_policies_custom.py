# Custom code. This file is not generated and is preserved across codegen runs.
# It isolates hand-written *_and_poll convenience methods from generated code to
# eliminate merge conflicts.

from __future__ import annotations

from typing import TYPE_CHECKING, Any, cast
from typing_extensions import Literal, overload

import httpx

from ....._types import NOT_GIVEN, Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit
from ....._utils import required_args
from .....types.cloud.task_id_list import TaskIDList
from .....types.cloud.load_balancer_l7_policy import LoadBalancerL7Policy

if TYPE_CHECKING:
    from ....._client import Gcore, AsyncGcore


class L7PoliciesResourceCustomMixin:
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
        action: Literal["REDIRECT_TO_URL"],
        listener_id: str,
        redirect_url: str,
        name: str | Omit = omit,
        position: int | Omit = omit,
        redirect_http_code: int | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LoadBalancerL7Policy:
        """Create L7 policy and poll for completion."""
        ...

    @overload
    def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["REDIRECT_PREFIX"],
        listener_id: str,
        redirect_prefix: str,
        name: str | Omit = omit,
        position: int | Omit = omit,
        redirect_http_code: int | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LoadBalancerL7Policy:
        """Create L7 policy and poll for completion."""
        ...

    @overload
    def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["REDIRECT_TO_POOL"],
        listener_id: str,
        redirect_pool_id: str,
        name: str | Omit = omit,
        position: int | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LoadBalancerL7Policy:
        """Create L7 policy and poll for completion."""
        ...

    @overload
    def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["REJECT"],
        listener_id: str,
        name: str | Omit = omit,
        position: int | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LoadBalancerL7Policy:
        """Create L7 policy and poll for completion."""
        ...

    @required_args(
        ["action", "listener_id", "redirect_url"],
        ["action", "listener_id", "redirect_prefix"],
        ["action", "listener_id", "redirect_pool_id"],
        ["action", "listener_id"],
    )
    def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["REDIRECT_TO_URL"]
        | Literal["REDIRECT_PREFIX"]
        | Literal["REDIRECT_TO_POOL"]
        | Literal["REJECT"],
        listener_id: str,
        redirect_url: str | Omit = omit,
        name: str | Omit = omit,
        position: int | Omit = omit,
        redirect_http_code: int | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        redirect_prefix: str | Omit = omit,
        redirect_pool_id: str | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LoadBalancerL7Policy:
        """Create L7 policy and poll for completion."""
        response: TaskIDList = self.create(  # type: ignore
            project_id=project_id,
            region_id=region_id,
            action=action,
            listener_id=listener_id,
            name=name,
            position=position,
            redirect_http_code=redirect_http_code,
            redirect_pool_id=redirect_pool_id,
            redirect_prefix=redirect_prefix,
            redirect_url=redirect_url,
            tags=tags,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks or len(response.tasks) != 1:  # type: ignore[union-attr]
            raise ValueError("Expected exactly one task to be created")
        task = self._client.cloud.tasks.poll(
            task_id=response.tasks[0],  # type: ignore[index]
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        if (
            not task.created_resources
            or not task.created_resources.l7polices
            or len(task.created_resources.l7polices) != 1
        ):
            raise ValueError("Expected exactly one resource to be created in a task")
        return cast(
            LoadBalancerL7Policy,
            self.get(
                l7policy_id=task.created_resources.l7polices[0],
                project_id=project_id,
                region_id=region_id,
                extra_headers=extra_headers,
                timeout=timeout,
            ),
        )

    def delete_and_poll(
        self,
        l7policy_id: str,
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
        response = self.delete(
            l7policy_id=l7policy_id,
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks or len(response.tasks) != 1:
            raise ValueError("Expected exactly one task to be created")
        self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )

    @overload
    def update_and_poll(
        self,
        l7policy_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["REDIRECT_TO_URL"],
        redirect_url: str,
        name: str | Omit = omit,
        position: int | Omit = omit,
        redirect_http_code: int | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LoadBalancerL7Policy:
        """Update L7 policy and poll for completion."""
        ...

    @overload
    def update_and_poll(
        self,
        l7policy_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["REDIRECT_PREFIX"],
        redirect_prefix: str,
        name: str | Omit = omit,
        position: int | Omit = omit,
        redirect_http_code: int | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LoadBalancerL7Policy:
        """Update L7 policy and poll for completion."""
        ...

    @overload
    def update_and_poll(
        self,
        l7policy_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["REDIRECT_TO_POOL"],
        redirect_pool_id: str,
        name: str | Omit = omit,
        position: int | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LoadBalancerL7Policy:
        """Update L7 policy and poll for completion."""
        ...

    @overload
    def update_and_poll(
        self,
        l7policy_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["REJECT"],
        name: str | Omit = omit,
        position: int | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LoadBalancerL7Policy:
        """Update L7 policy and poll for completion."""
        ...

    @required_args(
        ["action", "redirect_url"], ["action", "redirect_prefix"], ["action", "redirect_pool_id"], ["action"]
    )
    def update_and_poll(
        self,
        l7policy_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["REDIRECT_TO_URL"]
        | Literal["REDIRECT_PREFIX"]
        | Literal["REDIRECT_TO_POOL"]
        | Literal["REJECT"],
        redirect_url: str | Omit = omit,
        name: str | Omit = omit,
        position: int | Omit = omit,
        redirect_http_code: int | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        redirect_prefix: str | Omit = omit,
        redirect_pool_id: str | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LoadBalancerL7Policy:
        """Update L7 policy and poll for completion."""
        response: TaskIDList = self.update(  # type: ignore
            l7policy_id=l7policy_id,
            project_id=project_id,
            region_id=region_id,
            action=action,
            name=name,
            position=position,
            redirect_http_code=redirect_http_code,
            redirect_pool_id=redirect_pool_id,
            redirect_prefix=redirect_prefix,
            redirect_url=redirect_url,
            tags=tags,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks or len(response.tasks) != 1:  # type: ignore[union-attr]
            raise ValueError("Expected exactly one task to be created")
        self._client.cloud.tasks.poll(
            task_id=response.tasks[0],  # type: ignore[index]
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        return cast(
            LoadBalancerL7Policy,
            self.get(
                l7policy_id=l7policy_id,
                project_id=project_id,
                region_id=region_id,
                extra_headers=extra_headers,
                timeout=timeout,
            ),
        )


class AsyncL7PoliciesResourceCustomMixin:
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
        action: Literal["REDIRECT_TO_URL"],
        listener_id: str,
        redirect_url: str,
        name: str | Omit = omit,
        position: int | Omit = omit,
        redirect_http_code: int | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LoadBalancerL7Policy:
        """Create L7 policy and poll for completion."""
        ...

    @overload
    async def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["REDIRECT_PREFIX"],
        listener_id: str,
        redirect_prefix: str,
        name: str | Omit = omit,
        position: int | Omit = omit,
        redirect_http_code: int | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LoadBalancerL7Policy:
        """Create L7 policy and poll for completion."""
        ...

    @overload
    async def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["REDIRECT_TO_POOL"],
        listener_id: str,
        redirect_pool_id: str,
        name: str | Omit = omit,
        position: int | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LoadBalancerL7Policy:
        """Create L7 policy and poll for completion."""
        ...

    @overload
    async def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["REJECT"],
        listener_id: str,
        name: str | Omit = omit,
        position: int | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LoadBalancerL7Policy:
        """Create L7 policy and poll for completion."""
        ...

    @required_args(
        ["action", "listener_id", "redirect_url"],
        ["action", "listener_id", "redirect_prefix"],
        ["action", "listener_id", "redirect_pool_id"],
        ["action", "listener_id"],
    )
    async def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["REDIRECT_TO_URL"]
        | Literal["REDIRECT_PREFIX"]
        | Literal["REDIRECT_TO_POOL"]
        | Literal["REJECT"],
        listener_id: str,
        redirect_url: str | Omit = omit,
        name: str | Omit = omit,
        position: int | Omit = omit,
        redirect_http_code: int | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        redirect_prefix: str | Omit = omit,
        redirect_pool_id: str | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LoadBalancerL7Policy:
        """Create L7 policy and poll for completion."""
        response: TaskIDList = await self.create(  # type: ignore
            project_id=project_id,
            region_id=region_id,
            action=action,
            listener_id=listener_id,
            name=name,
            position=position,
            redirect_http_code=redirect_http_code,
            redirect_pool_id=redirect_pool_id,
            redirect_prefix=redirect_prefix,
            redirect_url=redirect_url,
            tags=tags,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks or len(response.tasks) != 1:  # type: ignore[union-attr]
            raise ValueError("Expected exactly one task to be created")
        task = await self._client.cloud.tasks.poll(
            task_id=response.tasks[0],  # type: ignore[index]
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        if (
            not task.created_resources
            or not task.created_resources.l7polices
            or len(task.created_resources.l7polices) != 1
        ):
            raise ValueError("Expected exactly one resource to be created in a task")
        return cast(
            LoadBalancerL7Policy,
            await self.get(
                l7policy_id=task.created_resources.l7polices[0],
                project_id=project_id,
                region_id=region_id,
                extra_headers=extra_headers,
                timeout=timeout,
            ),
        )

    async def delete_and_poll(
        self,
        l7policy_id: str,
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
        response = await self.delete(
            l7policy_id=l7policy_id,
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks or len(response.tasks) != 1:
            raise ValueError("Expected exactly one task to be created")
        await self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )

    @overload
    async def update_and_poll(
        self,
        l7policy_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["REDIRECT_TO_URL"],
        redirect_url: str,
        name: str | Omit = omit,
        position: int | Omit = omit,
        redirect_http_code: int | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LoadBalancerL7Policy:
        """Update L7 policy and poll for completion."""
        ...

    @overload
    async def update_and_poll(
        self,
        l7policy_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["REDIRECT_PREFIX"],
        redirect_prefix: str,
        name: str | Omit = omit,
        position: int | Omit = omit,
        redirect_http_code: int | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LoadBalancerL7Policy:
        """Update L7 policy and poll for completion."""
        ...

    @overload
    async def update_and_poll(
        self,
        l7policy_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["REDIRECT_TO_POOL"],
        redirect_pool_id: str,
        name: str | Omit = omit,
        position: int | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LoadBalancerL7Policy:
        """Update L7 policy and poll for completion."""
        ...

    @overload
    async def update_and_poll(
        self,
        l7policy_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["REJECT"],
        name: str | Omit = omit,
        position: int | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LoadBalancerL7Policy:
        """Update L7 policy and poll for completion."""
        ...

    @required_args(
        ["action", "redirect_url"], ["action", "redirect_prefix"], ["action", "redirect_pool_id"], ["action"]
    )
    async def update_and_poll(
        self,
        l7policy_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        action: Literal["REDIRECT_TO_URL"]
        | Literal["REDIRECT_PREFIX"]
        | Literal["REDIRECT_TO_POOL"]
        | Literal["REJECT"],
        redirect_url: str | Omit = omit,
        name: str | Omit = omit,
        position: int | Omit = omit,
        redirect_http_code: int | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        redirect_prefix: str | Omit = omit,
        redirect_pool_id: str | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LoadBalancerL7Policy:
        """Update L7 policy and poll for completion."""
        response: TaskIDList = await self.update(  # type: ignore
            l7policy_id=l7policy_id,
            project_id=project_id,
            region_id=region_id,
            action=action,
            name=name,
            position=position,
            redirect_http_code=redirect_http_code,
            redirect_pool_id=redirect_pool_id,
            redirect_prefix=redirect_prefix,
            redirect_url=redirect_url,
            tags=tags,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks or len(response.tasks) != 1:  # type: ignore[union-attr]
            raise ValueError("Expected exactly one task to be created")
        await self._client.cloud.tasks.poll(
            task_id=response.tasks[0],  # type: ignore[index]
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        return cast(
            LoadBalancerL7Policy,
            await self.get(
                l7policy_id=l7policy_id,
                project_id=project_id,
                region_id=region_id,
                extra_headers=extra_headers,
                timeout=timeout,
            ),
        )
