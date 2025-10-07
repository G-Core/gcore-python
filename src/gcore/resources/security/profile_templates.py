# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.security.profile_template_list_response import ProfileTemplateListResponse

__all__ = ["ProfileTemplatesResource", "AsyncProfileTemplatesResource"]


class ProfileTemplatesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProfileTemplatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return ProfileTemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProfileTemplatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return ProfileTemplatesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileTemplateListResponse:
        """Get list of profile templates.

        Profile template is used as a template to create
        profile. Client receives only common and created for him profile templates.
        """
        return self._get(
            "/security/iaas/profile-templates",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileTemplateListResponse,
        )


class AsyncProfileTemplatesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProfileTemplatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProfileTemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProfileTemplatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncProfileTemplatesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileTemplateListResponse:
        """Get list of profile templates.

        Profile template is used as a template to create
        profile. Client receives only common and created for him profile templates.
        """
        return await self._get(
            "/security/iaas/profile-templates",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileTemplateListResponse,
        )


class ProfileTemplatesResourceWithRawResponse:
    def __init__(self, profile_templates: ProfileTemplatesResource) -> None:
        self._profile_templates = profile_templates

        self.list = to_raw_response_wrapper(
            profile_templates.list,
        )


class AsyncProfileTemplatesResourceWithRawResponse:
    def __init__(self, profile_templates: AsyncProfileTemplatesResource) -> None:
        self._profile_templates = profile_templates

        self.list = async_to_raw_response_wrapper(
            profile_templates.list,
        )


class ProfileTemplatesResourceWithStreamingResponse:
    def __init__(self, profile_templates: ProfileTemplatesResource) -> None:
        self._profile_templates = profile_templates

        self.list = to_streamed_response_wrapper(
            profile_templates.list,
        )


class AsyncProfileTemplatesResourceWithStreamingResponse:
    def __init__(self, profile_templates: AsyncProfileTemplatesResource) -> None:
        self._profile_templates = profile_templates

        self.list = async_to_streamed_response_wrapper(
            profile_templates.list,
        )
