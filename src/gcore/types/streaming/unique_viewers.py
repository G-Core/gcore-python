# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["UniqueViewers", "Data"]


class Data(BaseModel):
    date: str

    unique_ips: int

    id: Optional[int] = None

    browser: Optional[str] = None

    country: Optional[str] = None

    event: Optional[str] = None

    host: Optional[str] = None

    ip: Optional[str] = None

    os: Optional[str] = None

    platform: Optional[str] = None

    type: Optional[str] = None


class UniqueViewers(BaseModel):
    data: Optional[List[Data]] = None
