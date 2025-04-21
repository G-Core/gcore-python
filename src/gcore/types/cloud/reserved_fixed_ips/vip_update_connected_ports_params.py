# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["VipUpdateConnectedPortsParams"]


class VipUpdateConnectedPortsParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Freserved_fixed_ips%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bport_id%7D%2Fconnected_devices/patch/parameters/0/schema'
    "$.paths['/cloud/v1/reserved_fixed_ips/{project_id}/{region_id}/{port_id}/connected_devices'].patch.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Freserved_fixed_ips%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bport_id%7D%2Fconnected_devices/patch/parameters/1/schema'
    "$.paths['/cloud/v1/reserved_fixed_ips/{project_id}/{region_id}/{port_id}/connected_devices'].patch.parameters[1].schema"
    """

    port_ids: List[str]
    """
    '#/components/schemas/PortIDsForVIPSerializer/properties/port_ids'
    "$.components.schemas.PortIDsForVIPSerializer.properties.port_ids"
    """
