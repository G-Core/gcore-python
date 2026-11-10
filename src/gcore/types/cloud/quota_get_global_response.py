# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["QuotaGetGlobalResponse"]


class QuotaGetGlobalResponse(BaseModel):
    inference_cpu_millicore_count_limit: int
    """Inference CPU millicore count limit"""

    inference_cpu_millicore_count_usage: int
    """Inference CPU millicore count usage"""

    inference_gpu_a100_count_limit: int
    """Inference GPU A100 Count limit"""

    inference_gpu_a100_count_usage: int
    """Inference GPU A100 Count usage"""

    inference_gpu_h100_count_limit: int
    """Inference GPU H100 Count limit"""

    inference_gpu_h100_count_usage: int
    """Inference GPU H100 Count usage"""

    inference_gpu_l40s_count_limit: int
    """Inference GPU L40s Count limit"""

    inference_gpu_l40s_count_usage: int
    """Inference GPU L40s Count usage"""

    inference_instance_count_limit: int
    """Inference instance count limit"""

    inference_instance_count_usage: int
    """Inference instance count usage"""

    inference_public_model_api_key_count_limit: int
    """Public model API keys count limit"""

    inference_public_model_api_key_count_usage: int
    """Public model API keys count usage"""

    keypair_count_limit: int
    """SSH Keys Count limit"""

    keypair_count_usage: int
    """SSH Keys Count usage"""

    project_count_limit: int
    """Projects Count limit"""

    project_count_usage: int
    """Projects Count usage"""
