# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["DeployStatus"]


class DeployStatus(BaseModel):
    ready: int
    """
    '#/components/schemas/DeployStatusSerializer/properties/ready'
    "$.components.schemas.DeployStatusSerializer.properties.ready"
    """

    total: int
    """
    '#/components/schemas/DeployStatusSerializer/properties/total'
    "$.components.schemas.DeployStatusSerializer.properties.total"
    """
