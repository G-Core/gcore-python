# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import TypedDict

__all__ = ["MetricListParams"]


class MetricListParams(TypedDict, total=False):
    client_ids: Iterable[int]
    """
    Admin and technical user can specify `client_id` to get metrics for particular
    client. Ignored for client
    """

    zone_names: List[str]
    """
    Admin and technical user can specify `monitor_id` to get metrics for particular
    zone. Ignored for client
    """
