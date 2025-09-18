# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .tags import (
    TagsResource,
    AsyncTagsResource,
    TagsResourceWithRawResponse,
    AsyncTagsResourceWithRawResponse,
    TagsResourceWithStreamingResponse,
    AsyncTagsResourceWithStreamingResponse,
)
from ..._types import Body, Query, Headers, NotGiven, not_given
from .insights import (
    InsightsResource,
    AsyncInsightsResource,
    InsightsResourceWithRawResponse,
    AsyncInsightsResourceWithRawResponse,
    InsightsResourceWithStreamingResponse,
    AsyncInsightsResourceWithStreamingResponse,
)
from ..._compat import cached_property
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
from .organizations import (
    OrganizationsResource,
    AsyncOrganizationsResource,
    OrganizationsResourceWithRawResponse,
    AsyncOrganizationsResourceWithRawResponse,
    OrganizationsResourceWithStreamingResponse,
    AsyncOrganizationsResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from .advanced_rules import (
    AdvancedRulesResource,
    AsyncAdvancedRulesResource,
    AdvancedRulesResourceWithRawResponse,
    AsyncAdvancedRulesResourceWithRawResponse,
    AdvancedRulesResourceWithStreamingResponse,
    AsyncAdvancedRulesResourceWithStreamingResponse,
)
from .domains.domains import (
    DomainsResource,
    AsyncDomainsResource,
    DomainsResourceWithRawResponse,
    AsyncDomainsResourceWithRawResponse,
    DomainsResourceWithStreamingResponse,
    AsyncDomainsResourceWithStreamingResponse,
)
from .ip_info.ip_info import (
    IPInfoResource,
    AsyncIPInfoResource,
    IPInfoResourceWithRawResponse,
    AsyncIPInfoResourceWithRawResponse,
    IPInfoResourceWithStreamingResponse,
    AsyncIPInfoResourceWithStreamingResponse,
)
from .custom_page_sets import (
    CustomPageSetsResource,
    AsyncCustomPageSetsResource,
    CustomPageSetsResourceWithRawResponse,
    AsyncCustomPageSetsResourceWithRawResponse,
    CustomPageSetsResourceWithStreamingResponse,
    AsyncCustomPageSetsResourceWithStreamingResponse,
)
from ...types.waap.waap_get_account_overview_response import WaapGetAccountOverviewResponse

__all__ = ["WaapResource", "AsyncWaapResource"]


class WaapResource(SyncAPIResource):
    @cached_property
    def statistics(self) -> StatisticsResource:
        return StatisticsResource(self._client)

    @cached_property
    def domains(self) -> DomainsResource:
        return DomainsResource(self._client)

    @cached_property
    def custom_page_sets(self) -> CustomPageSetsResource:
        return CustomPageSetsResource(self._client)

    @cached_property
    def advanced_rules(self) -> AdvancedRulesResource:
        return AdvancedRulesResource(self._client)

    @cached_property
    def tags(self) -> TagsResource:
        return TagsResource(self._client)

    @cached_property
    def organizations(self) -> OrganizationsResource:
        return OrganizationsResource(self._client)

    @cached_property
    def insights(self) -> InsightsResource:
        return InsightsResource(self._client)

    @cached_property
    def ip_info(self) -> IPInfoResource:
        return IPInfoResource(self._client)

    @cached_property
    def with_raw_response(self) -> WaapResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return WaapResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WaapResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return WaapResourceWithStreamingResponse(self)

    def get_account_overview(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapGetAccountOverviewResponse:
        """Get information about WAAP service for the client"""
        return self._get(
            "/waap/v1/clients/me",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapGetAccountOverviewResponse,
        )


class AsyncWaapResource(AsyncAPIResource):
    @cached_property
    def statistics(self) -> AsyncStatisticsResource:
        return AsyncStatisticsResource(self._client)

    @cached_property
    def domains(self) -> AsyncDomainsResource:
        return AsyncDomainsResource(self._client)

    @cached_property
    def custom_page_sets(self) -> AsyncCustomPageSetsResource:
        return AsyncCustomPageSetsResource(self._client)

    @cached_property
    def advanced_rules(self) -> AsyncAdvancedRulesResource:
        return AsyncAdvancedRulesResource(self._client)

    @cached_property
    def tags(self) -> AsyncTagsResource:
        return AsyncTagsResource(self._client)

    @cached_property
    def organizations(self) -> AsyncOrganizationsResource:
        return AsyncOrganizationsResource(self._client)

    @cached_property
    def insights(self) -> AsyncInsightsResource:
        return AsyncInsightsResource(self._client)

    @cached_property
    def ip_info(self) -> AsyncIPInfoResource:
        return AsyncIPInfoResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWaapResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWaapResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWaapResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncWaapResourceWithStreamingResponse(self)

    async def get_account_overview(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapGetAccountOverviewResponse:
        """Get information about WAAP service for the client"""
        return await self._get(
            "/waap/v1/clients/me",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapGetAccountOverviewResponse,
        )


class WaapResourceWithRawResponse:
    def __init__(self, waap: WaapResource) -> None:
        self._waap = waap

        self.get_account_overview = to_raw_response_wrapper(
            waap.get_account_overview,
        )

    @cached_property
    def statistics(self) -> StatisticsResourceWithRawResponse:
        return StatisticsResourceWithRawResponse(self._waap.statistics)

    @cached_property
    def domains(self) -> DomainsResourceWithRawResponse:
        return DomainsResourceWithRawResponse(self._waap.domains)

    @cached_property
    def custom_page_sets(self) -> CustomPageSetsResourceWithRawResponse:
        return CustomPageSetsResourceWithRawResponse(self._waap.custom_page_sets)

    @cached_property
    def advanced_rules(self) -> AdvancedRulesResourceWithRawResponse:
        return AdvancedRulesResourceWithRawResponse(self._waap.advanced_rules)

    @cached_property
    def tags(self) -> TagsResourceWithRawResponse:
        return TagsResourceWithRawResponse(self._waap.tags)

    @cached_property
    def organizations(self) -> OrganizationsResourceWithRawResponse:
        return OrganizationsResourceWithRawResponse(self._waap.organizations)

    @cached_property
    def insights(self) -> InsightsResourceWithRawResponse:
        return InsightsResourceWithRawResponse(self._waap.insights)

    @cached_property
    def ip_info(self) -> IPInfoResourceWithRawResponse:
        return IPInfoResourceWithRawResponse(self._waap.ip_info)


class AsyncWaapResourceWithRawResponse:
    def __init__(self, waap: AsyncWaapResource) -> None:
        self._waap = waap

        self.get_account_overview = async_to_raw_response_wrapper(
            waap.get_account_overview,
        )

    @cached_property
    def statistics(self) -> AsyncStatisticsResourceWithRawResponse:
        return AsyncStatisticsResourceWithRawResponse(self._waap.statistics)

    @cached_property
    def domains(self) -> AsyncDomainsResourceWithRawResponse:
        return AsyncDomainsResourceWithRawResponse(self._waap.domains)

    @cached_property
    def custom_page_sets(self) -> AsyncCustomPageSetsResourceWithRawResponse:
        return AsyncCustomPageSetsResourceWithRawResponse(self._waap.custom_page_sets)

    @cached_property
    def advanced_rules(self) -> AsyncAdvancedRulesResourceWithRawResponse:
        return AsyncAdvancedRulesResourceWithRawResponse(self._waap.advanced_rules)

    @cached_property
    def tags(self) -> AsyncTagsResourceWithRawResponse:
        return AsyncTagsResourceWithRawResponse(self._waap.tags)

    @cached_property
    def organizations(self) -> AsyncOrganizationsResourceWithRawResponse:
        return AsyncOrganizationsResourceWithRawResponse(self._waap.organizations)

    @cached_property
    def insights(self) -> AsyncInsightsResourceWithRawResponse:
        return AsyncInsightsResourceWithRawResponse(self._waap.insights)

    @cached_property
    def ip_info(self) -> AsyncIPInfoResourceWithRawResponse:
        return AsyncIPInfoResourceWithRawResponse(self._waap.ip_info)


class WaapResourceWithStreamingResponse:
    def __init__(self, waap: WaapResource) -> None:
        self._waap = waap

        self.get_account_overview = to_streamed_response_wrapper(
            waap.get_account_overview,
        )

    @cached_property
    def statistics(self) -> StatisticsResourceWithStreamingResponse:
        return StatisticsResourceWithStreamingResponse(self._waap.statistics)

    @cached_property
    def domains(self) -> DomainsResourceWithStreamingResponse:
        return DomainsResourceWithStreamingResponse(self._waap.domains)

    @cached_property
    def custom_page_sets(self) -> CustomPageSetsResourceWithStreamingResponse:
        return CustomPageSetsResourceWithStreamingResponse(self._waap.custom_page_sets)

    @cached_property
    def advanced_rules(self) -> AdvancedRulesResourceWithStreamingResponse:
        return AdvancedRulesResourceWithStreamingResponse(self._waap.advanced_rules)

    @cached_property
    def tags(self) -> TagsResourceWithStreamingResponse:
        return TagsResourceWithStreamingResponse(self._waap.tags)

    @cached_property
    def organizations(self) -> OrganizationsResourceWithStreamingResponse:
        return OrganizationsResourceWithStreamingResponse(self._waap.organizations)

    @cached_property
    def insights(self) -> InsightsResourceWithStreamingResponse:
        return InsightsResourceWithStreamingResponse(self._waap.insights)

    @cached_property
    def ip_info(self) -> IPInfoResourceWithStreamingResponse:
        return IPInfoResourceWithStreamingResponse(self._waap.ip_info)


class AsyncWaapResourceWithStreamingResponse:
    def __init__(self, waap: AsyncWaapResource) -> None:
        self._waap = waap

        self.get_account_overview = async_to_streamed_response_wrapper(
            waap.get_account_overview,
        )

    @cached_property
    def statistics(self) -> AsyncStatisticsResourceWithStreamingResponse:
        return AsyncStatisticsResourceWithStreamingResponse(self._waap.statistics)

    @cached_property
    def domains(self) -> AsyncDomainsResourceWithStreamingResponse:
        return AsyncDomainsResourceWithStreamingResponse(self._waap.domains)

    @cached_property
    def custom_page_sets(self) -> AsyncCustomPageSetsResourceWithStreamingResponse:
        return AsyncCustomPageSetsResourceWithStreamingResponse(self._waap.custom_page_sets)

    @cached_property
    def advanced_rules(self) -> AsyncAdvancedRulesResourceWithStreamingResponse:
        return AsyncAdvancedRulesResourceWithStreamingResponse(self._waap.advanced_rules)

    @cached_property
    def tags(self) -> AsyncTagsResourceWithStreamingResponse:
        return AsyncTagsResourceWithStreamingResponse(self._waap.tags)

    @cached_property
    def organizations(self) -> AsyncOrganizationsResourceWithStreamingResponse:
        return AsyncOrganizationsResourceWithStreamingResponse(self._waap.organizations)

    @cached_property
    def insights(self) -> AsyncInsightsResourceWithStreamingResponse:
        return AsyncInsightsResourceWithStreamingResponse(self._waap.insights)

    @cached_property
    def ip_info(self) -> AsyncIPInfoResourceWithStreamingResponse:
        return AsyncIPInfoResourceWithStreamingResponse(self._waap.ip_info)
