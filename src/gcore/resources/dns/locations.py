# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.dns.location_list_response import LocationListResponse
from ...types.dns.location_list_regions_response import LocationListRegionsResponse
from ...types.dns.location_list_countries_response import LocationListCountriesResponse
from ...types.dns.location_list_continents_response import LocationListContinentsResponse

__all__ = ["LocationsResource", "AsyncLocationsResource"]


class LocationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LocationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return LocationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LocationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return LocationsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LocationListResponse:
        """List of All locations continents/countries/regions."""
        return self._get(
            "/dns/v2/locations",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LocationListResponse,
        )

    def list_continents(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LocationListContinentsResponse:
        """List of All locations continents."""
        return self._get(
            "/dns/v2/locations/continents",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LocationListContinentsResponse,
        )

    def list_countries(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LocationListCountriesResponse:
        """List of All locations countries."""
        return self._get(
            "/dns/v2/locations/countries",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LocationListCountriesResponse,
        )

    def list_regions(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LocationListRegionsResponse:
        """List of All locations regions."""
        return self._get(
            "/dns/v2/locations/regions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LocationListRegionsResponse,
        )


class AsyncLocationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLocationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLocationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLocationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncLocationsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LocationListResponse:
        """List of All locations continents/countries/regions."""
        return await self._get(
            "/dns/v2/locations",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LocationListResponse,
        )

    async def list_continents(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LocationListContinentsResponse:
        """List of All locations continents."""
        return await self._get(
            "/dns/v2/locations/continents",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LocationListContinentsResponse,
        )

    async def list_countries(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LocationListCountriesResponse:
        """List of All locations countries."""
        return await self._get(
            "/dns/v2/locations/countries",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LocationListCountriesResponse,
        )

    async def list_regions(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LocationListRegionsResponse:
        """List of All locations regions."""
        return await self._get(
            "/dns/v2/locations/regions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LocationListRegionsResponse,
        )


class LocationsResourceWithRawResponse:
    def __init__(self, locations: LocationsResource) -> None:
        self._locations = locations

        self.list = to_raw_response_wrapper(
            locations.list,
        )
        self.list_continents = to_raw_response_wrapper(
            locations.list_continents,
        )
        self.list_countries = to_raw_response_wrapper(
            locations.list_countries,
        )
        self.list_regions = to_raw_response_wrapper(
            locations.list_regions,
        )


class AsyncLocationsResourceWithRawResponse:
    def __init__(self, locations: AsyncLocationsResource) -> None:
        self._locations = locations

        self.list = async_to_raw_response_wrapper(
            locations.list,
        )
        self.list_continents = async_to_raw_response_wrapper(
            locations.list_continents,
        )
        self.list_countries = async_to_raw_response_wrapper(
            locations.list_countries,
        )
        self.list_regions = async_to_raw_response_wrapper(
            locations.list_regions,
        )


class LocationsResourceWithStreamingResponse:
    def __init__(self, locations: LocationsResource) -> None:
        self._locations = locations

        self.list = to_streamed_response_wrapper(
            locations.list,
        )
        self.list_continents = to_streamed_response_wrapper(
            locations.list_continents,
        )
        self.list_countries = to_streamed_response_wrapper(
            locations.list_countries,
        )
        self.list_regions = to_streamed_response_wrapper(
            locations.list_regions,
        )


class AsyncLocationsResourceWithStreamingResponse:
    def __init__(self, locations: AsyncLocationsResource) -> None:
        self._locations = locations

        self.list = async_to_streamed_response_wrapper(
            locations.list,
        )
        self.list_continents = async_to_streamed_response_wrapper(
            locations.list_continents,
        )
        self.list_countries = async_to_streamed_response_wrapper(
            locations.list_countries,
        )
        self.list_regions = async_to_streamed_response_wrapper(
            locations.list_regions,
        )
