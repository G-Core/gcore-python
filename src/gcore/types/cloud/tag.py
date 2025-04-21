# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ..._models import BaseModel

__all__ = ["Tag"]


class Tag(BaseModel):
    key: str
    """
    '#/components/schemas/TagSerializer/properties/key'
    "$.components.schemas.TagSerializer.properties.key"
    """

    read_only: bool
    """
    '#/components/schemas/TagSerializer/properties/read_only'
    "$.components.schemas.TagSerializer.properties.read_only"
    """

    value: str
    """
    '#/components/schemas/TagSerializer/properties/value'
    "$.components.schemas.TagSerializer.properties.value"
    """
