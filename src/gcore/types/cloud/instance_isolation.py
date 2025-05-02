# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["InstanceIsolation"]


class InstanceIsolation(BaseModel):
    reason: Optional[str] = None
    """The reason of instance isolation if it is isolated from external internet."""
