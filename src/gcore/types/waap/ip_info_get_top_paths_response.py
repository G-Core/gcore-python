# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .waap_top_path_detail import WaapTopPathDetail

__all__ = ["IPInfoGetTopPathsResponse"]

IPInfoGetTopPathsResponse: TypeAlias = List[WaapTopPathDetail]
