# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo
from ...http_method import HTTPMethod
from ...health_monitor_type import HealthMonitorType

__all__ = ["HealthMonitorCreateParams"]


class HealthMonitorCreateParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bpool_id%7D%2Fhealthmonitor/post/parameters/0/schema'
    "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}/healthmonitor'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bpool_id%7D%2Fhealthmonitor/post/parameters/1/schema'
    "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}/healthmonitor'].post.parameters[1].schema"
    """

    delay: Required[int]
    """
    '#/components/schemas/CreateLbHealthMonitorSerializer/properties/delay'
    "$.components.schemas.CreateLbHealthMonitorSerializer.properties.delay"
    """

    max_retries: Required[int]
    """
    '#/components/schemas/CreateLbHealthMonitorSerializer/properties/max_retries'
    "$.components.schemas.CreateLbHealthMonitorSerializer.properties.max_retries"
    """

    api_timeout: Required[Annotated[int, PropertyInfo(alias="timeout")]]
    """
    '#/components/schemas/CreateLbHealthMonitorSerializer/properties/timeout'
    "$.components.schemas.CreateLbHealthMonitorSerializer.properties.timeout"
    """

    type: Required[HealthMonitorType]
    """
    '#/components/schemas/CreateLbHealthMonitorSerializer/properties/type'
    "$.components.schemas.CreateLbHealthMonitorSerializer.properties.type"
    """

    expected_codes: Optional[str]
    """
    '#/components/schemas/CreateLbHealthMonitorSerializer/properties/expected_codes/anyOf/0'
    "$.components.schemas.CreateLbHealthMonitorSerializer.properties.expected_codes.anyOf[0]"
    """

    http_method: Optional[HTTPMethod]
    """
    '#/components/schemas/CreateLbHealthMonitorSerializer/properties/http_method/anyOf/0'
    "$.components.schemas.CreateLbHealthMonitorSerializer.properties.http_method.anyOf[0]"
    """

    max_retries_down: Optional[int]
    """
    '#/components/schemas/CreateLbHealthMonitorSerializer/properties/max_retries_down/anyOf/0'
    "$.components.schemas.CreateLbHealthMonitorSerializer.properties.max_retries_down.anyOf[0]"
    """

    url_path: Optional[str]
    """
    '#/components/schemas/CreateLbHealthMonitorSerializer/properties/url_path/anyOf/0'
    "$.components.schemas.CreateLbHealthMonitorSerializer.properties.url_path.anyOf[0]"
    """
