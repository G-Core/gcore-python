# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ......_types import Body, Query, Headers, NotGiven, not_given
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_base_client import make_request_options
from ......types.cloud.databases.postgres.clusters.postgres_user_credentials import PostgresUserCredentials

__all__ = ["UserCredentialsResource", "AsyncUserCredentialsResource"]


class UserCredentialsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UserCredentialsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return UserCredentialsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UserCredentialsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return UserCredentialsResourceWithStreamingResponse(self)

    def get(
        self,
        username: str,
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
    ) -> PostgresUserCredentials:
        """Get the credentials for a specific user in a PostgreSQL cluster.

        This endpoint
        can only be used once per user.

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
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return self._get(
            f"/cloud/v1/dbaas/postgres/clusters/{project_id}/{region_id}/{cluster_name}/users/{username}/credentials",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostgresUserCredentials,
        )

    def regenerate(
        self,
        username: str,
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
    ) -> PostgresUserCredentials:
        """
        Generate new credentials for a specific user in a PostgreSQL cluster.

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
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return self._post(
            f"/cloud/v1/dbaas/postgres/clusters/{project_id}/{region_id}/{cluster_name}/users/{username}/credentials",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostgresUserCredentials,
        )


class AsyncUserCredentialsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUserCredentialsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUserCredentialsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUserCredentialsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncUserCredentialsResourceWithStreamingResponse(self)

    async def get(
        self,
        username: str,
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
    ) -> PostgresUserCredentials:
        """Get the credentials for a specific user in a PostgreSQL cluster.

        This endpoint
        can only be used once per user.

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
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return await self._get(
            f"/cloud/v1/dbaas/postgres/clusters/{project_id}/{region_id}/{cluster_name}/users/{username}/credentials",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostgresUserCredentials,
        )

    async def regenerate(
        self,
        username: str,
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
    ) -> PostgresUserCredentials:
        """
        Generate new credentials for a specific user in a PostgreSQL cluster.

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
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return await self._post(
            f"/cloud/v1/dbaas/postgres/clusters/{project_id}/{region_id}/{cluster_name}/users/{username}/credentials",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostgresUserCredentials,
        )


class UserCredentialsResourceWithRawResponse:
    def __init__(self, user_credentials: UserCredentialsResource) -> None:
        self._user_credentials = user_credentials

        self.get = to_raw_response_wrapper(
            user_credentials.get,
        )
        self.regenerate = to_raw_response_wrapper(
            user_credentials.regenerate,
        )


class AsyncUserCredentialsResourceWithRawResponse:
    def __init__(self, user_credentials: AsyncUserCredentialsResource) -> None:
        self._user_credentials = user_credentials

        self.get = async_to_raw_response_wrapper(
            user_credentials.get,
        )
        self.regenerate = async_to_raw_response_wrapper(
            user_credentials.regenerate,
        )


class UserCredentialsResourceWithStreamingResponse:
    def __init__(self, user_credentials: UserCredentialsResource) -> None:
        self._user_credentials = user_credentials

        self.get = to_streamed_response_wrapper(
            user_credentials.get,
        )
        self.regenerate = to_streamed_response_wrapper(
            user_credentials.regenerate,
        )


class AsyncUserCredentialsResourceWithStreamingResponse:
    def __init__(self, user_credentials: AsyncUserCredentialsResource) -> None:
        self._user_credentials = user_credentials

        self.get = async_to_streamed_response_wrapper(
            user_credentials.get,
        )
        self.regenerate = async_to_streamed_response_wrapper(
            user_credentials.regenerate,
        )
