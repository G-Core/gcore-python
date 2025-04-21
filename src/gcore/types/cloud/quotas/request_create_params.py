# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["RequestCreateParams", "RequestedLimits", "RequestedLimitsGlobalLimits", "RequestedLimitsRegionalLimit"]


class RequestCreateParams(TypedDict, total=False):
    description: Required[str]
    """
    '#/components/schemas/LimitsRequestCreateSerializer/properties/description'
    "$.components.schemas.LimitsRequestCreateSerializer.properties.description"
    """

    requested_limits: Required[RequestedLimits]
    """
    '#/components/schemas/LimitsRequestCreateSerializer/properties/requested_limits'
    "$.components.schemas.LimitsRequestCreateSerializer.properties.requested_limits"
    """

    client_id: int
    """
    '#/components/schemas/LimitsRequestCreateSerializer/properties/client_id'
    "$.components.schemas.LimitsRequestCreateSerializer.properties.client_id"
    """


class RequestedLimitsGlobalLimits(TypedDict, total=False):
    inference_cpu_millicore_count_limit: int
    """
    '#/components/schemas/CreateGlobalQuotasLimitsSerializer/properties/inference_cpu_millicore_count_limit'
    "$.components.schemas.CreateGlobalQuotasLimitsSerializer.properties.inference_cpu_millicore_count_limit"
    """

    inference_gpu_a100_count_limit: int
    """
    '#/components/schemas/CreateGlobalQuotasLimitsSerializer/properties/inference_gpu_a100_count_limit'
    "$.components.schemas.CreateGlobalQuotasLimitsSerializer.properties.inference_gpu_a100_count_limit"
    """

    inference_gpu_h100_count_limit: int
    """
    '#/components/schemas/CreateGlobalQuotasLimitsSerializer/properties/inference_gpu_h100_count_limit'
    "$.components.schemas.CreateGlobalQuotasLimitsSerializer.properties.inference_gpu_h100_count_limit"
    """

    inference_gpu_l40s_count_limit: int
    """
    '#/components/schemas/CreateGlobalQuotasLimitsSerializer/properties/inference_gpu_l40s_count_limit'
    "$.components.schemas.CreateGlobalQuotasLimitsSerializer.properties.inference_gpu_l40s_count_limit"
    """

    inference_instance_count_limit: int
    """
    '#/components/schemas/CreateGlobalQuotasLimitsSerializer/properties/inference_instance_count_limit'
    "$.components.schemas.CreateGlobalQuotasLimitsSerializer.properties.inference_instance_count_limit"
    """

    keypair_count_limit: int
    """
    '#/components/schemas/CreateGlobalQuotasLimitsSerializer/properties/keypair_count_limit'
    "$.components.schemas.CreateGlobalQuotasLimitsSerializer.properties.keypair_count_limit"
    """

    project_count_limit: int
    """
    '#/components/schemas/CreateGlobalQuotasLimitsSerializer/properties/project_count_limit'
    "$.components.schemas.CreateGlobalQuotasLimitsSerializer.properties.project_count_limit"
    """


class RequestedLimitsRegionalLimit(TypedDict, total=False):
    baremetal_basic_count_limit: int
    """
    '#/components/schemas/RegionalQuotasLimitsSerializer/properties/baremetal_basic_count_limit'
    "$.components.schemas.RegionalQuotasLimitsSerializer.properties.baremetal_basic_count_limit"
    """

    baremetal_gpu_count_limit: int
    """
    '#/components/schemas/RegionalQuotasLimitsSerializer/properties/baremetal_gpu_count_limit'
    "$.components.schemas.RegionalQuotasLimitsSerializer.properties.baremetal_gpu_count_limit"
    """

    baremetal_hf_count_limit: int
    """
    '#/components/schemas/RegionalQuotasLimitsSerializer/properties/baremetal_hf_count_limit'
    "$.components.schemas.RegionalQuotasLimitsSerializer.properties.baremetal_hf_count_limit"
    """

    baremetal_infrastructure_count_limit: int
    """
    '#/components/schemas/RegionalQuotasLimitsSerializer/properties/baremetal_infrastructure_count_limit'
    "$.components.schemas.RegionalQuotasLimitsSerializer.properties.baremetal_infrastructure_count_limit"
    """

    baremetal_network_count_limit: int
    """
    '#/components/schemas/RegionalQuotasLimitsSerializer/properties/baremetal_network_count_limit'
    "$.components.schemas.RegionalQuotasLimitsSerializer.properties.baremetal_network_count_limit"
    """

    baremetal_storage_count_limit: int
    """
    '#/components/schemas/RegionalQuotasLimitsSerializer/properties/baremetal_storage_count_limit'
    "$.components.schemas.RegionalQuotasLimitsSerializer.properties.baremetal_storage_count_limit"
    """

    caas_container_count_limit: int
    """
    '#/components/schemas/RegionalQuotasLimitsSerializer/properties/caas_container_count_limit'
    "$.components.schemas.RegionalQuotasLimitsSerializer.properties.caas_container_count_limit"
    """

    caas_cpu_count_limit: int
    """
    '#/components/schemas/RegionalQuotasLimitsSerializer/properties/caas_cpu_count_limit'
    "$.components.schemas.RegionalQuotasLimitsSerializer.properties.caas_cpu_count_limit"
    """

    caas_gpu_count_limit: int
    """
    '#/components/schemas/RegionalQuotasLimitsSerializer/properties/caas_gpu_count_limit'
    "$.components.schemas.RegionalQuotasLimitsSerializer.properties.caas_gpu_count_limit"
    """

    caas_ram_size_limit: int
    """
    '#/components/schemas/RegionalQuotasLimitsSerializer/properties/caas_ram_size_limit'
    "$.components.schemas.RegionalQuotasLimitsSerializer.properties.caas_ram_size_limit"
    """

    cluster_count_limit: int
    """
    '#/components/schemas/RegionalQuotasLimitsSerializer/properties/cluster_count_limit'
    "$.components.schemas.RegionalQuotasLimitsSerializer.properties.cluster_count_limit"
    """

    cpu_count_limit: int
    """
    '#/components/schemas/RegionalQuotasLimitsSerializer/properties/cpu_count_limit'
    "$.components.schemas.RegionalQuotasLimitsSerializer.properties.cpu_count_limit"
    """

    dbaas_postgres_cluster_count_limit: int
    """
    '#/components/schemas/RegionalQuotasLimitsSerializer/properties/dbaas_postgres_cluster_count_limit'
    "$.components.schemas.RegionalQuotasLimitsSerializer.properties.dbaas_postgres_cluster_count_limit"
    """

    external_ip_count_limit: int
    """
    '#/components/schemas/RegionalQuotasLimitsSerializer/properties/external_ip_count_limit'
    "$.components.schemas.RegionalQuotasLimitsSerializer.properties.external_ip_count_limit"
    """

    faas_cpu_count_limit: int
    """
    '#/components/schemas/RegionalQuotasLimitsSerializer/properties/faas_cpu_count_limit'
    "$.components.schemas.RegionalQuotasLimitsSerializer.properties.faas_cpu_count_limit"
    """

    faas_function_count_limit: int
    """
    '#/components/schemas/RegionalQuotasLimitsSerializer/properties/faas_function_count_limit'
    "$.components.schemas.RegionalQuotasLimitsSerializer.properties.faas_function_count_limit"
    """

    faas_namespace_count_limit: int
    """
    '#/components/schemas/RegionalQuotasLimitsSerializer/properties/faas_namespace_count_limit'
    "$.components.schemas.RegionalQuotasLimitsSerializer.properties.faas_namespace_count_limit"
    """

    faas_ram_size_limit: int
    """
    '#/components/schemas/RegionalQuotasLimitsSerializer/properties/faas_ram_size_limit'
    "$.components.schemas.RegionalQuotasLimitsSerializer.properties.faas_ram_size_limit"
    """

    firewall_count_limit: int
    """
    '#/components/schemas/RegionalQuotasLimitsSerializer/properties/firewall_count_limit'
    "$.components.schemas.RegionalQuotasLimitsSerializer.properties.firewall_count_limit"
    """

    floating_count_limit: int
    """
    '#/components/schemas/RegionalQuotasLimitsSerializer/properties/floating_count_limit'
    "$.components.schemas.RegionalQuotasLimitsSerializer.properties.floating_count_limit"
    """

    gpu_count_limit: int
    """
    '#/components/schemas/RegionalQuotasLimitsSerializer/properties/gpu_count_limit'
    "$.components.schemas.RegionalQuotasLimitsSerializer.properties.gpu_count_limit"
    """

    gpu_virtual_a100_count_limit: int
    """
    '#/components/schemas/RegionalQuotasLimitsSerializer/properties/gpu_virtual_a100_count_limit'
    "$.components.schemas.RegionalQuotasLimitsSerializer.properties.gpu_virtual_a100_count_limit"
    """

    gpu_virtual_h100_count_limit: int
    """
    '#/components/schemas/RegionalQuotasLimitsSerializer/properties/gpu_virtual_h100_count_limit'
    "$.components.schemas.RegionalQuotasLimitsSerializer.properties.gpu_virtual_h100_count_limit"
    """

    gpu_virtual_l40s_count_limit: int
    """
    '#/components/schemas/RegionalQuotasLimitsSerializer/properties/gpu_virtual_l40s_count_limit'
    "$.components.schemas.RegionalQuotasLimitsSerializer.properties.gpu_virtual_l40s_count_limit"
    """

    image_count_limit: int
    """
    '#/components/schemas/RegionalQuotasLimitsSerializer/properties/image_count_limit'
    "$.components.schemas.RegionalQuotasLimitsSerializer.properties.image_count_limit"
    """

    image_size_limit: int
    """
    '#/components/schemas/RegionalQuotasLimitsSerializer/properties/image_size_limit'
    "$.components.schemas.RegionalQuotasLimitsSerializer.properties.image_size_limit"
    """

    ipu_count_limit: int
    """
    '#/components/schemas/RegionalQuotasLimitsSerializer/properties/ipu_count_limit'
    "$.components.schemas.RegionalQuotasLimitsSerializer.properties.ipu_count_limit"
    """

    laas_topic_count_limit: int
    """
    '#/components/schemas/RegionalQuotasLimitsSerializer/properties/laas_topic_count_limit'
    "$.components.schemas.RegionalQuotasLimitsSerializer.properties.laas_topic_count_limit"
    """

    loadbalancer_count_limit: int
    """
    '#/components/schemas/RegionalQuotasLimitsSerializer/properties/loadbalancer_count_limit'
    "$.components.schemas.RegionalQuotasLimitsSerializer.properties.loadbalancer_count_limit"
    """

    network_count_limit: int
    """
    '#/components/schemas/RegionalQuotasLimitsSerializer/properties/network_count_limit'
    "$.components.schemas.RegionalQuotasLimitsSerializer.properties.network_count_limit"
    """

    ram_limit: int
    """
    '#/components/schemas/RegionalQuotasLimitsSerializer/properties/ram_limit'
    "$.components.schemas.RegionalQuotasLimitsSerializer.properties.ram_limit"
    """

    region_id: int
    """
    '#/components/schemas/RegionalQuotasLimitsSerializer/properties/region_id'
    "$.components.schemas.RegionalQuotasLimitsSerializer.properties.region_id"
    """

    registry_count_limit: int
    """
    '#/components/schemas/RegionalQuotasLimitsSerializer/properties/registry_count_limit'
    "$.components.schemas.RegionalQuotasLimitsSerializer.properties.registry_count_limit"
    """

    registry_storage_limit: int
    """
    '#/components/schemas/RegionalQuotasLimitsSerializer/properties/registry_storage_limit'
    "$.components.schemas.RegionalQuotasLimitsSerializer.properties.registry_storage_limit"
    """

    router_count_limit: int
    """
    '#/components/schemas/RegionalQuotasLimitsSerializer/properties/router_count_limit'
    "$.components.schemas.RegionalQuotasLimitsSerializer.properties.router_count_limit"
    """

    secret_count_limit: int
    """
    '#/components/schemas/RegionalQuotasLimitsSerializer/properties/secret_count_limit'
    "$.components.schemas.RegionalQuotasLimitsSerializer.properties.secret_count_limit"
    """

    servergroup_count_limit: int
    """
    '#/components/schemas/RegionalQuotasLimitsSerializer/properties/servergroup_count_limit'
    "$.components.schemas.RegionalQuotasLimitsSerializer.properties.servergroup_count_limit"
    """

    sfs_count_limit: int
    """
    '#/components/schemas/RegionalQuotasLimitsSerializer/properties/sfs_count_limit'
    "$.components.schemas.RegionalQuotasLimitsSerializer.properties.sfs_count_limit"
    """

    sfs_size_limit: int
    """
    '#/components/schemas/RegionalQuotasLimitsSerializer/properties/sfs_size_limit'
    "$.components.schemas.RegionalQuotasLimitsSerializer.properties.sfs_size_limit"
    """

    shared_vm_count_limit: int
    """
    '#/components/schemas/RegionalQuotasLimitsSerializer/properties/shared_vm_count_limit'
    "$.components.schemas.RegionalQuotasLimitsSerializer.properties.shared_vm_count_limit"
    """

    snapshot_schedule_count_limit: int
    """
    '#/components/schemas/RegionalQuotasLimitsSerializer/properties/snapshot_schedule_count_limit'
    "$.components.schemas.RegionalQuotasLimitsSerializer.properties.snapshot_schedule_count_limit"
    """

    subnet_count_limit: int
    """
    '#/components/schemas/RegionalQuotasLimitsSerializer/properties/subnet_count_limit'
    "$.components.schemas.RegionalQuotasLimitsSerializer.properties.subnet_count_limit"
    """

    vm_count_limit: int
    """
    '#/components/schemas/RegionalQuotasLimitsSerializer/properties/vm_count_limit'
    "$.components.schemas.RegionalQuotasLimitsSerializer.properties.vm_count_limit"
    """

    volume_count_limit: int
    """
    '#/components/schemas/RegionalQuotasLimitsSerializer/properties/volume_count_limit'
    "$.components.schemas.RegionalQuotasLimitsSerializer.properties.volume_count_limit"
    """

    volume_size_limit: int
    """
    '#/components/schemas/RegionalQuotasLimitsSerializer/properties/volume_size_limit'
    "$.components.schemas.RegionalQuotasLimitsSerializer.properties.volume_size_limit"
    """

    volume_snapshots_count_limit: int
    """
    '#/components/schemas/RegionalQuotasLimitsSerializer/properties/volume_snapshots_count_limit'
    "$.components.schemas.RegionalQuotasLimitsSerializer.properties.volume_snapshots_count_limit"
    """

    volume_snapshots_size_limit: int
    """
    '#/components/schemas/RegionalQuotasLimitsSerializer/properties/volume_snapshots_size_limit'
    "$.components.schemas.RegionalQuotasLimitsSerializer.properties.volume_snapshots_size_limit"
    """


class RequestedLimits(TypedDict, total=False):
    global_limits: RequestedLimitsGlobalLimits
    """
    '#/components/schemas/ClientMixedQuotasLimitsSerializer/properties/global_limits'
    "$.components.schemas.ClientMixedQuotasLimitsSerializer.properties.global_limits"
    """

    regional_limits: Iterable[RequestedLimitsRegionalLimit]
    """
    '#/components/schemas/ClientMixedQuotasLimitsSerializer/properties/regional_limits'
    "$.components.schemas.ClientMixedQuotasLimitsSerializer.properties.regional_limits"
    """
