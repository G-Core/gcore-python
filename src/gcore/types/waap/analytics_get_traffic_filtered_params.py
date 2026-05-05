# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["AnalyticsGetTrafficFilteredParams"]


class AnalyticsGetTrafficFilteredParams(TypedDict, total=False):
    resolution: Required[Literal["daily", "hourly", "minutely"]]
    """Specifies the granularity of the result data."""

    start: Required[str]
    """Filter data items starting from a specified date in ISO 8601 format"""

    bucket_size: Optional[Literal[60, 300, 600, 900, 1800, 3600, 7200, 10800, 21600, 43200, 86400]]
    """Optional explicit aggregation bucket width in seconds.

    When supplied, `bucket_size` supersedes `resolution` for aggregation
    granularity.
    """

    countries: SequenceNotStr[str]
    """
    Filter data by a country code of the originating IP address in ISO 3166-1
    alpha-2 format.
    """

    decision: List[Literal["blocked", "monitored", "allowed", "passed"]]
    """Filter data by decision."""

    domains: Iterable[int]
    """List of domain IDs.

    Empty list means all domains belonging to the current account.
    """

    end: Optional[str]
    """Filter data items up to a specified end date in ISO 8601 format.

    If not provided, defaults to the current date and time.
    """

    exclude_countries: SequenceNotStr[str]
    """
    Exclude data by a country code of the originating IP address in ISO 3166-1
    alpha-2 format.
    """

    exclude_domains: Iterable[int]
    """Exclude data by domain ID."""

    exclude_ips: SequenceNotStr[str]
    """Exclude traffic data by client IP."""

    exclude_ja3: Optional[str]
    """Exclude entries whose JA3 TLS client fingerprint equals the supplied value.

    Must be exactly 32 hexadecimal characters (mixed case allowed) and is
    case-folded to lowercase when the backend filter is built. Omit the parameter to
    apply no JA3 exclusion.
    """

    exclude_organizations: SequenceNotStr[str]
    """Exclude entries whose organization exactly equals any supplied value.

    Omit or provide an empty list to apply no organization exclusion.
    """

    exclude_reference_ids: SequenceNotStr[str]
    """Exclude data by reference IDs."""

    exclude_security_rule_names: SequenceNotStr[str]
    """Exclude data by name of a security rule matched the request."""

    exclude_session_ids: SequenceNotStr[str]
    """Exclude data by session IDs."""

    exclude_tags: SequenceNotStr[str]
    """Exclude entries whose tag exactly equals any supplied value.

    Omit or provide an empty list to apply no tag exclusion.
    """

    exclude_user_agent: Optional[str]
    """
    Exclude entries whose user agent contains the supplied text, case-insensitive
    partial match. Omit the parameter to apply no user agent text exclusion.
    """

    exclude_user_agent_clients: SequenceNotStr[str]
    """Exclude entries whose parsed user agent client exactly equals any supplied
    value.

    Omit or provide an empty list to apply no user agent client exclusion.
    """

    exclude_user_agent_devices: SequenceNotStr[str]
    """Exclude entries whose parsed user agent device exactly equals any supplied
    value.

    Omit or provide an empty list to apply no user agent device exclusion.
    """

    http_methods: List[Literal["DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT", "TRACE"]]
    """Filter by HTTP methods"""

    ips: SequenceNotStr[str]
    """Filter traffic data by client IP."""

    ja3: Optional[str]
    """Filter by JA3 TLS client fingerprint.

    When present, the value must be exactly 32 hexadecimal characters (mixed case
    allowed) and is case-folded to lowercase when the backend filter is built. Omit
    the parameter entirely to apply no JA3 filter.
    """

    optional_action: List[Literal["captcha", "challenge"]]
    """Filter data by optional action."""

    organizations: SequenceNotStr[str]
    """Include entries whose organization exactly equals any supplied value.

    Omit or provide an empty list to apply no organization filter.
    """

    path: Optional[str]
    """Filter by URL path with a glob-like pattern."""

    reference_ids: SequenceNotStr[str]
    """Filter data by reference IDs."""

    request_ids: SequenceNotStr[str]
    """Filter data by request IDs."""

    security_rule_names: SequenceNotStr[str]
    """Filter data by name of a security rule matched the request."""

    session_ids: SequenceNotStr[str]
    """Filter data by session IDs."""

    status_codes: Iterable[int]
    """Filter data by HTTP response status code."""

    tags: SequenceNotStr[str]
    """Include entries whose tag exactly equals any supplied value.

    Omit or provide an empty list to apply no tag filter.
    """

    user_agent: Optional[str]
    """
    Include entries whose user agent contains the supplied text, case-insensitive
    partial match. Omit the parameter to apply no user agent text filter.
    """

    user_agent_clients: SequenceNotStr[str]
    """Include entries whose parsed user agent client exactly equals any supplied
    value.

    Omit or provide an empty list to apply no user agent client filter.
    """

    user_agent_devices: SequenceNotStr[str]
    """Include entries whose parsed user agent device exactly equals any supplied
    value.

    Omit or provide an empty list to apply no user agent device filter.
    """
