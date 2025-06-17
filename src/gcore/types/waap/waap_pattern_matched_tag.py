# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["WaapPatternMatchedTag"]


class WaapPatternMatchedTag(BaseModel):
    description: str
    """Tag description information"""

    display_name: str
    """The tag's display name"""

    execution_phase: str
    """
    The phase in which the tag was triggered: access -> Request, `header_filter` ->
    `response_header`, `body_filter` -> `response_body`
    """

    field: str
    """The entity to which the variable that triggered the tag belong to.

    For example: `request_headers`, uri, cookies etc.
    """

    field_name: str
    """The name of the variable which holds the value that triggered the tag"""

    pattern_name: str
    """The name of the detected regexp pattern"""

    pattern_value: str
    """The pattern which triggered the tag"""

    tag: str
    """Tag name"""
