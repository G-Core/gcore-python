# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["LoadBalancerFailoverParams"]


class LoadBalancerFailoverParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bloadbalancer_id%7D%2Ffailover/post/parameters/0/schema'
    "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}/failover'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bloadbalancer_id%7D%2Ffailover/post/parameters/1/schema'
    "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}/failover'].post.parameters[1].schema"
    """

    force: bool
    """
    '#/components/schemas/FailoverLoadBalancer/properties/force'
    "$.components.schemas.FailoverLoadBalancer.properties.force"
    """
