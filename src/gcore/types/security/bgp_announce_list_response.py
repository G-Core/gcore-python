# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .client_announce import ClientAnnounce

__all__ = ["BgpAnnounceListResponse"]

BgpAnnounceListResponse: TypeAlias = List[ClientAnnounce]
