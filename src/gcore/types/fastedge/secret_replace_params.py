# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .secret_param import SecretParam

__all__ = ["SecretReplaceParams", "Body"]


class SecretReplaceParams(TypedDict, total=False):
    body: Required[Body]


class Body(SecretParam, total=False):
    pass
