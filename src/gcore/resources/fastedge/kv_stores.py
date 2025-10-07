# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.fastedge import kv_store_list_params, kv_store_create_params, kv_store_replace_params
from ...types.fastedge.kv_store import KvStore
from ...types.fastedge.kv_store_get_response import KvStoreGetResponse
from ...types.fastedge.kv_store_list_response import KvStoreListResponse

__all__ = ["KvStoresResource", "AsyncKvStoresResource"]


class KvStoresResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> KvStoresResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return KvStoresResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KvStoresResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return KvStoresResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        byod: kv_store_create_params.Byod | Omit = omit,
        comment: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KvStore:
        """
        Add a new KV store

        Args:
          byod: BYOD (Bring Your Own Data) settings

          comment: A description of the store

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/fastedge/v1/kv",
            body=maybe_transform(
                {
                    "byod": byod,
                    "comment": comment,
                },
                kv_store_create_params.KvStoreCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KvStore,
        )

    def list(
        self,
        *,
        app_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KvStoreListResponse:
        """
        List available stores

        Args:
          app_id: App ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/fastedge/v1/kv",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"app_id": app_id}, kv_store_list_params.KvStoreListParams),
            ),
            cast_to=KvStoreListResponse,
        )

    def delete(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a store

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/fastedge/v1/kv/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KvStoreGetResponse:
        """
        Get store by id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/fastedge/v1/kv/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KvStoreGetResponse,
        )

    def replace(
        self,
        id: int,
        *,
        byod: kv_store_replace_params.Byod | Omit = omit,
        comment: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KvStore:
        """
        Update a store

        Args:
          byod: BYOD (Bring Your Own Data) settings

          comment: A description of the store

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/fastedge/v1/kv/{id}",
            body=maybe_transform(
                {
                    "byod": byod,
                    "comment": comment,
                },
                kv_store_replace_params.KvStoreReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KvStore,
        )


class AsyncKvStoresResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncKvStoresResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncKvStoresResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKvStoresResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncKvStoresResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        byod: kv_store_create_params.Byod | Omit = omit,
        comment: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KvStore:
        """
        Add a new KV store

        Args:
          byod: BYOD (Bring Your Own Data) settings

          comment: A description of the store

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/fastedge/v1/kv",
            body=await async_maybe_transform(
                {
                    "byod": byod,
                    "comment": comment,
                },
                kv_store_create_params.KvStoreCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KvStore,
        )

    async def list(
        self,
        *,
        app_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KvStoreListResponse:
        """
        List available stores

        Args:
          app_id: App ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/fastedge/v1/kv",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"app_id": app_id}, kv_store_list_params.KvStoreListParams),
            ),
            cast_to=KvStoreListResponse,
        )

    async def delete(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a store

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/fastedge/v1/kv/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KvStoreGetResponse:
        """
        Get store by id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/fastedge/v1/kv/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KvStoreGetResponse,
        )

    async def replace(
        self,
        id: int,
        *,
        byod: kv_store_replace_params.Byod | Omit = omit,
        comment: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KvStore:
        """
        Update a store

        Args:
          byod: BYOD (Bring Your Own Data) settings

          comment: A description of the store

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/fastedge/v1/kv/{id}",
            body=await async_maybe_transform(
                {
                    "byod": byod,
                    "comment": comment,
                },
                kv_store_replace_params.KvStoreReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KvStore,
        )


class KvStoresResourceWithRawResponse:
    def __init__(self, kv_stores: KvStoresResource) -> None:
        self._kv_stores = kv_stores

        self.create = to_raw_response_wrapper(
            kv_stores.create,
        )
        self.list = to_raw_response_wrapper(
            kv_stores.list,
        )
        self.delete = to_raw_response_wrapper(
            kv_stores.delete,
        )
        self.get = to_raw_response_wrapper(
            kv_stores.get,
        )
        self.replace = to_raw_response_wrapper(
            kv_stores.replace,
        )


class AsyncKvStoresResourceWithRawResponse:
    def __init__(self, kv_stores: AsyncKvStoresResource) -> None:
        self._kv_stores = kv_stores

        self.create = async_to_raw_response_wrapper(
            kv_stores.create,
        )
        self.list = async_to_raw_response_wrapper(
            kv_stores.list,
        )
        self.delete = async_to_raw_response_wrapper(
            kv_stores.delete,
        )
        self.get = async_to_raw_response_wrapper(
            kv_stores.get,
        )
        self.replace = async_to_raw_response_wrapper(
            kv_stores.replace,
        )


class KvStoresResourceWithStreamingResponse:
    def __init__(self, kv_stores: KvStoresResource) -> None:
        self._kv_stores = kv_stores

        self.create = to_streamed_response_wrapper(
            kv_stores.create,
        )
        self.list = to_streamed_response_wrapper(
            kv_stores.list,
        )
        self.delete = to_streamed_response_wrapper(
            kv_stores.delete,
        )
        self.get = to_streamed_response_wrapper(
            kv_stores.get,
        )
        self.replace = to_streamed_response_wrapper(
            kv_stores.replace,
        )


class AsyncKvStoresResourceWithStreamingResponse:
    def __init__(self, kv_stores: AsyncKvStoresResource) -> None:
        self._kv_stores = kv_stores

        self.create = async_to_streamed_response_wrapper(
            kv_stores.create,
        )
        self.list = async_to_streamed_response_wrapper(
            kv_stores.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            kv_stores.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            kv_stores.get,
        )
        self.replace = async_to_streamed_response_wrapper(
            kv_stores.replace,
        )
