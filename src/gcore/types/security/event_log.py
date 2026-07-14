# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["EventLog"]


class EventLog(BaseModel):
    id: str

    alert_type: Optional[Literal["ddos_alert", "rtbh_alert"]] = None

    attack_packet_sizes: Optional[List[Dict[str, object]]] = None

    attack_power_bps: Optional[float] = None

    attack_power_pps: Optional[float] = None

    attack_start_time: Optional[datetime] = None

    attack_top_destination_ports: Optional[List[Dict[str, object]]] = None

    attack_top_protocols: Optional[List[Dict[str, object]]] = None

    attack_top_source_countries: Optional[List[Dict[str, object]]] = None

    attack_top_source_ips: Optional[List[Dict[str, object]]] = None

    attack_top_source_ports: Optional[List[Dict[str, object]]] = None

    attack_traffic: Optional[List[Dict[str, object]]] = None

    client_id: Optional[int] = None

    notification_type: Optional[str] = None

    number_of_ip_involved_in_attack: Optional[int] = None

    targeted_ip_addresses: Optional[str] = None
