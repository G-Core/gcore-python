# Custom code. This file is not generated and is preserved across codegen runs.
# It isolates hand-written *_and_poll convenience methods from generated code to
# eliminate merge conflicts.

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....types.cloud.security_group_rule import SecurityGroupRule

if TYPE_CHECKING:
    from ...._client import Gcore, AsyncGcore


class RulesResourceCustomMixin:
    if TYPE_CHECKING:
        # Provided by the concrete generated resource class this mixin is
        # combined with; declared here so client-derived locals keep their
        # real types and other resource methods resolve via __getattr__.
        _client: Gcore

        def __getattr__(self, name: str) -> Any: ...

    def create_and_poll(
        self,
        group_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        direction: Literal["egress", "ingress"],
        description: str | Omit = omit,
        ethertype: Literal["IPv4", "IPv6"] | Omit = omit,
        port_range_max: Optional[int] | Omit = omit,
        port_range_min: Optional[int] | Omit = omit,
        protocol: Literal[
            "ah",
            "dccp",
            "egp",
            "esp",
            "gre",
            "icmp",
            "igmp",
            "ipencap",
            "ipip",
            "ipv6-encap",
            "ipv6-frag",
            "ipv6-icmp",
            "ipv6-nonxt",
            "ipv6-opts",
            "ipv6-route",
            "ospf",
            "pgm",
            "rsvp",
            "sctp",
            "tcp",
            "udp",
            "udplite",
            "vrrp",
        ]
        | Omit = omit,
        remote_group_id: str | Omit = omit,
        remote_ip_prefix: Optional[str] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SecurityGroupRule:
        """Create a security group rule and poll for completion.

        After the task completes, fetches the parent security group and returns the created rule.
        """
        response = self.create(
            group_id=group_id,
            project_id=project_id,
            region_id=region_id,
            direction=direction,
            description=description,
            ethertype=ethertype,
            port_range_max=port_range_max,
            port_range_min=port_range_min,
            protocol=protocol,
            remote_group_id=remote_group_id,
            remote_ip_prefix=remote_ip_prefix,
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
            or not task.created_resources.security_group_rules
            or len(task.created_resources.security_group_rules) != 1
        ):
            raise ValueError("Expected exactly one security group rule to be created in a task")
        rule_id = task.created_resources.security_group_rules[0]

        # No individual GET for rules — read through parent security group
        sg = self._client.cloud.security_groups.get(
            group_id=group_id,
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
            timeout=timeout,
        )
        for rule in sg.security_group_rules or []:
            if rule.id == rule_id:
                return rule
        raise ValueError(f"Rule {rule_id} not found in security group {group_id} after creation")

    def delete_and_poll(
        self,
        rule_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        group_id: str,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a security group rule and poll for completion.

        Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.delete(
            rule_id=rule_id,
            project_id=project_id,
            region_id=region_id,
            group_id=group_id,
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


class AsyncRulesResourceCustomMixin:
    if TYPE_CHECKING:
        # Provided by the concrete generated resource class this mixin is
        # combined with; declared here so client-derived locals keep their
        # real types and other resource methods resolve via __getattr__.
        _client: AsyncGcore

        def __getattr__(self, name: str) -> Any: ...

    async def create_and_poll(
        self,
        group_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        direction: Literal["egress", "ingress"],
        description: str | Omit = omit,
        ethertype: Literal["IPv4", "IPv6"] | Omit = omit,
        port_range_max: Optional[int] | Omit = omit,
        port_range_min: Optional[int] | Omit = omit,
        protocol: Literal[
            "ah",
            "dccp",
            "egp",
            "esp",
            "gre",
            "icmp",
            "igmp",
            "ipencap",
            "ipip",
            "ipv6-encap",
            "ipv6-frag",
            "ipv6-icmp",
            "ipv6-nonxt",
            "ipv6-opts",
            "ipv6-route",
            "ospf",
            "pgm",
            "rsvp",
            "sctp",
            "tcp",
            "udp",
            "udplite",
            "vrrp",
        ]
        | Omit = omit,
        remote_group_id: str | Omit = omit,
        remote_ip_prefix: Optional[str] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SecurityGroupRule:
        """Create a security group rule and poll for completion.

        After the task completes, fetches the parent security group and returns the created rule.
        """
        response = await self.create(
            group_id=group_id,
            project_id=project_id,
            region_id=region_id,
            direction=direction,
            description=description,
            ethertype=ethertype,
            port_range_max=port_range_max,
            port_range_min=port_range_min,
            protocol=protocol,
            remote_group_id=remote_group_id,
            remote_ip_prefix=remote_ip_prefix,
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
            or not task.created_resources.security_group_rules
            or len(task.created_resources.security_group_rules) != 1
        ):
            raise ValueError("Expected exactly one security group rule to be created in a task")
        rule_id = task.created_resources.security_group_rules[0]

        # No individual GET for rules — read through parent security group
        sg = await self._client.cloud.security_groups.get(
            group_id=group_id,
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
            timeout=timeout,
        )
        for rule in sg.security_group_rules or []:
            if rule.id == rule_id:
                return rule
        raise ValueError(f"Rule {rule_id} not found in security group {group_id} after creation")

    async def delete_and_poll(
        self,
        rule_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        group_id: str,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a security group rule and poll for completion.

        Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.delete(
            rule_id=rule_id,
            project_id=project_id,
            region_id=region_id,
            group_id=group_id,
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
