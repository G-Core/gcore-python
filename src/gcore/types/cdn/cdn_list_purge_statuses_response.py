# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .purge_status import PurgeStatus

__all__ = ["CdnListPurgeStatusesResponse"]

CdnListPurgeStatusesResponse: TypeAlias = List[PurgeStatus]
