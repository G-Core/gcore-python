# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["DDOSProfileTemplateField"]


class DDOSProfileTemplateField(BaseModel):
    id: int
    """
    '#/components/schemas/ClientProfileTemplateFieldSerializer/properties/id'
    "$.components.schemas.ClientProfileTemplateFieldSerializer.properties.id"
    """

    name: str
    """
    '#/components/schemas/ClientProfileTemplateFieldSerializer/properties/name'
    "$.components.schemas.ClientProfileTemplateFieldSerializer.properties.name"
    """

    default: Optional[str] = None
    """
    '#/components/schemas/ClientProfileTemplateFieldSerializer/properties/default/anyOf/0'
    "$.components.schemas.ClientProfileTemplateFieldSerializer.properties['default'].anyOf[0]"
    """

    description: Optional[str] = None
    """
    '#/components/schemas/ClientProfileTemplateFieldSerializer/properties/description/anyOf/0'
    "$.components.schemas.ClientProfileTemplateFieldSerializer.properties.description.anyOf[0]"
    """

    field_type: Optional[str] = None
    """
    '#/components/schemas/ClientProfileTemplateFieldSerializer/properties/field_type/anyOf/0'
    "$.components.schemas.ClientProfileTemplateFieldSerializer.properties.field_type.anyOf[0]"
    """

    required: Optional[bool] = None
    """
    '#/components/schemas/ClientProfileTemplateFieldSerializer/properties/required/anyOf/0'
    "$.components.schemas.ClientProfileTemplateFieldSerializer.properties.required.anyOf[0]"
    """

    validation_schema: Optional[object] = None
    """
    '#/components/schemas/ClientProfileTemplateFieldSerializer/properties/validation_schema'
    "$.components.schemas.ClientProfileTemplateFieldSerializer.properties.validation_schema"
    """
