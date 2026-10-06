# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .waap_top_attack import WaapTopAttack

__all__ = ["IPInfoGetTopAttacksResponse"]

IPInfoGetTopAttacksResponse: TypeAlias = List[WaapTopAttack]
