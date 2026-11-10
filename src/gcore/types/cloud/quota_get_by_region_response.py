# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["QuotaGetByRegionResponse"]


class QuotaGetByRegionResponse(BaseModel):
    baremetal_basic_count_limit: int
    """Basic bare metal servers count limit"""

    baremetal_basic_count_usage: int
    """Basic bare metal servers count usage"""

    baremetal_gpu_a100_count_limit: int
    """Bare metal A100 GPU server count limit"""

    baremetal_gpu_a100_count_usage: int
    """Bare metal A100 GPU server count usage"""

    baremetal_gpu_count_limit: int
    """Total number of AI GPU bare metal servers.

    This field is deprecated and is now always calculated automatically as the sum
    of `baremetal_gpu_a100_count_limit`, `baremetal_gpu_h100_count_limit`,
    `baremetal_gpu_h200_count_limit`, and `baremetal_gpu_l40s_count_limit`.
    """

    baremetal_gpu_count_usage: int
    """Total number of AI GPU bare metal servers in use.

    This field is deprecated and is now always calculated automatically as the sum
    of `baremetal_gpu_a100_count_usage`, `baremetal_gpu_h100_count_usage`,
    `baremetal_gpu_h200_count_usage`, and `baremetal_gpu_l40s_count_usage`.
    """

    baremetal_gpu_h100_count_limit: int
    """Bare metal H100 GPU server count limit"""

    baremetal_gpu_h100_count_usage: int
    """Bare metal H100 GPU server count usage"""

    baremetal_gpu_h200_count_limit: int
    """Bare metal H200 GPU server count limit"""

    baremetal_gpu_h200_count_usage: int
    """Bare metal H200 GPU server count usage"""

    baremetal_gpu_l40s_count_limit: int
    """Bare metal L40S GPU server count limit"""

    baremetal_gpu_l40s_count_usage: int
    """Bare metal L40S GPU server count usage"""

    baremetal_hf_count_limit: int
    """High-frequency bare metal servers count limit"""

    baremetal_hf_count_usage: int
    """High-frequency bare metal servers count usage"""

    baremetal_infrastructure_count_limit: int
    """Infrastructure bare metal servers count limit"""

    baremetal_infrastructure_count_usage: int
    """Infrastructure bare metal servers count usage"""

    baremetal_network_count_limit: int
    """Bare metal Network Count limit"""

    baremetal_network_count_usage: int
    """Bare metal Network Count usage"""

    baremetal_storage_count_limit: int
    """Storage bare metal servers count limit"""

    baremetal_storage_count_usage: int
    """Storage bare metal servers count usage"""

    caas_container_count_limit: int
    """Containers count limit"""

    caas_container_count_usage: int
    """Containers count usage"""

    caas_cpu_count_limit: int
    """mCPU count for containers limit"""

    caas_cpu_count_usage: int
    """mCPU count for containers usage"""

    caas_gpu_count_limit: int
    """Containers gpu count limit"""

    caas_gpu_count_usage: int
    """Containers gpu count usage"""

    caas_ram_size_limit: int
    """MiB memory count for containers limit"""

    caas_ram_size_usage: int
    """MiB memory count for containers usage"""

    cluster_count_limit: int
    """K8s clusters count limit"""

    cluster_count_usage: int
    """K8s clusters count usage"""

    cpu_count_limit: int
    """vCPU Count limit"""

    cpu_count_usage: int
    """vCPU Count usage"""

    dbaas_postgres_cluster_count_limit: int
    """DBaaS cluster count limit"""

    dbaas_postgres_cluster_count_usage: int
    """DBaaS cluster count usage"""

    external_ip_count_limit: int
    """External IP Count limit"""

    external_ip_count_usage: int
    """External IP Count usage"""

    faas_cpu_count_limit: int
    """mCPU count for functions limit"""

    faas_cpu_count_usage: int
    """mCPU count for functions usage"""

    faas_function_count_limit: int
    """Functions count limit"""

    faas_function_count_usage: int
    """Functions count usage"""

    faas_namespace_count_limit: int
    """Functions namespace count limit"""

    faas_namespace_count_usage: int
    """Functions namespace count usage"""

    faas_ram_size_limit: int
    """MiB memory count for functions limit"""

    faas_ram_size_usage: int
    """MiB memory count for functions usage"""

    firewall_count_limit: int
    """Firewalls Count limit"""

    firewall_count_usage: int
    """Firewalls Count usage"""

    floating_count_limit: int
    """Floating IP Count limit"""

    floating_count_usage: int
    """Floating IP Count usage"""

    gpu_count_limit: int
    """GPU Count limit"""

    gpu_count_usage: int
    """GPU Count usage"""

    gpu_virtual_a100_count_limit: int
    """Virtual A100 GPU card count limit"""

    gpu_virtual_a100_count_usage: int
    """Virtual A100 GPU card count usage"""

    gpu_virtual_h100_count_limit: int
    """Virtual H100 GPU card count limit"""

    gpu_virtual_h100_count_usage: int
    """Virtual H100 GPU card count usage"""

    gpu_virtual_h200_count_limit: int
    """Virtual H200 GPU card count limit"""

    gpu_virtual_h200_count_usage: int
    """Virtual H200 GPU card count usage"""

    gpu_virtual_l40s_count_limit: int
    """Virtual L40S GPU card count limit"""

    gpu_virtual_l40s_count_usage: int
    """Virtual L40S GPU card count usage"""

    image_count_limit: int
    """Images Count limit"""

    image_count_usage: int
    """Images Count usage"""

    image_size_limit: int
    """Images Size, bytes limit"""

    image_size_usage: int
    """Images Size, bytes usage"""

    ipu_count_limit: int
    """IPU Count limit"""

    ipu_count_usage: int
    """IPU Count usage"""

    laas_topic_count_limit: int
    """LaaS Topics Count limit"""

    laas_topic_count_usage: int
    """LaaS Topics Count usage"""

    loadbalancer_count_limit: int
    """Load Balancers Count limit"""

    loadbalancer_count_usage: int
    """Load Balancers Count usage"""

    network_count_limit: int
    """Networks Count limit"""

    network_count_usage: int
    """Networks Count usage"""

    ram_limit: int
    """RAM Size, MiB limit"""

    ram_usage: int
    """RAM Size, MiB usage"""

    region_id: int
    """Region ID"""

    registry_count_limit: int
    """Registries count limit"""

    registry_count_usage: int
    """Registries count usage"""

    registry_storage_limit: int
    """Registries volume usage, GiB limit"""

    registry_storage_usage: int
    """Registries volume usage, GiB usage"""

    router_count_limit: int
    """Routers Count limit"""

    router_count_usage: int
    """Routers Count usage"""

    secret_count_limit: int
    """Secret Count limit"""

    secret_count_usage: int
    """Secret Count usage"""

    servergroup_count_limit: int
    """Placement Group Count limit"""

    servergroup_count_usage: int
    """Placement Group Count usage"""

    sfs_count_limit: int
    """Shared file system Count limit"""

    sfs_count_usage: int
    """Shared file system Count usage"""

    sfs_size_limit: int
    """Shared file system Size, GiB limit"""

    sfs_size_usage: int
    """Shared file system Size, GiB usage"""

    shared_vm_count_limit: int
    """Basic VMs Count limit"""

    shared_vm_count_usage: int
    """Basic VMs Count usage"""

    slurm_cluster_count_limit: int
    """Slurm cluster count limit for this region. 0 disables Slurm in this region."""

    slurm_cluster_count_usage: int
    """Slurm cluster count usage"""

    snapshot_schedule_count_limit: int
    """Snapshot Schedules Count limit"""

    snapshot_schedule_count_usage: int
    """Snapshot Schedules Count usage"""

    subnet_count_limit: int
    """Subnets Count limit"""

    subnet_count_usage: int
    """Subnets Count usage"""

    vm_count_limit: int
    """Instances Dedicated Count limit"""

    vm_count_usage: int
    """Instances Dedicated Count usage"""

    volume_count_limit: int
    """Volumes Count limit"""

    volume_count_usage: int
    """Volumes Count usage"""

    volume_size_limit: int
    """Volumes Size, GiB limit"""

    volume_size_usage: int
    """Volumes Size, GiB usage"""

    volume_snapshots_count_limit: int
    """Snapshots Count limit"""

    volume_snapshots_count_usage: int
    """Snapshots Count usage"""

    volume_snapshots_size_limit: int
    """Snapshots Size, GiB limit"""

    volume_snapshots_size_usage: int
    """Snapshots Size, GiB usage"""
