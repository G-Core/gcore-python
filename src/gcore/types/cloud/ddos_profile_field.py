# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["DDOSProfileField"]


class DDOSProfileField(BaseModel):
    id: int
    """Unique identifier for the DDoS protection field"""

    base_field: Optional[int] = None
    """ID of DDoS profile field"""

    default: Optional[str] = None
    """Predefined default value for the field if not specified"""

    description: Optional[str] = None
    """Detailed description explaining the field's purpose and usage guidelines"""

    field_name: Optional[str] = None
    """Name of DDoS profile field"""

    field_type: Optional[str] = None
    """Data type classification of the field (e.g., string, integer, array)"""

    field_value: object
    """Complex value. Only one of 'value' or '`field_value`' must be specified."""

    name: str
    """Human-readable name of the protection field"""

    required: Optional[bool] = None
    """
    Indicates whether this field must be provided when creating a protection profile
    """

    validation_schema: object
    """JSON schema defining validation rules and constraints for the field value"""

    value: Optional[str] = None
    """Basic type value. Only one of 'value' or '`field_value`' must be specified."""
