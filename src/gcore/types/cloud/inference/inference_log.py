# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ...._models import BaseModel

__all__ = ["InferenceLog"]


class InferenceLog(BaseModel):
    message: str
    """
    '#/components/schemas/InferenceInstanceLogSerializerV3/properties/message'
    "$.components.schemas.InferenceInstanceLogSerializerV3.properties.message"
    """

    pod: str
    """
    '#/components/schemas/InferenceInstanceLogSerializerV3/properties/pod'
    "$.components.schemas.InferenceInstanceLogSerializerV3.properties.pod"
    """

    region_id: int
    """
    '#/components/schemas/InferenceInstanceLogSerializerV3/properties/region_id'
    "$.components.schemas.InferenceInstanceLogSerializerV3.properties.region_id"
    """

    time: datetime
    """
    '#/components/schemas/InferenceInstanceLogSerializerV3/properties/time'
    "$.components.schemas.InferenceInstanceLogSerializerV3.properties.time"
    """
