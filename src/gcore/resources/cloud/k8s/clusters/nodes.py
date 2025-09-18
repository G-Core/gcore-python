# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from .....types.cloud.k8s.clusters import node_list_params
from .....types.cloud.instance_list import InstanceList

__all__ = ["NodesResource", "AsyncNodesResource"]


class NodesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NodesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return NodesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NodesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return NodesResourceWithStreamingResponse(self)

    def list(
        self,
        cluster_name: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        with_ddos: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceList:
        """
        List k8s cluster nodes

        Args:
          with_ddos: Include DDoS profile information if set to true. Default is false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not cluster_name:
            raise ValueError(f"Expected a non-empty value for `cluster_name` but received {cluster_name!r}")
        return self._get(
            f"/cloud/v2/k8s/clusters/{project_id}/{region_id}/{cluster_name}/instances",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"with_ddos": with_ddos}, node_list_params.NodeListParams),
            ),
            cast_to=InstanceList,
        )

    def delete(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        cluster_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        After deletion, the node will be automatically recreated to maintain the desired
        pool size.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not cluster_name:
            raise ValueError(f"Expected a non-empty value for `cluster_name` but received {cluster_name!r}")
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/cloud/v2/k8s/clusters/{project_id}/{region_id}/{cluster_name}/instances/{instance_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncNodesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNodesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNodesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNodesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncNodesResourceWithStreamingResponse(self)

    async def list(
        self,
        cluster_name: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        with_ddos: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstanceList:
        """
        List k8s cluster nodes

        Args:
          with_ddos: Include DDoS profile information if set to true. Default is false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not cluster_name:
            raise ValueError(f"Expected a non-empty value for `cluster_name` but received {cluster_name!r}")
        return await self._get(
            f"/cloud/v2/k8s/clusters/{project_id}/{region_id}/{cluster_name}/instances",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"with_ddos": with_ddos}, node_list_params.NodeListParams),
            ),
            cast_to=InstanceList,
        )

    async def delete(
        self,
        instance_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        cluster_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        After deletion, the node will be automatically recreated to maintain the desired
        pool size.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not cluster_name:
            raise ValueError(f"Expected a non-empty value for `cluster_name` but received {cluster_name!r}")
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/cloud/v2/k8s/clusters/{project_id}/{region_id}/{cluster_name}/instances/{instance_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class NodesResourceWithRawResponse:
    def __init__(self, nodes: NodesResource) -> None:
        self._nodes = nodes

        self.list = to_raw_response_wrapper(
            nodes.list,
        )
        self.delete = to_raw_response_wrapper(
            nodes.delete,
        )


class AsyncNodesResourceWithRawResponse:
    def __init__(self, nodes: AsyncNodesResource) -> None:
        self._nodes = nodes

        self.list = async_to_raw_response_wrapper(
            nodes.list,
        )
        self.delete = async_to_raw_response_wrapper(
            nodes.delete,
        )


class NodesResourceWithStreamingResponse:
    def __init__(self, nodes: NodesResource) -> None:
        self._nodes = nodes

        self.list = to_streamed_response_wrapper(
            nodes.list,
        )
        self.delete = to_streamed_response_wrapper(
            nodes.delete,
        )


class AsyncNodesResourceWithStreamingResponse:
    def __init__(self, nodes: AsyncNodesResource) -> None:
        self._nodes = nodes

        self.list = async_to_streamed_response_wrapper(
            nodes.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            nodes.delete,
        )
