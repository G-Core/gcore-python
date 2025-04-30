# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["RegistryResizeParams"]


class RegistryResizeParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fregistries%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bregistry_id%7D%2Fresize/patch/parameters/0/schema'
    "$.paths['/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/resize'].patch.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fregistries%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bregistry_id%7D%2Fresize/patch/parameters/1/schema'
    "$.paths['/cloud/v1/registries/{project_id}/{region_id}/{registry_id}/resize'].patch.parameters[1].schema"
    """

    storage_limit: int
    """
    '#/components/schemas/RegistryResizeSerializer/properties/storage_limit'
    "$.components.schemas.RegistryResizeSerializer.properties.storage_limit"
    """
