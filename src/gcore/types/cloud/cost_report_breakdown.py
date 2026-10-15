# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CostReportBreakdown", "Result", "ResultUsage"]


class ResultUsage(BaseModel):
    """How much the group was used that day, and what that costs."""

    cost: Optional[float] = None
    """Cost for the day, never rounded. Null if there is no price."""

    currency: Optional[str] = None
    """Currency of the cost, null if there is no cost"""

    unit: str
    """Unit of the billing value"""

    value: float
    """Usage of the billing metric for the day, in `unit`, kept at full precision."""


class Result(BaseModel):
    """One day of usage for one `group_by` value."""

    date: datetime.date
    """Day the usage was billed for"""

    error: Optional[Literal["Multiple subscriptions", "No tariff"]] = None
    """Why a row has no cost. Values are the plain strings v1 has always returned."""

    flavor: Optional[str] = None
    """Flavor name, set when `group_by` is 'flavor'"""

    project_id: Optional[int] = None
    """Project ID, set when `group_by` is 'project'"""

    region_id: Optional[int] = None
    """Region ID, set when `group_by` is 'region'.

    0 means global usage that has no region.
    """

    type: Optional[
        Literal[
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
    ] = None
    """Resource types for prebilling report"""

    usage: ResultUsage
    """How much the group was used that day, and what that costs."""


class CostReportBreakdown(BaseModel):
    count: int
    """Count of returned rows"""

    price_status: Literal["error", "hide", "show"]
    """
    'show' when the client may see prices, 'hide' for trial clients, clients with no
    product status, and clients of a reseller that does not expose prices. This
    report never returns 'error'.
    """

    results: List[Result]
