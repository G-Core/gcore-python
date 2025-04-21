# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["QuotaGetAllResponse", "GlobalQuotas", "RegionalQuota"]


class GlobalQuotas(BaseModel):
    inference_cpu_millicore_count_limit: Optional[int] = None
    """
    '#/components/schemas/GlobalQuotasSerializer/properties/inference_cpu_millicore_count_limit'
    "$.components.schemas.GlobalQuotasSerializer.properties.inference_cpu_millicore_count_limit"
    """

    inference_cpu_millicore_count_usage: Optional[int] = None
    """
    '#/components/schemas/GlobalQuotasSerializer/properties/inference_cpu_millicore_count_usage'
    "$.components.schemas.GlobalQuotasSerializer.properties.inference_cpu_millicore_count_usage"
    """

    inference_gpu_a100_count_limit: Optional[int] = None
    """
    '#/components/schemas/GlobalQuotasSerializer/properties/inference_gpu_a100_count_limit'
    "$.components.schemas.GlobalQuotasSerializer.properties.inference_gpu_a100_count_limit"
    """

    inference_gpu_a100_count_usage: Optional[int] = None
    """
    '#/components/schemas/GlobalQuotasSerializer/properties/inference_gpu_a100_count_usage'
    "$.components.schemas.GlobalQuotasSerializer.properties.inference_gpu_a100_count_usage"
    """

    inference_gpu_h100_count_limit: Optional[int] = None
    """
    '#/components/schemas/GlobalQuotasSerializer/properties/inference_gpu_h100_count_limit'
    "$.components.schemas.GlobalQuotasSerializer.properties.inference_gpu_h100_count_limit"
    """

    inference_gpu_h100_count_usage: Optional[int] = None
    """
    '#/components/schemas/GlobalQuotasSerializer/properties/inference_gpu_h100_count_usage'
    "$.components.schemas.GlobalQuotasSerializer.properties.inference_gpu_h100_count_usage"
    """

    inference_gpu_l40s_count_limit: Optional[int] = None
    """
    '#/components/schemas/GlobalQuotasSerializer/properties/inference_gpu_l40s_count_limit'
    "$.components.schemas.GlobalQuotasSerializer.properties.inference_gpu_l40s_count_limit"
    """

    inference_gpu_l40s_count_usage: Optional[int] = None
    """
    '#/components/schemas/GlobalQuotasSerializer/properties/inference_gpu_l40s_count_usage'
    "$.components.schemas.GlobalQuotasSerializer.properties.inference_gpu_l40s_count_usage"
    """

    inference_instance_count_limit: Optional[int] = None
    """
    '#/components/schemas/GlobalQuotasSerializer/properties/inference_instance_count_limit'
    "$.components.schemas.GlobalQuotasSerializer.properties.inference_instance_count_limit"
    """

    inference_instance_count_usage: Optional[int] = None
    """
    '#/components/schemas/GlobalQuotasSerializer/properties/inference_instance_count_usage'
    "$.components.schemas.GlobalQuotasSerializer.properties.inference_instance_count_usage"
    """

    keypair_count_limit: Optional[int] = None
    """
    '#/components/schemas/GlobalQuotasSerializer/properties/keypair_count_limit'
    "$.components.schemas.GlobalQuotasSerializer.properties.keypair_count_limit"
    """

    keypair_count_usage: Optional[int] = None
    """
    '#/components/schemas/GlobalQuotasSerializer/properties/keypair_count_usage'
    "$.components.schemas.GlobalQuotasSerializer.properties.keypair_count_usage"
    """

    project_count_limit: Optional[int] = None
    """
    '#/components/schemas/GlobalQuotasSerializer/properties/project_count_limit'
    "$.components.schemas.GlobalQuotasSerializer.properties.project_count_limit"
    """

    project_count_usage: Optional[int] = None
    """
    '#/components/schemas/GlobalQuotasSerializer/properties/project_count_usage'
    "$.components.schemas.GlobalQuotasSerializer.properties.project_count_usage"
    """


class RegionalQuota(BaseModel):
    baremetal_basic_count_limit: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/baremetal_basic_count_limit'
    "$.components.schemas.RegionalQuotasSerializer.properties.baremetal_basic_count_limit"
    """

    baremetal_basic_count_usage: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/baremetal_basic_count_usage'
    "$.components.schemas.RegionalQuotasSerializer.properties.baremetal_basic_count_usage"
    """

    baremetal_gpu_count_limit: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/baremetal_gpu_count_limit'
    "$.components.schemas.RegionalQuotasSerializer.properties.baremetal_gpu_count_limit"
    """

    baremetal_gpu_count_usage: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/baremetal_gpu_count_usage'
    "$.components.schemas.RegionalQuotasSerializer.properties.baremetal_gpu_count_usage"
    """

    baremetal_hf_count_limit: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/baremetal_hf_count_limit'
    "$.components.schemas.RegionalQuotasSerializer.properties.baremetal_hf_count_limit"
    """

    baremetal_hf_count_usage: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/baremetal_hf_count_usage'
    "$.components.schemas.RegionalQuotasSerializer.properties.baremetal_hf_count_usage"
    """

    baremetal_infrastructure_count_limit: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/baremetal_infrastructure_count_limit'
    "$.components.schemas.RegionalQuotasSerializer.properties.baremetal_infrastructure_count_limit"
    """

    baremetal_infrastructure_count_usage: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/baremetal_infrastructure_count_usage'
    "$.components.schemas.RegionalQuotasSerializer.properties.baremetal_infrastructure_count_usage"
    """

    baremetal_network_count_limit: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/baremetal_network_count_limit'
    "$.components.schemas.RegionalQuotasSerializer.properties.baremetal_network_count_limit"
    """

    baremetal_network_count_usage: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/baremetal_network_count_usage'
    "$.components.schemas.RegionalQuotasSerializer.properties.baremetal_network_count_usage"
    """

    baremetal_storage_count_limit: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/baremetal_storage_count_limit'
    "$.components.schemas.RegionalQuotasSerializer.properties.baremetal_storage_count_limit"
    """

    baremetal_storage_count_usage: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/baremetal_storage_count_usage'
    "$.components.schemas.RegionalQuotasSerializer.properties.baremetal_storage_count_usage"
    """

    caas_container_count_limit: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/caas_container_count_limit'
    "$.components.schemas.RegionalQuotasSerializer.properties.caas_container_count_limit"
    """

    caas_container_count_usage: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/caas_container_count_usage'
    "$.components.schemas.RegionalQuotasSerializer.properties.caas_container_count_usage"
    """

    caas_cpu_count_limit: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/caas_cpu_count_limit'
    "$.components.schemas.RegionalQuotasSerializer.properties.caas_cpu_count_limit"
    """

    caas_cpu_count_usage: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/caas_cpu_count_usage'
    "$.components.schemas.RegionalQuotasSerializer.properties.caas_cpu_count_usage"
    """

    caas_gpu_count_limit: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/caas_gpu_count_limit'
    "$.components.schemas.RegionalQuotasSerializer.properties.caas_gpu_count_limit"
    """

    caas_gpu_count_usage: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/caas_gpu_count_usage'
    "$.components.schemas.RegionalQuotasSerializer.properties.caas_gpu_count_usage"
    """

    caas_ram_size_limit: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/caas_ram_size_limit'
    "$.components.schemas.RegionalQuotasSerializer.properties.caas_ram_size_limit"
    """

    caas_ram_size_usage: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/caas_ram_size_usage'
    "$.components.schemas.RegionalQuotasSerializer.properties.caas_ram_size_usage"
    """

    cluster_count_limit: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/cluster_count_limit'
    "$.components.schemas.RegionalQuotasSerializer.properties.cluster_count_limit"
    """

    cluster_count_usage: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/cluster_count_usage'
    "$.components.schemas.RegionalQuotasSerializer.properties.cluster_count_usage"
    """

    cpu_count_limit: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/cpu_count_limit'
    "$.components.schemas.RegionalQuotasSerializer.properties.cpu_count_limit"
    """

    cpu_count_usage: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/cpu_count_usage'
    "$.components.schemas.RegionalQuotasSerializer.properties.cpu_count_usage"
    """

    dbaas_postgres_cluster_count_limit: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/dbaas_postgres_cluster_count_limit'
    "$.components.schemas.RegionalQuotasSerializer.properties.dbaas_postgres_cluster_count_limit"
    """

    dbaas_postgres_cluster_count_usage: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/dbaas_postgres_cluster_count_usage'
    "$.components.schemas.RegionalQuotasSerializer.properties.dbaas_postgres_cluster_count_usage"
    """

    external_ip_count_limit: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/external_ip_count_limit'
    "$.components.schemas.RegionalQuotasSerializer.properties.external_ip_count_limit"
    """

    external_ip_count_usage: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/external_ip_count_usage'
    "$.components.schemas.RegionalQuotasSerializer.properties.external_ip_count_usage"
    """

    faas_cpu_count_limit: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/faas_cpu_count_limit'
    "$.components.schemas.RegionalQuotasSerializer.properties.faas_cpu_count_limit"
    """

    faas_cpu_count_usage: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/faas_cpu_count_usage'
    "$.components.schemas.RegionalQuotasSerializer.properties.faas_cpu_count_usage"
    """

    faas_function_count_limit: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/faas_function_count_limit'
    "$.components.schemas.RegionalQuotasSerializer.properties.faas_function_count_limit"
    """

    faas_function_count_usage: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/faas_function_count_usage'
    "$.components.schemas.RegionalQuotasSerializer.properties.faas_function_count_usage"
    """

    faas_namespace_count_limit: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/faas_namespace_count_limit'
    "$.components.schemas.RegionalQuotasSerializer.properties.faas_namespace_count_limit"
    """

    faas_namespace_count_usage: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/faas_namespace_count_usage'
    "$.components.schemas.RegionalQuotasSerializer.properties.faas_namespace_count_usage"
    """

    faas_ram_size_limit: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/faas_ram_size_limit'
    "$.components.schemas.RegionalQuotasSerializer.properties.faas_ram_size_limit"
    """

    faas_ram_size_usage: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/faas_ram_size_usage'
    "$.components.schemas.RegionalQuotasSerializer.properties.faas_ram_size_usage"
    """

    firewall_count_limit: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/firewall_count_limit'
    "$.components.schemas.RegionalQuotasSerializer.properties.firewall_count_limit"
    """

    firewall_count_usage: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/firewall_count_usage'
    "$.components.schemas.RegionalQuotasSerializer.properties.firewall_count_usage"
    """

    floating_count_limit: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/floating_count_limit'
    "$.components.schemas.RegionalQuotasSerializer.properties.floating_count_limit"
    """

    floating_count_usage: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/floating_count_usage'
    "$.components.schemas.RegionalQuotasSerializer.properties.floating_count_usage"
    """

    gpu_count_limit: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/gpu_count_limit'
    "$.components.schemas.RegionalQuotasSerializer.properties.gpu_count_limit"
    """

    gpu_count_usage: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/gpu_count_usage'
    "$.components.schemas.RegionalQuotasSerializer.properties.gpu_count_usage"
    """

    gpu_virtual_a100_count_limit: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/gpu_virtual_a100_count_limit'
    "$.components.schemas.RegionalQuotasSerializer.properties.gpu_virtual_a100_count_limit"
    """

    gpu_virtual_a100_count_usage: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/gpu_virtual_a100_count_usage'
    "$.components.schemas.RegionalQuotasSerializer.properties.gpu_virtual_a100_count_usage"
    """

    gpu_virtual_h100_count_limit: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/gpu_virtual_h100_count_limit'
    "$.components.schemas.RegionalQuotasSerializer.properties.gpu_virtual_h100_count_limit"
    """

    gpu_virtual_h100_count_usage: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/gpu_virtual_h100_count_usage'
    "$.components.schemas.RegionalQuotasSerializer.properties.gpu_virtual_h100_count_usage"
    """

    gpu_virtual_l40s_count_limit: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/gpu_virtual_l40s_count_limit'
    "$.components.schemas.RegionalQuotasSerializer.properties.gpu_virtual_l40s_count_limit"
    """

    gpu_virtual_l40s_count_usage: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/gpu_virtual_l40s_count_usage'
    "$.components.schemas.RegionalQuotasSerializer.properties.gpu_virtual_l40s_count_usage"
    """

    image_count_limit: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/image_count_limit'
    "$.components.schemas.RegionalQuotasSerializer.properties.image_count_limit"
    """

    image_count_usage: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/image_count_usage'
    "$.components.schemas.RegionalQuotasSerializer.properties.image_count_usage"
    """

    image_size_limit: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/image_size_limit'
    "$.components.schemas.RegionalQuotasSerializer.properties.image_size_limit"
    """

    image_size_usage: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/image_size_usage'
    "$.components.schemas.RegionalQuotasSerializer.properties.image_size_usage"
    """

    ipu_count_limit: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/ipu_count_limit'
    "$.components.schemas.RegionalQuotasSerializer.properties.ipu_count_limit"
    """

    ipu_count_usage: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/ipu_count_usage'
    "$.components.schemas.RegionalQuotasSerializer.properties.ipu_count_usage"
    """

    laas_topic_count_limit: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/laas_topic_count_limit'
    "$.components.schemas.RegionalQuotasSerializer.properties.laas_topic_count_limit"
    """

    laas_topic_count_usage: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/laas_topic_count_usage'
    "$.components.schemas.RegionalQuotasSerializer.properties.laas_topic_count_usage"
    """

    loadbalancer_count_limit: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/loadbalancer_count_limit'
    "$.components.schemas.RegionalQuotasSerializer.properties.loadbalancer_count_limit"
    """

    loadbalancer_count_usage: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/loadbalancer_count_usage'
    "$.components.schemas.RegionalQuotasSerializer.properties.loadbalancer_count_usage"
    """

    network_count_limit: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/network_count_limit'
    "$.components.schemas.RegionalQuotasSerializer.properties.network_count_limit"
    """

    network_count_usage: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/network_count_usage'
    "$.components.schemas.RegionalQuotasSerializer.properties.network_count_usage"
    """

    ram_limit: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/ram_limit'
    "$.components.schemas.RegionalQuotasSerializer.properties.ram_limit"
    """

    ram_usage: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/ram_usage'
    "$.components.schemas.RegionalQuotasSerializer.properties.ram_usage"
    """

    region_id: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/region_id'
    "$.components.schemas.RegionalQuotasSerializer.properties.region_id"
    """

    registry_count_limit: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/registry_count_limit'
    "$.components.schemas.RegionalQuotasSerializer.properties.registry_count_limit"
    """

    registry_count_usage: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/registry_count_usage'
    "$.components.schemas.RegionalQuotasSerializer.properties.registry_count_usage"
    """

    registry_storage_limit: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/registry_storage_limit'
    "$.components.schemas.RegionalQuotasSerializer.properties.registry_storage_limit"
    """

    registry_storage_usage: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/registry_storage_usage'
    "$.components.schemas.RegionalQuotasSerializer.properties.registry_storage_usage"
    """

    router_count_limit: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/router_count_limit'
    "$.components.schemas.RegionalQuotasSerializer.properties.router_count_limit"
    """

    router_count_usage: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/router_count_usage'
    "$.components.schemas.RegionalQuotasSerializer.properties.router_count_usage"
    """

    secret_count_limit: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/secret_count_limit'
    "$.components.schemas.RegionalQuotasSerializer.properties.secret_count_limit"
    """

    secret_count_usage: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/secret_count_usage'
    "$.components.schemas.RegionalQuotasSerializer.properties.secret_count_usage"
    """

    servergroup_count_limit: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/servergroup_count_limit'
    "$.components.schemas.RegionalQuotasSerializer.properties.servergroup_count_limit"
    """

    servergroup_count_usage: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/servergroup_count_usage'
    "$.components.schemas.RegionalQuotasSerializer.properties.servergroup_count_usage"
    """

    sfs_count_limit: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/sfs_count_limit'
    "$.components.schemas.RegionalQuotasSerializer.properties.sfs_count_limit"
    """

    sfs_count_usage: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/sfs_count_usage'
    "$.components.schemas.RegionalQuotasSerializer.properties.sfs_count_usage"
    """

    sfs_size_limit: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/sfs_size_limit'
    "$.components.schemas.RegionalQuotasSerializer.properties.sfs_size_limit"
    """

    sfs_size_usage: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/sfs_size_usage'
    "$.components.schemas.RegionalQuotasSerializer.properties.sfs_size_usage"
    """

    shared_vm_count_limit: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/shared_vm_count_limit'
    "$.components.schemas.RegionalQuotasSerializer.properties.shared_vm_count_limit"
    """

    shared_vm_count_usage: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/shared_vm_count_usage'
    "$.components.schemas.RegionalQuotasSerializer.properties.shared_vm_count_usage"
    """

    snapshot_schedule_count_limit: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/snapshot_schedule_count_limit'
    "$.components.schemas.RegionalQuotasSerializer.properties.snapshot_schedule_count_limit"
    """

    snapshot_schedule_count_usage: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/snapshot_schedule_count_usage'
    "$.components.schemas.RegionalQuotasSerializer.properties.snapshot_schedule_count_usage"
    """

    subnet_count_limit: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/subnet_count_limit'
    "$.components.schemas.RegionalQuotasSerializer.properties.subnet_count_limit"
    """

    subnet_count_usage: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/subnet_count_usage'
    "$.components.schemas.RegionalQuotasSerializer.properties.subnet_count_usage"
    """

    vm_count_limit: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/vm_count_limit'
    "$.components.schemas.RegionalQuotasSerializer.properties.vm_count_limit"
    """

    vm_count_usage: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/vm_count_usage'
    "$.components.schemas.RegionalQuotasSerializer.properties.vm_count_usage"
    """

    volume_count_limit: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/volume_count_limit'
    "$.components.schemas.RegionalQuotasSerializer.properties.volume_count_limit"
    """

    volume_count_usage: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/volume_count_usage'
    "$.components.schemas.RegionalQuotasSerializer.properties.volume_count_usage"
    """

    volume_size_limit: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/volume_size_limit'
    "$.components.schemas.RegionalQuotasSerializer.properties.volume_size_limit"
    """

    volume_size_usage: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/volume_size_usage'
    "$.components.schemas.RegionalQuotasSerializer.properties.volume_size_usage"
    """

    volume_snapshots_count_limit: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/volume_snapshots_count_limit'
    "$.components.schemas.RegionalQuotasSerializer.properties.volume_snapshots_count_limit"
    """

    volume_snapshots_count_usage: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/volume_snapshots_count_usage'
    "$.components.schemas.RegionalQuotasSerializer.properties.volume_snapshots_count_usage"
    """

    volume_snapshots_size_limit: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/volume_snapshots_size_limit'
    "$.components.schemas.RegionalQuotasSerializer.properties.volume_snapshots_size_limit"
    """

    volume_snapshots_size_usage: Optional[int] = None
    """
    '#/components/schemas/RegionalQuotasSerializer/properties/volume_snapshots_size_usage'
    "$.components.schemas.RegionalQuotasSerializer.properties.volume_snapshots_size_usage"
    """


class QuotaGetAllResponse(BaseModel):
    global_quotas: Optional[GlobalQuotas] = None
    """
    '#/components/schemas/AllClientQuotasSerializer/properties/global_quotas'
    "$.components.schemas.AllClientQuotasSerializer.properties.global_quotas"
    """

    regional_quotas: Optional[List[RegionalQuota]] = None
    """
    '#/components/schemas/AllClientQuotasSerializer/properties/regional_quotas'
    "$.components.schemas.AllClientQuotasSerializer.properties.regional_quotas"
    """
