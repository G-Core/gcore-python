# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
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
    **Deprecated:** All endpoints in this section will be removed on **2026-07-17**.
    Use the [API Tokens V2](#tag/API-Tokens-V2) endpoints instead. Existing tokens
    issued by V1 endpoints continue to authenticate after the removal date.

    Use permanent API tokens for regular automated requests to services.
    You can either set its validity period when creating it or issue a token for an unlimited time.
    Please address the API documentation of the specific product in order to check if it supports API tokens.

    Provide your APIKey in the Authorization header.

    Example: ```curl -H "Authorization: APIKey 123$61b8e1e7a68c" https://api.gcore.com/iam/users/me```

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

    @typing_extensions.deprecated("deprecated")
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
        """**Deprecated:** This endpoint will be removed on **2026-07-17**.

        Use
        [`POST /v2/clients/{clientId}/tokens`](#operation/iamCreateApiTokenV2) instead.

        Create an API token in the current account.

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
            path_template("/iam/clients/{client_id}/tokens", client_id=client_id),
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

    @typing_extensions.deprecated("deprecated")
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
        """**Deprecated:** This endpoint will be removed on **2026-07-17**.

        Use
        [`GET /v2/clients/{clientId}/tokens`](#operation/iamGetApiTokensV2) instead.

        Get information about your permanent API tokens in the account. A user with the
        Administrators role gets information about all API tokens in the account.

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
            path_template("/iam/clients/{client_id}/tokens", client_id=client_id),
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

    @typing_extensions.deprecated("deprecated")
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
        """**Deprecated:** This endpoint will be removed on **2026-07-17**.

        Use
        [`DELETE /v2/clients/{clientId}/tokens/{tokenId}`](#operation/iamDeleteApiTokenV2)
        instead.

        Delete API token from current account. Ensure that the API token is not being
        used by an active application. After deleting the token, all applications that
        use this token will not be able to get access to your account via API. The
        action cannot be reversed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/iam/clients/{client_id}/tokens/{token_id}", client_id=client_id, token_id=token_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    @typing_extensions.deprecated("deprecated")
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
        """**Deprecated:** This endpoint will be removed on **2026-07-17**.

        Use
        [`GET /v2/clients/{clientId}/tokens/{tokenId}`](#operation/iamGetApiTokenV2)
        instead.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/iam/clients/{client_id}/tokens/{token_id}", client_id=client_id, token_id=token_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIToken,
        )


class AsyncAPITokensResource(AsyncAPIResource):
    """
    **Deprecated:** All endpoints in this section will be removed on **2026-07-17**.
    Use the [API Tokens V2](#tag/API-Tokens-V2) endpoints instead. Existing tokens
    issued by V1 endpoints continue to authenticate after the removal date.

    Use permanent API tokens for regular automated requests to services.
    You can either set its validity period when creating it or issue a token for an unlimited time.
    Please address the API documentation of the specific product in order to check if it supports API tokens.

    Provide your APIKey in the Authorization header.

    Example: ```curl -H "Authorization: APIKey 123$61b8e1e7a68c" https://api.gcore.com/iam/users/me```

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

    @typing_extensions.deprecated("deprecated")
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
        """**Deprecated:** This endpoint will be removed on **2026-07-17**.

        Use
        [`POST /v2/clients/{clientId}/tokens`](#operation/iamCreateApiTokenV2) instead.

        Create an API token in the current account.

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
            path_template("/iam/clients/{client_id}/tokens", client_id=client_id),
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

    @typing_extensions.deprecated("deprecated")
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
        """**Deprecated:** This endpoint will be removed on **2026-07-17**.

        Use
        [`GET /v2/clients/{clientId}/tokens`](#operation/iamGetApiTokensV2) instead.

        Get information about your permanent API tokens in the account. A user with the
        Administrators role gets information about all API tokens in the account.

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
            path_template("/iam/clients/{client_id}/tokens", client_id=client_id),
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

    @typing_extensions.deprecated("deprecated")
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
        """**Deprecated:** This endpoint will be removed on **2026-07-17**.

        Use
        [`DELETE /v2/clients/{clientId}/tokens/{tokenId}`](#operation/iamDeleteApiTokenV2)
        instead.

        Delete API token from current account. Ensure that the API token is not being
        used by an active application. After deleting the token, all applications that
        use this token will not be able to get access to your account via API. The
        action cannot be reversed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/iam/clients/{client_id}/tokens/{token_id}", client_id=client_id, token_id=token_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    @typing_extensions.deprecated("deprecated")
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
        """**Deprecated:** This endpoint will be removed on **2026-07-17**.

        Use
        [`GET /v2/clients/{clientId}/tokens/{tokenId}`](#operation/iamGetApiTokenV2)
        instead.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/iam/clients/{client_id}/tokens/{token_id}", client_id=client_id, token_id=token_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIToken,
        )


class APITokensResourceWithRawResponse:
    def __init__(self, api_tokens: APITokensResource) -> None:
        self._api_tokens = api_tokens

        self.create = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                api_tokens.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                api_tokens.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                api_tokens.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                api_tokens.get,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncAPITokensResourceWithRawResponse:
    def __init__(self, api_tokens: AsyncAPITokensResource) -> None:
        self._api_tokens = api_tokens

        self.create = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                api_tokens.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                api_tokens.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                api_tokens.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                api_tokens.get,  # pyright: ignore[reportDeprecated],
            )
        )


class APITokensResourceWithStreamingResponse:
    def __init__(self, api_tokens: APITokensResource) -> None:
        self._api_tokens = api_tokens

        self.create = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                api_tokens.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                api_tokens.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                api_tokens.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                api_tokens.get,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncAPITokensResourceWithStreamingResponse:
    def __init__(self, api_tokens: AsyncAPITokensResource) -> None:
        self._api_tokens = api_tokens

        self.create = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                api_tokens.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                api_tokens.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                api_tokens.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                api_tokens.get,  # pyright: ignore[reportDeprecated],
            )
        )
