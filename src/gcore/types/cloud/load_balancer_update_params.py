# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .laas_index_retention_policy_param import LaasIndexRetentionPolicyParam
from .load_balancer_member_connectivity import LoadBalancerMemberConnectivity

__all__ = ["LoadBalancerUpdateParams", "Logging"]


class LoadBalancerUpdateParams(TypedDict, total=False):
    project_id: int

    region_id: int

    logging: Logging
    """Logging configuration"""

    name: str
    """Name."""

    preferred_connectivity: LoadBalancerMemberConnectivity
    """
    Preferred option to establish connectivity between load balancer and its pools
    members
    """


class Logging(TypedDict, total=False):
    destination_region_id: Optional[int]
    """Destination region id to which the logs will be written"""

    enabled: bool
    """Enable/disable forwarding logs to LaaS"""

    retention_policy: Optional[LaasIndexRetentionPolicyParam]
    """The logs retention policy"""

    topic_name: Optional[str]
    """The topic name to which the logs will be written"""
