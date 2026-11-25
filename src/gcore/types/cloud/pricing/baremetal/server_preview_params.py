# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

from ...price_port_spec_param import PricePortSpecParam
from ...price_port_reference_param import PricePortReferenceParam

__all__ = ["ServerPreviewParams", "Interface"]


class ServerPreviewParams(TypedDict, total=False):
    project_id: int
    """Project ID."""

    flavor_name: Required[str]
    """Flavor of the server."""

    region_id: Required[int]
    """Region of the server."""

    interfaces: Iterable[Interface]
    """Ports in NIC order.

    An entry with `port_id` is an existing port, any other entry is a new one. Omit
    it to price the server without ports.
    """


Interface: TypeAlias = Union[PricePortReferenceParam, PricePortSpecParam]
