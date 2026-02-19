# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["AuthType"]

AuthType: TypeAlias = Literal["password", "sso", "github", "google-oauth2"]
