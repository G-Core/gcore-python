# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["RequestListResponse", "RequestedLimits", "RequestedLimitsGlobalLimits", "RequestedLimitsRegionalLimit"]


class RequestedLimitsGlobalLimits(BaseModel):
    inference_cpu_millicore_count_limit: Optional[int] = None
    """Inference CPU millicore count limit"""

    inference_gpu_a100_count_limit: Optional[int] = None
    """Inference GPU A100 Count limit"""

    inference_gpu_h100_count_limit: Optional[int] = None
    """Inference GPU H100 Count limit"""

    inference_gpu_l40s_count_limit: Optional[int] = None
    """Inference GPU L40s Count limit"""

    inference_instance_count_limit: Optional[int] = None
    """Inference instance count limit"""

    keypair_count_limit: Optional[int] = None
    """SSH Keys Count limit"""

    project_count_limit: Optional[int] = None
    """Projects Count limit"""


class RequestedLimitsRegionalLimit(BaseModel):
    baremetal_basic_count_limit: Optional[int] = None
    """Basic bare metal servers count limit"""

    baremetal_gpu_a100_count_limit: Optional[int] = None
    """Baremetal A100 GPU card count limit"""

    baremetal_gpu_count_limit: Optional[int] = None
    """AI GPU bare metal servers count limit"""

    baremetal_gpu_h100_count_limit: Optional[int] = None
    """Baremetal H100 GPU card count limit"""

    baremetal_gpu_l40s_count_limit: Optional[int] = None
    """Baremetal L40S GPU card count limit"""

    baremetal_hf_count_limit: Optional[int] = None
    """High-frequency bare metal servers count limit"""

    baremetal_infrastructure_count_limit: Optional[int] = None
    """Infrastructure bare metal servers count limit"""

    baremetal_network_count_limit: Optional[int] = None
    """Bare metal Network Count limit"""

    baremetal_storage_count_limit: Optional[int] = None
    """Storage bare metal servers count limit"""

    caas_container_count_limit: Optional[int] = None
    """Containers count limit"""

    caas_cpu_count_limit: Optional[int] = None
    """mCPU count for containers limit"""

    caas_gpu_count_limit: Optional[int] = None
    """Containers gpu count limit"""

    caas_ram_size_limit: Optional[int] = None
    """MB memory count for containers limit"""

    cluster_count_limit: Optional[int] = None
    """K8s clusters count limit"""

    cpu_count_limit: Optional[int] = None
    """vCPU Count limit"""

    dbaas_postgres_cluster_count_limit: Optional[int] = None
    """DBaaS cluster count limit"""

    external_ip_count_limit: Optional[int] = None
    """External IP Count limit"""

    faas_cpu_count_limit: Optional[int] = None
    """mCPU count for functions limit"""

    faas_function_count_limit: Optional[int] = None
    """Functions count limit"""

    faas_namespace_count_limit: Optional[int] = None
    """Functions namespace count limit"""

    faas_ram_size_limit: Optional[int] = None
    """MB memory count for functions limit"""

    firewall_count_limit: Optional[int] = None
    """Firewalls Count limit"""

    floating_count_limit: Optional[int] = None
    """Floating IP Count limit"""

    gpu_count_limit: Optional[int] = None
    """GPU Count limit"""

    gpu_virtual_a100_count_limit: Optional[int] = None
    """Virtual A100 GPU card count limit"""

    gpu_virtual_h100_count_limit: Optional[int] = None
    """Virtual H100 GPU card count limit"""

    gpu_virtual_l40s_count_limit: Optional[int] = None
    """Virtual L40S GPU card count limit"""

    image_count_limit: Optional[int] = None
    """Images Count limit"""

    image_size_limit: Optional[int] = None
    """Images Size, GiB limit"""

    ipu_count_limit: Optional[int] = None
    """IPU Count limit"""

    laas_topic_count_limit: Optional[int] = None
    """LaaS Topics Count limit"""

    loadbalancer_count_limit: Optional[int] = None
    """Load Balancers Count limit"""

    network_count_limit: Optional[int] = None
    """Networks Count limit"""

    ram_limit: Optional[int] = None
    """RAM Size, GiB limit"""

    region_id: Optional[int] = None
    """Region ID"""

    registry_count_limit: Optional[int] = None
    """Registries count limit"""

    registry_storage_limit: Optional[int] = None
    """Registries volume usage, GiB limit"""

    router_count_limit: Optional[int] = None
    """Routers Count limit"""

    secret_count_limit: Optional[int] = None
    """Secret Count limit"""

    servergroup_count_limit: Optional[int] = None
    """Placement Group Count limit"""

    sfs_count_limit: Optional[int] = None
    """Shared file system Count limit"""

    sfs_size_limit: Optional[int] = None
    """Shared file system Size, GiB limit"""

    shared_vm_count_limit: Optional[int] = None
    """Basic VMs Count limit"""

    snapshot_schedule_count_limit: Optional[int] = None
    """Snapshot Schedules Count limit"""

    subnet_count_limit: Optional[int] = None
    """Subnets Count limit"""

    vm_count_limit: Optional[int] = None
    """Instances Dedicated Count limit"""

    volume_count_limit: Optional[int] = None
    """Volumes Count limit"""

    volume_size_limit: Optional[int] = None
    """Volumes Size, GiB limit"""

    volume_snapshots_count_limit: Optional[int] = None
    """Snapshots Count limit"""

    volume_snapshots_size_limit: Optional[int] = None
    """Snapshots Size, GiB limit"""


class RequestedLimits(BaseModel):
    global_limits: Optional[RequestedLimitsGlobalLimits] = None
    """Global entity quota limits"""

    regional_limits: Optional[List[RequestedLimitsRegionalLimit]] = None
    """Regions and their quota limits"""


class RequestListResponse(BaseModel):
    id: int
    """Request ID"""

    client_id: int
    """Client ID"""

    requested_limits: RequestedLimits
    """Requested limits."""

    status: str
    """Request status"""

    created_at: Optional[datetime] = None
    """Datetime when the request was created."""

    description: Optional[str] = None
    """Describe the reason, in general terms."""

    updated_at: Optional[datetime] = None
    """Datetime when the request was updated."""
