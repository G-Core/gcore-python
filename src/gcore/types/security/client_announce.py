# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["ClientAnnounce"]


class ClientAnnounce(BaseModel):
    announced: List[str]

    client_id: int

    not_announced: List[str]
