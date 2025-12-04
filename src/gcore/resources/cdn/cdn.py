# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .logs import (
    LogsResource,
    AsyncLogsResource,
    LogsResourceWithRawResponse,
    AsyncLogsResourceWithRawResponse,
    LogsResourceWithStreamingResponse,
    AsyncLogsResourceWithStreamingResponse,
)
from .metrics import (
    MetricsResource,
    AsyncMetricsResource,
    MetricsResourceWithRawResponse,
    AsyncMetricsResourceWithRawResponse,
    MetricsResourceWithStreamingResponse,
    AsyncMetricsResourceWithStreamingResponse,
)
from .shields import (
    ShieldsResource,
    AsyncShieldsResource,
    ShieldsResourceWithRawResponse,
    AsyncShieldsResourceWithRawResponse,
    ShieldsResourceWithStreamingResponse,
    AsyncShieldsResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .ip_ranges import (
    IPRangesResource,
    AsyncIPRangesResource,
    IPRangesResourceWithRawResponse,
    AsyncIPRangesResourceWithRawResponse,
    IPRangesResourceWithStreamingResponse,
    AsyncIPRangesResourceWithStreamingResponse,
)
from .audit_logs import (
    AuditLogsResource,
    AsyncAuditLogsResource,
    AuditLogsResourceWithRawResponse,
    AsyncAuditLogsResourceWithRawResponse,
    AuditLogsResourceWithStreamingResponse,
    AsyncAuditLogsResourceWithStreamingResponse,
)
from .statistics import (
    StatisticsResource,
    AsyncStatisticsResource,
    StatisticsResourceWithRawResponse,
    AsyncStatisticsResourceWithRawResponse,
    StatisticsResourceWithStreamingResponse,
    AsyncStatisticsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.cdn import cdn_update_account_params, cdn_list_purge_statuses_params
from .certificates import (
    CertificatesResource,
    AsyncCertificatesResource,
    CertificatesResourceWithRawResponse,
    AsyncCertificatesResourceWithRawResponse,
    CertificatesResourceWithStreamingResponse,
    AsyncCertificatesResourceWithStreamingResponse,
)
from .origin_groups import (
    OriginGroupsResource,
    AsyncOriginGroupsResource,
    OriginGroupsResourceWithRawResponse,
    AsyncOriginGroupsResourceWithRawResponse,
    OriginGroupsResourceWithStreamingResponse,
    AsyncOriginGroupsResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from .rule_templates import (
    RuleTemplatesResource,
    AsyncRuleTemplatesResource,
    RuleTemplatesResourceWithRawResponse,
    AsyncRuleTemplatesResourceWithRawResponse,
    RuleTemplatesResourceWithStreamingResponse,
    AsyncRuleTemplatesResourceWithStreamingResponse,
)
from .network_capacity import (
    NetworkCapacityResource,
    AsyncNetworkCapacityResource,
    NetworkCapacityResourceWithRawResponse,
    AsyncNetworkCapacityResourceWithRawResponse,
    NetworkCapacityResourceWithStreamingResponse,
    AsyncNetworkCapacityResourceWithStreamingResponse,
)
from .resources.resources import (
    ResourcesResource,
    AsyncResourcesResource,
    ResourcesResourceWithRawResponse,
    AsyncResourcesResourceWithRawResponse,
    ResourcesResourceWithStreamingResponse,
    AsyncResourcesResourceWithStreamingResponse,
)
from ...types.cdn.aws_regions import AwsRegions
from ...types.cdn.cdn_account import CdnAccount
from .trusted_ca_certificates import (
    TrustedCaCertificatesResource,
    AsyncTrustedCaCertificatesResource,
    TrustedCaCertificatesResourceWithRawResponse,
    AsyncTrustedCaCertificatesResourceWithRawResponse,
    TrustedCaCertificatesResourceWithStreamingResponse,
    AsyncTrustedCaCertificatesResourceWithStreamingResponse,
)
from ...types.cdn.alibaba_regions import AlibabaRegions
from .logs_uploader.logs_uploader import (
    LogsUploaderResource,
    AsyncLogsUploaderResource,
    LogsUploaderResourceWithRawResponse,
    AsyncLogsUploaderResourceWithRawResponse,
    LogsUploaderResourceWithStreamingResponse,
    AsyncLogsUploaderResourceWithStreamingResponse,
)
from ...types.cdn.cdn_account_limits import CdnAccountLimits
from ...types.cdn.cdn_available_features import CdnAvailableFeatures
from ...types.cdn.cdn_list_purge_statuses_response import CdnListPurgeStatusesResponse

__all__ = ["CdnResource", "AsyncCdnResource"]


class CdnResource(SyncAPIResource):
    @cached_property
    def resources(self) -> ResourcesResource:
        return ResourcesResource(self._client)

    @cached_property
    def shields(self) -> ShieldsResource:
        return ShieldsResource(self._client)

    @cached_property
    def origin_groups(self) -> OriginGroupsResource:
        return OriginGroupsResource(self._client)

    @cached_property
    def rule_templates(self) -> RuleTemplatesResource:
        return RuleTemplatesResource(self._client)

    @cached_property
    def certificates(self) -> CertificatesResource:
        return CertificatesResource(self._client)

    @cached_property
    def trusted_ca_certificates(self) -> TrustedCaCertificatesResource:
        return TrustedCaCertificatesResource(self._client)

    @cached_property
    def audit_logs(self) -> AuditLogsResource:
        return AuditLogsResource(self._client)

    @cached_property
    def logs(self) -> LogsResource:
        return LogsResource(self._client)

    @cached_property
    def logs_uploader(self) -> LogsUploaderResource:
        return LogsUploaderResource(self._client)

    @cached_property
    def statistics(self) -> StatisticsResource:
        return StatisticsResource(self._client)

    @cached_property
    def network_capacity(self) -> NetworkCapacityResource:
        return NetworkCapacityResource(self._client)

    @cached_property
    def metrics(self) -> MetricsResource:
        return MetricsResource(self._client)

    @cached_property
    def ip_ranges(self) -> IPRangesResource:
        return IPRangesResource(self._client)

    @cached_property
    def with_raw_response(self) -> CdnResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return CdnResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CdnResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return CdnResourceWithStreamingResponse(self)

    def get_account_limits(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CdnAccountLimits:
        """Get information about CDN service limits."""
        return self._get(
            "/cdn/clients/me/limits",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CdnAccountLimits,
        )

    def get_account_overview(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CdnAccount:
        """Get information about CDN service."""
        return self._get(
            "/cdn/clients/me",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CdnAccount,
        )

    def get_available_features(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CdnAvailableFeatures:
        """Get information about available CDN features."""
        return self._get(
            "/cdn/clients/me/features",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CdnAvailableFeatures,
        )

    def list_alibaba_regions(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AlibabaRegions:
        """Get the list of Alibaba Cloud regions."""
        return self._get(
            "/cdn/alibaba_regions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AlibabaRegions,
        )

    def list_aws_regions(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AwsRegions:
        """Get the list of Amazon AWS regions."""
        return self._get(
            "/cdn/aws_regions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AwsRegions,
        )

    def list_purge_statuses(
        self,
        *,
        cname: str | Omit = omit,
        from_created: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        purge_type: str | Omit = omit,
        status: str | Omit = omit,
        to_created: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CdnListPurgeStatusesResponse:
        """
        Get purges history.

        Args:
          cname: Purges associated with a specific resource CNAME.

              Example:

              - &cname=example.com

          from_created: Start date and time of the requested time period (ISO 8601/RFC 3339 format,
              UTC.)

              Examples:

              - &`from_created`=2021-06-14T00:00:00Z
              - &`from_created`=2021-06-14T00:00:00.000Z

          limit: Maximum number of purges in the response.

          offset: Number of purge requests in the response to skip starting from the beginning of
              the requested period.

          purge_type: Purge requests with a certain purge type.

              Possible values:

              - **`purge_by_pattern`** - Purge by Pattern.
              - **`purge_by_url`** - Purge by URL.
              - **`purge_all`** - Purge All.

          status: Purge with a certain status.

              Possible values:

              - **In progress**
              - **Successful**
              - **Failed**
              - **Status report disabled**

          to_created: End date and time of the requested time period (ISO 8601/RFC 3339 format, UTC.)

              Examples:

              - &`to_created`=2021-06-15T00:00:00Z
              - &`to_created`=2021-06-15T00:00:00.000Z

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/cdn/purge_statuses",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cname": cname,
                        "from_created": from_created,
                        "limit": limit,
                        "offset": offset,
                        "purge_type": purge_type,
                        "status": status,
                        "to_created": to_created,
                    },
                    cdn_list_purge_statuses_params.CdnListPurgeStatusesParams,
                ),
            ),
            cast_to=CdnListPurgeStatusesResponse,
        )

    def update_account(
        self,
        *,
        utilization_level: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CdnAccount:
        """
        Change information about CDN service.

        Args:
          utilization_level: CDN traffic usage limit in gigabytes.

              When the limit is reached, we will send an email notification.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/cdn/clients/me",
            body=maybe_transform(
                {"utilization_level": utilization_level}, cdn_update_account_params.CdnUpdateAccountParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CdnAccount,
        )


class AsyncCdnResource(AsyncAPIResource):
    @cached_property
    def resources(self) -> AsyncResourcesResource:
        return AsyncResourcesResource(self._client)

    @cached_property
    def shields(self) -> AsyncShieldsResource:
        return AsyncShieldsResource(self._client)

    @cached_property
    def origin_groups(self) -> AsyncOriginGroupsResource:
        return AsyncOriginGroupsResource(self._client)

    @cached_property
    def rule_templates(self) -> AsyncRuleTemplatesResource:
        return AsyncRuleTemplatesResource(self._client)

    @cached_property
    def certificates(self) -> AsyncCertificatesResource:
        return AsyncCertificatesResource(self._client)

    @cached_property
    def trusted_ca_certificates(self) -> AsyncTrustedCaCertificatesResource:
        return AsyncTrustedCaCertificatesResource(self._client)

    @cached_property
    def audit_logs(self) -> AsyncAuditLogsResource:
        return AsyncAuditLogsResource(self._client)

    @cached_property
    def logs(self) -> AsyncLogsResource:
        return AsyncLogsResource(self._client)

    @cached_property
    def logs_uploader(self) -> AsyncLogsUploaderResource:
        return AsyncLogsUploaderResource(self._client)

    @cached_property
    def statistics(self) -> AsyncStatisticsResource:
        return AsyncStatisticsResource(self._client)

    @cached_property
    def network_capacity(self) -> AsyncNetworkCapacityResource:
        return AsyncNetworkCapacityResource(self._client)

    @cached_property
    def metrics(self) -> AsyncMetricsResource:
        return AsyncMetricsResource(self._client)

    @cached_property
    def ip_ranges(self) -> AsyncIPRangesResource:
        return AsyncIPRangesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCdnResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCdnResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCdnResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncCdnResourceWithStreamingResponse(self)

    async def get_account_limits(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CdnAccountLimits:
        """Get information about CDN service limits."""
        return await self._get(
            "/cdn/clients/me/limits",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CdnAccountLimits,
        )

    async def get_account_overview(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CdnAccount:
        """Get information about CDN service."""
        return await self._get(
            "/cdn/clients/me",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CdnAccount,
        )

    async def get_available_features(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CdnAvailableFeatures:
        """Get information about available CDN features."""
        return await self._get(
            "/cdn/clients/me/features",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CdnAvailableFeatures,
        )

    async def list_alibaba_regions(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AlibabaRegions:
        """Get the list of Alibaba Cloud regions."""
        return await self._get(
            "/cdn/alibaba_regions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AlibabaRegions,
        )

    async def list_aws_regions(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AwsRegions:
        """Get the list of Amazon AWS regions."""
        return await self._get(
            "/cdn/aws_regions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AwsRegions,
        )

    async def list_purge_statuses(
        self,
        *,
        cname: str | Omit = omit,
        from_created: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        purge_type: str | Omit = omit,
        status: str | Omit = omit,
        to_created: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CdnListPurgeStatusesResponse:
        """
        Get purges history.

        Args:
          cname: Purges associated with a specific resource CNAME.

              Example:

              - &cname=example.com

          from_created: Start date and time of the requested time period (ISO 8601/RFC 3339 format,
              UTC.)

              Examples:

              - &`from_created`=2021-06-14T00:00:00Z
              - &`from_created`=2021-06-14T00:00:00.000Z

          limit: Maximum number of purges in the response.

          offset: Number of purge requests in the response to skip starting from the beginning of
              the requested period.

          purge_type: Purge requests with a certain purge type.

              Possible values:

              - **`purge_by_pattern`** - Purge by Pattern.
              - **`purge_by_url`** - Purge by URL.
              - **`purge_all`** - Purge All.

          status: Purge with a certain status.

              Possible values:

              - **In progress**
              - **Successful**
              - **Failed**
              - **Status report disabled**

          to_created: End date and time of the requested time period (ISO 8601/RFC 3339 format, UTC.)

              Examples:

              - &`to_created`=2021-06-15T00:00:00Z
              - &`to_created`=2021-06-15T00:00:00.000Z

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/cdn/purge_statuses",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cname": cname,
                        "from_created": from_created,
                        "limit": limit,
                        "offset": offset,
                        "purge_type": purge_type,
                        "status": status,
                        "to_created": to_created,
                    },
                    cdn_list_purge_statuses_params.CdnListPurgeStatusesParams,
                ),
            ),
            cast_to=CdnListPurgeStatusesResponse,
        )

    async def update_account(
        self,
        *,
        utilization_level: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CdnAccount:
        """
        Change information about CDN service.

        Args:
          utilization_level: CDN traffic usage limit in gigabytes.

              When the limit is reached, we will send an email notification.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/cdn/clients/me",
            body=await async_maybe_transform(
                {"utilization_level": utilization_level}, cdn_update_account_params.CdnUpdateAccountParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CdnAccount,
        )


class CdnResourceWithRawResponse:
    def __init__(self, cdn: CdnResource) -> None:
        self._cdn = cdn

        self.get_account_limits = to_raw_response_wrapper(
            cdn.get_account_limits,
        )
        self.get_account_overview = to_raw_response_wrapper(
            cdn.get_account_overview,
        )
        self.get_available_features = to_raw_response_wrapper(
            cdn.get_available_features,
        )
        self.list_alibaba_regions = to_raw_response_wrapper(
            cdn.list_alibaba_regions,
        )
        self.list_aws_regions = to_raw_response_wrapper(
            cdn.list_aws_regions,
        )
        self.list_purge_statuses = to_raw_response_wrapper(
            cdn.list_purge_statuses,
        )
        self.update_account = to_raw_response_wrapper(
            cdn.update_account,
        )

    @cached_property
    def resources(self) -> ResourcesResourceWithRawResponse:
        return ResourcesResourceWithRawResponse(self._cdn.resources)

    @cached_property
    def shields(self) -> ShieldsResourceWithRawResponse:
        return ShieldsResourceWithRawResponse(self._cdn.shields)

    @cached_property
    def origin_groups(self) -> OriginGroupsResourceWithRawResponse:
        return OriginGroupsResourceWithRawResponse(self._cdn.origin_groups)

    @cached_property
    def rule_templates(self) -> RuleTemplatesResourceWithRawResponse:
        return RuleTemplatesResourceWithRawResponse(self._cdn.rule_templates)

    @cached_property
    def certificates(self) -> CertificatesResourceWithRawResponse:
        return CertificatesResourceWithRawResponse(self._cdn.certificates)

    @cached_property
    def trusted_ca_certificates(self) -> TrustedCaCertificatesResourceWithRawResponse:
        return TrustedCaCertificatesResourceWithRawResponse(self._cdn.trusted_ca_certificates)

    @cached_property
    def audit_logs(self) -> AuditLogsResourceWithRawResponse:
        return AuditLogsResourceWithRawResponse(self._cdn.audit_logs)

    @cached_property
    def logs(self) -> LogsResourceWithRawResponse:
        return LogsResourceWithRawResponse(self._cdn.logs)

    @cached_property
    def logs_uploader(self) -> LogsUploaderResourceWithRawResponse:
        return LogsUploaderResourceWithRawResponse(self._cdn.logs_uploader)

    @cached_property
    def statistics(self) -> StatisticsResourceWithRawResponse:
        return StatisticsResourceWithRawResponse(self._cdn.statistics)

    @cached_property
    def network_capacity(self) -> NetworkCapacityResourceWithRawResponse:
        return NetworkCapacityResourceWithRawResponse(self._cdn.network_capacity)

    @cached_property
    def metrics(self) -> MetricsResourceWithRawResponse:
        return MetricsResourceWithRawResponse(self._cdn.metrics)

    @cached_property
    def ip_ranges(self) -> IPRangesResourceWithRawResponse:
        return IPRangesResourceWithRawResponse(self._cdn.ip_ranges)


class AsyncCdnResourceWithRawResponse:
    def __init__(self, cdn: AsyncCdnResource) -> None:
        self._cdn = cdn

        self.get_account_limits = async_to_raw_response_wrapper(
            cdn.get_account_limits,
        )
        self.get_account_overview = async_to_raw_response_wrapper(
            cdn.get_account_overview,
        )
        self.get_available_features = async_to_raw_response_wrapper(
            cdn.get_available_features,
        )
        self.list_alibaba_regions = async_to_raw_response_wrapper(
            cdn.list_alibaba_regions,
        )
        self.list_aws_regions = async_to_raw_response_wrapper(
            cdn.list_aws_regions,
        )
        self.list_purge_statuses = async_to_raw_response_wrapper(
            cdn.list_purge_statuses,
        )
        self.update_account = async_to_raw_response_wrapper(
            cdn.update_account,
        )

    @cached_property
    def resources(self) -> AsyncResourcesResourceWithRawResponse:
        return AsyncResourcesResourceWithRawResponse(self._cdn.resources)

    @cached_property
    def shields(self) -> AsyncShieldsResourceWithRawResponse:
        return AsyncShieldsResourceWithRawResponse(self._cdn.shields)

    @cached_property
    def origin_groups(self) -> AsyncOriginGroupsResourceWithRawResponse:
        return AsyncOriginGroupsResourceWithRawResponse(self._cdn.origin_groups)

    @cached_property
    def rule_templates(self) -> AsyncRuleTemplatesResourceWithRawResponse:
        return AsyncRuleTemplatesResourceWithRawResponse(self._cdn.rule_templates)

    @cached_property
    def certificates(self) -> AsyncCertificatesResourceWithRawResponse:
        return AsyncCertificatesResourceWithRawResponse(self._cdn.certificates)

    @cached_property
    def trusted_ca_certificates(self) -> AsyncTrustedCaCertificatesResourceWithRawResponse:
        return AsyncTrustedCaCertificatesResourceWithRawResponse(self._cdn.trusted_ca_certificates)

    @cached_property
    def audit_logs(self) -> AsyncAuditLogsResourceWithRawResponse:
        return AsyncAuditLogsResourceWithRawResponse(self._cdn.audit_logs)

    @cached_property
    def logs(self) -> AsyncLogsResourceWithRawResponse:
        return AsyncLogsResourceWithRawResponse(self._cdn.logs)

    @cached_property
    def logs_uploader(self) -> AsyncLogsUploaderResourceWithRawResponse:
        return AsyncLogsUploaderResourceWithRawResponse(self._cdn.logs_uploader)

    @cached_property
    def statistics(self) -> AsyncStatisticsResourceWithRawResponse:
        return AsyncStatisticsResourceWithRawResponse(self._cdn.statistics)

    @cached_property
    def network_capacity(self) -> AsyncNetworkCapacityResourceWithRawResponse:
        return AsyncNetworkCapacityResourceWithRawResponse(self._cdn.network_capacity)

    @cached_property
    def metrics(self) -> AsyncMetricsResourceWithRawResponse:
        return AsyncMetricsResourceWithRawResponse(self._cdn.metrics)

    @cached_property
    def ip_ranges(self) -> AsyncIPRangesResourceWithRawResponse:
        return AsyncIPRangesResourceWithRawResponse(self._cdn.ip_ranges)


class CdnResourceWithStreamingResponse:
    def __init__(self, cdn: CdnResource) -> None:
        self._cdn = cdn

        self.get_account_limits = to_streamed_response_wrapper(
            cdn.get_account_limits,
        )
        self.get_account_overview = to_streamed_response_wrapper(
            cdn.get_account_overview,
        )
        self.get_available_features = to_streamed_response_wrapper(
            cdn.get_available_features,
        )
        self.list_alibaba_regions = to_streamed_response_wrapper(
            cdn.list_alibaba_regions,
        )
        self.list_aws_regions = to_streamed_response_wrapper(
            cdn.list_aws_regions,
        )
        self.list_purge_statuses = to_streamed_response_wrapper(
            cdn.list_purge_statuses,
        )
        self.update_account = to_streamed_response_wrapper(
            cdn.update_account,
        )

    @cached_property
    def resources(self) -> ResourcesResourceWithStreamingResponse:
        return ResourcesResourceWithStreamingResponse(self._cdn.resources)

    @cached_property
    def shields(self) -> ShieldsResourceWithStreamingResponse:
        return ShieldsResourceWithStreamingResponse(self._cdn.shields)

    @cached_property
    def origin_groups(self) -> OriginGroupsResourceWithStreamingResponse:
        return OriginGroupsResourceWithStreamingResponse(self._cdn.origin_groups)

    @cached_property
    def rule_templates(self) -> RuleTemplatesResourceWithStreamingResponse:
        return RuleTemplatesResourceWithStreamingResponse(self._cdn.rule_templates)

    @cached_property
    def certificates(self) -> CertificatesResourceWithStreamingResponse:
        return CertificatesResourceWithStreamingResponse(self._cdn.certificates)

    @cached_property
    def trusted_ca_certificates(self) -> TrustedCaCertificatesResourceWithStreamingResponse:
        return TrustedCaCertificatesResourceWithStreamingResponse(self._cdn.trusted_ca_certificates)

    @cached_property
    def audit_logs(self) -> AuditLogsResourceWithStreamingResponse:
        return AuditLogsResourceWithStreamingResponse(self._cdn.audit_logs)

    @cached_property
    def logs(self) -> LogsResourceWithStreamingResponse:
        return LogsResourceWithStreamingResponse(self._cdn.logs)

    @cached_property
    def logs_uploader(self) -> LogsUploaderResourceWithStreamingResponse:
        return LogsUploaderResourceWithStreamingResponse(self._cdn.logs_uploader)

    @cached_property
    def statistics(self) -> StatisticsResourceWithStreamingResponse:
        return StatisticsResourceWithStreamingResponse(self._cdn.statistics)

    @cached_property
    def network_capacity(self) -> NetworkCapacityResourceWithStreamingResponse:
        return NetworkCapacityResourceWithStreamingResponse(self._cdn.network_capacity)

    @cached_property
    def metrics(self) -> MetricsResourceWithStreamingResponse:
        return MetricsResourceWithStreamingResponse(self._cdn.metrics)

    @cached_property
    def ip_ranges(self) -> IPRangesResourceWithStreamingResponse:
        return IPRangesResourceWithStreamingResponse(self._cdn.ip_ranges)


class AsyncCdnResourceWithStreamingResponse:
    def __init__(self, cdn: AsyncCdnResource) -> None:
        self._cdn = cdn

        self.get_account_limits = async_to_streamed_response_wrapper(
            cdn.get_account_limits,
        )
        self.get_account_overview = async_to_streamed_response_wrapper(
            cdn.get_account_overview,
        )
        self.get_available_features = async_to_streamed_response_wrapper(
            cdn.get_available_features,
        )
        self.list_alibaba_regions = async_to_streamed_response_wrapper(
            cdn.list_alibaba_regions,
        )
        self.list_aws_regions = async_to_streamed_response_wrapper(
            cdn.list_aws_regions,
        )
        self.list_purge_statuses = async_to_streamed_response_wrapper(
            cdn.list_purge_statuses,
        )
        self.update_account = async_to_streamed_response_wrapper(
            cdn.update_account,
        )

    @cached_property
    def resources(self) -> AsyncResourcesResourceWithStreamingResponse:
        return AsyncResourcesResourceWithStreamingResponse(self._cdn.resources)

    @cached_property
    def shields(self) -> AsyncShieldsResourceWithStreamingResponse:
        return AsyncShieldsResourceWithStreamingResponse(self._cdn.shields)

    @cached_property
    def origin_groups(self) -> AsyncOriginGroupsResourceWithStreamingResponse:
        return AsyncOriginGroupsResourceWithStreamingResponse(self._cdn.origin_groups)

    @cached_property
    def rule_templates(self) -> AsyncRuleTemplatesResourceWithStreamingResponse:
        return AsyncRuleTemplatesResourceWithStreamingResponse(self._cdn.rule_templates)

    @cached_property
    def certificates(self) -> AsyncCertificatesResourceWithStreamingResponse:
        return AsyncCertificatesResourceWithStreamingResponse(self._cdn.certificates)

    @cached_property
    def trusted_ca_certificates(self) -> AsyncTrustedCaCertificatesResourceWithStreamingResponse:
        return AsyncTrustedCaCertificatesResourceWithStreamingResponse(self._cdn.trusted_ca_certificates)

    @cached_property
    def audit_logs(self) -> AsyncAuditLogsResourceWithStreamingResponse:
        return AsyncAuditLogsResourceWithStreamingResponse(self._cdn.audit_logs)

    @cached_property
    def logs(self) -> AsyncLogsResourceWithStreamingResponse:
        return AsyncLogsResourceWithStreamingResponse(self._cdn.logs)

    @cached_property
    def logs_uploader(self) -> AsyncLogsUploaderResourceWithStreamingResponse:
        return AsyncLogsUploaderResourceWithStreamingResponse(self._cdn.logs_uploader)

    @cached_property
    def statistics(self) -> AsyncStatisticsResourceWithStreamingResponse:
        return AsyncStatisticsResourceWithStreamingResponse(self._cdn.statistics)

    @cached_property
    def network_capacity(self) -> AsyncNetworkCapacityResourceWithStreamingResponse:
        return AsyncNetworkCapacityResourceWithStreamingResponse(self._cdn.network_capacity)

    @cached_property
    def metrics(self) -> AsyncMetricsResourceWithStreamingResponse:
        return AsyncMetricsResourceWithStreamingResponse(self._cdn.metrics)

    @cached_property
    def ip_ranges(self) -> AsyncIPRangesResourceWithStreamingResponse:
        return AsyncIPRangesResourceWithStreamingResponse(self._cdn.ip_ranges)
