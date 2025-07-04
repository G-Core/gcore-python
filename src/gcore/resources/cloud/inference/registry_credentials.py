# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncOffsetPage, AsyncOffsetPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.cloud.inference import (
    registry_credential_list_params,
    registry_credential_create_params,
    registry_credential_replace_params,
)
from ....types.cloud.inference.inference_registry_credentials import InferenceRegistryCredentials
from ....types.cloud.inference.inference_registry_credentials_create import InferenceRegistryCredentialsCreate

__all__ = ["RegistryCredentialsResource", "AsyncRegistryCredentialsResource"]


class RegistryCredentialsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RegistryCredentialsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return RegistryCredentialsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RegistryCredentialsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return RegistryCredentialsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        project_id: int | None = None,
        name: str,
        password: str,
        registry_url: str,
        username: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InferenceRegistryCredentialsCreate:
        """
        Create inference registry credential

        Args:
          project_id: Project ID

          name: Registry credential name.

          password: Registry password.

          registry_url: Registry URL.

          username: Registry username.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        return self._post(
            f"/cloud/v3/inference/{project_id}/registry_credentials",
            body=maybe_transform(
                {
                    "name": name,
                    "password": password,
                    "registry_url": registry_url,
                    "username": username,
                },
                registry_credential_create_params.RegistryCredentialCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InferenceRegistryCredentialsCreate,
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
    ) -> SyncOffsetPage[InferenceRegistryCredentials]:
        """
        List inference registry credentials

        Args:
          project_id: Project ID

          limit: Optional. Limit the number of returned items

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
            f"/cloud/v3/inference/{project_id}/registry_credentials",
            page=SyncOffsetPage[InferenceRegistryCredentials],
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
                    registry_credential_list_params.RegistryCredentialListParams,
                ),
            ),
            model=InferenceRegistryCredentials,
        )

    def delete(
        self,
        credential_name: str,
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
        Delete inference registry credential

        Args:
          project_id: Project ID

          credential_name: Registry credential name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not credential_name:
            raise ValueError(f"Expected a non-empty value for `credential_name` but received {credential_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/cloud/v3/inference/{project_id}/registry_credentials/{credential_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        credential_name: str,
        *,
        project_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InferenceRegistryCredentials:
        """
        Get inference registry credential

        Args:
          project_id: Project ID

          credential_name: Registry credential name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not credential_name:
            raise ValueError(f"Expected a non-empty value for `credential_name` but received {credential_name!r}")
        return self._get(
            f"/cloud/v3/inference/{project_id}/registry_credentials/{credential_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InferenceRegistryCredentials,
        )

    def replace(
        self,
        credential_name: str,
        *,
        project_id: int | None = None,
        password: str,
        registry_url: str,
        username: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Replace inference registry credential

        Args:
          project_id: Project ID

          credential_name: Registry credential name.

          password: Registry password.

          registry_url: Registry URL.

          username: Registry username.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not credential_name:
            raise ValueError(f"Expected a non-empty value for `credential_name` but received {credential_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/cloud/v3/inference/{project_id}/registry_credentials/{credential_name}",
            body=maybe_transform(
                {
                    "password": password,
                    "registry_url": registry_url,
                    "username": username,
                },
                registry_credential_replace_params.RegistryCredentialReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncRegistryCredentialsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRegistryCredentialsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRegistryCredentialsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRegistryCredentialsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncRegistryCredentialsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        project_id: int | None = None,
        name: str,
        password: str,
        registry_url: str,
        username: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InferenceRegistryCredentialsCreate:
        """
        Create inference registry credential

        Args:
          project_id: Project ID

          name: Registry credential name.

          password: Registry password.

          registry_url: Registry URL.

          username: Registry username.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        return await self._post(
            f"/cloud/v3/inference/{project_id}/registry_credentials",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "password": password,
                    "registry_url": registry_url,
                    "username": username,
                },
                registry_credential_create_params.RegistryCredentialCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InferenceRegistryCredentialsCreate,
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
    ) -> AsyncPaginator[InferenceRegistryCredentials, AsyncOffsetPage[InferenceRegistryCredentials]]:
        """
        List inference registry credentials

        Args:
          project_id: Project ID

          limit: Optional. Limit the number of returned items

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
            f"/cloud/v3/inference/{project_id}/registry_credentials",
            page=AsyncOffsetPage[InferenceRegistryCredentials],
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
                    registry_credential_list_params.RegistryCredentialListParams,
                ),
            ),
            model=InferenceRegistryCredentials,
        )

    async def delete(
        self,
        credential_name: str,
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
        Delete inference registry credential

        Args:
          project_id: Project ID

          credential_name: Registry credential name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not credential_name:
            raise ValueError(f"Expected a non-empty value for `credential_name` but received {credential_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/cloud/v3/inference/{project_id}/registry_credentials/{credential_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        credential_name: str,
        *,
        project_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InferenceRegistryCredentials:
        """
        Get inference registry credential

        Args:
          project_id: Project ID

          credential_name: Registry credential name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not credential_name:
            raise ValueError(f"Expected a non-empty value for `credential_name` but received {credential_name!r}")
        return await self._get(
            f"/cloud/v3/inference/{project_id}/registry_credentials/{credential_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InferenceRegistryCredentials,
        )

    async def replace(
        self,
        credential_name: str,
        *,
        project_id: int | None = None,
        password: str,
        registry_url: str,
        username: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Replace inference registry credential

        Args:
          project_id: Project ID

          credential_name: Registry credential name.

          password: Registry password.

          registry_url: Registry URL.

          username: Registry username.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not credential_name:
            raise ValueError(f"Expected a non-empty value for `credential_name` but received {credential_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/cloud/v3/inference/{project_id}/registry_credentials/{credential_name}",
            body=await async_maybe_transform(
                {
                    "password": password,
                    "registry_url": registry_url,
                    "username": username,
                },
                registry_credential_replace_params.RegistryCredentialReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class RegistryCredentialsResourceWithRawResponse:
    def __init__(self, registry_credentials: RegistryCredentialsResource) -> None:
        self._registry_credentials = registry_credentials

        self.create = to_raw_response_wrapper(
            registry_credentials.create,
        )
        self.list = to_raw_response_wrapper(
            registry_credentials.list,
        )
        self.delete = to_raw_response_wrapper(
            registry_credentials.delete,
        )
        self.get = to_raw_response_wrapper(
            registry_credentials.get,
        )
        self.replace = to_raw_response_wrapper(
            registry_credentials.replace,
        )


class AsyncRegistryCredentialsResourceWithRawResponse:
    def __init__(self, registry_credentials: AsyncRegistryCredentialsResource) -> None:
        self._registry_credentials = registry_credentials

        self.create = async_to_raw_response_wrapper(
            registry_credentials.create,
        )
        self.list = async_to_raw_response_wrapper(
            registry_credentials.list,
        )
        self.delete = async_to_raw_response_wrapper(
            registry_credentials.delete,
        )
        self.get = async_to_raw_response_wrapper(
            registry_credentials.get,
        )
        self.replace = async_to_raw_response_wrapper(
            registry_credentials.replace,
        )


class RegistryCredentialsResourceWithStreamingResponse:
    def __init__(self, registry_credentials: RegistryCredentialsResource) -> None:
        self._registry_credentials = registry_credentials

        self.create = to_streamed_response_wrapper(
            registry_credentials.create,
        )
        self.list = to_streamed_response_wrapper(
            registry_credentials.list,
        )
        self.delete = to_streamed_response_wrapper(
            registry_credentials.delete,
        )
        self.get = to_streamed_response_wrapper(
            registry_credentials.get,
        )
        self.replace = to_streamed_response_wrapper(
            registry_credentials.replace,
        )


class AsyncRegistryCredentialsResourceWithStreamingResponse:
    def __init__(self, registry_credentials: AsyncRegistryCredentialsResource) -> None:
        self._registry_credentials = registry_credentials

        self.create = async_to_streamed_response_wrapper(
            registry_credentials.create,
        )
        self.list = async_to_streamed_response_wrapper(
            registry_credentials.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            registry_credentials.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            registry_credentials.get,
        )
        self.replace = async_to_streamed_response_wrapper(
            registry_credentials.replace,
        )
