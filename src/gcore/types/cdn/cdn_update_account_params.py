# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CdnUpdateAccountParams"]


class CdnUpdateAccountParams(TypedDict, total=False):
    utilization_level: int
    """CDN traffic usage limit in gigabytes.

    When the limit is reached, we will send an email notification.
    """
