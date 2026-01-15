# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ....._models import BaseModel
from .candidate_port import CandidatePort

__all__ = ["CandidatePortList"]


class CandidatePortList(BaseModel):
    count: int
    """Number of objects"""

    results: List[CandidatePort]
    """Objects"""
