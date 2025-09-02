# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["MetricListParams"]


class MetricListParams(TypedDict, total=False):
    client_ids: Iterable[int]
    """
    Admin and technical user can specify `client_id` to get metrics for particular
    client. Ignored for client
    """

    zone_names: SequenceNotStr[str]
    """
    Admin and technical user can specify `monitor_id` to get metrics for particular
    zone. Ignored for client
    """
