# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["RequestCreateParams", "RequestedLimits", "RequestedLimitsGlobalLimits", "RequestedLimitsRegionalLimit"]


class RequestCreateParams(TypedDict, total=False):
    description: Required[str]
    """Describe the reason, in general terms."""

    requested_limits: Required[RequestedLimits]
    """Limits you want to increase."""


class RequestedLimitsGlobalLimits(TypedDict, total=False):
    """Global entity quota limits"""

    inference_cpu_millicore_count_limit: int
    """Inference CPU millicore count limit"""

    inference_gpu_a100_count_limit: int
    """Inference GPU A100 Count limit"""

    inference_gpu_h100_count_limit: int
    """Inference GPU H100 Count limit"""

    inference_gpu_l40s_count_limit: int
    """Inference GPU L40s Count limit"""

    inference_instance_count_limit: int
    """Inference instance count limit"""

    keypair_count_limit: int
    """SSH Keys Count limit"""

    project_count_limit: int
    """Projects Count limit"""


class RequestedLimitsRegionalLimit(TypedDict, total=False):
    baremetal_basic_count_limit: int
    """Basic bare metal servers count limit"""

    baremetal_gpu_a100_count_limit: int
    """Bare metal A100 GPU server count limit"""

    baremetal_gpu_count_limit: int
    """Total number of AI GPU bare metal servers.

    This field is deprecated and is now always calculated automatically as the sum
    of `baremetal_gpu_a100_count_limit`, `baremetal_gpu_h100_count_limit`,
    `baremetal_gpu_h200_count_limit`, and `baremetal_gpu_l40s_count_limit`.
    """

    baremetal_gpu_h100_count_limit: int
    """Bare metal H100 GPU server count limit"""

    baremetal_gpu_h200_count_limit: int
    """Bare metal H200 GPU server count limit"""

    baremetal_gpu_l40s_count_limit: int
    """Bare metal L40S GPU server count limit"""

    baremetal_hf_count_limit: int
    """High-frequency bare metal servers count limit"""

    baremetal_infrastructure_count_limit: int
    """Infrastructure bare metal servers count limit"""

    baremetal_network_count_limit: int
    """Bare metal Network Count limit"""

    baremetal_storage_count_limit: int
    """Storage bare metal servers count limit"""

    caas_container_count_limit: int
    """Containers count limit"""

    caas_cpu_count_limit: int
    """mCPU count for containers limit"""

    caas_gpu_count_limit: int
    """Containers gpu count limit"""

    caas_ram_size_limit: int
    """MB memory count for containers limit"""

    cluster_count_limit: int
    """K8s clusters count limit"""

    cpu_count_limit: int
    """vCPU Count limit"""

    dbaas_postgres_cluster_count_limit: int
    """DBaaS cluster count limit"""

    external_ip_count_limit: int
    """External IP Count limit"""

    faas_cpu_count_limit: int
    """mCPU count for functions limit"""

    faas_function_count_limit: int
    """Functions count limit"""

    faas_namespace_count_limit: int
    """Functions namespace count limit"""

    faas_ram_size_limit: int
    """MB memory count for functions limit"""

    firewall_count_limit: int
    """Firewalls Count limit"""

    floating_count_limit: int
    """Floating IP Count limit"""

    gpu_count_limit: int
    """GPU Count limit"""

    gpu_virtual_a100_count_limit: int
    """Virtual A100 GPU card count limit"""

    gpu_virtual_h100_count_limit: int
    """Virtual H100 GPU card count limit"""

    gpu_virtual_h200_count_limit: int
    """Virtual H200 GPU card count limit"""

    gpu_virtual_l40s_count_limit: int
    """Virtual L40S GPU card count limit"""

    image_count_limit: int
    """Images Count limit"""

    image_size_limit: int
    """Images Size, GiB limit"""

    ipu_count_limit: int
    """IPU Count limit"""

    laas_topic_count_limit: int
    """LaaS Topics Count limit"""

    loadbalancer_count_limit: int
    """Load Balancers Count limit"""

    network_count_limit: int
    """Networks Count limit"""

    ram_limit: int
    """RAM Size, GiB limit"""

    region_id: int
    """Region ID"""

    registry_count_limit: int
    """Registries count limit"""

    registry_storage_limit: int
    """Registries volume usage, GiB limit"""

    router_count_limit: int
    """Routers Count limit"""

    secret_count_limit: int
    """Secret Count limit"""

    servergroup_count_limit: int
    """Placement Group Count limit"""

    sfs_count_limit: int
    """Shared file system Count limit"""

    sfs_size_limit: int
    """Shared file system Size, GiB limit"""

    shared_vm_count_limit: int
    """Basic VMs Count limit"""

    snapshot_schedule_count_limit: int
    """Snapshot Schedules Count limit"""

    subnet_count_limit: int
    """Subnets Count limit"""

    vm_count_limit: int
    """Instances Dedicated Count limit"""

    volume_count_limit: int
    """Volumes Count limit"""

    volume_size_limit: int
    """Volumes Size, GiB limit"""

    volume_snapshots_count_limit: int
    """Snapshots Count limit"""

    volume_snapshots_size_limit: int
    """Snapshots Size, GiB limit"""


class RequestedLimits(TypedDict, total=False):
    """Limits you want to increase."""

    global_limits: RequestedLimitsGlobalLimits
    """Global entity quota limits"""

    regional_limits: Iterable[RequestedLimitsRegionalLimit]
    """Regions and their quota limits"""
