# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .client_profile import ClientProfile

__all__ = ["ProfileListResponse"]

ProfileListResponse: TypeAlias = List[ClientProfile]
