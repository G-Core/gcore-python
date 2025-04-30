# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["FlavorListParams"]


class FlavorListParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv3%2Fgpu%2Fbaremetal%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2Fflavors/get/parameters/0/schema'
    "$.paths['/cloud/v3/gpu/baremetal/{project_id}/{region_id}/flavors'].get.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv3%2Fgpu%2Fbaremetal%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2Fflavors/get/parameters/1/schema'
    "$.paths['/cloud/v3/gpu/baremetal/{project_id}/{region_id}/flavors'].get.parameters[1].schema"
    """

    hide_disabled: Optional[bool]
    """
    '#/paths/%2Fcloud%2Fv3%2Fgpu%2Fbaremetal%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2Fflavors/get/parameters/2/schema/anyOf/0'
    "$.paths['/cloud/v3/gpu/baremetal/{project_id}/{region_id}/flavors'].get.parameters[2].schema.anyOf[0]"
    """

    include_prices: Optional[bool]
    """
    '#/paths/%2Fcloud%2Fv3%2Fgpu%2Fbaremetal%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2Fflavors/get/parameters/3/schema/anyOf/0'
    "$.paths['/cloud/v3/gpu/baremetal/{project_id}/{region_id}/flavors'].get.parameters[3].schema.anyOf[0]"
    """
