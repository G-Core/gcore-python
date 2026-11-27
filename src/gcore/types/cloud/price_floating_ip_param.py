# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PriceFloatingIPParam"]


class PriceFloatingIPParam(TypedDict, total=False):
    id: str
    """ID of an existing floating IP. Omit it for a new floating IP."""
