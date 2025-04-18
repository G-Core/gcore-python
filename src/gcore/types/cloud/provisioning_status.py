# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["ProvisioningStatus"]

ProvisioningStatus: TypeAlias = Literal[
    "ACTIVE", "DELETED", "ERROR", "PENDING_CREATE", "PENDING_DELETE", "PENDING_UPDATE"
]
