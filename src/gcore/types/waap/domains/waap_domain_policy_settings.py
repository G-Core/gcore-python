# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["WaapDomainPolicySettings"]


class WaapDomainPolicySettings(BaseModel):
    """Configurable settings of a security rule (a.k.a. policy) on a domain."""

    mode: bool
    """Indicates if the security rule is active"""
