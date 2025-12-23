# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library, maybe_coerce_integer
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import GcoreError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.cdn import cdn
from .resources.dns import dns
from .resources.iam import iam
from .resources.waap import waap
from .resources.cloud import cloud
from .resources.storage import storage
from .resources.fastedge import fastedge
from .resources.security import security
from .resources.streaming import streaming

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Gcore", "AsyncGcore", "Client", "AsyncClient"]


class Gcore(SyncAPIClient):
    cloud: cloud.CloudResource
    waap: waap.WaapResource
    iam: iam.IamResource
    fastedge: fastedge.FastedgeResource
    streaming: streaming.StreamingResource
    security: security.SecurityResource
    dns: dns.DNSResource
    storage: storage.StorageResource
    cdn: cdn.CdnResource
    with_raw_response: GcoreWithRawResponse
    with_streaming_response: GcoreWithStreamedResponse

    # client options
    api_key: str
    cloud_project_id: int | None
    cloud_region_id: int | None
    cloud_polling_interval_seconds: int | None
    cloud_polling_timeout_seconds: int | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        cloud_project_id: int | None = None,
        cloud_region_id: int | None = None,
        cloud_polling_interval_seconds: int | None = 3,
        cloud_polling_timeout_seconds: int | None = 7200,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Gcore client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `GCORE_API_KEY`
        - `cloud_project_id` from `GCORE_CLOUD_PROJECT_ID`
        - `cloud_region_id` from `GCORE_CLOUD_REGION_ID`
        """
        if api_key is None:
            api_key = os.environ.get("GCORE_API_KEY")
        if api_key is None:
            raise GcoreError(
                "The api_key client option must be set either by passing api_key to the client or by setting the GCORE_API_KEY environment variable"
            )
        self.api_key = api_key

        if cloud_project_id is None:
            cloud_project_id = maybe_coerce_integer(os.environ.get("GCORE_CLOUD_PROJECT_ID"))
        self.cloud_project_id = cloud_project_id

        if cloud_region_id is None:
            cloud_region_id = maybe_coerce_integer(os.environ.get("GCORE_CLOUD_REGION_ID"))
        self.cloud_region_id = cloud_region_id

        if cloud_polling_interval_seconds is None:
            cloud_polling_interval_seconds = 3
        self.cloud_polling_interval_seconds = cloud_polling_interval_seconds

        if cloud_polling_timeout_seconds is None:
            cloud_polling_timeout_seconds = 7200
        self.cloud_polling_timeout_seconds = cloud_polling_timeout_seconds

        if base_url is None:
            base_url = os.environ.get("GCORE_BASE_URL")
        if base_url is None:
            base_url = f"https://api.gcore.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.cloud = cloud.CloudResource(self)
        self.waap = waap.WaapResource(self)
        self.iam = iam.IamResource(self)
        self.fastedge = fastedge.FastedgeResource(self)
        self.streaming = streaming.StreamingResource(self)
        self.security = security.SecurityResource(self)
        self.dns = dns.DNSResource(self)
        self.storage = storage.StorageResource(self)
        self.cdn = cdn.CdnResource(self)
        self.with_raw_response = GcoreWithRawResponse(self)
        self.with_streaming_response = GcoreWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(nested_format="dots", array_format="repeat")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"APIKey {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        cloud_project_id: int | None = None,
        cloud_region_id: int | None = None,
        cloud_polling_interval_seconds: int | None = None,
        cloud_polling_timeout_seconds: int | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            cloud_project_id=cloud_project_id or self.cloud_project_id,
            cloud_region_id=cloud_region_id or self.cloud_region_id,
            cloud_polling_interval_seconds=cloud_polling_interval_seconds or self.cloud_polling_interval_seconds,
            cloud_polling_timeout_seconds=cloud_polling_timeout_seconds or self.cloud_polling_timeout_seconds,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    def _get_cloud_project_id_path_param(self) -> int:
        from_client = self.cloud_project_id
        if from_client is not None:
            return from_client

        raise ValueError(
            "Missing cloud_project_id argument; Please provide it at the client level, e.g. Gcore(cloud_project_id='abcd') or per method."
        )

    def _get_cloud_region_id_path_param(self) -> int:
        from_client = self.cloud_region_id
        if from_client is not None:
            return from_client

        raise ValueError(
            "Missing cloud_region_id argument; Please provide it at the client level, e.g. Gcore(cloud_region_id='abcd') or per method."
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncGcore(AsyncAPIClient):
    cloud: cloud.AsyncCloudResource
    waap: waap.AsyncWaapResource
    iam: iam.AsyncIamResource
    fastedge: fastedge.AsyncFastedgeResource
    streaming: streaming.AsyncStreamingResource
    security: security.AsyncSecurityResource
    dns: dns.AsyncDNSResource
    storage: storage.AsyncStorageResource
    cdn: cdn.AsyncCdnResource
    with_raw_response: AsyncGcoreWithRawResponse
    with_streaming_response: AsyncGcoreWithStreamedResponse

    # client options
    api_key: str
    cloud_project_id: int | None
    cloud_region_id: int | None
    cloud_polling_interval_seconds: int | None
    cloud_polling_timeout_seconds: int | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        cloud_project_id: int | None = None,
        cloud_region_id: int | None = None,
        cloud_polling_interval_seconds: int | None = 3,
        cloud_polling_timeout_seconds: int | None = 7200,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncGcore client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `GCORE_API_KEY`
        - `cloud_project_id` from `GCORE_CLOUD_PROJECT_ID`
        - `cloud_region_id` from `GCORE_CLOUD_REGION_ID`
        """
        if api_key is None:
            api_key = os.environ.get("GCORE_API_KEY")
        if api_key is None:
            raise GcoreError(
                "The api_key client option must be set either by passing api_key to the client or by setting the GCORE_API_KEY environment variable"
            )
        self.api_key = api_key

        if cloud_project_id is None:
            cloud_project_id = maybe_coerce_integer(os.environ.get("GCORE_CLOUD_PROJECT_ID"))
        self.cloud_project_id = cloud_project_id

        if cloud_region_id is None:
            cloud_region_id = maybe_coerce_integer(os.environ.get("GCORE_CLOUD_REGION_ID"))
        self.cloud_region_id = cloud_region_id

        if cloud_polling_interval_seconds is None:
            cloud_polling_interval_seconds = 3
        self.cloud_polling_interval_seconds = cloud_polling_interval_seconds

        if cloud_polling_timeout_seconds is None:
            cloud_polling_timeout_seconds = 7200
        self.cloud_polling_timeout_seconds = cloud_polling_timeout_seconds

        if base_url is None:
            base_url = os.environ.get("GCORE_BASE_URL")
        if base_url is None:
            base_url = f"https://api.gcore.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.cloud = cloud.AsyncCloudResource(self)
        self.waap = waap.AsyncWaapResource(self)
        self.iam = iam.AsyncIamResource(self)
        self.fastedge = fastedge.AsyncFastedgeResource(self)
        self.streaming = streaming.AsyncStreamingResource(self)
        self.security = security.AsyncSecurityResource(self)
        self.dns = dns.AsyncDNSResource(self)
        self.storage = storage.AsyncStorageResource(self)
        self.cdn = cdn.AsyncCdnResource(self)
        self.with_raw_response = AsyncGcoreWithRawResponse(self)
        self.with_streaming_response = AsyncGcoreWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(nested_format="dots", array_format="repeat")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"APIKey {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        cloud_project_id: int | None = None,
        cloud_region_id: int | None = None,
        cloud_polling_interval_seconds: int | None = None,
        cloud_polling_timeout_seconds: int | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            cloud_project_id=cloud_project_id or self.cloud_project_id,
            cloud_region_id=cloud_region_id or self.cloud_region_id,
            cloud_polling_interval_seconds=cloud_polling_interval_seconds or self.cloud_polling_interval_seconds,
            cloud_polling_timeout_seconds=cloud_polling_timeout_seconds or self.cloud_polling_timeout_seconds,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    def _get_cloud_project_id_path_param(self) -> int:
        from_client = self.cloud_project_id
        if from_client is not None:
            return from_client

        raise ValueError(
            "Missing cloud_project_id argument; Please provide it at the client level, e.g. AsyncGcore(cloud_project_id='abcd') or per method."
        )

    def _get_cloud_region_id_path_param(self) -> int:
        from_client = self.cloud_region_id
        if from_client is not None:
            return from_client

        raise ValueError(
            "Missing cloud_region_id argument; Please provide it at the client level, e.g. AsyncGcore(cloud_region_id='abcd') or per method."
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class GcoreWithRawResponse:
    def __init__(self, client: Gcore) -> None:
        self.cloud = cloud.CloudResourceWithRawResponse(client.cloud)
        self.waap = waap.WaapResourceWithRawResponse(client.waap)
        self.iam = iam.IamResourceWithRawResponse(client.iam)
        self.fastedge = fastedge.FastedgeResourceWithRawResponse(client.fastedge)
        self.streaming = streaming.StreamingResourceWithRawResponse(client.streaming)
        self.security = security.SecurityResourceWithRawResponse(client.security)
        self.dns = dns.DNSResourceWithRawResponse(client.dns)
        self.storage = storage.StorageResourceWithRawResponse(client.storage)
        self.cdn = cdn.CdnResourceWithRawResponse(client.cdn)


class AsyncGcoreWithRawResponse:
    def __init__(self, client: AsyncGcore) -> None:
        self.cloud = cloud.AsyncCloudResourceWithRawResponse(client.cloud)
        self.waap = waap.AsyncWaapResourceWithRawResponse(client.waap)
        self.iam = iam.AsyncIamResourceWithRawResponse(client.iam)
        self.fastedge = fastedge.AsyncFastedgeResourceWithRawResponse(client.fastedge)
        self.streaming = streaming.AsyncStreamingResourceWithRawResponse(client.streaming)
        self.security = security.AsyncSecurityResourceWithRawResponse(client.security)
        self.dns = dns.AsyncDNSResourceWithRawResponse(client.dns)
        self.storage = storage.AsyncStorageResourceWithRawResponse(client.storage)
        self.cdn = cdn.AsyncCdnResourceWithRawResponse(client.cdn)


class GcoreWithStreamedResponse:
    def __init__(self, client: Gcore) -> None:
        self.cloud = cloud.CloudResourceWithStreamingResponse(client.cloud)
        self.waap = waap.WaapResourceWithStreamingResponse(client.waap)
        self.iam = iam.IamResourceWithStreamingResponse(client.iam)
        self.fastedge = fastedge.FastedgeResourceWithStreamingResponse(client.fastedge)
        self.streaming = streaming.StreamingResourceWithStreamingResponse(client.streaming)
        self.security = security.SecurityResourceWithStreamingResponse(client.security)
        self.dns = dns.DNSResourceWithStreamingResponse(client.dns)
        self.storage = storage.StorageResourceWithStreamingResponse(client.storage)
        self.cdn = cdn.CdnResourceWithStreamingResponse(client.cdn)


class AsyncGcoreWithStreamedResponse:
    def __init__(self, client: AsyncGcore) -> None:
        self.cloud = cloud.AsyncCloudResourceWithStreamingResponse(client.cloud)
        self.waap = waap.AsyncWaapResourceWithStreamingResponse(client.waap)
        self.iam = iam.AsyncIamResourceWithStreamingResponse(client.iam)
        self.fastedge = fastedge.AsyncFastedgeResourceWithStreamingResponse(client.fastedge)
        self.streaming = streaming.AsyncStreamingResourceWithStreamingResponse(client.streaming)
        self.security = security.AsyncSecurityResourceWithStreamingResponse(client.security)
        self.dns = dns.AsyncDNSResourceWithStreamingResponse(client.dns)
        self.storage = storage.AsyncStorageResourceWithStreamingResponse(client.storage)
        self.cdn = cdn.AsyncCdnResourceWithStreamingResponse(client.cdn)


Client = Gcore

AsyncClient = AsyncGcore
