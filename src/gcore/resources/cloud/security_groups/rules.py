# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.cloud.task_id_list import TaskIDList
from ....types.cloud.security_groups import rule_create_params

__all__ = ["RulesResource", "AsyncRulesResource"]


class RulesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return RulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return RulesResourceWithStreamingResponse(self)

    def create(
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
            "any",
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """Add a new rule to an existing security group.

        Returns a task ID for tracking the
        asynchronous operation.

        Args:
          project_id: Project ID

          region_id: Region ID

          group_id: Security group ID

          direction: Ingress or egress, which is the direction in which the security group is applied

          description: Rule description

          ethertype: Ether type

          port_range_max: The maximum port number in the range that is matched by the security group rule

          port_range_min: The minimum port number in the range that is matched by the security group rule

          protocol: Protocol

          remote_group_id: The remote group UUID to associate with this security group

          remote_ip_prefix: The remote IP prefix that is matched by this security group rule

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return self._post(
            f"/cloud/v2/security_groups/{project_id}/{region_id}/{group_id}/rules",
            body=maybe_transform(
                {
                    "direction": direction,
                    "description": description,
                    "ethertype": ethertype,
                    "port_range_max": port_range_max,
                    "port_range_min": port_range_min,
                    "protocol": protocol,
                    "remote_group_id": remote_group_id,
                    "remote_ip_prefix": remote_ip_prefix,
                },
                rule_create_params.RuleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def delete(
        self,
        rule_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        group_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """Delete a specific rule from a security group.

        Returns a task ID for tracking the
        asynchronous operation.

        Args:
          project_id: Project ID

          region_id: Region ID

          group_id: Security group ID

          rule_id: Security group rule ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return self._delete(
            f"/cloud/v2/security_groups/{project_id}/{region_id}/{group_id}/rules/{rule_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )


class AsyncRulesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncRulesResourceWithStreamingResponse(self)

    async def create(
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
            "any",
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """Add a new rule to an existing security group.

        Returns a task ID for tracking the
        asynchronous operation.

        Args:
          project_id: Project ID

          region_id: Region ID

          group_id: Security group ID

          direction: Ingress or egress, which is the direction in which the security group is applied

          description: Rule description

          ethertype: Ether type

          port_range_max: The maximum port number in the range that is matched by the security group rule

          port_range_min: The minimum port number in the range that is matched by the security group rule

          protocol: Protocol

          remote_group_id: The remote group UUID to associate with this security group

          remote_ip_prefix: The remote IP prefix that is matched by this security group rule

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return await self._post(
            f"/cloud/v2/security_groups/{project_id}/{region_id}/{group_id}/rules",
            body=await async_maybe_transform(
                {
                    "direction": direction,
                    "description": description,
                    "ethertype": ethertype,
                    "port_range_max": port_range_max,
                    "port_range_min": port_range_min,
                    "protocol": protocol,
                    "remote_group_id": remote_group_id,
                    "remote_ip_prefix": remote_ip_prefix,
                },
                rule_create_params.RuleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def delete(
        self,
        rule_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        group_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """Delete a specific rule from a security group.

        Returns a task ID for tracking the
        asynchronous operation.

        Args:
          project_id: Project ID

          region_id: Region ID

          group_id: Security group ID

          rule_id: Security group rule ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return await self._delete(
            f"/cloud/v2/security_groups/{project_id}/{region_id}/{group_id}/rules/{rule_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )


class RulesResourceWithRawResponse:
    def __init__(self, rules: RulesResource) -> None:
        self._rules = rules

        self.create = to_raw_response_wrapper(
            rules.create,
        )
        self.delete = to_raw_response_wrapper(
            rules.delete,
        )


class AsyncRulesResourceWithRawResponse:
    def __init__(self, rules: AsyncRulesResource) -> None:
        self._rules = rules

        self.create = async_to_raw_response_wrapper(
            rules.create,
        )
        self.delete = async_to_raw_response_wrapper(
            rules.delete,
        )


class RulesResourceWithStreamingResponse:
    def __init__(self, rules: RulesResource) -> None:
        self._rules = rules

        self.create = to_streamed_response_wrapper(
            rules.create,
        )
        self.delete = to_streamed_response_wrapper(
            rules.delete,
        )


class AsyncRulesResourceWithStreamingResponse:
    def __init__(self, rules: AsyncRulesResource) -> None:
        self._rules = rules

        self.create = async_to_streamed_response_wrapper(
            rules.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            rules.delete,
        )
