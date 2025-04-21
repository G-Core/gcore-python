# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ProjectReplaceParams"]


class ProjectReplaceParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fprojects%2F%7Bproject_id%7D/put/parameters/0/schema'
    "$.paths['/cloud/v1/projects/{project_id}'].put.parameters[0].schema"
    """

    name: Required[str]
    """
    '#/components/schemas/NameDescriptionSerializer/properties/name'
    "$.components.schemas.NameDescriptionSerializer.properties.name"
    """

    description: Optional[str]
    """
    '#/components/schemas/NameDescriptionSerializer/properties/description/anyOf/0'
    "$.components.schemas.NameDescriptionSerializer.properties.description.anyOf[0]"
    """
