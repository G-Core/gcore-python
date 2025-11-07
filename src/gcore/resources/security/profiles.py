# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

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
from ...types.security import (
    profile_list_params,
    profile_create_params,
    profile_replace_params,
    profile_recreate_params,
)
from ...types.security.client_profile import ClientProfile
from ...types.security.profile_list_response import ProfileListResponse

__all__ = ["ProfilesResource", "AsyncProfilesResource"]


class ProfilesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProfilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return ProfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProfilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return ProfilesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        fields: Iterable[profile_create_params.Field],
        profile_template: int,
        site: str,
        ip_address: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClientProfile:
        """Create protection profile.

        Protection is enabled at the same time as profile is
        created

        Args:
          site: Region where the protection profiles will be deployed

          ip_address: Required for Universal template only. Optional for all others.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/security/iaas/v2/profiles",
            body=maybe_transform(
                {
                    "fields": fields,
                    "profile_template": profile_template,
                    "site": site,
                    "ip_address": ip_address,
                },
                profile_create_params.ProfileCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClientProfile,
        )

    def list(
        self,
        *,
        exclude_empty_address: bool | Omit = omit,
        include_deleted: bool | Omit = omit,
        ip_address: str | Omit = omit,
        site: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileListResponse:
        """Get list of protection profiles.

        Client receives only profiles created by him

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/security/iaas/v2/profiles",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "exclude_empty_address": exclude_empty_address,
                        "include_deleted": include_deleted,
                        "ip_address": ip_address,
                        "site": site,
                    },
                    profile_list_params.ProfileListParams,
                ),
            ),
            cast_to=ProfileListResponse,
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
        """Delete protection profile.

        Protection is disabled at the same time as profile is
        deleted

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/security/iaas/v2/profiles/{id}",
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
    ) -> ClientProfile:
        """
        Get profile by id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/security/iaas/v2/profiles/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClientProfile,
        )

    def recreate(
        self,
        id: int,
        *,
        fields: Iterable[profile_recreate_params.Field],
        profile_template: int,
        ip_address: str | Omit = omit,
        site: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClientProfile:
        """
        Recreate profile with another profile template (for other cases use detail API)

        Args:
          ip_address: Required for Universal template only. Optional for all others.

          site: Region where the protection profiles will be deployed

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/security/iaas/v2/profiles/{id}/recreate",
            body=maybe_transform(
                {
                    "fields": fields,
                    "profile_template": profile_template,
                    "ip_address": ip_address,
                    "site": site,
                },
                profile_recreate_params.ProfileRecreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClientProfile,
        )

    def replace(
        self,
        id: int,
        *,
        fields: Iterable[profile_replace_params.Field],
        profile_template: int,
        ip_address: str | Omit = omit,
        site: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClientProfile:
        """Update profile.

        Protection policies are updated at the same time as profile
        updated

        Args:
          ip_address: Required for Universal template only. Optional for all others.

          site: Region where the protection profiles will be deployed

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/security/iaas/v2/profiles/{id}",
            body=maybe_transform(
                {
                    "fields": fields,
                    "profile_template": profile_template,
                    "ip_address": ip_address,
                    "site": site,
                },
                profile_replace_params.ProfileReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClientProfile,
        )


class AsyncProfilesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProfilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProfilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncProfilesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        fields: Iterable[profile_create_params.Field],
        profile_template: int,
        site: str,
        ip_address: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClientProfile:
        """Create protection profile.

        Protection is enabled at the same time as profile is
        created

        Args:
          site: Region where the protection profiles will be deployed

          ip_address: Required for Universal template only. Optional for all others.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/security/iaas/v2/profiles",
            body=await async_maybe_transform(
                {
                    "fields": fields,
                    "profile_template": profile_template,
                    "site": site,
                    "ip_address": ip_address,
                },
                profile_create_params.ProfileCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClientProfile,
        )

    async def list(
        self,
        *,
        exclude_empty_address: bool | Omit = omit,
        include_deleted: bool | Omit = omit,
        ip_address: str | Omit = omit,
        site: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileListResponse:
        """Get list of protection profiles.

        Client receives only profiles created by him

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/security/iaas/v2/profiles",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "exclude_empty_address": exclude_empty_address,
                        "include_deleted": include_deleted,
                        "ip_address": ip_address,
                        "site": site,
                    },
                    profile_list_params.ProfileListParams,
                ),
            ),
            cast_to=ProfileListResponse,
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
        """Delete protection profile.

        Protection is disabled at the same time as profile is
        deleted

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/security/iaas/v2/profiles/{id}",
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
    ) -> ClientProfile:
        """
        Get profile by id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/security/iaas/v2/profiles/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClientProfile,
        )

    async def recreate(
        self,
        id: int,
        *,
        fields: Iterable[profile_recreate_params.Field],
        profile_template: int,
        ip_address: str | Omit = omit,
        site: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClientProfile:
        """
        Recreate profile with another profile template (for other cases use detail API)

        Args:
          ip_address: Required for Universal template only. Optional for all others.

          site: Region where the protection profiles will be deployed

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/security/iaas/v2/profiles/{id}/recreate",
            body=await async_maybe_transform(
                {
                    "fields": fields,
                    "profile_template": profile_template,
                    "ip_address": ip_address,
                    "site": site,
                },
                profile_recreate_params.ProfileRecreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClientProfile,
        )

    async def replace(
        self,
        id: int,
        *,
        fields: Iterable[profile_replace_params.Field],
        profile_template: int,
        ip_address: str | Omit = omit,
        site: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClientProfile:
        """Update profile.

        Protection policies are updated at the same time as profile
        updated

        Args:
          ip_address: Required for Universal template only. Optional for all others.

          site: Region where the protection profiles will be deployed

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/security/iaas/v2/profiles/{id}",
            body=await async_maybe_transform(
                {
                    "fields": fields,
                    "profile_template": profile_template,
                    "ip_address": ip_address,
                    "site": site,
                },
                profile_replace_params.ProfileReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClientProfile,
        )


class ProfilesResourceWithRawResponse:
    def __init__(self, profiles: ProfilesResource) -> None:
        self._profiles = profiles

        self.create = to_raw_response_wrapper(
            profiles.create,
        )
        self.list = to_raw_response_wrapper(
            profiles.list,
        )
        self.delete = to_raw_response_wrapper(
            profiles.delete,
        )
        self.get = to_raw_response_wrapper(
            profiles.get,
        )
        self.recreate = to_raw_response_wrapper(
            profiles.recreate,
        )
        self.replace = to_raw_response_wrapper(
            profiles.replace,
        )


class AsyncProfilesResourceWithRawResponse:
    def __init__(self, profiles: AsyncProfilesResource) -> None:
        self._profiles = profiles

        self.create = async_to_raw_response_wrapper(
            profiles.create,
        )
        self.list = async_to_raw_response_wrapper(
            profiles.list,
        )
        self.delete = async_to_raw_response_wrapper(
            profiles.delete,
        )
        self.get = async_to_raw_response_wrapper(
            profiles.get,
        )
        self.recreate = async_to_raw_response_wrapper(
            profiles.recreate,
        )
        self.replace = async_to_raw_response_wrapper(
            profiles.replace,
        )


class ProfilesResourceWithStreamingResponse:
    def __init__(self, profiles: ProfilesResource) -> None:
        self._profiles = profiles

        self.create = to_streamed_response_wrapper(
            profiles.create,
        )
        self.list = to_streamed_response_wrapper(
            profiles.list,
        )
        self.delete = to_streamed_response_wrapper(
            profiles.delete,
        )
        self.get = to_streamed_response_wrapper(
            profiles.get,
        )
        self.recreate = to_streamed_response_wrapper(
            profiles.recreate,
        )
        self.replace = to_streamed_response_wrapper(
            profiles.replace,
        )


class AsyncProfilesResourceWithStreamingResponse:
    def __init__(self, profiles: AsyncProfilesResource) -> None:
        self._profiles = profiles

        self.create = async_to_streamed_response_wrapper(
            profiles.create,
        )
        self.list = async_to_streamed_response_wrapper(
            profiles.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            profiles.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            profiles.get,
        )
        self.recreate = async_to_streamed_response_wrapper(
            profiles.recreate,
        )
        self.replace = async_to_streamed_response_wrapper(
            profiles.replace,
        )
