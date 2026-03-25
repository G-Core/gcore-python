# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .secrets import (
    SecretsResource,
    AsyncSecretsResource,
    SecretsResourceWithRawResponse,
    AsyncSecretsResourceWithRawResponse,
    SecretsResourceWithStreamingResponse,
    AsyncSecretsResourceWithStreamingResponse,
)
from ..._types import Body, Query, Headers, NotGiven, not_given
from .binaries import (
    BinariesResource,
    AsyncBinariesResource,
    BinariesResourceWithRawResponse,
    AsyncBinariesResourceWithRawResponse,
    BinariesResourceWithStreamingResponse,
    AsyncBinariesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .apps.apps import (
    AppsResource,
    AsyncAppsResource,
    AppsResourceWithRawResponse,
    AsyncAppsResourceWithRawResponse,
    AppsResourceWithStreamingResponse,
    AsyncAppsResourceWithStreamingResponse,
)
from .kv_stores import (
    KvStoresResource,
    AsyncKvStoresResource,
    KvStoresResourceWithRawResponse,
    AsyncKvStoresResourceWithRawResponse,
    KvStoresResourceWithStreamingResponse,
    AsyncKvStoresResourceWithStreamingResponse,
)
from .templates import (
    TemplatesResource,
    AsyncTemplatesResource,
    TemplatesResourceWithRawResponse,
    AsyncTemplatesResourceWithRawResponse,
    TemplatesResourceWithStreamingResponse,
    AsyncTemplatesResourceWithStreamingResponse,
)
from .statistics import (
    StatisticsResource,
    AsyncStatisticsResource,
    StatisticsResourceWithRawResponse,
    AsyncStatisticsResourceWithRawResponse,
    StatisticsResourceWithStreamingResponse,
    AsyncStatisticsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.fastedge.client import Client

__all__ = ["FastedgeResource", "AsyncFastedgeResource"]


class FastedgeResource(SyncAPIResource):
    """Client-level settings and limits"""

    @cached_property
    def templates(self) -> TemplatesResource:
        """
        FastEdge templates encapsulate reusable configurations for FastEdge applications, including a WebAssembly binary reference and configurable parameters.
        """
        return TemplatesResource(self._client)

    @cached_property
    def secrets(self) -> SecretsResource:
        """
        FastEdge secrets store sensitive values such as API keys and tokens that can be referenced by FastEdge applications.
        """
        return SecretsResource(self._client)

    @cached_property
    def binaries(self) -> BinariesResource:
        """
        FastEdge binaries are immutable WebAssembly modules that implement edge application logic.
        """
        return BinariesResource(self._client)

    @cached_property
    def statistics(self) -> StatisticsResource:
        """Statistics of edge app use"""
        return StatisticsResource(self._client)

    @cached_property
    def apps(self) -> AppsResource:
        """
        FastEdge applications combine a WebAssembly binary with configuration, environment variables, and secrets for deployment at the CDN edge.
        """
        return AppsResource(self._client)

    @cached_property
    def kv_stores(self) -> KvStoresResource:
        """Key-value edge storage for apps"""
        return KvStoresResource(self._client)

    @cached_property
    def with_raw_response(self) -> FastedgeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return FastedgeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FastedgeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return FastedgeResourceWithStreamingResponse(self)

    def get_account_overview(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Client:
        """
        Retrieve the authenticated client's account status, resource quotas, and usage
        limits. Shows current plan, available resources, and any active restrictions.
        """
        return self._get(
            "/fastedge/v1/me",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Client,
        )


class AsyncFastedgeResource(AsyncAPIResource):
    """Client-level settings and limits"""

    @cached_property
    def templates(self) -> AsyncTemplatesResource:
        """
        FastEdge templates encapsulate reusable configurations for FastEdge applications, including a WebAssembly binary reference and configurable parameters.
        """
        return AsyncTemplatesResource(self._client)

    @cached_property
    def secrets(self) -> AsyncSecretsResource:
        """
        FastEdge secrets store sensitive values such as API keys and tokens that can be referenced by FastEdge applications.
        """
        return AsyncSecretsResource(self._client)

    @cached_property
    def binaries(self) -> AsyncBinariesResource:
        """
        FastEdge binaries are immutable WebAssembly modules that implement edge application logic.
        """
        return AsyncBinariesResource(self._client)

    @cached_property
    def statistics(self) -> AsyncStatisticsResource:
        """Statistics of edge app use"""
        return AsyncStatisticsResource(self._client)

    @cached_property
    def apps(self) -> AsyncAppsResource:
        """
        FastEdge applications combine a WebAssembly binary with configuration, environment variables, and secrets for deployment at the CDN edge.
        """
        return AsyncAppsResource(self._client)

    @cached_property
    def kv_stores(self) -> AsyncKvStoresResource:
        """Key-value edge storage for apps"""
        return AsyncKvStoresResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFastedgeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFastedgeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFastedgeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncFastedgeResourceWithStreamingResponse(self)

    async def get_account_overview(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Client:
        """
        Retrieve the authenticated client's account status, resource quotas, and usage
        limits. Shows current plan, available resources, and any active restrictions.
        """
        return await self._get(
            "/fastedge/v1/me",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Client,
        )


class FastedgeResourceWithRawResponse:
    def __init__(self, fastedge: FastedgeResource) -> None:
        self._fastedge = fastedge

        self.get_account_overview = to_raw_response_wrapper(
            fastedge.get_account_overview,
        )

    @cached_property
    def templates(self) -> TemplatesResourceWithRawResponse:
        """
        FastEdge templates encapsulate reusable configurations for FastEdge applications, including a WebAssembly binary reference and configurable parameters.
        """
        return TemplatesResourceWithRawResponse(self._fastedge.templates)

    @cached_property
    def secrets(self) -> SecretsResourceWithRawResponse:
        """
        FastEdge secrets store sensitive values such as API keys and tokens that can be referenced by FastEdge applications.
        """
        return SecretsResourceWithRawResponse(self._fastedge.secrets)

    @cached_property
    def binaries(self) -> BinariesResourceWithRawResponse:
        """
        FastEdge binaries are immutable WebAssembly modules that implement edge application logic.
        """
        return BinariesResourceWithRawResponse(self._fastedge.binaries)

    @cached_property
    def statistics(self) -> StatisticsResourceWithRawResponse:
        """Statistics of edge app use"""
        return StatisticsResourceWithRawResponse(self._fastedge.statistics)

    @cached_property
    def apps(self) -> AppsResourceWithRawResponse:
        """
        FastEdge applications combine a WebAssembly binary with configuration, environment variables, and secrets for deployment at the CDN edge.
        """
        return AppsResourceWithRawResponse(self._fastedge.apps)

    @cached_property
    def kv_stores(self) -> KvStoresResourceWithRawResponse:
        """Key-value edge storage for apps"""
        return KvStoresResourceWithRawResponse(self._fastedge.kv_stores)


class AsyncFastedgeResourceWithRawResponse:
    def __init__(self, fastedge: AsyncFastedgeResource) -> None:
        self._fastedge = fastedge

        self.get_account_overview = async_to_raw_response_wrapper(
            fastedge.get_account_overview,
        )

    @cached_property
    def templates(self) -> AsyncTemplatesResourceWithRawResponse:
        """
        FastEdge templates encapsulate reusable configurations for FastEdge applications, including a WebAssembly binary reference and configurable parameters.
        """
        return AsyncTemplatesResourceWithRawResponse(self._fastedge.templates)

    @cached_property
    def secrets(self) -> AsyncSecretsResourceWithRawResponse:
        """
        FastEdge secrets store sensitive values such as API keys and tokens that can be referenced by FastEdge applications.
        """
        return AsyncSecretsResourceWithRawResponse(self._fastedge.secrets)

    @cached_property
    def binaries(self) -> AsyncBinariesResourceWithRawResponse:
        """
        FastEdge binaries are immutable WebAssembly modules that implement edge application logic.
        """
        return AsyncBinariesResourceWithRawResponse(self._fastedge.binaries)

    @cached_property
    def statistics(self) -> AsyncStatisticsResourceWithRawResponse:
        """Statistics of edge app use"""
        return AsyncStatisticsResourceWithRawResponse(self._fastedge.statistics)

    @cached_property
    def apps(self) -> AsyncAppsResourceWithRawResponse:
        """
        FastEdge applications combine a WebAssembly binary with configuration, environment variables, and secrets for deployment at the CDN edge.
        """
        return AsyncAppsResourceWithRawResponse(self._fastedge.apps)

    @cached_property
    def kv_stores(self) -> AsyncKvStoresResourceWithRawResponse:
        """Key-value edge storage for apps"""
        return AsyncKvStoresResourceWithRawResponse(self._fastedge.kv_stores)


class FastedgeResourceWithStreamingResponse:
    def __init__(self, fastedge: FastedgeResource) -> None:
        self._fastedge = fastedge

        self.get_account_overview = to_streamed_response_wrapper(
            fastedge.get_account_overview,
        )

    @cached_property
    def templates(self) -> TemplatesResourceWithStreamingResponse:
        """
        FastEdge templates encapsulate reusable configurations for FastEdge applications, including a WebAssembly binary reference and configurable parameters.
        """
        return TemplatesResourceWithStreamingResponse(self._fastedge.templates)

    @cached_property
    def secrets(self) -> SecretsResourceWithStreamingResponse:
        """
        FastEdge secrets store sensitive values such as API keys and tokens that can be referenced by FastEdge applications.
        """
        return SecretsResourceWithStreamingResponse(self._fastedge.secrets)

    @cached_property
    def binaries(self) -> BinariesResourceWithStreamingResponse:
        """
        FastEdge binaries are immutable WebAssembly modules that implement edge application logic.
        """
        return BinariesResourceWithStreamingResponse(self._fastedge.binaries)

    @cached_property
    def statistics(self) -> StatisticsResourceWithStreamingResponse:
        """Statistics of edge app use"""
        return StatisticsResourceWithStreamingResponse(self._fastedge.statistics)

    @cached_property
    def apps(self) -> AppsResourceWithStreamingResponse:
        """
        FastEdge applications combine a WebAssembly binary with configuration, environment variables, and secrets for deployment at the CDN edge.
        """
        return AppsResourceWithStreamingResponse(self._fastedge.apps)

    @cached_property
    def kv_stores(self) -> KvStoresResourceWithStreamingResponse:
        """Key-value edge storage for apps"""
        return KvStoresResourceWithStreamingResponse(self._fastedge.kv_stores)


class AsyncFastedgeResourceWithStreamingResponse:
    def __init__(self, fastedge: AsyncFastedgeResource) -> None:
        self._fastedge = fastedge

        self.get_account_overview = async_to_streamed_response_wrapper(
            fastedge.get_account_overview,
        )

    @cached_property
    def templates(self) -> AsyncTemplatesResourceWithStreamingResponse:
        """
        FastEdge templates encapsulate reusable configurations for FastEdge applications, including a WebAssembly binary reference and configurable parameters.
        """
        return AsyncTemplatesResourceWithStreamingResponse(self._fastedge.templates)

    @cached_property
    def secrets(self) -> AsyncSecretsResourceWithStreamingResponse:
        """
        FastEdge secrets store sensitive values such as API keys and tokens that can be referenced by FastEdge applications.
        """
        return AsyncSecretsResourceWithStreamingResponse(self._fastedge.secrets)

    @cached_property
    def binaries(self) -> AsyncBinariesResourceWithStreamingResponse:
        """
        FastEdge binaries are immutable WebAssembly modules that implement edge application logic.
        """
        return AsyncBinariesResourceWithStreamingResponse(self._fastedge.binaries)

    @cached_property
    def statistics(self) -> AsyncStatisticsResourceWithStreamingResponse:
        """Statistics of edge app use"""
        return AsyncStatisticsResourceWithStreamingResponse(self._fastedge.statistics)

    @cached_property
    def apps(self) -> AsyncAppsResourceWithStreamingResponse:
        """
        FastEdge applications combine a WebAssembly binary with configuration, environment variables, and secrets for deployment at the CDN edge.
        """
        return AsyncAppsResourceWithStreamingResponse(self._fastedge.apps)

    @cached_property
    def kv_stores(self) -> AsyncKvStoresResourceWithStreamingResponse:
        """Key-value edge storage for apps"""
        return AsyncKvStoresResourceWithStreamingResponse(self._fastedge.kv_stores)
