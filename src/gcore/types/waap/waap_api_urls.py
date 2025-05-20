# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["WaapAPIURLs"]


class WaapAPIURLs(BaseModel):
    api_urls: Optional[List[str]] = None
    """The API URLs for a domain.

    If your domain has a common base URL for all API paths, it can be set here
    """
