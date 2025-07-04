# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["APITokenCreate"]


class APITokenCreate(BaseModel):
    token: Optional[str] = None
    """
    API token. Copy it, because you will not be able to get it again. We do not
    store tokens. All responsibility for token storage and usage is on the issuer.
    """
