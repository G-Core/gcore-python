# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DNSGetAccountOverviewResponse", "Info"]


class Info(BaseModel):
    contact: Optional[str] = None

    name_server_1: Optional[str] = None

    name_server_2: Optional[str] = None


class DNSGetAccountOverviewResponse(BaseModel):
    info: Optional[Info] = FieldInfo(alias="Info", default=None)
