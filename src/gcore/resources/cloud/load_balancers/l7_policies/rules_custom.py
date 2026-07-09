# Custom code. This file is not generated and is preserved across codegen runs.
# It isolates hand-written *_and_poll convenience methods from generated code to
# eliminate merge conflicts.

from __future__ import annotations

from typing import TYPE_CHECKING, Any, cast
from typing_extensions import Literal

import httpx

from ....._types import NOT_GIVEN, Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit
from .....types.cloud.load_balancer_l7_rule import LoadBalancerL7Rule

if TYPE_CHECKING:
    from ....._client import Gcore, AsyncGcore


class RulesResourceCustomMixin:
    if TYPE_CHECKING:
        # Provided by the concrete generated resource class this mixin is
        # combined with; declared here so client-derived locals keep their
        # real types and other resource methods resolve via __getattr__.
        _client: Gcore

        def __getattr__(self, name: str) -> Any: ...

    def create_and_poll(
        self,
        l7policy_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        compare_type: Literal["CONTAINS", "ENDS_WITH", "EQUAL_TO", "REGEX", "STARTS_WITH"],
        type: Literal[
            "COOKIE",
            "FILE_TYPE",
            "HEADER",
            "HOST_NAME",
            "PATH",
            "SSL_CONN_HAS_CERT",
            "SSL_DN_FIELD",
            "SSL_VERIFY_RESULT",
        ],
        value: str,
        invert: bool | Omit = omit,
        key: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LoadBalancerL7Rule:
        response = self.create(
            l7policy_id=l7policy_id,
            project_id=project_id,
            region_id=region_id,
            compare_type=compare_type,
            type=type,
            value=value,
            invert=invert,
            key=key,
            tags=tags,
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
        if not task.created_resources or not task.created_resources.l7rules or len(task.created_resources.l7rules) != 1:
            raise ValueError("Expected exactly one resource to be created in a task")
        return cast(
            LoadBalancerL7Rule,
            self.get(
                l7rule_id=task.created_resources.l7rules[0],
                project_id=project_id,
                region_id=region_id,
                l7policy_id=l7policy_id,
                extra_headers=extra_headers,
                timeout=timeout,
            ),
        )

    def delete_and_poll(
        self,
        l7rule_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        l7policy_id: str,
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
        Delete L7 rule and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.delete(
            l7rule_id=l7rule_id,
            project_id=project_id,
            region_id=region_id,
            l7policy_id=l7policy_id,
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

    def replace_and_poll(
        self,
        l7rule_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        l7policy_id: str,
        compare_type: Literal["CONTAINS", "ENDS_WITH", "EQUAL_TO", "REGEX", "STARTS_WITH"],
        type: Literal[
            "COOKIE",
            "FILE_TYPE",
            "HEADER",
            "HOST_NAME",
            "PATH",
            "SSL_CONN_HAS_CERT",
            "SSL_DN_FIELD",
            "SSL_VERIFY_RESULT",
        ],
        value: str,
        invert: bool | Omit = omit,
        key: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LoadBalancerL7Rule:
        """
        Replace L7 rule and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.replace(
            l7rule_id=l7rule_id,
            project_id=project_id,
            region_id=region_id,
            l7policy_id=l7policy_id,
            compare_type=compare_type,
            type=type,
            value=value,
            invert=invert,
            key=key,
            tags=tags,
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
        return cast(
            LoadBalancerL7Rule,
            self.get(
                l7rule_id=l7rule_id,
                project_id=project_id,
                region_id=region_id,
                l7policy_id=l7policy_id,
                extra_headers=extra_headers,
                timeout=timeout,
            ),
        )


class AsyncRulesResourceCustomMixin:
    if TYPE_CHECKING:
        # Provided by the concrete generated resource class this mixin is
        # combined with; declared here so client-derived locals keep their
        # real types and other resource methods resolve via __getattr__.
        _client: AsyncGcore

        def __getattr__(self, name: str) -> Any: ...

    async def create_and_poll(
        self,
        l7policy_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        compare_type: Literal["CONTAINS", "ENDS_WITH", "EQUAL_TO", "REGEX", "STARTS_WITH"],
        type: Literal[
            "COOKIE",
            "FILE_TYPE",
            "HEADER",
            "HOST_NAME",
            "PATH",
            "SSL_CONN_HAS_CERT",
            "SSL_DN_FIELD",
            "SSL_VERIFY_RESULT",
        ],
        value: str,
        invert: bool | Omit = omit,
        key: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LoadBalancerL7Rule:
        response = await self.create(
            l7policy_id=l7policy_id,
            project_id=project_id,
            region_id=region_id,
            compare_type=compare_type,
            type=type,
            value=value,
            invert=invert,
            key=key,
            tags=tags,
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
        if not task.created_resources or not task.created_resources.l7rules or len(task.created_resources.l7rules) != 1:
            raise ValueError("Expected exactly one resource to be created in a task")
        return cast(
            LoadBalancerL7Rule,
            await self.get(
                l7rule_id=task.created_resources.l7rules[0],
                project_id=project_id,
                region_id=region_id,
                l7policy_id=l7policy_id,
                extra_headers=extra_headers,
                timeout=timeout,
            ),
        )

    async def delete_and_poll(
        self,
        l7rule_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        l7policy_id: str,
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
        Delete L7 rule and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.delete(
            l7rule_id=l7rule_id,
            project_id=project_id,
            region_id=region_id,
            l7policy_id=l7policy_id,
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

    async def replace_and_poll(
        self,
        l7rule_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        l7policy_id: str,
        compare_type: Literal["CONTAINS", "ENDS_WITH", "EQUAL_TO", "REGEX", "STARTS_WITH"],
        type: Literal[
            "COOKIE",
            "FILE_TYPE",
            "HEADER",
            "HOST_NAME",
            "PATH",
            "SSL_CONN_HAS_CERT",
            "SSL_DN_FIELD",
            "SSL_VERIFY_RESULT",
        ],
        value: str,
        invert: bool | Omit = omit,
        key: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> LoadBalancerL7Rule:
        """
        Replace L7 rule and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.replace(
            l7rule_id=l7rule_id,
            project_id=project_id,
            region_id=region_id,
            l7policy_id=l7policy_id,
            compare_type=compare_type,
            type=type,
            value=value,
            invert=invert,
            key=key,
            tags=tags,
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
        return cast(
            LoadBalancerL7Rule,
            await self.get(
                l7rule_id=l7rule_id,
                project_id=project_id,
                region_id=region_id,
                l7policy_id=l7policy_id,
                extra_headers=extra_headers,
                timeout=timeout,
            ),
        )
