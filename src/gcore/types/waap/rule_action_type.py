# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["RuleActionType"]

RuleActionType: TypeAlias = Literal["allow", "block", "captcha", "handshake", "monitor", "tag"]
