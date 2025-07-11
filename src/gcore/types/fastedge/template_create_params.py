# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .template_parameter_param import TemplateParameterParam

__all__ = ["TemplateCreateParams"]


class TemplateCreateParams(TypedDict, total=False):
    binary_id: Required[int]
    """Binary ID"""

    name: Required[str]
    """Name of the template"""

    owned: Required[bool]
    """Is the template owned by user?"""

    params: Required[Iterable[TemplateParameterParam]]
    """Parameters"""

    long_descr: str
    """Long description of the template"""

    short_descr: str
    """Short description of the template"""
