# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .laas_index_retention_policy import LaasIndexRetentionPolicy

__all__ = ["Logging"]


class Logging(BaseModel):
    destination_region_id: Optional[int] = None
    """
    '#/components/schemas/LoggingOutSerializer/properties/destination_region_id/anyOf/0'
    "$.components.schemas.LoggingOutSerializer.properties.destination_region_id.anyOf[0]"
    """

    enabled: bool
    """
    '#/components/schemas/LoggingOutSerializer/properties/enabled'
    "$.components.schemas.LoggingOutSerializer.properties.enabled"
    """

    topic_name: Optional[str] = None
    """
    '#/components/schemas/LoggingOutSerializer/properties/topic_name/anyOf/0'
    "$.components.schemas.LoggingOutSerializer.properties.topic_name.anyOf[0]"
    """

    retention_policy: Optional[LaasIndexRetentionPolicy] = None
    """
    '#/components/schemas/LoggingOutSerializer/properties/retention_policy/anyOf/0'
    "$.components.schemas.LoggingOutSerializer.properties.retention_policy.anyOf[0]"
    """
