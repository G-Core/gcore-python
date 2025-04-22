# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["DDOSProfileField"]


class DDOSProfileField(BaseModel):
    id: int
    """
    '#/components/schemas/ClientProfileFieldSerializer/properties/id'
    "$.components.schemas.ClientProfileFieldSerializer.properties.id"
    """

    default: object
    """
    '#/components/schemas/ClientProfileFieldSerializer/properties/default'
    "$.components.schemas.ClientProfileFieldSerializer.properties['default']"
    """

    description: str
    """
    '#/components/schemas/ClientProfileFieldSerializer/properties/description'
    "$.components.schemas.ClientProfileFieldSerializer.properties.description"
    """

    field_value: object
    """
    '#/components/schemas/ClientProfileFieldSerializer/properties/field_value'
    "$.components.schemas.ClientProfileFieldSerializer.properties.field_value"
    """

    name: str
    """
    '#/components/schemas/ClientProfileFieldSerializer/properties/name'
    "$.components.schemas.ClientProfileFieldSerializer.properties.name"
    """

    base_field: Optional[int] = None
    """
    '#/components/schemas/ClientProfileFieldSerializer/properties/base_field/anyOf/0'
    "$.components.schemas.ClientProfileFieldSerializer.properties.base_field.anyOf[0]"
    """

    field_name: Optional[str] = None
    """
    '#/components/schemas/ClientProfileFieldSerializer/properties/field_name/anyOf/0'
    "$.components.schemas.ClientProfileFieldSerializer.properties.field_name.anyOf[0]"
    """

    field_type: Optional[str] = None
    """
    '#/components/schemas/ClientProfileFieldSerializer/properties/field_type/anyOf/0'
    "$.components.schemas.ClientProfileFieldSerializer.properties.field_type.anyOf[0]"
    """

    required: Optional[bool] = None
    """
    '#/components/schemas/ClientProfileFieldSerializer/properties/required/anyOf/0'
    "$.components.schemas.ClientProfileFieldSerializer.properties.required.anyOf[0]"
    """

    validation_schema: Optional[object] = None
    """
    '#/components/schemas/ClientProfileFieldSerializer/properties/validation_schema'
    "$.components.schemas.ClientProfileFieldSerializer.properties.validation_schema"
    """

    value: Optional[str] = None
    """
    '#/components/schemas/ClientProfileFieldSerializer/properties/value/anyOf/0'
    "$.components.schemas.ClientProfileFieldSerializer.properties.value.anyOf[0]"
    """
