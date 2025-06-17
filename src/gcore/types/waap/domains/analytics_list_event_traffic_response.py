# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..waap_traffic_metrics import WaapTrafficMetrics

__all__ = ["AnalyticsListEventTrafficResponse"]

AnalyticsListEventTrafficResponse: TypeAlias = List[WaapTrafficMetrics]
