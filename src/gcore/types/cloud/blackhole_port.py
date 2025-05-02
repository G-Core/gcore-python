# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["BlackholePort"]


class BlackholePort(BaseModel):
    alarm_end: datetime = FieldInfo(alias="AlarmEnd")
    """
    '#/components/schemas/BlackholePortSerializer/properties/AlarmEnd'
    "$.components.schemas.BlackholePortSerializer.properties.AlarmEnd"
    """

    alarm_start: datetime = FieldInfo(alias="AlarmStart")
    """
    '#/components/schemas/BlackholePortSerializer/properties/AlarmStart'
    "$.components.schemas.BlackholePortSerializer.properties.AlarmStart"
    """

    alarm_state: Literal[
        "ACK_REQ",
        "ALARM",
        "ARCHIVED",
        "CLEAR",
        "CLEARING",
        "CLEARING_FAIL",
        "END_GRACE",
        "END_WAIT",
        "MANUAL_CLEAR",
        "MANUAL_CLEARING",
        "MANUAL_CLEARING_FAIL",
        "MANUAL_MITIGATING",
        "MANUAL_STARTING",
        "MANUAL_STARTING_FAIL",
        "MITIGATING",
        "STARTING",
        "STARTING_FAIL",
        "START_WAIT",
        "ack_req",
        "alarm",
        "archived",
        "clear",
        "clearing",
        "clearing_fail",
        "end_grace",
        "end_wait",
        "manual_clear",
        "manual_clearing",
        "manual_clearing_fail",
        "manual_mitigating",
        "manual_starting",
        "manual_starting_fail",
        "mitigating",
        "start_wait",
        "starting",
        "starting_fail",
    ] = FieldInfo(alias="AlarmState")
    """
    '#/components/schemas/BlackholePortSerializer/properties/AlarmState'
    "$.components.schemas.BlackholePortSerializer.properties.AlarmState"
    """

    alert_duration: str = FieldInfo(alias="AlertDuration")
    """
    '#/components/schemas/BlackholePortSerializer/properties/AlertDuration'
    "$.components.schemas.BlackholePortSerializer.properties.AlertDuration"
    """

    destination_ip: str = FieldInfo(alias="DestinationIP")
    """
    '#/components/schemas/BlackholePortSerializer/properties/DestinationIP'
    "$.components.schemas.BlackholePortSerializer.properties.DestinationIP"
    """

    id: int = FieldInfo(alias="ID")
    """
    '#/components/schemas/BlackholePortSerializer/properties/ID'
    "$.components.schemas.BlackholePortSerializer.properties.ID"
    """
