# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["EventListParams"]


class EventListParams(TypedDict, total=False):
    alert_type: Optional[Literal["ddos_alert", "rtbh_alert"]]

    date_from: Annotated[Union[Union[str, datetime], str], PropertyInfo(format="iso8601")]

    date_to: Annotated[Union[Union[str, datetime], str], PropertyInfo(format="iso8601")]

    limit: int

    offset: int

    ordering: Literal[
        "attack_start_time",
        "-attack_start_time",
        "attack_power_bps",
        "-attack_power_bps",
        "attack_power_pps",
        "-attack_power_pps",
        "number_of_ip_involved_in_attack",
        "-number_of_ip_involved_in_attack",
        "alert_type",
        "-alert_type",
    ]

    targeted_ip_addresses: Optional[str]
