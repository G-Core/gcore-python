# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .waap_top_session import WaapTopSession

__all__ = ["IPInfoGetTopSessionsResponse"]

IPInfoGetTopSessionsResponse: TypeAlias = List[WaapTopSession]
