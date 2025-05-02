# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .laas_index_retention_policy import LaasIndexRetentionPolicy

__all__ = ["Logging"]


class Logging(BaseModel):
    destination_region_id: Optional[int] = None
    """ID of the region in which the logs will be stored"""

    enabled: bool
    """Indicates if log streaming is enabled or disabled"""

    topic_name: Optional[str] = None
    """The topic name to stream logs to"""

    retention_policy: Optional[LaasIndexRetentionPolicy] = None
    """Logs retention policy"""
