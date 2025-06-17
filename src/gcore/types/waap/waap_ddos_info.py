# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["WaapDDOSInfo"]


class WaapDDOSInfo(BaseModel):
    count: int
    """The number of requests made"""

    identity: str
    """The value for the grouped by type"""

    type: Literal["URL", "IP", "User-Agent"]
