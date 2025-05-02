# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["InstanceActionParams", "StartActionInstanceSerializer", "BasicActionInstanceSerializer"]


class StartActionInstanceSerializer(TypedDict, total=False):
    project_id: int

    region_id: int

    action: Required[Literal["start"]]
    """Instance action name"""

    activate_profile: Optional[bool]
    """Used on start instance to activate Advanced DDoS profile"""


class BasicActionInstanceSerializer(TypedDict, total=False):
    project_id: int

    region_id: int

    action: Required[Literal["reboot", "reboot_hard", "resume", "stop", "suspend"]]
    """Instance action name"""


InstanceActionParams: TypeAlias = Union[StartActionInstanceSerializer, BasicActionInstanceSerializer]
