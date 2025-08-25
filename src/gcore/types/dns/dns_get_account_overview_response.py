# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DNSGetAccountOverviewResponse", "Client", "Settings"]


class Client(BaseModel):
    client_id: Optional[int] = None

    enabled: Optional[bool] = None

    reseller: Optional[int] = None

    status: Optional[str] = None

    tariff_id: Optional[int] = None

    tariff_name: Optional[str] = None
    """TariffName"""


class Settings(BaseModel):
    contact: Optional[str] = None

    name_server_1: Optional[str] = None

    name_server_2: Optional[str] = None


class DNSGetAccountOverviewResponse(BaseModel):
    client: Optional[Client] = FieldInfo(alias="Client", default=None)
    """Client"""

    settings: Optional[Settings] = None
