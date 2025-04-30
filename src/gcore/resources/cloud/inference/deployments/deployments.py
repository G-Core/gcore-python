# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional

import httpx

from .logs import (
    LogsResource,
    AsyncLogsResource,
    LogsResourceWithRawResponse,
    AsyncLogsResourceWithRawResponse,
    LogsResourceWithStreamingResponse,
    AsyncLogsResourceWithStreamingResponse,
)
from ....._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from .....types.cloud.ingress_opts_param import IngressOptsParam
from .....types.cloud.inference.inference import Inference
from .....types.cloud.inference.inference_apikey_secret import InferenceApikeySecret

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

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return DeploymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DeploymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
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
        auth_enabled: bool | NotGiven = NOT_GIVEN,
        command: Optional[List[str]] | NotGiven = NOT_GIVEN,
        credentials_name: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        envs: Dict[str, str] | NotGiven = NOT_GIVEN,
        ingress_opts: Optional[IngressOptsParam] | NotGiven = NOT_GIVEN,
        logging: Optional[deployment_create_params.Logging] | NotGiven = NOT_GIVEN,
        probes: Optional[deployment_create_params.Probes] | NotGiven = NOT_GIVEN,
        api_timeout: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Create inference deployment

        Args:
          project_id: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments/post/parameters/0/schema'
              "$.paths['/cloud/v3/inference/{project_id}/deployments'].post.parameters[0].schema"

          containers: '#/components/schemas/InferenceInstanceInSerializerV3/properties/containers'
              "$.components.schemas.InferenceInstanceInSerializerV3.properties.containers"

          flavor_name: '#/components/schemas/InferenceInstanceInSerializerV3/properties/flavor_name'
              "$.components.schemas.InferenceInstanceInSerializerV3.properties.flavor_name"

          image: '#/components/schemas/InferenceInstanceInSerializerV3/properties/image'
              "$.components.schemas.InferenceInstanceInSerializerV3.properties.image"

          listening_port: '#/components/schemas/InferenceInstanceInSerializerV3/properties/listening_port'
              "$.components.schemas.InferenceInstanceInSerializerV3.properties.listening_port"

          name: '#/components/schemas/InferenceInstanceInSerializerV3/properties/name'
              "$.components.schemas.InferenceInstanceInSerializerV3.properties.name"

          auth_enabled: '#/components/schemas/InferenceInstanceInSerializerV3/properties/auth_enabled'
              "$.components.schemas.InferenceInstanceInSerializerV3.properties.auth_enabled"

          command: '#/components/schemas/InferenceInstanceInSerializerV3/properties/command/anyOf/0'
              "$.components.schemas.InferenceInstanceInSerializerV3.properties.command.anyOf[0]"

          credentials_name: '#/components/schemas/InferenceInstanceInSerializerV3/properties/credentials_name/anyOf/0'
              "$.components.schemas.InferenceInstanceInSerializerV3.properties.credentials_name.anyOf[0]"

          description: '#/components/schemas/InferenceInstanceInSerializerV3/properties/description/anyOf/0'
              "$.components.schemas.InferenceInstanceInSerializerV3.properties.description.anyOf[0]"

          envs: '#/components/schemas/InferenceInstanceInSerializerV3/properties/envs'
              "$.components.schemas.InferenceInstanceInSerializerV3.properties.envs"

          ingress_opts: '#/components/schemas/InferenceInstanceInSerializerV3/properties/ingress_opts/anyOf/0'
              "$.components.schemas.InferenceInstanceInSerializerV3.properties.ingress_opts.anyOf[0]"

          logging: '#/components/schemas/InferenceInstanceInSerializerV3/properties/logging/anyOf/0'
              "$.components.schemas.InferenceInstanceInSerializerV3.properties.logging.anyOf[0]"

          probes: '#/components/schemas/InferenceInstanceInSerializerV3/properties/probes/anyOf/0'
              "$.components.schemas.InferenceInstanceInSerializerV3.properties.probes.anyOf[0]"

          api_timeout: '#/components/schemas/InferenceInstanceInSerializerV3/properties/timeout/anyOf/0'
              "$.components.schemas.InferenceInstanceInSerializerV3.properties.timeout.anyOf[0]"

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
        auth_enabled: Optional[bool] | NotGiven = NOT_GIVEN,
        command: Optional[List[str]] | NotGiven = NOT_GIVEN,
        containers: Optional[Iterable[deployment_update_params.Container]] | NotGiven = NOT_GIVEN,
        credentials_name: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        envs: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        flavor_name: Optional[str] | NotGiven = NOT_GIVEN,
        image: Optional[str] | NotGiven = NOT_GIVEN,
        ingress_opts: Optional[IngressOptsParam] | NotGiven = NOT_GIVEN,
        listening_port: Optional[int] | NotGiven = NOT_GIVEN,
        logging: Optional[deployment_update_params.Logging] | NotGiven = NOT_GIVEN,
        probes: Optional[deployment_update_params.Probes] | NotGiven = NOT_GIVEN,
        api_timeout: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Update inference deployment

        Args:
          project_id: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments%2F%7Bdeployment_name%7D/patch/parameters/0/schema'
              "$.paths['/cloud/v3/inference/{project_id}/deployments/{deployment_name}'].patch.parameters[0].schema"

          deployment_name: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments%2F%7Bdeployment_name%7D/patch/parameters/1/schema'
              "$.paths['/cloud/v3/inference/{project_id}/deployments/{deployment_name}'].patch.parameters[1].schema"

          auth_enabled: '#/components/schemas/InferenceInstanceInUpdateSerializerV3/properties/auth_enabled/anyOf/0'
              "$.components.schemas.InferenceInstanceInUpdateSerializerV3.properties.auth_enabled.anyOf[0]"

          command: '#/components/schemas/InferenceInstanceInUpdateSerializerV3/properties/command/anyOf/0'
              "$.components.schemas.InferenceInstanceInUpdateSerializerV3.properties.command.anyOf[0]"

          containers: '#/components/schemas/InferenceInstanceInUpdateSerializerV3/properties/containers/anyOf/0'
              "$.components.schemas.InferenceInstanceInUpdateSerializerV3.properties.containers.anyOf[0]"

          credentials_name: '#/components/schemas/InferenceInstanceInUpdateSerializerV3/properties/credentials_name/anyOf/0'
              "$.components.schemas.InferenceInstanceInUpdateSerializerV3.properties.credentials_name.anyOf[0]"

          description: '#/components/schemas/InferenceInstanceInUpdateSerializerV3/properties/description/anyOf/0'
              "$.components.schemas.InferenceInstanceInUpdateSerializerV3.properties.description.anyOf[0]"

          envs: '#/components/schemas/InferenceInstanceInUpdateSerializerV3/properties/envs/anyOf/0'
              "$.components.schemas.InferenceInstanceInUpdateSerializerV3.properties.envs.anyOf[0]"

          flavor_name: '#/components/schemas/InferenceInstanceInUpdateSerializerV3/properties/flavor_name/anyOf/0'
              "$.components.schemas.InferenceInstanceInUpdateSerializerV3.properties.flavor_name.anyOf[0]"

          image: '#/components/schemas/InferenceInstanceInUpdateSerializerV3/properties/image/anyOf/0'
              "$.components.schemas.InferenceInstanceInUpdateSerializerV3.properties.image.anyOf[0]"

          ingress_opts: '#/components/schemas/InferenceInstanceInUpdateSerializerV3/properties/ingress_opts/anyOf/0'
              "$.components.schemas.InferenceInstanceInUpdateSerializerV3.properties.ingress_opts.anyOf[0]"

          listening_port: '#/components/schemas/InferenceInstanceInUpdateSerializerV3/properties/listening_port/anyOf/0'
              "$.components.schemas.InferenceInstanceInUpdateSerializerV3.properties.listening_port.anyOf[0]"

          logging: '#/components/schemas/InferenceInstanceInUpdateSerializerV3/properties/logging/anyOf/0'
              "$.components.schemas.InferenceInstanceInUpdateSerializerV3.properties.logging.anyOf[0]"

          probes: '#/components/schemas/InferenceInstanceInUpdateSerializerV3/properties/probes/anyOf/0'
              "$.components.schemas.InferenceInstanceInUpdateSerializerV3.properties.probes.anyOf[0]"

          api_timeout: '#/components/schemas/InferenceInstanceInUpdateSerializerV3/properties/timeout/anyOf/0'
              "$.components.schemas.InferenceInstanceInUpdateSerializerV3.properties.timeout.anyOf[0]"

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
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[Inference]:
        """
        List inference deployments

        Args:
          project_id: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments/get/parameters/0/schema'
              "$.paths['/cloud/v3/inference/{project_id}/deployments'].get.parameters[0].schema"

          limit: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments/get/parameters/1'
              "$.paths['/cloud/v3/inference/{project_id}/deployments'].get.parameters[1]"

          offset: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments/get/parameters/2'
              "$.paths['/cloud/v3/inference/{project_id}/deployments'].get.parameters[2]"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        return self._get_api_list(
            f"/cloud/v3/inference/{project_id}/deployments",
            page=SyncOffsetPage[Inference],
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
            model=Inference,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Delete inference deployment

        Args:
          project_id: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments%2F%7Bdeployment_name%7D/delete/parameters/0/schema'
              "$.paths['/cloud/v3/inference/{project_id}/deployments/{deployment_name}']['delete'].parameters[0].schema"

          deployment_name: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments%2F%7Bdeployment_name%7D/delete/parameters/1/schema'
              "$.paths['/cloud/v3/inference/{project_id}/deployments/{deployment_name}']['delete'].parameters[1].schema"

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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Inference:
        """
        Get inference deployment

        Args:
          project_id: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments%2F%7Bdeployment_name%7D/get/parameters/0/schema'
              "$.paths['/cloud/v3/inference/{project_id}/deployments/{deployment_name}'].get.parameters[0].schema"

          deployment_name: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments%2F%7Bdeployment_name%7D/get/parameters/1/schema'
              "$.paths['/cloud/v3/inference/{project_id}/deployments/{deployment_name}'].get.parameters[1].schema"

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
            cast_to=Inference,
        )

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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InferenceApikeySecret:
        """
        Get inference deployment API key

        Args:
          project_id: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments%2F%7Bdeployment_name%7D%2Fapikey/get/parameters/0/schema'
              "$.paths['/cloud/v3/inference/{project_id}/deployments/{deployment_name}/apikey'].get.parameters[0].schema"

          deployment_name: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments%2F%7Bdeployment_name%7D%2Fapikey/get/parameters/1/schema'
              "$.paths['/cloud/v3/inference/{project_id}/deployments/{deployment_name}/apikey'].get.parameters[1].schema"

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
            cast_to=InferenceApikeySecret,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
          project_id: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments%2F%7Bdeployment_name%7D%2Fstart/post/parameters/0/schema'
              "$.paths['/cloud/v3/inference/{project_id}/deployments/{deployment_name}/start'].post.parameters[0].schema"

          deployment_name: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments%2F%7Bdeployment_name%7D%2Fstart/post/parameters/1/schema'
              "$.paths['/cloud/v3/inference/{project_id}/deployments/{deployment_name}/start'].post.parameters[1].schema"

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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
          project_id: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments%2F%7Bdeployment_name%7D%2Fstop/post/parameters/0/schema'
              "$.paths['/cloud/v3/inference/{project_id}/deployments/{deployment_name}/stop'].post.parameters[0].schema"

          deployment_name: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments%2F%7Bdeployment_name%7D%2Fstop/post/parameters/1/schema'
              "$.paths['/cloud/v3/inference/{project_id}/deployments/{deployment_name}/stop'].post.parameters[1].schema"

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


class AsyncDeploymentsResource(AsyncAPIResource):
    @cached_property
    def logs(self) -> AsyncLogsResource:
        return AsyncLogsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDeploymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDeploymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDeploymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
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
        auth_enabled: bool | NotGiven = NOT_GIVEN,
        command: Optional[List[str]] | NotGiven = NOT_GIVEN,
        credentials_name: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        envs: Dict[str, str] | NotGiven = NOT_GIVEN,
        ingress_opts: Optional[IngressOptsParam] | NotGiven = NOT_GIVEN,
        logging: Optional[deployment_create_params.Logging] | NotGiven = NOT_GIVEN,
        probes: Optional[deployment_create_params.Probes] | NotGiven = NOT_GIVEN,
        api_timeout: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Create inference deployment

        Args:
          project_id: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments/post/parameters/0/schema'
              "$.paths['/cloud/v3/inference/{project_id}/deployments'].post.parameters[0].schema"

          containers: '#/components/schemas/InferenceInstanceInSerializerV3/properties/containers'
              "$.components.schemas.InferenceInstanceInSerializerV3.properties.containers"

          flavor_name: '#/components/schemas/InferenceInstanceInSerializerV3/properties/flavor_name'
              "$.components.schemas.InferenceInstanceInSerializerV3.properties.flavor_name"

          image: '#/components/schemas/InferenceInstanceInSerializerV3/properties/image'
              "$.components.schemas.InferenceInstanceInSerializerV3.properties.image"

          listening_port: '#/components/schemas/InferenceInstanceInSerializerV3/properties/listening_port'
              "$.components.schemas.InferenceInstanceInSerializerV3.properties.listening_port"

          name: '#/components/schemas/InferenceInstanceInSerializerV3/properties/name'
              "$.components.schemas.InferenceInstanceInSerializerV3.properties.name"

          auth_enabled: '#/components/schemas/InferenceInstanceInSerializerV3/properties/auth_enabled'
              "$.components.schemas.InferenceInstanceInSerializerV3.properties.auth_enabled"

          command: '#/components/schemas/InferenceInstanceInSerializerV3/properties/command/anyOf/0'
              "$.components.schemas.InferenceInstanceInSerializerV3.properties.command.anyOf[0]"

          credentials_name: '#/components/schemas/InferenceInstanceInSerializerV3/properties/credentials_name/anyOf/0'
              "$.components.schemas.InferenceInstanceInSerializerV3.properties.credentials_name.anyOf[0]"

          description: '#/components/schemas/InferenceInstanceInSerializerV3/properties/description/anyOf/0'
              "$.components.schemas.InferenceInstanceInSerializerV3.properties.description.anyOf[0]"

          envs: '#/components/schemas/InferenceInstanceInSerializerV3/properties/envs'
              "$.components.schemas.InferenceInstanceInSerializerV3.properties.envs"

          ingress_opts: '#/components/schemas/InferenceInstanceInSerializerV3/properties/ingress_opts/anyOf/0'
              "$.components.schemas.InferenceInstanceInSerializerV3.properties.ingress_opts.anyOf[0]"

          logging: '#/components/schemas/InferenceInstanceInSerializerV3/properties/logging/anyOf/0'
              "$.components.schemas.InferenceInstanceInSerializerV3.properties.logging.anyOf[0]"

          probes: '#/components/schemas/InferenceInstanceInSerializerV3/properties/probes/anyOf/0'
              "$.components.schemas.InferenceInstanceInSerializerV3.properties.probes.anyOf[0]"

          api_timeout: '#/components/schemas/InferenceInstanceInSerializerV3/properties/timeout/anyOf/0'
              "$.components.schemas.InferenceInstanceInSerializerV3.properties.timeout.anyOf[0]"

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
        auth_enabled: Optional[bool] | NotGiven = NOT_GIVEN,
        command: Optional[List[str]] | NotGiven = NOT_GIVEN,
        containers: Optional[Iterable[deployment_update_params.Container]] | NotGiven = NOT_GIVEN,
        credentials_name: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        envs: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        flavor_name: Optional[str] | NotGiven = NOT_GIVEN,
        image: Optional[str] | NotGiven = NOT_GIVEN,
        ingress_opts: Optional[IngressOptsParam] | NotGiven = NOT_GIVEN,
        listening_port: Optional[int] | NotGiven = NOT_GIVEN,
        logging: Optional[deployment_update_params.Logging] | NotGiven = NOT_GIVEN,
        probes: Optional[deployment_update_params.Probes] | NotGiven = NOT_GIVEN,
        api_timeout: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Update inference deployment

        Args:
          project_id: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments%2F%7Bdeployment_name%7D/patch/parameters/0/schema'
              "$.paths['/cloud/v3/inference/{project_id}/deployments/{deployment_name}'].patch.parameters[0].schema"

          deployment_name: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments%2F%7Bdeployment_name%7D/patch/parameters/1/schema'
              "$.paths['/cloud/v3/inference/{project_id}/deployments/{deployment_name}'].patch.parameters[1].schema"

          auth_enabled: '#/components/schemas/InferenceInstanceInUpdateSerializerV3/properties/auth_enabled/anyOf/0'
              "$.components.schemas.InferenceInstanceInUpdateSerializerV3.properties.auth_enabled.anyOf[0]"

          command: '#/components/schemas/InferenceInstanceInUpdateSerializerV3/properties/command/anyOf/0'
              "$.components.schemas.InferenceInstanceInUpdateSerializerV3.properties.command.anyOf[0]"

          containers: '#/components/schemas/InferenceInstanceInUpdateSerializerV3/properties/containers/anyOf/0'
              "$.components.schemas.InferenceInstanceInUpdateSerializerV3.properties.containers.anyOf[0]"

          credentials_name: '#/components/schemas/InferenceInstanceInUpdateSerializerV3/properties/credentials_name/anyOf/0'
              "$.components.schemas.InferenceInstanceInUpdateSerializerV3.properties.credentials_name.anyOf[0]"

          description: '#/components/schemas/InferenceInstanceInUpdateSerializerV3/properties/description/anyOf/0'
              "$.components.schemas.InferenceInstanceInUpdateSerializerV3.properties.description.anyOf[0]"

          envs: '#/components/schemas/InferenceInstanceInUpdateSerializerV3/properties/envs/anyOf/0'
              "$.components.schemas.InferenceInstanceInUpdateSerializerV3.properties.envs.anyOf[0]"

          flavor_name: '#/components/schemas/InferenceInstanceInUpdateSerializerV3/properties/flavor_name/anyOf/0'
              "$.components.schemas.InferenceInstanceInUpdateSerializerV3.properties.flavor_name.anyOf[0]"

          image: '#/components/schemas/InferenceInstanceInUpdateSerializerV3/properties/image/anyOf/0'
              "$.components.schemas.InferenceInstanceInUpdateSerializerV3.properties.image.anyOf[0]"

          ingress_opts: '#/components/schemas/InferenceInstanceInUpdateSerializerV3/properties/ingress_opts/anyOf/0'
              "$.components.schemas.InferenceInstanceInUpdateSerializerV3.properties.ingress_opts.anyOf[0]"

          listening_port: '#/components/schemas/InferenceInstanceInUpdateSerializerV3/properties/listening_port/anyOf/0'
              "$.components.schemas.InferenceInstanceInUpdateSerializerV3.properties.listening_port.anyOf[0]"

          logging: '#/components/schemas/InferenceInstanceInUpdateSerializerV3/properties/logging/anyOf/0'
              "$.components.schemas.InferenceInstanceInUpdateSerializerV3.properties.logging.anyOf[0]"

          probes: '#/components/schemas/InferenceInstanceInUpdateSerializerV3/properties/probes/anyOf/0'
              "$.components.schemas.InferenceInstanceInUpdateSerializerV3.properties.probes.anyOf[0]"

          api_timeout: '#/components/schemas/InferenceInstanceInUpdateSerializerV3/properties/timeout/anyOf/0'
              "$.components.schemas.InferenceInstanceInUpdateSerializerV3.properties.timeout.anyOf[0]"

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
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Inference, AsyncOffsetPage[Inference]]:
        """
        List inference deployments

        Args:
          project_id: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments/get/parameters/0/schema'
              "$.paths['/cloud/v3/inference/{project_id}/deployments'].get.parameters[0].schema"

          limit: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments/get/parameters/1'
              "$.paths['/cloud/v3/inference/{project_id}/deployments'].get.parameters[1]"

          offset: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments/get/parameters/2'
              "$.paths['/cloud/v3/inference/{project_id}/deployments'].get.parameters[2]"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        return self._get_api_list(
            f"/cloud/v3/inference/{project_id}/deployments",
            page=AsyncOffsetPage[Inference],
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
            model=Inference,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Delete inference deployment

        Args:
          project_id: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments%2F%7Bdeployment_name%7D/delete/parameters/0/schema'
              "$.paths['/cloud/v3/inference/{project_id}/deployments/{deployment_name}']['delete'].parameters[0].schema"

          deployment_name: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments%2F%7Bdeployment_name%7D/delete/parameters/1/schema'
              "$.paths['/cloud/v3/inference/{project_id}/deployments/{deployment_name}']['delete'].parameters[1].schema"

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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Inference:
        """
        Get inference deployment

        Args:
          project_id: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments%2F%7Bdeployment_name%7D/get/parameters/0/schema'
              "$.paths['/cloud/v3/inference/{project_id}/deployments/{deployment_name}'].get.parameters[0].schema"

          deployment_name: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments%2F%7Bdeployment_name%7D/get/parameters/1/schema'
              "$.paths['/cloud/v3/inference/{project_id}/deployments/{deployment_name}'].get.parameters[1].schema"

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
            cast_to=Inference,
        )

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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InferenceApikeySecret:
        """
        Get inference deployment API key

        Args:
          project_id: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments%2F%7Bdeployment_name%7D%2Fapikey/get/parameters/0/schema'
              "$.paths['/cloud/v3/inference/{project_id}/deployments/{deployment_name}/apikey'].get.parameters[0].schema"

          deployment_name: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments%2F%7Bdeployment_name%7D%2Fapikey/get/parameters/1/schema'
              "$.paths['/cloud/v3/inference/{project_id}/deployments/{deployment_name}/apikey'].get.parameters[1].schema"

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
            cast_to=InferenceApikeySecret,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
          project_id: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments%2F%7Bdeployment_name%7D%2Fstart/post/parameters/0/schema'
              "$.paths['/cloud/v3/inference/{project_id}/deployments/{deployment_name}/start'].post.parameters[0].schema"

          deployment_name: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments%2F%7Bdeployment_name%7D%2Fstart/post/parameters/1/schema'
              "$.paths['/cloud/v3/inference/{project_id}/deployments/{deployment_name}/start'].post.parameters[1].schema"

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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
          project_id: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments%2F%7Bdeployment_name%7D%2Fstop/post/parameters/0/schema'
              "$.paths['/cloud/v3/inference/{project_id}/deployments/{deployment_name}/stop'].post.parameters[0].schema"

          deployment_name: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments%2F%7Bdeployment_name%7D%2Fstop/post/parameters/1/schema'
              "$.paths['/cloud/v3/inference/{project_id}/deployments/{deployment_name}/stop'].post.parameters[1].schema"

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
        self.get_api_key = to_raw_response_wrapper(
            deployments.get_api_key,
        )
        self.start = to_raw_response_wrapper(
            deployments.start,
        )
        self.stop = to_raw_response_wrapper(
            deployments.stop,
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
        self.get_api_key = async_to_raw_response_wrapper(
            deployments.get_api_key,
        )
        self.start = async_to_raw_response_wrapper(
            deployments.start,
        )
        self.stop = async_to_raw_response_wrapper(
            deployments.stop,
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
        self.get_api_key = to_streamed_response_wrapper(
            deployments.get_api_key,
        )
        self.start = to_streamed_response_wrapper(
            deployments.start,
        )
        self.stop = to_streamed_response_wrapper(
            deployments.stop,
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
        self.get_api_key = async_to_streamed_response_wrapper(
            deployments.get_api_key,
        )
        self.start = async_to_streamed_response_wrapper(
            deployments.start,
        )
        self.stop = async_to_streamed_response_wrapper(
            deployments.stop,
        )

    @cached_property
    def logs(self) -> AsyncLogsResourceWithStreamingResponse:
        return AsyncLogsResourceWithStreamingResponse(self._deployments.logs)
