# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ClientProfileTemplate", "Field"]


class Field(BaseModel):
    id: int

    name: str

    default: Optional[str] = None

    description: Optional[str] = None

    field_type: Optional[Literal["int", "bool", "str"]] = None

    required: Optional[bool] = None

    validation_schema: Optional[Dict[str, object]] = None


class ClientProfileTemplate(BaseModel):
    id: int

    created: datetime

    fields: List[Field]

    name: str

    version: str

    base_template: Optional[int] = None

    description: Optional[str] = None

    template_sifter: Optional[str] = None
