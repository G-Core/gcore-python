# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["ServerActionParams", "StartActionInstanceSerializer", "BasicBareMetalActionInstanceSerializer"]


class StartActionInstanceSerializer(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    action: Required[Literal["start"]]
    """Instance action name"""

    activate_profile: Optional[bool]
    """Used on start instance to activate Advanced DDoS profile"""


class BasicBareMetalActionInstanceSerializer(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    action: Required[Literal["reboot", "reboot_hard", "stop"]]
    """Instance action name"""


ServerActionParams: TypeAlias = Union[StartActionInstanceSerializer, BasicBareMetalActionInstanceSerializer]
