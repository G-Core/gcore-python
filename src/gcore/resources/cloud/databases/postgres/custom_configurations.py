# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import Body, Query, Headers, NotGiven, not_given
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
from .....types.cloud.databases.postgres import custom_configuration_validate_params
from .....types.cloud.databases.postgres.pg_conf_validation import PgConfValidation

__all__ = ["CustomConfigurationsResource", "AsyncCustomConfigurationsResource"]


class CustomConfigurationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CustomConfigurationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return CustomConfigurationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomConfigurationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return CustomConfigurationsResourceWithStreamingResponse(self)

    def validate(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        pg_conf: str,
        version: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PgConfValidation:
        """
        Validate a custom PostgreSQL configuration file.

        Args:
          pg_conf: PostgreSQL configuration

          version: PostgreSQL version

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return self._post(
            f"/cloud/v1/dbaas/postgres/validate_pg_conf/{project_id}/{region_id}",
            body=maybe_transform(
                {
                    "pg_conf": pg_conf,
                    "version": version,
                },
                custom_configuration_validate_params.CustomConfigurationValidateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PgConfValidation,
        )


class AsyncCustomConfigurationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCustomConfigurationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCustomConfigurationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomConfigurationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncCustomConfigurationsResourceWithStreamingResponse(self)

    async def validate(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        pg_conf: str,
        version: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PgConfValidation:
        """
        Validate a custom PostgreSQL configuration file.

        Args:
          pg_conf: PostgreSQL configuration

          version: PostgreSQL version

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return await self._post(
            f"/cloud/v1/dbaas/postgres/validate_pg_conf/{project_id}/{region_id}",
            body=await async_maybe_transform(
                {
                    "pg_conf": pg_conf,
                    "version": version,
                },
                custom_configuration_validate_params.CustomConfigurationValidateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PgConfValidation,
        )


class CustomConfigurationsResourceWithRawResponse:
    def __init__(self, custom_configurations: CustomConfigurationsResource) -> None:
        self._custom_configurations = custom_configurations

        self.validate = to_raw_response_wrapper(
            custom_configurations.validate,
        )


class AsyncCustomConfigurationsResourceWithRawResponse:
    def __init__(self, custom_configurations: AsyncCustomConfigurationsResource) -> None:
        self._custom_configurations = custom_configurations

        self.validate = async_to_raw_response_wrapper(
            custom_configurations.validate,
        )


class CustomConfigurationsResourceWithStreamingResponse:
    def __init__(self, custom_configurations: CustomConfigurationsResource) -> None:
        self._custom_configurations = custom_configurations

        self.validate = to_streamed_response_wrapper(
            custom_configurations.validate,
        )


class AsyncCustomConfigurationsResourceWithStreamingResponse:
    def __init__(self, custom_configurations: AsyncCustomConfigurationsResource) -> None:
        self._custom_configurations = custom_configurations

        self.validate = async_to_streamed_response_wrapper(
            custom_configurations.validate,
        )
