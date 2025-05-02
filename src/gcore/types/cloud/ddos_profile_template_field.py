# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["DDOSProfileTemplateField"]


class DDOSProfileTemplateField(BaseModel):
    id: int

    name: str

    default: Optional[str] = None

    description: Optional[str] = None

    field_type: Optional[str] = None

    required: Optional[bool] = None

    validation_schema: Optional[object] = None
