# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .price_floating_ip_param import PriceFloatingIPParam

__all__ = ["PricePortReferenceParam"]


class PricePortReferenceParam(TypedDict, total=False):
    port_id: Required[str]
    """Existing port."""

    floating_ip: PriceFloatingIPParam
    """Floating IP of the port."""
