# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ...._models import BaseModel

__all__ = ["InferenceLog"]


class InferenceLog(BaseModel):
    message: str
    """Log message."""

    pod: str
    """Pod name."""

    region_id: int
    """Region ID where the container is deployed."""

    time: datetime
    """Log message timestamp in ISO 8601 format."""
