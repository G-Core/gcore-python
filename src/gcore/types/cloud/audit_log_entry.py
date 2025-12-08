# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AuditLogEntry", "Resource", "TotalPrice"]


class Resource(BaseModel):
    resource_id: str
    """Resource ID"""

    resource_type: Literal[
        "caas_container",
        "caas_key",
        "caas_pull_secret",
        "dbaas_postgres",
        "ddos_profile",
        "external_ip",
        "faas_function",
        "faas_key",
        "faas_namespace",
        "file_shares",
        "floating_ip",
        "gpu_baremetal_server",
        "gpu_virtual_server",
        "gpuai_cluster",
        "image",
        "inference_api_key",
        "inference_application",
        "inference_instance",
        "inference_registry_credentials",
        "inference_secret",
        "instance",
        "ipu_cluster",
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
        "registry_repository",
        "registry_repository_artifact",
        "registry_repository_tag",
        "registry_user",
        "registry_user_sercret",
        "reservation",
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
        "token",
        "user",
        "virtual_gpu_cluster",
        "volume",
    ]
    """Resource type"""

    resource_body: Optional[Dict[str, object]] = None
    """Free-form object, resource body."""

    search_field: Optional[str] = None
    """Often used property for filtering actions.

    It can be a name, IP address, or other property, depending on the
    `resource_type`
    """


class TotalPrice(BaseModel):
    """Total resource price VAT inclusive"""

    currency_code: Optional[str] = None
    """Currency code (3 letter code per ISO 4217)"""

    price_per_hour: Optional[float] = None
    """Total price VAT inclusive per hour"""

    price_per_month: Optional[float] = None
    """Total price VAT inclusive per month (30 days)"""

    price_status: Literal["error", "hide", "show"]
    """Price status for the UI"""


class AuditLogEntry(BaseModel):
    id: str
    """User action ID"""

    acknowledged: bool
    """
    User action log was successfully received by its subscriber in case there is one
    """

    action_data: Optional[Dict[str, object]] = None
    """Additional information about the action"""

    action_type: Literal[
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
    """Action type"""

    api_group: Literal[
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
    """API group"""

    client_id: Optional[int] = None
    """Client ID of the user."""

    email: Optional[str] = None
    """User email address"""

    is_complete: bool
    """User action was filled with all necessary information.

    If false, then something went wrong during user action creation or update
    """

    issued_by_user_id: Optional[int] = None
    """User ID who issued the token that made the request"""

    project_id: Optional[int] = None
    """Project ID"""

    region_id: Optional[int] = None
    """Region ID"""

    resources: List[Resource]
    """Resources"""

    source_user_ip: Optional[str] = None
    """User IP that made the request"""

    task_id: Optional[str] = None
    """Task ID"""

    timestamp: datetime
    """Datetime. Action timestamp"""

    token_id: Optional[int] = None
    """Token ID"""

    total_price: Optional[TotalPrice] = None
    """Total resource price VAT inclusive"""

    user_agent: Optional[str] = None
    """User-Agent that made the request"""

    user_id: int
    """User ID"""
