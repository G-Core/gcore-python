# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ..._models import BaseModel

__all__ = ["DDOSProfileStatus"]


class DDOSProfileStatus(BaseModel):
    error_description: str
    """
    '#/components/schemas/DdosProfileStatusSerializer/properties/error_description'
    "$.components.schemas.DdosProfileStatusSerializer.properties.error_description"
    """

    status: str
    """
    '#/components/schemas/DdosProfileStatusSerializer/properties/status'
    "$.components.schemas.DdosProfileStatusSerializer.properties.status"
    """
