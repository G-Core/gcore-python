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
from ....types.cloud.inference import secret_list_params, secret_create_params, secret_replace_params
from ....types.cloud.aws_iam_data_param import AwsIamDataParam
from ....types.cloud.inference.inference_secret import InferenceSecret

__all__ = ["SecretsResource", "AsyncSecretsResource"]


class SecretsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SecretsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return SecretsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SecretsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
        """
        return SecretsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        project_id: int | None = None,
        data: AwsIamDataParam,
        name: str,
        type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InferenceSecret:
        """
        Create Inference Secret

        Args:
          project_id: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fsecrets/post/parameters/0/schema'
              "$.paths['/cloud/v3/inference/{project_id}/secrets'].post.parameters[0].schema"

          data: '#/components/schemas/InferenceBoxSecretsInSerializer/properties/data'
              "$.components.schemas.InferenceBoxSecretsInSerializer.properties.data"

          name: '#/components/schemas/InferenceBoxSecretsInSerializer/properties/name'
              "$.components.schemas.InferenceBoxSecretsInSerializer.properties.name"

          type: '#/components/schemas/InferenceBoxSecretsInSerializer/properties/type'
              "$.components.schemas.InferenceBoxSecretsInSerializer.properties.type"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        return self._post(
            f"/cloud/v3/inference/{project_id}/secrets",
            body=maybe_transform(
                {
                    "data": data,
                    "name": name,
                    "type": type,
                },
                secret_create_params.SecretCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InferenceSecret,
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
    ) -> SyncOffsetPage[InferenceSecret]:
        """
        List Secrets for Inference

        Args:
          project_id: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fsecrets/get/parameters/0/schema'
              "$.paths['/cloud/v3/inference/{project_id}/secrets'].get.parameters[0].schema"

          limit: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fsecrets/get/parameters/1'
              "$.paths['/cloud/v3/inference/{project_id}/secrets'].get.parameters[1]"

          offset: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fsecrets/get/parameters/2'
              "$.paths['/cloud/v3/inference/{project_id}/secrets'].get.parameters[2]"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        return self._get_api_list(
            f"/cloud/v3/inference/{project_id}/secrets",
            page=SyncOffsetPage[InferenceSecret],
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
                    secret_list_params.SecretListParams,
                ),
            ),
            model=InferenceSecret,
        )

    def delete(
        self,
        secret_name: str,
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
        Delete Inference Secret

        Args:
          project_id: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fsecrets%2F%7Bsecret_name%7D/delete/parameters/0/schema'
              "$.paths['/cloud/v3/inference/{project_id}/secrets/{secret_name}']['delete'].parameters[0].schema"

          secret_name: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fsecrets%2F%7Bsecret_name%7D/delete/parameters/1/schema'
              "$.paths['/cloud/v3/inference/{project_id}/secrets/{secret_name}']['delete'].parameters[1].schema"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not secret_name:
            raise ValueError(f"Expected a non-empty value for `secret_name` but received {secret_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/cloud/v3/inference/{project_id}/secrets/{secret_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        secret_name: str,
        *,
        project_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InferenceSecret:
        """
        Get Inference Secret

        Args:
          project_id: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fsecrets%2F%7Bsecret_name%7D/get/parameters/0/schema'
              "$.paths['/cloud/v3/inference/{project_id}/secrets/{secret_name}'].get.parameters[0].schema"

          secret_name: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fsecrets%2F%7Bsecret_name%7D/get/parameters/1/schema'
              "$.paths['/cloud/v3/inference/{project_id}/secrets/{secret_name}'].get.parameters[1].schema"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not secret_name:
            raise ValueError(f"Expected a non-empty value for `secret_name` but received {secret_name!r}")
        return self._get(
            f"/cloud/v3/inference/{project_id}/secrets/{secret_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InferenceSecret,
        )

    def replace(
        self,
        secret_name: str,
        *,
        project_id: int | None = None,
        data: AwsIamDataParam,
        type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InferenceSecret:
        """
        Update Inference Secret

        Args:
          project_id: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fsecrets%2F%7Bsecret_name%7D/put/parameters/0/schema'
              "$.paths['/cloud/v3/inference/{project_id}/secrets/{secret_name}'].put.parameters[0].schema"

          secret_name: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fsecrets%2F%7Bsecret_name%7D/put/parameters/1/schema'
              "$.paths['/cloud/v3/inference/{project_id}/secrets/{secret_name}'].put.parameters[1].schema"

          data: '#/components/schemas/InferenceSecretInUpdateSerializer/properties/data'
              "$.components.schemas.InferenceSecretInUpdateSerializer.properties.data"

          type: '#/components/schemas/InferenceSecretInUpdateSerializer/properties/type'
              "$.components.schemas.InferenceSecretInUpdateSerializer.properties.type"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not secret_name:
            raise ValueError(f"Expected a non-empty value for `secret_name` but received {secret_name!r}")
        return self._put(
            f"/cloud/v3/inference/{project_id}/secrets/{secret_name}",
            body=maybe_transform(
                {
                    "data": data,
                    "type": type,
                },
                secret_replace_params.SecretReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InferenceSecret,
        )


class AsyncSecretsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSecretsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSecretsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSecretsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
        """
        return AsyncSecretsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        project_id: int | None = None,
        data: AwsIamDataParam,
        name: str,
        type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InferenceSecret:
        """
        Create Inference Secret

        Args:
          project_id: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fsecrets/post/parameters/0/schema'
              "$.paths['/cloud/v3/inference/{project_id}/secrets'].post.parameters[0].schema"

          data: '#/components/schemas/InferenceBoxSecretsInSerializer/properties/data'
              "$.components.schemas.InferenceBoxSecretsInSerializer.properties.data"

          name: '#/components/schemas/InferenceBoxSecretsInSerializer/properties/name'
              "$.components.schemas.InferenceBoxSecretsInSerializer.properties.name"

          type: '#/components/schemas/InferenceBoxSecretsInSerializer/properties/type'
              "$.components.schemas.InferenceBoxSecretsInSerializer.properties.type"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        return await self._post(
            f"/cloud/v3/inference/{project_id}/secrets",
            body=await async_maybe_transform(
                {
                    "data": data,
                    "name": name,
                    "type": type,
                },
                secret_create_params.SecretCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InferenceSecret,
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
    ) -> AsyncPaginator[InferenceSecret, AsyncOffsetPage[InferenceSecret]]:
        """
        List Secrets for Inference

        Args:
          project_id: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fsecrets/get/parameters/0/schema'
              "$.paths['/cloud/v3/inference/{project_id}/secrets'].get.parameters[0].schema"

          limit: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fsecrets/get/parameters/1'
              "$.paths['/cloud/v3/inference/{project_id}/secrets'].get.parameters[1]"

          offset: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fsecrets/get/parameters/2'
              "$.paths['/cloud/v3/inference/{project_id}/secrets'].get.parameters[2]"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        return self._get_api_list(
            f"/cloud/v3/inference/{project_id}/secrets",
            page=AsyncOffsetPage[InferenceSecret],
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
                    secret_list_params.SecretListParams,
                ),
            ),
            model=InferenceSecret,
        )

    async def delete(
        self,
        secret_name: str,
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
        Delete Inference Secret

        Args:
          project_id: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fsecrets%2F%7Bsecret_name%7D/delete/parameters/0/schema'
              "$.paths['/cloud/v3/inference/{project_id}/secrets/{secret_name}']['delete'].parameters[0].schema"

          secret_name: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fsecrets%2F%7Bsecret_name%7D/delete/parameters/1/schema'
              "$.paths['/cloud/v3/inference/{project_id}/secrets/{secret_name}']['delete'].parameters[1].schema"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not secret_name:
            raise ValueError(f"Expected a non-empty value for `secret_name` but received {secret_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/cloud/v3/inference/{project_id}/secrets/{secret_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        secret_name: str,
        *,
        project_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InferenceSecret:
        """
        Get Inference Secret

        Args:
          project_id: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fsecrets%2F%7Bsecret_name%7D/get/parameters/0/schema'
              "$.paths['/cloud/v3/inference/{project_id}/secrets/{secret_name}'].get.parameters[0].schema"

          secret_name: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fsecrets%2F%7Bsecret_name%7D/get/parameters/1/schema'
              "$.paths['/cloud/v3/inference/{project_id}/secrets/{secret_name}'].get.parameters[1].schema"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not secret_name:
            raise ValueError(f"Expected a non-empty value for `secret_name` but received {secret_name!r}")
        return await self._get(
            f"/cloud/v3/inference/{project_id}/secrets/{secret_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InferenceSecret,
        )

    async def replace(
        self,
        secret_name: str,
        *,
        project_id: int | None = None,
        data: AwsIamDataParam,
        type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InferenceSecret:
        """
        Update Inference Secret

        Args:
          project_id: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fsecrets%2F%7Bsecret_name%7D/put/parameters/0/schema'
              "$.paths['/cloud/v3/inference/{project_id}/secrets/{secret_name}'].put.parameters[0].schema"

          secret_name: '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fsecrets%2F%7Bsecret_name%7D/put/parameters/1/schema'
              "$.paths['/cloud/v3/inference/{project_id}/secrets/{secret_name}'].put.parameters[1].schema"

          data: '#/components/schemas/InferenceSecretInUpdateSerializer/properties/data'
              "$.components.schemas.InferenceSecretInUpdateSerializer.properties.data"

          type: '#/components/schemas/InferenceSecretInUpdateSerializer/properties/type'
              "$.components.schemas.InferenceSecretInUpdateSerializer.properties.type"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if not secret_name:
            raise ValueError(f"Expected a non-empty value for `secret_name` but received {secret_name!r}")
        return await self._put(
            f"/cloud/v3/inference/{project_id}/secrets/{secret_name}",
            body=await async_maybe_transform(
                {
                    "data": data,
                    "type": type,
                },
                secret_replace_params.SecretReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InferenceSecret,
        )


class SecretsResourceWithRawResponse:
    def __init__(self, secrets: SecretsResource) -> None:
        self._secrets = secrets

        self.create = to_raw_response_wrapper(
            secrets.create,
        )
        self.list = to_raw_response_wrapper(
            secrets.list,
        )
        self.delete = to_raw_response_wrapper(
            secrets.delete,
        )
        self.get = to_raw_response_wrapper(
            secrets.get,
        )
        self.replace = to_raw_response_wrapper(
            secrets.replace,
        )


class AsyncSecretsResourceWithRawResponse:
    def __init__(self, secrets: AsyncSecretsResource) -> None:
        self._secrets = secrets

        self.create = async_to_raw_response_wrapper(
            secrets.create,
        )
        self.list = async_to_raw_response_wrapper(
            secrets.list,
        )
        self.delete = async_to_raw_response_wrapper(
            secrets.delete,
        )
        self.get = async_to_raw_response_wrapper(
            secrets.get,
        )
        self.replace = async_to_raw_response_wrapper(
            secrets.replace,
        )


class SecretsResourceWithStreamingResponse:
    def __init__(self, secrets: SecretsResource) -> None:
        self._secrets = secrets

        self.create = to_streamed_response_wrapper(
            secrets.create,
        )
        self.list = to_streamed_response_wrapper(
            secrets.list,
        )
        self.delete = to_streamed_response_wrapper(
            secrets.delete,
        )
        self.get = to_streamed_response_wrapper(
            secrets.get,
        )
        self.replace = to_streamed_response_wrapper(
            secrets.replace,
        )


class AsyncSecretsResourceWithStreamingResponse:
    def __init__(self, secrets: AsyncSecretsResource) -> None:
        self._secrets = secrets

        self.create = async_to_streamed_response_wrapper(
            secrets.create,
        )
        self.list = async_to_streamed_response_wrapper(
            secrets.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            secrets.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            secrets.get,
        )
        self.replace = async_to_streamed_response_wrapper(
            secrets.replace,
        )
