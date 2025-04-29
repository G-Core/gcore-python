# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["RuleCreateParams"]


class RuleCreateParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D%2Frules/post/parameters/0/schema'
    "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D%2Frules/post/parameters/1/schema'
    "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules'].post.parameters[1].schema"
    """

    compare_type: Required[Literal["CONTAINS", "ENDS_WITH", "EQUAL_TO", "REGEX", "STARTS_WITH"]]
    """
    '#/components/schemas/CreateL7RuleSchema/properties/compare_type'
    "$.components.schemas.CreateL7RuleSchema.properties.compare_type"
    """

    type: Required[
        Literal[
            "COOKIE",
            "FILE_TYPE",
            "HEADER",
            "HOST_NAME",
            "PATH",
            "SSL_CONN_HAS_CERT",
            "SSL_DN_FIELD",
            "SSL_VERIFY_RESULT",
        ]
    ]
    """
    '#/components/schemas/CreateL7RuleSchema/properties/type'
    "$.components.schemas.CreateL7RuleSchema.properties.type"
    """

    value: Required[str]
    """
    '#/components/schemas/CreateL7RuleSchema/properties/value'
    "$.components.schemas.CreateL7RuleSchema.properties.value"
    """

    invert: bool
    """
    '#/components/schemas/CreateL7RuleSchema/properties/invert'
    "$.components.schemas.CreateL7RuleSchema.properties.invert"
    """

    key: str
    """
    '#/components/schemas/CreateL7RuleSchema/properties/key'
    "$.components.schemas.CreateL7RuleSchema.properties.key"
    """

    tags: List[str]
    """
    '#/components/schemas/CreateL7RuleSchema/properties/tags'
    "$.components.schemas.CreateL7RuleSchema.properties.tags"
    """
