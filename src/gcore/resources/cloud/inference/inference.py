# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .flavors import (
    FlavorsResource,
    AsyncFlavorsResource,
    FlavorsResourceWithRawResponse,
    AsyncFlavorsResourceWithRawResponse,
    FlavorsResourceWithStreamingResponse,
    AsyncFlavorsResourceWithStreamingResponse,
)
from .secrets import (
    SecretsResource,
    AsyncSecretsResource,
    SecretsResourceWithRawResponse,
    AsyncSecretsResourceWithRawResponse,
    SecretsResourceWithStreamingResponse,
    AsyncSecretsResourceWithStreamingResponse,
)
from .api_keys import (
    APIKeysResource,
    AsyncAPIKeysResource,
    APIKeysResourceWithRawResponse,
    AsyncAPIKeysResourceWithRawResponse,
    APIKeysResourceWithStreamingResponse,
    AsyncAPIKeysResourceWithStreamingResponse,
)
from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from .registry_credentials import (
    RegistryCredentialsResource,
    AsyncRegistryCredentialsResource,
    RegistryCredentialsResourceWithRawResponse,
    AsyncRegistryCredentialsResourceWithRawResponse,
    RegistryCredentialsResourceWithStreamingResponse,
    AsyncRegistryCredentialsResourceWithStreamingResponse,
)
from .deployments.deployments import (
    DeploymentsResource,
    AsyncDeploymentsResource,
    DeploymentsResourceWithRawResponse,
    AsyncDeploymentsResourceWithRawResponse,
    DeploymentsResourceWithStreamingResponse,
    AsyncDeploymentsResourceWithStreamingResponse,
)
from .applications.applications import (
    ApplicationsResource,
    AsyncApplicationsResource,
    ApplicationsResourceWithRawResponse,
    AsyncApplicationsResourceWithRawResponse,
    ApplicationsResourceWithStreamingResponse,
    AsyncApplicationsResourceWithStreamingResponse,
)
from ....types.cloud.inference_region_capacity_list import InferenceRegionCapacityList

__all__ = ["InferenceResource", "AsyncInferenceResource"]


class InferenceResource(SyncAPIResource):
    @cached_property
    def flavors(self) -> FlavorsResource:
        return FlavorsResource(self._client)

    @cached_property
    def deployments(self) -> DeploymentsResource:
        return DeploymentsResource(self._client)

    @cached_property
    def registry_credentials(self) -> RegistryCredentialsResource:
        return RegistryCredentialsResource(self._client)

    @cached_property
    def secrets(self) -> SecretsResource:
        return SecretsResource(self._client)

    @cached_property
    def api_keys(self) -> APIKeysResource:
        return APIKeysResource(self._client)

    @cached_property
    def applications(self) -> ApplicationsResource:
        return ApplicationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> InferenceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return InferenceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InferenceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return InferenceResourceWithStreamingResponse(self)

    def get_capacity_by_region(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InferenceRegionCapacityList:
        """Get inference capacity by region"""
        return self._get(
            "/cloud/v3/inference/capacity",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InferenceRegionCapacityList,
        )


class AsyncInferenceResource(AsyncAPIResource):
    @cached_property
    def flavors(self) -> AsyncFlavorsResource:
        return AsyncFlavorsResource(self._client)

    @cached_property
    def deployments(self) -> AsyncDeploymentsResource:
        return AsyncDeploymentsResource(self._client)

    @cached_property
    def registry_credentials(self) -> AsyncRegistryCredentialsResource:
        return AsyncRegistryCredentialsResource(self._client)

    @cached_property
    def secrets(self) -> AsyncSecretsResource:
        return AsyncSecretsResource(self._client)

    @cached_property
    def api_keys(self) -> AsyncAPIKeysResource:
        return AsyncAPIKeysResource(self._client)

    @cached_property
    def applications(self) -> AsyncApplicationsResource:
        return AsyncApplicationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncInferenceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInferenceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInferenceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncInferenceResourceWithStreamingResponse(self)

    async def get_capacity_by_region(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InferenceRegionCapacityList:
        """Get inference capacity by region"""
        return await self._get(
            "/cloud/v3/inference/capacity",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InferenceRegionCapacityList,
        )


class InferenceResourceWithRawResponse:
    def __init__(self, inference: InferenceResource) -> None:
        self._inference = inference

        self.get_capacity_by_region = to_raw_response_wrapper(
            inference.get_capacity_by_region,
        )

    @cached_property
    def flavors(self) -> FlavorsResourceWithRawResponse:
        return FlavorsResourceWithRawResponse(self._inference.flavors)

    @cached_property
    def deployments(self) -> DeploymentsResourceWithRawResponse:
        return DeploymentsResourceWithRawResponse(self._inference.deployments)

    @cached_property
    def registry_credentials(self) -> RegistryCredentialsResourceWithRawResponse:
        return RegistryCredentialsResourceWithRawResponse(self._inference.registry_credentials)

    @cached_property
    def secrets(self) -> SecretsResourceWithRawResponse:
        return SecretsResourceWithRawResponse(self._inference.secrets)

    @cached_property
    def api_keys(self) -> APIKeysResourceWithRawResponse:
        return APIKeysResourceWithRawResponse(self._inference.api_keys)

    @cached_property
    def applications(self) -> ApplicationsResourceWithRawResponse:
        return ApplicationsResourceWithRawResponse(self._inference.applications)


class AsyncInferenceResourceWithRawResponse:
    def __init__(self, inference: AsyncInferenceResource) -> None:
        self._inference = inference

        self.get_capacity_by_region = async_to_raw_response_wrapper(
            inference.get_capacity_by_region,
        )

    @cached_property
    def flavors(self) -> AsyncFlavorsResourceWithRawResponse:
        return AsyncFlavorsResourceWithRawResponse(self._inference.flavors)

    @cached_property
    def deployments(self) -> AsyncDeploymentsResourceWithRawResponse:
        return AsyncDeploymentsResourceWithRawResponse(self._inference.deployments)

    @cached_property
    def registry_credentials(self) -> AsyncRegistryCredentialsResourceWithRawResponse:
        return AsyncRegistryCredentialsResourceWithRawResponse(self._inference.registry_credentials)

    @cached_property
    def secrets(self) -> AsyncSecretsResourceWithRawResponse:
        return AsyncSecretsResourceWithRawResponse(self._inference.secrets)

    @cached_property
    def api_keys(self) -> AsyncAPIKeysResourceWithRawResponse:
        return AsyncAPIKeysResourceWithRawResponse(self._inference.api_keys)

    @cached_property
    def applications(self) -> AsyncApplicationsResourceWithRawResponse:
        return AsyncApplicationsResourceWithRawResponse(self._inference.applications)


class InferenceResourceWithStreamingResponse:
    def __init__(self, inference: InferenceResource) -> None:
        self._inference = inference

        self.get_capacity_by_region = to_streamed_response_wrapper(
            inference.get_capacity_by_region,
        )

    @cached_property
    def flavors(self) -> FlavorsResourceWithStreamingResponse:
        return FlavorsResourceWithStreamingResponse(self._inference.flavors)

    @cached_property
    def deployments(self) -> DeploymentsResourceWithStreamingResponse:
        return DeploymentsResourceWithStreamingResponse(self._inference.deployments)

    @cached_property
    def registry_credentials(self) -> RegistryCredentialsResourceWithStreamingResponse:
        return RegistryCredentialsResourceWithStreamingResponse(self._inference.registry_credentials)

    @cached_property
    def secrets(self) -> SecretsResourceWithStreamingResponse:
        return SecretsResourceWithStreamingResponse(self._inference.secrets)

    @cached_property
    def api_keys(self) -> APIKeysResourceWithStreamingResponse:
        return APIKeysResourceWithStreamingResponse(self._inference.api_keys)

    @cached_property
    def applications(self) -> ApplicationsResourceWithStreamingResponse:
        return ApplicationsResourceWithStreamingResponse(self._inference.applications)


class AsyncInferenceResourceWithStreamingResponse:
    def __init__(self, inference: AsyncInferenceResource) -> None:
        self._inference = inference

        self.get_capacity_by_region = async_to_streamed_response_wrapper(
            inference.get_capacity_by_region,
        )

    @cached_property
    def flavors(self) -> AsyncFlavorsResourceWithStreamingResponse:
        return AsyncFlavorsResourceWithStreamingResponse(self._inference.flavors)

    @cached_property
    def deployments(self) -> AsyncDeploymentsResourceWithStreamingResponse:
        return AsyncDeploymentsResourceWithStreamingResponse(self._inference.deployments)

    @cached_property
    def registry_credentials(self) -> AsyncRegistryCredentialsResourceWithStreamingResponse:
        return AsyncRegistryCredentialsResourceWithStreamingResponse(self._inference.registry_credentials)

    @cached_property
    def secrets(self) -> AsyncSecretsResourceWithStreamingResponse:
        return AsyncSecretsResourceWithStreamingResponse(self._inference.secrets)

    @cached_property
    def api_keys(self) -> AsyncAPIKeysResourceWithStreamingResponse:
        return AsyncAPIKeysResourceWithStreamingResponse(self._inference.api_keys)

    @cached_property
    def applications(self) -> AsyncApplicationsResourceWithStreamingResponse:
        return AsyncApplicationsResourceWithStreamingResponse(self._inference.applications)
