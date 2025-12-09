# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .metrics import (
    MetricsResource,
    AsyncMetricsResource,
    MetricsResourceWithRawResponse,
    AsyncMetricsResourceWithRawResponse,
    MetricsResourceWithStreamingResponse,
    AsyncMetricsResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .locations import (
    LocationsResource,
    AsyncLocationsResource,
    LocationsResourceWithRawResponse,
    AsyncLocationsResourceWithRawResponse,
    LocationsResourceWithStreamingResponse,
    AsyncLocationsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.dns import dns_lookup_params
from .zones.zones import (
    ZonesResource,
    AsyncZonesResource,
    ZonesResourceWithRawResponse,
    AsyncZonesResourceWithRawResponse,
    ZonesResourceWithStreamingResponse,
    AsyncZonesResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from .pickers.pickers import (
    PickersResource,
    AsyncPickersResource,
    PickersResourceWithRawResponse,
    AsyncPickersResourceWithRawResponse,
    PickersResourceWithStreamingResponse,
    AsyncPickersResourceWithStreamingResponse,
)
from .network_mappings import (
    NetworkMappingsResource,
    AsyncNetworkMappingsResource,
    NetworkMappingsResourceWithRawResponse,
    AsyncNetworkMappingsResourceWithRawResponse,
    NetworkMappingsResourceWithStreamingResponse,
    AsyncNetworkMappingsResourceWithStreamingResponse,
)
from ...types.dns.dns_lookup_response import DNSLookupResponse
from ...types.dns.dns_get_account_overview_response import DNSGetAccountOverviewResponse

__all__ = ["DNSResource", "AsyncDNSResource"]


class DNSResource(SyncAPIResource):
    @cached_property
    def locations(self) -> LocationsResource:
        return LocationsResource(self._client)

    @cached_property
    def metrics(self) -> MetricsResource:
        return MetricsResource(self._client)

    @cached_property
    def pickers(self) -> PickersResource:
        return PickersResource(self._client)

    @cached_property
    def zones(self) -> ZonesResource:
        return ZonesResource(self._client)

    @cached_property
    def network_mappings(self) -> NetworkMappingsResource:
        return NetworkMappingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> DNSResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return DNSResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DNSResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return DNSResourceWithStreamingResponse(self)

    def get_account_overview(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DNSGetAccountOverviewResponse:
        """Get info about client"""
        return self._get(
            "/dns/v2/platform/info",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DNSGetAccountOverviewResponse,
        )

    def lookup(
        self,
        *,
        name: str | Omit = omit,
        request_server: Literal["authoritative_dns", "google", "cloudflare", "open_dns", "quad9", "gcore"]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DNSLookupResponse:
        """
        Get the dns records from a specific domain or ip.

        Args:
          name: Domain name

          request_server: Server that will be used as resolver

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/dns/v2/lookup",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "name": name,
                        "request_server": request_server,
                    },
                    dns_lookup_params.DNSLookupParams,
                ),
            ),
            cast_to=DNSLookupResponse,
        )


class AsyncDNSResource(AsyncAPIResource):
    @cached_property
    def locations(self) -> AsyncLocationsResource:
        return AsyncLocationsResource(self._client)

    @cached_property
    def metrics(self) -> AsyncMetricsResource:
        return AsyncMetricsResource(self._client)

    @cached_property
    def pickers(self) -> AsyncPickersResource:
        return AsyncPickersResource(self._client)

    @cached_property
    def zones(self) -> AsyncZonesResource:
        return AsyncZonesResource(self._client)

    @cached_property
    def network_mappings(self) -> AsyncNetworkMappingsResource:
        return AsyncNetworkMappingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDNSResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDNSResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDNSResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncDNSResourceWithStreamingResponse(self)

    async def get_account_overview(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DNSGetAccountOverviewResponse:
        """Get info about client"""
        return await self._get(
            "/dns/v2/platform/info",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DNSGetAccountOverviewResponse,
        )

    async def lookup(
        self,
        *,
        name: str | Omit = omit,
        request_server: Literal["authoritative_dns", "google", "cloudflare", "open_dns", "quad9", "gcore"]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DNSLookupResponse:
        """
        Get the dns records from a specific domain or ip.

        Args:
          name: Domain name

          request_server: Server that will be used as resolver

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/dns/v2/lookup",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "name": name,
                        "request_server": request_server,
                    },
                    dns_lookup_params.DNSLookupParams,
                ),
            ),
            cast_to=DNSLookupResponse,
        )


class DNSResourceWithRawResponse:
    def __init__(self, dns: DNSResource) -> None:
        self._dns = dns

        self.get_account_overview = to_raw_response_wrapper(
            dns.get_account_overview,
        )
        self.lookup = to_raw_response_wrapper(
            dns.lookup,
        )

    @cached_property
    def locations(self) -> LocationsResourceWithRawResponse:
        return LocationsResourceWithRawResponse(self._dns.locations)

    @cached_property
    def metrics(self) -> MetricsResourceWithRawResponse:
        return MetricsResourceWithRawResponse(self._dns.metrics)

    @cached_property
    def pickers(self) -> PickersResourceWithRawResponse:
        return PickersResourceWithRawResponse(self._dns.pickers)

    @cached_property
    def zones(self) -> ZonesResourceWithRawResponse:
        return ZonesResourceWithRawResponse(self._dns.zones)

    @cached_property
    def network_mappings(self) -> NetworkMappingsResourceWithRawResponse:
        return NetworkMappingsResourceWithRawResponse(self._dns.network_mappings)


class AsyncDNSResourceWithRawResponse:
    def __init__(self, dns: AsyncDNSResource) -> None:
        self._dns = dns

        self.get_account_overview = async_to_raw_response_wrapper(
            dns.get_account_overview,
        )
        self.lookup = async_to_raw_response_wrapper(
            dns.lookup,
        )

    @cached_property
    def locations(self) -> AsyncLocationsResourceWithRawResponse:
        return AsyncLocationsResourceWithRawResponse(self._dns.locations)

    @cached_property
    def metrics(self) -> AsyncMetricsResourceWithRawResponse:
        return AsyncMetricsResourceWithRawResponse(self._dns.metrics)

    @cached_property
    def pickers(self) -> AsyncPickersResourceWithRawResponse:
        return AsyncPickersResourceWithRawResponse(self._dns.pickers)

    @cached_property
    def zones(self) -> AsyncZonesResourceWithRawResponse:
        return AsyncZonesResourceWithRawResponse(self._dns.zones)

    @cached_property
    def network_mappings(self) -> AsyncNetworkMappingsResourceWithRawResponse:
        return AsyncNetworkMappingsResourceWithRawResponse(self._dns.network_mappings)


class DNSResourceWithStreamingResponse:
    def __init__(self, dns: DNSResource) -> None:
        self._dns = dns

        self.get_account_overview = to_streamed_response_wrapper(
            dns.get_account_overview,
        )
        self.lookup = to_streamed_response_wrapper(
            dns.lookup,
        )

    @cached_property
    def locations(self) -> LocationsResourceWithStreamingResponse:
        return LocationsResourceWithStreamingResponse(self._dns.locations)

    @cached_property
    def metrics(self) -> MetricsResourceWithStreamingResponse:
        return MetricsResourceWithStreamingResponse(self._dns.metrics)

    @cached_property
    def pickers(self) -> PickersResourceWithStreamingResponse:
        return PickersResourceWithStreamingResponse(self._dns.pickers)

    @cached_property
    def zones(self) -> ZonesResourceWithStreamingResponse:
        return ZonesResourceWithStreamingResponse(self._dns.zones)

    @cached_property
    def network_mappings(self) -> NetworkMappingsResourceWithStreamingResponse:
        return NetworkMappingsResourceWithStreamingResponse(self._dns.network_mappings)


class AsyncDNSResourceWithStreamingResponse:
    def __init__(self, dns: AsyncDNSResource) -> None:
        self._dns = dns

        self.get_account_overview = async_to_streamed_response_wrapper(
            dns.get_account_overview,
        )
        self.lookup = async_to_streamed_response_wrapper(
            dns.lookup,
        )

    @cached_property
    def locations(self) -> AsyncLocationsResourceWithStreamingResponse:
        return AsyncLocationsResourceWithStreamingResponse(self._dns.locations)

    @cached_property
    def metrics(self) -> AsyncMetricsResourceWithStreamingResponse:
        return AsyncMetricsResourceWithStreamingResponse(self._dns.metrics)

    @cached_property
    def pickers(self) -> AsyncPickersResourceWithStreamingResponse:
        return AsyncPickersResourceWithStreamingResponse(self._dns.pickers)

    @cached_property
    def zones(self) -> AsyncZonesResourceWithStreamingResponse:
        return AsyncZonesResourceWithStreamingResponse(self._dns.zones)

    @cached_property
    def network_mappings(self) -> AsyncNetworkMappingsResourceWithStreamingResponse:
        return AsyncNetworkMappingsResourceWithStreamingResponse(self._dns.network_mappings)
