# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

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
from ...pagination import SyncOffsetPage, AsyncOffsetPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.storage import sftp_storage_list_params, sftp_storage_create_params, sftp_storage_update_params
from ...types.storage.sftp_storage import SftpStorage

__all__ = ["SftpStoragesResource", "AsyncSftpStoragesResource"]


class SftpStoragesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SftpStoragesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return SftpStoragesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SftpStoragesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return SftpStoragesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        location_name: str,
        name: str,
        password_mode: Literal["auto", "set", "none"],
        expires: str | Omit = omit,
        has_custom_config_file: bool | Omit = omit,
        is_http_disabled: bool | Omit = omit,
        server_alias: str | Omit = omit,
        sftp_password: str | Omit = omit,
        ssh_key_ids: Iterable[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SftpStorage:
        """
        Creates a new SFTP storage instance in the specified location and returns the
        storage details including credentials.

        Args:
          location_name: Location code where the storage should be created

          name: User-defined name for the storage instance

          password_mode: Password handling mode for SFTP access: 'auto': generate a random password
              (returned in the response) 'set': use the password provided in `sftp_password`
              'none': no password (SSH-key-only access)

          expires: Duration when the storage should expire (e.g., "2 years 6 months"). Omit for no
              expiration.

          has_custom_config_file: Whether this storage should use a custom configuration file

          is_http_disabled: Whether HTTP access should be disabled (HTTPS only)

          server_alias: Custom domain alias for accessing the storage. Omit for no alias.

          sftp_password: SFTP password (8-63 chars). Required when `password_mode` is 'set'. Must be
              omitted when `password_mode` is 'auto' or 'none'.

          ssh_key_ids: SSH key IDs to associate with this storage at creation time. If omitted, no keys
              are linked.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/storage/v4/sftp_storages",
            body=maybe_transform(
                {
                    "location_name": location_name,
                    "name": name,
                    "password_mode": password_mode,
                    "expires": expires,
                    "has_custom_config_file": has_custom_config_file,
                    "is_http_disabled": is_http_disabled,
                    "server_alias": server_alias,
                    "sftp_password": sftp_password,
                    "ssh_key_ids": ssh_key_ids,
                },
                sftp_storage_create_params.SftpStorageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SftpStorage,
        )

    def update(
        self,
        storage_id: int,
        *,
        expires: str | Omit = omit,
        has_custom_config_file: bool | Omit = omit,
        is_http_disabled: bool | Omit = omit,
        password_mode: Literal["auto", "none"] | Omit = omit,
        server_alias: str | Omit = omit,
        ssh_key_ids: Iterable[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SftpStorage:
        """
        Updates SFTP storage configuration and/or credentials including password and SSH
        key management. Supports JSON merge patch semantics: "password": null deletes
        the password, "ssh_key_ids": [] clears all keys.

        Args:
          expires: Duration when the storage should expire (e.g., "2 years 6 months"). Empty string
              to remove.

          has_custom_config_file: Whether this storage should use a custom configuration file

          is_http_disabled: Whether HTTP access should be disabled (HTTPS only)

          password_mode: Password handling mode. Omit to leave password unchanged. 'auto': regenerate
              password (returned in response) 'none': remove password Note: 'set' is not
              allowed in PATCH.

          server_alias: Custom domain alias for accessing the storage. Empty string to remove.

          ssh_key_ids: SSH key IDs to associate with this storage. Replaces all existing keys. If
              omitted, existing keys are unchanged. If empty array, all keys are removed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            path_template("/storage/v4/sftp_storages/{storage_id}", storage_id=storage_id),
            body=maybe_transform(
                {
                    "expires": expires,
                    "has_custom_config_file": has_custom_config_file,
                    "is_http_disabled": is_http_disabled,
                    "password_mode": password_mode,
                    "server_alias": server_alias,
                    "ssh_key_ids": ssh_key_ids,
                },
                sftp_storage_update_params.SftpStorageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SftpStorage,
        )

    def list(
        self,
        *,
        id: str | Omit = omit,
        limit: int | Omit = omit,
        location_name: str | Omit = omit,
        name: str | Omit = omit,
        offset: int | Omit = omit,
        order_by: str | Omit = omit,
        provisioning_status: Literal["active", "creating", "updating", "deleting", "deleted"] | Omit = omit,
        show_deleted: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[SftpStorage]:
        """
        Returns a paginated list of SFTP storage instances for the authenticated client.

        Args:
          id: Filter by storage ID

          limit: Max number of records in response

          location_name: Filter by storage location/region

          name: Filter by storage name

          offset: Number of records to skip

          provisioning_status: Filter by provisioning status

          show_deleted: Include deleted storages

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/storage/v4/sftp_storages",
            page=SyncOffsetPage[SftpStorage],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "limit": limit,
                        "location_name": location_name,
                        "name": name,
                        "offset": offset,
                        "order_by": order_by,
                        "provisioning_status": provisioning_status,
                        "show_deleted": show_deleted,
                    },
                    sftp_storage_list_params.SftpStorageListParams,
                ),
            ),
            model=SftpStorage,
        )

    def delete(
        self,
        storage_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Deletes an SFTP storage instance.

        This operation cannot be undone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/storage/v4/sftp_storages/{storage_id}", storage_id=storage_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        storage_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SftpStorage:
        """
        Returns details of a specific SFTP storage instance (without credentials).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/storage/v4/sftp_storages/{storage_id}", storage_id=storage_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SftpStorage,
        )


class AsyncSftpStoragesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSftpStoragesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSftpStoragesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSftpStoragesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncSftpStoragesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        location_name: str,
        name: str,
        password_mode: Literal["auto", "set", "none"],
        expires: str | Omit = omit,
        has_custom_config_file: bool | Omit = omit,
        is_http_disabled: bool | Omit = omit,
        server_alias: str | Omit = omit,
        sftp_password: str | Omit = omit,
        ssh_key_ids: Iterable[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SftpStorage:
        """
        Creates a new SFTP storage instance in the specified location and returns the
        storage details including credentials.

        Args:
          location_name: Location code where the storage should be created

          name: User-defined name for the storage instance

          password_mode: Password handling mode for SFTP access: 'auto': generate a random password
              (returned in the response) 'set': use the password provided in `sftp_password`
              'none': no password (SSH-key-only access)

          expires: Duration when the storage should expire (e.g., "2 years 6 months"). Omit for no
              expiration.

          has_custom_config_file: Whether this storage should use a custom configuration file

          is_http_disabled: Whether HTTP access should be disabled (HTTPS only)

          server_alias: Custom domain alias for accessing the storage. Omit for no alias.

          sftp_password: SFTP password (8-63 chars). Required when `password_mode` is 'set'. Must be
              omitted when `password_mode` is 'auto' or 'none'.

          ssh_key_ids: SSH key IDs to associate with this storage at creation time. If omitted, no keys
              are linked.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/storage/v4/sftp_storages",
            body=await async_maybe_transform(
                {
                    "location_name": location_name,
                    "name": name,
                    "password_mode": password_mode,
                    "expires": expires,
                    "has_custom_config_file": has_custom_config_file,
                    "is_http_disabled": is_http_disabled,
                    "server_alias": server_alias,
                    "sftp_password": sftp_password,
                    "ssh_key_ids": ssh_key_ids,
                },
                sftp_storage_create_params.SftpStorageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SftpStorage,
        )

    async def update(
        self,
        storage_id: int,
        *,
        expires: str | Omit = omit,
        has_custom_config_file: bool | Omit = omit,
        is_http_disabled: bool | Omit = omit,
        password_mode: Literal["auto", "none"] | Omit = omit,
        server_alias: str | Omit = omit,
        ssh_key_ids: Iterable[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SftpStorage:
        """
        Updates SFTP storage configuration and/or credentials including password and SSH
        key management. Supports JSON merge patch semantics: "password": null deletes
        the password, "ssh_key_ids": [] clears all keys.

        Args:
          expires: Duration when the storage should expire (e.g., "2 years 6 months"). Empty string
              to remove.

          has_custom_config_file: Whether this storage should use a custom configuration file

          is_http_disabled: Whether HTTP access should be disabled (HTTPS only)

          password_mode: Password handling mode. Omit to leave password unchanged. 'auto': regenerate
              password (returned in response) 'none': remove password Note: 'set' is not
              allowed in PATCH.

          server_alias: Custom domain alias for accessing the storage. Empty string to remove.

          ssh_key_ids: SSH key IDs to associate with this storage. Replaces all existing keys. If
              omitted, existing keys are unchanged. If empty array, all keys are removed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            path_template("/storage/v4/sftp_storages/{storage_id}", storage_id=storage_id),
            body=await async_maybe_transform(
                {
                    "expires": expires,
                    "has_custom_config_file": has_custom_config_file,
                    "is_http_disabled": is_http_disabled,
                    "password_mode": password_mode,
                    "server_alias": server_alias,
                    "ssh_key_ids": ssh_key_ids,
                },
                sftp_storage_update_params.SftpStorageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SftpStorage,
        )

    def list(
        self,
        *,
        id: str | Omit = omit,
        limit: int | Omit = omit,
        location_name: str | Omit = omit,
        name: str | Omit = omit,
        offset: int | Omit = omit,
        order_by: str | Omit = omit,
        provisioning_status: Literal["active", "creating", "updating", "deleting", "deleted"] | Omit = omit,
        show_deleted: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[SftpStorage, AsyncOffsetPage[SftpStorage]]:
        """
        Returns a paginated list of SFTP storage instances for the authenticated client.

        Args:
          id: Filter by storage ID

          limit: Max number of records in response

          location_name: Filter by storage location/region

          name: Filter by storage name

          offset: Number of records to skip

          provisioning_status: Filter by provisioning status

          show_deleted: Include deleted storages

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/storage/v4/sftp_storages",
            page=AsyncOffsetPage[SftpStorage],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "limit": limit,
                        "location_name": location_name,
                        "name": name,
                        "offset": offset,
                        "order_by": order_by,
                        "provisioning_status": provisioning_status,
                        "show_deleted": show_deleted,
                    },
                    sftp_storage_list_params.SftpStorageListParams,
                ),
            ),
            model=SftpStorage,
        )

    async def delete(
        self,
        storage_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Deletes an SFTP storage instance.

        This operation cannot be undone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/storage/v4/sftp_storages/{storage_id}", storage_id=storage_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        storage_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SftpStorage:
        """
        Returns details of a specific SFTP storage instance (without credentials).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/storage/v4/sftp_storages/{storage_id}", storage_id=storage_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SftpStorage,
        )


class SftpStoragesResourceWithRawResponse:
    def __init__(self, sftp_storages: SftpStoragesResource) -> None:
        self._sftp_storages = sftp_storages

        self.create = to_raw_response_wrapper(
            sftp_storages.create,
        )
        self.update = to_raw_response_wrapper(
            sftp_storages.update,
        )
        self.list = to_raw_response_wrapper(
            sftp_storages.list,
        )
        self.delete = to_raw_response_wrapper(
            sftp_storages.delete,
        )
        self.get = to_raw_response_wrapper(
            sftp_storages.get,
        )


class AsyncSftpStoragesResourceWithRawResponse:
    def __init__(self, sftp_storages: AsyncSftpStoragesResource) -> None:
        self._sftp_storages = sftp_storages

        self.create = async_to_raw_response_wrapper(
            sftp_storages.create,
        )
        self.update = async_to_raw_response_wrapper(
            sftp_storages.update,
        )
        self.list = async_to_raw_response_wrapper(
            sftp_storages.list,
        )
        self.delete = async_to_raw_response_wrapper(
            sftp_storages.delete,
        )
        self.get = async_to_raw_response_wrapper(
            sftp_storages.get,
        )


class SftpStoragesResourceWithStreamingResponse:
    def __init__(self, sftp_storages: SftpStoragesResource) -> None:
        self._sftp_storages = sftp_storages

        self.create = to_streamed_response_wrapper(
            sftp_storages.create,
        )
        self.update = to_streamed_response_wrapper(
            sftp_storages.update,
        )
        self.list = to_streamed_response_wrapper(
            sftp_storages.list,
        )
        self.delete = to_streamed_response_wrapper(
            sftp_storages.delete,
        )
        self.get = to_streamed_response_wrapper(
            sftp_storages.get,
        )


class AsyncSftpStoragesResourceWithStreamingResponse:
    def __init__(self, sftp_storages: AsyncSftpStoragesResource) -> None:
        self._sftp_storages = sftp_storages

        self.create = async_to_streamed_response_wrapper(
            sftp_storages.create,
        )
        self.update = async_to_streamed_response_wrapper(
            sftp_storages.update,
        )
        self.list = async_to_streamed_response_wrapper(
            sftp_storages.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            sftp_storages.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            sftp_storages.get,
        )
