# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
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
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import GcoreError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import cdn, dns, iam, waap, cloud, storage, fastedge, security, streaming
    from .resources.cdn.cdn import CdnResource, AsyncCdnResource
    from .resources.dns.dns import DNSResource, AsyncDNSResource
    from .resources.iam.iam import IamResource, AsyncIamResource
    from .resources.waap.waap import WaapResource, AsyncWaapResource
    from .resources.cloud.cloud import CloudResource, AsyncCloudResource
    from .resources.storage.storage import StorageResource, AsyncStorageResource
    from .resources.fastedge.fastedge import FastedgeResource, AsyncFastedgeResource
    from .resources.security.security import SecurityResource, AsyncSecurityResource
    from .resources.streaming.streaming import StreamingResource, AsyncStreamingResource

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Gcore", "AsyncGcore", "Client", "AsyncClient"]


class Gcore(SyncAPIClient):
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

    @cached_property
    def cloud(self) -> CloudResource:
        from .resources.cloud import CloudResource

        return CloudResource(self)

    @cached_property
    def waap(self) -> WaapResource:
        from .resources.waap import WaapResource

        return WaapResource(self)

    @cached_property
    def iam(self) -> IamResource:
        from .resources.iam import IamResource

        return IamResource(self)

    @cached_property
    def fastedge(self) -> FastedgeResource:
        from .resources.fastedge import FastedgeResource

        return FastedgeResource(self)

    @cached_property
    def streaming(self) -> StreamingResource:
        from .resources.streaming import StreamingResource

        return StreamingResource(self)

    @cached_property
    def security(self) -> SecurityResource:
        from .resources.security import SecurityResource

        return SecurityResource(self)

    @cached_property
    def dns(self) -> DNSResource:
        from .resources.dns import DNSResource

        return DNSResource(self)

    @cached_property
    def storage(self) -> StorageResource:
        from .resources.storage import StorageResource

        return StorageResource(self)

    @cached_property
    def cdn(self) -> CdnResource:
        from .resources.cdn import CdnResource

        return CdnResource(self)

    @cached_property
    def with_raw_response(self) -> GcoreWithRawResponse:
        return GcoreWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GcoreWithStreamedResponse:
        return GcoreWithStreamedResponse(self)

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

    @cached_property
    def cloud(self) -> AsyncCloudResource:
        from .resources.cloud import AsyncCloudResource

        return AsyncCloudResource(self)

    @cached_property
    def waap(self) -> AsyncWaapResource:
        from .resources.waap import AsyncWaapResource

        return AsyncWaapResource(self)

    @cached_property
    def iam(self) -> AsyncIamResource:
        from .resources.iam import AsyncIamResource

        return AsyncIamResource(self)

    @cached_property
    def fastedge(self) -> AsyncFastedgeResource:
        from .resources.fastedge import AsyncFastedgeResource

        return AsyncFastedgeResource(self)

    @cached_property
    def streaming(self) -> AsyncStreamingResource:
        from .resources.streaming import AsyncStreamingResource

        return AsyncStreamingResource(self)

    @cached_property
    def security(self) -> AsyncSecurityResource:
        from .resources.security import AsyncSecurityResource

        return AsyncSecurityResource(self)

    @cached_property
    def dns(self) -> AsyncDNSResource:
        from .resources.dns import AsyncDNSResource

        return AsyncDNSResource(self)

    @cached_property
    def storage(self) -> AsyncStorageResource:
        from .resources.storage import AsyncStorageResource

        return AsyncStorageResource(self)

    @cached_property
    def cdn(self) -> AsyncCdnResource:
        from .resources.cdn import AsyncCdnResource

        return AsyncCdnResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncGcoreWithRawResponse:
        return AsyncGcoreWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGcoreWithStreamedResponse:
        return AsyncGcoreWithStreamedResponse(self)

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
    _client: Gcore

    def __init__(self, client: Gcore) -> None:
        self._client = client

    @cached_property
    def cloud(self) -> cloud.CloudResourceWithRawResponse:
        from .resources.cloud import CloudResourceWithRawResponse

        return CloudResourceWithRawResponse(self._client.cloud)

    @cached_property
    def waap(self) -> waap.WaapResourceWithRawResponse:
        from .resources.waap import WaapResourceWithRawResponse

        return WaapResourceWithRawResponse(self._client.waap)

    @cached_property
    def iam(self) -> iam.IamResourceWithRawResponse:
        from .resources.iam import IamResourceWithRawResponse

        return IamResourceWithRawResponse(self._client.iam)

    @cached_property
    def fastedge(self) -> fastedge.FastedgeResourceWithRawResponse:
        from .resources.fastedge import FastedgeResourceWithRawResponse

        return FastedgeResourceWithRawResponse(self._client.fastedge)

    @cached_property
    def streaming(self) -> streaming.StreamingResourceWithRawResponse:
        from .resources.streaming import StreamingResourceWithRawResponse

        return StreamingResourceWithRawResponse(self._client.streaming)

    @cached_property
    def security(self) -> security.SecurityResourceWithRawResponse:
        from .resources.security import SecurityResourceWithRawResponse

        return SecurityResourceWithRawResponse(self._client.security)

    @cached_property
    def dns(self) -> dns.DNSResourceWithRawResponse:
        from .resources.dns import DNSResourceWithRawResponse

        return DNSResourceWithRawResponse(self._client.dns)

    @cached_property
    def storage(self) -> storage.StorageResourceWithRawResponse:
        from .resources.storage import StorageResourceWithRawResponse

        return StorageResourceWithRawResponse(self._client.storage)

    @cached_property
    def cdn(self) -> cdn.CdnResourceWithRawResponse:
        from .resources.cdn import CdnResourceWithRawResponse

        return CdnResourceWithRawResponse(self._client.cdn)


class AsyncGcoreWithRawResponse:
    _client: AsyncGcore

    def __init__(self, client: AsyncGcore) -> None:
        self._client = client

    @cached_property
    def cloud(self) -> cloud.AsyncCloudResourceWithRawResponse:
        from .resources.cloud import AsyncCloudResourceWithRawResponse

        return AsyncCloudResourceWithRawResponse(self._client.cloud)

    @cached_property
    def waap(self) -> waap.AsyncWaapResourceWithRawResponse:
        from .resources.waap import AsyncWaapResourceWithRawResponse

        return AsyncWaapResourceWithRawResponse(self._client.waap)

    @cached_property
    def iam(self) -> iam.AsyncIamResourceWithRawResponse:
        from .resources.iam import AsyncIamResourceWithRawResponse

        return AsyncIamResourceWithRawResponse(self._client.iam)

    @cached_property
    def fastedge(self) -> fastedge.AsyncFastedgeResourceWithRawResponse:
        from .resources.fastedge import AsyncFastedgeResourceWithRawResponse

        return AsyncFastedgeResourceWithRawResponse(self._client.fastedge)

    @cached_property
    def streaming(self) -> streaming.AsyncStreamingResourceWithRawResponse:
        from .resources.streaming import AsyncStreamingResourceWithRawResponse

        return AsyncStreamingResourceWithRawResponse(self._client.streaming)

    @cached_property
    def security(self) -> security.AsyncSecurityResourceWithRawResponse:
        from .resources.security import AsyncSecurityResourceWithRawResponse

        return AsyncSecurityResourceWithRawResponse(self._client.security)

    @cached_property
    def dns(self) -> dns.AsyncDNSResourceWithRawResponse:
        from .resources.dns import AsyncDNSResourceWithRawResponse

        return AsyncDNSResourceWithRawResponse(self._client.dns)

    @cached_property
    def storage(self) -> storage.AsyncStorageResourceWithRawResponse:
        from .resources.storage import AsyncStorageResourceWithRawResponse

        return AsyncStorageResourceWithRawResponse(self._client.storage)

    @cached_property
    def cdn(self) -> cdn.AsyncCdnResourceWithRawResponse:
        from .resources.cdn import AsyncCdnResourceWithRawResponse

        return AsyncCdnResourceWithRawResponse(self._client.cdn)


class GcoreWithStreamedResponse:
    _client: Gcore

    def __init__(self, client: Gcore) -> None:
        self._client = client

    @cached_property
    def cloud(self) -> cloud.CloudResourceWithStreamingResponse:
        from .resources.cloud import CloudResourceWithStreamingResponse

        return CloudResourceWithStreamingResponse(self._client.cloud)

    @cached_property
    def waap(self) -> waap.WaapResourceWithStreamingResponse:
        from .resources.waap import WaapResourceWithStreamingResponse

        return WaapResourceWithStreamingResponse(self._client.waap)

    @cached_property
    def iam(self) -> iam.IamResourceWithStreamingResponse:
        from .resources.iam import IamResourceWithStreamingResponse

        return IamResourceWithStreamingResponse(self._client.iam)

    @cached_property
    def fastedge(self) -> fastedge.FastedgeResourceWithStreamingResponse:
        from .resources.fastedge import FastedgeResourceWithStreamingResponse

        return FastedgeResourceWithStreamingResponse(self._client.fastedge)

    @cached_property
    def streaming(self) -> streaming.StreamingResourceWithStreamingResponse:
        from .resources.streaming import StreamingResourceWithStreamingResponse

        return StreamingResourceWithStreamingResponse(self._client.streaming)

    @cached_property
    def security(self) -> security.SecurityResourceWithStreamingResponse:
        from .resources.security import SecurityResourceWithStreamingResponse

        return SecurityResourceWithStreamingResponse(self._client.security)

    @cached_property
    def dns(self) -> dns.DNSResourceWithStreamingResponse:
        from .resources.dns import DNSResourceWithStreamingResponse

        return DNSResourceWithStreamingResponse(self._client.dns)

    @cached_property
    def storage(self) -> storage.StorageResourceWithStreamingResponse:
        from .resources.storage import StorageResourceWithStreamingResponse

        return StorageResourceWithStreamingResponse(self._client.storage)

    @cached_property
    def cdn(self) -> cdn.CdnResourceWithStreamingResponse:
        from .resources.cdn import CdnResourceWithStreamingResponse

        return CdnResourceWithStreamingResponse(self._client.cdn)


class AsyncGcoreWithStreamedResponse:
    _client: AsyncGcore

    def __init__(self, client: AsyncGcore) -> None:
        self._client = client

    @cached_property
    def cloud(self) -> cloud.AsyncCloudResourceWithStreamingResponse:
        from .resources.cloud import AsyncCloudResourceWithStreamingResponse

        return AsyncCloudResourceWithStreamingResponse(self._client.cloud)

    @cached_property
    def waap(self) -> waap.AsyncWaapResourceWithStreamingResponse:
        from .resources.waap import AsyncWaapResourceWithStreamingResponse

        return AsyncWaapResourceWithStreamingResponse(self._client.waap)

    @cached_property
    def iam(self) -> iam.AsyncIamResourceWithStreamingResponse:
        from .resources.iam import AsyncIamResourceWithStreamingResponse

        return AsyncIamResourceWithStreamingResponse(self._client.iam)

    @cached_property
    def fastedge(self) -> fastedge.AsyncFastedgeResourceWithStreamingResponse:
        from .resources.fastedge import AsyncFastedgeResourceWithStreamingResponse

        return AsyncFastedgeResourceWithStreamingResponse(self._client.fastedge)

    @cached_property
    def streaming(self) -> streaming.AsyncStreamingResourceWithStreamingResponse:
        from .resources.streaming import AsyncStreamingResourceWithStreamingResponse

        return AsyncStreamingResourceWithStreamingResponse(self._client.streaming)

    @cached_property
    def security(self) -> security.AsyncSecurityResourceWithStreamingResponse:
        from .resources.security import AsyncSecurityResourceWithStreamingResponse

        return AsyncSecurityResourceWithStreamingResponse(self._client.security)

    @cached_property
    def dns(self) -> dns.AsyncDNSResourceWithStreamingResponse:
        from .resources.dns import AsyncDNSResourceWithStreamingResponse

        return AsyncDNSResourceWithStreamingResponse(self._client.dns)

    @cached_property
    def storage(self) -> storage.AsyncStorageResourceWithStreamingResponse:
        from .resources.storage import AsyncStorageResourceWithStreamingResponse

        return AsyncStorageResourceWithStreamingResponse(self._client.storage)

    @cached_property
    def cdn(self) -> cdn.AsyncCdnResourceWithStreamingResponse:
        from .resources.cdn import AsyncCdnResourceWithStreamingResponse

        return AsyncCdnResourceWithStreamingResponse(self._client.cdn)


Client = Gcore

AsyncClient = AsyncGcore
