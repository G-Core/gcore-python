# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .api_token import APIToken

__all__ = ["APITokenCreated"]


class APITokenCreated(APIToken):
    token: Optional[str] = None
    """
    API token with `_` separator. Copy it, because you will not be able to get it
    again. We do not store tokens. All responsibility for token storage and usage is
    on the issuer.
    """
