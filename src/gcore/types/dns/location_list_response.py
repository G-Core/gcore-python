# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel
from .dns_location_translations import DNSLocationTranslations

__all__ = ["LocationListResponse"]


class LocationListResponse(BaseModel):
    continents: Optional[Dict[str, DNSLocationTranslations]] = None

    countries: Optional[Dict[str, DNSLocationTranslations]] = None

    regions: Optional[Dict[str, DNSLocationTranslations]] = None
