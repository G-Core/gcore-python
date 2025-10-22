# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.cdn import (
    statistic_get_logs_usage_series_params,
    statistic_get_shield_usage_series_params,
    statistic_get_logs_usage_aggregated_params,
    statistic_get_resource_usage_series_params,
    statistic_get_shield_usage_aggregated_params,
    statistic_get_resource_usage_aggregated_params,
)
from ..._base_client import make_request_options
from ...types.cdn.usage_series_stats import UsageSeriesStats
from ...types.cdn.resource_usage_stats import ResourceUsageStats
from ...types.cdn.logs_aggregated_stats import LogsAggregatedStats
from ...types.cdn.shield_aggregated_stats import ShieldAggregatedStats
from ...types.cdn.resource_aggregated_stats import ResourceAggregatedStats

__all__ = ["StatisticsResource", "AsyncStatisticsResource"]


class StatisticsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StatisticsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return StatisticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StatisticsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return StatisticsResourceWithStreamingResponse(self)

    def get_logs_usage_aggregated(
        self,
        *,
        from_: str,
        to: str,
        flat: bool | Omit = omit,
        group_by: str | Omit = omit,
        resource: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsAggregatedStats:
        """
        Get the number of CDN resources that used Logs uploader.

        Request URL parameters should be added as a query string after the endpoint.

        Args:
          from_: Beginning of the requested time period (ISO 8601/RFC 3339 format, UTC.)

          to: End of the requested time period (ISO 8601/RFC 3339 format, UTC.)

          flat: The way the parameters are arranged in the response.

              Possible values:

              - **true** – Flat structure is used.
              - **false** – Embedded structure is used (default.)

          group_by: Output data grouping.

              Possible value:

              - **resource** - Data is grouped by CDN resources.

          resource: CDN resources IDs by that statistics data is grouped.

              To request multiple values, use:

              - &resource=1&resource=2

              If CDN resource ID is not specified, data related to all CDN resources is
              returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/cdn/statistics/raw_logs_usage/aggregated",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                        "flat": flat,
                        "group_by": group_by,
                        "resource": resource,
                    },
                    statistic_get_logs_usage_aggregated_params.StatisticGetLogsUsageAggregatedParams,
                ),
            ),
            cast_to=LogsAggregatedStats,
        )

    def get_logs_usage_series(
        self,
        *,
        from_: str,
        to: str,
        resource: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageSeriesStats:
        """
        Get Logs uploader usage statistics for up to 90 days starting today.

        Request URL parameters should be added as a query string after the endpoint.

        Args:
          from_: Beginning of the requested time period (ISO 8601/RFC 3339 format, UTC.)

          to: End of the requested time period (ISO 8601/RFC 3339 format, UTC.)

          resource: CDN resources IDs by that statistics data is grouped.

              To request multiple values, use:

              - &resource=1&resource=2

              If CDN resource ID is not specified, data related to all CDN resources is
              returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/cdn/statistics/raw_logs_usage/series",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                        "resource": resource,
                    },
                    statistic_get_logs_usage_series_params.StatisticGetLogsUsageSeriesParams,
                ),
            ),
            cast_to=UsageSeriesStats,
        )

    def get_resource_usage_aggregated(
        self,
        *,
        from_: str,
        metrics: str,
        service: str,
        to: str,
        countries: str | Omit = omit,
        flat: bool | Omit = omit,
        group_by: str | Omit = omit,
        regions: str | Omit = omit,
        resource: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResourceAggregatedStats:
        """
        Get aggregated CDN resources statistics.

        Request URL parameters should be added as a query string after the endpoint.

        Aggregated data does not include data for the last two hours.

        Args:
          from_: Beginning of the requested time period (ISO 8601/RFC 3339 format, UTC.)

          metrics: Types of statistics data.

              Possible values:

              - **`upstream_bytes`** – Traffic in bytes from an origin server to CDN servers
                or to origin shielding when used.
              - **`sent_bytes`** – Traffic in bytes from CDN servers to clients.
              - **`shield_bytes`** – Traffic in bytes from origin shielding to CDN servers.
              - **`backblaze_bytes`** - Traffic in bytes from Backblaze origin.
              - **`total_bytes`** – `shield_bytes`, `upstream_bytes` and `sent_bytes`
                combined.
              - **`cdn_bytes`** – `sent_bytes` and `shield_bytes` combined.
              - **requests** – Number of requests to edge servers.
              - **`responses_2xx`** – Number of 2xx response codes.
              - **`responses_3xx`** – Number of 3xx response codes.
              - **`responses_4xx`** – Number of 4xx response codes.
              - **`responses_5xx`** – Number of 5xx response codes.
              - **`responses_hit`** – Number of responses with the header Cache: HIT.
              - **`responses_miss`** – Number of responses with the header Cache: MISS.
              - **`response_types`** – Statistics by content type. It returns a number of
                responses for content with different MIME types.
              - **`cache_hit_traffic_ratio`** – Formula: 1 - `upstream_bytes` / `sent_bytes`.
                We deduct the non-cached traffic from the total traffic amount.
              - **`cache_hit_requests_ratio`** – Formula: `responses_hit` / requests. The
                share of sending cached content.
              - **`shield_traffic_ratio`** – Formula: (`shield_bytes` - `upstream_bytes`) /
                `shield_bytes`. The efficiency of the Origin Shielding: how much more traffic
                is sent from the Origin Shielding than from the origin.
              - **`image_processed`** - Number of images transformed on the Image optimization
                service.
              - **`request_time`** - Time elapsed between the first bytes of a request were
                processed and logging after the last bytes were sent to a user.
              - **`upstream_response_time`** - Number of milliseconds it took to receive a
                response from an origin. If upstream `response_time_` contains several
                indications for one request (in case of more than 1 origin), we summarize
                them. In case of aggregating several queries, the average of this amount is
                calculated.
              - **`95_percentile`** - Represents the 95th percentile of network bandwidth
                usage in bytes per second. This means that 95% of the time, the network
                resource usage was below this value.
              - **`max_bandwidth`** - The maximum network bandwidth that was used during the
                selected time represented in bytes per second.
              - **`min_bandwidth`** - The minimum network bandwidth that was used during the
                selected time represented in bytes per second.

              Metrics **`upstream_response_time`** and **`request_time`** should be requested
              separately from other metrics

          service: Service name.

              Possible value:

              - CDN

          to: End of the requested time period (ISO 8601/RFC 3339 format, UTC.)

          countries: Names of countries for which data should be displayed. English short name from
              [ISO 3166 standard][1] without the definite article ("the") should be used.

              [1]: https://www.iso.org/obp/ui/#search/code/

              To request multiple values, use:

              - &countries=france&countries=denmark

          flat: The way the parameters are arranged in the response.

              Possible values:

              - **true** – Flat structure is used.
              - **false** – Embedded structure is used (default.)

          group_by: Output data grouping.

              Possible values:

              - **resource** – Data is grouped by CDN resources IDs.
              - **region** – Data is grouped by regions of CDN edge servers.
              - **country** – Data is grouped by countries of CDN edge servers.
              - **vhost** – Data is grouped by resources CNAMEs.
              - **`client_country`** - Data is grouped by countries, based on end-users'
                location.

              To request multiple values, use:

              - &`group_by`=region&`group_by`=resource

          regions: Regions for which data is displayed.

              Possible values:

              - **na** – North America
              - **eu** – Europe
              - **cis** – Commonwealth of Independent States
              - **asia** – Asia
              - **au** – Australia
              - **latam** – Latin America
              - **me** – Middle East
              - **africa** - Africa
              - **sa** - South America

          resource: CDN resources IDs by that statistics data is grouped.

              To request multiple values, use:

              - &resource=1&resource=2

              If CDN resource ID is not specified, data related to all CDN resources is
              returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/cdn/statistics/aggregate/stats",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "metrics": metrics,
                        "service": service,
                        "to": to,
                        "countries": countries,
                        "flat": flat,
                        "group_by": group_by,
                        "regions": regions,
                        "resource": resource,
                    },
                    statistic_get_resource_usage_aggregated_params.StatisticGetResourceUsageAggregatedParams,
                ),
            ),
            cast_to=ResourceAggregatedStats,
        )

    def get_resource_usage_series(
        self,
        *,
        from_: str,
        granularity: str,
        metrics: str,
        service: str,
        to: str,
        countries: str | Omit = omit,
        group_by: str | Omit = omit,
        regions: str | Omit = omit,
        resource: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResourceUsageStats:
        """
        Get CDN resources statistics for up to 365 days starting today.

        Args:
          from_: Beginning of the requested time period (ISO 8601/RFC 3339 format, UTC.)

          granularity: Duration of the time blocks into which the data will be divided.

              Possible values:

              - **1m** - available only for up to 1 month in the past.
              - **5m**
              - **15m**
              - **1h**
              - **1d**

          metrics: Types of statistics data.

              Possible values:

              - **`upstream_bytes`** – Traffic in bytes from an origin server to CDN servers
                or to origin shielding when used.
              - **`sent_bytes`** – Traffic in bytes from CDN servers to clients.
              - **`shield_bytes`** – Traffic in bytes from origin shielding to CDN servers.
              - **`backblaze_bytes`** - Traffic in bytes from Backblaze origin.
              - **`total_bytes`** – `shield_bytes`, `upstream_bytes` and `sent_bytes`
                combined.
              - **`cdn_bytes`** – `sent_bytes` and `shield_bytes` combined.
              - **requests** – Number of requests to edge servers.
              - **`responses_2xx`** – Number of 2xx response codes.
              - **`responses_3xx`** – Number of 3xx response codes.
              - **`responses_4xx`** – Number of 4xx response codes.
              - **`responses_5xx`** – Number of 5xx response codes.
              - **`responses_hit`** – Number of responses with the header Cache: HIT.
              - **`responses_miss`** – Number of responses with the header Cache: MISS.
              - **`response_types`** – Statistics by content type. It returns a number of
                responses for content with different MIME types.
              - **`cache_hit_traffic_ratio`** – Formula: 1 - `upstream_bytes` / `sent_bytes`.
                We deduct the non-cached traffic from the total traffic amount.
              - **`cache_hit_requests_ratio`** – Formula: `responses_hit` / requests. The
                share of sending cached content.
              - **`shield_traffic_ratio`** – Formula: (`shield_bytes` - `upstream_bytes`) /
                `shield_bytes`. The efficiency of the Origin Shielding: how much more traffic
                is sent from the Origin Shielding than from the origin.
              - **`image_processed`** - Number of images transformed on the Image optimization
                service.
              - **`request_time`** - Time elapsed between the first bytes of a request were
                processed and logging after the last bytes were sent to a user.
              - **`upstream_response_time`** - Number of milliseconds it took to receive a
                response from an origin. If upstream `response_time_` contains several
                indications for one request (in case of more than 1 origin), we summarize
                them. In case of aggregating several queries, the average of this amount is
                calculated.

              Metrics **`upstream_response_time`** and **`request_time`** should be requested
              separately from other metrics

          service: Service name.

              Possible value:

              - CDN

          to: End of the requested time period (ISO 8601/RFC 3339 format, UTC.)

          countries: Names of countries for which data should be displayed. English short name from
              [ISO 3166 standard][1] without the definite article ("the") should be used.

              [1]: https://www.iso.org/obp/ui/#search/code/

              To request multiple values, use:

              - &countries=france&countries=denmark

          group_by: Output data grouping.

              Possible values:

              - **resource** – Data is grouped by CDN resources IDs.
              - **region** – Data is grouped by regions of CDN edge servers.
              - **country** – Data is grouped by countries of CDN edge servers.
              - **vhost** – Data is grouped by resources CNAMEs.
              - **`client_country`** - Data is grouped by countries, based on end-users'
                location.

              To request multiple values, use:

              - &`group_by`=region&`group_by`=resource

          regions: Regions for which data is displayed.

              Possible values:

              - **na** – North America
              - **eu** – Europe
              - **cis** – Commonwealth of Independent States
              - **asia** – Asia
              - **au** – Australia
              - **latam** – Latin America
              - **me** – Middle East
              - **africa** - Africa
              - **sa** - South America

          resource: CDN resources IDs by that statistics data is grouped.

              To request multiple values, use:

              - &resource=1&resource=2

              If CDN resource ID is not specified, data related to all CDN resources is
              returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/cdn/statistics/series",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "granularity": granularity,
                        "metrics": metrics,
                        "service": service,
                        "to": to,
                        "countries": countries,
                        "group_by": group_by,
                        "regions": regions,
                        "resource": resource,
                    },
                    statistic_get_resource_usage_series_params.StatisticGetResourceUsageSeriesParams,
                ),
            ),
            cast_to=ResourceUsageStats,
        )

    def get_shield_usage_aggregated(
        self,
        *,
        from_: str,
        to: str,
        flat: bool | Omit = omit,
        group_by: str | Omit = omit,
        resource: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShieldAggregatedStats:
        """
        The number of CDN resources that use origin shielding.

        Request URL parameters should be added as a query string after the endpoint.

        Args:
          from_: Beginning of the requested time period (ISO 8601/RFC 3339 format, UTC.)

          to: End of the requested time period (ISO 8601/RFC 3339 format, UTC.)

          flat: The way the parameters are arranged in the response.

              Possible values:

              - **true** – Flat structure is used.
              - **false** – Embedded structure is used (default.)

          group_by: Output data grouping.

              Possible value:

              - **resource** - Data is grouped by CDN resources.

          resource: CDN resources IDs by that statistics data is grouped.

              To request multiple values, use:

              - &resource=1&resource=2

              If CDN resource ID is not specified, data related to all CDN resources is
              returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/cdn/statistics/shield_usage/aggregated",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                        "flat": flat,
                        "group_by": group_by,
                        "resource": resource,
                    },
                    statistic_get_shield_usage_aggregated_params.StatisticGetShieldUsageAggregatedParams,
                ),
            ),
            cast_to=ShieldAggregatedStats,
        )

    def get_shield_usage_series(
        self,
        *,
        from_: str,
        to: str,
        resource: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageSeriesStats:
        """
        Get origin shielding usage statistics for up to 365 days starting from today.

        Request URL parameters should be added as a query string after the endpoint.

        Args:
          from_: Beginning of the requested time period (ISO 8601/RFC 3339 format, UTC.)

          to: End of the requested time period (ISO 8601/RFC 3339 format, UTC.)

          resource: CDN resources IDs by that statistics data is grouped.

              To request multiple values, use:

              - &resource=1&resource=2

              If CDN resource ID is not specified, data related to all CDN resources is
              returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/cdn/statistics/shield_usage/series",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                        "resource": resource,
                    },
                    statistic_get_shield_usage_series_params.StatisticGetShieldUsageSeriesParams,
                ),
            ),
            cast_to=UsageSeriesStats,
        )


class AsyncStatisticsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStatisticsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStatisticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStatisticsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncStatisticsResourceWithStreamingResponse(self)

    async def get_logs_usage_aggregated(
        self,
        *,
        from_: str,
        to: str,
        flat: bool | Omit = omit,
        group_by: str | Omit = omit,
        resource: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogsAggregatedStats:
        """
        Get the number of CDN resources that used Logs uploader.

        Request URL parameters should be added as a query string after the endpoint.

        Args:
          from_: Beginning of the requested time period (ISO 8601/RFC 3339 format, UTC.)

          to: End of the requested time period (ISO 8601/RFC 3339 format, UTC.)

          flat: The way the parameters are arranged in the response.

              Possible values:

              - **true** – Flat structure is used.
              - **false** – Embedded structure is used (default.)

          group_by: Output data grouping.

              Possible value:

              - **resource** - Data is grouped by CDN resources.

          resource: CDN resources IDs by that statistics data is grouped.

              To request multiple values, use:

              - &resource=1&resource=2

              If CDN resource ID is not specified, data related to all CDN resources is
              returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/cdn/statistics/raw_logs_usage/aggregated",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                        "flat": flat,
                        "group_by": group_by,
                        "resource": resource,
                    },
                    statistic_get_logs_usage_aggregated_params.StatisticGetLogsUsageAggregatedParams,
                ),
            ),
            cast_to=LogsAggregatedStats,
        )

    async def get_logs_usage_series(
        self,
        *,
        from_: str,
        to: str,
        resource: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageSeriesStats:
        """
        Get Logs uploader usage statistics for up to 90 days starting today.

        Request URL parameters should be added as a query string after the endpoint.

        Args:
          from_: Beginning of the requested time period (ISO 8601/RFC 3339 format, UTC.)

          to: End of the requested time period (ISO 8601/RFC 3339 format, UTC.)

          resource: CDN resources IDs by that statistics data is grouped.

              To request multiple values, use:

              - &resource=1&resource=2

              If CDN resource ID is not specified, data related to all CDN resources is
              returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/cdn/statistics/raw_logs_usage/series",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                        "resource": resource,
                    },
                    statistic_get_logs_usage_series_params.StatisticGetLogsUsageSeriesParams,
                ),
            ),
            cast_to=UsageSeriesStats,
        )

    async def get_resource_usage_aggregated(
        self,
        *,
        from_: str,
        metrics: str,
        service: str,
        to: str,
        countries: str | Omit = omit,
        flat: bool | Omit = omit,
        group_by: str | Omit = omit,
        regions: str | Omit = omit,
        resource: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResourceAggregatedStats:
        """
        Get aggregated CDN resources statistics.

        Request URL parameters should be added as a query string after the endpoint.

        Aggregated data does not include data for the last two hours.

        Args:
          from_: Beginning of the requested time period (ISO 8601/RFC 3339 format, UTC.)

          metrics: Types of statistics data.

              Possible values:

              - **`upstream_bytes`** – Traffic in bytes from an origin server to CDN servers
                or to origin shielding when used.
              - **`sent_bytes`** – Traffic in bytes from CDN servers to clients.
              - **`shield_bytes`** – Traffic in bytes from origin shielding to CDN servers.
              - **`backblaze_bytes`** - Traffic in bytes from Backblaze origin.
              - **`total_bytes`** – `shield_bytes`, `upstream_bytes` and `sent_bytes`
                combined.
              - **`cdn_bytes`** – `sent_bytes` and `shield_bytes` combined.
              - **requests** – Number of requests to edge servers.
              - **`responses_2xx`** – Number of 2xx response codes.
              - **`responses_3xx`** – Number of 3xx response codes.
              - **`responses_4xx`** – Number of 4xx response codes.
              - **`responses_5xx`** – Number of 5xx response codes.
              - **`responses_hit`** – Number of responses with the header Cache: HIT.
              - **`responses_miss`** – Number of responses with the header Cache: MISS.
              - **`response_types`** – Statistics by content type. It returns a number of
                responses for content with different MIME types.
              - **`cache_hit_traffic_ratio`** – Formula: 1 - `upstream_bytes` / `sent_bytes`.
                We deduct the non-cached traffic from the total traffic amount.
              - **`cache_hit_requests_ratio`** – Formula: `responses_hit` / requests. The
                share of sending cached content.
              - **`shield_traffic_ratio`** – Formula: (`shield_bytes` - `upstream_bytes`) /
                `shield_bytes`. The efficiency of the Origin Shielding: how much more traffic
                is sent from the Origin Shielding than from the origin.
              - **`image_processed`** - Number of images transformed on the Image optimization
                service.
              - **`request_time`** - Time elapsed between the first bytes of a request were
                processed and logging after the last bytes were sent to a user.
              - **`upstream_response_time`** - Number of milliseconds it took to receive a
                response from an origin. If upstream `response_time_` contains several
                indications for one request (in case of more than 1 origin), we summarize
                them. In case of aggregating several queries, the average of this amount is
                calculated.
              - **`95_percentile`** - Represents the 95th percentile of network bandwidth
                usage in bytes per second. This means that 95% of the time, the network
                resource usage was below this value.
              - **`max_bandwidth`** - The maximum network bandwidth that was used during the
                selected time represented in bytes per second.
              - **`min_bandwidth`** - The minimum network bandwidth that was used during the
                selected time represented in bytes per second.

              Metrics **`upstream_response_time`** and **`request_time`** should be requested
              separately from other metrics

          service: Service name.

              Possible value:

              - CDN

          to: End of the requested time period (ISO 8601/RFC 3339 format, UTC.)

          countries: Names of countries for which data should be displayed. English short name from
              [ISO 3166 standard][1] without the definite article ("the") should be used.

              [1]: https://www.iso.org/obp/ui/#search/code/

              To request multiple values, use:

              - &countries=france&countries=denmark

          flat: The way the parameters are arranged in the response.

              Possible values:

              - **true** – Flat structure is used.
              - **false** – Embedded structure is used (default.)

          group_by: Output data grouping.

              Possible values:

              - **resource** – Data is grouped by CDN resources IDs.
              - **region** – Data is grouped by regions of CDN edge servers.
              - **country** – Data is grouped by countries of CDN edge servers.
              - **vhost** – Data is grouped by resources CNAMEs.
              - **`client_country`** - Data is grouped by countries, based on end-users'
                location.

              To request multiple values, use:

              - &`group_by`=region&`group_by`=resource

          regions: Regions for which data is displayed.

              Possible values:

              - **na** – North America
              - **eu** – Europe
              - **cis** – Commonwealth of Independent States
              - **asia** – Asia
              - **au** – Australia
              - **latam** – Latin America
              - **me** – Middle East
              - **africa** - Africa
              - **sa** - South America

          resource: CDN resources IDs by that statistics data is grouped.

              To request multiple values, use:

              - &resource=1&resource=2

              If CDN resource ID is not specified, data related to all CDN resources is
              returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/cdn/statistics/aggregate/stats",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_": from_,
                        "metrics": metrics,
                        "service": service,
                        "to": to,
                        "countries": countries,
                        "flat": flat,
                        "group_by": group_by,
                        "regions": regions,
                        "resource": resource,
                    },
                    statistic_get_resource_usage_aggregated_params.StatisticGetResourceUsageAggregatedParams,
                ),
            ),
            cast_to=ResourceAggregatedStats,
        )

    async def get_resource_usage_series(
        self,
        *,
        from_: str,
        granularity: str,
        metrics: str,
        service: str,
        to: str,
        countries: str | Omit = omit,
        group_by: str | Omit = omit,
        regions: str | Omit = omit,
        resource: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResourceUsageStats:
        """
        Get CDN resources statistics for up to 365 days starting today.

        Args:
          from_: Beginning of the requested time period (ISO 8601/RFC 3339 format, UTC.)

          granularity: Duration of the time blocks into which the data will be divided.

              Possible values:

              - **1m** - available only for up to 1 month in the past.
              - **5m**
              - **15m**
              - **1h**
              - **1d**

          metrics: Types of statistics data.

              Possible values:

              - **`upstream_bytes`** – Traffic in bytes from an origin server to CDN servers
                or to origin shielding when used.
              - **`sent_bytes`** – Traffic in bytes from CDN servers to clients.
              - **`shield_bytes`** – Traffic in bytes from origin shielding to CDN servers.
              - **`backblaze_bytes`** - Traffic in bytes from Backblaze origin.
              - **`total_bytes`** – `shield_bytes`, `upstream_bytes` and `sent_bytes`
                combined.
              - **`cdn_bytes`** – `sent_bytes` and `shield_bytes` combined.
              - **requests** – Number of requests to edge servers.
              - **`responses_2xx`** – Number of 2xx response codes.
              - **`responses_3xx`** – Number of 3xx response codes.
              - **`responses_4xx`** – Number of 4xx response codes.
              - **`responses_5xx`** – Number of 5xx response codes.
              - **`responses_hit`** – Number of responses with the header Cache: HIT.
              - **`responses_miss`** – Number of responses with the header Cache: MISS.
              - **`response_types`** – Statistics by content type. It returns a number of
                responses for content with different MIME types.
              - **`cache_hit_traffic_ratio`** – Formula: 1 - `upstream_bytes` / `sent_bytes`.
                We deduct the non-cached traffic from the total traffic amount.
              - **`cache_hit_requests_ratio`** – Formula: `responses_hit` / requests. The
                share of sending cached content.
              - **`shield_traffic_ratio`** – Formula: (`shield_bytes` - `upstream_bytes`) /
                `shield_bytes`. The efficiency of the Origin Shielding: how much more traffic
                is sent from the Origin Shielding than from the origin.
              - **`image_processed`** - Number of images transformed on the Image optimization
                service.
              - **`request_time`** - Time elapsed between the first bytes of a request were
                processed and logging after the last bytes were sent to a user.
              - **`upstream_response_time`** - Number of milliseconds it took to receive a
                response from an origin. If upstream `response_time_` contains several
                indications for one request (in case of more than 1 origin), we summarize
                them. In case of aggregating several queries, the average of this amount is
                calculated.

              Metrics **`upstream_response_time`** and **`request_time`** should be requested
              separately from other metrics

          service: Service name.

              Possible value:

              - CDN

          to: End of the requested time period (ISO 8601/RFC 3339 format, UTC.)

          countries: Names of countries for which data should be displayed. English short name from
              [ISO 3166 standard][1] without the definite article ("the") should be used.

              [1]: https://www.iso.org/obp/ui/#search/code/

              To request multiple values, use:

              - &countries=france&countries=denmark

          group_by: Output data grouping.

              Possible values:

              - **resource** – Data is grouped by CDN resources IDs.
              - **region** – Data is grouped by regions of CDN edge servers.
              - **country** – Data is grouped by countries of CDN edge servers.
              - **vhost** – Data is grouped by resources CNAMEs.
              - **`client_country`** - Data is grouped by countries, based on end-users'
                location.

              To request multiple values, use:

              - &`group_by`=region&`group_by`=resource

          regions: Regions for which data is displayed.

              Possible values:

              - **na** – North America
              - **eu** – Europe
              - **cis** – Commonwealth of Independent States
              - **asia** – Asia
              - **au** – Australia
              - **latam** – Latin America
              - **me** – Middle East
              - **africa** - Africa
              - **sa** - South America

          resource: CDN resources IDs by that statistics data is grouped.

              To request multiple values, use:

              - &resource=1&resource=2

              If CDN resource ID is not specified, data related to all CDN resources is
              returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/cdn/statistics/series",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_": from_,
                        "granularity": granularity,
                        "metrics": metrics,
                        "service": service,
                        "to": to,
                        "countries": countries,
                        "group_by": group_by,
                        "regions": regions,
                        "resource": resource,
                    },
                    statistic_get_resource_usage_series_params.StatisticGetResourceUsageSeriesParams,
                ),
            ),
            cast_to=ResourceUsageStats,
        )

    async def get_shield_usage_aggregated(
        self,
        *,
        from_: str,
        to: str,
        flat: bool | Omit = omit,
        group_by: str | Omit = omit,
        resource: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShieldAggregatedStats:
        """
        The number of CDN resources that use origin shielding.

        Request URL parameters should be added as a query string after the endpoint.

        Args:
          from_: Beginning of the requested time period (ISO 8601/RFC 3339 format, UTC.)

          to: End of the requested time period (ISO 8601/RFC 3339 format, UTC.)

          flat: The way the parameters are arranged in the response.

              Possible values:

              - **true** – Flat structure is used.
              - **false** – Embedded structure is used (default.)

          group_by: Output data grouping.

              Possible value:

              - **resource** - Data is grouped by CDN resources.

          resource: CDN resources IDs by that statistics data is grouped.

              To request multiple values, use:

              - &resource=1&resource=2

              If CDN resource ID is not specified, data related to all CDN resources is
              returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/cdn/statistics/shield_usage/aggregated",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                        "flat": flat,
                        "group_by": group_by,
                        "resource": resource,
                    },
                    statistic_get_shield_usage_aggregated_params.StatisticGetShieldUsageAggregatedParams,
                ),
            ),
            cast_to=ShieldAggregatedStats,
        )

    async def get_shield_usage_series(
        self,
        *,
        from_: str,
        to: str,
        resource: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageSeriesStats:
        """
        Get origin shielding usage statistics for up to 365 days starting from today.

        Request URL parameters should be added as a query string after the endpoint.

        Args:
          from_: Beginning of the requested time period (ISO 8601/RFC 3339 format, UTC.)

          to: End of the requested time period (ISO 8601/RFC 3339 format, UTC.)

          resource: CDN resources IDs by that statistics data is grouped.

              To request multiple values, use:

              - &resource=1&resource=2

              If CDN resource ID is not specified, data related to all CDN resources is
              returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/cdn/statistics/shield_usage/series",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                        "resource": resource,
                    },
                    statistic_get_shield_usage_series_params.StatisticGetShieldUsageSeriesParams,
                ),
            ),
            cast_to=UsageSeriesStats,
        )


class StatisticsResourceWithRawResponse:
    def __init__(self, statistics: StatisticsResource) -> None:
        self._statistics = statistics

        self.get_logs_usage_aggregated = to_raw_response_wrapper(
            statistics.get_logs_usage_aggregated,
        )
        self.get_logs_usage_series = to_raw_response_wrapper(
            statistics.get_logs_usage_series,
        )
        self.get_resource_usage_aggregated = to_raw_response_wrapper(
            statistics.get_resource_usage_aggregated,
        )
        self.get_resource_usage_series = to_raw_response_wrapper(
            statistics.get_resource_usage_series,
        )
        self.get_shield_usage_aggregated = to_raw_response_wrapper(
            statistics.get_shield_usage_aggregated,
        )
        self.get_shield_usage_series = to_raw_response_wrapper(
            statistics.get_shield_usage_series,
        )


class AsyncStatisticsResourceWithRawResponse:
    def __init__(self, statistics: AsyncStatisticsResource) -> None:
        self._statistics = statistics

        self.get_logs_usage_aggregated = async_to_raw_response_wrapper(
            statistics.get_logs_usage_aggregated,
        )
        self.get_logs_usage_series = async_to_raw_response_wrapper(
            statistics.get_logs_usage_series,
        )
        self.get_resource_usage_aggregated = async_to_raw_response_wrapper(
            statistics.get_resource_usage_aggregated,
        )
        self.get_resource_usage_series = async_to_raw_response_wrapper(
            statistics.get_resource_usage_series,
        )
        self.get_shield_usage_aggregated = async_to_raw_response_wrapper(
            statistics.get_shield_usage_aggregated,
        )
        self.get_shield_usage_series = async_to_raw_response_wrapper(
            statistics.get_shield_usage_series,
        )


class StatisticsResourceWithStreamingResponse:
    def __init__(self, statistics: StatisticsResource) -> None:
        self._statistics = statistics

        self.get_logs_usage_aggregated = to_streamed_response_wrapper(
            statistics.get_logs_usage_aggregated,
        )
        self.get_logs_usage_series = to_streamed_response_wrapper(
            statistics.get_logs_usage_series,
        )
        self.get_resource_usage_aggregated = to_streamed_response_wrapper(
            statistics.get_resource_usage_aggregated,
        )
        self.get_resource_usage_series = to_streamed_response_wrapper(
            statistics.get_resource_usage_series,
        )
        self.get_shield_usage_aggregated = to_streamed_response_wrapper(
            statistics.get_shield_usage_aggregated,
        )
        self.get_shield_usage_series = to_streamed_response_wrapper(
            statistics.get_shield_usage_series,
        )


class AsyncStatisticsResourceWithStreamingResponse:
    def __init__(self, statistics: AsyncStatisticsResource) -> None:
        self._statistics = statistics

        self.get_logs_usage_aggregated = async_to_streamed_response_wrapper(
            statistics.get_logs_usage_aggregated,
        )
        self.get_logs_usage_series = async_to_streamed_response_wrapper(
            statistics.get_logs_usage_series,
        )
        self.get_resource_usage_aggregated = async_to_streamed_response_wrapper(
            statistics.get_resource_usage_aggregated,
        )
        self.get_resource_usage_series = async_to_streamed_response_wrapper(
            statistics.get_resource_usage_series,
        )
        self.get_shield_usage_aggregated = async_to_streamed_response_wrapper(
            statistics.get_shield_usage_aggregated,
        )
        self.get_shield_usage_series = async_to_streamed_response_wrapper(
            statistics.get_shield_usage_series,
        )
