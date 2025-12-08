# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .tag_update_map_param import TagUpdateMapParam
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

    tags: Optional[TagUpdateMapParam]
    """Update key-value tags using JSON Merge Patch semantics (RFC 7386).

    Provide key-value pairs to add or update tags. Set tag values to `null` to
    remove tags. Unspecified tags remain unchanged. Read-only tags are always
    preserved and cannot be modified.

    **Examples:**

    - **Add/update tags:**
      `{'tags': {'environment': 'production', 'team': 'backend'}}` adds new tags or
      updates existing ones.

    - **Delete tags:** `{'tags': {'old_tag': null}}` removes specific tags.

    - **Remove all tags:** `{'tags': null}` removes all user-managed tags (read-only
      tags are preserved).

    - **Partial update:** `{'tags': {'environment': 'staging'}}` only updates
      specified tags.

    - **Mixed operations:**
      `{'tags': {'environment': 'production', 'cost_center': 'engineering', 'deprecated_tag': null}}`
      adds/updates 'environment' and '`cost_center`' while removing
      '`deprecated_tag`', preserving other existing tags.

    - **Replace all:** first delete existing tags with null values, then add new
      ones in the same request.
    """


class Logging(TypedDict, total=False):
    """Logging configuration"""

    destination_region_id: Optional[int]
    """Destination region id to which the logs will be written"""

    enabled: bool
    """Enable/disable forwarding logs to LaaS"""

    retention_policy: Optional[LaasIndexRetentionPolicyParam]
    """The logs retention policy"""

    topic_name: Optional[str]
    """The topic name to which the logs will be written"""
