# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["VipToggleParams"]


class VipToggleParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Freserved_fixed_ips%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bport_id%7D/patch/parameters/0/schema'
    "$.paths['/cloud/v1/reserved_fixed_ips/{project_id}/{region_id}/{port_id}'].patch.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Freserved_fixed_ips%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bport_id%7D/patch/parameters/1/schema'
    "$.paths['/cloud/v1/reserved_fixed_ips/{project_id}/{region_id}/{port_id}'].patch.parameters[1].schema"
    """

    is_vip: Required[bool]
    """
    '#/components/schemas/PatchReservedFixedIPSerializer/properties/is_vip'
    "$.components.schemas.PatchReservedFixedIPSerializer.properties.is_vip"
    """
