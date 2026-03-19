# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["WaapSimpleEventStatistics", "Reference", "ReferenceIPReference", "ReferenceDomainReference"]


class ReferenceIPReference(BaseModel):
    country: str

    org: str


class ReferenceDomainReference(BaseModel):
    domain_id: int


Reference: TypeAlias = Union[ReferenceIPReference, ReferenceDomainReference]


class WaapSimpleEventStatistics(BaseModel):
    """A collection of event counts per dimension values over a time span."""

    allowed: List[List[object]]
    """Number of requests passed due to a permissive security rule."""

    blocked: List[List[object]]
    """
    Number of blocked request events, with the same keys and formatted the same as
    in the total field.
    """

    reference: Optional[Dict[str, Reference]] = None
    """Additional information, depending on the selected dimension.

    Keys refer to the items in the result (first value of a tuple).
    """

    suppressed: List[List[object]]
    """
    Number of requests observed in monitoring mode that would have been blocked
    otherwise.
    """

    total: List[List[object]]
    """Total number of observed requests.

    First element of the tuple is a key, the second one is its counter value. The
    key refers to a point in the requested dimension (e.g., an IP address). Results
    are ordered by the counter value in descending order.
    """
