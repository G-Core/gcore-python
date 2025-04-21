# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..network import Network
from ...._models import BaseModel
from .ip_assignment import IPAssignment

__all__ = ["CandidatePort"]


class CandidatePort(BaseModel):
    instance_id: str
    """
    '#/components/schemas/VIPAttachCandidateSerializer/properties/instance_id'
    "$.components.schemas.VIPAttachCandidateSerializer.properties.instance_id"
    """

    instance_name: str
    """
    '#/components/schemas/VIPAttachCandidateSerializer/properties/instance_name'
    "$.components.schemas.VIPAttachCandidateSerializer.properties.instance_name"
    """

    ip_assignments: List[IPAssignment]
    """
    '#/components/schemas/VIPAttachCandidateSerializer/properties/ip_assignments'
    "$.components.schemas.VIPAttachCandidateSerializer.properties.ip_assignments"
    """

    network: Network
    """
    '#/components/schemas/VIPAttachCandidateSerializer/properties/network'
    "$.components.schemas.VIPAttachCandidateSerializer.properties.network"
    """

    port_id: str
    """
    '#/components/schemas/VIPAttachCandidateSerializer/properties/port_id'
    "$.components.schemas.VIPAttachCandidateSerializer.properties.port_id"
    """
