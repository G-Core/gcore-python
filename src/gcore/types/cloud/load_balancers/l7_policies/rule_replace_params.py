# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ....._types import SequenceNotStr

__all__ = ["RuleReplaceParams"]


class RuleReplaceParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    l7policy_id: Required[str]
    """L7 policy ID"""

    compare_type: Required[Literal["CONTAINS", "ENDS_WITH", "EQUAL_TO", "REGEX", "STARTS_WITH"]]
    """The comparison type for the L7 rule"""

    invert: bool
    """When true the logic of the rule is inverted."""

    key: str
    """The key to use for the comparison. Required for COOKIE and HEADER `type` only."""

    tags: SequenceNotStr[str]
    """A list of simple strings assigned to the l7 rule"""

    type: Literal[
        "COOKIE", "FILE_TYPE", "HEADER", "HOST_NAME", "PATH", "SSL_CONN_HAS_CERT", "SSL_DN_FIELD", "SSL_VERIFY_RESULT"
    ]
    """The L7 rule type"""

    value: str
    """The value to use for the comparison"""
