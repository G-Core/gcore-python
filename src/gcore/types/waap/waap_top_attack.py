# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["WaapTopAttack"]


class WaapTopAttack(BaseModel):
    attack_type: str
    """The attack type (rule name)"""

    attacks: int
    """Total number of attack requests (blocked + monitored)"""

    blocked: int
    """Number of blocked attack requests"""

    domains: Optional[List[str]] = None
    """Full list of domains where this attack type was seen"""

    paths: Optional[List[str]] = None
    """Full list of paths where this attack type was seen"""
