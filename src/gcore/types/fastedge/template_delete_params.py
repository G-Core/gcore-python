# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TemplateDeleteParams"]


class TemplateDeleteParams(TypedDict, total=False):
    force: bool
    """Force template deletion even if it is shared to groups"""
