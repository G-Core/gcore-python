# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.cloud.file_shares import access_rule_create_params
from ....types.cloud.file_shares.access_rule import AccessRule
from ....types.cloud.file_shares.access_rule_list import AccessRuleList

__all__ = ["AccessRulesResource", "AsyncAccessRulesResource"]


class AccessRulesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccessRulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AccessRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccessRulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AccessRulesResourceWithStreamingResponse(self)

    def create(
        self,
        file_share_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        access_mode: Literal["ro", "rw"],
        ip_address: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccessRule:
        """
        Create file share access rule

        Args:
          project_id: Project ID

          region_id: Region ID

          file_share_id: File Share ID

          access_mode: Access mode

          ip_address: Source IP or network

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not file_share_id:
            raise ValueError(f"Expected a non-empty value for `file_share_id` but received {file_share_id!r}")
        return self._post(
            f"/cloud/v1/file_shares/{project_id}/{region_id}/{file_share_id}/access_rule",
            body=maybe_transform(
                {
                    "access_mode": access_mode,
                    "ip_address": ip_address,
                },
                access_rule_create_params.AccessRuleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccessRule,
        )

    def list(
        self,
        file_share_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccessRuleList:
        """
        List file share access rules

        Args:
          project_id: Project ID

          region_id: Region ID

          file_share_id: File Share ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not file_share_id:
            raise ValueError(f"Expected a non-empty value for `file_share_id` but received {file_share_id!r}")
        return self._get(
            f"/cloud/v1/file_shares/{project_id}/{region_id}/{file_share_id}/access_rule",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccessRuleList,
        )

    def delete(
        self,
        access_rule_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        file_share_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete file share access rule

        Args:
          project_id: Project ID

          region_id: Region ID

          file_share_id: File Share ID

          access_rule_id: Access Rule ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not file_share_id:
            raise ValueError(f"Expected a non-empty value for `file_share_id` but received {file_share_id!r}")
        if not access_rule_id:
            raise ValueError(f"Expected a non-empty value for `access_rule_id` but received {access_rule_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/cloud/v1/file_shares/{project_id}/{region_id}/{file_share_id}/access_rule/{access_rule_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAccessRulesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccessRulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccessRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccessRulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncAccessRulesResourceWithStreamingResponse(self)

    async def create(
        self,
        file_share_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        access_mode: Literal["ro", "rw"],
        ip_address: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccessRule:
        """
        Create file share access rule

        Args:
          project_id: Project ID

          region_id: Region ID

          file_share_id: File Share ID

          access_mode: Access mode

          ip_address: Source IP or network

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not file_share_id:
            raise ValueError(f"Expected a non-empty value for `file_share_id` but received {file_share_id!r}")
        return await self._post(
            f"/cloud/v1/file_shares/{project_id}/{region_id}/{file_share_id}/access_rule",
            body=await async_maybe_transform(
                {
                    "access_mode": access_mode,
                    "ip_address": ip_address,
                },
                access_rule_create_params.AccessRuleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccessRule,
        )

    async def list(
        self,
        file_share_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccessRuleList:
        """
        List file share access rules

        Args:
          project_id: Project ID

          region_id: Region ID

          file_share_id: File Share ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not file_share_id:
            raise ValueError(f"Expected a non-empty value for `file_share_id` but received {file_share_id!r}")
        return await self._get(
            f"/cloud/v1/file_shares/{project_id}/{region_id}/{file_share_id}/access_rule",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccessRuleList,
        )

    async def delete(
        self,
        access_rule_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        file_share_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete file share access rule

        Args:
          project_id: Project ID

          region_id: Region ID

          file_share_id: File Share ID

          access_rule_id: Access Rule ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not file_share_id:
            raise ValueError(f"Expected a non-empty value for `file_share_id` but received {file_share_id!r}")
        if not access_rule_id:
            raise ValueError(f"Expected a non-empty value for `access_rule_id` but received {access_rule_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/cloud/v1/file_shares/{project_id}/{region_id}/{file_share_id}/access_rule/{access_rule_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AccessRulesResourceWithRawResponse:
    def __init__(self, access_rules: AccessRulesResource) -> None:
        self._access_rules = access_rules

        self.create = to_raw_response_wrapper(
            access_rules.create,
        )
        self.list = to_raw_response_wrapper(
            access_rules.list,
        )
        self.delete = to_raw_response_wrapper(
            access_rules.delete,
        )


class AsyncAccessRulesResourceWithRawResponse:
    def __init__(self, access_rules: AsyncAccessRulesResource) -> None:
        self._access_rules = access_rules

        self.create = async_to_raw_response_wrapper(
            access_rules.create,
        )
        self.list = async_to_raw_response_wrapper(
            access_rules.list,
        )
        self.delete = async_to_raw_response_wrapper(
            access_rules.delete,
        )


class AccessRulesResourceWithStreamingResponse:
    def __init__(self, access_rules: AccessRulesResource) -> None:
        self._access_rules = access_rules

        self.create = to_streamed_response_wrapper(
            access_rules.create,
        )
        self.list = to_streamed_response_wrapper(
            access_rules.list,
        )
        self.delete = to_streamed_response_wrapper(
            access_rules.delete,
        )


class AsyncAccessRulesResourceWithStreamingResponse:
    def __init__(self, access_rules: AsyncAccessRulesResource) -> None:
        self._access_rules = access_rules

        self.create = async_to_streamed_response_wrapper(
            access_rules.create,
        )
        self.list = async_to_streamed_response_wrapper(
            access_rules.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            access_rules.delete,
        )
