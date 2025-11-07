# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel
from .client_profile_template import ClientProfileTemplate

__all__ = ["ClientProfile", "Field", "Options"]


class Field(BaseModel):
    id: int

    base_field: int

    default: str

    description: str

    field_type: str

    name: str

    required: bool

    validation_schema: Dict[str, object]

    field_value: Optional[object] = None


class Options(BaseModel):
    active: bool

    bgp: bool

    price: str


class ClientProfile(BaseModel):
    id: int

    fields: List[Field]

    options: Options

    plan: str

    profile_template: ClientProfileTemplate

    protocols: List[Dict[str, object]]

    site: str
    """Region where the protection profiles will be deployed"""

    status: Dict[str, object]

    ip_address: Optional[str] = None
