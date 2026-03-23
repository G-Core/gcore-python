# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = [
    "NotificationThresholdUpdateParams",
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


class NotificationThresholdUpdateParams(TypedDict, total=False):
    threshold: Required[int]
    """Quota notification threshold in percentage"""

    last_message: Optional[LastMessage]
    """A message data"""

    last_sending: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Time of last successful email sending"""


class LastMessageGlobalQuotasInferenceCPUMillicoreCountLimit(TypedDict, total=False):
    """Inference CPU millicore count limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageGlobalQuotasInferenceCPUMillicoreCountUsage(TypedDict, total=False):
    """Inference CPU millicore count usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageGlobalQuotasInferenceGPUA100CountLimit(TypedDict, total=False):
    """Inference GPU A100 Count limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageGlobalQuotasInferenceGPUA100CountUsage(TypedDict, total=False):
    """Inference GPU A100 Count usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageGlobalQuotasInferenceGPUH100CountLimit(TypedDict, total=False):
    """Inference GPU H100 Count limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageGlobalQuotasInferenceGPUH100CountUsage(TypedDict, total=False):
    """Inference GPU H100 Count usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageGlobalQuotasInferenceGPUL40sCountLimit(TypedDict, total=False):
    """Inference GPU L40s Count limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageGlobalQuotasInferenceGPUL40sCountUsage(TypedDict, total=False):
    """Inference GPU L40s Count usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageGlobalQuotasInferenceInstanceCountLimit(TypedDict, total=False):
    """Inference instance count limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageGlobalQuotasInferenceInstanceCountUsage(TypedDict, total=False):
    """Inference instance count usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageGlobalQuotasKeypairCountLimit(TypedDict, total=False):
    """SSH Keys Count limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageGlobalQuotasKeypairCountUsage(TypedDict, total=False):
    """SSH Keys Count usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageGlobalQuotasProjectCountLimit(TypedDict, total=False):
    """Projects Count limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageGlobalQuotasProjectCountUsage(TypedDict, total=False):
    """Projects Count usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageGlobalQuotas(TypedDict, total=False):
    """Global quota that exceed the threshold"""

    inference_cpu_millicore_count_limit: LastMessageGlobalQuotasInferenceCPUMillicoreCountLimit
    """Inference CPU millicore count limit"""

    inference_cpu_millicore_count_usage: LastMessageGlobalQuotasInferenceCPUMillicoreCountUsage
    """Inference CPU millicore count usage"""

    inference_gpu_a100_count_limit: LastMessageGlobalQuotasInferenceGPUA100CountLimit
    """Inference GPU A100 Count limit"""

    inference_gpu_a100_count_usage: LastMessageGlobalQuotasInferenceGPUA100CountUsage
    """Inference GPU A100 Count usage"""

    inference_gpu_h100_count_limit: LastMessageGlobalQuotasInferenceGPUH100CountLimit
    """Inference GPU H100 Count limit"""

    inference_gpu_h100_count_usage: LastMessageGlobalQuotasInferenceGPUH100CountUsage
    """Inference GPU H100 Count usage"""

    inference_gpu_l40s_count_limit: LastMessageGlobalQuotasInferenceGPUL40sCountLimit
    """Inference GPU L40s Count limit"""

    inference_gpu_l40s_count_usage: LastMessageGlobalQuotasInferenceGPUL40sCountUsage
    """Inference GPU L40s Count usage"""

    inference_instance_count_limit: LastMessageGlobalQuotasInferenceInstanceCountLimit
    """Inference instance count limit"""

    inference_instance_count_usage: LastMessageGlobalQuotasInferenceInstanceCountUsage
    """Inference instance count usage"""

    keypair_count_limit: LastMessageGlobalQuotasKeypairCountLimit
    """SSH Keys Count limit"""

    keypair_count_usage: LastMessageGlobalQuotasKeypairCountUsage
    """SSH Keys Count usage"""

    project_count_limit: LastMessageGlobalQuotasProjectCountLimit
    """Projects Count limit"""

    project_count_usage: LastMessageGlobalQuotasProjectCountUsage
    """Projects Count usage"""


class LastMessageRegionalQuotaBaremetalBasicCountLimit(TypedDict, total=False):
    """Basic bare metal servers count limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaBaremetalBasicCountUsage(TypedDict, total=False):
    """Basic bare metal servers count usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaBaremetalGPUA100CountLimit(TypedDict, total=False):
    """Bare metal A100 GPU server count limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaBaremetalGPUA100CountUsage(TypedDict, total=False):
    """Bare metal A100 GPU server count usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaBaremetalGPUH100CountLimit(TypedDict, total=False):
    """Bare metal H100 GPU server count limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaBaremetalGPUH100CountUsage(TypedDict, total=False):
    """Bare metal H100 GPU server count usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaBaremetalGPUH200CountLimit(TypedDict, total=False):
    """Bare metal H200 GPU server count limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaBaremetalGPUH200CountUsage(TypedDict, total=False):
    """Bare metal H200 GPU server count usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaBaremetalGPUL40sCountLimit(TypedDict, total=False):
    """Bare metal L40S GPU server count limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaBaremetalGPUL40sCountUsage(TypedDict, total=False):
    """Bare metal L40S GPU server count usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaBaremetalHfCountLimit(TypedDict, total=False):
    """High-frequency bare metal servers count limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaBaremetalHfCountUsage(TypedDict, total=False):
    """High-frequency bare metal servers count usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaBaremetalInfrastructureCountLimit(TypedDict, total=False):
    """Infrastructure bare metal servers count limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaBaremetalInfrastructureCountUsage(TypedDict, total=False):
    """Infrastructure bare metal servers count usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaBaremetalNetworkCountLimit(TypedDict, total=False):
    """Bare metal Network Count limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaBaremetalNetworkCountUsage(TypedDict, total=False):
    """Bare metal Network Count usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaBaremetalStorageCountLimit(TypedDict, total=False):
    """Storage bare metal servers count limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaBaremetalStorageCountUsage(TypedDict, total=False):
    """Storage bare metal servers count usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaCaasContainerCountLimit(TypedDict, total=False):
    """Containers count limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaCaasContainerCountUsage(TypedDict, total=False):
    """Containers count usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaCaasCPUCountLimit(TypedDict, total=False):
    """mCPU count for containers limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaCaasCPUCountUsage(TypedDict, total=False):
    """mCPU count for containers usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaCaasGPUCountLimit(TypedDict, total=False):
    """Containers gpu count limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaCaasGPUCountUsage(TypedDict, total=False):
    """Containers gpu count usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaCaasRamSizeLimit(TypedDict, total=False):
    """MiB memory count for containers limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaCaasRamSizeUsage(TypedDict, total=False):
    """MiB memory count for containers usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaClusterCountLimit(TypedDict, total=False):
    """K8s clusters count limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaClusterCountUsage(TypedDict, total=False):
    """K8s clusters count usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaCPUCountLimit(TypedDict, total=False):
    """vCPU Count limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaCPUCountUsage(TypedDict, total=False):
    """vCPU Count usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaDbaasPostgresClusterCountLimit(TypedDict, total=False):
    """DBaaS cluster count limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaDbaasPostgresClusterCountUsage(TypedDict, total=False):
    """DBaaS cluster count usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaExternalIPCountLimit(TypedDict, total=False):
    """External IP Count limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaExternalIPCountUsage(TypedDict, total=False):
    """External IP Count usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaFaasCPUCountLimit(TypedDict, total=False):
    """mCPU count for functions limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaFaasCPUCountUsage(TypedDict, total=False):
    """mCPU count for functions usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaFaasFunctionCountLimit(TypedDict, total=False):
    """Functions count limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaFaasFunctionCountUsage(TypedDict, total=False):
    """Functions count usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaFaasNamespaceCountLimit(TypedDict, total=False):
    """Functions namespace count limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaFaasNamespaceCountUsage(TypedDict, total=False):
    """Functions namespace count usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaFaasRamSizeLimit(TypedDict, total=False):
    """MiB memory count for functions limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaFaasRamSizeUsage(TypedDict, total=False):
    """MiB memory count for functions usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaFirewallCountLimit(TypedDict, total=False):
    """Firewalls Count limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaFirewallCountUsage(TypedDict, total=False):
    """Firewalls Count usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaFloatingCountLimit(TypedDict, total=False):
    """Floating IP Count limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaFloatingCountUsage(TypedDict, total=False):
    """Floating IP Count usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaGPUCountLimit(TypedDict, total=False):
    """GPU Count limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaGPUCountUsage(TypedDict, total=False):
    """GPU Count usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaGPUVirtualA100CountLimit(TypedDict, total=False):
    """Virtual A100 GPU card count limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaGPUVirtualA100CountUsage(TypedDict, total=False):
    """Virtual A100 GPU card count usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaGPUVirtualH100CountLimit(TypedDict, total=False):
    """Virtual H100 GPU card count limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaGPUVirtualH100CountUsage(TypedDict, total=False):
    """Virtual H100 GPU card count usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaGPUVirtualH200CountLimit(TypedDict, total=False):
    """Virtual H200 GPU card count limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaGPUVirtualH200CountUsage(TypedDict, total=False):
    """Virtual H200 GPU card count usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaGPUVirtualL40sCountLimit(TypedDict, total=False):
    """Virtual L40S GPU card count limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaGPUVirtualL40sCountUsage(TypedDict, total=False):
    """Virtual L40S GPU card count usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaImageCountLimit(TypedDict, total=False):
    """Images Count limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaImageCountUsage(TypedDict, total=False):
    """Images Count usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaImageSizeLimit(TypedDict, total=False):
    """Images Size, bytes limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaImageSizeUsage(TypedDict, total=False):
    """Images Size, bytes usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaIpuCountLimit(TypedDict, total=False):
    """IPU Count limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaIpuCountUsage(TypedDict, total=False):
    """IPU Count usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaLaasTopicCountLimit(TypedDict, total=False):
    """LaaS Topics Count limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaLaasTopicCountUsage(TypedDict, total=False):
    """LaaS Topics Count usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaLoadbalancerCountLimit(TypedDict, total=False):
    """Load Balancers Count limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaLoadbalancerCountUsage(TypedDict, total=False):
    """Load Balancers Count usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaNetworkCountLimit(TypedDict, total=False):
    """Networks Count limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaNetworkCountUsage(TypedDict, total=False):
    """Networks Count usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaRamLimit(TypedDict, total=False):
    """RAM Size, MiB limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaRamUsage(TypedDict, total=False):
    """RAM Size, MiB usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaRegistryCountLimit(TypedDict, total=False):
    """Registries count limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaRegistryCountUsage(TypedDict, total=False):
    """Registries count usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaRegistryStorageLimit(TypedDict, total=False):
    """Registries volume usage, GiB limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaRegistryStorageUsage(TypedDict, total=False):
    """Registries volume usage, GiB usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaRouterCountLimit(TypedDict, total=False):
    """Routers Count limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaRouterCountUsage(TypedDict, total=False):
    """Routers Count usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaSecretCountLimit(TypedDict, total=False):
    """Secret Count limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaSecretCountUsage(TypedDict, total=False):
    """Secret Count usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaServergroupCountLimit(TypedDict, total=False):
    """Placement Group Count limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaServergroupCountUsage(TypedDict, total=False):
    """Placement Group Count usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaSfsCountLimit(TypedDict, total=False):
    """Shared file system Count limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaSfsCountUsage(TypedDict, total=False):
    """Shared file system Count usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaSfsSizeLimit(TypedDict, total=False):
    """Shared file system Size, GiB limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaSfsSizeUsage(TypedDict, total=False):
    """Shared file system Size, GiB usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaSharedVmCountLimit(TypedDict, total=False):
    """Basic VMs Count limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaSharedVmCountUsage(TypedDict, total=False):
    """Basic VMs Count usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaSnapshotScheduleCountLimit(TypedDict, total=False):
    """Snapshot Schedules Count limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaSnapshotScheduleCountUsage(TypedDict, total=False):
    """Snapshot Schedules Count usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaSubnetCountLimit(TypedDict, total=False):
    """Subnets Count limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaSubnetCountUsage(TypedDict, total=False):
    """Subnets Count usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaVmCountLimit(TypedDict, total=False):
    """Instances Dedicated Count limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaVmCountUsage(TypedDict, total=False):
    """Instances Dedicated Count usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaVolumeCountLimit(TypedDict, total=False):
    """Volumes Count limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaVolumeCountUsage(TypedDict, total=False):
    """Volumes Count usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaVolumeSizeLimit(TypedDict, total=False):
    """Volumes Size, GiB limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaVolumeSizeUsage(TypedDict, total=False):
    """Volumes Size, GiB usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaVolumeSnapshotsCountLimit(TypedDict, total=False):
    """Snapshots Count limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaVolumeSnapshotsCountUsage(TypedDict, total=False):
    """Snapshots Count usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaVolumeSnapshotsSizeLimit(TypedDict, total=False):
    """Snapshots Size, GiB limit"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuotaVolumeSnapshotsSizeUsage(TypedDict, total=False):
    """Snapshots Size, GiB usage"""

    limit: Required[int]
    """Сurrent quota limit"""

    usage: Required[int]
    """Сurrent amount of resource used"""


class LastMessageRegionalQuota(TypedDict, total=False):
    region_id: Required[int]
    """Region id"""

    region_name: Required[str]
    """Region name"""

    baremetal_basic_count_limit: LastMessageRegionalQuotaBaremetalBasicCountLimit
    """Basic bare metal servers count limit"""

    baremetal_basic_count_usage: LastMessageRegionalQuotaBaremetalBasicCountUsage
    """Basic bare metal servers count usage"""

    baremetal_gpu_a100_count_limit: LastMessageRegionalQuotaBaremetalGPUA100CountLimit
    """Bare metal A100 GPU server count limit"""

    baremetal_gpu_a100_count_usage: LastMessageRegionalQuotaBaremetalGPUA100CountUsage
    """Bare metal A100 GPU server count usage"""

    baremetal_gpu_h100_count_limit: LastMessageRegionalQuotaBaremetalGPUH100CountLimit
    """Bare metal H100 GPU server count limit"""

    baremetal_gpu_h100_count_usage: LastMessageRegionalQuotaBaremetalGPUH100CountUsage
    """Bare metal H100 GPU server count usage"""

    baremetal_gpu_h200_count_limit: LastMessageRegionalQuotaBaremetalGPUH200CountLimit
    """Bare metal H200 GPU server count limit"""

    baremetal_gpu_h200_count_usage: LastMessageRegionalQuotaBaremetalGPUH200CountUsage
    """Bare metal H200 GPU server count usage"""

    baremetal_gpu_l40s_count_limit: LastMessageRegionalQuotaBaremetalGPUL40sCountLimit
    """Bare metal L40S GPU server count limit"""

    baremetal_gpu_l40s_count_usage: LastMessageRegionalQuotaBaremetalGPUL40sCountUsage
    """Bare metal L40S GPU server count usage"""

    baremetal_hf_count_limit: LastMessageRegionalQuotaBaremetalHfCountLimit
    """High-frequency bare metal servers count limit"""

    baremetal_hf_count_usage: LastMessageRegionalQuotaBaremetalHfCountUsage
    """High-frequency bare metal servers count usage"""

    baremetal_infrastructure_count_limit: LastMessageRegionalQuotaBaremetalInfrastructureCountLimit
    """Infrastructure bare metal servers count limit"""

    baremetal_infrastructure_count_usage: LastMessageRegionalQuotaBaremetalInfrastructureCountUsage
    """Infrastructure bare metal servers count usage"""

    baremetal_network_count_limit: LastMessageRegionalQuotaBaremetalNetworkCountLimit
    """Bare metal Network Count limit"""

    baremetal_network_count_usage: LastMessageRegionalQuotaBaremetalNetworkCountUsage
    """Bare metal Network Count usage"""

    baremetal_storage_count_limit: LastMessageRegionalQuotaBaremetalStorageCountLimit
    """Storage bare metal servers count limit"""

    baremetal_storage_count_usage: LastMessageRegionalQuotaBaremetalStorageCountUsage
    """Storage bare metal servers count usage"""

    caas_container_count_limit: LastMessageRegionalQuotaCaasContainerCountLimit
    """Containers count limit"""

    caas_container_count_usage: LastMessageRegionalQuotaCaasContainerCountUsage
    """Containers count usage"""

    caas_cpu_count_limit: LastMessageRegionalQuotaCaasCPUCountLimit
    """mCPU count for containers limit"""

    caas_cpu_count_usage: LastMessageRegionalQuotaCaasCPUCountUsage
    """mCPU count for containers usage"""

    caas_gpu_count_limit: LastMessageRegionalQuotaCaasGPUCountLimit
    """Containers gpu count limit"""

    caas_gpu_count_usage: LastMessageRegionalQuotaCaasGPUCountUsage
    """Containers gpu count usage"""

    caas_ram_size_limit: LastMessageRegionalQuotaCaasRamSizeLimit
    """MiB memory count for containers limit"""

    caas_ram_size_usage: LastMessageRegionalQuotaCaasRamSizeUsage
    """MiB memory count for containers usage"""

    cluster_count_limit: LastMessageRegionalQuotaClusterCountLimit
    """K8s clusters count limit"""

    cluster_count_usage: LastMessageRegionalQuotaClusterCountUsage
    """K8s clusters count usage"""

    cpu_count_limit: LastMessageRegionalQuotaCPUCountLimit
    """vCPU Count limit"""

    cpu_count_usage: LastMessageRegionalQuotaCPUCountUsage
    """vCPU Count usage"""

    dbaas_postgres_cluster_count_limit: LastMessageRegionalQuotaDbaasPostgresClusterCountLimit
    """DBaaS cluster count limit"""

    dbaas_postgres_cluster_count_usage: LastMessageRegionalQuotaDbaasPostgresClusterCountUsage
    """DBaaS cluster count usage"""

    external_ip_count_limit: LastMessageRegionalQuotaExternalIPCountLimit
    """External IP Count limit"""

    external_ip_count_usage: LastMessageRegionalQuotaExternalIPCountUsage
    """External IP Count usage"""

    faas_cpu_count_limit: LastMessageRegionalQuotaFaasCPUCountLimit
    """mCPU count for functions limit"""

    faas_cpu_count_usage: LastMessageRegionalQuotaFaasCPUCountUsage
    """mCPU count for functions usage"""

    faas_function_count_limit: LastMessageRegionalQuotaFaasFunctionCountLimit
    """Functions count limit"""

    faas_function_count_usage: LastMessageRegionalQuotaFaasFunctionCountUsage
    """Functions count usage"""

    faas_namespace_count_limit: LastMessageRegionalQuotaFaasNamespaceCountLimit
    """Functions namespace count limit"""

    faas_namespace_count_usage: LastMessageRegionalQuotaFaasNamespaceCountUsage
    """Functions namespace count usage"""

    faas_ram_size_limit: LastMessageRegionalQuotaFaasRamSizeLimit
    """MiB memory count for functions limit"""

    faas_ram_size_usage: LastMessageRegionalQuotaFaasRamSizeUsage
    """MiB memory count for functions usage"""

    firewall_count_limit: LastMessageRegionalQuotaFirewallCountLimit
    """Firewalls Count limit"""

    firewall_count_usage: LastMessageRegionalQuotaFirewallCountUsage
    """Firewalls Count usage"""

    floating_count_limit: LastMessageRegionalQuotaFloatingCountLimit
    """Floating IP Count limit"""

    floating_count_usage: LastMessageRegionalQuotaFloatingCountUsage
    """Floating IP Count usage"""

    gpu_count_limit: LastMessageRegionalQuotaGPUCountLimit
    """GPU Count limit"""

    gpu_count_usage: LastMessageRegionalQuotaGPUCountUsage
    """GPU Count usage"""

    gpu_virtual_a100_count_limit: LastMessageRegionalQuotaGPUVirtualA100CountLimit
    """Virtual A100 GPU card count limit"""

    gpu_virtual_a100_count_usage: LastMessageRegionalQuotaGPUVirtualA100CountUsage
    """Virtual A100 GPU card count usage"""

    gpu_virtual_h100_count_limit: LastMessageRegionalQuotaGPUVirtualH100CountLimit
    """Virtual H100 GPU card count limit"""

    gpu_virtual_h100_count_usage: LastMessageRegionalQuotaGPUVirtualH100CountUsage
    """Virtual H100 GPU card count usage"""

    gpu_virtual_h200_count_limit: LastMessageRegionalQuotaGPUVirtualH200CountLimit
    """Virtual H200 GPU card count limit"""

    gpu_virtual_h200_count_usage: LastMessageRegionalQuotaGPUVirtualH200CountUsage
    """Virtual H200 GPU card count usage"""

    gpu_virtual_l40s_count_limit: LastMessageRegionalQuotaGPUVirtualL40sCountLimit
    """Virtual L40S GPU card count limit"""

    gpu_virtual_l40s_count_usage: LastMessageRegionalQuotaGPUVirtualL40sCountUsage
    """Virtual L40S GPU card count usage"""

    image_count_limit: LastMessageRegionalQuotaImageCountLimit
    """Images Count limit"""

    image_count_usage: LastMessageRegionalQuotaImageCountUsage
    """Images Count usage"""

    image_size_limit: LastMessageRegionalQuotaImageSizeLimit
    """Images Size, bytes limit"""

    image_size_usage: LastMessageRegionalQuotaImageSizeUsage
    """Images Size, bytes usage"""

    ipu_count_limit: LastMessageRegionalQuotaIpuCountLimit
    """IPU Count limit"""

    ipu_count_usage: LastMessageRegionalQuotaIpuCountUsage
    """IPU Count usage"""

    laas_topic_count_limit: LastMessageRegionalQuotaLaasTopicCountLimit
    """LaaS Topics Count limit"""

    laas_topic_count_usage: LastMessageRegionalQuotaLaasTopicCountUsage
    """LaaS Topics Count usage"""

    loadbalancer_count_limit: LastMessageRegionalQuotaLoadbalancerCountLimit
    """Load Balancers Count limit"""

    loadbalancer_count_usage: LastMessageRegionalQuotaLoadbalancerCountUsage
    """Load Balancers Count usage"""

    network_count_limit: LastMessageRegionalQuotaNetworkCountLimit
    """Networks Count limit"""

    network_count_usage: LastMessageRegionalQuotaNetworkCountUsage
    """Networks Count usage"""

    ram_limit: LastMessageRegionalQuotaRamLimit
    """RAM Size, MiB limit"""

    ram_usage: LastMessageRegionalQuotaRamUsage
    """RAM Size, MiB usage"""

    registry_count_limit: LastMessageRegionalQuotaRegistryCountLimit
    """Registries count limit"""

    registry_count_usage: LastMessageRegionalQuotaRegistryCountUsage
    """Registries count usage"""

    registry_storage_limit: LastMessageRegionalQuotaRegistryStorageLimit
    """Registries volume usage, GiB limit"""

    registry_storage_usage: LastMessageRegionalQuotaRegistryStorageUsage
    """Registries volume usage, GiB usage"""

    router_count_limit: LastMessageRegionalQuotaRouterCountLimit
    """Routers Count limit"""

    router_count_usage: LastMessageRegionalQuotaRouterCountUsage
    """Routers Count usage"""

    secret_count_limit: LastMessageRegionalQuotaSecretCountLimit
    """Secret Count limit"""

    secret_count_usage: LastMessageRegionalQuotaSecretCountUsage
    """Secret Count usage"""

    servergroup_count_limit: LastMessageRegionalQuotaServergroupCountLimit
    """Placement Group Count limit"""

    servergroup_count_usage: LastMessageRegionalQuotaServergroupCountUsage
    """Placement Group Count usage"""

    sfs_count_limit: LastMessageRegionalQuotaSfsCountLimit
    """Shared file system Count limit"""

    sfs_count_usage: LastMessageRegionalQuotaSfsCountUsage
    """Shared file system Count usage"""

    sfs_size_limit: LastMessageRegionalQuotaSfsSizeLimit
    """Shared file system Size, GiB limit"""

    sfs_size_usage: LastMessageRegionalQuotaSfsSizeUsage
    """Shared file system Size, GiB usage"""

    shared_vm_count_limit: LastMessageRegionalQuotaSharedVmCountLimit
    """Basic VMs Count limit"""

    shared_vm_count_usage: LastMessageRegionalQuotaSharedVmCountUsage
    """Basic VMs Count usage"""

    snapshot_schedule_count_limit: LastMessageRegionalQuotaSnapshotScheduleCountLimit
    """Snapshot Schedules Count limit"""

    snapshot_schedule_count_usage: LastMessageRegionalQuotaSnapshotScheduleCountUsage
    """Snapshot Schedules Count usage"""

    subnet_count_limit: LastMessageRegionalQuotaSubnetCountLimit
    """Subnets Count limit"""

    subnet_count_usage: LastMessageRegionalQuotaSubnetCountUsage
    """Subnets Count usage"""

    vm_count_limit: LastMessageRegionalQuotaVmCountLimit
    """Instances Dedicated Count limit"""

    vm_count_usage: LastMessageRegionalQuotaVmCountUsage
    """Instances Dedicated Count usage"""

    volume_count_limit: LastMessageRegionalQuotaVolumeCountLimit
    """Volumes Count limit"""

    volume_count_usage: LastMessageRegionalQuotaVolumeCountUsage
    """Volumes Count usage"""

    volume_size_limit: LastMessageRegionalQuotaVolumeSizeLimit
    """Volumes Size, GiB limit"""

    volume_size_usage: LastMessageRegionalQuotaVolumeSizeUsage
    """Volumes Size, GiB usage"""

    volume_snapshots_count_limit: LastMessageRegionalQuotaVolumeSnapshotsCountLimit
    """Snapshots Count limit"""

    volume_snapshots_count_usage: LastMessageRegionalQuotaVolumeSnapshotsCountUsage
    """Snapshots Count usage"""

    volume_snapshots_size_limit: LastMessageRegionalQuotaVolumeSnapshotsSizeLimit
    """Snapshots Size, GiB limit"""

    volume_snapshots_size_usage: LastMessageRegionalQuotaVolumeSnapshotsSizeUsage
    """Snapshots Size, GiB usage"""


class LastMessage(TypedDict, total=False):
    """A message data"""

    global_quotas: Required[LastMessageGlobalQuotas]
    """Global quota that exceed the threshold"""

    regional_quotas: Required[Iterable[LastMessageRegionalQuota]]
    """Regional quota that exceed the threshold"""
