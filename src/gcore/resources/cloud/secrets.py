# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.cloud import secret_create_params, secret_upload_tls_certificate_params
from ..._base_client import make_request_options
from ...types.cloud.secret import Secret
from ...types.cloud.task_id_list import TaskIDList
from ...types.cloud.secret_list_response import SecretListResponse

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
        region_id: int | None = None,
        name: str,
        payload: str,
        payload_content_encoding: Literal["base64"],
        payload_content_type: str,
        secret_type: Literal["certificate", "opaque", "passphrase", "private", "public", "symmetric"],
        algorithm: Optional[str] | NotGiven = NOT_GIVEN,
        bit_length: Optional[int] | NotGiven = NOT_GIVEN,
        expiration: Optional[str] | NotGiven = NOT_GIVEN,
        mode: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Create secret

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fsecrets%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
              "$.paths['/cloud/v1/secrets/{project_id}/{region_id}'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fsecrets%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
              "$.paths['/cloud/v1/secrets/{project_id}/{region_id}'].post.parameters[1].schema"

          name: '#/components/schemas/CreateSecretSerializer/properties/name'
              "$.components.schemas.CreateSecretSerializer.properties.name"

          payload: '#/components/schemas/CreateSecretSerializer/properties/payload'
              "$.components.schemas.CreateSecretSerializer.properties.payload"

          payload_content_encoding: '#/components/schemas/CreateSecretSerializer/properties/payload_content_encoding'
              "$.components.schemas.CreateSecretSerializer.properties.payload_content_encoding"

          payload_content_type: '#/components/schemas/CreateSecretSerializer/properties/payload_content_type'
              "$.components.schemas.CreateSecretSerializer.properties.payload_content_type"

          secret_type: '#/components/schemas/CreateSecretSerializer/properties/secret_type'
              "$.components.schemas.CreateSecretSerializer.properties.secret_type"

          algorithm: '#/components/schemas/CreateSecretSerializer/properties/algorithm/anyOf/0'
              "$.components.schemas.CreateSecretSerializer.properties.algorithm.anyOf[0]"

          bit_length: '#/components/schemas/CreateSecretSerializer/properties/bit_length/anyOf/0'
              "$.components.schemas.CreateSecretSerializer.properties.bit_length.anyOf[0]"

          expiration: '#/components/schemas/CreateSecretSerializer/properties/expiration/anyOf/0'
              "$.components.schemas.CreateSecretSerializer.properties.expiration.anyOf[0]"

          mode: '#/components/schemas/CreateSecretSerializer/properties/mode/anyOf/0'
              "$.components.schemas.CreateSecretSerializer.properties.mode.anyOf[0]"

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
            f"/cloud/v1/secrets/{project_id}/{region_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "payload": payload,
                    "payload_content_encoding": payload_content_encoding,
                    "payload_content_type": payload_content_type,
                    "secret_type": secret_type,
                    "algorithm": algorithm,
                    "bit_length": bit_length,
                    "expiration": expiration,
                    "mode": mode,
                },
                secret_create_params.SecretCreateParams,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecretListResponse:
        """
        List secrets

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fsecrets%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/secrets/{project_id}/{region_id}'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fsecrets%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v1/secrets/{project_id}/{region_id}'].get.parameters[1].schema"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return self._get(
            f"/cloud/v1/secrets/{project_id}/{region_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecretListResponse,
        )

    def delete(
        self,
        secret_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Delete secret

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fsecrets%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bsecret_id%7D/delete/parameters/0/schema'
              "$.paths['/cloud/v1/secrets/{project_id}/{region_id}/{secret_id}']['delete'].parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fsecrets%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bsecret_id%7D/delete/parameters/1/schema'
              "$.paths['/cloud/v1/secrets/{project_id}/{region_id}/{secret_id}']['delete'].parameters[1].schema"

          secret_id: '#/paths/%2Fcloud%2Fv1%2Fsecrets%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bsecret_id%7D/delete/parameters/2/schema'
              "$.paths['/cloud/v1/secrets/{project_id}/{region_id}/{secret_id}']['delete'].parameters[2].schema"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not secret_id:
            raise ValueError(f"Expected a non-empty value for `secret_id` but received {secret_id!r}")
        return self._delete(
            f"/cloud/v1/secrets/{project_id}/{region_id}/{secret_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def get(
        self,
        secret_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Secret:
        """
        Get secret

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fsecrets%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bsecret_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/secrets/{project_id}/{region_id}/{secret_id}'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fsecrets%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bsecret_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v1/secrets/{project_id}/{region_id}/{secret_id}'].get.parameters[1].schema"

          secret_id: '#/paths/%2Fcloud%2Fv1%2Fsecrets%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bsecret_id%7D/get/parameters/2/schema'
              "$.paths['/cloud/v1/secrets/{project_id}/{region_id}/{secret_id}'].get.parameters[2].schema"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not secret_id:
            raise ValueError(f"Expected a non-empty value for `secret_id` but received {secret_id!r}")
        return self._get(
            f"/cloud/v1/secrets/{project_id}/{region_id}/{secret_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Secret,
        )

    def upload_tls_certificate(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        payload: secret_upload_tls_certificate_params.Payload,
        expiration: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Create secret

        Args:
          project_id: '#/paths/%2Fcloud%2Fv2%2Fsecrets%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
              "$.paths['/cloud/v2/secrets/{project_id}/{region_id}'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv2%2Fsecrets%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
              "$.paths['/cloud/v2/secrets/{project_id}/{region_id}'].post.parameters[1].schema"

          name: '#/components/schemas/CreateSecretSerializerV2/properties/name'
              "$.components.schemas.CreateSecretSerializerV2.properties.name"

          payload: '#/components/schemas/CreateSecretSerializerV2/properties/payload'
              "$.components.schemas.CreateSecretSerializerV2.properties.payload"

          expiration: '#/components/schemas/CreateSecretSerializerV2/properties/expiration/anyOf/0'
              "$.components.schemas.CreateSecretSerializerV2.properties.expiration.anyOf[0]"

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
            f"/cloud/v2/secrets/{project_id}/{region_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "payload": payload,
                    "expiration": expiration,
                },
                secret_upload_tls_certificate_params.SecretUploadTlsCertificateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
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
        region_id: int | None = None,
        name: str,
        payload: str,
        payload_content_encoding: Literal["base64"],
        payload_content_type: str,
        secret_type: Literal["certificate", "opaque", "passphrase", "private", "public", "symmetric"],
        algorithm: Optional[str] | NotGiven = NOT_GIVEN,
        bit_length: Optional[int] | NotGiven = NOT_GIVEN,
        expiration: Optional[str] | NotGiven = NOT_GIVEN,
        mode: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Create secret

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fsecrets%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
              "$.paths['/cloud/v1/secrets/{project_id}/{region_id}'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fsecrets%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
              "$.paths['/cloud/v1/secrets/{project_id}/{region_id}'].post.parameters[1].schema"

          name: '#/components/schemas/CreateSecretSerializer/properties/name'
              "$.components.schemas.CreateSecretSerializer.properties.name"

          payload: '#/components/schemas/CreateSecretSerializer/properties/payload'
              "$.components.schemas.CreateSecretSerializer.properties.payload"

          payload_content_encoding: '#/components/schemas/CreateSecretSerializer/properties/payload_content_encoding'
              "$.components.schemas.CreateSecretSerializer.properties.payload_content_encoding"

          payload_content_type: '#/components/schemas/CreateSecretSerializer/properties/payload_content_type'
              "$.components.schemas.CreateSecretSerializer.properties.payload_content_type"

          secret_type: '#/components/schemas/CreateSecretSerializer/properties/secret_type'
              "$.components.schemas.CreateSecretSerializer.properties.secret_type"

          algorithm: '#/components/schemas/CreateSecretSerializer/properties/algorithm/anyOf/0'
              "$.components.schemas.CreateSecretSerializer.properties.algorithm.anyOf[0]"

          bit_length: '#/components/schemas/CreateSecretSerializer/properties/bit_length/anyOf/0'
              "$.components.schemas.CreateSecretSerializer.properties.bit_length.anyOf[0]"

          expiration: '#/components/schemas/CreateSecretSerializer/properties/expiration/anyOf/0'
              "$.components.schemas.CreateSecretSerializer.properties.expiration.anyOf[0]"

          mode: '#/components/schemas/CreateSecretSerializer/properties/mode/anyOf/0'
              "$.components.schemas.CreateSecretSerializer.properties.mode.anyOf[0]"

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
            f"/cloud/v1/secrets/{project_id}/{region_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "payload": payload,
                    "payload_content_encoding": payload_content_encoding,
                    "payload_content_type": payload_content_type,
                    "secret_type": secret_type,
                    "algorithm": algorithm,
                    "bit_length": bit_length,
                    "expiration": expiration,
                    "mode": mode,
                },
                secret_create_params.SecretCreateParams,
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
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecretListResponse:
        """
        List secrets

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fsecrets%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/secrets/{project_id}/{region_id}'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fsecrets%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v1/secrets/{project_id}/{region_id}'].get.parameters[1].schema"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return await self._get(
            f"/cloud/v1/secrets/{project_id}/{region_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecretListResponse,
        )

    async def delete(
        self,
        secret_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Delete secret

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fsecrets%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bsecret_id%7D/delete/parameters/0/schema'
              "$.paths['/cloud/v1/secrets/{project_id}/{region_id}/{secret_id}']['delete'].parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fsecrets%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bsecret_id%7D/delete/parameters/1/schema'
              "$.paths['/cloud/v1/secrets/{project_id}/{region_id}/{secret_id}']['delete'].parameters[1].schema"

          secret_id: '#/paths/%2Fcloud%2Fv1%2Fsecrets%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bsecret_id%7D/delete/parameters/2/schema'
              "$.paths['/cloud/v1/secrets/{project_id}/{region_id}/{secret_id}']['delete'].parameters[2].schema"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not secret_id:
            raise ValueError(f"Expected a non-empty value for `secret_id` but received {secret_id!r}")
        return await self._delete(
            f"/cloud/v1/secrets/{project_id}/{region_id}/{secret_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def get(
        self,
        secret_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Secret:
        """
        Get secret

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fsecrets%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bsecret_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/secrets/{project_id}/{region_id}/{secret_id}'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fsecrets%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bsecret_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v1/secrets/{project_id}/{region_id}/{secret_id}'].get.parameters[1].schema"

          secret_id: '#/paths/%2Fcloud%2Fv1%2Fsecrets%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bsecret_id%7D/get/parameters/2/schema'
              "$.paths['/cloud/v1/secrets/{project_id}/{region_id}/{secret_id}'].get.parameters[2].schema"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not secret_id:
            raise ValueError(f"Expected a non-empty value for `secret_id` but received {secret_id!r}")
        return await self._get(
            f"/cloud/v1/secrets/{project_id}/{region_id}/{secret_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Secret,
        )

    async def upload_tls_certificate(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        payload: secret_upload_tls_certificate_params.Payload,
        expiration: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Create secret

        Args:
          project_id: '#/paths/%2Fcloud%2Fv2%2Fsecrets%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
              "$.paths['/cloud/v2/secrets/{project_id}/{region_id}'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv2%2Fsecrets%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
              "$.paths['/cloud/v2/secrets/{project_id}/{region_id}'].post.parameters[1].schema"

          name: '#/components/schemas/CreateSecretSerializerV2/properties/name'
              "$.components.schemas.CreateSecretSerializerV2.properties.name"

          payload: '#/components/schemas/CreateSecretSerializerV2/properties/payload'
              "$.components.schemas.CreateSecretSerializerV2.properties.payload"

          expiration: '#/components/schemas/CreateSecretSerializerV2/properties/expiration/anyOf/0'
              "$.components.schemas.CreateSecretSerializerV2.properties.expiration.anyOf[0]"

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
            f"/cloud/v2/secrets/{project_id}/{region_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "payload": payload,
                    "expiration": expiration,
                },
                secret_upload_tls_certificate_params.SecretUploadTlsCertificateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
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
        self.upload_tls_certificate = to_raw_response_wrapper(
            secrets.upload_tls_certificate,
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
        self.upload_tls_certificate = async_to_raw_response_wrapper(
            secrets.upload_tls_certificate,
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
        self.upload_tls_certificate = to_streamed_response_wrapper(
            secrets.upload_tls_certificate,
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
        self.upload_tls_certificate = async_to_streamed_response_wrapper(
            secrets.upload_tls_certificate,
        )
