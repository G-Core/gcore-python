# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["WaapDomainAPISettings"]


class WaapDomainAPISettings(BaseModel):
    api_urls: Optional[List[str]] = None
    """The API URLs for a domain.

    If your domain has a common base URL for all API paths, it can be set here
    """

    is_api: Optional[bool] = None
    """Indicates if the domain is an API domain.

    All requests to an API domain are treated as API requests. If this is set to
    true then the `api_urls` field is ignored.
    """
