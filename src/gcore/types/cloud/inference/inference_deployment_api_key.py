# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["InferenceDeploymentAPIKey"]


class InferenceDeploymentAPIKey(BaseModel):
    secret: str
    """API key secret"""

    status: Literal["PENDING", "READY"]
    """API key status"""
