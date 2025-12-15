# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel

__all__ = ["K8SClusterPoolQuota"]


class K8SClusterPoolQuota(BaseModel):
    """Response schema for K8s cluster quota check.

    Returns quota fields that are exceeded. Fields are only included when
    regional limits would be violated. Empty response means no quotas exceeded.
    """

    baremetal_gpu_a100_count_limit: Optional[int] = None
    """Bare metal A100 GPU server count limit"""

    baremetal_gpu_a100_count_requested: Optional[int] = None
    """Bare metal A100 GPU server count requested"""

    baremetal_gpu_a100_count_usage: Optional[int] = None
    """Bare metal A100 GPU server count usage"""

    baremetal_gpu_h100_count_limit: Optional[int] = None
    """Bare metal H100 GPU server count limit"""

    baremetal_gpu_h100_count_requested: Optional[int] = None
    """Bare metal H100 GPU server count requested"""

    baremetal_gpu_h100_count_usage: Optional[int] = None
    """Bare metal H100 GPU server count usage"""

    baremetal_gpu_h200_count_limit: Optional[int] = None
    """Bare metal H200 GPU server count limit"""

    baremetal_gpu_h200_count_requested: Optional[int] = None
    """Bare metal H200 GPU server count requested"""

    baremetal_gpu_h200_count_usage: Optional[int] = None
    """Bare metal H200 GPU server count usage"""

    baremetal_gpu_l40s_count_limit: Optional[int] = None
    """Bare metal L40S GPU server count limit"""

    baremetal_gpu_l40s_count_requested: Optional[int] = None
    """Bare metal L40S GPU server count requested"""

    baremetal_gpu_l40s_count_usage: Optional[int] = None
    """Bare metal L40S GPU server count usage"""

    baremetal_hf_count_limit: Optional[int] = None
    """High-frequency bare metal servers count limit"""

    baremetal_hf_count_requested: Optional[int] = None
    """High-frequency bare metal servers count requested"""

    baremetal_hf_count_usage: Optional[int] = None
    """High-frequency bare metal servers count usage"""

    cluster_count_limit: Optional[int] = None
    """K8s clusters count limit"""

    cluster_count_requested: Optional[int] = None
    """K8s clusters count requested"""

    cluster_count_usage: Optional[int] = None
    """K8s clusters count usage"""

    cpu_count_limit: Optional[int] = None
    """vCPU Count limit"""

    cpu_count_requested: Optional[int] = None
    """vCPU Count requested"""

    cpu_count_usage: Optional[int] = None
    """vCPU Count usage"""

    firewall_count_limit: Optional[int] = None
    """Firewalls Count limit"""

    firewall_count_requested: Optional[int] = None
    """Firewalls Count requested"""

    firewall_count_usage: Optional[int] = None
    """Firewalls Count usage"""

    floating_count_limit: Optional[int] = None
    """Floating IP Count limit"""

    floating_count_requested: Optional[int] = None
    """Floating IP Count requested"""

    floating_count_usage: Optional[int] = None
    """Floating IP Count usage"""

    gpu_count_limit: Optional[int] = None
    """GPU Count limit"""

    gpu_count_requested: Optional[int] = None
    """GPU Count requested"""

    gpu_count_usage: Optional[int] = None
    """GPU Count usage"""

    gpu_virtual_a100_count_limit: Optional[int] = None
    """Virtual A100 GPU card count limit"""

    gpu_virtual_a100_count_requested: Optional[int] = None
    """Virtual A100 GPU card count requested"""

    gpu_virtual_a100_count_usage: Optional[int] = None
    """Virtual A100 GPU card count usage"""

    gpu_virtual_h100_count_limit: Optional[int] = None
    """Virtual H100 GPU card count limit"""

    gpu_virtual_h100_count_requested: Optional[int] = None
    """Virtual H100 GPU card count requested"""

    gpu_virtual_h100_count_usage: Optional[int] = None
    """Virtual H100 GPU card count usage"""

    gpu_virtual_h200_count_limit: Optional[int] = None
    """Virtual H200 GPU card count limit"""

    gpu_virtual_h200_count_requested: Optional[int] = None
    """Virtual H200 GPU card count requested"""

    gpu_virtual_h200_count_usage: Optional[int] = None
    """Virtual H200 GPU card count usage"""

    gpu_virtual_l40s_count_limit: Optional[int] = None
    """Virtual L40S GPU card count limit"""

    gpu_virtual_l40s_count_requested: Optional[int] = None
    """Virtual L40S GPU card count requested"""

    gpu_virtual_l40s_count_usage: Optional[int] = None
    """Virtual L40S GPU card count usage"""

    laas_topic_count_limit: Optional[int] = None
    """LaaS Topics Count limit"""

    laas_topic_count_requested: Optional[int] = None
    """LaaS Topics Count requested"""

    laas_topic_count_usage: Optional[int] = None
    """LaaS Topics Count usage"""

    loadbalancer_count_limit: Optional[int] = None
    """Load Balancers Count limit"""

    loadbalancer_count_requested: Optional[int] = None
    """Load Balancers Count requested"""

    loadbalancer_count_usage: Optional[int] = None
    """Load Balancers Count usage"""

    ram_limit: Optional[int] = None
    """RAM Size, MiB limit"""

    ram_requested: Optional[int] = None
    """RAM Size, MiB requested"""

    ram_usage: Optional[int] = None
    """RAM Size, MiB usage"""

    servergroup_count_limit: Optional[int] = None
    """Placement Group Count limit"""

    servergroup_count_requested: Optional[int] = None
    """Placement Group Count requested"""

    servergroup_count_usage: Optional[int] = None
    """Placement Group Count usage"""

    vm_count_limit: Optional[int] = None
    """VMs Count limit"""

    vm_count_requested: Optional[int] = None
    """VMs Count requested"""

    vm_count_usage: Optional[int] = None
    """VMs Count usage"""

    volume_count_limit: Optional[int] = None
    """Volumes Count limit"""

    volume_count_requested: Optional[int] = None
    """Volumes Count requested"""

    volume_count_usage: Optional[int] = None
    """Volumes Count usage"""

    volume_size_limit: Optional[int] = None
    """Volumes Size, GiB limit"""

    volume_size_requested: Optional[int] = None
    """Volumes Size, GiB requested"""

    volume_size_usage: Optional[int] = None
    """Volumes Size, GiB usage"""
