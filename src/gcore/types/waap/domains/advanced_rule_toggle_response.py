# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["AdvancedRuleToggleResponse"]


class AdvancedRuleToggleResponse(BaseModel):
    enabled: bool
    """Rule enabled status after operation"""
