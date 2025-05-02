# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["InstanceIsolation"]


class InstanceIsolation(BaseModel):
    reason: Optional[str] = None
    """
    '#/components/schemas/IsolationSerializer/properties/reason/anyOf/0'
    "$.components.schemas.IsolationSerializer.properties.reason.anyOf[0]"
    """
