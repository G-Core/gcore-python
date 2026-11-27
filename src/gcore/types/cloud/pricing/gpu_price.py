# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel
from .gpu_currency import GPUCurrency
from .gpu_price_detail import GPUPriceDetail
from .gpu_deployment_type import GPUDeploymentType

__all__ = ["GPUPrice"]


class GPUPrice(BaseModel):
    currency: GPUCurrency
    """ISO 4217 currency code."""

    deployment_type: GPUDeploymentType
    """Baremetal or virtual."""

    gpu_count: int
    """Number of GPU cards this price covers."""

    gpu_model: str
    """GPU model."""

    price_per_gpu_hour: str
    """On-demand price per GPU per hour."""

    price_per_hour: str
    """On-demand price per node/instance per hour."""

    pricing_detail: GPUPriceDetail
    """Pricing-specific detail."""

    region_name: str
    """Region this price applies to."""
