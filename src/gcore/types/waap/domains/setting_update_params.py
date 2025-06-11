# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["SettingUpdateParams", "API", "DDOS"]


class SettingUpdateParams(TypedDict, total=False):
    api: API
    """Editable API settings of a domain"""

    ddos: DDOS
    """Editable DDoS settings for a domain."""


class API(TypedDict, total=False):
    api_urls: List[str]
    """The API URLs for a domain.

    If your domain has a common base URL for all API paths, it can be set here
    """

    is_api: bool
    """Indicates if the domain is an API domain.

    All requests to an API domain are treated as API requests. If this is set to
    true then the `api_urls` field is ignored.
    """


class DDOS(TypedDict, total=False):
    burst_threshold: int
    """The burst threshold detects sudden rises in traffic.

    If it is met and the number of requests is at least five times the last 2-second
    interval, DDoS protection will activate. Default is 1000.
    """

    global_threshold: int
    """
    The global threshold is responsible for identifying DDoS attacks with a slow
    rise in traffic. If the threshold is met and the current number of requests is
    at least double that of the previous 10-second window, DDoS protection will
    activate. Default is 5000.
    """
