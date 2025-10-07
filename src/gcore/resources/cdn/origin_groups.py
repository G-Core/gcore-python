# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Iterable, cast
from typing_extensions import overload

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import required_args, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.cdn import (
    origin_group_list_params,
    origin_group_create_params,
    origin_group_update_params,
    origin_group_replace_params,
)
from ..._base_client import make_request_options
from ...types.cdn.origin_groups import OriginGroups
from ...types.cdn.origin_groups_list import OriginGroupsList

__all__ = ["OriginGroupsResource", "AsyncOriginGroupsResource"]


class OriginGroupsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OriginGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return OriginGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OriginGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return OriginGroupsResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        name: str,
        sources: Iterable[origin_group_create_params.NoneAuthSource],
        auth_type: str | Omit = omit,
        proxy_next_upstream: SequenceNotStr[str] | Omit = omit,
        use_next: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginGroups:
        """
        Create an origin group with one or more origin sources.

        Args:
          name: Origin group name.

          sources: List of origin sources in the origin group.

          auth_type: Origin authentication type.

              Possible values:

              - **none** - Used for public origins.
              - **awsSignatureV4** - Used for S3 storage.

          proxy_next_upstream: Defines cases when the request should be passed on to the next origin.

              Possible values:

              - **error** - an error occurred while establishing a connection with the origin,
                passing a request to it, or reading the response header
              - **timeout** - a timeout has occurred while establishing a connection with the
                origin, passing a request to it, or reading the response header
              - **`invalid_header`** - a origin returned an empty or invalid response
              - **`http_403`** - a origin returned a response with the code 403
              - **`http_404`** - a origin returned a response with the code 404
              - **`http_429`** - a origin returned a response with the code 429
              - **`http_500`** - a origin returned a response with the code 500
              - **`http_502`** - a origin returned a response with the code 502
              - **`http_503`** - a origin returned a response with the code 503
              - **`http_504`** - a origin returned a response with the code 504

          use_next: Defines whether to use the next origin from the origin group if origin responds
              with the cases specified in `proxy_next_upstream`. If you enable it, you must
              specify cases in `proxy_next_upstream`.

              Possible values:

              - **true** - Option is enabled.
              - **false** - Option is disabled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        auth: origin_group_create_params.AwsSignatureV4Auth,
        auth_type: str,
        name: str,
        proxy_next_upstream: SequenceNotStr[str] | Omit = omit,
        use_next: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginGroups:
        """
        Create an origin group with one or more origin sources.

        Args:
          auth: Credentials to access the private bucket.

          auth_type: Authentication type.

              **awsSignatureV4** value is used for S3 storage.

          name: Origin group name.

          proxy_next_upstream: Defines cases when the request should be passed on to the next origin.

              Possible values:

              - **error** - an error occurred while establishing a connection with the origin,
                passing a request to it, or reading the response header
              - **timeout** - a timeout has occurred while establishing a connection with the
                origin, passing a request to it, or reading the response header
              - **`invalid_header`** - a origin returned an empty or invalid response
              - **`http_403`** - a origin returned a response with the code 403
              - **`http_404`** - a origin returned a response with the code 404
              - **`http_429`** - a origin returned a response with the code 429
              - **`http_500`** - a origin returned a response with the code 500
              - **`http_502`** - a origin returned a response with the code 502
              - **`http_503`** - a origin returned a response with the code 503
              - **`http_504`** - a origin returned a response with the code 504

          use_next: Defines whether to use the next origin from the origin group if origin responds
              with the cases specified in `proxy_next_upstream`. If you enable it, you must
              specify cases in `proxy_next_upstream`.

              Possible values:

              - **true** - Option is enabled.
              - **false** - Option is disabled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["name", "sources"], ["auth", "auth_type", "name"])
    def create(
        self,
        *,
        name: str,
        sources: Iterable[origin_group_create_params.NoneAuthSource] | Omit = omit,
        auth_type: str | Omit = omit,
        proxy_next_upstream: SequenceNotStr[str] | Omit = omit,
        use_next: bool | Omit = omit,
        auth: origin_group_create_params.AwsSignatureV4Auth | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginGroups:
        return cast(
            OriginGroups,
            self._post(
                "/cdn/origin_groups",
                body=maybe_transform(
                    {
                        "name": name,
                        "sources": sources,
                        "auth_type": auth_type,
                        "proxy_next_upstream": proxy_next_upstream,
                        "use_next": use_next,
                        "auth": auth,
                    },
                    origin_group_create_params.OriginGroupCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, OriginGroups),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @overload
    def update(
        self,
        origin_group_id: int,
        *,
        name: str,
        auth_type: str | Omit = omit,
        path: str | Omit = omit,
        proxy_next_upstream: SequenceNotStr[str] | Omit = omit,
        sources: Iterable[origin_group_update_params.NoneAuthSource] | Omit = omit,
        use_next: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginGroups:
        """
        Change origin group

        Args:
          name: Origin group name.

          auth_type: Origin authentication type.

              Possible values:

              - **none** - Used for public origins.
              - **awsSignatureV4** - Used for S3 storage.

          path: Parameter is **deprecated**.

          proxy_next_upstream: Defines cases when the request should be passed on to the next origin.

              Possible values:

              - **error** - an error occurred while establishing a connection with the origin,
                passing a request to it, or reading the response header
              - **timeout** - a timeout has occurred while establishing a connection with the
                origin, passing a request to it, or reading the response header
              - **`invalid_header`** - a origin returned an empty or invalid response
              - **`http_403`** - a origin returned a response with the code 403
              - **`http_404`** - a origin returned a response with the code 404
              - **`http_429`** - a origin returned a response with the code 429
              - **`http_500`** - a origin returned a response with the code 500
              - **`http_502`** - a origin returned a response with the code 502
              - **`http_503`** - a origin returned a response with the code 503
              - **`http_504`** - a origin returned a response with the code 504

          sources: List of origin sources in the origin group.

          use_next: Defines whether to use the next origin from the origin group if origin responds
              with the cases specified in `proxy_next_upstream`. If you enable it, you must
              specify cases in `proxy_next_upstream`.

              Possible values:

              - **true** - Option is enabled.
              - **false** - Option is disabled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        origin_group_id: int,
        *,
        auth: origin_group_update_params.AwsSignatureV4Auth | Omit = omit,
        auth_type: str | Omit = omit,
        name: str | Omit = omit,
        path: str | Omit = omit,
        proxy_next_upstream: SequenceNotStr[str] | Omit = omit,
        use_next: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginGroups:
        """
        Change origin group

        Args:
          auth: Credentials to access the private bucket.

          auth_type: Authentication type.

              **awsSignatureV4** value is used for S3 storage.

          name: Origin group name.

          path: Parameter is **deprecated**.

          proxy_next_upstream: Defines cases when the request should be passed on to the next origin.

              Possible values:

              - **error** - an error occurred while establishing a connection with the origin,
                passing a request to it, or reading the response header
              - **timeout** - a timeout has occurred while establishing a connection with the
                origin, passing a request to it, or reading the response header
              - **`invalid_header`** - a origin returned an empty or invalid response
              - **`http_403`** - a origin returned a response with the code 403
              - **`http_404`** - a origin returned a response with the code 404
              - **`http_429`** - a origin returned a response with the code 429
              - **`http_500`** - a origin returned a response with the code 500
              - **`http_502`** - a origin returned a response with the code 502
              - **`http_503`** - a origin returned a response with the code 503
              - **`http_504`** - a origin returned a response with the code 504

          use_next: Defines whether to use the next origin from the origin group if origin responds
              with the cases specified in `proxy_next_upstream`. If you enable it, you must
              specify cases in `proxy_next_upstream`.

              Possible values:

              - **true** - Option is enabled.
              - **false** - Option is disabled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    def update(
        self,
        origin_group_id: int,
        *,
        name: str | Omit = omit,
        auth_type: str | Omit = omit,
        path: str | Omit = omit,
        proxy_next_upstream: SequenceNotStr[str] | Omit = omit,
        sources: Iterable[origin_group_update_params.NoneAuthSource] | Omit = omit,
        use_next: bool | Omit = omit,
        auth: origin_group_update_params.AwsSignatureV4Auth | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginGroups:
        return cast(
            OriginGroups,
            self._patch(
                f"/cdn/origin_groups/{origin_group_id}",
                body=maybe_transform(
                    {
                        "name": name,
                        "auth_type": auth_type,
                        "path": path,
                        "proxy_next_upstream": proxy_next_upstream,
                        "sources": sources,
                        "use_next": use_next,
                        "auth": auth,
                    },
                    origin_group_update_params.OriginGroupUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, OriginGroups),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        has_related_resources: bool | Omit = omit,
        name: str | Omit = omit,
        sources: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginGroupsList:
        """
        Get all origin groups and related origin sources.

        Args:
          has_related_resources: Defines whether the origin group has related CDN resources.

              Possible values:

              - **true** – Origin group has related CDN resources.
              - **false** – Origin group does not have related CDN resources.

          name: Origin group name.

          sources: Origin sources (IP addresses or domains) in the origin group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/cdn/origin_groups",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "has_related_resources": has_related_resources,
                        "name": name,
                        "sources": sources,
                    },
                    origin_group_list_params.OriginGroupListParams,
                ),
            ),
            cast_to=OriginGroupsList,
        )

    def delete(
        self,
        origin_group_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete origin group

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/cdn/origin_groups/{origin_group_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        origin_group_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginGroups:
        """
        Get origin group details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            OriginGroups,
            self._get(
                f"/cdn/origin_groups/{origin_group_id}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, OriginGroups),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @overload
    def replace(
        self,
        origin_group_id: int,
        *,
        auth_type: str,
        name: str,
        path: str,
        sources: Iterable[origin_group_replace_params.NoneAuthSource],
        use_next: bool,
        proxy_next_upstream: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginGroups:
        """
        Change origin group

        Args:
          auth_type: Origin authentication type.

              Possible values:

              - **none** - Used for public origins.
              - **awsSignatureV4** - Used for S3 storage.

          name: Origin group name.

          path: Parameter is **deprecated**.

          sources: List of origin sources in the origin group.

          use_next: Defines whether to use the next origin from the origin group if origin responds
              with the cases specified in `proxy_next_upstream`. If you enable it, you must
              specify cases in `proxy_next_upstream`.

              Possible values:

              - **true** - Option is enabled.
              - **false** - Option is disabled.

          proxy_next_upstream: Defines cases when the request should be passed on to the next origin.

              Possible values:

              - **error** - an error occurred while establishing a connection with the origin,
                passing a request to it, or reading the response header
              - **timeout** - a timeout has occurred while establishing a connection with the
                origin, passing a request to it, or reading the response header
              - **`invalid_header`** - a origin returned an empty or invalid response
              - **`http_403`** - a origin returned a response with the code 403
              - **`http_404`** - a origin returned a response with the code 404
              - **`http_429`** - a origin returned a response with the code 429
              - **`http_500`** - a origin returned a response with the code 500
              - **`http_502`** - a origin returned a response with the code 502
              - **`http_503`** - a origin returned a response with the code 503
              - **`http_504`** - a origin returned a response with the code 504

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def replace(
        self,
        origin_group_id: int,
        *,
        auth: origin_group_replace_params.AwsSignatureV4Auth,
        auth_type: str,
        name: str,
        path: str,
        use_next: bool,
        proxy_next_upstream: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginGroups:
        """
        Change origin group

        Args:
          auth: Credentials to access the private bucket.

          auth_type: Authentication type.

              **awsSignatureV4** value is used for S3 storage.

          name: Origin group name.

          path: Parameter is **deprecated**.

          use_next: Defines whether to use the next origin from the origin group if origin responds
              with the cases specified in `proxy_next_upstream`. If you enable it, you must
              specify cases in `proxy_next_upstream`.

              Possible values:

              - **true** - Option is enabled.
              - **false** - Option is disabled.

          proxy_next_upstream: Defines cases when the request should be passed on to the next origin.

              Possible values:

              - **error** - an error occurred while establishing a connection with the origin,
                passing a request to it, or reading the response header
              - **timeout** - a timeout has occurred while establishing a connection with the
                origin, passing a request to it, or reading the response header
              - **`invalid_header`** - a origin returned an empty or invalid response
              - **`http_403`** - a origin returned a response with the code 403
              - **`http_404`** - a origin returned a response with the code 404
              - **`http_429`** - a origin returned a response with the code 429
              - **`http_500`** - a origin returned a response with the code 500
              - **`http_502`** - a origin returned a response with the code 502
              - **`http_503`** - a origin returned a response with the code 503
              - **`http_504`** - a origin returned a response with the code 504

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["auth_type", "name", "path", "sources", "use_next"], ["auth", "auth_type", "name", "path", "use_next"]
    )
    def replace(
        self,
        origin_group_id: int,
        *,
        auth_type: str,
        name: str,
        path: str,
        sources: Iterable[origin_group_replace_params.NoneAuthSource] | Omit = omit,
        use_next: bool,
        proxy_next_upstream: SequenceNotStr[str] | Omit = omit,
        auth: origin_group_replace_params.AwsSignatureV4Auth | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginGroups:
        return cast(
            OriginGroups,
            self._put(
                f"/cdn/origin_groups/{origin_group_id}",
                body=maybe_transform(
                    {
                        "auth_type": auth_type,
                        "name": name,
                        "path": path,
                        "sources": sources,
                        "use_next": use_next,
                        "proxy_next_upstream": proxy_next_upstream,
                        "auth": auth,
                    },
                    origin_group_replace_params.OriginGroupReplaceParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, OriginGroups),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncOriginGroupsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOriginGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOriginGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOriginGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncOriginGroupsResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        name: str,
        sources: Iterable[origin_group_create_params.NoneAuthSource],
        auth_type: str | Omit = omit,
        proxy_next_upstream: SequenceNotStr[str] | Omit = omit,
        use_next: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginGroups:
        """
        Create an origin group with one or more origin sources.

        Args:
          name: Origin group name.

          sources: List of origin sources in the origin group.

          auth_type: Origin authentication type.

              Possible values:

              - **none** - Used for public origins.
              - **awsSignatureV4** - Used for S3 storage.

          proxy_next_upstream: Defines cases when the request should be passed on to the next origin.

              Possible values:

              - **error** - an error occurred while establishing a connection with the origin,
                passing a request to it, or reading the response header
              - **timeout** - a timeout has occurred while establishing a connection with the
                origin, passing a request to it, or reading the response header
              - **`invalid_header`** - a origin returned an empty or invalid response
              - **`http_403`** - a origin returned a response with the code 403
              - **`http_404`** - a origin returned a response with the code 404
              - **`http_429`** - a origin returned a response with the code 429
              - **`http_500`** - a origin returned a response with the code 500
              - **`http_502`** - a origin returned a response with the code 502
              - **`http_503`** - a origin returned a response with the code 503
              - **`http_504`** - a origin returned a response with the code 504

          use_next: Defines whether to use the next origin from the origin group if origin responds
              with the cases specified in `proxy_next_upstream`. If you enable it, you must
              specify cases in `proxy_next_upstream`.

              Possible values:

              - **true** - Option is enabled.
              - **false** - Option is disabled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        auth: origin_group_create_params.AwsSignatureV4Auth,
        auth_type: str,
        name: str,
        proxy_next_upstream: SequenceNotStr[str] | Omit = omit,
        use_next: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginGroups:
        """
        Create an origin group with one or more origin sources.

        Args:
          auth: Credentials to access the private bucket.

          auth_type: Authentication type.

              **awsSignatureV4** value is used for S3 storage.

          name: Origin group name.

          proxy_next_upstream: Defines cases when the request should be passed on to the next origin.

              Possible values:

              - **error** - an error occurred while establishing a connection with the origin,
                passing a request to it, or reading the response header
              - **timeout** - a timeout has occurred while establishing a connection with the
                origin, passing a request to it, or reading the response header
              - **`invalid_header`** - a origin returned an empty or invalid response
              - **`http_403`** - a origin returned a response with the code 403
              - **`http_404`** - a origin returned a response with the code 404
              - **`http_429`** - a origin returned a response with the code 429
              - **`http_500`** - a origin returned a response with the code 500
              - **`http_502`** - a origin returned a response with the code 502
              - **`http_503`** - a origin returned a response with the code 503
              - **`http_504`** - a origin returned a response with the code 504

          use_next: Defines whether to use the next origin from the origin group if origin responds
              with the cases specified in `proxy_next_upstream`. If you enable it, you must
              specify cases in `proxy_next_upstream`.

              Possible values:

              - **true** - Option is enabled.
              - **false** - Option is disabled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["name", "sources"], ["auth", "auth_type", "name"])
    async def create(
        self,
        *,
        name: str,
        sources: Iterable[origin_group_create_params.NoneAuthSource] | Omit = omit,
        auth_type: str | Omit = omit,
        proxy_next_upstream: SequenceNotStr[str] | Omit = omit,
        use_next: bool | Omit = omit,
        auth: origin_group_create_params.AwsSignatureV4Auth | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginGroups:
        return cast(
            OriginGroups,
            await self._post(
                "/cdn/origin_groups",
                body=await async_maybe_transform(
                    {
                        "name": name,
                        "sources": sources,
                        "auth_type": auth_type,
                        "proxy_next_upstream": proxy_next_upstream,
                        "use_next": use_next,
                        "auth": auth,
                    },
                    origin_group_create_params.OriginGroupCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, OriginGroups),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @overload
    async def update(
        self,
        origin_group_id: int,
        *,
        name: str,
        auth_type: str | Omit = omit,
        path: str | Omit = omit,
        proxy_next_upstream: SequenceNotStr[str] | Omit = omit,
        sources: Iterable[origin_group_update_params.NoneAuthSource] | Omit = omit,
        use_next: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginGroups:
        """
        Change origin group

        Args:
          name: Origin group name.

          auth_type: Origin authentication type.

              Possible values:

              - **none** - Used for public origins.
              - **awsSignatureV4** - Used for S3 storage.

          path: Parameter is **deprecated**.

          proxy_next_upstream: Defines cases when the request should be passed on to the next origin.

              Possible values:

              - **error** - an error occurred while establishing a connection with the origin,
                passing a request to it, or reading the response header
              - **timeout** - a timeout has occurred while establishing a connection with the
                origin, passing a request to it, or reading the response header
              - **`invalid_header`** - a origin returned an empty or invalid response
              - **`http_403`** - a origin returned a response with the code 403
              - **`http_404`** - a origin returned a response with the code 404
              - **`http_429`** - a origin returned a response with the code 429
              - **`http_500`** - a origin returned a response with the code 500
              - **`http_502`** - a origin returned a response with the code 502
              - **`http_503`** - a origin returned a response with the code 503
              - **`http_504`** - a origin returned a response with the code 504

          sources: List of origin sources in the origin group.

          use_next: Defines whether to use the next origin from the origin group if origin responds
              with the cases specified in `proxy_next_upstream`. If you enable it, you must
              specify cases in `proxy_next_upstream`.

              Possible values:

              - **true** - Option is enabled.
              - **false** - Option is disabled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        origin_group_id: int,
        *,
        auth: origin_group_update_params.AwsSignatureV4Auth | Omit = omit,
        auth_type: str | Omit = omit,
        name: str | Omit = omit,
        path: str | Omit = omit,
        proxy_next_upstream: SequenceNotStr[str] | Omit = omit,
        use_next: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginGroups:
        """
        Change origin group

        Args:
          auth: Credentials to access the private bucket.

          auth_type: Authentication type.

              **awsSignatureV4** value is used for S3 storage.

          name: Origin group name.

          path: Parameter is **deprecated**.

          proxy_next_upstream: Defines cases when the request should be passed on to the next origin.

              Possible values:

              - **error** - an error occurred while establishing a connection with the origin,
                passing a request to it, or reading the response header
              - **timeout** - a timeout has occurred while establishing a connection with the
                origin, passing a request to it, or reading the response header
              - **`invalid_header`** - a origin returned an empty or invalid response
              - **`http_403`** - a origin returned a response with the code 403
              - **`http_404`** - a origin returned a response with the code 404
              - **`http_429`** - a origin returned a response with the code 429
              - **`http_500`** - a origin returned a response with the code 500
              - **`http_502`** - a origin returned a response with the code 502
              - **`http_503`** - a origin returned a response with the code 503
              - **`http_504`** - a origin returned a response with the code 504

          use_next: Defines whether to use the next origin from the origin group if origin responds
              with the cases specified in `proxy_next_upstream`. If you enable it, you must
              specify cases in `proxy_next_upstream`.

              Possible values:

              - **true** - Option is enabled.
              - **false** - Option is disabled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    async def update(
        self,
        origin_group_id: int,
        *,
        name: str | Omit = omit,
        auth_type: str | Omit = omit,
        path: str | Omit = omit,
        proxy_next_upstream: SequenceNotStr[str] | Omit = omit,
        sources: Iterable[origin_group_update_params.NoneAuthSource] | Omit = omit,
        use_next: bool | Omit = omit,
        auth: origin_group_update_params.AwsSignatureV4Auth | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginGroups:
        return cast(
            OriginGroups,
            await self._patch(
                f"/cdn/origin_groups/{origin_group_id}",
                body=await async_maybe_transform(
                    {
                        "name": name,
                        "auth_type": auth_type,
                        "path": path,
                        "proxy_next_upstream": proxy_next_upstream,
                        "sources": sources,
                        "use_next": use_next,
                        "auth": auth,
                    },
                    origin_group_update_params.OriginGroupUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, OriginGroups),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def list(
        self,
        *,
        has_related_resources: bool | Omit = omit,
        name: str | Omit = omit,
        sources: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginGroupsList:
        """
        Get all origin groups and related origin sources.

        Args:
          has_related_resources: Defines whether the origin group has related CDN resources.

              Possible values:

              - **true** – Origin group has related CDN resources.
              - **false** – Origin group does not have related CDN resources.

          name: Origin group name.

          sources: Origin sources (IP addresses or domains) in the origin group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/cdn/origin_groups",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "has_related_resources": has_related_resources,
                        "name": name,
                        "sources": sources,
                    },
                    origin_group_list_params.OriginGroupListParams,
                ),
            ),
            cast_to=OriginGroupsList,
        )

    async def delete(
        self,
        origin_group_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete origin group

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/cdn/origin_groups/{origin_group_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        origin_group_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginGroups:
        """
        Get origin group details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            OriginGroups,
            await self._get(
                f"/cdn/origin_groups/{origin_group_id}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, OriginGroups),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @overload
    async def replace(
        self,
        origin_group_id: int,
        *,
        auth_type: str,
        name: str,
        path: str,
        sources: Iterable[origin_group_replace_params.NoneAuthSource],
        use_next: bool,
        proxy_next_upstream: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginGroups:
        """
        Change origin group

        Args:
          auth_type: Origin authentication type.

              Possible values:

              - **none** - Used for public origins.
              - **awsSignatureV4** - Used for S3 storage.

          name: Origin group name.

          path: Parameter is **deprecated**.

          sources: List of origin sources in the origin group.

          use_next: Defines whether to use the next origin from the origin group if origin responds
              with the cases specified in `proxy_next_upstream`. If you enable it, you must
              specify cases in `proxy_next_upstream`.

              Possible values:

              - **true** - Option is enabled.
              - **false** - Option is disabled.

          proxy_next_upstream: Defines cases when the request should be passed on to the next origin.

              Possible values:

              - **error** - an error occurred while establishing a connection with the origin,
                passing a request to it, or reading the response header
              - **timeout** - a timeout has occurred while establishing a connection with the
                origin, passing a request to it, or reading the response header
              - **`invalid_header`** - a origin returned an empty or invalid response
              - **`http_403`** - a origin returned a response with the code 403
              - **`http_404`** - a origin returned a response with the code 404
              - **`http_429`** - a origin returned a response with the code 429
              - **`http_500`** - a origin returned a response with the code 500
              - **`http_502`** - a origin returned a response with the code 502
              - **`http_503`** - a origin returned a response with the code 503
              - **`http_504`** - a origin returned a response with the code 504

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def replace(
        self,
        origin_group_id: int,
        *,
        auth: origin_group_replace_params.AwsSignatureV4Auth,
        auth_type: str,
        name: str,
        path: str,
        use_next: bool,
        proxy_next_upstream: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginGroups:
        """
        Change origin group

        Args:
          auth: Credentials to access the private bucket.

          auth_type: Authentication type.

              **awsSignatureV4** value is used for S3 storage.

          name: Origin group name.

          path: Parameter is **deprecated**.

          use_next: Defines whether to use the next origin from the origin group if origin responds
              with the cases specified in `proxy_next_upstream`. If you enable it, you must
              specify cases in `proxy_next_upstream`.

              Possible values:

              - **true** - Option is enabled.
              - **false** - Option is disabled.

          proxy_next_upstream: Defines cases when the request should be passed on to the next origin.

              Possible values:

              - **error** - an error occurred while establishing a connection with the origin,
                passing a request to it, or reading the response header
              - **timeout** - a timeout has occurred while establishing a connection with the
                origin, passing a request to it, or reading the response header
              - **`invalid_header`** - a origin returned an empty or invalid response
              - **`http_403`** - a origin returned a response with the code 403
              - **`http_404`** - a origin returned a response with the code 404
              - **`http_429`** - a origin returned a response with the code 429
              - **`http_500`** - a origin returned a response with the code 500
              - **`http_502`** - a origin returned a response with the code 502
              - **`http_503`** - a origin returned a response with the code 503
              - **`http_504`** - a origin returned a response with the code 504

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["auth_type", "name", "path", "sources", "use_next"], ["auth", "auth_type", "name", "path", "use_next"]
    )
    async def replace(
        self,
        origin_group_id: int,
        *,
        auth_type: str,
        name: str,
        path: str,
        sources: Iterable[origin_group_replace_params.NoneAuthSource] | Omit = omit,
        use_next: bool,
        proxy_next_upstream: SequenceNotStr[str] | Omit = omit,
        auth: origin_group_replace_params.AwsSignatureV4Auth | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginGroups:
        return cast(
            OriginGroups,
            await self._put(
                f"/cdn/origin_groups/{origin_group_id}",
                body=await async_maybe_transform(
                    {
                        "auth_type": auth_type,
                        "name": name,
                        "path": path,
                        "sources": sources,
                        "use_next": use_next,
                        "proxy_next_upstream": proxy_next_upstream,
                        "auth": auth,
                    },
                    origin_group_replace_params.OriginGroupReplaceParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, OriginGroups),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class OriginGroupsResourceWithRawResponse:
    def __init__(self, origin_groups: OriginGroupsResource) -> None:
        self._origin_groups = origin_groups

        self.create = to_raw_response_wrapper(
            origin_groups.create,
        )
        self.update = to_raw_response_wrapper(
            origin_groups.update,
        )
        self.list = to_raw_response_wrapper(
            origin_groups.list,
        )
        self.delete = to_raw_response_wrapper(
            origin_groups.delete,
        )
        self.get = to_raw_response_wrapper(
            origin_groups.get,
        )
        self.replace = to_raw_response_wrapper(
            origin_groups.replace,
        )


class AsyncOriginGroupsResourceWithRawResponse:
    def __init__(self, origin_groups: AsyncOriginGroupsResource) -> None:
        self._origin_groups = origin_groups

        self.create = async_to_raw_response_wrapper(
            origin_groups.create,
        )
        self.update = async_to_raw_response_wrapper(
            origin_groups.update,
        )
        self.list = async_to_raw_response_wrapper(
            origin_groups.list,
        )
        self.delete = async_to_raw_response_wrapper(
            origin_groups.delete,
        )
        self.get = async_to_raw_response_wrapper(
            origin_groups.get,
        )
        self.replace = async_to_raw_response_wrapper(
            origin_groups.replace,
        )


class OriginGroupsResourceWithStreamingResponse:
    def __init__(self, origin_groups: OriginGroupsResource) -> None:
        self._origin_groups = origin_groups

        self.create = to_streamed_response_wrapper(
            origin_groups.create,
        )
        self.update = to_streamed_response_wrapper(
            origin_groups.update,
        )
        self.list = to_streamed_response_wrapper(
            origin_groups.list,
        )
        self.delete = to_streamed_response_wrapper(
            origin_groups.delete,
        )
        self.get = to_streamed_response_wrapper(
            origin_groups.get,
        )
        self.replace = to_streamed_response_wrapper(
            origin_groups.replace,
        )


class AsyncOriginGroupsResourceWithStreamingResponse:
    def __init__(self, origin_groups: AsyncOriginGroupsResource) -> None:
        self._origin_groups = origin_groups

        self.create = async_to_streamed_response_wrapper(
            origin_groups.create,
        )
        self.update = async_to_streamed_response_wrapper(
            origin_groups.update,
        )
        self.list = async_to_streamed_response_wrapper(
            origin_groups.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            origin_groups.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            origin_groups.get,
        )
        self.replace = async_to_streamed_response_wrapper(
            origin_groups.replace,
        )
