# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TemplateParameterParam"]


class TemplateParameterParam(TypedDict, total=False):
    data_type: Required[Literal["string", "number", "date", "time", "secret"]]
    """Parameter type"""

    mandatory: Required[bool]
    """Is this field mandatory?"""

    name: Required[str]
    """Parameter name"""

    descr: str
    """Parameter description"""
