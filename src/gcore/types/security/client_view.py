# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ClientView"]


class ClientView(BaseModel):
    id: str

    alert_type: Optional[Literal["ddos_alert", "rtbh_alert"]] = None

    attack_power_bps: Optional[float] = None

    attack_power_pps: Optional[float] = None

    attack_start_time: Optional[datetime] = None

    client_id: Optional[int] = None

    notification_type: Optional[str] = None

    number_of_ip_involved_in_attack: Optional[int] = None

    targeted_ip_addresses: Optional[str] = None
