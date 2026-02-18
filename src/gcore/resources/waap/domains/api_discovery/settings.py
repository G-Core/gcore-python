# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.waap.domains.api_discovery import setting_update_params
from .....types.waap.domains.api_discovery.waap_api_discovery_settings import WaapAPIDiscoverySettings

__all__ = ["SettingsResource", "AsyncSettingsResource"]


class SettingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return SettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return SettingsResourceWithStreamingResponse(self)

    def update(
        self,
        domain_id: int,
        *,
        description_file_location: Optional[str] | Omit = omit,
        description_file_scan_enabled: Optional[bool] | Omit = omit,
        description_file_scan_interval_hours: Optional[int] | Omit = omit,
        traffic_scan_enabled: Optional[bool] | Omit = omit,
        traffic_scan_interval_hours: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapAPIDiscoverySettings:
        """
        Update the API discovery settings for a domain

        Args:
          domain_id: The domain ID

          description_file_location: The URL of the API description file. This will be periodically scanned if
              `descriptionFileScanEnabled` is enabled. Supported formats are YAML and JSON,
              and it must adhere to OpenAPI versions 2, 3, or 3.1.

          description_file_scan_enabled: Indicates if periodic scan of the description file is enabled

          description_file_scan_interval_hours: The interval in hours for scanning the description file

          traffic_scan_enabled: Indicates if traffic scan is enabled

          traffic_scan_interval_hours: The interval in hours for scanning the traffic

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/waap/v1/domains/{domain_id}/api-discovery/settings",
            body=maybe_transform(
                {
                    "description_file_location": description_file_location,
                    "description_file_scan_enabled": description_file_scan_enabled,
                    "description_file_scan_interval_hours": description_file_scan_interval_hours,
                    "traffic_scan_enabled": traffic_scan_enabled,
                    "traffic_scan_interval_hours": traffic_scan_interval_hours,
                },
                setting_update_params.SettingUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapAPIDiscoverySettings,
        )

    def get(
        self,
        domain_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapAPIDiscoverySettings:
        """
        Retrieve the API discovery settings for a domain

        Args:
          domain_id: The domain ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/waap/v1/domains/{domain_id}/api-discovery/settings",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapAPIDiscoverySettings,
        )


class AsyncSettingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncSettingsResourceWithStreamingResponse(self)

    async def update(
        self,
        domain_id: int,
        *,
        description_file_location: Optional[str] | Omit = omit,
        description_file_scan_enabled: Optional[bool] | Omit = omit,
        description_file_scan_interval_hours: Optional[int] | Omit = omit,
        traffic_scan_enabled: Optional[bool] | Omit = omit,
        traffic_scan_interval_hours: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapAPIDiscoverySettings:
        """
        Update the API discovery settings for a domain

        Args:
          domain_id: The domain ID

          description_file_location: The URL of the API description file. This will be periodically scanned if
              `descriptionFileScanEnabled` is enabled. Supported formats are YAML and JSON,
              and it must adhere to OpenAPI versions 2, 3, or 3.1.

          description_file_scan_enabled: Indicates if periodic scan of the description file is enabled

          description_file_scan_interval_hours: The interval in hours for scanning the description file

          traffic_scan_enabled: Indicates if traffic scan is enabled

          traffic_scan_interval_hours: The interval in hours for scanning the traffic

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/waap/v1/domains/{domain_id}/api-discovery/settings",
            body=await async_maybe_transform(
                {
                    "description_file_location": description_file_location,
                    "description_file_scan_enabled": description_file_scan_enabled,
                    "description_file_scan_interval_hours": description_file_scan_interval_hours,
                    "traffic_scan_enabled": traffic_scan_enabled,
                    "traffic_scan_interval_hours": traffic_scan_interval_hours,
                },
                setting_update_params.SettingUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapAPIDiscoverySettings,
        )

    async def get(
        self,
        domain_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapAPIDiscoverySettings:
        """
        Retrieve the API discovery settings for a domain

        Args:
          domain_id: The domain ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/waap/v1/domains/{domain_id}/api-discovery/settings",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapAPIDiscoverySettings,
        )


class SettingsResourceWithRawResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

        self.update = to_raw_response_wrapper(
            settings.update,
        )
        self.get = to_raw_response_wrapper(
            settings.get,
        )


class AsyncSettingsResourceWithRawResponse:
    def __init__(self, settings: AsyncSettingsResource) -> None:
        self._settings = settings

        self.update = async_to_raw_response_wrapper(
            settings.update,
        )
        self.get = async_to_raw_response_wrapper(
            settings.get,
        )


class SettingsResourceWithStreamingResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

        self.update = to_streamed_response_wrapper(
            settings.update,
        )
        self.get = to_streamed_response_wrapper(
            settings.get,
        )


class AsyncSettingsResourceWithStreamingResponse:
    def __init__(self, settings: AsyncSettingsResource) -> None:
        self._settings = settings

        self.update = async_to_streamed_response_wrapper(
            settings.update,
        )
        self.get = async_to_streamed_response_wrapper(
            settings.get,
        )
