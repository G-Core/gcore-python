# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["LogsUploaderValidation"]


class LogsUploaderValidation(BaseModel):
    code: Optional[int] = None
    """Error code indicating the type of validation error."""

    details: Optional[str] = None
    """Error message if the validation failed."""

    status: Optional[Literal["in_progress", "successful", "failed"]] = None
    """Status of the validation."""

    updated: Optional[datetime] = None
    """Time when the validation status was updated."""
