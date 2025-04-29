# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["BillingReservation", "AmountPrices", "Resource"]


class AmountPrices(BaseModel):
    commit_price_per_month: str
    """
    '#/components/schemas/BillingReservationAmountPricesResponseSerializer/properties/commit_price_per_month'
    "$.components.schemas.BillingReservationAmountPricesResponseSerializer.properties.commit_price_per_month"
    """

    commit_price_per_unit: str
    """
    '#/components/schemas/BillingReservationAmountPricesResponseSerializer/properties/commit_price_per_unit'
    "$.components.schemas.BillingReservationAmountPricesResponseSerializer.properties.commit_price_per_unit"
    """

    commit_price_total: str
    """
    '#/components/schemas/BillingReservationAmountPricesResponseSerializer/properties/commit_price_total'
    "$.components.schemas.BillingReservationAmountPricesResponseSerializer.properties.commit_price_total"
    """

    currency_code: str
    """
    '#/components/schemas/BillingReservationAmountPricesResponseSerializer/properties/currency_code'
    "$.components.schemas.BillingReservationAmountPricesResponseSerializer.properties.currency_code"
    """

    overcommit_price_per_month: str
    """
    '#/components/schemas/BillingReservationAmountPricesResponseSerializer/properties/overcommit_price_per_month'
    "$.components.schemas.BillingReservationAmountPricesResponseSerializer.properties.overcommit_price_per_month"
    """

    overcommit_price_per_unit: str
    """
    '#/components/schemas/BillingReservationAmountPricesResponseSerializer/properties/overcommit_price_per_unit'
    "$.components.schemas.BillingReservationAmountPricesResponseSerializer.properties.overcommit_price_per_unit"
    """

    overcommit_price_total: str
    """
    '#/components/schemas/BillingReservationAmountPricesResponseSerializer/properties/overcommit_price_total'
    "$.components.schemas.BillingReservationAmountPricesResponseSerializer.properties.overcommit_price_total"
    """


class Resource(BaseModel):
    activity_period: str
    """
    '#/components/schemas/BillingReservationResourceSerializer/properties/activity_period'
    "$.components.schemas.BillingReservationResourceSerializer.properties.activity_period"
    """

    activity_period_length: int
    """
    '#/components/schemas/BillingReservationResourceSerializer/properties/activity_period_length'
    "$.components.schemas.BillingReservationResourceSerializer.properties.activity_period_length"
    """

    billing_plan_item_id: int
    """
    '#/components/schemas/BillingReservationResourceSerializer/properties/billing_plan_item_id'
    "$.components.schemas.BillingReservationResourceSerializer.properties.billing_plan_item_id"
    """

    commit_price_per_month: str
    """
    '#/components/schemas/BillingReservationResourceSerializer/properties/commit_price_per_month'
    "$.components.schemas.BillingReservationResourceSerializer.properties.commit_price_per_month"
    """

    commit_price_per_unit: str
    """
    '#/components/schemas/BillingReservationResourceSerializer/properties/commit_price_per_unit'
    "$.components.schemas.BillingReservationResourceSerializer.properties.commit_price_per_unit"
    """

    commit_price_total: str
    """
    '#/components/schemas/BillingReservationResourceSerializer/properties/commit_price_total'
    "$.components.schemas.BillingReservationResourceSerializer.properties.commit_price_total"
    """

    overcommit_billing_plan_item_id: int
    """
    '#/components/schemas/BillingReservationResourceSerializer/properties/overcommit_billing_plan_item_id'
    "$.components.schemas.BillingReservationResourceSerializer.properties.overcommit_billing_plan_item_id"
    """

    overcommit_price_per_month: str
    """
    '#/components/schemas/BillingReservationResourceSerializer/properties/overcommit_price_per_month'
    "$.components.schemas.BillingReservationResourceSerializer.properties.overcommit_price_per_month"
    """

    overcommit_price_per_unit: str
    """
    '#/components/schemas/BillingReservationResourceSerializer/properties/overcommit_price_per_unit'
    "$.components.schemas.BillingReservationResourceSerializer.properties.overcommit_price_per_unit"
    """

    overcommit_price_total: str
    """
    '#/components/schemas/BillingReservationResourceSerializer/properties/overcommit_price_total'
    "$.components.schemas.BillingReservationResourceSerializer.properties.overcommit_price_total"
    """

    resource_count: int
    """
    '#/components/schemas/BillingReservationResourceSerializer/properties/resource_count'
    "$.components.schemas.BillingReservationResourceSerializer.properties.resource_count"
    """

    resource_name: str
    """
    '#/components/schemas/BillingReservationResourceSerializer/properties/resource_name'
    "$.components.schemas.BillingReservationResourceSerializer.properties.resource_name"
    """

    resource_type: Literal["flavor"]
    """
    '#/components/schemas/BillingReservationResourceSerializer/properties/resource_type'
    "$.components.schemas.BillingReservationResourceSerializer.properties.resource_type"
    """

    unit_name: str
    """
    '#/components/schemas/BillingReservationResourceSerializer/properties/unit_name'
    "$.components.schemas.BillingReservationResourceSerializer.properties.unit_name"
    """

    unit_size_month: str
    """
    '#/components/schemas/BillingReservationResourceSerializer/properties/unit_size_month'
    "$.components.schemas.BillingReservationResourceSerializer.properties.unit_size_month"
    """

    unit_size_total: str
    """
    '#/components/schemas/BillingReservationResourceSerializer/properties/unit_size_total'
    "$.components.schemas.BillingReservationResourceSerializer.properties.unit_size_total"
    """

    cpu: Optional[str] = None
    """
    '#/components/schemas/BillingReservationResourceSerializer/properties/cpu/anyOf/0'
    "$.components.schemas.BillingReservationResourceSerializer.properties.cpu.anyOf[0]"
    """

    disk: Optional[str] = None
    """
    '#/components/schemas/BillingReservationResourceSerializer/properties/disk/anyOf/0'
    "$.components.schemas.BillingReservationResourceSerializer.properties.disk.anyOf[0]"
    """

    ram: Optional[str] = None
    """
    '#/components/schemas/BillingReservationResourceSerializer/properties/ram/anyOf/0'
    "$.components.schemas.BillingReservationResourceSerializer.properties.ram.anyOf[0]"
    """


class BillingReservation(BaseModel):
    id: int
    """
    '#/components/schemas/BillingReservationItemResponseSerializer/properties/id'
    "$.components.schemas.BillingReservationItemResponseSerializer.properties.id"
    """

    active_from: date
    """
    '#/components/schemas/BillingReservationItemResponseSerializer/properties/active_from'
    "$.components.schemas.BillingReservationItemResponseSerializer.properties.active_from"
    """

    active_to: date
    """
    '#/components/schemas/BillingReservationItemResponseSerializer/properties/active_to'
    "$.components.schemas.BillingReservationItemResponseSerializer.properties.active_to"
    """

    activity_period: str
    """
    '#/components/schemas/BillingReservationItemResponseSerializer/properties/activity_period'
    "$.components.schemas.BillingReservationItemResponseSerializer.properties.activity_period"
    """

    activity_period_length: int
    """
    '#/components/schemas/BillingReservationItemResponseSerializer/properties/activity_period_length'
    "$.components.schemas.BillingReservationItemResponseSerializer.properties.activity_period_length"
    """

    amount_prices: AmountPrices
    """
    '#/components/schemas/BillingReservationItemResponseSerializer/properties/amount_prices'
    "$.components.schemas.BillingReservationItemResponseSerializer.properties.amount_prices"
    """

    billing_plan_id: int
    """
    '#/components/schemas/BillingReservationItemResponseSerializer/properties/billing_plan_id'
    "$.components.schemas.BillingReservationItemResponseSerializer.properties.billing_plan_id"
    """

    created_at: datetime
    """
    '#/components/schemas/BillingReservationItemResponseSerializer/properties/created_at'
    "$.components.schemas.BillingReservationItemResponseSerializer.properties.created_at"
    """

    error: Optional[str] = None
    """
    '#/components/schemas/BillingReservationItemResponseSerializer/properties/error/anyOf/0'
    "$.components.schemas.BillingReservationItemResponseSerializer.properties.error.anyOf[0]"
    """

    eta: Optional[date] = None
    """
    '#/components/schemas/BillingReservationItemResponseSerializer/properties/eta/anyOf/0'
    "$.components.schemas.BillingReservationItemResponseSerializer.properties.eta.anyOf[0]"
    """

    is_expiration_message_visible: bool
    """
    '#/components/schemas/BillingReservationItemResponseSerializer/properties/is_expiration_message_visible'
    "$.components.schemas.BillingReservationItemResponseSerializer.properties.is_expiration_message_visible"
    """

    name: str
    """
    '#/components/schemas/BillingReservationItemResponseSerializer/properties/name'
    "$.components.schemas.BillingReservationItemResponseSerializer.properties.name"
    """

    next_statuses: List[str]
    """
    '#/components/schemas/BillingReservationItemResponseSerializer/properties/next_statuses'
    "$.components.schemas.BillingReservationItemResponseSerializer.properties.next_statuses"
    """

    region_id: int
    """
    '#/components/schemas/BillingReservationItemResponseSerializer/properties/region_id'
    "$.components.schemas.BillingReservationItemResponseSerializer.properties.region_id"
    """

    region_name: str
    """
    '#/components/schemas/BillingReservationItemResponseSerializer/properties/region_name'
    "$.components.schemas.BillingReservationItemResponseSerializer.properties.region_name"
    """

    remind_expiration_message: Optional[date] = None
    """
    '#/components/schemas/BillingReservationItemResponseSerializer/properties/remind_expiration_message/anyOf/0'
    "$.components.schemas.BillingReservationItemResponseSerializer.properties.remind_expiration_message.anyOf[0]"
    """

    resources: List[Resource]
    """
    '#/components/schemas/BillingReservationItemResponseSerializer/properties/resources'
    "$.components.schemas.BillingReservationItemResponseSerializer.properties.resources"
    """

    status: str
    """
    '#/components/schemas/BillingReservationItemResponseSerializer/properties/status'
    "$.components.schemas.BillingReservationItemResponseSerializer.properties.status"
    """

    user_status: str
    """
    '#/components/schemas/BillingReservationItemResponseSerializer/properties/user_status'
    "$.components.schemas.BillingReservationItemResponseSerializer.properties.user_status"
    """
