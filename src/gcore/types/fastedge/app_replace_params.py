# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .app_param import AppParam

__all__ = ["AppReplaceParams", "Body"]


class AppReplaceParams(TypedDict, total=False):
    body: Body


class Body(AppParam, total=False):
    pass
