# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ....types.waap.domains import api_path_list_params, api_path_create_params, api_path_update_params
from ....types.waap.domains.waap_api_path import WaapAPIPath

__all__ = ["APIPathsResource", "AsyncAPIPathsResource"]


class APIPathsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> APIPathsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return APIPathsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> APIPathsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return APIPathsResourceWithStreamingResponse(self)

    def create(
        self,
        domain_id: int,
        *,
        http_scheme: Literal["HTTP", "HTTPS"],
        method: Literal["GET", "POST", "PUT", "PATCH", "DELETE", "TRACE", "HEAD", "OPTIONS"],
        path: str,
        api_groups: SequenceNotStr[str] | Omit = omit,
        api_version: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapAPIPath:
        """
        Create an API path for a domain

        Args:
          domain_id: The domain ID

          http_scheme: The different HTTP schemes an API path can have

          method: The different methods an API path can have

          path: The API path, locations that are saved for resource IDs will be put in curly
              brackets

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/waap/v1/domains/{domain_id}/api-paths",
            body=maybe_transform(
                {
                    "http_scheme": http_scheme,
                    "method": method,
                    "path": path,
                    "api_groups": api_groups,
                    "api_version": api_version,
                    "tags": tags,
                },
                api_path_create_params.APIPathCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapAPIPath,
        )

    def update(
        self,
        path_id: str,
        *,
        domain_id: int,
        api_groups: SequenceNotStr[str] | Omit = omit,
        path: str | Omit = omit,
        status: Literal["CONFIRMED_API", "POTENTIAL_API", "NOT_API", "DELISTED_API"] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Update a specific API path for a domain

        Args:
          domain_id: The domain ID

          path_id: The path ID

          path: The updated API path. When updating the path, variables can be renamed, path
              parts can be converted to variables and vice versa.

          status: The different statuses an API path can have

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            f"/waap/v1/domains/{domain_id}/api-paths/{path_id}",
            body=maybe_transform(
                {
                    "api_groups": api_groups,
                    "path": path,
                    "status": status,
                    "tags": tags,
                },
                api_path_update_params.APIPathUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        domain_id: int,
        *,
        api_group: Optional[str] | Omit = omit,
        api_version: Optional[str] | Omit = omit,
        http_scheme: Optional[Literal["HTTP", "HTTPS"]] | Omit = omit,
        ids: Optional[SequenceNotStr[str]] | Omit = omit,
        limit: int | Omit = omit,
        method: Optional[Literal["GET", "POST", "PUT", "PATCH", "DELETE", "TRACE", "HEAD", "OPTIONS"]] | Omit = omit,
        offset: int | Omit = omit,
        ordering: Literal[
            "id",
            "path",
            "method",
            "api_version",
            "http_scheme",
            "first_detected",
            "last_detected",
            "status",
            "source",
            "-id",
            "-path",
            "-method",
            "-api_version",
            "-http_scheme",
            "-first_detected",
            "-last_detected",
            "-status",
            "-source",
        ]
        | Omit = omit,
        path: Optional[str] | Omit = omit,
        source: Optional[Literal["API_DESCRIPTION_FILE", "TRAFFIC_SCAN", "USER_DEFINED"]] | Omit = omit,
        status: Optional[List[Literal["CONFIRMED_API", "POTENTIAL_API", "NOT_API", "DELISTED_API"]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[WaapAPIPath]:
        """
        Retrieve a list of API paths for a specific domain

        Args:
          domain_id: The domain ID

          api_group: Filter by the API group associated with the API path

          api_version: Filter by the API version

          http_scheme: The different HTTP schemes an API path can have

          ids: Filter by the path ID

          limit: Number of items to return

          method: The different methods an API path can have

          offset: Number of items to skip

          ordering: Sort the response by given field.

          path: Filter by the path. Supports '\\**' as a wildcard character

          source: The different sources an API path can have

          status: Filter by the status of the discovered API path

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            f"/waap/v1/domains/{domain_id}/api-paths",
            page=SyncOffsetPage[WaapAPIPath],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "api_group": api_group,
                        "api_version": api_version,
                        "http_scheme": http_scheme,
                        "ids": ids,
                        "limit": limit,
                        "method": method,
                        "offset": offset,
                        "ordering": ordering,
                        "path": path,
                        "source": source,
                        "status": status,
                    },
                    api_path_list_params.APIPathListParams,
                ),
            ),
            model=WaapAPIPath,
        )

    def delete(
        self,
        path_id: str,
        *,
        domain_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a specific API path for a domain

        Args:
          domain_id: The domain ID

          path_id: The path ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/waap/v1/domains/{domain_id}/api-paths/{path_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        path_id: str,
        *,
        domain_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapAPIPath:
        """
        Retrieve a specific API path for a domain

        Args:
          domain_id: The domain ID

          path_id: The path ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        return self._get(
            f"/waap/v1/domains/{domain_id}/api-paths/{path_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapAPIPath,
        )


class AsyncAPIPathsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAPIPathsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAPIPathsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAPIPathsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncAPIPathsResourceWithStreamingResponse(self)

    async def create(
        self,
        domain_id: int,
        *,
        http_scheme: Literal["HTTP", "HTTPS"],
        method: Literal["GET", "POST", "PUT", "PATCH", "DELETE", "TRACE", "HEAD", "OPTIONS"],
        path: str,
        api_groups: SequenceNotStr[str] | Omit = omit,
        api_version: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapAPIPath:
        """
        Create an API path for a domain

        Args:
          domain_id: The domain ID

          http_scheme: The different HTTP schemes an API path can have

          method: The different methods an API path can have

          path: The API path, locations that are saved for resource IDs will be put in curly
              brackets

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/waap/v1/domains/{domain_id}/api-paths",
            body=await async_maybe_transform(
                {
                    "http_scheme": http_scheme,
                    "method": method,
                    "path": path,
                    "api_groups": api_groups,
                    "api_version": api_version,
                    "tags": tags,
                },
                api_path_create_params.APIPathCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapAPIPath,
        )

    async def update(
        self,
        path_id: str,
        *,
        domain_id: int,
        api_groups: SequenceNotStr[str] | Omit = omit,
        path: str | Omit = omit,
        status: Literal["CONFIRMED_API", "POTENTIAL_API", "NOT_API", "DELISTED_API"] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Update a specific API path for a domain

        Args:
          domain_id: The domain ID

          path_id: The path ID

          path: The updated API path. When updating the path, variables can be renamed, path
              parts can be converted to variables and vice versa.

          status: The different statuses an API path can have

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            f"/waap/v1/domains/{domain_id}/api-paths/{path_id}",
            body=await async_maybe_transform(
                {
                    "api_groups": api_groups,
                    "path": path,
                    "status": status,
                    "tags": tags,
                },
                api_path_update_params.APIPathUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        domain_id: int,
        *,
        api_group: Optional[str] | Omit = omit,
        api_version: Optional[str] | Omit = omit,
        http_scheme: Optional[Literal["HTTP", "HTTPS"]] | Omit = omit,
        ids: Optional[SequenceNotStr[str]] | Omit = omit,
        limit: int | Omit = omit,
        method: Optional[Literal["GET", "POST", "PUT", "PATCH", "DELETE", "TRACE", "HEAD", "OPTIONS"]] | Omit = omit,
        offset: int | Omit = omit,
        ordering: Literal[
            "id",
            "path",
            "method",
            "api_version",
            "http_scheme",
            "first_detected",
            "last_detected",
            "status",
            "source",
            "-id",
            "-path",
            "-method",
            "-api_version",
            "-http_scheme",
            "-first_detected",
            "-last_detected",
            "-status",
            "-source",
        ]
        | Omit = omit,
        path: Optional[str] | Omit = omit,
        source: Optional[Literal["API_DESCRIPTION_FILE", "TRAFFIC_SCAN", "USER_DEFINED"]] | Omit = omit,
        status: Optional[List[Literal["CONFIRMED_API", "POTENTIAL_API", "NOT_API", "DELISTED_API"]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[WaapAPIPath, AsyncOffsetPage[WaapAPIPath]]:
        """
        Retrieve a list of API paths for a specific domain

        Args:
          domain_id: The domain ID

          api_group: Filter by the API group associated with the API path

          api_version: Filter by the API version

          http_scheme: The different HTTP schemes an API path can have

          ids: Filter by the path ID

          limit: Number of items to return

          method: The different methods an API path can have

          offset: Number of items to skip

          ordering: Sort the response by given field.

          path: Filter by the path. Supports '\\**' as a wildcard character

          source: The different sources an API path can have

          status: Filter by the status of the discovered API path

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            f"/waap/v1/domains/{domain_id}/api-paths",
            page=AsyncOffsetPage[WaapAPIPath],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "api_group": api_group,
                        "api_version": api_version,
                        "http_scheme": http_scheme,
                        "ids": ids,
                        "limit": limit,
                        "method": method,
                        "offset": offset,
                        "ordering": ordering,
                        "path": path,
                        "source": source,
                        "status": status,
                    },
                    api_path_list_params.APIPathListParams,
                ),
            ),
            model=WaapAPIPath,
        )

    async def delete(
        self,
        path_id: str,
        *,
        domain_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a specific API path for a domain

        Args:
          domain_id: The domain ID

          path_id: The path ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/waap/v1/domains/{domain_id}/api-paths/{path_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        path_id: str,
        *,
        domain_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WaapAPIPath:
        """
        Retrieve a specific API path for a domain

        Args:
          domain_id: The domain ID

          path_id: The path ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        return await self._get(
            f"/waap/v1/domains/{domain_id}/api-paths/{path_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapAPIPath,
        )


class APIPathsResourceWithRawResponse:
    def __init__(self, api_paths: APIPathsResource) -> None:
        self._api_paths = api_paths

        self.create = to_raw_response_wrapper(
            api_paths.create,
        )
        self.update = to_raw_response_wrapper(
            api_paths.update,
        )
        self.list = to_raw_response_wrapper(
            api_paths.list,
        )
        self.delete = to_raw_response_wrapper(
            api_paths.delete,
        )
        self.get = to_raw_response_wrapper(
            api_paths.get,
        )


class AsyncAPIPathsResourceWithRawResponse:
    def __init__(self, api_paths: AsyncAPIPathsResource) -> None:
        self._api_paths = api_paths

        self.create = async_to_raw_response_wrapper(
            api_paths.create,
        )
        self.update = async_to_raw_response_wrapper(
            api_paths.update,
        )
        self.list = async_to_raw_response_wrapper(
            api_paths.list,
        )
        self.delete = async_to_raw_response_wrapper(
            api_paths.delete,
        )
        self.get = async_to_raw_response_wrapper(
            api_paths.get,
        )


class APIPathsResourceWithStreamingResponse:
    def __init__(self, api_paths: APIPathsResource) -> None:
        self._api_paths = api_paths

        self.create = to_streamed_response_wrapper(
            api_paths.create,
        )
        self.update = to_streamed_response_wrapper(
            api_paths.update,
        )
        self.list = to_streamed_response_wrapper(
            api_paths.list,
        )
        self.delete = to_streamed_response_wrapper(
            api_paths.delete,
        )
        self.get = to_streamed_response_wrapper(
            api_paths.get,
        )


class AsyncAPIPathsResourceWithStreamingResponse:
    def __init__(self, api_paths: AsyncAPIPathsResource) -> None:
        self._api_paths = api_paths

        self.create = async_to_streamed_response_wrapper(
            api_paths.create,
        )
        self.update = async_to_streamed_response_wrapper(
            api_paths.update,
        )
        self.list = async_to_streamed_response_wrapper(
            api_paths.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            api_paths.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            api_paths.get,
        )
