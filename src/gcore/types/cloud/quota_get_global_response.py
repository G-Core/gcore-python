# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["QuotaGetGlobalResponse"]


class QuotaGetGlobalResponse(BaseModel):
    inference_cpu_millicore_count_limit: Optional[int] = None
    """Inference CPU millicore count limit"""

    inference_cpu_millicore_count_usage: Optional[int] = None
    """Inference CPU millicore count usage"""

    inference_gpu_a100_count_limit: Optional[int] = None
    """Inference GPU A100 Count limit"""

    inference_gpu_a100_count_usage: Optional[int] = None
    """Inference GPU A100 Count usage"""

    inference_gpu_h100_count_limit: Optional[int] = None
    """Inference GPU H100 Count limit"""

    inference_gpu_h100_count_usage: Optional[int] = None
    """Inference GPU H100 Count usage"""

    inference_gpu_l40s_count_limit: Optional[int] = None
    """Inference GPU L40s Count limit"""

    inference_gpu_l40s_count_usage: Optional[int] = None
    """Inference GPU L40s Count usage"""

    inference_instance_count_limit: Optional[int] = None
    """Inference instance count limit"""

    inference_instance_count_usage: Optional[int] = None
    """Inference instance count usage"""

    keypair_count_limit: Optional[int] = None
    """SSH Keys Count limit"""

    keypair_count_usage: Optional[int] = None
    """SSH Keys Count usage"""

    project_count_limit: Optional[int] = None
    """Projects Count limit"""

    project_count_usage: Optional[int] = None
    """Projects Count usage"""
