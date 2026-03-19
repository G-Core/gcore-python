# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import Body, Query, Headers, NotGiven, not_given
from ....._utils import path_template
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.cloud.k8s.k8s_cluster_kubeconfig import K8SClusterKubeconfig

__all__ = ["KubeconfigResource", "AsyncKubeconfigResource"]


class KubeconfigResource(SyncAPIResource):
    """
    Kubeconfig provides the necessary configuration and credentials to access a Kubernetes cluster using kubectl or other Kubernetes clients.
    """

    @cached_property
    def with_raw_response(self) -> KubeconfigResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return KubeconfigResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KubeconfigResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return KubeconfigResourceWithStreamingResponse(self)

    def get(
        self,
        cluster_name: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> K8SClusterKubeconfig:
        """
        Get k8s cluster kubeconfig

        Args:
          project_id: Project ID

          region_id: Region ID

          cluster_name: Cluster name

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
            path_template(
                "/cloud/v2/k8s/clusters/{project_id}/{region_id}/{cluster_name}/config",
                project_id=project_id,
                region_id=region_id,
                cluster_name=cluster_name,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=K8SClusterKubeconfig,
        )


class AsyncKubeconfigResource(AsyncAPIResource):
    """
    Kubeconfig provides the necessary configuration and credentials to access a Kubernetes cluster using kubectl or other Kubernetes clients.
    """

    @cached_property
    def with_raw_response(self) -> AsyncKubeconfigResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncKubeconfigResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKubeconfigResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncKubeconfigResourceWithStreamingResponse(self)

    async def get(
        self,
        cluster_name: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> K8SClusterKubeconfig:
        """
        Get k8s cluster kubeconfig

        Args:
          project_id: Project ID

          region_id: Region ID

          cluster_name: Cluster name

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
            path_template(
                "/cloud/v2/k8s/clusters/{project_id}/{region_id}/{cluster_name}/config",
                project_id=project_id,
                region_id=region_id,
                cluster_name=cluster_name,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=K8SClusterKubeconfig,
        )


class KubeconfigResourceWithRawResponse:
    def __init__(self, kubeconfig: KubeconfigResource) -> None:
        self._kubeconfig = kubeconfig

        self.get = to_raw_response_wrapper(
            kubeconfig.get,
        )


class AsyncKubeconfigResourceWithRawResponse:
    def __init__(self, kubeconfig: AsyncKubeconfigResource) -> None:
        self._kubeconfig = kubeconfig

        self.get = async_to_raw_response_wrapper(
            kubeconfig.get,
        )


class KubeconfigResourceWithStreamingResponse:
    def __init__(self, kubeconfig: KubeconfigResource) -> None:
        self._kubeconfig = kubeconfig

        self.get = to_streamed_response_wrapper(
            kubeconfig.get,
        )


class AsyncKubeconfigResourceWithStreamingResponse:
    def __init__(self, kubeconfig: AsyncKubeconfigResource) -> None:
        self._kubeconfig = kubeconfig

        self.get = async_to_streamed_response_wrapper(
            kubeconfig.get,
        )
