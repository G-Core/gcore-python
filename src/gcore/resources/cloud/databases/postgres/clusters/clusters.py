# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ......_types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ......_utils import maybe_transform, async_maybe_transform
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......pagination import SyncOffsetPage, AsyncOffsetPage
from .user_credentials import (
    UserCredentialsResource,
    AsyncUserCredentialsResource,
    UserCredentialsResourceWithRawResponse,
    AsyncUserCredentialsResourceWithRawResponse,
    UserCredentialsResourceWithStreamingResponse,
    AsyncUserCredentialsResourceWithStreamingResponse,
)
from ......_base_client import AsyncPaginator, make_request_options
from ......types.cloud.task_id_list import TaskIDList
from ......types.cloud.databases.postgres import cluster_list_params, cluster_create_params, cluster_update_params
from ......types.cloud.databases.postgres.postgres_cluster import PostgresCluster
from ......types.cloud.databases.postgres.postgres_cluster_short import PostgresClusterShort

__all__ = ["ClustersResource", "AsyncClustersResource"]


class ClustersResource(SyncAPIResource):
    @cached_property
    def user_credentials(self) -> UserCredentialsResource:
        return UserCredentialsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ClustersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return ClustersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClustersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return ClustersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        cluster_name: str,
        flavor: cluster_create_params.Flavor,
        high_availability: Optional[cluster_create_params.HighAvailability],
        network: cluster_create_params.Network,
        pg_server_configuration: cluster_create_params.PgServerConfiguration,
        storage: cluster_create_params.Storage,
        databases: Iterable[cluster_create_params.Database] | Omit = omit,
        users: Iterable[cluster_create_params.User] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Create a new PostgreSQL cluster with the specified configuration.

        Args:
          cluster_name: PostgreSQL cluster name

          flavor: Instance RAM and CPU

          high_availability: High Availability settings

          pg_server_configuration: PosgtreSQL cluster configuration

          storage: Cluster's storage configuration

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
            f"/cloud/v1/dbaas/postgres/clusters/{project_id}/{region_id}",
            body=maybe_transform(
                {
                    "cluster_name": cluster_name,
                    "flavor": flavor,
                    "high_availability": high_availability,
                    "network": network,
                    "pg_server_configuration": pg_server_configuration,
                    "storage": storage,
                    "databases": databases,
                    "users": users,
                },
                cluster_create_params.ClusterCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def update(
        self,
        cluster_name: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        databases: Iterable[cluster_update_params.Database] | Omit = omit,
        flavor: Optional[cluster_update_params.Flavor] | Omit = omit,
        high_availability: Optional[cluster_update_params.HighAvailability] | Omit = omit,
        network: Optional[cluster_update_params.Network] | Omit = omit,
        pg_server_configuration: Optional[cluster_update_params.PgServerConfiguration] | Omit = omit,
        storage: Optional[cluster_update_params.Storage] | Omit = omit,
        users: Iterable[cluster_update_params.User] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Update the configuration of an existing PostgreSQL cluster.

        Args:
          flavor: New instance RAM and CPU

          high_availability: New High Availability settings

          pg_server_configuration: New PosgtreSQL cluster configuration

          storage: New storage configuration

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
        return self._patch(
            f"/cloud/v1/dbaas/postgres/clusters/{project_id}/{region_id}/{cluster_name}",
            body=maybe_transform(
                {
                    "databases": databases,
                    "flavor": flavor,
                    "high_availability": high_availability,
                    "network": network,
                    "pg_server_configuration": pg_server_configuration,
                    "storage": storage,
                    "users": users,
                },
                cluster_update_params.ClusterUpdateParams,
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
        region_id: int | None = None,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[PostgresClusterShort]:
        """List all PostgreSQL clusters in the specified project and region.

        Results can be
        filtered by search query and paginated.

        Args:
          limit: Maximum number of clusters to return

          offset: Number of clusters to skip

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return self._get_api_list(
            f"/cloud/v1/dbaas/postgres/clusters/{project_id}/{region_id}",
            page=SyncOffsetPage[PostgresClusterShort],
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
                    cluster_list_params.ClusterListParams,
                ),
            ),
            model=PostgresClusterShort,
        )

    def delete(
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
    ) -> TaskIDList:
        """
        Delete a PostgreSQL cluster and all its associated resources.

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
        return self._delete(
            f"/cloud/v1/dbaas/postgres/clusters/{project_id}/{region_id}/{cluster_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

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
    ) -> PostgresCluster:
        """
        Get detailed information about a specific PostgreSQL cluster.

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
        return self._get(
            f"/cloud/v1/dbaas/postgres/clusters/{project_id}/{region_id}/{cluster_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostgresCluster,
        )


class AsyncClustersResource(AsyncAPIResource):
    @cached_property
    def user_credentials(self) -> AsyncUserCredentialsResource:
        return AsyncUserCredentialsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncClustersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncClustersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClustersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncClustersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        cluster_name: str,
        flavor: cluster_create_params.Flavor,
        high_availability: Optional[cluster_create_params.HighAvailability],
        network: cluster_create_params.Network,
        pg_server_configuration: cluster_create_params.PgServerConfiguration,
        storage: cluster_create_params.Storage,
        databases: Iterable[cluster_create_params.Database] | Omit = omit,
        users: Iterable[cluster_create_params.User] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Create a new PostgreSQL cluster with the specified configuration.

        Args:
          cluster_name: PostgreSQL cluster name

          flavor: Instance RAM and CPU

          high_availability: High Availability settings

          pg_server_configuration: PosgtreSQL cluster configuration

          storage: Cluster's storage configuration

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
            f"/cloud/v1/dbaas/postgres/clusters/{project_id}/{region_id}",
            body=await async_maybe_transform(
                {
                    "cluster_name": cluster_name,
                    "flavor": flavor,
                    "high_availability": high_availability,
                    "network": network,
                    "pg_server_configuration": pg_server_configuration,
                    "storage": storage,
                    "databases": databases,
                    "users": users,
                },
                cluster_create_params.ClusterCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def update(
        self,
        cluster_name: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        databases: Iterable[cluster_update_params.Database] | Omit = omit,
        flavor: Optional[cluster_update_params.Flavor] | Omit = omit,
        high_availability: Optional[cluster_update_params.HighAvailability] | Omit = omit,
        network: Optional[cluster_update_params.Network] | Omit = omit,
        pg_server_configuration: Optional[cluster_update_params.PgServerConfiguration] | Omit = omit,
        storage: Optional[cluster_update_params.Storage] | Omit = omit,
        users: Iterable[cluster_update_params.User] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Update the configuration of an existing PostgreSQL cluster.

        Args:
          flavor: New instance RAM and CPU

          high_availability: New High Availability settings

          pg_server_configuration: New PosgtreSQL cluster configuration

          storage: New storage configuration

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
        return await self._patch(
            f"/cloud/v1/dbaas/postgres/clusters/{project_id}/{region_id}/{cluster_name}",
            body=await async_maybe_transform(
                {
                    "databases": databases,
                    "flavor": flavor,
                    "high_availability": high_availability,
                    "network": network,
                    "pg_server_configuration": pg_server_configuration,
                    "storage": storage,
                    "users": users,
                },
                cluster_update_params.ClusterUpdateParams,
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
        region_id: int | None = None,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PostgresClusterShort, AsyncOffsetPage[PostgresClusterShort]]:
        """List all PostgreSQL clusters in the specified project and region.

        Results can be
        filtered by search query and paginated.

        Args:
          limit: Maximum number of clusters to return

          offset: Number of clusters to skip

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return self._get_api_list(
            f"/cloud/v1/dbaas/postgres/clusters/{project_id}/{region_id}",
            page=AsyncOffsetPage[PostgresClusterShort],
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
                    cluster_list_params.ClusterListParams,
                ),
            ),
            model=PostgresClusterShort,
        )

    async def delete(
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
    ) -> TaskIDList:
        """
        Delete a PostgreSQL cluster and all its associated resources.

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
        return await self._delete(
            f"/cloud/v1/dbaas/postgres/clusters/{project_id}/{region_id}/{cluster_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

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
    ) -> PostgresCluster:
        """
        Get detailed information about a specific PostgreSQL cluster.

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
        return await self._get(
            f"/cloud/v1/dbaas/postgres/clusters/{project_id}/{region_id}/{cluster_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostgresCluster,
        )


class ClustersResourceWithRawResponse:
    def __init__(self, clusters: ClustersResource) -> None:
        self._clusters = clusters

        self.create = to_raw_response_wrapper(
            clusters.create,
        )
        self.update = to_raw_response_wrapper(
            clusters.update,
        )
        self.list = to_raw_response_wrapper(
            clusters.list,
        )
        self.delete = to_raw_response_wrapper(
            clusters.delete,
        )
        self.get = to_raw_response_wrapper(
            clusters.get,
        )

    @cached_property
    def user_credentials(self) -> UserCredentialsResourceWithRawResponse:
        return UserCredentialsResourceWithRawResponse(self._clusters.user_credentials)


class AsyncClustersResourceWithRawResponse:
    def __init__(self, clusters: AsyncClustersResource) -> None:
        self._clusters = clusters

        self.create = async_to_raw_response_wrapper(
            clusters.create,
        )
        self.update = async_to_raw_response_wrapper(
            clusters.update,
        )
        self.list = async_to_raw_response_wrapper(
            clusters.list,
        )
        self.delete = async_to_raw_response_wrapper(
            clusters.delete,
        )
        self.get = async_to_raw_response_wrapper(
            clusters.get,
        )

    @cached_property
    def user_credentials(self) -> AsyncUserCredentialsResourceWithRawResponse:
        return AsyncUserCredentialsResourceWithRawResponse(self._clusters.user_credentials)


class ClustersResourceWithStreamingResponse:
    def __init__(self, clusters: ClustersResource) -> None:
        self._clusters = clusters

        self.create = to_streamed_response_wrapper(
            clusters.create,
        )
        self.update = to_streamed_response_wrapper(
            clusters.update,
        )
        self.list = to_streamed_response_wrapper(
            clusters.list,
        )
        self.delete = to_streamed_response_wrapper(
            clusters.delete,
        )
        self.get = to_streamed_response_wrapper(
            clusters.get,
        )

    @cached_property
    def user_credentials(self) -> UserCredentialsResourceWithStreamingResponse:
        return UserCredentialsResourceWithStreamingResponse(self._clusters.user_credentials)


class AsyncClustersResourceWithStreamingResponse:
    def __init__(self, clusters: AsyncClustersResource) -> None:
        self._clusters = clusters

        self.create = async_to_streamed_response_wrapper(
            clusters.create,
        )
        self.update = async_to_streamed_response_wrapper(
            clusters.update,
        )
        self.list = async_to_streamed_response_wrapper(
            clusters.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            clusters.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            clusters.get,
        )

    @cached_property
    def user_credentials(self) -> AsyncUserCredentialsResourceWithStreamingResponse:
        return AsyncUserCredentialsResourceWithStreamingResponse(self._clusters.user_credentials)
