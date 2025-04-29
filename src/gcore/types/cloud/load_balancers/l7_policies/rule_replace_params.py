# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["RuleReplaceParams"]


class RuleReplaceParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D%2Frules%2F%7Bl7rule_id%7D/put/parameters/0/schema'
    "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules/{l7rule_id}'].put.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D%2Frules%2F%7Bl7rule_id%7D/put/parameters/1/schema'
    "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules/{l7rule_id}'].put.parameters[1].schema"
    """

    l7policy_id: Required[str]
    """
    '#/paths/%2Fcloud%2Fv1%2Fl7policies%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bl7policy_id%7D%2Frules%2F%7Bl7rule_id%7D/put/parameters/2/schema'
    "$.paths['/cloud/v1/l7policies/{project_id}/{region_id}/{l7policy_id}/rules/{l7rule_id}'].put.parameters[2].schema"
    """

    compare_type: Literal["CONTAINS", "ENDS_WITH", "EQUAL_TO", "REGEX", "STARTS_WITH"]
    """
    '#/components/schemas/UpdateL7RuleSchema/properties/compare_type'
    "$.components.schemas.UpdateL7RuleSchema.properties.compare_type"
    """

    invert: bool
    """
    '#/components/schemas/UpdateL7RuleSchema/properties/invert'
    "$.components.schemas.UpdateL7RuleSchema.properties.invert"
    """

    key: str
    """
    '#/components/schemas/UpdateL7RuleSchema/properties/key'
    "$.components.schemas.UpdateL7RuleSchema.properties.key"
    """

    tags: List[str]
    """
    '#/components/schemas/UpdateL7RuleSchema/properties/tags'
    "$.components.schemas.UpdateL7RuleSchema.properties.tags"
    """

    type: Literal[
        "COOKIE", "FILE_TYPE", "HEADER", "HOST_NAME", "PATH", "SSL_CONN_HAS_CERT", "SSL_DN_FIELD", "SSL_VERIFY_RESULT"
    ]
    """
    '#/components/schemas/UpdateL7RuleSchema/properties/type'
    "$.components.schemas.UpdateL7RuleSchema.properties.type"
    """

    value: str
    """
    '#/components/schemas/UpdateL7RuleSchema/properties/value'
    "$.components.schemas.UpdateL7RuleSchema.properties.value"
    """
