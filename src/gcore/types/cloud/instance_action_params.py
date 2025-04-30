# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["InstanceActionParams", "StartActionInstanceSerializer", "BasicActionInstanceSerializer"]


class StartActionInstanceSerializer(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv2%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Faction/post/parameters/0/schema'
    "$.paths['/cloud/v2/instances/{project_id}/{region_id}/{instance_id}/action'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv2%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Faction/post/parameters/1/schema'
    "$.paths['/cloud/v2/instances/{project_id}/{region_id}/{instance_id}/action'].post.parameters[1].schema"
    """

    action: Required[Literal["start"]]
    """
    '#/components/schemas/StartActionInstanceSerializer/properties/action'
    "$.components.schemas.StartActionInstanceSerializer.properties.action"
    """

    activate_profile: Optional[bool]
    """
    '#/components/schemas/StartActionInstanceSerializer/properties/activate_profile/anyOf/0'
    "$.components.schemas.StartActionInstanceSerializer.properties.activate_profile.anyOf[0]"
    """


class BasicActionInstanceSerializer(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv2%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Faction/post/parameters/0/schema'
    "$.paths['/cloud/v2/instances/{project_id}/{region_id}/{instance_id}/action'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv2%2Finstances%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Binstance_id%7D%2Faction/post/parameters/1/schema'
    "$.paths['/cloud/v2/instances/{project_id}/{region_id}/{instance_id}/action'].post.parameters[1].schema"
    """

    action: Required[Literal["reboot", "reboot_hard", "resume", "stop", "suspend"]]
    """
    '#/components/schemas/BasicActionInstanceSerializer/properties/action'
    "$.components.schemas.BasicActionInstanceSerializer.properties.action"
    """


InstanceActionParams: TypeAlias = Union[StartActionInstanceSerializer, BasicActionInstanceSerializer]
