# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .users import (
    UsersResource,
    AsyncUsersResource,
    UsersResourceWithRawResponse,
    AsyncUsersResourceWithRawResponse,
    UsersResourceWithStreamingResponse,
    AsyncUsersResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from .api_tokens import (
    APITokensResource,
    AsyncAPITokensResource,
    APITokensResourceWithRawResponse,
    AsyncAPITokensResourceWithRawResponse,
    APITokensResourceWithStreamingResponse,
    AsyncAPITokensResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.iam.account_overview import AccountOverview

__all__ = ["IamResource", "AsyncIamResource"]


class IamResource(SyncAPIResource):
    @cached_property
    def api_tokens(self) -> APITokensResource:
        return APITokensResource(self._client)

    @cached_property
    def users(self) -> UsersResource:
        return UsersResource(self._client)

    @cached_property
    def with_raw_response(self) -> IamResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return IamResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IamResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return IamResourceWithStreamingResponse(self)

    def get_account_overview(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountOverview:
        """Get information about your profile, users and other account details."""
        return self._get(
            "/iam/clients/me",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountOverview,
        )


class AsyncIamResource(AsyncAPIResource):
    @cached_property
    def api_tokens(self) -> AsyncAPITokensResource:
        return AsyncAPITokensResource(self._client)

    @cached_property
    def users(self) -> AsyncUsersResource:
        return AsyncUsersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncIamResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIamResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIamResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncIamResourceWithStreamingResponse(self)

    async def get_account_overview(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountOverview:
        """Get information about your profile, users and other account details."""
        return await self._get(
            "/iam/clients/me",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountOverview,
        )


class IamResourceWithRawResponse:
    def __init__(self, iam: IamResource) -> None:
        self._iam = iam

        self.get_account_overview = to_raw_response_wrapper(
            iam.get_account_overview,
        )

    @cached_property
    def api_tokens(self) -> APITokensResourceWithRawResponse:
        return APITokensResourceWithRawResponse(self._iam.api_tokens)

    @cached_property
    def users(self) -> UsersResourceWithRawResponse:
        return UsersResourceWithRawResponse(self._iam.users)


class AsyncIamResourceWithRawResponse:
    def __init__(self, iam: AsyncIamResource) -> None:
        self._iam = iam

        self.get_account_overview = async_to_raw_response_wrapper(
            iam.get_account_overview,
        )

    @cached_property
    def api_tokens(self) -> AsyncAPITokensResourceWithRawResponse:
        return AsyncAPITokensResourceWithRawResponse(self._iam.api_tokens)

    @cached_property
    def users(self) -> AsyncUsersResourceWithRawResponse:
        return AsyncUsersResourceWithRawResponse(self._iam.users)


class IamResourceWithStreamingResponse:
    def __init__(self, iam: IamResource) -> None:
        self._iam = iam

        self.get_account_overview = to_streamed_response_wrapper(
            iam.get_account_overview,
        )

    @cached_property
    def api_tokens(self) -> APITokensResourceWithStreamingResponse:
        return APITokensResourceWithStreamingResponse(self._iam.api_tokens)

    @cached_property
    def users(self) -> UsersResourceWithStreamingResponse:
        return UsersResourceWithStreamingResponse(self._iam.users)


class AsyncIamResourceWithStreamingResponse:
    def __init__(self, iam: AsyncIamResource) -> None:
        self._iam = iam

        self.get_account_overview = async_to_streamed_response_wrapper(
            iam.get_account_overview,
        )

    @cached_property
    def api_tokens(self) -> AsyncAPITokensResourceWithStreamingResponse:
        return AsyncAPITokensResourceWithStreamingResponse(self._iam.api_tokens)

    @cached_property
    def users(self) -> AsyncUsersResourceWithStreamingResponse:
        return AsyncUsersResourceWithStreamingResponse(self._iam.users)
