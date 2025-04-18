# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ProjectCreateParams"]


class ProjectCreateParams(TypedDict, total=False):
    name: Required[str]
    """
    '#/components/schemas/CreateProjectSerializer/properties/name'
    "$.components.schemas.CreateProjectSerializer.properties.name"
    """

    client_id: Optional[int]
    """
    '#/components/schemas/CreateProjectSerializer/properties/client_id/anyOf/0'
    "$.components.schemas.CreateProjectSerializer.properties.client_id.anyOf[0]"
    """

    description: Optional[str]
    """
    '#/components/schemas/CreateProjectSerializer/properties/description/anyOf/0'
    "$.components.schemas.CreateProjectSerializer.properties.description.anyOf[0]"
    """

    state: Optional[str]
    """
    '#/components/schemas/CreateProjectSerializer/properties/state/anyOf/0'
    "$.components.schemas.CreateProjectSerializer.properties.state.anyOf[0]"
    """
