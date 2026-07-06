# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncOffsetPage, AsyncOffsetPage
from ...types.waap import (
    analytics_get_filters_params,
    analytics_get_traffic_params,
    analytics_get_requests_params,
    analytics_get_event_statistics_params,
    analytics_get_traffic_filtered_params,
)
from ..._base_client import AsyncPaginator, make_request_options
from ...types.waap.waap_request_summary import WaapRequestSummary
from ...types.waap.waap_simple_event_statistics import WaapSimpleEventStatistics
from ...types.waap.analytics_get_filters_response import AnalyticsGetFiltersResponse
from ...types.waap.analytics_get_traffic_response import AnalyticsGetTrafficResponse
from ...types.waap.analytics_get_traffic_filtered_response import AnalyticsGetTrafficFilteredResponse

__all__ = ["AnalyticsResource", "AsyncAnalyticsResource"]


class AnalyticsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AnalyticsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AnalyticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnalyticsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AnalyticsResourceWithStreamingResponse(self)

    def get_event_statistics(
        self,
        dimension: Literal["country", "rule", "org", "ip", "useragent", "target"],
        *,
        start: str,
        domains: Iterable[int] | Omit = omit,
        end: Optional[str] | Omit = omit,
        ips: SequenceNotStr[str] | Omit = omit,
        order_by: Literal["total.desc", "threats.desc"] | Omit = omit,
        security_rule_names: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapSimpleEventStatistics:
        """Retrieves event statistics per given dimension of a request characteristics.

        A
        WAAP _Event_ represents a request observed by the system. The report contains
        the total, blocked, suppressed, and allowed event counts for top ten points in
        the selected dimension.

        Args:
          dimension: A request characteristics dimension

          start: Filter data items starting from a specified date in ISO 8601 format

          domains: List of domain IDs. Empty list means all domains belonging to the current
              account.

          end: Filter data items up to a specified end date in ISO 8601 format. If not
              provided, defaults to the current date and time.

          ips: Filter statistics by client IP addresses (max 10).

          order_by: Ordering applied to the ranked points within the dimension. `total.desc` ranks
              by total event count descending; `threats.desc` ranks by threat (blocked and
              monitored) event count descending.

          security_rule_names: Filter data by name of a security rule matched the request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dimension:
            raise ValueError(f"Expected a non-empty value for `dimension` but received {dimension!r}")
        return self._get(
            path_template("/waap/v1/analytics/stats/{dimension}", dimension=dimension),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "start": start,
                        "domains": domains,
                        "end": end,
                        "ips": ips,
                        "order_by": order_by,
                        "security_rule_names": security_rule_names,
                    },
                    analytics_get_event_statistics_params.AnalyticsGetEventStatisticsParams,
                ),
            ),
            cast_to=WaapSimpleEventStatistics,
        )

    def get_filters(
        self,
        type: Literal["user-agent-clients", "user-agent-devices", "organizations"],
        *,
        start: str,
        domains: Iterable[int] | Omit = omit,
        end: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        name: Optional[str] | Omit = omit,
        offset: int | Omit = omit,
        ordering: Literal["count", "value"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[AnalyticsGetFiltersResponse]:
        """
        Retrieves autocomplete suggestions for specified filter parameter values
        observed within the current client account during the requested time range. Use
        the returned `value` in the filter parameters of an analytics data request
        ([GET /v1/analytics/requests](/docs/api-reference/waap/analytics/get-request-log-data)
        and
        [GET /v1/analytics/traffic-filtered](/docs/api-reference/waap/analytics/get-filtered-traffic-data)).
        `count` reports how many times the value was observed in the requested range.

        Args:
          type: Parsed user-agent field type.

          start: Filter data items starting from a specified date in ISO 8601 format

          domains: List of domain IDs. Empty list means all domains belonging to the current
              account.

          end: Filter data items up to a specified end date in ISO 8601 format. If not
              provided, defaults to the current date and time.

          limit: Number of items to return

          name: Case-insensitive partial autocomplete pattern matched against the value name by
              the value provider. Must be between 2 and 100 characters; empty or omitted
              returns the available suggestions for the current account and time range.

          offset: Number of items to skip

          ordering: Suggestion ordering. `count` sorts by observed occurrence count descending (most
              frequent first) with value as a tie breaker; `value` sorts alphabetically by
              value ascending with count as a tie breaker.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not type:
            raise ValueError(f"Expected a non-empty value for `type` but received {type!r}")
        return self._get_api_list(
            path_template("/waap/v1/analytics/filters/{type}", type=type),
            page=SyncOffsetPage[AnalyticsGetFiltersResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "start": start,
                        "domains": domains,
                        "end": end,
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "ordering": ordering,
                    },
                    analytics_get_filters_params.AnalyticsGetFiltersParams,
                ),
            ),
            model=AnalyticsGetFiltersResponse,
        )

    def get_requests(
        self,
        *,
        start: str,
        countries: SequenceNotStr[str] | Omit = omit,
        decision: List[Literal["blocked", "monitored", "allowed", "passed"]] | Omit = omit,
        domains: Iterable[int] | Omit = omit,
        end: Optional[str] | Omit = omit,
        exclude_countries: SequenceNotStr[str] | Omit = omit,
        exclude_decision: List[Literal["blocked", "monitored", "allowed", "passed"]] | Omit = omit,
        exclude_domains: Iterable[int] | Omit = omit,
        exclude_http_methods: List[Literal["DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT", "TRACE"]]
        | Omit = omit,
        exclude_ips: SequenceNotStr[str] | Omit = omit,
        exclude_ja3: SequenceNotStr[str] | Omit = omit,
        exclude_ja4: SequenceNotStr[str] | Omit = omit,
        exclude_optional_action: List[Literal["captcha", "challenge"]] | Omit = omit,
        exclude_organizations: SequenceNotStr[str] | Omit = omit,
        exclude_path: SequenceNotStr[str] | Omit = omit,
        exclude_reference_ids: SequenceNotStr[str] | Omit = omit,
        exclude_request_ids: SequenceNotStr[str] | Omit = omit,
        exclude_security_rule_names: SequenceNotStr[str] | Omit = omit,
        exclude_session_ids: SequenceNotStr[str] | Omit = omit,
        exclude_status_codes: Iterable[int] | Omit = omit,
        exclude_tags: SequenceNotStr[str] | Omit = omit,
        exclude_user_agent: SequenceNotStr[str] | Omit = omit,
        exclude_user_agent_clients: SequenceNotStr[str] | Omit = omit,
        exclude_user_agent_devices: SequenceNotStr[str] | Omit = omit,
        http_methods: List[Literal["DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT", "TRACE"]] | Omit = omit,
        ips: SequenceNotStr[str] | Omit = omit,
        ja3: SequenceNotStr[str] | Omit = omit,
        ja4: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        optional_action: List[Literal["captcha", "challenge"]] | Omit = omit,
        ordering: str | Omit = omit,
        organizations: SequenceNotStr[str] | Omit = omit,
        path: SequenceNotStr[str] | Omit = omit,
        reference_ids: SequenceNotStr[str] | Omit = omit,
        request_ids: SequenceNotStr[str] | Omit = omit,
        security_rule_names: SequenceNotStr[str] | Omit = omit,
        session_ids: SequenceNotStr[str] | Omit = omit,
        status_codes: Iterable[int] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        user_agent: SequenceNotStr[str] | Omit = omit,
        user_agent_clients: SequenceNotStr[str] | Omit = omit,
        user_agent_devices: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[WaapRequestSummary]:
        """Retrieve request log data over account's domains.

        The log records every request
        passing through WAAP towards the origin server.

        Args:
          start: Filter data items starting from a specified date in ISO 8601 format

          countries: Filter data by a country code of the originating IP address in ISO 3166-1
              alpha-2 format.

          decision: Filter data by decision.

          domains: List of domain IDs. Empty list means all domains belonging to the current
              account.

          end: Filter data items up to a specified end date in ISO 8601 format. If not
              provided, defaults to the current date and time.

          exclude_countries: Exclude data by a country code of the originating IP address in ISO 3166-1
              alpha-2 format.

          exclude_decision: Exclude entries that match any of the given decisions.

          exclude_domains: Exclude data by domain ID.

          exclude_http_methods: Exclude entries with any of the given HTTP methods.

          exclude_ips: Exclude traffic data by client IP.

          exclude_ja3: Exclude entries whose JA3 TLS client fingerprint matches any of the supplied
              values. Each value must be exactly 32 hexadecimal characters (mixed case
              allowed) and is case-folded to lowercase when the backend filter is built.
              Supply multiple values to exclude any of them. Omit the parameter to apply no
              JA3 exclusion.

          exclude_ja4: Exclude entries whose JA4 TLS client fingerprint equals any of the supplied
              values. An item must match the JA4 form `<ja4_a>_<ja4_b>_<ja4_c>` (a
              10-character prefix and two 12-character hexadecimal hashes, mixed case allowed)
              and is case-folded to lowercase when the backend filter is built. Omit the
              parameter to apply no JA4 exclusion.

          exclude_optional_action: Exclude entries that match any of the given optional action values.

          exclude_organizations: Exclude entries whose organization exactly equals any supplied value. Omit or
              provide an empty list to apply no organization exclusion.

          exclude_path: Exclude entries that match the given URL path pattern; '\\**' is wildcard.

          exclude_reference_ids: Exclude data by reference IDs.

          exclude_request_ids: Exclude data by request IDs.

          exclude_security_rule_names: Exclude data by name of a security rule matched the request.

          exclude_session_ids: Exclude data by session IDs.

          exclude_status_codes: Exclude entries with any of the given HTTP response status codes.

          exclude_tags: Exclude entries whose tag exactly equals any supplied value. Omit or provide an
              empty list to apply no tag exclusion.

          exclude_user_agent: Exclude entries whose user agent contains any of the supplied texts,
              case-insensitive partial match. Omit or provide an empty list to apply no user
              agent text exclusion.

          exclude_user_agent_clients: Exclude entries whose parsed user agent client exactly equals any supplied
              value. Omit or provide an empty list to apply no user agent client exclusion.

          exclude_user_agent_devices: Exclude entries whose parsed user agent device exactly equals any supplied
              value. Omit or provide an empty list to apply no user agent device exclusion.

          http_methods: Filter by HTTP methods

          ips: Filter traffic data by client IP.

          ja3: Filter by JA3 TLS client fingerprint. Each value must be exactly 32 hexadecimal
              characters (mixed case allowed) and is case-folded to lowercase when the backend
              filter is built. Supply multiple values to match any of them. Omit the parameter
              to apply no JA3 filter.

          ja4: Filter by JA4 TLS client fingerprint. When present, the value must match the JA4
              form `<ja4_a>_<ja4_b>_<ja4_c>` (a 10-character prefix and two 12-character
              hexadecimal hashes, mixed case allowed) and is case-folded to lowercase when the
              backend filter is built. Supply multiple values to match any of them. Omit the
              parameter entirely to apply no JA4 filter.

          limit: Number of items to return

          offset: Number of items to skip

          optional_action: Filter data by optional action.

          ordering: Sort data by given field.

          organizations: Include entries whose organization exactly equals any supplied value. Omit or
              provide an empty list to apply no organization filter.

          path: Filter by URL path. '\\**' is wildcard.

          reference_ids: Filter data by reference IDs.

          request_ids: Filter data by request IDs.

          security_rule_names: Filter data by name of a security rule matched the request.

          session_ids: Filter data by session IDs.

          status_codes: Filter data by HTTP response status code.

          tags: Include entries whose tag exactly equals any supplied value. Omit or provide an
              empty list to apply no tag filter.

          user_agent: Include entries whose user agent contains any of the supplied texts,
              case-insensitive partial match. Omit or provide an empty list to apply no user
              agent text filter.

          user_agent_clients: Include entries whose parsed user agent client exactly equals any supplied
              value. Omit or provide an empty list to apply no user agent client filter.

          user_agent_devices: Include entries whose parsed user agent device exactly equals any supplied
              value. Omit or provide an empty list to apply no user agent device filter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/waap/v1/analytics/requests",
            page=SyncOffsetPage[WaapRequestSummary],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "start": start,
                        "countries": countries,
                        "decision": decision,
                        "domains": domains,
                        "end": end,
                        "exclude_countries": exclude_countries,
                        "exclude_decision": exclude_decision,
                        "exclude_domains": exclude_domains,
                        "exclude_http_methods": exclude_http_methods,
                        "exclude_ips": exclude_ips,
                        "exclude_ja3": exclude_ja3,
                        "exclude_ja4": exclude_ja4,
                        "exclude_optional_action": exclude_optional_action,
                        "exclude_organizations": exclude_organizations,
                        "exclude_path": exclude_path,
                        "exclude_reference_ids": exclude_reference_ids,
                        "exclude_request_ids": exclude_request_ids,
                        "exclude_security_rule_names": exclude_security_rule_names,
                        "exclude_session_ids": exclude_session_ids,
                        "exclude_status_codes": exclude_status_codes,
                        "exclude_tags": exclude_tags,
                        "exclude_user_agent": exclude_user_agent,
                        "exclude_user_agent_clients": exclude_user_agent_clients,
                        "exclude_user_agent_devices": exclude_user_agent_devices,
                        "http_methods": http_methods,
                        "ips": ips,
                        "ja3": ja3,
                        "ja4": ja4,
                        "limit": limit,
                        "offset": offset,
                        "optional_action": optional_action,
                        "ordering": ordering,
                        "organizations": organizations,
                        "path": path,
                        "reference_ids": reference_ids,
                        "request_ids": request_ids,
                        "security_rule_names": security_rule_names,
                        "session_ids": session_ids,
                        "status_codes": status_codes,
                        "tags": tags,
                        "user_agent": user_agent,
                        "user_agent_clients": user_agent_clients,
                        "user_agent_devices": user_agent_devices,
                    },
                    analytics_get_requests_params.AnalyticsGetRequestsParams,
                ),
            ),
            model=WaapRequestSummary,
        )

    def get_traffic(
        self,
        *,
        resolution: Literal["daily", "hourly", "minutely"],
        start: str,
        bucket_size: Optional[Literal[60, 300, 600, 900, 1800, 3600, 7200, 10800, 21600, 43200, 86400]] | Omit = omit,
        domains: Iterable[int] | Omit = omit,
        end: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalyticsGetTrafficResponse:
        """Retrieves a comprehensive report on traffic statistics for a set of domains.

        The
        report includes details such as API requests, blocked events, error counts, and
        many more traffic-related metrics.

        Args:
          resolution: Specifies the granularity of the result data.

          start: Filter data items starting from a specified date in ISO 8601 format

          bucket_size: Optional explicit aggregation bucket width in seconds. When supplied,
              `bucket_size` supersedes `resolution` for aggregation granularity.

          domains: List of domain IDs. Empty list means all domains belonging to the current
              account.

          end: Filter data items up to a specified end date in ISO 8601 format. If not
              provided, defaults to the current date and time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/waap/v1/analytics/traffic",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "resolution": resolution,
                        "start": start,
                        "bucket_size": bucket_size,
                        "domains": domains,
                        "end": end,
                    },
                    analytics_get_traffic_params.AnalyticsGetTrafficParams,
                ),
            ),
            cast_to=AnalyticsGetTrafficResponse,
        )

    def get_traffic_filtered(
        self,
        *,
        resolution: Literal["daily", "hourly", "minutely"],
        start: str,
        bucket_size: Optional[Literal[60, 300, 600, 900, 1800, 3600, 7200, 10800, 21600, 43200, 86400]] | Omit = omit,
        countries: SequenceNotStr[str] | Omit = omit,
        decision: List[Literal["blocked", "monitored", "allowed", "passed"]] | Omit = omit,
        domains: Iterable[int] | Omit = omit,
        end: Optional[str] | Omit = omit,
        exclude_countries: SequenceNotStr[str] | Omit = omit,
        exclude_decision: List[Literal["blocked", "monitored", "allowed", "passed"]] | Omit = omit,
        exclude_domains: Iterable[int] | Omit = omit,
        exclude_http_methods: List[Literal["DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT", "TRACE"]]
        | Omit = omit,
        exclude_ips: SequenceNotStr[str] | Omit = omit,
        exclude_ja3: SequenceNotStr[str] | Omit = omit,
        exclude_ja4: SequenceNotStr[str] | Omit = omit,
        exclude_optional_action: List[Literal["captcha", "challenge"]] | Omit = omit,
        exclude_organizations: SequenceNotStr[str] | Omit = omit,
        exclude_path: SequenceNotStr[str] | Omit = omit,
        exclude_reference_ids: SequenceNotStr[str] | Omit = omit,
        exclude_request_ids: SequenceNotStr[str] | Omit = omit,
        exclude_security_rule_names: SequenceNotStr[str] | Omit = omit,
        exclude_session_ids: SequenceNotStr[str] | Omit = omit,
        exclude_status_codes: Iterable[int] | Omit = omit,
        exclude_tags: SequenceNotStr[str] | Omit = omit,
        exclude_user_agent: SequenceNotStr[str] | Omit = omit,
        exclude_user_agent_clients: SequenceNotStr[str] | Omit = omit,
        exclude_user_agent_devices: SequenceNotStr[str] | Omit = omit,
        http_methods: List[Literal["DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT", "TRACE"]] | Omit = omit,
        ips: SequenceNotStr[str] | Omit = omit,
        ja3: SequenceNotStr[str] | Omit = omit,
        ja4: SequenceNotStr[str] | Omit = omit,
        optional_action: List[Literal["captcha", "challenge"]] | Omit = omit,
        organizations: SequenceNotStr[str] | Omit = omit,
        path: SequenceNotStr[str] | Omit = omit,
        reference_ids: SequenceNotStr[str] | Omit = omit,
        request_ids: SequenceNotStr[str] | Omit = omit,
        security_rule_names: SequenceNotStr[str] | Omit = omit,
        session_ids: SequenceNotStr[str] | Omit = omit,
        status_codes: Iterable[int] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        user_agent: SequenceNotStr[str] | Omit = omit,
        user_agent_clients: SequenceNotStr[str] | Omit = omit,
        user_agent_devices: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalyticsGetTrafficFilteredResponse:
        """Retrieves a traffic time series data over a set of domains.

        The response is
        suitable for plotting a time series chart. This method allows filtering the
        traffic data by various criteria.

        Args:
          resolution: Specifies the granularity of the result data.

          start: Filter data items starting from a specified date in ISO 8601 format

          bucket_size: Optional explicit aggregation bucket width in seconds. When supplied,
              `bucket_size` supersedes `resolution` for aggregation granularity.

          countries: Filter data by a country code of the originating IP address in ISO 3166-1
              alpha-2 format.

          decision: Filter data by decision.

          domains: List of domain IDs. Empty list means all domains belonging to the current
              account.

          end: Filter data items up to a specified end date in ISO 8601 format. If not
              provided, defaults to the current date and time.

          exclude_countries: Exclude data by a country code of the originating IP address in ISO 3166-1
              alpha-2 format.

          exclude_decision: Exclude entries that match any of the given decisions.

          exclude_domains: Exclude data by domain ID.

          exclude_http_methods: Exclude entries with any of the given HTTP methods.

          exclude_ips: Exclude traffic data by client IP.

          exclude_ja3: Exclude entries whose JA3 TLS client fingerprint matches any of the supplied
              values. Each value must be exactly 32 hexadecimal characters (mixed case
              allowed) and is case-folded to lowercase when the backend filter is built.
              Supply multiple values to exclude any of them. Omit the parameter to apply no
              JA3 exclusion.

          exclude_ja4: Exclude entries whose JA4 TLS client fingerprint equals any of the supplied
              values. An item must match the JA4 form `<ja4_a>_<ja4_b>_<ja4_c>` (a
              10-character prefix and two 12-character hexadecimal hashes, mixed case allowed)
              and is case-folded to lowercase when the backend filter is built. Omit the
              parameter to apply no JA4 exclusion.

          exclude_optional_action: Exclude entries that match any of the given optional action values.

          exclude_organizations: Exclude entries whose organization exactly equals any supplied value. Omit or
              provide an empty list to apply no organization exclusion.

          exclude_path: Exclude entries that match the given URL path pattern; '\\**' is wildcard.

          exclude_reference_ids: Exclude data by reference IDs.

          exclude_request_ids: Exclude data by request IDs.

          exclude_security_rule_names: Exclude data by name of a security rule matched the request.

          exclude_session_ids: Exclude data by session IDs.

          exclude_status_codes: Exclude entries with any of the given HTTP response status codes.

          exclude_tags: Exclude entries whose tag exactly equals any supplied value. Omit or provide an
              empty list to apply no tag exclusion.

          exclude_user_agent: Exclude entries whose user agent contains any of the supplied texts,
              case-insensitive partial match. Omit or provide an empty list to apply no user
              agent text exclusion.

          exclude_user_agent_clients: Exclude entries whose parsed user agent client exactly equals any supplied
              value. Omit or provide an empty list to apply no user agent client exclusion.

          exclude_user_agent_devices: Exclude entries whose parsed user agent device exactly equals any supplied
              value. Omit or provide an empty list to apply no user agent device exclusion.

          http_methods: Filter by HTTP methods

          ips: Filter traffic data by client IP.

          ja3: Filter by JA3 TLS client fingerprint. Each value must be exactly 32 hexadecimal
              characters (mixed case allowed) and is case-folded to lowercase when the backend
              filter is built. Supply multiple values to match any of them. Omit the parameter
              to apply no JA3 filter.

          ja4: Filter by JA4 TLS client fingerprint. When present, the value must match the JA4
              form `<ja4_a>_<ja4_b>_<ja4_c>` (a 10-character prefix and two 12-character
              hexadecimal hashes, mixed case allowed) and is case-folded to lowercase when the
              backend filter is built. Supply multiple values to match any of them. Omit the
              parameter entirely to apply no JA4 filter.

          optional_action: Filter data by optional action.

          organizations: Include entries whose organization exactly equals any supplied value. Omit or
              provide an empty list to apply no organization filter.

          path: Filter by URL path. '\\**' is wildcard.

          reference_ids: Filter data by reference IDs.

          request_ids: Filter data by request IDs.

          security_rule_names: Filter data by name of a security rule matched the request.

          session_ids: Filter data by session IDs.

          status_codes: Filter data by HTTP response status code.

          tags: Include entries whose tag exactly equals any supplied value. Omit or provide an
              empty list to apply no tag filter.

          user_agent: Include entries whose user agent contains any of the supplied texts,
              case-insensitive partial match. Omit or provide an empty list to apply no user
              agent text filter.

          user_agent_clients: Include entries whose parsed user agent client exactly equals any supplied
              value. Omit or provide an empty list to apply no user agent client filter.

          user_agent_devices: Include entries whose parsed user agent device exactly equals any supplied
              value. Omit or provide an empty list to apply no user agent device filter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/waap/v1/analytics/traffic-filtered",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "resolution": resolution,
                        "start": start,
                        "bucket_size": bucket_size,
                        "countries": countries,
                        "decision": decision,
                        "domains": domains,
                        "end": end,
                        "exclude_countries": exclude_countries,
                        "exclude_decision": exclude_decision,
                        "exclude_domains": exclude_domains,
                        "exclude_http_methods": exclude_http_methods,
                        "exclude_ips": exclude_ips,
                        "exclude_ja3": exclude_ja3,
                        "exclude_ja4": exclude_ja4,
                        "exclude_optional_action": exclude_optional_action,
                        "exclude_organizations": exclude_organizations,
                        "exclude_path": exclude_path,
                        "exclude_reference_ids": exclude_reference_ids,
                        "exclude_request_ids": exclude_request_ids,
                        "exclude_security_rule_names": exclude_security_rule_names,
                        "exclude_session_ids": exclude_session_ids,
                        "exclude_status_codes": exclude_status_codes,
                        "exclude_tags": exclude_tags,
                        "exclude_user_agent": exclude_user_agent,
                        "exclude_user_agent_clients": exclude_user_agent_clients,
                        "exclude_user_agent_devices": exclude_user_agent_devices,
                        "http_methods": http_methods,
                        "ips": ips,
                        "ja3": ja3,
                        "ja4": ja4,
                        "optional_action": optional_action,
                        "organizations": organizations,
                        "path": path,
                        "reference_ids": reference_ids,
                        "request_ids": request_ids,
                        "security_rule_names": security_rule_names,
                        "session_ids": session_ids,
                        "status_codes": status_codes,
                        "tags": tags,
                        "user_agent": user_agent,
                        "user_agent_clients": user_agent_clients,
                        "user_agent_devices": user_agent_devices,
                    },
                    analytics_get_traffic_filtered_params.AnalyticsGetTrafficFilteredParams,
                ),
            ),
            cast_to=AnalyticsGetTrafficFilteredResponse,
        )


class AsyncAnalyticsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAnalyticsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAnalyticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnalyticsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncAnalyticsResourceWithStreamingResponse(self)

    async def get_event_statistics(
        self,
        dimension: Literal["country", "rule", "org", "ip", "useragent", "target"],
        *,
        start: str,
        domains: Iterable[int] | Omit = omit,
        end: Optional[str] | Omit = omit,
        ips: SequenceNotStr[str] | Omit = omit,
        order_by: Literal["total.desc", "threats.desc"] | Omit = omit,
        security_rule_names: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapSimpleEventStatistics:
        """Retrieves event statistics per given dimension of a request characteristics.

        A
        WAAP _Event_ represents a request observed by the system. The report contains
        the total, blocked, suppressed, and allowed event counts for top ten points in
        the selected dimension.

        Args:
          dimension: A request characteristics dimension

          start: Filter data items starting from a specified date in ISO 8601 format

          domains: List of domain IDs. Empty list means all domains belonging to the current
              account.

          end: Filter data items up to a specified end date in ISO 8601 format. If not
              provided, defaults to the current date and time.

          ips: Filter statistics by client IP addresses (max 10).

          order_by: Ordering applied to the ranked points within the dimension. `total.desc` ranks
              by total event count descending; `threats.desc` ranks by threat (blocked and
              monitored) event count descending.

          security_rule_names: Filter data by name of a security rule matched the request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dimension:
            raise ValueError(f"Expected a non-empty value for `dimension` but received {dimension!r}")
        return await self._get(
            path_template("/waap/v1/analytics/stats/{dimension}", dimension=dimension),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "start": start,
                        "domains": domains,
                        "end": end,
                        "ips": ips,
                        "order_by": order_by,
                        "security_rule_names": security_rule_names,
                    },
                    analytics_get_event_statistics_params.AnalyticsGetEventStatisticsParams,
                ),
            ),
            cast_to=WaapSimpleEventStatistics,
        )

    def get_filters(
        self,
        type: Literal["user-agent-clients", "user-agent-devices", "organizations"],
        *,
        start: str,
        domains: Iterable[int] | Omit = omit,
        end: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        name: Optional[str] | Omit = omit,
        offset: int | Omit = omit,
        ordering: Literal["count", "value"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AnalyticsGetFiltersResponse, AsyncOffsetPage[AnalyticsGetFiltersResponse]]:
        """
        Retrieves autocomplete suggestions for specified filter parameter values
        observed within the current client account during the requested time range. Use
        the returned `value` in the filter parameters of an analytics data request
        ([GET /v1/analytics/requests](/docs/api-reference/waap/analytics/get-request-log-data)
        and
        [GET /v1/analytics/traffic-filtered](/docs/api-reference/waap/analytics/get-filtered-traffic-data)).
        `count` reports how many times the value was observed in the requested range.

        Args:
          type: Parsed user-agent field type.

          start: Filter data items starting from a specified date in ISO 8601 format

          domains: List of domain IDs. Empty list means all domains belonging to the current
              account.

          end: Filter data items up to a specified end date in ISO 8601 format. If not
              provided, defaults to the current date and time.

          limit: Number of items to return

          name: Case-insensitive partial autocomplete pattern matched against the value name by
              the value provider. Must be between 2 and 100 characters; empty or omitted
              returns the available suggestions for the current account and time range.

          offset: Number of items to skip

          ordering: Suggestion ordering. `count` sorts by observed occurrence count descending (most
              frequent first) with value as a tie breaker; `value` sorts alphabetically by
              value ascending with count as a tie breaker.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not type:
            raise ValueError(f"Expected a non-empty value for `type` but received {type!r}")
        return self._get_api_list(
            path_template("/waap/v1/analytics/filters/{type}", type=type),
            page=AsyncOffsetPage[AnalyticsGetFiltersResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "start": start,
                        "domains": domains,
                        "end": end,
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "ordering": ordering,
                    },
                    analytics_get_filters_params.AnalyticsGetFiltersParams,
                ),
            ),
            model=AnalyticsGetFiltersResponse,
        )

    def get_requests(
        self,
        *,
        start: str,
        countries: SequenceNotStr[str] | Omit = omit,
        decision: List[Literal["blocked", "monitored", "allowed", "passed"]] | Omit = omit,
        domains: Iterable[int] | Omit = omit,
        end: Optional[str] | Omit = omit,
        exclude_countries: SequenceNotStr[str] | Omit = omit,
        exclude_decision: List[Literal["blocked", "monitored", "allowed", "passed"]] | Omit = omit,
        exclude_domains: Iterable[int] | Omit = omit,
        exclude_http_methods: List[Literal["DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT", "TRACE"]]
        | Omit = omit,
        exclude_ips: SequenceNotStr[str] | Omit = omit,
        exclude_ja3: SequenceNotStr[str] | Omit = omit,
        exclude_ja4: SequenceNotStr[str] | Omit = omit,
        exclude_optional_action: List[Literal["captcha", "challenge"]] | Omit = omit,
        exclude_organizations: SequenceNotStr[str] | Omit = omit,
        exclude_path: SequenceNotStr[str] | Omit = omit,
        exclude_reference_ids: SequenceNotStr[str] | Omit = omit,
        exclude_request_ids: SequenceNotStr[str] | Omit = omit,
        exclude_security_rule_names: SequenceNotStr[str] | Omit = omit,
        exclude_session_ids: SequenceNotStr[str] | Omit = omit,
        exclude_status_codes: Iterable[int] | Omit = omit,
        exclude_tags: SequenceNotStr[str] | Omit = omit,
        exclude_user_agent: SequenceNotStr[str] | Omit = omit,
        exclude_user_agent_clients: SequenceNotStr[str] | Omit = omit,
        exclude_user_agent_devices: SequenceNotStr[str] | Omit = omit,
        http_methods: List[Literal["DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT", "TRACE"]] | Omit = omit,
        ips: SequenceNotStr[str] | Omit = omit,
        ja3: SequenceNotStr[str] | Omit = omit,
        ja4: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        optional_action: List[Literal["captcha", "challenge"]] | Omit = omit,
        ordering: str | Omit = omit,
        organizations: SequenceNotStr[str] | Omit = omit,
        path: SequenceNotStr[str] | Omit = omit,
        reference_ids: SequenceNotStr[str] | Omit = omit,
        request_ids: SequenceNotStr[str] | Omit = omit,
        security_rule_names: SequenceNotStr[str] | Omit = omit,
        session_ids: SequenceNotStr[str] | Omit = omit,
        status_codes: Iterable[int] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        user_agent: SequenceNotStr[str] | Omit = omit,
        user_agent_clients: SequenceNotStr[str] | Omit = omit,
        user_agent_devices: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[WaapRequestSummary, AsyncOffsetPage[WaapRequestSummary]]:
        """Retrieve request log data over account's domains.

        The log records every request
        passing through WAAP towards the origin server.

        Args:
          start: Filter data items starting from a specified date in ISO 8601 format

          countries: Filter data by a country code of the originating IP address in ISO 3166-1
              alpha-2 format.

          decision: Filter data by decision.

          domains: List of domain IDs. Empty list means all domains belonging to the current
              account.

          end: Filter data items up to a specified end date in ISO 8601 format. If not
              provided, defaults to the current date and time.

          exclude_countries: Exclude data by a country code of the originating IP address in ISO 3166-1
              alpha-2 format.

          exclude_decision: Exclude entries that match any of the given decisions.

          exclude_domains: Exclude data by domain ID.

          exclude_http_methods: Exclude entries with any of the given HTTP methods.

          exclude_ips: Exclude traffic data by client IP.

          exclude_ja3: Exclude entries whose JA3 TLS client fingerprint matches any of the supplied
              values. Each value must be exactly 32 hexadecimal characters (mixed case
              allowed) and is case-folded to lowercase when the backend filter is built.
              Supply multiple values to exclude any of them. Omit the parameter to apply no
              JA3 exclusion.

          exclude_ja4: Exclude entries whose JA4 TLS client fingerprint equals any of the supplied
              values. An item must match the JA4 form `<ja4_a>_<ja4_b>_<ja4_c>` (a
              10-character prefix and two 12-character hexadecimal hashes, mixed case allowed)
              and is case-folded to lowercase when the backend filter is built. Omit the
              parameter to apply no JA4 exclusion.

          exclude_optional_action: Exclude entries that match any of the given optional action values.

          exclude_organizations: Exclude entries whose organization exactly equals any supplied value. Omit or
              provide an empty list to apply no organization exclusion.

          exclude_path: Exclude entries that match the given URL path pattern; '\\**' is wildcard.

          exclude_reference_ids: Exclude data by reference IDs.

          exclude_request_ids: Exclude data by request IDs.

          exclude_security_rule_names: Exclude data by name of a security rule matched the request.

          exclude_session_ids: Exclude data by session IDs.

          exclude_status_codes: Exclude entries with any of the given HTTP response status codes.

          exclude_tags: Exclude entries whose tag exactly equals any supplied value. Omit or provide an
              empty list to apply no tag exclusion.

          exclude_user_agent: Exclude entries whose user agent contains any of the supplied texts,
              case-insensitive partial match. Omit or provide an empty list to apply no user
              agent text exclusion.

          exclude_user_agent_clients: Exclude entries whose parsed user agent client exactly equals any supplied
              value. Omit or provide an empty list to apply no user agent client exclusion.

          exclude_user_agent_devices: Exclude entries whose parsed user agent device exactly equals any supplied
              value. Omit or provide an empty list to apply no user agent device exclusion.

          http_methods: Filter by HTTP methods

          ips: Filter traffic data by client IP.

          ja3: Filter by JA3 TLS client fingerprint. Each value must be exactly 32 hexadecimal
              characters (mixed case allowed) and is case-folded to lowercase when the backend
              filter is built. Supply multiple values to match any of them. Omit the parameter
              to apply no JA3 filter.

          ja4: Filter by JA4 TLS client fingerprint. When present, the value must match the JA4
              form `<ja4_a>_<ja4_b>_<ja4_c>` (a 10-character prefix and two 12-character
              hexadecimal hashes, mixed case allowed) and is case-folded to lowercase when the
              backend filter is built. Supply multiple values to match any of them. Omit the
              parameter entirely to apply no JA4 filter.

          limit: Number of items to return

          offset: Number of items to skip

          optional_action: Filter data by optional action.

          ordering: Sort data by given field.

          organizations: Include entries whose organization exactly equals any supplied value. Omit or
              provide an empty list to apply no organization filter.

          path: Filter by URL path. '\\**' is wildcard.

          reference_ids: Filter data by reference IDs.

          request_ids: Filter data by request IDs.

          security_rule_names: Filter data by name of a security rule matched the request.

          session_ids: Filter data by session IDs.

          status_codes: Filter data by HTTP response status code.

          tags: Include entries whose tag exactly equals any supplied value. Omit or provide an
              empty list to apply no tag filter.

          user_agent: Include entries whose user agent contains any of the supplied texts,
              case-insensitive partial match. Omit or provide an empty list to apply no user
              agent text filter.

          user_agent_clients: Include entries whose parsed user agent client exactly equals any supplied
              value. Omit or provide an empty list to apply no user agent client filter.

          user_agent_devices: Include entries whose parsed user agent device exactly equals any supplied
              value. Omit or provide an empty list to apply no user agent device filter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/waap/v1/analytics/requests",
            page=AsyncOffsetPage[WaapRequestSummary],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "start": start,
                        "countries": countries,
                        "decision": decision,
                        "domains": domains,
                        "end": end,
                        "exclude_countries": exclude_countries,
                        "exclude_decision": exclude_decision,
                        "exclude_domains": exclude_domains,
                        "exclude_http_methods": exclude_http_methods,
                        "exclude_ips": exclude_ips,
                        "exclude_ja3": exclude_ja3,
                        "exclude_ja4": exclude_ja4,
                        "exclude_optional_action": exclude_optional_action,
                        "exclude_organizations": exclude_organizations,
                        "exclude_path": exclude_path,
                        "exclude_reference_ids": exclude_reference_ids,
                        "exclude_request_ids": exclude_request_ids,
                        "exclude_security_rule_names": exclude_security_rule_names,
                        "exclude_session_ids": exclude_session_ids,
                        "exclude_status_codes": exclude_status_codes,
                        "exclude_tags": exclude_tags,
                        "exclude_user_agent": exclude_user_agent,
                        "exclude_user_agent_clients": exclude_user_agent_clients,
                        "exclude_user_agent_devices": exclude_user_agent_devices,
                        "http_methods": http_methods,
                        "ips": ips,
                        "ja3": ja3,
                        "ja4": ja4,
                        "limit": limit,
                        "offset": offset,
                        "optional_action": optional_action,
                        "ordering": ordering,
                        "organizations": organizations,
                        "path": path,
                        "reference_ids": reference_ids,
                        "request_ids": request_ids,
                        "security_rule_names": security_rule_names,
                        "session_ids": session_ids,
                        "status_codes": status_codes,
                        "tags": tags,
                        "user_agent": user_agent,
                        "user_agent_clients": user_agent_clients,
                        "user_agent_devices": user_agent_devices,
                    },
                    analytics_get_requests_params.AnalyticsGetRequestsParams,
                ),
            ),
            model=WaapRequestSummary,
        )

    async def get_traffic(
        self,
        *,
        resolution: Literal["daily", "hourly", "minutely"],
        start: str,
        bucket_size: Optional[Literal[60, 300, 600, 900, 1800, 3600, 7200, 10800, 21600, 43200, 86400]] | Omit = omit,
        domains: Iterable[int] | Omit = omit,
        end: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalyticsGetTrafficResponse:
        """Retrieves a comprehensive report on traffic statistics for a set of domains.

        The
        report includes details such as API requests, blocked events, error counts, and
        many more traffic-related metrics.

        Args:
          resolution: Specifies the granularity of the result data.

          start: Filter data items starting from a specified date in ISO 8601 format

          bucket_size: Optional explicit aggregation bucket width in seconds. When supplied,
              `bucket_size` supersedes `resolution` for aggregation granularity.

          domains: List of domain IDs. Empty list means all domains belonging to the current
              account.

          end: Filter data items up to a specified end date in ISO 8601 format. If not
              provided, defaults to the current date and time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/waap/v1/analytics/traffic",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "resolution": resolution,
                        "start": start,
                        "bucket_size": bucket_size,
                        "domains": domains,
                        "end": end,
                    },
                    analytics_get_traffic_params.AnalyticsGetTrafficParams,
                ),
            ),
            cast_to=AnalyticsGetTrafficResponse,
        )

    async def get_traffic_filtered(
        self,
        *,
        resolution: Literal["daily", "hourly", "minutely"],
        start: str,
        bucket_size: Optional[Literal[60, 300, 600, 900, 1800, 3600, 7200, 10800, 21600, 43200, 86400]] | Omit = omit,
        countries: SequenceNotStr[str] | Omit = omit,
        decision: List[Literal["blocked", "monitored", "allowed", "passed"]] | Omit = omit,
        domains: Iterable[int] | Omit = omit,
        end: Optional[str] | Omit = omit,
        exclude_countries: SequenceNotStr[str] | Omit = omit,
        exclude_decision: List[Literal["blocked", "monitored", "allowed", "passed"]] | Omit = omit,
        exclude_domains: Iterable[int] | Omit = omit,
        exclude_http_methods: List[Literal["DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT", "TRACE"]]
        | Omit = omit,
        exclude_ips: SequenceNotStr[str] | Omit = omit,
        exclude_ja3: SequenceNotStr[str] | Omit = omit,
        exclude_ja4: SequenceNotStr[str] | Omit = omit,
        exclude_optional_action: List[Literal["captcha", "challenge"]] | Omit = omit,
        exclude_organizations: SequenceNotStr[str] | Omit = omit,
        exclude_path: SequenceNotStr[str] | Omit = omit,
        exclude_reference_ids: SequenceNotStr[str] | Omit = omit,
        exclude_request_ids: SequenceNotStr[str] | Omit = omit,
        exclude_security_rule_names: SequenceNotStr[str] | Omit = omit,
        exclude_session_ids: SequenceNotStr[str] | Omit = omit,
        exclude_status_codes: Iterable[int] | Omit = omit,
        exclude_tags: SequenceNotStr[str] | Omit = omit,
        exclude_user_agent: SequenceNotStr[str] | Omit = omit,
        exclude_user_agent_clients: SequenceNotStr[str] | Omit = omit,
        exclude_user_agent_devices: SequenceNotStr[str] | Omit = omit,
        http_methods: List[Literal["DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT", "TRACE"]] | Omit = omit,
        ips: SequenceNotStr[str] | Omit = omit,
        ja3: SequenceNotStr[str] | Omit = omit,
        ja4: SequenceNotStr[str] | Omit = omit,
        optional_action: List[Literal["captcha", "challenge"]] | Omit = omit,
        organizations: SequenceNotStr[str] | Omit = omit,
        path: SequenceNotStr[str] | Omit = omit,
        reference_ids: SequenceNotStr[str] | Omit = omit,
        request_ids: SequenceNotStr[str] | Omit = omit,
        security_rule_names: SequenceNotStr[str] | Omit = omit,
        session_ids: SequenceNotStr[str] | Omit = omit,
        status_codes: Iterable[int] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        user_agent: SequenceNotStr[str] | Omit = omit,
        user_agent_clients: SequenceNotStr[str] | Omit = omit,
        user_agent_devices: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalyticsGetTrafficFilteredResponse:
        """Retrieves a traffic time series data over a set of domains.

        The response is
        suitable for plotting a time series chart. This method allows filtering the
        traffic data by various criteria.

        Args:
          resolution: Specifies the granularity of the result data.

          start: Filter data items starting from a specified date in ISO 8601 format

          bucket_size: Optional explicit aggregation bucket width in seconds. When supplied,
              `bucket_size` supersedes `resolution` for aggregation granularity.

          countries: Filter data by a country code of the originating IP address in ISO 3166-1
              alpha-2 format.

          decision: Filter data by decision.

          domains: List of domain IDs. Empty list means all domains belonging to the current
              account.

          end: Filter data items up to a specified end date in ISO 8601 format. If not
              provided, defaults to the current date and time.

          exclude_countries: Exclude data by a country code of the originating IP address in ISO 3166-1
              alpha-2 format.

          exclude_decision: Exclude entries that match any of the given decisions.

          exclude_domains: Exclude data by domain ID.

          exclude_http_methods: Exclude entries with any of the given HTTP methods.

          exclude_ips: Exclude traffic data by client IP.

          exclude_ja3: Exclude entries whose JA3 TLS client fingerprint matches any of the supplied
              values. Each value must be exactly 32 hexadecimal characters (mixed case
              allowed) and is case-folded to lowercase when the backend filter is built.
              Supply multiple values to exclude any of them. Omit the parameter to apply no
              JA3 exclusion.

          exclude_ja4: Exclude entries whose JA4 TLS client fingerprint equals any of the supplied
              values. An item must match the JA4 form `<ja4_a>_<ja4_b>_<ja4_c>` (a
              10-character prefix and two 12-character hexadecimal hashes, mixed case allowed)
              and is case-folded to lowercase when the backend filter is built. Omit the
              parameter to apply no JA4 exclusion.

          exclude_optional_action: Exclude entries that match any of the given optional action values.

          exclude_organizations: Exclude entries whose organization exactly equals any supplied value. Omit or
              provide an empty list to apply no organization exclusion.

          exclude_path: Exclude entries that match the given URL path pattern; '\\**' is wildcard.

          exclude_reference_ids: Exclude data by reference IDs.

          exclude_request_ids: Exclude data by request IDs.

          exclude_security_rule_names: Exclude data by name of a security rule matched the request.

          exclude_session_ids: Exclude data by session IDs.

          exclude_status_codes: Exclude entries with any of the given HTTP response status codes.

          exclude_tags: Exclude entries whose tag exactly equals any supplied value. Omit or provide an
              empty list to apply no tag exclusion.

          exclude_user_agent: Exclude entries whose user agent contains any of the supplied texts,
              case-insensitive partial match. Omit or provide an empty list to apply no user
              agent text exclusion.

          exclude_user_agent_clients: Exclude entries whose parsed user agent client exactly equals any supplied
              value. Omit or provide an empty list to apply no user agent client exclusion.

          exclude_user_agent_devices: Exclude entries whose parsed user agent device exactly equals any supplied
              value. Omit or provide an empty list to apply no user agent device exclusion.

          http_methods: Filter by HTTP methods

          ips: Filter traffic data by client IP.

          ja3: Filter by JA3 TLS client fingerprint. Each value must be exactly 32 hexadecimal
              characters (mixed case allowed) and is case-folded to lowercase when the backend
              filter is built. Supply multiple values to match any of them. Omit the parameter
              to apply no JA3 filter.

          ja4: Filter by JA4 TLS client fingerprint. When present, the value must match the JA4
              form `<ja4_a>_<ja4_b>_<ja4_c>` (a 10-character prefix and two 12-character
              hexadecimal hashes, mixed case allowed) and is case-folded to lowercase when the
              backend filter is built. Supply multiple values to match any of them. Omit the
              parameter entirely to apply no JA4 filter.

          optional_action: Filter data by optional action.

          organizations: Include entries whose organization exactly equals any supplied value. Omit or
              provide an empty list to apply no organization filter.

          path: Filter by URL path. '\\**' is wildcard.

          reference_ids: Filter data by reference IDs.

          request_ids: Filter data by request IDs.

          security_rule_names: Filter data by name of a security rule matched the request.

          session_ids: Filter data by session IDs.

          status_codes: Filter data by HTTP response status code.

          tags: Include entries whose tag exactly equals any supplied value. Omit or provide an
              empty list to apply no tag filter.

          user_agent: Include entries whose user agent contains any of the supplied texts,
              case-insensitive partial match. Omit or provide an empty list to apply no user
              agent text filter.

          user_agent_clients: Include entries whose parsed user agent client exactly equals any supplied
              value. Omit or provide an empty list to apply no user agent client filter.

          user_agent_devices: Include entries whose parsed user agent device exactly equals any supplied
              value. Omit or provide an empty list to apply no user agent device filter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/waap/v1/analytics/traffic-filtered",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "resolution": resolution,
                        "start": start,
                        "bucket_size": bucket_size,
                        "countries": countries,
                        "decision": decision,
                        "domains": domains,
                        "end": end,
                        "exclude_countries": exclude_countries,
                        "exclude_decision": exclude_decision,
                        "exclude_domains": exclude_domains,
                        "exclude_http_methods": exclude_http_methods,
                        "exclude_ips": exclude_ips,
                        "exclude_ja3": exclude_ja3,
                        "exclude_ja4": exclude_ja4,
                        "exclude_optional_action": exclude_optional_action,
                        "exclude_organizations": exclude_organizations,
                        "exclude_path": exclude_path,
                        "exclude_reference_ids": exclude_reference_ids,
                        "exclude_request_ids": exclude_request_ids,
                        "exclude_security_rule_names": exclude_security_rule_names,
                        "exclude_session_ids": exclude_session_ids,
                        "exclude_status_codes": exclude_status_codes,
                        "exclude_tags": exclude_tags,
                        "exclude_user_agent": exclude_user_agent,
                        "exclude_user_agent_clients": exclude_user_agent_clients,
                        "exclude_user_agent_devices": exclude_user_agent_devices,
                        "http_methods": http_methods,
                        "ips": ips,
                        "ja3": ja3,
                        "ja4": ja4,
                        "optional_action": optional_action,
                        "organizations": organizations,
                        "path": path,
                        "reference_ids": reference_ids,
                        "request_ids": request_ids,
                        "security_rule_names": security_rule_names,
                        "session_ids": session_ids,
                        "status_codes": status_codes,
                        "tags": tags,
                        "user_agent": user_agent,
                        "user_agent_clients": user_agent_clients,
                        "user_agent_devices": user_agent_devices,
                    },
                    analytics_get_traffic_filtered_params.AnalyticsGetTrafficFilteredParams,
                ),
            ),
            cast_to=AnalyticsGetTrafficFilteredResponse,
        )


class AnalyticsResourceWithRawResponse:
    def __init__(self, analytics: AnalyticsResource) -> None:
        self._analytics = analytics

        self.get_event_statistics = to_raw_response_wrapper(
            analytics.get_event_statistics,
        )
        self.get_filters = to_raw_response_wrapper(
            analytics.get_filters,
        )
        self.get_requests = to_raw_response_wrapper(
            analytics.get_requests,
        )
        self.get_traffic = to_raw_response_wrapper(
            analytics.get_traffic,
        )
        self.get_traffic_filtered = to_raw_response_wrapper(
            analytics.get_traffic_filtered,
        )


class AsyncAnalyticsResourceWithRawResponse:
    def __init__(self, analytics: AsyncAnalyticsResource) -> None:
        self._analytics = analytics

        self.get_event_statistics = async_to_raw_response_wrapper(
            analytics.get_event_statistics,
        )
        self.get_filters = async_to_raw_response_wrapper(
            analytics.get_filters,
        )
        self.get_requests = async_to_raw_response_wrapper(
            analytics.get_requests,
        )
        self.get_traffic = async_to_raw_response_wrapper(
            analytics.get_traffic,
        )
        self.get_traffic_filtered = async_to_raw_response_wrapper(
            analytics.get_traffic_filtered,
        )


class AnalyticsResourceWithStreamingResponse:
    def __init__(self, analytics: AnalyticsResource) -> None:
        self._analytics = analytics

        self.get_event_statistics = to_streamed_response_wrapper(
            analytics.get_event_statistics,
        )
        self.get_filters = to_streamed_response_wrapper(
            analytics.get_filters,
        )
        self.get_requests = to_streamed_response_wrapper(
            analytics.get_requests,
        )
        self.get_traffic = to_streamed_response_wrapper(
            analytics.get_traffic,
        )
        self.get_traffic_filtered = to_streamed_response_wrapper(
            analytics.get_traffic_filtered,
        )


class AsyncAnalyticsResourceWithStreamingResponse:
    def __init__(self, analytics: AsyncAnalyticsResource) -> None:
        self._analytics = analytics

        self.get_event_statistics = async_to_streamed_response_wrapper(
            analytics.get_event_statistics,
        )
        self.get_filters = async_to_streamed_response_wrapper(
            analytics.get_filters,
        )
        self.get_requests = async_to_streamed_response_wrapper(
            analytics.get_requests,
        )
        self.get_traffic = async_to_streamed_response_wrapper(
            analytics.get_traffic,
        )
        self.get_traffic_filtered = async_to_streamed_response_wrapper(
            analytics.get_traffic_filtered,
        )
