# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ContainerScaleTriggerSqs"]


class ContainerScaleTriggerSqs(BaseModel):
    activation_queue_length: int
    """
    '#/components/schemas/ContainerScaleTriggersSqsOutSerializer/properties/activation_queue_length'
    "$.components.schemas.ContainerScaleTriggersSqsOutSerializer.properties.activation_queue_length"
    """

    aws_endpoint: Optional[str] = None
    """
    '#/components/schemas/ContainerScaleTriggersSqsOutSerializer/properties/aws_endpoint/anyOf/0'
    "$.components.schemas.ContainerScaleTriggersSqsOutSerializer.properties.aws_endpoint.anyOf[0]"
    """

    aws_region: str
    """
    '#/components/schemas/ContainerScaleTriggersSqsOutSerializer/properties/aws_region'
    "$.components.schemas.ContainerScaleTriggersSqsOutSerializer.properties.aws_region"
    """

    queue_length: int
    """
    '#/components/schemas/ContainerScaleTriggersSqsOutSerializer/properties/queue_length'
    "$.components.schemas.ContainerScaleTriggersSqsOutSerializer.properties.queue_length"
    """

    queue_url: str
    """
    '#/components/schemas/ContainerScaleTriggersSqsOutSerializer/properties/queue_url'
    "$.components.schemas.ContainerScaleTriggersSqsOutSerializer.properties.queue_url"
    """

    scale_on_delayed: bool
    """
    '#/components/schemas/ContainerScaleTriggersSqsOutSerializer/properties/scale_on_delayed'
    "$.components.schemas.ContainerScaleTriggersSqsOutSerializer.properties.scale_on_delayed"
    """

    scale_on_flight: bool
    """
    '#/components/schemas/ContainerScaleTriggersSqsOutSerializer/properties/scale_on_flight'
    "$.components.schemas.ContainerScaleTriggersSqsOutSerializer.properties.scale_on_flight"
    """

    secret_name: str
    """
    '#/components/schemas/ContainerScaleTriggersSqsOutSerializer/properties/secret_name'
    "$.components.schemas.ContainerScaleTriggersSqsOutSerializer.properties.secret_name"
    """
