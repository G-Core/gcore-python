# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import date, datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BillingReservationListParams"]


class BillingReservationListParams(TypedDict, total=False):
    activated_from: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """
    '#/paths/%2Fcloud%2Fv1%2Freservations/get/parameters/0'
    "$.paths['/cloud/v1/reservations'].get.parameters[0]"
    """

    activated_to: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """
    '#/paths/%2Fcloud%2Fv1%2Freservations/get/parameters/1'
    "$.paths['/cloud/v1/reservations'].get.parameters[1]"
    """

    created_from: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    '#/paths/%2Fcloud%2Fv1%2Freservations/get/parameters/2'
    "$.paths['/cloud/v1/reservations'].get.parameters[2]"
    """

    created_to: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    '#/paths/%2Fcloud%2Fv1%2Freservations/get/parameters/3'
    "$.paths['/cloud/v1/reservations'].get.parameters[3]"
    """

    deactivated_from: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """
    '#/paths/%2Fcloud%2Fv1%2Freservations/get/parameters/4'
    "$.paths['/cloud/v1/reservations'].get.parameters[4]"
    """

    deactivated_to: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """
    '#/paths/%2Fcloud%2Fv1%2Freservations/get/parameters/5'
    "$.paths['/cloud/v1/reservations'].get.parameters[5]"
    """

    limit: int
    """
    '#/paths/%2Fcloud%2Fv1%2Freservations/get/parameters/6'
    "$.paths['/cloud/v1/reservations'].get.parameters[6]"
    """

    metric_name: str
    """
    '#/paths/%2Fcloud%2Fv1%2Freservations/get/parameters/7'
    "$.paths['/cloud/v1/reservations'].get.parameters[7]"
    """

    offset: int
    """
    '#/paths/%2Fcloud%2Fv1%2Freservations/get/parameters/8'
    "$.paths['/cloud/v1/reservations'].get.parameters[8]"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Freservations/get/parameters/9'
    "$.paths['/cloud/v1/reservations'].get.parameters[9]"
    """

    status: List[
        Literal["ACTIVATED", "APPROVED", "COPIED", "CREATED", "EXPIRED", "REJECTED", "RESERVED", "WAITING_FOR_PAYMENT"]
    ]
    """
    '#/paths/%2Fcloud%2Fv1%2Freservations/get/parameters/10'
    "$.paths['/cloud/v1/reservations'].get.parameters[10]"
    """
