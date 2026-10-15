# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CostReportDetailed", "Result", "ResultResource", "ResultUsage"]


class ResultResource(BaseModel):
    """What the resource is."""

    flavor: Optional[str] = None
    """Flavor name"""

    name: Optional[str] = None
    """Name of the resource"""

    tags: Optional[List[Dict[str, str]]] = None
    """List of tags"""

    type: Literal[
        "ai_cluster",
        "ai_virtual_cluster",
        "backup",
        "baremetal",
        "basic_vm",
        "containers",
        "dbaas_postgresql_connection_pooler",
        "dbaas_postgresql_cpu",
        "dbaas_postgresql_memory",
        "dbaas_postgresql_public_network",
        "dbaas_postgresql_volume",
        "egress_traffic",
        "external_ip",
        "file_share",
        "floatingip",
        "functions",
        "functions_calls",
        "functions_traffic",
        "image",
        "inference",
        "inference_public_models",
        "instance",
        "load_balancer",
        "log_index",
        "snapshot",
        "volume",
    ]
    """Resource type"""

    uuid: Optional[str] = None
    """UUID of the resource"""


class ResultUsage(BaseModel):
    """How much it was used, and what that costs."""

    cost: Optional[float] = None
    """Cost for the requested period, never rounded. Null if there is no price."""

    currency: Optional[str] = None
    """Currency of the cost, null if there is no cost"""

    first_seen: datetime
    """First time the resource was seen in the given period"""

    last_seen: datetime
    """Last time the resource was seen in the given period.

    Earlier than 'time_to' means the resource stopped before the period ended.
    """

    unit: str
    """Unit of the billing value"""

    value: float
    """Usage of the billing metric for the period, in `unit`, kept at full precision."""


class Result(BaseModel):
    error: Optional[Literal["Multiple subscriptions", "No tariff"]] = None
    """Why a row has no cost. Values are the plain strings v1 has always returned."""

    project_id: int
    """ID of the project the resource belongs to"""

    region_id: int
    """Region ID. 0 means global usage that has no region."""

    resource: ResultResource
    """What the resource is."""

    usage: ResultUsage
    """How much it was used, and what that costs."""


class CostReportDetailed(BaseModel):
    count: int
    """Count of all the resources"""

    price_status: Literal["error", "hide", "show"]
    """
    'show' when the client may see prices, 'hide' for trial clients, clients with no
    product status, and clients of a reseller that does not expose prices.
    """

    results: List[Result]
