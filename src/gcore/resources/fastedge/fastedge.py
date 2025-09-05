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
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
    @cached_property
    def templates(self) -> TemplatesResource:
        return TemplatesResource(self._client)

    @cached_property
    def secrets(self) -> SecretsResource:
        return SecretsResource(self._client)

    @cached_property
    def binaries(self) -> BinariesResource:
        return BinariesResource(self._client)

    @cached_property
    def statistics(self) -> StatisticsResource:
        return StatisticsResource(self._client)

    @cached_property
    def apps(self) -> AppsResource:
        return AppsResource(self._client)

    @cached_property
    def kv_stores(self) -> KvStoresResource:
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
    @cached_property
    def templates(self) -> AsyncTemplatesResource:
        return AsyncTemplatesResource(self._client)

    @cached_property
    def secrets(self) -> AsyncSecretsResource:
        return AsyncSecretsResource(self._client)

    @cached_property
    def binaries(self) -> AsyncBinariesResource:
        return AsyncBinariesResource(self._client)

    @cached_property
    def statistics(self) -> AsyncStatisticsResource:
        return AsyncStatisticsResource(self._client)

    @cached_property
    def apps(self) -> AsyncAppsResource:
        return AsyncAppsResource(self._client)

    @cached_property
    def kv_stores(self) -> AsyncKvStoresResource:
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        return TemplatesResourceWithRawResponse(self._fastedge.templates)

    @cached_property
    def secrets(self) -> SecretsResourceWithRawResponse:
        return SecretsResourceWithRawResponse(self._fastedge.secrets)

    @cached_property
    def binaries(self) -> BinariesResourceWithRawResponse:
        return BinariesResourceWithRawResponse(self._fastedge.binaries)

    @cached_property
    def statistics(self) -> StatisticsResourceWithRawResponse:
        return StatisticsResourceWithRawResponse(self._fastedge.statistics)

    @cached_property
    def apps(self) -> AppsResourceWithRawResponse:
        return AppsResourceWithRawResponse(self._fastedge.apps)

    @cached_property
    def kv_stores(self) -> KvStoresResourceWithRawResponse:
        return KvStoresResourceWithRawResponse(self._fastedge.kv_stores)


class AsyncFastedgeResourceWithRawResponse:
    def __init__(self, fastedge: AsyncFastedgeResource) -> None:
        self._fastedge = fastedge

        self.get_account_overview = async_to_raw_response_wrapper(
            fastedge.get_account_overview,
        )

    @cached_property
    def templates(self) -> AsyncTemplatesResourceWithRawResponse:
        return AsyncTemplatesResourceWithRawResponse(self._fastedge.templates)

    @cached_property
    def secrets(self) -> AsyncSecretsResourceWithRawResponse:
        return AsyncSecretsResourceWithRawResponse(self._fastedge.secrets)

    @cached_property
    def binaries(self) -> AsyncBinariesResourceWithRawResponse:
        return AsyncBinariesResourceWithRawResponse(self._fastedge.binaries)

    @cached_property
    def statistics(self) -> AsyncStatisticsResourceWithRawResponse:
        return AsyncStatisticsResourceWithRawResponse(self._fastedge.statistics)

    @cached_property
    def apps(self) -> AsyncAppsResourceWithRawResponse:
        return AsyncAppsResourceWithRawResponse(self._fastedge.apps)

    @cached_property
    def kv_stores(self) -> AsyncKvStoresResourceWithRawResponse:
        return AsyncKvStoresResourceWithRawResponse(self._fastedge.kv_stores)


class FastedgeResourceWithStreamingResponse:
    def __init__(self, fastedge: FastedgeResource) -> None:
        self._fastedge = fastedge

        self.get_account_overview = to_streamed_response_wrapper(
            fastedge.get_account_overview,
        )

    @cached_property
    def templates(self) -> TemplatesResourceWithStreamingResponse:
        return TemplatesResourceWithStreamingResponse(self._fastedge.templates)

    @cached_property
    def secrets(self) -> SecretsResourceWithStreamingResponse:
        return SecretsResourceWithStreamingResponse(self._fastedge.secrets)

    @cached_property
    def binaries(self) -> BinariesResourceWithStreamingResponse:
        return BinariesResourceWithStreamingResponse(self._fastedge.binaries)

    @cached_property
    def statistics(self) -> StatisticsResourceWithStreamingResponse:
        return StatisticsResourceWithStreamingResponse(self._fastedge.statistics)

    @cached_property
    def apps(self) -> AppsResourceWithStreamingResponse:
        return AppsResourceWithStreamingResponse(self._fastedge.apps)

    @cached_property
    def kv_stores(self) -> KvStoresResourceWithStreamingResponse:
        return KvStoresResourceWithStreamingResponse(self._fastedge.kv_stores)


class AsyncFastedgeResourceWithStreamingResponse:
    def __init__(self, fastedge: AsyncFastedgeResource) -> None:
        self._fastedge = fastedge

        self.get_account_overview = async_to_streamed_response_wrapper(
            fastedge.get_account_overview,
        )

    @cached_property
    def templates(self) -> AsyncTemplatesResourceWithStreamingResponse:
        return AsyncTemplatesResourceWithStreamingResponse(self._fastedge.templates)

    @cached_property
    def secrets(self) -> AsyncSecretsResourceWithStreamingResponse:
        return AsyncSecretsResourceWithStreamingResponse(self._fastedge.secrets)

    @cached_property
    def binaries(self) -> AsyncBinariesResourceWithStreamingResponse:
        return AsyncBinariesResourceWithStreamingResponse(self._fastedge.binaries)

    @cached_property
    def statistics(self) -> AsyncStatisticsResourceWithStreamingResponse:
        return AsyncStatisticsResourceWithStreamingResponse(self._fastedge.statistics)

    @cached_property
    def apps(self) -> AsyncAppsResourceWithStreamingResponse:
        return AsyncAppsResourceWithStreamingResponse(self._fastedge.apps)

    @cached_property
    def kv_stores(self) -> AsyncKvStoresResourceWithStreamingResponse:
        return AsyncKvStoresResourceWithStreamingResponse(self._fastedge.kv_stores)
