# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["WaapPolicyMode"]


class WaapPolicyMode(BaseModel):
    """Represents the mode of a security rule."""

    mode: bool
    """Indicates if the security rule is active"""
