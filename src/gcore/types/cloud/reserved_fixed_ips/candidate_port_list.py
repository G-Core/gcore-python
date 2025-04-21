# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .candidate_port import CandidatePort

__all__ = ["CandidatePortList"]


class CandidatePortList(BaseModel):
    count: int
    """
    '#/components/schemas/VIPAttachCandidateSerializerList/properties/count'
    "$.components.schemas.VIPAttachCandidateSerializerList.properties.count"
    """

    results: List[CandidatePort]
    """
    '#/components/schemas/VIPAttachCandidateSerializerList/properties/results'
    "$.components.schemas.VIPAttachCandidateSerializerList.properties.results"
    """
