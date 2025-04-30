# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import maybe_transform
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
from .....types.cloud.inference.deployments import log_list_params
from .....types.cloud.inference.inference_log import InferenceLog

__all__ = ["LogsResource", "AsyncLogsResource"]


class LogsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LogsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return LogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LogsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
        """
        return LogsResourceWithStreamingResponse(self)

    def list(
        self,
        deployment_name: str,
        *,
        project_id: int | None = None,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        order_by: Literal["time.asc", "time.desc"] | NotGiven = NOT_GIVEN,
        region_id: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[InferenceLog]:
        """
        Get inference deployment logs

        Args:
          project_id: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments%2F%7Bdeployment_name%7D%2Flogs/get/parameters/0/schema'
              "$.paths['/cloud/v3/inference/{project_id}/deployments/{deployment_name}/logs'].get.parameters[0].schema"

          deployment_name: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments%2F%7Bdeployment_name%7D%2Flogs/get/parameters/1/schema'
              "$.paths['/cloud/v3/inference/{project_id}/deployments/{deployment_name}/logs'].get.parameters[1].schema"

          limit: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments%2F%7Bdeployment_name%7D%2Flogs/get/parameters/2'
              "$.paths['/cloud/v3/inference/{project_id}/deployments/{deployment_name}/logs'].get.parameters[2]"

          offset: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments%2F%7Bdeployment_name%7D%2Flogs/get/parameters/3'
              "$.paths['/cloud/v3/inference/{project_id}/deployments/{deployment_name}/logs'].get.parameters[3]"

          order_by: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments%2F%7Bdeployment_name%7D%2Flogs/get/parameters/4'
              "$.paths['/cloud/v3/inference/{project_id}/deployments/{deployment_name}/logs'].get.parameters[4]"

          region_id: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments%2F%7Bdeployment_name%7D%2Flogs/get/parameters/5/schema/anyOf/0'
              "$.paths['/cloud/v3/inference/{project_id}/deployments/{deployment_name}/logs'].get.parameters[5].schema.anyOf[0]"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not deployment_name:
            raise ValueError(f"Expected a non-empty value for `deployment_name` but received {deployment_name!r}")
        return self._get_api_list(
            f"/cloud/v3/inference/{project_id}/deployments/{deployment_name}/logs",
            page=SyncOffsetPage[InferenceLog],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "order_by": order_by,
                        "region_id": region_id,
                    },
                    log_list_params.LogListParams,
                ),
            ),
            model=InferenceLog,
        )


class AsyncLogsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLogsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLogsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
        """
        return AsyncLogsResourceWithStreamingResponse(self)

    def list(
        self,
        deployment_name: str,
        *,
        project_id: int | None = None,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        order_by: Literal["time.asc", "time.desc"] | NotGiven = NOT_GIVEN,
        region_id: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[InferenceLog, AsyncOffsetPage[InferenceLog]]:
        """
        Get inference deployment logs

        Args:
          project_id: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments%2F%7Bdeployment_name%7D%2Flogs/get/parameters/0/schema'
              "$.paths['/cloud/v3/inference/{project_id}/deployments/{deployment_name}/logs'].get.parameters[0].schema"

          deployment_name: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments%2F%7Bdeployment_name%7D%2Flogs/get/parameters/1/schema'
              "$.paths['/cloud/v3/inference/{project_id}/deployments/{deployment_name}/logs'].get.parameters[1].schema"

          limit: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments%2F%7Bdeployment_name%7D%2Flogs/get/parameters/2'
              "$.paths['/cloud/v3/inference/{project_id}/deployments/{deployment_name}/logs'].get.parameters[2]"

          offset: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments%2F%7Bdeployment_name%7D%2Flogs/get/parameters/3'
              "$.paths['/cloud/v3/inference/{project_id}/deployments/{deployment_name}/logs'].get.parameters[3]"

          order_by: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments%2F%7Bdeployment_name%7D%2Flogs/get/parameters/4'
              "$.paths['/cloud/v3/inference/{project_id}/deployments/{deployment_name}/logs'].get.parameters[4]"

          region_id: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments%2F%7Bdeployment_name%7D%2Flogs/get/parameters/5/schema/anyOf/0'
              "$.paths['/cloud/v3/inference/{project_id}/deployments/{deployment_name}/logs'].get.parameters[5].schema.anyOf[0]"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not deployment_name:
            raise ValueError(f"Expected a non-empty value for `deployment_name` but received {deployment_name!r}")
        return self._get_api_list(
            f"/cloud/v3/inference/{project_id}/deployments/{deployment_name}/logs",
            page=AsyncOffsetPage[InferenceLog],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "order_by": order_by,
                        "region_id": region_id,
                    },
                    log_list_params.LogListParams,
                ),
            ),
            model=InferenceLog,
        )


class LogsResourceWithRawResponse:
    def __init__(self, logs: LogsResource) -> None:
        self._logs = logs

        self.list = to_raw_response_wrapper(
            logs.list,
        )


class AsyncLogsResourceWithRawResponse:
    def __init__(self, logs: AsyncLogsResource) -> None:
        self._logs = logs

        self.list = async_to_raw_response_wrapper(
            logs.list,
        )


class LogsResourceWithStreamingResponse:
    def __init__(self, logs: LogsResource) -> None:
        self._logs = logs

        self.list = to_streamed_response_wrapper(
            logs.list,
        )


class AsyncLogsResourceWithStreamingResponse:
    def __init__(self, logs: AsyncLogsResource) -> None:
        self._logs = logs

        self.list = async_to_streamed_response_wrapper(
            logs.list,
        )
