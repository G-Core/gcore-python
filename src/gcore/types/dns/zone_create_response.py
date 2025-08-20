# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ZoneCreateResponse"]


class ZoneCreateResponse(BaseModel):
    id: Optional[int] = None

    warnings: Optional[List[str]] = None
