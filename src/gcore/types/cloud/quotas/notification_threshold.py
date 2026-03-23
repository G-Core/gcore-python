# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = [
    "NotificationThreshold",
    "LastMessage",
    "LastMessageGlobalQuotas",
    "LastMessageGlobalQuotasInferenceCPUMillicoreCountLimit",
    "LastMessageGlobalQuotasInferenceCPUMillicoreCountUsage",
    "LastMessageGlobalQuotasInferenceGPUA100CountLimit",
    "LastMessageGlobalQuotasInferenceGPUA100CountUsage",
    "LastMessageGlobalQuotasInferenceGPUH100CountLimit",
    "LastMessageGlobalQuotasInferenceGPUH100CountUsage",
    "LastMessageGlobalQuotasInferenceGPUL40sCountLimit",
    "LastMessageGlobalQuotasInferenceGPUL40sCountUsage",
    "LastMessageGlobalQuotasInferenceInstanceCountLimit",
    "LastMessageGlobalQuotasInferenceInstanceCountUsage",
    "LastMessageGlobalQuotasKeypairCountLimit",
    "LastMessageGlobalQuotasKeypairCountUsage",
    "LastMessageGlobalQuotasProjectCountLimit",
    "LastMessageGlobalQuotasProjectCountUsage",
    "LastMessageRegionalQuota",
    "LastMessageRegionalQuotaBaremetalBasicCountLimit",
    "LastMessageRegionalQuotaBaremetalBasicCountUsage",
    "LastMessageRegionalQuotaBaremetalGPUA100CountLimit",
    "LastMessageRegionalQuotaBaremetalGPUA100CountUsage",
    "LastMessageRegionalQuotaBaremetalGPUH100CountLimit",
    "LastMessageRegionalQuotaBaremetalGPUH100CountUsage",
    "LastMessageRegionalQuotaBaremetalGPUH200CountLimit",
    "LastMessageRegionalQuotaBaremetalGPUH200CountUsage",
    "LastMessageRegionalQuotaBaremetalGPUL40sCountLimit",
    "LastMessageRegionalQuotaBaremetalGPUL40sCountUsage",
    "LastMessageRegionalQuotaBaremetalHfCountLimit",
    "LastMessageRegionalQuotaBaremetalHfCountUsage",
    "LastMessageRegionalQuotaBaremetalInfrastructureCountLimit",
    "LastMessageRegionalQuotaBaremetalInfrastructureCountUsage",
    "LastMessageRegionalQuotaBaremetalNetworkCountLimit",
    "LastMessageRegionalQuotaBaremetalNetworkCountUsage",
    "LastMessageRegionalQuotaBaremetalStorageCountLimit",
    "LastMessageRegionalQuotaBaremetalStorageCountUsage",
    "LastMessageRegionalQuotaCaasContainerCountLimit",
    "LastMessageRegionalQuotaCaasContainerCountUsage",
    "LastMessageRegionalQuotaCaasCPUCountLimit",
    "LastMessageRegionalQuotaCaasCPUCountUsage",
    "LastMessageRegionalQuotaCaasGPUCountLimit",
    "LastMessageRegionalQuotaCaasGPUCountUsage",
    "LastMessageRegionalQuotaCaasRamSizeLimit",
    "LastMessageRegionalQuotaCaasRamSizeUsage",
    "LastMessageRegionalQuotaClusterCountLimit",
    "LastMessageRegionalQuotaClusterCountUsage",
    "LastMessageRegionalQuotaCPUCountLimit",
    "LastMessageRegionalQuotaCPUCountUsage",
    "LastMessageRegionalQuotaDbaasPostgresClusterCountLimit",
    "LastMessageRegionalQuotaDbaasPostgresClusterCountUsage",
    "LastMessageRegionalQuotaExternalIPCountLimit",
    "LastMessageRegionalQuotaExternalIPCountUsage",
    "LastMessageRegionalQuotaFaasCPUCountLimit",
    "LastMessageRegionalQuotaFaasCPUCountUsage",
    "LastMessageRegionalQuotaFaasFunctionCountLimit",
    "LastMessageRegionalQuotaFaasFunctionCountUsage",
    "LastMessageRegionalQuotaFaasNamespaceCountLimit",
    "LastMessageRegionalQuotaFaasNamespaceCountUsage",
    "LastMessageRegionalQuotaFaasRamSizeLimit",
    "LastMessageRegionalQuotaFaasRamSizeUsage",
    "LastMessageRegionalQuotaFirewallCountLimit",
    "LastMessageRegionalQuotaFirewallCountUsage",
    "LastMessageRegionalQuotaFloatingCountLimit",
    "LastMessageRegionalQuotaFloatingCountUsage",
    "LastMessageRegionalQuotaGPUCountLimit",
    "LastMessageRegionalQuotaGPUCountUsage",
    "LastMessageRegionalQuotaGPUVirtualA100CountLimit",
    "LastMessageRegionalQuotaGPUVirtualA100CountUsage",
    "LastMessageRegionalQuotaGPUVirtualH100CountLimit",
    "LastMessageRegionalQuotaGPUVirtualH100CountUsage",
    "LastMessageRegionalQuotaGPUVirtualH200CountLimit",
    "LastMessageRegionalQuotaGPUVirtualH200CountUsage",
    "LastMessageRegionalQuotaGPUVirtualL40sCountLimit",
    "LastMessageRegionalQuotaGPUVirtualL40sCountUsage",
    "LastMessageRegionalQuotaImageCountLimit",
    "LastMessageRegionalQuotaImageCountUsage",
    "LastMessageRegionalQuotaImageSizeLimit",
    "LastMessageRegionalQuotaImageSizeUsage",
    "LastMessageRegionalQuotaIpuCountLimit",
    "LastMessageRegionalQuotaIpuCountUsage",
    "LastMessageRegionalQuotaLaasTopicCountLimit",
    "LastMessageRegionalQuotaLaasTopicCountUsage",
    "LastMessageRegionalQuotaLoadbalancerCountLimit",
    "LastMessageRegionalQuotaLoadbalancerCountUsage",
    "LastMessageRegionalQuotaNetworkCountLimit",
    "LastMessageRegionalQuotaNetworkCountUsage",
    "LastMessageRegionalQuotaRamLimit",
    "LastMessageRegionalQuotaRamUsage",
    "LastMessageRegionalQuotaRegistryCountLimit",
    "LastMessageRegionalQuotaRegistryCountUsage",
    "LastMessageRegionalQuotaRegistryStorageLimit",
    "LastMessageRegionalQuotaRegistryStorageUsage",
    "LastMessageRegionalQuotaRouterCountLimit",
    "LastMessageRegionalQuotaRouterCountUsage",
    "LastMessageRegionalQuotaSecretCountLimit",
    "LastMessageRegionalQuotaSecretCountUsage",
    "LastMessageRegionalQuotaServergroupCountLimit",
    "LastMessageRegionalQuotaServergroupCountUsage",
    "LastMessageRegionalQuotaSfsCountLimit",
    "LastMessageRegionalQuotaSfsCountUsage",
    "LastMessageRegionalQuotaSfsSizeLimit",
    "LastMessageRegionalQuotaSfsSizeUsage",
    "LastMessageRegionalQuotaSharedVmCountLimit",
    "LastMessageRegionalQuotaSharedVmCountUsage",
    "LastMessageRegionalQuotaSnapshotScheduleCountLimit",
    "LastMessageRegionalQuotaSnapshotScheduleCountUsage",
    "LastMessageRegionalQuotaSubnetCountLimit",
    "LastMessageRegionalQuotaSubnetCountUsage",
    "LastMessageRegionalQuotaVmCountLimit",
    "LastMessageRegionalQuotaVmCountUsage",
    "LastMessageRegionalQuotaVolumeCountLimit",
    "LastMessageRegionalQuotaVolumeCountUsage",
    "LastMessageRegionalQuotaVolumeSizeLimit",
    "LastMessageRegionalQuotaVolumeSizeUsage",
    "LastMessageRegionalQuotaVolumeSnapshotsCountLimit",
    "LastMessageRegionalQuotaVolumeSnapshotsCountUsage",
    "LastMessageRegionalQuotaVolumeSnapshotsSizeLimit",
    "LastMessageRegionalQuotaVolumeSnapshotsSizeUsage",
]


class LastMessageGlobalQuotasInferenceCPUMillicoreCountLimit(BaseModel):
    """Inference CPU millicore count limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageGlobalQuotasInferenceCPUMillicoreCountUsage(BaseModel):
    """Inference CPU millicore count usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageGlobalQuotasInferenceGPUA100CountLimit(BaseModel):
    """Inference GPU A100 Count limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageGlobalQuotasInferenceGPUA100CountUsage(BaseModel):
    """Inference GPU A100 Count usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageGlobalQuotasInferenceGPUH100CountLimit(BaseModel):
    """Inference GPU H100 Count limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageGlobalQuotasInferenceGPUH100CountUsage(BaseModel):
    """Inference GPU H100 Count usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageGlobalQuotasInferenceGPUL40sCountLimit(BaseModel):
    """Inference GPU L40s Count limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageGlobalQuotasInferenceGPUL40sCountUsage(BaseModel):
    """Inference GPU L40s Count usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageGlobalQuotasInferenceInstanceCountLimit(BaseModel):
    """Inference instance count limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageGlobalQuotasInferenceInstanceCountUsage(BaseModel):
    """Inference instance count usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageGlobalQuotasKeypairCountLimit(BaseModel):
    """SSH Keys Count limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageGlobalQuotasKeypairCountUsage(BaseModel):
    """SSH Keys Count usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageGlobalQuotasProjectCountLimit(BaseModel):
    """Projects Count limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageGlobalQuotasProjectCountUsage(BaseModel):
    """Projects Count usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageGlobalQuotas(BaseModel):
    """Global quota that exceed the threshold"""

    inference_cpu_millicore_count_limit: Optional[LastMessageGlobalQuotasInferenceCPUMillicoreCountLimit] = None
    """Inference CPU millicore count limit"""

    inference_cpu_millicore_count_usage: Optional[LastMessageGlobalQuotasInferenceCPUMillicoreCountUsage] = None
    """Inference CPU millicore count usage"""

    inference_gpu_a100_count_limit: Optional[LastMessageGlobalQuotasInferenceGPUA100CountLimit] = None
    """Inference GPU A100 Count limit"""

    inference_gpu_a100_count_usage: Optional[LastMessageGlobalQuotasInferenceGPUA100CountUsage] = None
    """Inference GPU A100 Count usage"""

    inference_gpu_h100_count_limit: Optional[LastMessageGlobalQuotasInferenceGPUH100CountLimit] = None
    """Inference GPU H100 Count limit"""

    inference_gpu_h100_count_usage: Optional[LastMessageGlobalQuotasInferenceGPUH100CountUsage] = None
    """Inference GPU H100 Count usage"""

    inference_gpu_l40s_count_limit: Optional[LastMessageGlobalQuotasInferenceGPUL40sCountLimit] = None
    """Inference GPU L40s Count limit"""

    inference_gpu_l40s_count_usage: Optional[LastMessageGlobalQuotasInferenceGPUL40sCountUsage] = None
    """Inference GPU L40s Count usage"""

    inference_instance_count_limit: Optional[LastMessageGlobalQuotasInferenceInstanceCountLimit] = None
    """Inference instance count limit"""

    inference_instance_count_usage: Optional[LastMessageGlobalQuotasInferenceInstanceCountUsage] = None
    """Inference instance count usage"""

    keypair_count_limit: Optional[LastMessageGlobalQuotasKeypairCountLimit] = None
    """SSH Keys Count limit"""

    keypair_count_usage: Optional[LastMessageGlobalQuotasKeypairCountUsage] = None
    """SSH Keys Count usage"""

    project_count_limit: Optional[LastMessageGlobalQuotasProjectCountLimit] = None
    """Projects Count limit"""

    project_count_usage: Optional[LastMessageGlobalQuotasProjectCountUsage] = None
    """Projects Count usage"""


class LastMessageRegionalQuotaBaremetalBasicCountLimit(BaseModel):
    """Basic bare metal servers count limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaBaremetalBasicCountUsage(BaseModel):
    """Basic bare metal servers count usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaBaremetalGPUA100CountLimit(BaseModel):
    """Bare metal A100 GPU server count limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaBaremetalGPUA100CountUsage(BaseModel):
    """Bare metal A100 GPU server count usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaBaremetalGPUH100CountLimit(BaseModel):
    """Bare metal H100 GPU server count limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaBaremetalGPUH100CountUsage(BaseModel):
    """Bare metal H100 GPU server count usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaBaremetalGPUH200CountLimit(BaseModel):
    """Bare metal H200 GPU server count limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaBaremetalGPUH200CountUsage(BaseModel):
    """Bare metal H200 GPU server count usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaBaremetalGPUL40sCountLimit(BaseModel):
    """Bare metal L40S GPU server count limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaBaremetalGPUL40sCountUsage(BaseModel):
    """Bare metal L40S GPU server count usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaBaremetalHfCountLimit(BaseModel):
    """High-frequency bare metal servers count limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaBaremetalHfCountUsage(BaseModel):
    """High-frequency bare metal servers count usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaBaremetalInfrastructureCountLimit(BaseModel):
    """Infrastructure bare metal servers count limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaBaremetalInfrastructureCountUsage(BaseModel):
    """Infrastructure bare metal servers count usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaBaremetalNetworkCountLimit(BaseModel):
    """Bare metal Network Count limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaBaremetalNetworkCountUsage(BaseModel):
    """Bare metal Network Count usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaBaremetalStorageCountLimit(BaseModel):
    """Storage bare metal servers count limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaBaremetalStorageCountUsage(BaseModel):
    """Storage bare metal servers count usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaCaasContainerCountLimit(BaseModel):
    """Containers count limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaCaasContainerCountUsage(BaseModel):
    """Containers count usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaCaasCPUCountLimit(BaseModel):
    """mCPU count for containers limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaCaasCPUCountUsage(BaseModel):
    """mCPU count for containers usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaCaasGPUCountLimit(BaseModel):
    """Containers gpu count limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaCaasGPUCountUsage(BaseModel):
    """Containers gpu count usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaCaasRamSizeLimit(BaseModel):
    """MiB memory count for containers limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaCaasRamSizeUsage(BaseModel):
    """MiB memory count for containers usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaClusterCountLimit(BaseModel):
    """K8s clusters count limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaClusterCountUsage(BaseModel):
    """K8s clusters count usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaCPUCountLimit(BaseModel):
    """vCPU Count limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaCPUCountUsage(BaseModel):
    """vCPU Count usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaDbaasPostgresClusterCountLimit(BaseModel):
    """DBaaS cluster count limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaDbaasPostgresClusterCountUsage(BaseModel):
    """DBaaS cluster count usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaExternalIPCountLimit(BaseModel):
    """External IP Count limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaExternalIPCountUsage(BaseModel):
    """External IP Count usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaFaasCPUCountLimit(BaseModel):
    """mCPU count for functions limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaFaasCPUCountUsage(BaseModel):
    """mCPU count for functions usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaFaasFunctionCountLimit(BaseModel):
    """Functions count limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaFaasFunctionCountUsage(BaseModel):
    """Functions count usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaFaasNamespaceCountLimit(BaseModel):
    """Functions namespace count limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaFaasNamespaceCountUsage(BaseModel):
    """Functions namespace count usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaFaasRamSizeLimit(BaseModel):
    """MiB memory count for functions limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaFaasRamSizeUsage(BaseModel):
    """MiB memory count for functions usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaFirewallCountLimit(BaseModel):
    """Firewalls Count limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaFirewallCountUsage(BaseModel):
    """Firewalls Count usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaFloatingCountLimit(BaseModel):
    """Floating IP Count limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaFloatingCountUsage(BaseModel):
    """Floating IP Count usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaGPUCountLimit(BaseModel):
    """GPU Count limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaGPUCountUsage(BaseModel):
    """GPU Count usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaGPUVirtualA100CountLimit(BaseModel):
    """Virtual A100 GPU card count limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaGPUVirtualA100CountUsage(BaseModel):
    """Virtual A100 GPU card count usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaGPUVirtualH100CountLimit(BaseModel):
    """Virtual H100 GPU card count limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaGPUVirtualH100CountUsage(BaseModel):
    """Virtual H100 GPU card count usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaGPUVirtualH200CountLimit(BaseModel):
    """Virtual H200 GPU card count limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaGPUVirtualH200CountUsage(BaseModel):
    """Virtual H200 GPU card count usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaGPUVirtualL40sCountLimit(BaseModel):
    """Virtual L40S GPU card count limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaGPUVirtualL40sCountUsage(BaseModel):
    """Virtual L40S GPU card count usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaImageCountLimit(BaseModel):
    """Images Count limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaImageCountUsage(BaseModel):
    """Images Count usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaImageSizeLimit(BaseModel):
    """Images Size, bytes limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaImageSizeUsage(BaseModel):
    """Images Size, bytes usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaIpuCountLimit(BaseModel):
    """IPU Count limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaIpuCountUsage(BaseModel):
    """IPU Count usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaLaasTopicCountLimit(BaseModel):
    """LaaS Topics Count limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaLaasTopicCountUsage(BaseModel):
    """LaaS Topics Count usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaLoadbalancerCountLimit(BaseModel):
    """Load Balancers Count limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaLoadbalancerCountUsage(BaseModel):
    """Load Balancers Count usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaNetworkCountLimit(BaseModel):
    """Networks Count limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaNetworkCountUsage(BaseModel):
    """Networks Count usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaRamLimit(BaseModel):
    """RAM Size, MiB limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaRamUsage(BaseModel):
    """RAM Size, MiB usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaRegistryCountLimit(BaseModel):
    """Registries count limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaRegistryCountUsage(BaseModel):
    """Registries count usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaRegistryStorageLimit(BaseModel):
    """Registries volume usage, GiB limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaRegistryStorageUsage(BaseModel):
    """Registries volume usage, GiB usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaRouterCountLimit(BaseModel):
    """Routers Count limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaRouterCountUsage(BaseModel):
    """Routers Count usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaSecretCountLimit(BaseModel):
    """Secret Count limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaSecretCountUsage(BaseModel):
    """Secret Count usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaServergroupCountLimit(BaseModel):
    """Placement Group Count limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaServergroupCountUsage(BaseModel):
    """Placement Group Count usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaSfsCountLimit(BaseModel):
    """Shared file system Count limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaSfsCountUsage(BaseModel):
    """Shared file system Count usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaSfsSizeLimit(BaseModel):
    """Shared file system Size, GiB limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaSfsSizeUsage(BaseModel):
    """Shared file system Size, GiB usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaSharedVmCountLimit(BaseModel):
    """Basic VMs Count limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaSharedVmCountUsage(BaseModel):
    """Basic VMs Count usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaSnapshotScheduleCountLimit(BaseModel):
    """Snapshot Schedules Count limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaSnapshotScheduleCountUsage(BaseModel):
    """Snapshot Schedules Count usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaSubnetCountLimit(BaseModel):
    """Subnets Count limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaSubnetCountUsage(BaseModel):
    """Subnets Count usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaVmCountLimit(BaseModel):
    """Instances Dedicated Count limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaVmCountUsage(BaseModel):
    """Instances Dedicated Count usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaVolumeCountLimit(BaseModel):
    """Volumes Count limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaVolumeCountUsage(BaseModel):
    """Volumes Count usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaVolumeSizeLimit(BaseModel):
    """Volumes Size, GiB limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaVolumeSizeUsage(BaseModel):
    """Volumes Size, GiB usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaVolumeSnapshotsCountLimit(BaseModel):
    """Snapshots Count limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaVolumeSnapshotsCountUsage(BaseModel):
    """Snapshots Count usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaVolumeSnapshotsSizeLimit(BaseModel):
    """Snapshots Size, GiB limit"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaVolumeSnapshotsSizeUsage(BaseModel):
    """Snapshots Size, GiB usage"""

    limit: int
    """Сurrent quota limit"""

    usage: int
    """Сurrent amount of resource used"""


class LastMessageRegionalQuota(BaseModel):
    region_id: int
    """Region id"""

    region_name: str
    """Region name"""

    baremetal_basic_count_limit: Optional[LastMessageRegionalQuotaBaremetalBasicCountLimit] = None
    """Basic bare metal servers count limit"""

    baremetal_basic_count_usage: Optional[LastMessageRegionalQuotaBaremetalBasicCountUsage] = None
    """Basic bare metal servers count usage"""

    baremetal_gpu_a100_count_limit: Optional[LastMessageRegionalQuotaBaremetalGPUA100CountLimit] = None
    """Bare metal A100 GPU server count limit"""

    baremetal_gpu_a100_count_usage: Optional[LastMessageRegionalQuotaBaremetalGPUA100CountUsage] = None
    """Bare metal A100 GPU server count usage"""

    baremetal_gpu_h100_count_limit: Optional[LastMessageRegionalQuotaBaremetalGPUH100CountLimit] = None
    """Bare metal H100 GPU server count limit"""

    baremetal_gpu_h100_count_usage: Optional[LastMessageRegionalQuotaBaremetalGPUH100CountUsage] = None
    """Bare metal H100 GPU server count usage"""

    baremetal_gpu_h200_count_limit: Optional[LastMessageRegionalQuotaBaremetalGPUH200CountLimit] = None
    """Bare metal H200 GPU server count limit"""

    baremetal_gpu_h200_count_usage: Optional[LastMessageRegionalQuotaBaremetalGPUH200CountUsage] = None
    """Bare metal H200 GPU server count usage"""

    baremetal_gpu_l40s_count_limit: Optional[LastMessageRegionalQuotaBaremetalGPUL40sCountLimit] = None
    """Bare metal L40S GPU server count limit"""

    baremetal_gpu_l40s_count_usage: Optional[LastMessageRegionalQuotaBaremetalGPUL40sCountUsage] = None
    """Bare metal L40S GPU server count usage"""

    baremetal_hf_count_limit: Optional[LastMessageRegionalQuotaBaremetalHfCountLimit] = None
    """High-frequency bare metal servers count limit"""

    baremetal_hf_count_usage: Optional[LastMessageRegionalQuotaBaremetalHfCountUsage] = None
    """High-frequency bare metal servers count usage"""

    baremetal_infrastructure_count_limit: Optional[LastMessageRegionalQuotaBaremetalInfrastructureCountLimit] = None
    """Infrastructure bare metal servers count limit"""

    baremetal_infrastructure_count_usage: Optional[LastMessageRegionalQuotaBaremetalInfrastructureCountUsage] = None
    """Infrastructure bare metal servers count usage"""

    baremetal_network_count_limit: Optional[LastMessageRegionalQuotaBaremetalNetworkCountLimit] = None
    """Bare metal Network Count limit"""

    baremetal_network_count_usage: Optional[LastMessageRegionalQuotaBaremetalNetworkCountUsage] = None
    """Bare metal Network Count usage"""

    baremetal_storage_count_limit: Optional[LastMessageRegionalQuotaBaremetalStorageCountLimit] = None
    """Storage bare metal servers count limit"""

    baremetal_storage_count_usage: Optional[LastMessageRegionalQuotaBaremetalStorageCountUsage] = None
    """Storage bare metal servers count usage"""

    caas_container_count_limit: Optional[LastMessageRegionalQuotaCaasContainerCountLimit] = None
    """Containers count limit"""

    caas_container_count_usage: Optional[LastMessageRegionalQuotaCaasContainerCountUsage] = None
    """Containers count usage"""

    caas_cpu_count_limit: Optional[LastMessageRegionalQuotaCaasCPUCountLimit] = None
    """mCPU count for containers limit"""

    caas_cpu_count_usage: Optional[LastMessageRegionalQuotaCaasCPUCountUsage] = None
    """mCPU count for containers usage"""

    caas_gpu_count_limit: Optional[LastMessageRegionalQuotaCaasGPUCountLimit] = None
    """Containers gpu count limit"""

    caas_gpu_count_usage: Optional[LastMessageRegionalQuotaCaasGPUCountUsage] = None
    """Containers gpu count usage"""

    caas_ram_size_limit: Optional[LastMessageRegionalQuotaCaasRamSizeLimit] = None
    """MiB memory count for containers limit"""

    caas_ram_size_usage: Optional[LastMessageRegionalQuotaCaasRamSizeUsage] = None
    """MiB memory count for containers usage"""

    cluster_count_limit: Optional[LastMessageRegionalQuotaClusterCountLimit] = None
    """K8s clusters count limit"""

    cluster_count_usage: Optional[LastMessageRegionalQuotaClusterCountUsage] = None
    """K8s clusters count usage"""

    cpu_count_limit: Optional[LastMessageRegionalQuotaCPUCountLimit] = None
    """vCPU Count limit"""

    cpu_count_usage: Optional[LastMessageRegionalQuotaCPUCountUsage] = None
    """vCPU Count usage"""

    dbaas_postgres_cluster_count_limit: Optional[LastMessageRegionalQuotaDbaasPostgresClusterCountLimit] = None
    """DBaaS cluster count limit"""

    dbaas_postgres_cluster_count_usage: Optional[LastMessageRegionalQuotaDbaasPostgresClusterCountUsage] = None
    """DBaaS cluster count usage"""

    external_ip_count_limit: Optional[LastMessageRegionalQuotaExternalIPCountLimit] = None
    """External IP Count limit"""

    external_ip_count_usage: Optional[LastMessageRegionalQuotaExternalIPCountUsage] = None
    """External IP Count usage"""

    faas_cpu_count_limit: Optional[LastMessageRegionalQuotaFaasCPUCountLimit] = None
    """mCPU count for functions limit"""

    faas_cpu_count_usage: Optional[LastMessageRegionalQuotaFaasCPUCountUsage] = None
    """mCPU count for functions usage"""

    faas_function_count_limit: Optional[LastMessageRegionalQuotaFaasFunctionCountLimit] = None
    """Functions count limit"""

    faas_function_count_usage: Optional[LastMessageRegionalQuotaFaasFunctionCountUsage] = None
    """Functions count usage"""

    faas_namespace_count_limit: Optional[LastMessageRegionalQuotaFaasNamespaceCountLimit] = None
    """Functions namespace count limit"""

    faas_namespace_count_usage: Optional[LastMessageRegionalQuotaFaasNamespaceCountUsage] = None
    """Functions namespace count usage"""

    faas_ram_size_limit: Optional[LastMessageRegionalQuotaFaasRamSizeLimit] = None
    """MiB memory count for functions limit"""

    faas_ram_size_usage: Optional[LastMessageRegionalQuotaFaasRamSizeUsage] = None
    """MiB memory count for functions usage"""

    firewall_count_limit: Optional[LastMessageRegionalQuotaFirewallCountLimit] = None
    """Firewalls Count limit"""

    firewall_count_usage: Optional[LastMessageRegionalQuotaFirewallCountUsage] = None
    """Firewalls Count usage"""

    floating_count_limit: Optional[LastMessageRegionalQuotaFloatingCountLimit] = None
    """Floating IP Count limit"""

    floating_count_usage: Optional[LastMessageRegionalQuotaFloatingCountUsage] = None
    """Floating IP Count usage"""

    gpu_count_limit: Optional[LastMessageRegionalQuotaGPUCountLimit] = None
    """GPU Count limit"""

    gpu_count_usage: Optional[LastMessageRegionalQuotaGPUCountUsage] = None
    """GPU Count usage"""

    gpu_virtual_a100_count_limit: Optional[LastMessageRegionalQuotaGPUVirtualA100CountLimit] = None
    """Virtual A100 GPU card count limit"""

    gpu_virtual_a100_count_usage: Optional[LastMessageRegionalQuotaGPUVirtualA100CountUsage] = None
    """Virtual A100 GPU card count usage"""

    gpu_virtual_h100_count_limit: Optional[LastMessageRegionalQuotaGPUVirtualH100CountLimit] = None
    """Virtual H100 GPU card count limit"""

    gpu_virtual_h100_count_usage: Optional[LastMessageRegionalQuotaGPUVirtualH100CountUsage] = None
    """Virtual H100 GPU card count usage"""

    gpu_virtual_h200_count_limit: Optional[LastMessageRegionalQuotaGPUVirtualH200CountLimit] = None
    """Virtual H200 GPU card count limit"""

    gpu_virtual_h200_count_usage: Optional[LastMessageRegionalQuotaGPUVirtualH200CountUsage] = None
    """Virtual H200 GPU card count usage"""

    gpu_virtual_l40s_count_limit: Optional[LastMessageRegionalQuotaGPUVirtualL40sCountLimit] = None
    """Virtual L40S GPU card count limit"""

    gpu_virtual_l40s_count_usage: Optional[LastMessageRegionalQuotaGPUVirtualL40sCountUsage] = None
    """Virtual L40S GPU card count usage"""

    image_count_limit: Optional[LastMessageRegionalQuotaImageCountLimit] = None
    """Images Count limit"""

    image_count_usage: Optional[LastMessageRegionalQuotaImageCountUsage] = None
    """Images Count usage"""

    image_size_limit: Optional[LastMessageRegionalQuotaImageSizeLimit] = None
    """Images Size, bytes limit"""

    image_size_usage: Optional[LastMessageRegionalQuotaImageSizeUsage] = None
    """Images Size, bytes usage"""

    ipu_count_limit: Optional[LastMessageRegionalQuotaIpuCountLimit] = None
    """IPU Count limit"""

    ipu_count_usage: Optional[LastMessageRegionalQuotaIpuCountUsage] = None
    """IPU Count usage"""

    laas_topic_count_limit: Optional[LastMessageRegionalQuotaLaasTopicCountLimit] = None
    """LaaS Topics Count limit"""

    laas_topic_count_usage: Optional[LastMessageRegionalQuotaLaasTopicCountUsage] = None
    """LaaS Topics Count usage"""

    loadbalancer_count_limit: Optional[LastMessageRegionalQuotaLoadbalancerCountLimit] = None
    """Load Balancers Count limit"""

    loadbalancer_count_usage: Optional[LastMessageRegionalQuotaLoadbalancerCountUsage] = None
    """Load Balancers Count usage"""

    network_count_limit: Optional[LastMessageRegionalQuotaNetworkCountLimit] = None
    """Networks Count limit"""

    network_count_usage: Optional[LastMessageRegionalQuotaNetworkCountUsage] = None
    """Networks Count usage"""

    ram_limit: Optional[LastMessageRegionalQuotaRamLimit] = None
    """RAM Size, MiB limit"""

    ram_usage: Optional[LastMessageRegionalQuotaRamUsage] = None
    """RAM Size, MiB usage"""

    registry_count_limit: Optional[LastMessageRegionalQuotaRegistryCountLimit] = None
    """Registries count limit"""

    registry_count_usage: Optional[LastMessageRegionalQuotaRegistryCountUsage] = None
    """Registries count usage"""

    registry_storage_limit: Optional[LastMessageRegionalQuotaRegistryStorageLimit] = None
    """Registries volume usage, GiB limit"""

    registry_storage_usage: Optional[LastMessageRegionalQuotaRegistryStorageUsage] = None
    """Registries volume usage, GiB usage"""

    router_count_limit: Optional[LastMessageRegionalQuotaRouterCountLimit] = None
    """Routers Count limit"""

    router_count_usage: Optional[LastMessageRegionalQuotaRouterCountUsage] = None
    """Routers Count usage"""

    secret_count_limit: Optional[LastMessageRegionalQuotaSecretCountLimit] = None
    """Secret Count limit"""

    secret_count_usage: Optional[LastMessageRegionalQuotaSecretCountUsage] = None
    """Secret Count usage"""

    servergroup_count_limit: Optional[LastMessageRegionalQuotaServergroupCountLimit] = None
    """Placement Group Count limit"""

    servergroup_count_usage: Optional[LastMessageRegionalQuotaServergroupCountUsage] = None
    """Placement Group Count usage"""

    sfs_count_limit: Optional[LastMessageRegionalQuotaSfsCountLimit] = None
    """Shared file system Count limit"""

    sfs_count_usage: Optional[LastMessageRegionalQuotaSfsCountUsage] = None
    """Shared file system Count usage"""

    sfs_size_limit: Optional[LastMessageRegionalQuotaSfsSizeLimit] = None
    """Shared file system Size, GiB limit"""

    sfs_size_usage: Optional[LastMessageRegionalQuotaSfsSizeUsage] = None
    """Shared file system Size, GiB usage"""

    shared_vm_count_limit: Optional[LastMessageRegionalQuotaSharedVmCountLimit] = None
    """Basic VMs Count limit"""

    shared_vm_count_usage: Optional[LastMessageRegionalQuotaSharedVmCountUsage] = None
    """Basic VMs Count usage"""

    snapshot_schedule_count_limit: Optional[LastMessageRegionalQuotaSnapshotScheduleCountLimit] = None
    """Snapshot Schedules Count limit"""

    snapshot_schedule_count_usage: Optional[LastMessageRegionalQuotaSnapshotScheduleCountUsage] = None
    """Snapshot Schedules Count usage"""

    subnet_count_limit: Optional[LastMessageRegionalQuotaSubnetCountLimit] = None
    """Subnets Count limit"""

    subnet_count_usage: Optional[LastMessageRegionalQuotaSubnetCountUsage] = None
    """Subnets Count usage"""

    vm_count_limit: Optional[LastMessageRegionalQuotaVmCountLimit] = None
    """Instances Dedicated Count limit"""

    vm_count_usage: Optional[LastMessageRegionalQuotaVmCountUsage] = None
    """Instances Dedicated Count usage"""

    volume_count_limit: Optional[LastMessageRegionalQuotaVolumeCountLimit] = None
    """Volumes Count limit"""

    volume_count_usage: Optional[LastMessageRegionalQuotaVolumeCountUsage] = None
    """Volumes Count usage"""

    volume_size_limit: Optional[LastMessageRegionalQuotaVolumeSizeLimit] = None
    """Volumes Size, GiB limit"""

    volume_size_usage: Optional[LastMessageRegionalQuotaVolumeSizeUsage] = None
    """Volumes Size, GiB usage"""

    volume_snapshots_count_limit: Optional[LastMessageRegionalQuotaVolumeSnapshotsCountLimit] = None
    """Snapshots Count limit"""

    volume_snapshots_count_usage: Optional[LastMessageRegionalQuotaVolumeSnapshotsCountUsage] = None
    """Snapshots Count usage"""

    volume_snapshots_size_limit: Optional[LastMessageRegionalQuotaVolumeSnapshotsSizeLimit] = None
    """Snapshots Size, GiB limit"""

    volume_snapshots_size_usage: Optional[LastMessageRegionalQuotaVolumeSnapshotsSizeUsage] = None
    """Snapshots Size, GiB usage"""


class LastMessage(BaseModel):
    """A message data"""

    global_quotas: LastMessageGlobalQuotas
    """Global quota that exceed the threshold"""

    regional_quotas: List[LastMessageRegionalQuota]
    """Regional quota that exceed the threshold"""


class NotificationThreshold(BaseModel):
    client_id: int
    """Client id"""

    last_message: Optional[LastMessage] = None
    """A message data"""

    last_sending: Optional[datetime] = None
    """Time of last successful email sending"""

    threshold: int
    """Quota notification threshold in percentage"""
