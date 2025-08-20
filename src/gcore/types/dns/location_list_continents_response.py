# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict
from typing_extensions import TypeAlias

from .dns_location_translations import DNSLocationTranslations

__all__ = ["LocationListContinentsResponse"]

LocationListContinentsResponse: TypeAlias = Dict[str, DNSLocationTranslations]
