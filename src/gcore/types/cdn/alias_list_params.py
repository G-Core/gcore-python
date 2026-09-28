# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AliasListParams"]


class AliasListParams(TypedDict, total=False):
    automated: bool
    """How the alias certificate is managed.

    Possible values:

    - **true** – Certificate is issued and renewed automatically.
    - **false** – Certificate was added by a user.
    """

    cname: str
    """Hostname substring, case-insensitive."""

    cname_endswith: str
    """Hostname suffix, case-insensitive."""

    cname_startswith: str
    """Hostname prefix, case-insensitive."""

    limit: int
    """Maximum number of items to return in the response. Cannot exceed 1000."""

    offset: int
    """Number of items to skip from the beginning of the list."""

    ordering: str
    """Field to sort by. Prefix with `-` for descending order.

    Possible values: `id`, `cname`, `status`, `created`, `updated`, `resource_id`.
    """

    resource_id: int
    """CDN resource ID. Only aliases of this CDN resource are returned."""

    resource_id_in: Annotated[str, PropertyInfo(alias="resource_id__in")]
    """Comma-separated list of CDN resource IDs."""

    search: str
    """Search by alias ID or hostname."""

    ssl_id: int
    """SSL certificate ID. Only aliases linked to this certificate are returned."""

    ssl_status: Optional[Literal["pending", "issued", "failed"]]
    """Certificate outcome."""

    ssl_status_in: Annotated[str, PropertyInfo(alias="ssl_status__in")]
    """Comma-separated list of certificate outcomes."""

    ssl_validity_not_after_gte: str
    """
    Only aliases whose served certificate expires at or after this date and time
    (ISO 8601/RFC 3339 format, UTC).
    """

    ssl_validity_not_after_lte: str
    """
    Only aliases whose served certificate expires at or before this date and time
    (ISO 8601/RFC 3339 format, UTC).
    """

    status: Literal["pending", "active", "ssl_issuing", "ssl_error", "inactive"]
    """Alias status."""

    status_in: Annotated[str, PropertyInfo(alias="status__in")]
    """Comma-separated list of alias statuses."""
