# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.iam import api_token_list_params, api_token_create_params
from ..._base_client import make_request_options
from ...types.iam.api_token import APIToken
from ...types.iam.api_token_list import APITokenList
from ...types.iam.api_token_created import APITokenCreated

__all__ = ["APITokensResource", "AsyncAPITokensResource"]


class APITokensResource(SyncAPIResource):
    """
    Use permanent API tokens for regular automated requests to services.
    You can either set its validity period when creating it or issue a token for an unlimited time.
    Please address the API documentation of the specific product in order to check if it supports API tokens.

    Newer endpoints under `/v2/…` issue tokens using `_` (underscore) as the separator
    (for example `42_a1b2c3d4e5f6...`) and are the recommended way to create new tokens.
    Legacy endpoints that issue `$`-separated tokens are marked deprecated and will be removed
    on **2026-07-17**; tokens that were already issued keep authenticating.

    Provide your APIKey in the Authorization header.

    Example: ```curl -H "Authorization: APIKey 42_a1b2c3d4e5f6..." https://api.gcore.com/iam/users/me```

    Please note: When authorizing via SAML SSO, our system does not have any
    information about permissions given to the user by the identity provider.
    Even if the provider revokes the user's access rights, their tokens remain active.
    Therefore, if necessary, the token will need to be deleted manually.
    """

    @cached_property
    def with_raw_response(self) -> APITokensResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return APITokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> APITokensResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return APITokensResourceWithStreamingResponse(self)

    def create(
        self,
        client_id: int,
        *,
        client_user: api_token_create_params.ClientUser,
        exp_date: Optional[str],
        name: str,
        description: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APITokenCreated:
        """
        Create an API token in the current account.

        This V2 endpoint generates tokens that use `_` (underscore) as the separator
        between the token ID and the secret string, instead of the `$` separator used by
        the V1 endpoint. For example: `42_a1b2c3d4...`

        Tokens created via this endpoint are fully compatible with all existing
        authentication mechanisms.

        Args:
          client_user: API token role.

          exp_date: Date when the API token becomes expired (ISO 8086/RFC 3339 format), UTC. If
              null, then the API token will never expire.

          name: API token name.

          description: API token description.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            path_template("/iam/v2/clients/{client_id}/tokens", client_id=client_id),
            body=maybe_transform(
                {
                    "client_user": client_user,
                    "exp_date": exp_date,
                    "name": name,
                    "description": description,
                },
                api_token_create_params.APITokenCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APITokenCreated,
        )

    def list(
        self,
        client_id: int,
        *,
        deleted: bool | Omit = omit,
        issued_by: int | Omit = omit,
        not_issued_by: int | Omit = omit,
        role: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APITokenList:
        """Get information about your permanent API tokens in the account.

        A user with the
        Administrators role gets information about all API tokens in the account.

        This endpoint is identical to the V1 endpoint.

        Args:
          deleted: The state of API tokens included in the response.
               Two possible values:

              - True - API token was not deleted.\\** False - API token was deleted.

              Example, _&deleted=True_

          issued_by: User's ID. Use to get API tokens issued by a particular user.
               Example, _&`issued_by`=1234_

          not_issued_by: User's ID. Use to get API tokens issued by anyone except a particular user.
               Example, _¬_issued_by=1234_

          role:
              Group's ID. Possible values are:

              - 1 - Administrators* 2 - Users* 5 - Engineers* 3009 - Purge and Prefetch only
                (API+Web)* 3022 - Purge and Prefetch only (API)

              Example, _&role=Engineers_

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/iam/v2/clients/{client_id}/tokens", client_id=client_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "deleted": deleted,
                        "issued_by": issued_by,
                        "not_issued_by": not_issued_by,
                        "role": role,
                    },
                    api_token_list_params.APITokenListParams,
                ),
            ),
            cast_to=APITokenList,
        )

    def delete(
        self,
        token_id: int,
        *,
        client_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete API token from current account.

        Ensure that the API token is not being
        used by an active application. After deleting the token, all applications that
        use this token will not be able to get access to your account via API. The
        action cannot be reversed.

        This endpoint is identical to the V1 endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/iam/v2/clients/{client_id}/tokens/{token_id}", client_id=client_id, token_id=token_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        token_id: int,
        *,
        client_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIToken:
        """
        Get information about a specific API token.

        This endpoint is identical to the V1 endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/iam/v2/clients/{client_id}/tokens/{token_id}", client_id=client_id, token_id=token_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIToken,
        )


class AsyncAPITokensResource(AsyncAPIResource):
    """
    Use permanent API tokens for regular automated requests to services.
    You can either set its validity period when creating it or issue a token for an unlimited time.
    Please address the API documentation of the specific product in order to check if it supports API tokens.

    Newer endpoints under `/v2/…` issue tokens using `_` (underscore) as the separator
    (for example `42_a1b2c3d4e5f6...`) and are the recommended way to create new tokens.
    Legacy endpoints that issue `$`-separated tokens are marked deprecated and will be removed
    on **2026-07-17**; tokens that were already issued keep authenticating.

    Provide your APIKey in the Authorization header.

    Example: ```curl -H "Authorization: APIKey 42_a1b2c3d4e5f6..." https://api.gcore.com/iam/users/me```

    Please note: When authorizing via SAML SSO, our system does not have any
    information about permissions given to the user by the identity provider.
    Even if the provider revokes the user's access rights, their tokens remain active.
    Therefore, if necessary, the token will need to be deleted manually.
    """

    @cached_property
    def with_raw_response(self) -> AsyncAPITokensResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAPITokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAPITokensResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncAPITokensResourceWithStreamingResponse(self)

    async def create(
        self,
        client_id: int,
        *,
        client_user: api_token_create_params.ClientUser,
        exp_date: Optional[str],
        name: str,
        description: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APITokenCreated:
        """
        Create an API token in the current account.

        This V2 endpoint generates tokens that use `_` (underscore) as the separator
        between the token ID and the secret string, instead of the `$` separator used by
        the V1 endpoint. For example: `42_a1b2c3d4...`

        Tokens created via this endpoint are fully compatible with all existing
        authentication mechanisms.

        Args:
          client_user: API token role.

          exp_date: Date when the API token becomes expired (ISO 8086/RFC 3339 format), UTC. If
              null, then the API token will never expire.

          name: API token name.

          description: API token description.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            path_template("/iam/v2/clients/{client_id}/tokens", client_id=client_id),
            body=await async_maybe_transform(
                {
                    "client_user": client_user,
                    "exp_date": exp_date,
                    "name": name,
                    "description": description,
                },
                api_token_create_params.APITokenCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APITokenCreated,
        )

    async def list(
        self,
        client_id: int,
        *,
        deleted: bool | Omit = omit,
        issued_by: int | Omit = omit,
        not_issued_by: int | Omit = omit,
        role: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APITokenList:
        """Get information about your permanent API tokens in the account.

        A user with the
        Administrators role gets information about all API tokens in the account.

        This endpoint is identical to the V1 endpoint.

        Args:
          deleted: The state of API tokens included in the response.
               Two possible values:

              - True - API token was not deleted.\\** False - API token was deleted.

              Example, _&deleted=True_

          issued_by: User's ID. Use to get API tokens issued by a particular user.
               Example, _&`issued_by`=1234_

          not_issued_by: User's ID. Use to get API tokens issued by anyone except a particular user.
               Example, _¬_issued_by=1234_

          role:
              Group's ID. Possible values are:

              - 1 - Administrators* 2 - Users* 5 - Engineers* 3009 - Purge and Prefetch only
                (API+Web)* 3022 - Purge and Prefetch only (API)

              Example, _&role=Engineers_

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/iam/v2/clients/{client_id}/tokens", client_id=client_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "deleted": deleted,
                        "issued_by": issued_by,
                        "not_issued_by": not_issued_by,
                        "role": role,
                    },
                    api_token_list_params.APITokenListParams,
                ),
            ),
            cast_to=APITokenList,
        )

    async def delete(
        self,
        token_id: int,
        *,
        client_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete API token from current account.

        Ensure that the API token is not being
        used by an active application. After deleting the token, all applications that
        use this token will not be able to get access to your account via API. The
        action cannot be reversed.

        This endpoint is identical to the V1 endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/iam/v2/clients/{client_id}/tokens/{token_id}", client_id=client_id, token_id=token_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        token_id: int,
        *,
        client_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIToken:
        """
        Get information about a specific API token.

        This endpoint is identical to the V1 endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/iam/v2/clients/{client_id}/tokens/{token_id}", client_id=client_id, token_id=token_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIToken,
        )


class APITokensResourceWithRawResponse:
    def __init__(self, api_tokens: APITokensResource) -> None:
        self._api_tokens = api_tokens

        self.create = to_raw_response_wrapper(
            api_tokens.create,
        )
        self.list = to_raw_response_wrapper(
            api_tokens.list,
        )
        self.delete = to_raw_response_wrapper(
            api_tokens.delete,
        )
        self.get = to_raw_response_wrapper(
            api_tokens.get,
        )


class AsyncAPITokensResourceWithRawResponse:
    def __init__(self, api_tokens: AsyncAPITokensResource) -> None:
        self._api_tokens = api_tokens

        self.create = async_to_raw_response_wrapper(
            api_tokens.create,
        )
        self.list = async_to_raw_response_wrapper(
            api_tokens.list,
        )
        self.delete = async_to_raw_response_wrapper(
            api_tokens.delete,
        )
        self.get = async_to_raw_response_wrapper(
            api_tokens.get,
        )


class APITokensResourceWithStreamingResponse:
    def __init__(self, api_tokens: APITokensResource) -> None:
        self._api_tokens = api_tokens

        self.create = to_streamed_response_wrapper(
            api_tokens.create,
        )
        self.list = to_streamed_response_wrapper(
            api_tokens.list,
        )
        self.delete = to_streamed_response_wrapper(
            api_tokens.delete,
        )
        self.get = to_streamed_response_wrapper(
            api_tokens.get,
        )


class AsyncAPITokensResourceWithStreamingResponse:
    def __init__(self, api_tokens: AsyncAPITokensResource) -> None:
        self._api_tokens = api_tokens

        self.create = async_to_streamed_response_wrapper(
            api_tokens.create,
        )
        self.list = async_to_streamed_response_wrapper(
            api_tokens.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            api_tokens.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            api_tokens.get,
        )
