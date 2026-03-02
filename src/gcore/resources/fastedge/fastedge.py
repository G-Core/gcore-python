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
        """Application templates"""
        return TemplatesResource(self._client)

    @cached_property
    def secrets(self) -> SecretsResource:
        """Secret values that can be used in apps"""
        return SecretsResource(self._client)

    @cached_property
    def binaries(self) -> BinariesResource:
        """
        Binaries are WebAssembly executables that are actually executed when app is ran.
        """
        return BinariesResource(self._client)

    @cached_property
    def statistics(self) -> StatisticsResource:
        """Statistics of edge app use"""
        return StatisticsResource(self._client)

    @cached_property
    def apps(self) -> AppsResource:
        """
        Apps are descriptions of edge apps, that reference the binary and may contain app-specific settings, such as environment variables.
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
        """Get status and limits for the client"""
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
        """Application templates"""
        return AsyncTemplatesResource(self._client)

    @cached_property
    def secrets(self) -> AsyncSecretsResource:
        """Secret values that can be used in apps"""
        return AsyncSecretsResource(self._client)

    @cached_property
    def binaries(self) -> AsyncBinariesResource:
        """
        Binaries are WebAssembly executables that are actually executed when app is ran.
        """
        return AsyncBinariesResource(self._client)

    @cached_property
    def statistics(self) -> AsyncStatisticsResource:
        """Statistics of edge app use"""
        return AsyncStatisticsResource(self._client)

    @cached_property
    def apps(self) -> AsyncAppsResource:
        """
        Apps are descriptions of edge apps, that reference the binary and may contain app-specific settings, such as environment variables.
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
        """Get status and limits for the client"""
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
        """Application templates"""
        return TemplatesResourceWithRawResponse(self._fastedge.templates)

    @cached_property
    def secrets(self) -> SecretsResourceWithRawResponse:
        """Secret values that can be used in apps"""
        return SecretsResourceWithRawResponse(self._fastedge.secrets)

    @cached_property
    def binaries(self) -> BinariesResourceWithRawResponse:
        """
        Binaries are WebAssembly executables that are actually executed when app is ran.
        """
        return BinariesResourceWithRawResponse(self._fastedge.binaries)

    @cached_property
    def statistics(self) -> StatisticsResourceWithRawResponse:
        """Statistics of edge app use"""
        return StatisticsResourceWithRawResponse(self._fastedge.statistics)

    @cached_property
    def apps(self) -> AppsResourceWithRawResponse:
        """
        Apps are descriptions of edge apps, that reference the binary and may contain app-specific settings, such as environment variables.
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
        """Application templates"""
        return AsyncTemplatesResourceWithRawResponse(self._fastedge.templates)

    @cached_property
    def secrets(self) -> AsyncSecretsResourceWithRawResponse:
        """Secret values that can be used in apps"""
        return AsyncSecretsResourceWithRawResponse(self._fastedge.secrets)

    @cached_property
    def binaries(self) -> AsyncBinariesResourceWithRawResponse:
        """
        Binaries are WebAssembly executables that are actually executed when app is ran.
        """
        return AsyncBinariesResourceWithRawResponse(self._fastedge.binaries)

    @cached_property
    def statistics(self) -> AsyncStatisticsResourceWithRawResponse:
        """Statistics of edge app use"""
        return AsyncStatisticsResourceWithRawResponse(self._fastedge.statistics)

    @cached_property
    def apps(self) -> AsyncAppsResourceWithRawResponse:
        """
        Apps are descriptions of edge apps, that reference the binary and may contain app-specific settings, such as environment variables.
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
        """Application templates"""
        return TemplatesResourceWithStreamingResponse(self._fastedge.templates)

    @cached_property
    def secrets(self) -> SecretsResourceWithStreamingResponse:
        """Secret values that can be used in apps"""
        return SecretsResourceWithStreamingResponse(self._fastedge.secrets)

    @cached_property
    def binaries(self) -> BinariesResourceWithStreamingResponse:
        """
        Binaries are WebAssembly executables that are actually executed when app is ran.
        """
        return BinariesResourceWithStreamingResponse(self._fastedge.binaries)

    @cached_property
    def statistics(self) -> StatisticsResourceWithStreamingResponse:
        """Statistics of edge app use"""
        return StatisticsResourceWithStreamingResponse(self._fastedge.statistics)

    @cached_property
    def apps(self) -> AppsResourceWithStreamingResponse:
        """
        Apps are descriptions of edge apps, that reference the binary and may contain app-specific settings, such as environment variables.
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
        """Application templates"""
        return AsyncTemplatesResourceWithStreamingResponse(self._fastedge.templates)

    @cached_property
    def secrets(self) -> AsyncSecretsResourceWithStreamingResponse:
        """Secret values that can be used in apps"""
        return AsyncSecretsResourceWithStreamingResponse(self._fastedge.secrets)

    @cached_property
    def binaries(self) -> AsyncBinariesResourceWithStreamingResponse:
        """
        Binaries are WebAssembly executables that are actually executed when app is ran.
        """
        return AsyncBinariesResourceWithStreamingResponse(self._fastedge.binaries)

    @cached_property
    def statistics(self) -> AsyncStatisticsResourceWithStreamingResponse:
        """Statistics of edge app use"""
        return AsyncStatisticsResourceWithStreamingResponse(self._fastedge.statistics)

    @cached_property
    def apps(self) -> AsyncAppsResourceWithStreamingResponse:
        """
        Apps are descriptions of edge apps, that reference the binary and may contain app-specific settings, such as environment variables.
        """
        return AsyncAppsResourceWithStreamingResponse(self._fastedge.apps)

    @cached_property
    def kv_stores(self) -> AsyncKvStoresResourceWithStreamingResponse:
        """Key-value edge storage for apps"""
        return AsyncKvStoresResourceWithStreamingResponse(self._fastedge.kv_stores)
