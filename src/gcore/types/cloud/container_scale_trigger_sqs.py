# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ContainerScaleTriggerSqs"]


class ContainerScaleTriggerSqs(BaseModel):
    activation_queue_length: int
    """Number of messages for activation"""

    aws_endpoint: Optional[str] = None
    """Custom AWS endpoint"""

    aws_region: str
    """AWS region"""

    queue_length: int
    """Number of messages for one replica"""

    queue_url: str
    """SQS queue URL"""

    scale_on_delayed: bool
    """Scale on delayed messages"""

    scale_on_flight: bool
    """Scale on in-flight messages"""

    secret_name: str
    """Auth secret name"""
