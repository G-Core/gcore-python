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

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return SecretsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SecretsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
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
          project_id: Project ID

          region_id: Region ID

          name: Secret name

          payload: Secret payload. For HTTPS-terminated load balancing, provide base64 encoded
              conents of a PKCS12 file. The PKCS12 file is the combined TLS certificate, key,
              and intermediate certificate chain obtained from an external certificate
              authority. The file can be created via openssl, e.g.'openssl pkcs12 -export
              -inkey server.key -in server.crt -certfile ca-chain.crt -passout pass: -out
              server.p12'The key and certificate should be PEM-encoded, and the intermediate
              certificate chain should be multiple PEM-encoded certs concatenated together

          payload_content_encoding: The encoding used for the payload to be able to include it in the JSON request.
              Currently only base64 is supported

          payload_content_type: The media type for the content of the payload

          secret_type: Secret type. symmetric - Used for storing byte arrays such as keys suitable for
              symmetric encryption; public - Used for storing the public key of an asymmetric
              keypair; private - Used for storing the private key of an asymmetric keypair;
              passphrase - Used for storing plain text passphrases; certificate - Used for
              storing cryptographic certificates such as X.509 certificates; opaque - Used for
              backwards compatibility with previous versions of the API

          algorithm: Metadata provided by a user or system for informational purposes.

          bit_length: Metadata provided by a user or system for informational purposes. Value must be
              greater than zero.

          expiration: Datetime when the secret will expire.

          mode: Metadata provided by a user or system for informational purposes.

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
          project_id: Project ID

          region_id: Region ID

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
          project_id: Project ID

          region_id: Region ID

          secret_id: Secret ID

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
          project_id: Project ID

          region_id: Region ID

          secret_id: Secret ID

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
          project_id: Project ID

          region_id: Region ID

          name: Secret name

          payload: Secret payload.

          expiration: Datetime when the secret will expire. Defaults to None

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

    def upload_tls_certificate_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        payload: secret_upload_tls_certificate_params.Payload,
        expiration: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        polling_interval_seconds: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Secret:
        response = self.upload_tls_certificate(
            project_id=project_id,
            region_id=region_id,
            name=name,
            payload=payload,
            expiration=expiration,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )
        if not response.tasks or len(response.tasks) != 1:
            raise ValueError(f"Expected exactly one task to be created")
        task = self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
        )
        if not task.created_resources or not task.created_resources.secrets or len(task.created_resources.secrets) != 1:
            raise ValueError(f"Expected exactly one resource to be created in a task")
        return self.get(
            secret_id=task.created_resources.secrets[0],
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
        )


class AsyncSecretsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSecretsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSecretsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSecretsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
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
          project_id: Project ID

          region_id: Region ID

          name: Secret name

          payload: Secret payload. For HTTPS-terminated load balancing, provide base64 encoded
              conents of a PKCS12 file. The PKCS12 file is the combined TLS certificate, key,
              and intermediate certificate chain obtained from an external certificate
              authority. The file can be created via openssl, e.g.'openssl pkcs12 -export
              -inkey server.key -in server.crt -certfile ca-chain.crt -passout pass: -out
              server.p12'The key and certificate should be PEM-encoded, and the intermediate
              certificate chain should be multiple PEM-encoded certs concatenated together

          payload_content_encoding: The encoding used for the payload to be able to include it in the JSON request.
              Currently only base64 is supported

          payload_content_type: The media type for the content of the payload

          secret_type: Secret type. symmetric - Used for storing byte arrays such as keys suitable for
              symmetric encryption; public - Used for storing the public key of an asymmetric
              keypair; private - Used for storing the private key of an asymmetric keypair;
              passphrase - Used for storing plain text passphrases; certificate - Used for
              storing cryptographic certificates such as X.509 certificates; opaque - Used for
              backwards compatibility with previous versions of the API

          algorithm: Metadata provided by a user or system for informational purposes.

          bit_length: Metadata provided by a user or system for informational purposes. Value must be
              greater than zero.

          expiration: Datetime when the secret will expire.

          mode: Metadata provided by a user or system for informational purposes.

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
          project_id: Project ID

          region_id: Region ID

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
          project_id: Project ID

          region_id: Region ID

          secret_id: Secret ID

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
          project_id: Project ID

          region_id: Region ID

          secret_id: Secret ID

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
          project_id: Project ID

          region_id: Region ID

          name: Secret name

          payload: Secret payload.

          expiration: Datetime when the secret will expire. Defaults to None

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

    async def upload_tls_certificate_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        payload: secret_upload_tls_certificate_params.Payload,
        expiration: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        polling_interval_seconds: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Secret:
        response = await self.upload_tls_certificate(
            project_id=project_id,
            region_id=region_id,
            name=name,
            payload=payload,
            expiration=expiration,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )
        if not response.tasks or len(response.tasks) != 1:
            raise ValueError(f"Expected exactly one task to be created")
        task = await self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
        )
        if not task.created_resources or not task.created_resources.secrets or len(task.created_resources.secrets) != 1:
            raise ValueError(f"Expected exactly one resource to be created in a task")
        return await self.get(
            secret_id=task.created_resources.secrets[0],
            project_id=project_id,
            region_id=region_id,
            extra_headers=extra_headers,
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
