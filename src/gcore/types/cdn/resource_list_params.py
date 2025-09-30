# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ResourceListParams"]


class ResourceListParams(TypedDict, total=False):
    cname: str
    """Delivery domain (CNAME) of the CDN resource."""

    deleted: bool
    """Defines whether a CDN resource has been deleted.

    Possible values:

    - **true** - CDN resource has been deleted.
    - **false** - CDN resource has not been deleted.
    """

    enabled: bool
    """Enables or disables a CDN resource change by a user.

    Possible values:

    - **true** - CDN resource is enabled.
    - **false** - CDN resource is disabled.
    """

    max_created: str
    """
    Most recent date of CDN resource creation for which CDN resources should be
    returned (ISO 8601/RFC 3339 format, UTC.)
    """

    min_created: str
    """
    Earliest date of CDN resource creation for which CDN resources should be
    returned (ISO 8601/RFC 3339 format, UTC.)
    """

    origin_group: Annotated[int, PropertyInfo(alias="originGroup")]
    """Origin group ID."""

    rules: str
    """Rule name or pattern."""

    secondary_hostnames: Annotated[str, PropertyInfo(alias="secondaryHostnames")]
    """Additional delivery domains (CNAMEs) of the CDN resource."""

    shield_dc: str
    """Name of the origin shielding data center location."""

    shielded: bool
    """Defines whether origin shielding is enabled for the CDN resource.

    Possible values:

    - **true** - Origin shielding is enabled for the CDN resource.
    - **false** - Origin shielding is disabled for the CDN resource.
    """

    ssl_data: Annotated[int, PropertyInfo(alias="sslData")]
    """SSL certificate ID."""

    ssl_data_in: Annotated[int, PropertyInfo(alias="sslData_in")]
    """SSL certificates IDs.

    Example:

    - ?`sslData_in`=1643,1644,1652
    """

    ssl_enabled: Annotated[bool, PropertyInfo(alias="sslEnabled")]
    """Defines whether the HTTPS protocol is enabled for content delivery.

    Possible values:

    - **true** - HTTPS protocol is enabled for CDN resource.
    - **false** - HTTPS protocol is disabled for CDN resource.
    """

    status: Literal["active", "processed", "suspended", "deleted"]
    """CDN resource status."""

    suspend: bool
    """Defines whether the CDN resource was automatically suspended by the system.

    Possible values:

    - **true** - CDN resource is selected for automatic suspension in the next 7
      days.
    - **false** - CDN resource is not selected for automatic suspension.
    """

    vp_enabled: bool
    """Defines whether the CDN resource is integrated with the Streaming platform.

    Possible values:

    - **true** - CDN resource is used for Streaming platform.
    - **false** - CDN resource is not used for Streaming platform.
    """
