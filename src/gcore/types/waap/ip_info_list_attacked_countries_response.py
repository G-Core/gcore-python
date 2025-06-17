# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .waap_ip_country_attack import WaapIPCountryAttack

__all__ = ["IPInfoListAttackedCountriesResponse"]

IPInfoListAttackedCountriesResponse: TypeAlias = List[WaapIPCountryAttack]
