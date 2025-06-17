# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["ScanResultGetResponse"]


class ScanResultGetResponse(BaseModel):
    id: str
    """The scan ID"""

    end_time: Optional[datetime] = None
    """The date and time the scan ended"""

    message: str
    """The message associated with the scan"""

    start_time: datetime
    """The date and time the scan started"""

    status: Literal["SUCCESS", "FAILURE", "IN_PROGRESS"]
    """The different statuses a task result can have"""

    type: Literal["TRAFFIC_SCAN", "API_DESCRIPTION_FILE_SCAN"]
    """The different types of scans that can be performed"""
