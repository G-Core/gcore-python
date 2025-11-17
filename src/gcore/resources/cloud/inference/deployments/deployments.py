# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import Dict, Iterable, Optional

import httpx

from .logs import (
    LogsResource,
    AsyncLogsResource,
    LogsResourceWithRawResponse,
    AsyncLogsResourceWithRawResponse,
    LogsResourceWithStreamingResponse,
    AsyncLogsResourceWithStreamingResponse,
)
from ....._types import NOT_GIVEN, Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .....pagination import SyncOffsetPage, AsyncOffsetPage
from ....._base_client import AsyncPaginator, make_request_options
from .....types.cloud.inference import deployment_list_params, deployment_create_params, deployment_update_params
from .....types.cloud.task_id_list import TaskIDList
from .....types.cloud.inference.inference_deployment import InferenceDeployment
from .....types.cloud.inference.inference_deployment_api_key import InferenceDeploymentAPIKey

__all__ = ["DeploymentsResource", "AsyncDeploymentsResource"]


class DeploymentsResource(SyncAPIResource):
    @cached_property
    def logs(self) -> LogsResource:
        return LogsResource(self._client)

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
        containers: Iterable[deployment_create_params.Container],
        flavor_name: str,
        image: str,
        listening_port: int,
        name: str,
        api_keys: SequenceNotStr[str] | Omit = omit,
        auth_enabled: bool | Omit = omit,
        command: Optional[SequenceNotStr[str]] | Omit = omit,
        credentials_name: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        envs: Dict[str, str] | Omit = omit,
        ingress_opts: Optional[deployment_create_params.IngressOpts] | Omit = omit,
        logging: Optional[deployment_create_params.Logging] | Omit = omit,
        probes: Optional[deployment_create_params.Probes] | Omit = omit,
        api_timeout: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Create inference deployment

        Args:
          project_id: Project ID

          containers: List of containers for the inference instance.

          flavor_name: Flavor name for the inference instance.

          image: Docker image for the inference instance. This field should contain the image
              name and tag in the format 'name:tag', e.g., 'nginx:latest'. It defaults to
              Docker Hub as the image registry, but any accessible Docker image URL can be
              specified.

          listening_port: Listening port for the inference instance.

          name: Inference instance name.

          api_keys: List of API keys for the inference instance. Multiple keys can be attached to
              one deployment.If `auth_enabled` and `api_keys` are both specified, a
              ValidationError will be raised.

          auth_enabled: Set to `true` to enable API key authentication for the inference instance.
              `"Authorization": "Bearer *****"` or `"X-Api-Key": "*****"` header is required
              for the requests to the instance if enabled. This field is deprecated and will
              be removed in the future. Use `api_keys` field instead.If `auth_enabled` and
              `api_keys` are both specified, a ValidationError will be raised.

          command: Command to be executed when running a container from an image.

          credentials_name: Registry credentials name

          description: Inference instance description.

          envs: Environment variables for the inference instance.

          ingress_opts: Ingress options for the inference instance

          logging: Logging configuration for the inference instance

          probes: Probes configured for all containers of the inference instance. If probes are
              not provided, and the `image_name` is from a the Model Catalog registry, the
              default probes will be used.

          api_timeout: Specifies the duration in seconds without any requests after which the
              containers will be downscaled to their minimum scale value as defined by
              `scale.min`. If set, this helps in optimizing resource usage by reducing the
              number of container instances during periods of inactivity. The default value
              when the parameter is not set is 120.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        return self._post(
            f"/cloud/v3/inference/{project_id}/deployments",
            body=maybe_transform(
                {
                    "containers": containers,
                    "flavor_name": flavor_name,
                    "image": image,
                    "listening_port": listening_port,
                    "name": name,
                    "api_keys": api_keys,
                    "auth_enabled": auth_enabled,
                    "command": command,
                    "credentials_name": credentials_name,
                    "description": description,
                    "envs": envs,
                    "ingress_opts": ingress_opts,
                    "logging": logging,
                    "probes": probes,
                    "api_timeout": api_timeout,
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
        api_keys: Optional[SequenceNotStr[str]] | Omit = omit,
        auth_enabled: bool | Omit = omit,
        command: Optional[SequenceNotStr[str]] | Omit = omit,
        containers: Optional[Iterable[deployment_update_params.Container]] | Omit = omit,
        credentials_name: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        envs: Optional[Dict[str, str]] | Omit = omit,
        flavor_name: str | Omit = omit,
        image: Optional[str] | Omit = omit,
        ingress_opts: Optional[deployment_update_params.IngressOpts] | Omit = omit,
        listening_port: Optional[int] | Omit = omit,
        logging: Optional[deployment_update_params.Logging] | Omit = omit,
        probes: Optional[deployment_update_params.Probes] | Omit = omit,
        api_timeout: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Update inference deployment

        Args:
          project_id: Project ID

          deployment_name: Inference instance name.

          api_keys: List of API keys for the inference instance. Multiple keys can be attached to
              one deployment.If `auth_enabled` and `api_keys` are both specified, a
              ValidationError will be raised.If `[]` is provided, the API keys will be removed
              and auth will be disabled on the deployment.

          auth_enabled: Set to `true` to enable API key authentication for the inference instance.
              `"Authorization": "Bearer *****"` or `"X-Api-Key": "*****"` header is required
              for the requests to the instance if enabled. This field is deprecated and will
              be removed in the future. Use `api_keys` field instead.If `auth_enabled` and
              `api_keys` are both specified, a ValidationError will be raised.

          command: Command to be executed when running a container from an image.

          containers: List of containers for the inference instance.

          credentials_name: Registry credentials name

          description: Inference instance description.

          envs: Environment variables for the inference instance.

          flavor_name: Flavor name for the inference instance.

          image: Docker image for the inference instance. This field should contain the image
              name and tag in the format 'name:tag', e.g., 'nginx:latest'. It defaults to
              Docker Hub as the image registry, but any accessible Docker image URL can be
              specified.

          ingress_opts: Ingress options for the inference instance

          listening_port: Listening port for the inference instance.

          logging: Logging configuration for the inference instance

          probes: Probes configured for all containers of the inference instance.

          api_timeout: Specifies the duration in seconds without any requests after which the
              containers will be downscaled to their minimum scale value as defined by
              `scale.min`. If set, this helps in optimizing resource usage by reducing the
              number of container instances during periods of inactivity. The default value
              when the parameter is not set is 120.

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
            f"/cloud/v3/inference/{project_id}/deployments/{deployment_name}",
            body=maybe_transform(
                {
                    "api_keys": api_keys,
                    "auth_enabled": auth_enabled,
                    "command": command,
                    "containers": containers,
                    "credentials_name": credentials_name,
                    "description": description,
                    "envs": envs,
                    "flavor_name": flavor_name,
                    "image": image,
                    "ingress_opts": ingress_opts,
                    "listening_port": listening_port,
                    "logging": logging,
                    "probes": probes,
                    "api_timeout": api_timeout,
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
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[InferenceDeployment]:
        """List inference deployments

        Args:
          project_id: Project ID

          limit: Optional.

        Limit the number of returned items

          offset: Optional. Offset value is used to exclude the first set of records from the
              result

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        return self._get_api_list(
            f"/cloud/v3/inference/{project_id}/deployments",
            page=SyncOffsetPage[InferenceDeployment],
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
                    deployment_list_params.DeploymentListParams,
                ),
            ),
            model=InferenceDeployment,
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
        Delete inference deployment

        Args:
          project_id: Project ID

          deployment_name: Inference instance name.

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
            f"/cloud/v3/inference/{project_id}/deployments/{deployment_name}",
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
    ) -> InferenceDeployment:
        """
        Get inference deployment

        Args:
          project_id: Project ID

          deployment_name: Inference instance name.

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
            f"/cloud/v3/inference/{project_id}/deployments/{deployment_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InferenceDeployment,
        )

    @typing_extensions.deprecated("deprecated")
    def get_api_key(
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
    ) -> InferenceDeploymentAPIKey:
        """
        Get inference deployment API key

        Args:
          project_id: Project ID

          deployment_name: Inference instance name.

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
            f"/cloud/v3/inference/{project_id}/deployments/{deployment_name}/apikey",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InferenceDeploymentAPIKey,
        )

    def start(
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
    ) -> None:
        """
        This operation initializes an inference deployment after it was stopped, making
        it available to handle inference requests again. The instance will launch with
        the **minimum** number of replicas defined in the scaling settings.

        - If the minimum replicas are set to **0**, the instance will initially start
          with **0** replicas.
        - It will automatically scale up when it receives requests or SQS messages,
          according to the configured scaling rules.

        Args:
          project_id: Project ID

          deployment_name: Inference instance name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not deployment_name:
            raise ValueError(f"Expected a non-empty value for `deployment_name` but received {deployment_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/cloud/v3/inference/{project_id}/deployments/{deployment_name}/start",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def stop(
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
    ) -> None:
        """
        This operation shuts down an inference deployment, making it unavailable for
        handling requests. The deployment will scale down to **0** replicas, overriding
        any minimum replica settings.

        - Once stopped, the deployment will **not** process any inference requests or
          SQS messages.
        - It will **not** restart automatically and must be started manually.
        - While stopped, the deployment will **not** incur any charges.

        Args:
          project_id: Project ID

          deployment_name: Inference instance name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not deployment_name:
            raise ValueError(f"Expected a non-empty value for `deployment_name` but received {deployment_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/cloud/v3/inference/{project_id}/deployments/{deployment_name}/stop",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        containers: Iterable[deployment_create_params.Container],
        flavor_name: str,
        image: str,
        listening_port: int,
        name: str,
        api_keys: SequenceNotStr[str] | Omit = omit,
        auth_enabled: bool | Omit = omit,
        command: Optional[SequenceNotStr[str]] | Omit = omit,
        credentials_name: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        envs: Dict[str, str] | Omit = omit,
        ingress_opts: Optional[deployment_create_params.IngressOpts] | Omit = omit,
        logging: Optional[deployment_create_params.Logging] | Omit = omit,
        probes: Optional[deployment_create_params.Probes] | Omit = omit,
        api_timeout: Optional[int] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> InferenceDeployment:
        response = self.create(
            project_id=project_id,
            containers=containers,
            flavor_name=flavor_name,
            image=image,
            listening_port=listening_port,
            name=name,
            api_keys=api_keys,
            auth_enabled=auth_enabled,
            command=command,
            credentials_name=credentials_name,
            description=description,
            envs=envs,
            ingress_opts=ingress_opts,
            logging=logging,
            probes=probes,
            api_timeout=api_timeout,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks or len(response.tasks) != 1:
            raise ValueError(f"Expected exactly one task to be created")
        task = self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        if (
            not task.created_resources
            or not task.created_resources.inference_instances
            or len(task.created_resources.inference_instances) != 1
        ):
            raise ValueError(f"Expected exactly one resource to be created in a task")
        return self.get(
            deployment_name=task.created_resources.inference_instances[0],
            project_id=project_id,
            extra_headers=extra_headers,
            timeout=timeout,
        )

    def update_and_poll(
        self,
        deployment_name: str,
        *,
        project_id: int | None = None,
        api_keys: Optional[SequenceNotStr[str]] | Omit = omit,
        auth_enabled: bool | Omit = omit,
        command: Optional[SequenceNotStr[str]] | Omit = omit,
        containers: Optional[Iterable[deployment_update_params.Container]] | Omit = omit,
        credentials_name: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        envs: Optional[Dict[str, str]] | Omit = omit,
        flavor_name: str | Omit = omit,
        image: Optional[str] | Omit = omit,
        ingress_opts: Optional[deployment_update_params.IngressOpts] | Omit = omit,
        listening_port: Optional[int] | Omit = omit,
        logging: Optional[deployment_update_params.Logging] | Omit = omit,
        probes: Optional[deployment_update_params.Probes] | Omit = omit,
        api_timeout: Optional[int] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> InferenceDeployment:
        """
        Update inference deployment and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.update(
            deployment_name=deployment_name,
            project_id=project_id,
            api_keys=api_keys,
            auth_enabled=auth_enabled,
            command=command,
            containers=containers,
            credentials_name=credentials_name,
            description=description,
            envs=envs,
            flavor_name=flavor_name,
            image=image,
            ingress_opts=ingress_opts,
            listening_port=listening_port,
            logging=logging,
            probes=probes,
            api_timeout=api_timeout,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks or len(response.tasks) < 1:
            raise ValueError("Expected at least one task to be created")
        self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        return self.get(
            deployment_name=deployment_name,
            project_id=project_id,
            extra_headers=extra_headers,
            timeout=timeout,
        )

    def delete_and_poll(
        self,
        deployment_name: str,
        *,
        project_id: int | None = None,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> None:
        """
        Delete inference deployment and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = self.delete(
            deployment_name=deployment_name,
            project_id=project_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks or len(response.tasks) < 1:
            raise ValueError("Expected at least one task to be created")
        self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )


class AsyncDeploymentsResource(AsyncAPIResource):
    @cached_property
    def logs(self) -> AsyncLogsResource:
        return AsyncLogsResource(self._client)

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
        containers: Iterable[deployment_create_params.Container],
        flavor_name: str,
        image: str,
        listening_port: int,
        name: str,
        api_keys: SequenceNotStr[str] | Omit = omit,
        auth_enabled: bool | Omit = omit,
        command: Optional[SequenceNotStr[str]] | Omit = omit,
        credentials_name: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        envs: Dict[str, str] | Omit = omit,
        ingress_opts: Optional[deployment_create_params.IngressOpts] | Omit = omit,
        logging: Optional[deployment_create_params.Logging] | Omit = omit,
        probes: Optional[deployment_create_params.Probes] | Omit = omit,
        api_timeout: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Create inference deployment

        Args:
          project_id: Project ID

          containers: List of containers for the inference instance.

          flavor_name: Flavor name for the inference instance.

          image: Docker image for the inference instance. This field should contain the image
              name and tag in the format 'name:tag', e.g., 'nginx:latest'. It defaults to
              Docker Hub as the image registry, but any accessible Docker image URL can be
              specified.

          listening_port: Listening port for the inference instance.

          name: Inference instance name.

          api_keys: List of API keys for the inference instance. Multiple keys can be attached to
              one deployment.If `auth_enabled` and `api_keys` are both specified, a
              ValidationError will be raised.

          auth_enabled: Set to `true` to enable API key authentication for the inference instance.
              `"Authorization": "Bearer *****"` or `"X-Api-Key": "*****"` header is required
              for the requests to the instance if enabled. This field is deprecated and will
              be removed in the future. Use `api_keys` field instead.If `auth_enabled` and
              `api_keys` are both specified, a ValidationError will be raised.

          command: Command to be executed when running a container from an image.

          credentials_name: Registry credentials name

          description: Inference instance description.

          envs: Environment variables for the inference instance.

          ingress_opts: Ingress options for the inference instance

          logging: Logging configuration for the inference instance

          probes: Probes configured for all containers of the inference instance. If probes are
              not provided, and the `image_name` is from a the Model Catalog registry, the
              default probes will be used.

          api_timeout: Specifies the duration in seconds without any requests after which the
              containers will be downscaled to their minimum scale value as defined by
              `scale.min`. If set, this helps in optimizing resource usage by reducing the
              number of container instances during periods of inactivity. The default value
              when the parameter is not set is 120.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        return await self._post(
            f"/cloud/v3/inference/{project_id}/deployments",
            body=await async_maybe_transform(
                {
                    "containers": containers,
                    "flavor_name": flavor_name,
                    "image": image,
                    "listening_port": listening_port,
                    "name": name,
                    "api_keys": api_keys,
                    "auth_enabled": auth_enabled,
                    "command": command,
                    "credentials_name": credentials_name,
                    "description": description,
                    "envs": envs,
                    "ingress_opts": ingress_opts,
                    "logging": logging,
                    "probes": probes,
                    "api_timeout": api_timeout,
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
        api_keys: Optional[SequenceNotStr[str]] | Omit = omit,
        auth_enabled: bool | Omit = omit,
        command: Optional[SequenceNotStr[str]] | Omit = omit,
        containers: Optional[Iterable[deployment_update_params.Container]] | Omit = omit,
        credentials_name: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        envs: Optional[Dict[str, str]] | Omit = omit,
        flavor_name: str | Omit = omit,
        image: Optional[str] | Omit = omit,
        ingress_opts: Optional[deployment_update_params.IngressOpts] | Omit = omit,
        listening_port: Optional[int] | Omit = omit,
        logging: Optional[deployment_update_params.Logging] | Omit = omit,
        probes: Optional[deployment_update_params.Probes] | Omit = omit,
        api_timeout: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Update inference deployment

        Args:
          project_id: Project ID

          deployment_name: Inference instance name.

          api_keys: List of API keys for the inference instance. Multiple keys can be attached to
              one deployment.If `auth_enabled` and `api_keys` are both specified, a
              ValidationError will be raised.If `[]` is provided, the API keys will be removed
              and auth will be disabled on the deployment.

          auth_enabled: Set to `true` to enable API key authentication for the inference instance.
              `"Authorization": "Bearer *****"` or `"X-Api-Key": "*****"` header is required
              for the requests to the instance if enabled. This field is deprecated and will
              be removed in the future. Use `api_keys` field instead.If `auth_enabled` and
              `api_keys` are both specified, a ValidationError will be raised.

          command: Command to be executed when running a container from an image.

          containers: List of containers for the inference instance.

          credentials_name: Registry credentials name

          description: Inference instance description.

          envs: Environment variables for the inference instance.

          flavor_name: Flavor name for the inference instance.

          image: Docker image for the inference instance. This field should contain the image
              name and tag in the format 'name:tag', e.g., 'nginx:latest'. It defaults to
              Docker Hub as the image registry, but any accessible Docker image URL can be
              specified.

          ingress_opts: Ingress options for the inference instance

          listening_port: Listening port for the inference instance.

          logging: Logging configuration for the inference instance

          probes: Probes configured for all containers of the inference instance.

          api_timeout: Specifies the duration in seconds without any requests after which the
              containers will be downscaled to their minimum scale value as defined by
              `scale.min`. If set, this helps in optimizing resource usage by reducing the
              number of container instances during periods of inactivity. The default value
              when the parameter is not set is 120.

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
            f"/cloud/v3/inference/{project_id}/deployments/{deployment_name}",
            body=await async_maybe_transform(
                {
                    "api_keys": api_keys,
                    "auth_enabled": auth_enabled,
                    "command": command,
                    "containers": containers,
                    "credentials_name": credentials_name,
                    "description": description,
                    "envs": envs,
                    "flavor_name": flavor_name,
                    "image": image,
                    "ingress_opts": ingress_opts,
                    "listening_port": listening_port,
                    "logging": logging,
                    "probes": probes,
                    "api_timeout": api_timeout,
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
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[InferenceDeployment, AsyncOffsetPage[InferenceDeployment]]:
        """List inference deployments

        Args:
          project_id: Project ID

          limit: Optional.

        Limit the number of returned items

          offset: Optional. Offset value is used to exclude the first set of records from the
              result

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        return self._get_api_list(
            f"/cloud/v3/inference/{project_id}/deployments",
            page=AsyncOffsetPage[InferenceDeployment],
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
                    deployment_list_params.DeploymentListParams,
                ),
            ),
            model=InferenceDeployment,
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
        Delete inference deployment

        Args:
          project_id: Project ID

          deployment_name: Inference instance name.

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
            f"/cloud/v3/inference/{project_id}/deployments/{deployment_name}",
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
    ) -> InferenceDeployment:
        """
        Get inference deployment

        Args:
          project_id: Project ID

          deployment_name: Inference instance name.

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
            f"/cloud/v3/inference/{project_id}/deployments/{deployment_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InferenceDeployment,
        )

    @typing_extensions.deprecated("deprecated")
    async def get_api_key(
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
    ) -> InferenceDeploymentAPIKey:
        """
        Get inference deployment API key

        Args:
          project_id: Project ID

          deployment_name: Inference instance name.

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
            f"/cloud/v3/inference/{project_id}/deployments/{deployment_name}/apikey",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InferenceDeploymentAPIKey,
        )

    async def start(
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
    ) -> None:
        """
        This operation initializes an inference deployment after it was stopped, making
        it available to handle inference requests again. The instance will launch with
        the **minimum** number of replicas defined in the scaling settings.

        - If the minimum replicas are set to **0**, the instance will initially start
          with **0** replicas.
        - It will automatically scale up when it receives requests or SQS messages,
          according to the configured scaling rules.

        Args:
          project_id: Project ID

          deployment_name: Inference instance name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not deployment_name:
            raise ValueError(f"Expected a non-empty value for `deployment_name` but received {deployment_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/cloud/v3/inference/{project_id}/deployments/{deployment_name}/start",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def stop(
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
    ) -> None:
        """
        This operation shuts down an inference deployment, making it unavailable for
        handling requests. The deployment will scale down to **0** replicas, overriding
        any minimum replica settings.

        - Once stopped, the deployment will **not** process any inference requests or
          SQS messages.
        - It will **not** restart automatically and must be started manually.
        - While stopped, the deployment will **not** incur any charges.

        Args:
          project_id: Project ID

          deployment_name: Inference instance name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not deployment_name:
            raise ValueError(f"Expected a non-empty value for `deployment_name` but received {deployment_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/cloud/v3/inference/{project_id}/deployments/{deployment_name}/stop",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        containers: Iterable[deployment_create_params.Container],
        flavor_name: str,
        image: str,
        listening_port: int,
        name: str,
        api_keys: SequenceNotStr[str] | Omit = omit,
        auth_enabled: bool | Omit = omit,
        command: Optional[SequenceNotStr[str]] | Omit = omit,
        credentials_name: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        envs: Dict[str, str] | Omit = omit,
        ingress_opts: Optional[deployment_create_params.IngressOpts] | Omit = omit,
        logging: Optional[deployment_create_params.Logging] | Omit = omit,
        probes: Optional[deployment_create_params.Probes] | Omit = omit,
        api_timeout: Optional[int] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> InferenceDeployment:
        response = await self.create(
            project_id=project_id,
            containers=containers,
            flavor_name=flavor_name,
            image=image,
            listening_port=listening_port,
            name=name,
            api_keys=api_keys,
            auth_enabled=auth_enabled,
            command=command,
            credentials_name=credentials_name,
            description=description,
            envs=envs,
            ingress_opts=ingress_opts,
            logging=logging,
            probes=probes,
            api_timeout=api_timeout,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks or len(response.tasks) != 1:
            raise ValueError(f"Expected exactly one task to be created")
        task = await self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        if (
            not task.created_resources
            or not task.created_resources.inference_instances
            or len(task.created_resources.inference_instances) != 1
        ):
            raise ValueError(f"Expected exactly one resource to be created in a task")
        return await self.get(
            deployment_name=task.created_resources.inference_instances[0],
            project_id=project_id,
            extra_headers=extra_headers,
            timeout=timeout,
        )

    async def update_and_poll(
        self,
        deployment_name: str,
        *,
        project_id: int | None = None,
        api_keys: Optional[SequenceNotStr[str]] | Omit = omit,
        auth_enabled: bool | Omit = omit,
        command: Optional[SequenceNotStr[str]] | Omit = omit,
        containers: Optional[Iterable[deployment_update_params.Container]] | Omit = omit,
        credentials_name: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        envs: Optional[Dict[str, str]] | Omit = omit,
        flavor_name: str | Omit = omit,
        image: Optional[str] | Omit = omit,
        ingress_opts: Optional[deployment_update_params.IngressOpts] | Omit = omit,
        listening_port: Optional[int] | Omit = omit,
        logging: Optional[deployment_update_params.Logging] | Omit = omit,
        probes: Optional[deployment_update_params.Probes] | Omit = omit,
        api_timeout: Optional[int] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> InferenceDeployment:
        """
        Update inference deployment and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.update(
            deployment_name=deployment_name,
            project_id=project_id,
            api_keys=api_keys,
            auth_enabled=auth_enabled,
            command=command,
            containers=containers,
            credentials_name=credentials_name,
            description=description,
            envs=envs,
            flavor_name=flavor_name,
            image=image,
            ingress_opts=ingress_opts,
            listening_port=listening_port,
            logging=logging,
            probes=probes,
            api_timeout=api_timeout,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks or len(response.tasks) < 1:
            raise ValueError("Expected at least one task to be created")
        await self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        return await self.get(
            deployment_name=deployment_name,
            project_id=project_id,
            extra_headers=extra_headers,
            timeout=timeout,
        )

    async def delete_and_poll(
        self,
        deployment_name: str,
        *,
        project_id: int | None = None,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> None:
        """
        Delete inference deployment and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.
        """
        response = await self.delete(
            deployment_name=deployment_name,
            project_id=project_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks or len(response.tasks) < 1:
            raise ValueError("Expected at least one task to be created")
        await self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
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
        self.get_api_key = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                deployments.get_api_key,  # pyright: ignore[reportDeprecated],
            )
        )
        self.start = to_raw_response_wrapper(
            deployments.start,
        )
        self.stop = to_raw_response_wrapper(
            deployments.stop,
        )
        self.create_and_poll = to_raw_response_wrapper(
            deployments.create_and_poll,
        )
        self.update_and_poll = to_raw_response_wrapper(
            deployments.update_and_poll,
        )
        self.delete_and_poll = to_raw_response_wrapper(
            deployments.delete_and_poll,
        )

    @cached_property
    def logs(self) -> LogsResourceWithRawResponse:
        return LogsResourceWithRawResponse(self._deployments.logs)


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
        self.get_api_key = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                deployments.get_api_key,  # pyright: ignore[reportDeprecated],
            )
        )
        self.start = async_to_raw_response_wrapper(
            deployments.start,
        )
        self.stop = async_to_raw_response_wrapper(
            deployments.stop,
        )
        self.create_and_poll = async_to_raw_response_wrapper(
            deployments.create_and_poll,
        )
        self.update_and_poll = async_to_raw_response_wrapper(
            deployments.update_and_poll,
        )
        self.delete_and_poll = async_to_raw_response_wrapper(
            deployments.delete_and_poll,
        )

    @cached_property
    def logs(self) -> AsyncLogsResourceWithRawResponse:
        return AsyncLogsResourceWithRawResponse(self._deployments.logs)


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
        self.get_api_key = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                deployments.get_api_key,  # pyright: ignore[reportDeprecated],
            )
        )
        self.start = to_streamed_response_wrapper(
            deployments.start,
        )
        self.stop = to_streamed_response_wrapper(
            deployments.stop,
        )
        self.create_and_poll = to_streamed_response_wrapper(
            deployments.create_and_poll,
        )
        self.update_and_poll = to_streamed_response_wrapper(
            deployments.update_and_poll,
        )
        self.delete_and_poll = to_streamed_response_wrapper(
            deployments.delete_and_poll,
        )

    @cached_property
    def logs(self) -> LogsResourceWithStreamingResponse:
        return LogsResourceWithStreamingResponse(self._deployments.logs)


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
        self.get_api_key = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                deployments.get_api_key,  # pyright: ignore[reportDeprecated],
            )
        )
        self.start = async_to_streamed_response_wrapper(
            deployments.start,
        )
        self.stop = async_to_streamed_response_wrapper(
            deployments.stop,
        )
        self.create_and_poll = async_to_streamed_response_wrapper(
            deployments.create_and_poll,
        )
        self.update_and_poll = async_to_streamed_response_wrapper(
            deployments.update_and_poll,
        )
        self.delete_and_poll = async_to_streamed_response_wrapper(
            deployments.delete_and_poll,
        )

    @cached_property
    def logs(self) -> AsyncLogsResourceWithStreamingResponse:
        return AsyncLogsResourceWithStreamingResponse(self._deployments.logs)
