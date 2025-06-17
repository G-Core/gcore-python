# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .waap_top_user_agent import WaapTopUserAgent

__all__ = ["IPInfoGetTopUserAgentsResponse"]

IPInfoGetTopUserAgentsResponse: TypeAlias = List[WaapTopUserAgent]
