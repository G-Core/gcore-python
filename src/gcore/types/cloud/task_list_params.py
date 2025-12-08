# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TaskListParams"]


class TaskListParams(TypedDict, total=False):
    from_timestamp: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """ISO formatted datetime string.

    Filter the tasks by creation date greater than or equal to `from_timestamp`
    """

    is_acknowledged: bool
    """Filter the tasks by their acknowledgement status"""

    limit: int
    """Limit the number of returned tasks.

    Falls back to default of 10 if not specified. Limited by max limit value of 1000
    """

    offset: int
    """Offset value is used to exclude the first set of records from the result"""

    order_by: Literal["asc", "desc"]
    """Sorting by creation date. Oldest first, or most recent first"""

    project_id: Iterable[int]
    """The project ID to filter the tasks by project.

    Supports multiple values of kind key=value1&key=value2
    """

    region_id: Iterable[int]
    """The region ID to filter the tasks by region.

    Supports multiple values of kind key=value1&key=value2
    """

    sorting: Literal["asc", "desc"]
    """(DEPRECATED Use '`order_by`' instead) Sorting by creation date.

    Oldest first, or most recent first
    """

    state: List[Literal["ERROR", "FINISHED", "NEW", "RUNNING"]]
    """Filter the tasks by state.

    Supports multiple values of kind key=value1&key=value2
    """

    task_type: str
    """
    Filter the tasks by their type one of ['`activate_ddos_profile`',
    '`attach_bm_to_reserved_fixed_ip`', '`attach_vm_interface`',
    '`attach_vm_to_reserved_fixed_ip`', '`attach_volume`',
    '`create_ai_cluster_gpu`', '`create_bm`', '`create_caas_container`',
    '`create_dbaas_postgres_cluster`', '`create_ddos_profile`',
    '`create_faas_function`', '`create_faas_namespace`', '`create_fip`',
    '`create_gpu_virtual_cluster`', '`create_image`',
    '`create_inference_application`', '`create_inference_instance`',
    '`create_k8s_cluster_pool_v2`', '`create_k8s_cluster_v2`', '`create_l7policy`',
    '`create_l7rule`', '`create_lblistener`', '`create_lbmember`',
    '`create_lbpool`', '`create_lbpool_health_monitor`', '`create_loadbalancer`',
    '`create_network`', '`create_reserved_fixed_ip`', '`create_router`',
    '`create_secret`', '`create_servergroup`', '`create_sfs`', '`create_snapshot`',
    '`create_subnet`', '`create_vm`', '`create_volume`',
    '`deactivate_ddos_profile`', '`delete_ai_cluster_gpu`',
    '`delete_caas_container`', '`delete_dbaas_postgres_cluster`',
    '`delete_ddos_profile`', '`delete_faas_function`', '`delete_faas_namespace`',
    '`delete_fip`', '`delete_gpu_virtual_cluster`', '`delete_gpu_virtual_server`',
    '`delete_image`', '`delete_inference_application`',
    '`delete_inference_instance`', '`delete_k8s_cluster_pool_v2`',
    '`delete_k8s_cluster_v2`', '`delete_l7policy`', '`delete_l7rule`',
    '`delete_lblistener`', '`delete_lbmember`', '`delete_lbmetadata`',
    '`delete_lbpool`', '`delete_loadbalancer`', '`delete_network`',
    '`delete_project`', '`delete_reserved_fixed_ip`', '`delete_router`',
    '`delete_secret`', '`delete_servergroup`', '`delete_sfs`', '`delete_snapshot`',
    '`delete_subnet`', '`delete_vm`', '`delete_volume`', '`detach_vm_interface`',
    '`detach_volume`', '`download_image`', '`downscale_ai_cluster_gpu`',
    '`downscale_gpu_virtual_cluster`', '`extend_sfs`', '`extend_volume`',
    '`failover_loadbalancer`', '`hard_reboot_gpu_baremetal_server`',
    '`hard_reboot_gpu_virtual_cluster`', '`hard_reboot_gpu_virtual_server`',
    '`hard_reboot_vm`', '`patch_caas_container`', '`patch_dbaas_postgres_cluster`',
    '`patch_faas_function`', '`patch_faas_namespace`', '`patch_lblistener`',
    '`patch_lbpool`', '`put_into_server_group`', '`put_l7rule`', '`rebuild_bm`',
    '`rebuild_gpu_baremetal_node`', '`remove_from_server_group`',
    '`replace_lbmetadata`', '`resize_k8s_cluster_v2`', '`resize_loadbalancer`',
    '`resize_vm`', '`resume_vm`', '`revert_volume`',
    '`soft_reboot_gpu_baremetal_server`', '`soft_reboot_gpu_virtual_cluster`',
    '`soft_reboot_gpu_virtual_server`', '`soft_reboot_vm`',
    '`start_gpu_baremetal_server`', '`start_gpu_virtual_cluster`',
    '`start_gpu_virtual_server`', '`start_vm`', '`stop_gpu_baremetal_server`',
    '`stop_gpu_virtual_cluster`', '`stop_gpu_virtual_server`', '`stop_vm`',
    '`suspend_vm`', '`sync_private_flavors`', '`update_ddos_profile`',
    '`update_inference_application`', '`update_inference_instance`',
    '`update_k8s_cluster_v2`', '`update_l7policy`', '`update_lbmetadata`',
    '`update_port_allowed_address_pairs`', '`update_sfs`',
    '`update_tags_gpu_virtual_cluster`', '`upgrade_k8s_cluster_v2`',
    '`upscale_ai_cluster_gpu`', '`upscale_gpu_virtual_cluster`']
    """

    to_timestamp: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """ISO formatted datetime string.

    Filter the tasks by creation date less than or equal to `to_timestamp`
    """
