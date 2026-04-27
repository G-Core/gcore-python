# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ....._models import BaseModel

__all__ = ["PgConfValidation"]


class PgConfValidation(BaseModel):
    errors: List[str]
    """Errors list"""

    is_valid: bool
    """Validity of pg.conf file"""
