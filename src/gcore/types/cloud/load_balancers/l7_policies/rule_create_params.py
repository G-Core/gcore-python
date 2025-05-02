# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["RuleCreateParams"]


class RuleCreateParams(TypedDict, total=False):
    project_id: int

    region_id: int

    compare_type: Required[Literal["CONTAINS", "ENDS_WITH", "EQUAL_TO", "REGEX", "STARTS_WITH"]]
    """The comparison type for the L7 rule"""

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
    """The L7 rule type"""

    value: Required[str]
    """The value to use for the comparison. For example, the file type to compare"""

    invert: bool
    """When true the logic of the rule is inverted.

    For example, with invert true, 'equal to' would become 'not equal to'. Default
    is false.
    """

    key: str
    """The key to use for the comparison.

    For example, the name of the cookie to evaluate.
    """

    tags: List[str]
    """A list of simple strings assigned to the l7 rule"""
