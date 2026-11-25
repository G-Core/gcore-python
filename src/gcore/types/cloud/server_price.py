# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ServerPrice", "BootVolume", "DataVolume", "EgressTraffic", "ExternalIPs", "Flavor", "FloatingIPs"]


class BootVolume(BaseModel):
    """Price of the boot volume. Null when the body has no boot volume."""

    discount_percent: float
    """Discount in percent. 0 when there is no discount."""

    hourly: float
    """Price per hour after the discount."""

    monthly: float
    """Price per month after the discount."""

    monthly_before_discount: float
    """Price per month before the discount."""

    size: int
    """Volume size in GiB. The price uses the size in GB"""

    type: str
    """Volume type."""


class DataVolume(BaseModel):
    discount_percent: float
    """Discount in percent. 0 when there is no discount."""

    hourly: float
    """Price per hour after the discount."""

    monthly: float
    """Price per month after the discount."""

    monthly_before_discount: float
    """Price per month before the discount."""

    size: int
    """Volume size in GiB. The price uses the size in GB"""

    type: str
    """Volume type."""


class EgressTraffic(BaseModel):
    """Rate of the outgoing traffic.

    It is not part of the totals. Null when the traffic of the server has no tariff.
    """

    discount_percent: float
    """Discount in percent. 0 when there is no discount."""

    per_gb: float
    """Price of one GB of used traffic after the discount."""

    per_gb_before_discount: float
    """Price of one GB before the discount."""


class ExternalIPs(BaseModel):
    """Price of the IPv4 addresses that ports have on the public network."""

    count: int
    """Number of IP addresses. 0 when the server has none."""

    discount_percent: float
    """Discount in percent. 0 when there is no discount."""

    hourly: float
    """Price per hour after the discount."""

    monthly: float
    """Price per month after the discount."""

    monthly_before_discount: float
    """Price per month before the discount."""


class Flavor(BaseModel):
    """Price of the flavor."""

    count: int
    """Number of servers. The create makes one server."""

    discount_percent: float
    """Discount in percent. 0 when there is no discount."""

    hourly: float
    """Price per hour after the discount."""

    monthly: float
    """Price per month after the discount."""

    monthly_before_discount: float
    """Price per month before the discount."""

    name: str
    """Flavor name."""


class FloatingIPs(BaseModel):
    """Price of the floating IPs.

    A floating IP is a separate address that maps to a port.
    """

    count: int
    """Number of IP addresses. 0 when the server has none."""

    discount_percent: float
    """Discount in percent. 0 when there is no discount."""

    hourly: float
    """Price per hour after the discount."""

    monthly: float
    """Price per month after the discount."""

    monthly_before_discount: float
    """Price per month before the discount."""


class ServerPrice(BaseModel):
    boot_volume: Optional[BootVolume] = None
    """Price of the boot volume. Null when the body has no boot volume."""

    currency: str
    """Currency code."""

    data_volumes: List[DataVolume]
    """Prices of the data volumes, in the order of the request."""

    egress_traffic: Optional[EgressTraffic] = None
    """Rate of the outgoing traffic.

    It is not part of the totals. Null when the traffic of the server has no tariff.
    """

    external_ips: ExternalIPs
    """Price of the IPv4 addresses that ports have on the public network."""

    flavor: Flavor
    """Price of the flavor."""

    floating_ips: FloatingIPs
    """Price of the floating IPs.

    A floating IP is a separate address that maps to a port.
    """

    hourly: float
    """Sum of the hourly prices of all sections."""

    monthly: float
    """Sum of the monthly prices of all sections."""

    monthly_before_discount: float
    """Sum of the monthly prices before the discount."""

    tax_percent: float
    """Tax in percent. The prices include it."""
