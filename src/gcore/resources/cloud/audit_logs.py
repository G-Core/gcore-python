# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncOffsetPage, AsyncOffsetPage
from ...types.cloud import audit_log_list_params
from ..._base_client import AsyncPaginator, make_request_options
from ...types.cloud.audit_log_entry import AuditLogEntry

__all__ = ["AuditLogsResource", "AsyncAuditLogsResource"]


class AuditLogsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuditLogsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AuditLogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuditLogsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AuditLogsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        action_type: List[
            Literal[
                "activate",
                "attach",
                "change_logging_resources",
                "create",
                "create_access_rule",
                "deactivate",
                "delete",
                "delete_access_rule",
                "delete_metadata",
                "detach",
                "disable_logging",
                "disable_portsecurity",
                "download",
                "enable_logging",
                "enable_portsecurity",
                "failover",
                "put_into_servergroup",
                "reboot",
                "reboot_hard",
                "rebuild",
                "regenerate_credentials",
                "remove_from_servergroup",
                "replace_metadata",
                "resize",
                "resume",
                "retype",
                "revert",
                "scale_down",
                "scale_up",
                "start",
                "stop",
                "suspend",
                "update",
                "update_metadata",
                "upgrade",
            ]
        ]
        | Omit = omit,
        api_group: List[
            Literal[
                "ai_cluster",
                "backup_service",
                "caas_container",
                "caas_key",
                "caas_pull_secret",
                "dbaas_postgres",
                "ddos_profile",
                "faas_function",
                "faas_key",
                "faas_namespace",
                "file_shares",
                "floating_ip",
                "image",
                "inference_at_the_edge",
                "instance",
                "instance_isolation",
                "k8s_cluster",
                "k8s_cluster_template",
                "k8s_pool",
                "laas",
                "laas_topic",
                "lb_health_monitor",
                "lb_l7policy",
                "lb_l7rule",
                "lblistener",
                "lbpool",
                "lbpool_member",
                "lifecycle_policy",
                "lifecycle_policy_volume_member",
                "loadbalancer",
                "network",
                "port",
                "project",
                "quota_limit_request",
                "registry",
                "reservation",
                "reserved_fixed_ip",
                "role",
                "router",
                "secret",
                "securitygroup",
                "securitygrouprule",
                "servergroup",
                "shared_flavor",
                "shared_image",
                "shared_network",
                "snapshot",
                "snapshot_schedule",
                "ssh_key",
                "subnet",
                "user",
                "vip_ip_addresses",
                "volume",
            ]
        ]
        | Omit = omit,
        from_timestamp: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        order_by: Literal["asc", "desc"] | Omit = omit,
        project_id: Iterable[int] | Omit = omit,
        region_id: Iterable[int] | Omit = omit,
        resource_id: SequenceNotStr[str] | Omit = omit,
        search_field: str | Omit = omit,
        sorting: Literal["asc", "desc"] | Omit = omit,
        source_user_ips: SequenceNotStr[str] | Omit = omit,
        to_timestamp: Union[str, datetime] | Omit = omit,
        user_agents: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[AuditLogEntry]:
        """
        Retrieve user action log for one client or a set of projects

        Args:
          action_type: User action type. Several options can be specified.

          api_group: API group that requested action belongs to. Several options can be specified.

          from_timestamp: ISO formatted datetime string. Starting timestamp from which user actions are
              requested

          limit: Optional. Limit the number of returned items

          offset: Optional. Offset value is used to exclude the first set of records from the
              result

          order_by: Sorting by timestamp. Oldest first, or most recent first

          project_id: Project ID. Several options can be specified.

          region_id: Region ID. Several options can be specified.

          resource_id: Resource ID. Several options can be specified.

          search_field: Extra search field for common object properties such as name, IP address, or
              other, depending on the `resource_type`

          sorting: (DEPRECATED Use '`order_by`' instead) Sorting by timestamp. Oldest first, or
              most recent first

          source_user_ips: Originating IP address of the client making the request. Several options can be
              specified.

          to_timestamp: ISO formatted datetime string. Ending timestamp until which user actions are
              requested

          user_agents: User-Agent string identifying the client making the request. Several options can
              be specified.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/cloud/v1/user_actions",
            page=SyncOffsetPage[AuditLogEntry],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "action_type": action_type,
                        "api_group": api_group,
                        "from_timestamp": from_timestamp,
                        "limit": limit,
                        "offset": offset,
                        "order_by": order_by,
                        "project_id": project_id,
                        "region_id": region_id,
                        "resource_id": resource_id,
                        "search_field": search_field,
                        "sorting": sorting,
                        "source_user_ips": source_user_ips,
                        "to_timestamp": to_timestamp,
                        "user_agents": user_agents,
                    },
                    audit_log_list_params.AuditLogListParams,
                ),
            ),
            model=AuditLogEntry,
        )


class AsyncAuditLogsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAuditLogsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAuditLogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuditLogsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncAuditLogsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        action_type: List[
            Literal[
                "activate",
                "attach",
                "change_logging_resources",
                "create",
                "create_access_rule",
                "deactivate",
                "delete",
                "delete_access_rule",
                "delete_metadata",
                "detach",
                "disable_logging",
                "disable_portsecurity",
                "download",
                "enable_logging",
                "enable_portsecurity",
                "failover",
                "put_into_servergroup",
                "reboot",
                "reboot_hard",
                "rebuild",
                "regenerate_credentials",
                "remove_from_servergroup",
                "replace_metadata",
                "resize",
                "resume",
                "retype",
                "revert",
                "scale_down",
                "scale_up",
                "start",
                "stop",
                "suspend",
                "update",
                "update_metadata",
                "upgrade",
            ]
        ]
        | Omit = omit,
        api_group: List[
            Literal[
                "ai_cluster",
                "backup_service",
                "caas_container",
                "caas_key",
                "caas_pull_secret",
                "dbaas_postgres",
                "ddos_profile",
                "faas_function",
                "faas_key",
                "faas_namespace",
                "file_shares",
                "floating_ip",
                "image",
                "inference_at_the_edge",
                "instance",
                "instance_isolation",
                "k8s_cluster",
                "k8s_cluster_template",
                "k8s_pool",
                "laas",
                "laas_topic",
                "lb_health_monitor",
                "lb_l7policy",
                "lb_l7rule",
                "lblistener",
                "lbpool",
                "lbpool_member",
                "lifecycle_policy",
                "lifecycle_policy_volume_member",
                "loadbalancer",
                "network",
                "port",
                "project",
                "quota_limit_request",
                "registry",
                "reservation",
                "reserved_fixed_ip",
                "role",
                "router",
                "secret",
                "securitygroup",
                "securitygrouprule",
                "servergroup",
                "shared_flavor",
                "shared_image",
                "shared_network",
                "snapshot",
                "snapshot_schedule",
                "ssh_key",
                "subnet",
                "user",
                "vip_ip_addresses",
                "volume",
            ]
        ]
        | Omit = omit,
        from_timestamp: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        order_by: Literal["asc", "desc"] | Omit = omit,
        project_id: Iterable[int] | Omit = omit,
        region_id: Iterable[int] | Omit = omit,
        resource_id: SequenceNotStr[str] | Omit = omit,
        search_field: str | Omit = omit,
        sorting: Literal["asc", "desc"] | Omit = omit,
        source_user_ips: SequenceNotStr[str] | Omit = omit,
        to_timestamp: Union[str, datetime] | Omit = omit,
        user_agents: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AuditLogEntry, AsyncOffsetPage[AuditLogEntry]]:
        """
        Retrieve user action log for one client or a set of projects

        Args:
          action_type: User action type. Several options can be specified.

          api_group: API group that requested action belongs to. Several options can be specified.

          from_timestamp: ISO formatted datetime string. Starting timestamp from which user actions are
              requested

          limit: Optional. Limit the number of returned items

          offset: Optional. Offset value is used to exclude the first set of records from the
              result

          order_by: Sorting by timestamp. Oldest first, or most recent first

          project_id: Project ID. Several options can be specified.

          region_id: Region ID. Several options can be specified.

          resource_id: Resource ID. Several options can be specified.

          search_field: Extra search field for common object properties such as name, IP address, or
              other, depending on the `resource_type`

          sorting: (DEPRECATED Use '`order_by`' instead) Sorting by timestamp. Oldest first, or
              most recent first

          source_user_ips: Originating IP address of the client making the request. Several options can be
              specified.

          to_timestamp: ISO formatted datetime string. Ending timestamp until which user actions are
              requested

          user_agents: User-Agent string identifying the client making the request. Several options can
              be specified.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/cloud/v1/user_actions",
            page=AsyncOffsetPage[AuditLogEntry],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "action_type": action_type,
                        "api_group": api_group,
                        "from_timestamp": from_timestamp,
                        "limit": limit,
                        "offset": offset,
                        "order_by": order_by,
                        "project_id": project_id,
                        "region_id": region_id,
                        "resource_id": resource_id,
                        "search_field": search_field,
                        "sorting": sorting,
                        "source_user_ips": source_user_ips,
                        "to_timestamp": to_timestamp,
                        "user_agents": user_agents,
                    },
                    audit_log_list_params.AuditLogListParams,
                ),
            ),
            model=AuditLogEntry,
        )


class AuditLogsResourceWithRawResponse:
    def __init__(self, audit_logs: AuditLogsResource) -> None:
        self._audit_logs = audit_logs

        self.list = to_raw_response_wrapper(
            audit_logs.list,
        )


class AsyncAuditLogsResourceWithRawResponse:
    def __init__(self, audit_logs: AsyncAuditLogsResource) -> None:
        self._audit_logs = audit_logs

        self.list = async_to_raw_response_wrapper(
            audit_logs.list,
        )


class AuditLogsResourceWithStreamingResponse:
    def __init__(self, audit_logs: AuditLogsResource) -> None:
        self._audit_logs = audit_logs

        self.list = to_streamed_response_wrapper(
            audit_logs.list,
        )


class AsyncAuditLogsResourceWithStreamingResponse:
    def __init__(self, audit_logs: AsyncAuditLogsResource) -> None:
        self._audit_logs = audit_logs

        self.list = async_to_streamed_response_wrapper(
            audit_logs.list,
        )
