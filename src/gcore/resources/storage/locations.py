# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncOffsetPage, AsyncOffsetPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.storage import location_list_params
from ...types.storage.location import Location

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
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[Location]:
        """Returns available storage locations where you can create storages.

        Each location
        represents a geographic region with specific data center facilities.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/storage/provisioning/v2/locations",
            page=SyncOffsetPage[Location],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    location_list_params.LocationListParams,
                ),
            ),
            model=Location,
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

    def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Location, AsyncOffsetPage[Location]]:
        """Returns available storage locations where you can create storages.

        Each location
        represents a geographic region with specific data center facilities.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/storage/provisioning/v2/locations",
            page=AsyncOffsetPage[Location],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    location_list_params.LocationListParams,
                ),
            ),
            model=Location,
        )


class LocationsResourceWithRawResponse:
    def __init__(self, locations: LocationsResource) -> None:
        self._locations = locations

        self.list = to_raw_response_wrapper(
            locations.list,
        )


class AsyncLocationsResourceWithRawResponse:
    def __init__(self, locations: AsyncLocationsResource) -> None:
        self._locations = locations

        self.list = async_to_raw_response_wrapper(
            locations.list,
        )


class LocationsResourceWithStreamingResponse:
    def __init__(self, locations: LocationsResource) -> None:
        self._locations = locations

        self.list = to_streamed_response_wrapper(
            locations.list,
        )


class AsyncLocationsResourceWithStreamingResponse:
    def __init__(self, locations: AsyncLocationsResource) -> None:
        self._locations = locations

        self.list = async_to_streamed_response_wrapper(
            locations.list,
        )
