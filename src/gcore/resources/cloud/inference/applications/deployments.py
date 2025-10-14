# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from .....types.cloud.task_id_list import TaskIDList
from .....types.cloud.inference.applications import deployment_create_params, deployment_update_params
from .....types.cloud.inference.applications.inference_application_deployment import InferenceApplicationDeployment
from .....types.cloud.inference.applications.inference_application_deployment_list import (
    InferenceApplicationDeploymentList,
)

__all__ = ["DeploymentsResource", "AsyncDeploymentsResource"]


class DeploymentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DeploymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return DeploymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DeploymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return DeploymentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        project_id: int | None = None,
        application_name: str,
        components_configuration: Dict[str, deployment_create_params.ComponentsConfiguration],
        name: str,
        regions: Iterable[int],
        api_keys: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Creates a new application deployment based on a selected catalog application.
        Specify the desired deployment name, target regions, and configuration for each
        component. The platform will provision the necessary resources and initialize
        the application accordingly.

        Args:
          project_id: Project ID

          application_name: Identifier of the application from the catalog

          components_configuration: Mapping of component names to their configuration (e.g., `"model": {...}`)

          name: Desired name for the new deployment

          regions: Geographical regions where the deployment should be created

          api_keys: List of API keys for the application

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        return self._post(
            f"/cloud/v3/inference/applications/{project_id}/deployments",
            body=maybe_transform(
                {
                    "application_name": application_name,
                    "components_configuration": components_configuration,
                    "name": name,
                    "regions": regions,
                    "api_keys": api_keys,
                },
                deployment_create_params.DeploymentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def update(
        self,
        deployment_name: str,
        *,
        project_id: int | None = None,
        api_keys: SequenceNotStr[str] | Omit = omit,
        components_configuration: Dict[str, Optional[deployment_update_params.ComponentsConfiguration]] | Omit = omit,
        regions: Iterable[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """Updates an existing application deployment.

        You can modify the target regions
        and update configurations for individual components. To disable a component, set
        its value to null. Only the provided fields will be updated; all others remain
        unchanged.

        Args:
          project_id: Project ID

          deployment_name: Name of deployment

          api_keys: List of API keys for the application

          components_configuration: Mapping of component names to their configuration (e.g., `"model": {...}`)

          regions: Geographical regions to be updated for the deployment

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not deployment_name:
            raise ValueError(f"Expected a non-empty value for `deployment_name` but received {deployment_name!r}")
        return self._patch(
            f"/cloud/v3/inference/applications/{project_id}/deployments/{deployment_name}",
            body=maybe_transform(
                {
                    "api_keys": api_keys,
                    "components_configuration": components_configuration,
                    "regions": regions,
                },
                deployment_update_params.DeploymentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def list(
        self,
        *,
        project_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InferenceApplicationDeploymentList:
        """
        Returns a list of your application deployments, including deployment names,
        associated catalog applications, regions, component configurations, and current
        status. Useful for monitoring and managing all active AI application instances.

        Args:
          project_id: Project ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        return self._get(
            f"/cloud/v3/inference/applications/{project_id}/deployments",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InferenceApplicationDeploymentList,
        )

    def delete(
        self,
        deployment_name: str,
        *,
        project_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Deletes an existing application deployment along with all associated resources.
        This action will permanently remove the deployment and **terminate all related
        inference instances** that are part of the application.

        Args:
          project_id: Project ID

          deployment_name: Name of deployment

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not deployment_name:
            raise ValueError(f"Expected a non-empty value for `deployment_name` but received {deployment_name!r}")
        return self._delete(
            f"/cloud/v3/inference/applications/{project_id}/deployments/{deployment_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def get(
        self,
        deployment_name: str,
        *,
        project_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InferenceApplicationDeployment:
        """Retrieves detailed information about a specific application deployment.

        The
        response includes the catalog application it was created from, deployment name,
        active regions, configuration of each component, and the current status of the
        deployment.

        Args:
          project_id: Project ID

          deployment_name: Name of deployment

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not deployment_name:
            raise ValueError(f"Expected a non-empty value for `deployment_name` but received {deployment_name!r}")
        return self._get(
            f"/cloud/v3/inference/applications/{project_id}/deployments/{deployment_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InferenceApplicationDeployment,
        )


class AsyncDeploymentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDeploymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDeploymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDeploymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncDeploymentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        project_id: int | None = None,
        application_name: str,
        components_configuration: Dict[str, deployment_create_params.ComponentsConfiguration],
        name: str,
        regions: Iterable[int],
        api_keys: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Creates a new application deployment based on a selected catalog application.
        Specify the desired deployment name, target regions, and configuration for each
        component. The platform will provision the necessary resources and initialize
        the application accordingly.

        Args:
          project_id: Project ID

          application_name: Identifier of the application from the catalog

          components_configuration: Mapping of component names to their configuration (e.g., `"model": {...}`)

          name: Desired name for the new deployment

          regions: Geographical regions where the deployment should be created

          api_keys: List of API keys for the application

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        return await self._post(
            f"/cloud/v3/inference/applications/{project_id}/deployments",
            body=await async_maybe_transform(
                {
                    "application_name": application_name,
                    "components_configuration": components_configuration,
                    "name": name,
                    "regions": regions,
                    "api_keys": api_keys,
                },
                deployment_create_params.DeploymentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def update(
        self,
        deployment_name: str,
        *,
        project_id: int | None = None,
        api_keys: SequenceNotStr[str] | Omit = omit,
        components_configuration: Dict[str, Optional[deployment_update_params.ComponentsConfiguration]] | Omit = omit,
        regions: Iterable[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """Updates an existing application deployment.

        You can modify the target regions
        and update configurations for individual components. To disable a component, set
        its value to null. Only the provided fields will be updated; all others remain
        unchanged.

        Args:
          project_id: Project ID

          deployment_name: Name of deployment

          api_keys: List of API keys for the application

          components_configuration: Mapping of component names to their configuration (e.g., `"model": {...}`)

          regions: Geographical regions to be updated for the deployment

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not deployment_name:
            raise ValueError(f"Expected a non-empty value for `deployment_name` but received {deployment_name!r}")
        return await self._patch(
            f"/cloud/v3/inference/applications/{project_id}/deployments/{deployment_name}",
            body=await async_maybe_transform(
                {
                    "api_keys": api_keys,
                    "components_configuration": components_configuration,
                    "regions": regions,
                },
                deployment_update_params.DeploymentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def list(
        self,
        *,
        project_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InferenceApplicationDeploymentList:
        """
        Returns a list of your application deployments, including deployment names,
        associated catalog applications, regions, component configurations, and current
        status. Useful for monitoring and managing all active AI application instances.

        Args:
          project_id: Project ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        return await self._get(
            f"/cloud/v3/inference/applications/{project_id}/deployments",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InferenceApplicationDeploymentList,
        )

    async def delete(
        self,
        deployment_name: str,
        *,
        project_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Deletes an existing application deployment along with all associated resources.
        This action will permanently remove the deployment and **terminate all related
        inference instances** that are part of the application.

        Args:
          project_id: Project ID

          deployment_name: Name of deployment

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not deployment_name:
            raise ValueError(f"Expected a non-empty value for `deployment_name` but received {deployment_name!r}")
        return await self._delete(
            f"/cloud/v3/inference/applications/{project_id}/deployments/{deployment_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def get(
        self,
        deployment_name: str,
        *,
        project_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InferenceApplicationDeployment:
        """Retrieves detailed information about a specific application deployment.

        The
        response includes the catalog application it was created from, deployment name,
        active regions, configuration of each component, and the current status of the
        deployment.

        Args:
          project_id: Project ID

          deployment_name: Name of deployment

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not deployment_name:
            raise ValueError(f"Expected a non-empty value for `deployment_name` but received {deployment_name!r}")
        return await self._get(
            f"/cloud/v3/inference/applications/{project_id}/deployments/{deployment_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InferenceApplicationDeployment,
        )


class DeploymentsResourceWithRawResponse:
    def __init__(self, deployments: DeploymentsResource) -> None:
        self._deployments = deployments

        self.create = to_raw_response_wrapper(
            deployments.create,
        )
        self.update = to_raw_response_wrapper(
            deployments.update,
        )
        self.list = to_raw_response_wrapper(
            deployments.list,
        )
        self.delete = to_raw_response_wrapper(
            deployments.delete,
        )
        self.get = to_raw_response_wrapper(
            deployments.get,
        )


class AsyncDeploymentsResourceWithRawResponse:
    def __init__(self, deployments: AsyncDeploymentsResource) -> None:
        self._deployments = deployments

        self.create = async_to_raw_response_wrapper(
            deployments.create,
        )
        self.update = async_to_raw_response_wrapper(
            deployments.update,
        )
        self.list = async_to_raw_response_wrapper(
            deployments.list,
        )
        self.delete = async_to_raw_response_wrapper(
            deployments.delete,
        )
        self.get = async_to_raw_response_wrapper(
            deployments.get,
        )


class DeploymentsResourceWithStreamingResponse:
    def __init__(self, deployments: DeploymentsResource) -> None:
        self._deployments = deployments

        self.create = to_streamed_response_wrapper(
            deployments.create,
        )
        self.update = to_streamed_response_wrapper(
            deployments.update,
        )
        self.list = to_streamed_response_wrapper(
            deployments.list,
        )
        self.delete = to_streamed_response_wrapper(
            deployments.delete,
        )
        self.get = to_streamed_response_wrapper(
            deployments.get,
        )


class AsyncDeploymentsResourceWithStreamingResponse:
    def __init__(self, deployments: AsyncDeploymentsResource) -> None:
        self._deployments = deployments

        self.create = async_to_streamed_response_wrapper(
            deployments.create,
        )
        self.update = async_to_streamed_response_wrapper(
            deployments.update,
        )
        self.list = async_to_streamed_response_wrapper(
            deployments.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            deployments.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            deployments.get,
        )
