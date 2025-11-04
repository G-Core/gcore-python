# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ......_models import BaseModel

__all__ = ["PostgresUserCredentials"]


class PostgresUserCredentials(BaseModel):
    password: str
    """Password"""

    username: str
    """Username"""
