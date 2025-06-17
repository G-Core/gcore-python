# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .waap_time_series_attack import WaapTimeSeriesAttack

__all__ = ["IPInfoGetAttackTimeSeriesResponse"]

IPInfoGetAttackTimeSeriesResponse: TypeAlias = List[WaapTimeSeriesAttack]
