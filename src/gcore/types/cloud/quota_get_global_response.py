# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["QuotaGetGlobalResponse"]


class QuotaGetGlobalResponse(BaseModel):
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
