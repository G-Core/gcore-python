# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["AnalyticsGetRequestsParams"]


class AnalyticsGetRequestsParams(TypedDict, total=False):
    start: Required[str]
    """Filter data items starting from a specified date in ISO 8601 format"""

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

    exclude_decision: List[Literal["blocked", "monitored", "allowed", "passed"]]
    """Exclude entries that match any of the given decisions."""

    exclude_domains: Iterable[int]
    """Exclude data by domain ID."""

    exclude_http_methods: List[Literal["DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT", "TRACE"]]
    """Exclude entries with any of the given HTTP methods."""

    exclude_ips: SequenceNotStr[str]
    """Exclude traffic data by client IP."""

    exclude_ja3: SequenceNotStr[str]
    """
    Exclude entries whose JA3 TLS client fingerprint matches any of the supplied
    values. Each value must be exactly 32 hexadecimal characters (mixed case
    allowed) and is case-folded to lowercase when the backend filter is built.
    Supply multiple values to exclude any of them. Omit the parameter to apply no
    JA3 exclusion.
    """

    exclude_ja4: SequenceNotStr[str]
    """
    Exclude entries whose JA4 TLS client fingerprint equals any of the supplied
    values. An item must match the JA4 form `<ja4_a>_<ja4_b>_<ja4_c>` (a
    10-character prefix and two 12-character hexadecimal hashes, mixed case allowed)
    and is case-folded to lowercase when the backend filter is built. Omit the
    parameter to apply no JA4 exclusion.
    """

    exclude_optional_action: List[Literal["captcha", "challenge"]]
    """Exclude entries that match any of the given optional action values."""

    exclude_organizations: SequenceNotStr[str]
    """Exclude entries whose organization exactly equals any supplied value.

    Omit or provide an empty list to apply no organization exclusion.
    """

    exclude_path: SequenceNotStr[str]
    """Exclude entries that match the given URL path pattern; '\\**' is wildcard."""

    exclude_reference_ids: SequenceNotStr[str]
    """Exclude data by reference IDs."""

    exclude_request_ids: SequenceNotStr[str]
    """Exclude data by request IDs."""

    exclude_security_rule_names: SequenceNotStr[str]
    """Exclude data by name of a security rule matched the request."""

    exclude_session_ids: SequenceNotStr[str]
    """Exclude data by session IDs."""

    exclude_status_codes: Iterable[int]
    """Exclude entries with any of the given HTTP response status codes."""

    exclude_tags: SequenceNotStr[str]
    """Exclude entries whose tag exactly equals any supplied value.

    Omit or provide an empty list to apply no tag exclusion.
    """

    exclude_user_agent: SequenceNotStr[str]
    """
    Exclude entries whose user agent contains any of the supplied texts,
    case-insensitive partial match. Omit or provide an empty list to apply no user
    agent text exclusion.
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

    ja3: SequenceNotStr[str]
    """Filter by JA3 TLS client fingerprint.

    Each value must be exactly 32 hexadecimal characters (mixed case allowed) and is
    case-folded to lowercase when the backend filter is built. Supply multiple
    values to match any of them. Omit the parameter to apply no JA3 filter.
    """

    ja4: SequenceNotStr[str]
    """Filter by JA4 TLS client fingerprint.

    When present, the value must match the JA4 form `<ja4_a>_<ja4_b>_<ja4_c>` (a
    10-character prefix and two 12-character hexadecimal hashes, mixed case allowed)
    and is case-folded to lowercase when the backend filter is built. Supply
    multiple values to match any of them. Omit the parameter entirely to apply no
    JA4 filter.
    """

    limit: int
    """Number of items to return"""

    offset: int
    """Number of items to skip"""

    optional_action: List[Literal["captcha", "challenge"]]
    """Filter data by optional action."""

    ordering: str
    """Results sorting order."""

    organizations: SequenceNotStr[str]
    """Include entries whose organization exactly equals any supplied value.

    Omit or provide an empty list to apply no organization filter.
    """

    path: SequenceNotStr[str]
    """Filter by URL path. '\\**' is wildcard."""

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

    user_agent: SequenceNotStr[str]
    """
    Include entries whose user agent contains any of the supplied texts,
    case-insensitive partial match. Omit or provide an empty list to apply no user
    agent text filter.
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
