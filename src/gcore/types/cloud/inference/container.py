# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel
from ..deploy_status import DeployStatus
from ..container_scale import ContainerScale

__all__ = ["Container"]


class Container(BaseModel):
    address: Optional[str] = None
    """Address of the inference instance"""

    deploy_status: DeployStatus
    """Status of the containers deployment"""

    error_message: Optional[str] = None
    """Error message if the container deployment failed"""

    region_id: int
    """Region name for the container"""

    scale: ContainerScale
    """Scale for the container"""
