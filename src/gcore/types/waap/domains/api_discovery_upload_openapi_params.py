# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["APIDiscoveryUploadOpenAPIParams"]


class APIDiscoveryUploadOpenAPIParams(TypedDict, total=False):
    file_data: Required[str]
    """Base64 representation of the description file.

    Supported formats are YAML and JSON, and it must adhere to OpenAPI versions 2,
    3, or 3.1.
    """

    file_name: Required[str]
    """The name of the file"""
