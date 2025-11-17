# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["AuditLogListParams"]


class AuditLogListParams(TypedDict, total=False):
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
    """User action type. Several options can be specified."""

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
    """API group that requested action belongs to. Several options can be specified."""

    from_timestamp: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """ISO formatted datetime string.

    Starting timestamp from which user actions are requested
    """

    limit: int
    """Optional. Limit the number of returned items"""

    offset: int
    """Optional.

    Offset value is used to exclude the first set of records from the result
    """

    order_by: Literal["asc", "desc"]
    """Sorting by timestamp. Oldest first, or most recent first"""

    project_id: Iterable[int]
    """Project ID. Several options can be specified."""

    region_id: Iterable[int]
    """Region ID. Several options can be specified."""

    resource_id: SequenceNotStr[str]
    """Resource ID. Several options can be specified."""

    search_field: str
    """
    Extra search field for common object properties such as name, IP address, or
    other, depending on the `resource_type`
    """

    sorting: Literal["asc", "desc"]
    """(DEPRECATED Use '`order_by`' instead) Sorting by timestamp.

    Oldest first, or most recent first
    """

    source_user_ips: SequenceNotStr[str]
    """Originating IP address of the client making the request.

    Several options can be specified.
    """

    to_timestamp: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """ISO formatted datetime string.

    Ending timestamp until which user actions are requested
    """

    user_agents: SequenceNotStr[str]
    """User-Agent string identifying the client making the request.

    Several options can be specified.
    """
