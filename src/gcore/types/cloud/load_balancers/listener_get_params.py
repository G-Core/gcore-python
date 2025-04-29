# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ListenerGetParams"]


class ListenerGetParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Flblisteners%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Blistener_id%7D/get/parameters/0/schema'
    "$.paths['/cloud/v1/lblisteners/{project_id}/{region_id}/{listener_id}'].get.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Flblisteners%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Blistener_id%7D/get/parameters/1/schema'
    "$.paths['/cloud/v1/lblisteners/{project_id}/{region_id}/{listener_id}'].get.parameters[1].schema"
    """

    show_stats: bool
    """
    '#/paths/%2Fcloud%2Fv1%2Flblisteners%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Blistener_id%7D/get/parameters/3'
    "$.paths['/cloud/v1/lblisteners/{project_id}/{region_id}/{listener_id}'].get.parameters[3]"
    """
