# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["CertificateGetStatusParams"]


class CertificateGetStatusParams(TypedDict, total=False):
    exclude: SequenceNotStr[str]
    """Listed fields will be excluded from the response."""
