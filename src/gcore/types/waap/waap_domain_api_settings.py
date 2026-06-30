# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["WaapDomainAPISettings"]


class WaapDomainAPISettings(BaseModel):
    """API settings of a domain"""

    api_urls: Optional[List[str]] = None
    """The API base paths for a domain.

    If your domain has a common base path for all API endpoints, it can be set here.
    When set or updated, each entry must contain at least one letter or digit; a
    value that would match the whole domain (such as "/") is rejected - to treat the
    entire domain as an API domain, use the `is_api` field instead.
    """

    is_api: Optional[bool] = None
    """Indicates if the domain is an API domain.

    All requests to an API domain are treated as API requests. If this is set to
    true then the `api_urls` field is ignored.
    """
