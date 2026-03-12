# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .template_parameter_param import TemplateParameterParam

__all__ = ["TemplateCreateParams"]


class TemplateCreateParams(TypedDict, total=False):
    binary_id: Required[int]
    """ID of the WebAssembly binary to use for this template"""

    name: Required[str]
    """Unique name for the template (used for identification and searching)"""

    owned: Required[bool]
    """Is the template owned by user?"""

    params: Required[Iterable[TemplateParameterParam]]
    """Parameters"""

    long_descr: str
    """Detailed markdown description explaining template features and usage"""

    short_descr: str
    """Brief one-line description displayed in template listings"""
