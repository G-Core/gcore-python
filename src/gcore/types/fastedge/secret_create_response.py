# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .secret import Secret

__all__ = ["SecretCreateResponse"]


class SecretCreateResponse(Secret):
    id: Optional[int] = None
    """The unique identifier of the secret."""
