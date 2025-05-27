# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["QuotaGetByRegionResponse"]


class QuotaGetByRegionResponse(BaseModel):
    baremetal_basic_count_limit: Optional[int] = None
    """Basic bare metal servers count limit"""

    baremetal_basic_count_usage: Optional[int] = None
    """Basic bare metal servers count usage"""

    baremetal_gpu_a100_count_limit: Optional[int] = None
    """Baremetal A100 GPU card count limit"""

    baremetal_gpu_a100_count_usage: Optional[int] = None
    """Baremetal A100 GPU card count usage"""

    baremetal_gpu_count_limit: Optional[int] = None
    """AI GPU bare metal servers count limit"""

    baremetal_gpu_count_usage: Optional[int] = None
    """AI GPU bare metal servers count usage"""

    baremetal_gpu_h100_count_limit: Optional[int] = None
    """Baremetal H100 GPU card count limit"""

    baremetal_gpu_h100_count_usage: Optional[int] = None
    """Baremetal H100 GPU card count usage"""

    baremetal_gpu_l40s_count_limit: Optional[int] = None
    """Baremetal L40S GPU card count limit"""

    baremetal_gpu_l40s_count_usage: Optional[int] = None
    """Baremetal L40S GPU card count usage"""

    baremetal_hf_count_limit: Optional[int] = None
    """High-frequency bare metal servers count limit"""

    baremetal_hf_count_usage: Optional[int] = None
    """High-frequency bare metal servers count usage"""

    baremetal_infrastructure_count_limit: Optional[int] = None
    """Infrastructure bare metal servers count limit"""

    baremetal_infrastructure_count_usage: Optional[int] = None
    """Infrastructure bare metal servers count usage"""

    baremetal_network_count_limit: Optional[int] = None
    """Bare metal Network Count limit"""

    baremetal_network_count_usage: Optional[int] = None
    """Bare metal Network Count usage"""

    baremetal_storage_count_limit: Optional[int] = None
    """Storage bare metal servers count limit"""

    baremetal_storage_count_usage: Optional[int] = None
    """Storage bare metal servers count usage"""

    caas_container_count_limit: Optional[int] = None
    """Containers count limit"""

    caas_container_count_usage: Optional[int] = None
    """Containers count usage"""

    caas_cpu_count_limit: Optional[int] = None
    """mCPU count for containers limit"""

    caas_cpu_count_usage: Optional[int] = None
    """mCPU count for containers usage"""

    caas_gpu_count_limit: Optional[int] = None
    """Containers gpu count limit"""

    caas_gpu_count_usage: Optional[int] = None
    """Containers gpu count usage"""

    caas_ram_size_limit: Optional[int] = None
    """MB memory count for containers limit"""

    caas_ram_size_usage: Optional[int] = None
    """MB memory count for containers usage"""

    cluster_count_limit: Optional[int] = None
    """K8s clusters count limit"""

    cluster_count_usage: Optional[int] = None
    """K8s clusters count usage"""

    cpu_count_limit: Optional[int] = None
    """vCPU Count limit"""

    cpu_count_usage: Optional[int] = None
    """vCPU Count usage"""

    dbaas_postgres_cluster_count_limit: Optional[int] = None
    """DBaaS cluster count limit"""

    dbaas_postgres_cluster_count_usage: Optional[int] = None
    """DBaaS cluster count usage"""

    external_ip_count_limit: Optional[int] = None
    """External IP Count limit"""

    external_ip_count_usage: Optional[int] = None
    """External IP Count usage"""

    faas_cpu_count_limit: Optional[int] = None
    """mCPU count for functions limit"""

    faas_cpu_count_usage: Optional[int] = None
    """mCPU count for functions usage"""

    faas_function_count_limit: Optional[int] = None
    """Functions count limit"""

    faas_function_count_usage: Optional[int] = None
    """Functions count usage"""

    faas_namespace_count_limit: Optional[int] = None
    """Functions namespace count limit"""

    faas_namespace_count_usage: Optional[int] = None
    """Functions namespace count usage"""

    faas_ram_size_limit: Optional[int] = None
    """MB memory count for functions limit"""

    faas_ram_size_usage: Optional[int] = None
    """MB memory count for functions usage"""

    firewall_count_limit: Optional[int] = None
    """Firewalls Count limit"""

    firewall_count_usage: Optional[int] = None
    """Firewalls Count usage"""

    floating_count_limit: Optional[int] = None
    """Floating IP Count limit"""

    floating_count_usage: Optional[int] = None
    """Floating IP Count usage"""

    gpu_count_limit: Optional[int] = None
    """GPU Count limit"""

    gpu_count_usage: Optional[int] = None
    """GPU Count usage"""

    gpu_virtual_a100_count_limit: Optional[int] = None
    """Virtual A100 GPU card count limit"""

    gpu_virtual_a100_count_usage: Optional[int] = None
    """Virtual A100 GPU card count usage"""

    gpu_virtual_h100_count_limit: Optional[int] = None
    """Virtual H100 GPU card count limit"""

    gpu_virtual_h100_count_usage: Optional[int] = None
    """Virtual H100 GPU card count usage"""

    gpu_virtual_l40s_count_limit: Optional[int] = None
    """Virtual L40S GPU card count limit"""

    gpu_virtual_l40s_count_usage: Optional[int] = None
    """Virtual L40S GPU card count usage"""

    image_count_limit: Optional[int] = None
    """Images Count limit"""

    image_count_usage: Optional[int] = None
    """Images Count usage"""

    image_size_limit: Optional[int] = None
    """Images Size, GiB limit"""

    image_size_usage: Optional[int] = None
    """Images Size, GiB usage"""

    ipu_count_limit: Optional[int] = None
    """IPU Count limit"""

    ipu_count_usage: Optional[int] = None
    """IPU Count usage"""

    laas_topic_count_limit: Optional[int] = None
    """LaaS Topics Count limit"""

    laas_topic_count_usage: Optional[int] = None
    """LaaS Topics Count usage"""

    loadbalancer_count_limit: Optional[int] = None
    """Load Balancers Count limit"""

    loadbalancer_count_usage: Optional[int] = None
    """Load Balancers Count usage"""

    network_count_limit: Optional[int] = None
    """Networks Count limit"""

    network_count_usage: Optional[int] = None
    """Networks Count usage"""

    ram_limit: Optional[int] = None
    """RAM Size, GiB limit"""

    ram_usage: Optional[int] = None
    """RAM Size, GiB usage"""

    region_id: Optional[int] = None
    """Region ID"""

    registry_count_limit: Optional[int] = None
    """Registries count limit"""

    registry_count_usage: Optional[int] = None
    """Registries count usage"""

    registry_storage_limit: Optional[int] = None
    """Registries volume usage, GiB limit"""

    registry_storage_usage: Optional[int] = None
    """Registries volume usage, GiB usage"""

    router_count_limit: Optional[int] = None
    """Routers Count limit"""

    router_count_usage: Optional[int] = None
    """Routers Count usage"""

    secret_count_limit: Optional[int] = None
    """Secret Count limit"""

    secret_count_usage: Optional[int] = None
    """Secret Count usage"""

    servergroup_count_limit: Optional[int] = None
    """Placement Group Count limit"""

    servergroup_count_usage: Optional[int] = None
    """Placement Group Count usage"""

    sfs_count_limit: Optional[int] = None
    """Shared file system Count limit"""

    sfs_count_usage: Optional[int] = None
    """Shared file system Count usage"""

    sfs_size_limit: Optional[int] = None
    """Shared file system Size, GiB limit"""

    sfs_size_usage: Optional[int] = None
    """Shared file system Size, GiB usage"""

    shared_vm_count_limit: Optional[int] = None
    """Basic VMs Count limit"""

    shared_vm_count_usage: Optional[int] = None
    """Basic VMs Count usage"""

    snapshot_schedule_count_limit: Optional[int] = None
    """Snapshot Schedules Count limit"""

    snapshot_schedule_count_usage: Optional[int] = None
    """Snapshot Schedules Count usage"""

    subnet_count_limit: Optional[int] = None
    """Subnets Count limit"""

    subnet_count_usage: Optional[int] = None
    """Subnets Count usage"""

    vm_count_limit: Optional[int] = None
    """Instances Dedicated Count limit"""

    vm_count_usage: Optional[int] = None
    """Instances Dedicated Count usage"""

    volume_count_limit: Optional[int] = None
    """Volumes Count limit"""

    volume_count_usage: Optional[int] = None
    """Volumes Count usage"""

    volume_size_limit: Optional[int] = None
    """Volumes Size, GiB limit"""

    volume_size_usage: Optional[int] = None
    """Volumes Size, GiB usage"""

    volume_snapshots_count_limit: Optional[int] = None
    """Snapshots Count limit"""

    volume_snapshots_count_usage: Optional[int] = None
    """Snapshots Count usage"""

    volume_snapshots_size_limit: Optional[int] = None
    """Snapshots Size, GiB limit"""

    volume_snapshots_size_usage: Optional[int] = None
    """Snapshots Size, GiB usage"""
