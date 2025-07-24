# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["BroadcastSpectatorsCount"]


class BroadcastSpectatorsCount(BaseModel):
    spectators_count: Optional[int] = None
    """Number of spectators at the moment"""
