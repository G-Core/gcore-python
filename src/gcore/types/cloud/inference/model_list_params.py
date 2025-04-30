# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .mlcatalog_order_by_choices import MlcatalogOrderByChoices

__all__ = ["ModelListParams"]


class ModelListParams(TypedDict, total=False):
    limit: int
    """
    '#/paths/%2Fcloud%2Fv3%2Finference%2Fmodels/get/parameters/0'
    "$.paths['/cloud/v3/inference/models'].get.parameters[0]"
    """

    offset: int
    """
    '#/paths/%2Fcloud%2Fv3%2Finference%2Fmodels/get/parameters/1'
    "$.paths['/cloud/v3/inference/models'].get.parameters[1]"
    """

    order_by: MlcatalogOrderByChoices
    """
    '#/paths/%2Fcloud%2Fv3%2Finference%2Fmodels/get/parameters/2'
    "$.paths['/cloud/v3/inference/models'].get.parameters[2]"
    """
