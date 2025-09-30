# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PurgeStatus", "Resource"]


class Resource(BaseModel):
    id: Optional[int] = None
    """Resource ID."""

    cname: Optional[str] = None
    """CNAME of the resource."""


class PurgeStatus(BaseModel):
    created: Optional[str] = None
    """Date and time when the purge was created (ISO 8601/RFC 3339 format, UTC)."""

    payload: Optional[object] = None
    """Purge payload depends on purge type.

    Possible values:

    - **urls** - Purge by URL.
    - **paths** - Purge by Pattern and purge All.
    """

    purge_id: Optional[int] = None
    """Purge ID."""

    purge_type: Optional[str] = None
    """Contains the name of the purge request type.

    Possible values:

    - **`purge_by_pattern`** - Purge by Pattern.
    - **`purge_by_url`** - Purge by URL.
    - **`purge_all`** - Purge All.
    """

    resource: Optional[Resource] = None

    status: Optional[Literal["In progress", "Successful", "Failed"]] = None
    """Purge status.

    Possible values:

    - **In progress** - Purge is in progress.
    - **Successful** - Purge was successful.
    - **Failed** - Purge failed.
    """
