# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["CdnAccount", "Service"]


class Service(BaseModel):
    """Information about the CDN service status."""

    enabled: Optional[bool] = None
    """Defines whether the CDN service is activated.

    Possible values:

    - **true** - Service is activated.
    - **false** - Service is not activated.
    """

    status: Optional[str] = None
    """CDN service status.

    Possible values:

    - **new** - CDN service is not activated.
    - **trial** - Free trial is in progress.
    - **trialend** - Free trial has ended and CDN service is stopped. All CDN
      resources are suspended.
    - **activating** - CDN service is being activated. It can take up to 15 minutes.
    - **active** - CDN service is active.
    - **paused** - CDN service is stopped. All CDN resources are suspended.
    - **deleted** - CDN service is stopped. All CDN resources are deleted.
    """

    updated: Optional[str] = None
    """Date of the last CDN service status update (ISO 8601/RFC 3339 format, UTC.)"""


class CdnAccount(BaseModel):
    id: Optional[int] = None
    """Account ID."""

    auto_suspend_enabled: Optional[bool] = None
    """Defines whether resources will be deactivated automatically by inactivity.

    Possible values:

    - **true** - Resources will be deactivated.
    - **false** - Resources will not be deactivated.
    """

    cdn_resources_rules_max_count: Optional[int] = None
    """Limit on the number of rules for each CDN resource."""

    cname: Optional[str] = None
    """Domain zone to which a CNAME record of your CDN resources should be pointed."""

    created: Optional[str] = None
    """
    Date of the first synchronization with the Platform (ISO 8601/RFC 3339 format,
    UTC.)
    """

    service: Optional[Service] = None
    """Information about the CDN service status."""

    updated: Optional[str] = None
    """
    Date of the last update of information about CDN service (ISO 8601/RFC 3339
    format, UTC.)
    """

    use_balancer: Optional[bool] = None
    """Defines whether custom balancing is used for content delivery.

    Possible values:

    - **true** - Custom balancing is used for content delivery.
    - **false** - Custom balancing is not used for content delivery.
    """

    utilization_level: Optional[int] = None
    """CDN traffic usage limit in gigabytes.

    When the limit is reached, we will send an email notification.
    """
