# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TemplateDeleteParams"]


class TemplateDeleteParams(TypedDict, total=False):
    force: bool
    """When true, deletes template even if shared with groups. Defaults to false."""
