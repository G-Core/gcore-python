# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LoadBalancerResizeParams"]


class LoadBalancerResizeParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bloadbalancer_id%7D%2Fresize/post/parameters/0/schema'
    "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}/resize'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bloadbalancer_id%7D%2Fresize/post/parameters/1/schema'
    "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}/{loadbalancer_id}/resize'].post.parameters[1].schema"
    """

    flavor: Required[str]
    """
    '#/components/schemas/ResizeLoadBalancer/properties/flavor'
    "$.components.schemas.ResizeLoadBalancer.properties.flavor"
    """
