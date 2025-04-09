# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .global_ import (
    GlobalResource,
    AsyncGlobalResource,
    GlobalResourceWithRawResponse,
    AsyncGlobalResourceWithRawResponse,
    GlobalResourceWithStreamingResponse,
    AsyncGlobalResourceWithStreamingResponse,
)
from .regional import (
    RegionalResource,
    AsyncRegionalResource,
    RegionalResourceWithRawResponse,
    AsyncRegionalResourceWithRawResponse,
    RegionalResourceWithStreamingResponse,
    AsyncRegionalResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .client_quotas import (
    ClientQuotasResource,
    AsyncClientQuotasResource,
    ClientQuotasResourceWithRawResponse,
    AsyncClientQuotasResourceWithRawResponse,
    ClientQuotasResourceWithStreamingResponse,
    AsyncClientQuotasResourceWithStreamingResponse,
)
from .limits_request import (
    LimitsRequestResource,
    AsyncLimitsRequestResource,
    LimitsRequestResourceWithRawResponse,
    AsyncLimitsRequestResourceWithRawResponse,
    LimitsRequestResourceWithStreamingResponse,
    AsyncLimitsRequestResourceWithStreamingResponse,
)

__all__ = ["QuotasResource", "AsyncQuotasResource"]


class QuotasResource(SyncAPIResource):
    @cached_property
    def client_quotas(self) -> ClientQuotasResource:
        return ClientQuotasResource(self._client)

    @cached_property
    def global_(self) -> GlobalResource:
        return GlobalResource(self._client)

    @cached_property
    def regional(self) -> RegionalResource:
        return RegionalResource(self._client)

    @cached_property
    def limits_request(self) -> LimitsRequestResource:
        return LimitsRequestResource(self._client)

    @cached_property
    def with_raw_response(self) -> QuotasResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return QuotasResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QuotasResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
        """
        return QuotasResourceWithStreamingResponse(self)


class AsyncQuotasResource(AsyncAPIResource):
    @cached_property
    def client_quotas(self) -> AsyncClientQuotasResource:
        return AsyncClientQuotasResource(self._client)

    @cached_property
    def global_(self) -> AsyncGlobalResource:
        return AsyncGlobalResource(self._client)

    @cached_property
    def regional(self) -> AsyncRegionalResource:
        return AsyncRegionalResource(self._client)

    @cached_property
    def limits_request(self) -> AsyncLimitsRequestResource:
        return AsyncLimitsRequestResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncQuotasResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncQuotasResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQuotasResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
        """
        return AsyncQuotasResourceWithStreamingResponse(self)


class QuotasResourceWithRawResponse:
    def __init__(self, quotas: QuotasResource) -> None:
        self._quotas = quotas

    @cached_property
    def client_quotas(self) -> ClientQuotasResourceWithRawResponse:
        return ClientQuotasResourceWithRawResponse(self._quotas.client_quotas)

    @cached_property
    def global_(self) -> GlobalResourceWithRawResponse:
        return GlobalResourceWithRawResponse(self._quotas.global_)

    @cached_property
    def regional(self) -> RegionalResourceWithRawResponse:
        return RegionalResourceWithRawResponse(self._quotas.regional)

    @cached_property
    def limits_request(self) -> LimitsRequestResourceWithRawResponse:
        return LimitsRequestResourceWithRawResponse(self._quotas.limits_request)


class AsyncQuotasResourceWithRawResponse:
    def __init__(self, quotas: AsyncQuotasResource) -> None:
        self._quotas = quotas

    @cached_property
    def client_quotas(self) -> AsyncClientQuotasResourceWithRawResponse:
        return AsyncClientQuotasResourceWithRawResponse(self._quotas.client_quotas)

    @cached_property
    def global_(self) -> AsyncGlobalResourceWithRawResponse:
        return AsyncGlobalResourceWithRawResponse(self._quotas.global_)

    @cached_property
    def regional(self) -> AsyncRegionalResourceWithRawResponse:
        return AsyncRegionalResourceWithRawResponse(self._quotas.regional)

    @cached_property
    def limits_request(self) -> AsyncLimitsRequestResourceWithRawResponse:
        return AsyncLimitsRequestResourceWithRawResponse(self._quotas.limits_request)


class QuotasResourceWithStreamingResponse:
    def __init__(self, quotas: QuotasResource) -> None:
        self._quotas = quotas

    @cached_property
    def client_quotas(self) -> ClientQuotasResourceWithStreamingResponse:
        return ClientQuotasResourceWithStreamingResponse(self._quotas.client_quotas)

    @cached_property
    def global_(self) -> GlobalResourceWithStreamingResponse:
        return GlobalResourceWithStreamingResponse(self._quotas.global_)

    @cached_property
    def regional(self) -> RegionalResourceWithStreamingResponse:
        return RegionalResourceWithStreamingResponse(self._quotas.regional)

    @cached_property
    def limits_request(self) -> LimitsRequestResourceWithStreamingResponse:
        return LimitsRequestResourceWithStreamingResponse(self._quotas.limits_request)


class AsyncQuotasResourceWithStreamingResponse:
    def __init__(self, quotas: AsyncQuotasResource) -> None:
        self._quotas = quotas

    @cached_property
    def client_quotas(self) -> AsyncClientQuotasResourceWithStreamingResponse:
        return AsyncClientQuotasResourceWithStreamingResponse(self._quotas.client_quotas)

    @cached_property
    def global_(self) -> AsyncGlobalResourceWithStreamingResponse:
        return AsyncGlobalResourceWithStreamingResponse(self._quotas.global_)

    @cached_property
    def regional(self) -> AsyncRegionalResourceWithStreamingResponse:
        return AsyncRegionalResourceWithStreamingResponse(self._quotas.regional)

    @cached_property
    def limits_request(self) -> AsyncLimitsRequestResourceWithStreamingResponse:
        return AsyncLimitsRequestResourceWithStreamingResponse(self._quotas.limits_request)
