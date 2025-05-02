# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .laas_index_retention_policy_param import LaasIndexRetentionPolicyParam
from .load_balancer_member_connectivity import LoadBalancerMemberConnectivity

__all__ = ["LoadBalancerUpdateParams", "Logging"]


class LoadBalancerUpdateParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bloadbalancer_id%7D/patch/parameters/0/schema'
    "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}'].patch.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bloadbalancer_id%7D/patch/parameters/1/schema'
    "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}'].patch.parameters[1].schema"
    """

    logging: Logging
    """
    '#/components/schemas/LoadBalancerPatchSerializer/properties/logging'
    "$.components.schemas.LoadBalancerPatchSerializer.properties.logging"
    """

    name: str
    """
    '#/components/schemas/LoadBalancerPatchSerializer/properties/name'
    "$.components.schemas.LoadBalancerPatchSerializer.properties.name"
    """

    preferred_connectivity: LoadBalancerMemberConnectivity
    """
    '#/components/schemas/LoadBalancerPatchSerializer/properties/preferred_connectivity'
    "$.components.schemas.LoadBalancerPatchSerializer.properties.preferred_connectivity"
    """


class Logging(TypedDict, total=False):
    destination_region_id: Optional[int]
    """
    '#/components/schemas/LoadbalancerLoggingSerializer/properties/destination_region_id/anyOf/0'
    "$.components.schemas.LoadbalancerLoggingSerializer.properties.destination_region_id.anyOf[0]"
    """

    enabled: bool
    """
    '#/components/schemas/LoadbalancerLoggingSerializer/properties/enabled'
    "$.components.schemas.LoadbalancerLoggingSerializer.properties.enabled"
    """

    retention_policy: Optional[LaasIndexRetentionPolicyParam]
    """
    '#/components/schemas/LoadbalancerLoggingSerializer/properties/retention_policy/anyOf/0'
    "$.components.schemas.LoadbalancerLoggingSerializer.properties.retention_policy.anyOf[0]"
    """

    topic_name: Optional[str]
    """
    '#/components/schemas/LoadbalancerLoggingSerializer/properties/topic_name/anyOf/0'
    "$.components.schemas.LoadbalancerLoggingSerializer.properties.topic_name.anyOf[0]"
    """
