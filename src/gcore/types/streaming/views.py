# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["Views", "Data"]


class Data(BaseModel):
    date: str

    type: str

    views: int

    id: Optional[int] = None

    browser: Optional[str] = None

    country: Optional[str] = None

    event: Optional[str] = None

    host: Optional[str] = None

    ip: Optional[str] = None

    os: Optional[str] = None

    platform: Optional[str] = None


class Views(BaseModel):
    data: Optional[List[Data]] = None
