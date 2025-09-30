# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ....types.cdn.logs import setting_create_params, setting_update_params
from ....types.cdn.logs.log_settings import LogSettings

__all__ = ["SettingsResource", "AsyncSettingsResource"]


class SettingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return SettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return SettingsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        all_resources_bucket: str,
        all_resources_folder: str,
        folders: Iterable[setting_create_params.Folder],
        for_all_resources: bool,
        ftp_hostname: str,
        ftp_login: str,
        ftp_password: str,
        s3_access_key_id: str,
        s3_hostname: str,
        s3_secret_key: str,
        s3_type: str,
        sftp_hostname: str,
        sftp_login: str,
        sftp_password: str,
        storage_type: str,
        archive_size_mb: Optional[int] | Omit = omit,
        enabled: bool | Omit = omit,
        ftp_prepend_folder: str | Omit = omit,
        ignore_empty_logs: bool | Omit = omit,
        s3_aws_region: int | Omit = omit,
        s3_bucket_location: str | Omit = omit,
        s3_host_bucket: str | Omit = omit,
        sftp_key_passphrase: str | Omit = omit,
        sftp_prepend_folder: str | Omit = omit,
        sftp_private_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Setup raw logs settings

        Args:
          all_resources_bucket: Name of the S3 bucket to which logs for all CDN resources are delivered.

          all_resources_folder:
              Parameter meaning depends on the value of the "`storage_type`" value:

              - If "`storage_type`": s3 - Name of the S3 bucket sub-folder to which logs for
                all CDN resources are delivered.
              - If "`storage_type`": ftp/sftp - Name of the folder (or path) to which logs for
                all CDN resources are delivered.

          folders: List of folders/buckets for receiving CDN resources logs.

          for_all_resources: Defines whether logs of all CDN resources are delivered to one folder/bucket or
              to separate ones.

              Possible values:

              - **true** - Logs of all CDN resources are delivered to one folder/bucket.
              - **false** - Logs of different CDN resources are delivered to separate
                folders/buckets.

          ftp_hostname: FTP storage hostname.

          ftp_login: FTP storage login.

          ftp_password: FTP storage password.

          s3_access_key_id: Access key ID for the S3 account.

              Access Key ID is 20 alpha-numeric characters like 022QF06E7MXBSH9DHM02

          s3_hostname: S3 storage hostname.

              It is required if "`s3_type`": other.

          s3_secret_key: Secret access key for the S3 account.

              Secret Access Key is 20-50 alpha-numeric-slash-plus characters like
              kWcrlUX5JEDGM/LtmEENI/aVmYvHNif5zB+d9+ct

          s3_type: Storage type compatible with S3.

              Possible values:

              - **amazon** – AWS S3 storage.
              - **other** – Other (not AWS) S3 compatible storage.

          sftp_hostname: SFTP storage hostname.

          sftp_login: SFTP storage login.

          sftp_password: SFTP storage password.

              It should be empty if "`sftp_private_key`" is set.

          storage_type: Storage type.

              Possible values:

              - **ftp**
              - **sftp**
              - **s3**

          archive_size_mb: The size of a single piece of the archive in MB. In case of **null** value logs
              are delivered without slicing.

          enabled: Enables or disables a log forwarding feature.

              Possible values:

              - **true** - log forwarding feature is active.
              - **false** - log forwarding feature is deactivated.

          ftp_prepend_folder: Name of the FTP prepend folder for log delivery.

              **Null** is allowed.

          ignore_empty_logs: Enables or disables the forwarding of empty logs.

              Possible values:

              - **true** - Empty logs are not sent.
              - **false** - Empty logs are sent.

          s3_aws_region: Amazon AWS region.

          s3_bucket_location: Location of S3 storage.

              Restrictions:

              - Maximum of 255 symbols.
              - Latin letters (A-Z, a-z), digits (0-9), dots, colons, dashes, and underscores
                (.:\\__-).

          s3_host_bucket: S3 bucket hostname.

              Restrictions:

              - Maximum of 255 symbols.
              - Latin letters (A-Z, a-z,) digits (0-9,) dots, colons, dashes, and underscores.
              - Required if "`s3_type`": other.

          sftp_key_passphrase: Passphrase for SFTP private key.

              Restrictions:

              - Should be set if private key encoded with passphrase.
              - Should be empty if "`sftp_password`" is set.

          sftp_prepend_folder: Name of the SFTP prepend folder for log delivery.

              **Null** is allowed.

          sftp_private_key: Private key for SFTP authorization.

              Possible values:

              - **RSA**
              - **ED25519**

              It should be empty if "`sftp_password`" is set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/cdn/raw_log_settings"
            if self._client._base_url_overridden
            else "https://api.gcore.com//cdn/raw_log_settings",
            body=maybe_transform(
                {
                    "all_resources_bucket": all_resources_bucket,
                    "all_resources_folder": all_resources_folder,
                    "folders": folders,
                    "for_all_resources": for_all_resources,
                    "ftp_hostname": ftp_hostname,
                    "ftp_login": ftp_login,
                    "ftp_password": ftp_password,
                    "s3_access_key_id": s3_access_key_id,
                    "s3_hostname": s3_hostname,
                    "s3_secret_key": s3_secret_key,
                    "s3_type": s3_type,
                    "sftp_hostname": sftp_hostname,
                    "sftp_login": sftp_login,
                    "sftp_password": sftp_password,
                    "storage_type": storage_type,
                    "archive_size_mb": archive_size_mb,
                    "enabled": enabled,
                    "ftp_prepend_folder": ftp_prepend_folder,
                    "ignore_empty_logs": ignore_empty_logs,
                    "s3_aws_region": s3_aws_region,
                    "s3_bucket_location": s3_bucket_location,
                    "s3_host_bucket": s3_host_bucket,
                    "sftp_key_passphrase": sftp_key_passphrase,
                    "sftp_prepend_folder": sftp_prepend_folder,
                    "sftp_private_key": sftp_private_key,
                },
                setting_create_params.SettingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def update(
        self,
        *,
        all_resources_bucket: str,
        all_resources_folder: str,
        folders: Iterable[setting_update_params.Folder],
        for_all_resources: bool,
        ftp_hostname: str,
        ftp_login: str,
        ftp_password: str,
        s3_access_key_id: str,
        s3_hostname: str,
        s3_secret_key: str,
        s3_type: str,
        sftp_hostname: str,
        sftp_login: str,
        sftp_password: str,
        storage_type: str,
        archive_size_mb: Optional[int] | Omit = omit,
        enabled: bool | Omit = omit,
        ftp_prepend_folder: str | Omit = omit,
        ignore_empty_logs: bool | Omit = omit,
        s3_aws_region: int | Omit = omit,
        s3_bucket_location: str | Omit = omit,
        s3_host_bucket: str | Omit = omit,
        sftp_key_passphrase: str | Omit = omit,
        sftp_prepend_folder: str | Omit = omit,
        sftp_private_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        PATCH method is not allowed.

        Args:
          all_resources_bucket: Name of the S3 bucket to which logs for all CDN resources are delivered.

          all_resources_folder:
              Parameter meaning depends on the value of the "`storage_type`" value:

              - If "`storage_type`": s3 - Name of the S3 bucket sub-folder to which logs for
                all CDN resources are delivered.
              - If "`storage_type`": ftp/sftp - Name of the folder (or path) to which logs for
                all CDN resources are delivered.

          folders: List of folders/buckets for receiving CDN resources logs.

          for_all_resources: Defines whether logs of all CDN resources are delivered to one folder/bucket or
              to separate ones.

              Possible values:

              - **true** - Logs of all CDN resources are delivered to one folder/bucket.
              - **false** - Logs of different CDN resources are delivered to separate
                folders/buckets.

          ftp_hostname: FTP storage hostname.

          ftp_login: FTP storage login.

          ftp_password: FTP storage password.

          s3_access_key_id: Access key ID for the S3 account.

              Access Key ID is 20 alpha-numeric characters like 022QF06E7MXBSH9DHM02

          s3_hostname: S3 storage hostname.

              It is required if "`s3_type`": other.

          s3_secret_key: Secret access key for the S3 account.

              Secret Access Key is 20-50 alpha-numeric-slash-plus characters like
              kWcrlUX5JEDGM/LtmEENI/aVmYvHNif5zB+d9+ct

          s3_type: Storage type compatible with S3.

              Possible values:

              - **amazon** – AWS S3 storage.
              - **other** – Other (not AWS) S3 compatible storage.

          sftp_hostname: SFTP storage hostname.

          sftp_login: SFTP storage login.

          sftp_password: SFTP storage password.

              It should be empty if "`sftp_private_key`" is set.

          storage_type: Storage type.

              Possible values:

              - **ftp**
              - **sftp**
              - **s3**

          archive_size_mb: The size of a single piece of the archive in MB. In case of **null** value logs
              are delivered without slicing.

          enabled: Enables or disables a log forwarding feature.

              Possible values:

              - **true** - log forwarding feature is active.
              - **false** - log forwarding feature is deactivated.

          ftp_prepend_folder: Name of the FTP prepend folder for log delivery.

              **Null** is allowed.

          ignore_empty_logs: Enables or disables the forwarding of empty logs.

              Possible values:

              - **true** - Empty logs are not sent.
              - **false** - Empty logs are sent.

          s3_aws_region: Amazon AWS region.

          s3_bucket_location: Location of S3 storage.

              Restrictions:

              - Maximum of 255 symbols.
              - Latin letters (A-Z, a-z), digits (0-9), dots, colons, dashes, and underscores
                (.:\\__-).

          s3_host_bucket: S3 bucket hostname.

              Restrictions:

              - Maximum of 255 symbols.
              - Latin letters (A-Z, a-z,) digits (0-9,) dots, colons, dashes, and underscores.
              - Required if "`s3_type`": other.

          sftp_key_passphrase: Passphrase for SFTP private key.

              Restrictions:

              - Should be set if private key encoded with passphrase.
              - Should be empty if "`sftp_password`" is set.

          sftp_prepend_folder: Name of the SFTP prepend folder for log delivery.

              **Null** is allowed.

          sftp_private_key: Private key for SFTP authorization.

              Possible values:

              - **RSA**
              - **ED25519**

              It should be empty if "`sftp_password`" is set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            "/cdn/raw_log_settings"
            if self._client._base_url_overridden
            else "https://api.gcore.com//cdn/raw_log_settings",
            body=maybe_transform(
                {
                    "all_resources_bucket": all_resources_bucket,
                    "all_resources_folder": all_resources_folder,
                    "folders": folders,
                    "for_all_resources": for_all_resources,
                    "ftp_hostname": ftp_hostname,
                    "ftp_login": ftp_login,
                    "ftp_password": ftp_password,
                    "s3_access_key_id": s3_access_key_id,
                    "s3_hostname": s3_hostname,
                    "s3_secret_key": s3_secret_key,
                    "s3_type": s3_type,
                    "sftp_hostname": sftp_hostname,
                    "sftp_login": sftp_login,
                    "sftp_password": sftp_password,
                    "storage_type": storage_type,
                    "archive_size_mb": archive_size_mb,
                    "enabled": enabled,
                    "ftp_prepend_folder": ftp_prepend_folder,
                    "ignore_empty_logs": ignore_empty_logs,
                    "s3_aws_region": s3_aws_region,
                    "s3_bucket_location": s3_bucket_location,
                    "s3_host_bucket": s3_host_bucket,
                    "sftp_key_passphrase": sftp_key_passphrase,
                    "sftp_prepend_folder": sftp_prepend_folder,
                    "sftp_private_key": sftp_private_key,
                },
                setting_update_params.SettingUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def delete(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete the raw logs delivery configuration from the system permanently.

        Notes:

        - **Deactivation Requirement**: Set the `enabled` attribute to `false` before
          deletion.
        - **Irreversibility**: This action is irreversible. Once deleted, the raw logs
          delivery configuration cannot be recovered.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            "/cdn/raw_log_settings"
            if self._client._base_url_overridden
            else "https://api.gcore.com//cdn/raw_log_settings",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogSettings:
        """Get information about raw logs feature settings."""
        return self._get(
            "/cdn/raw_log_settings"
            if self._client._base_url_overridden
            else "https://api.gcore.com//cdn/raw_log_settings",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogSettings,
        )


class AsyncSettingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncSettingsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        all_resources_bucket: str,
        all_resources_folder: str,
        folders: Iterable[setting_create_params.Folder],
        for_all_resources: bool,
        ftp_hostname: str,
        ftp_login: str,
        ftp_password: str,
        s3_access_key_id: str,
        s3_hostname: str,
        s3_secret_key: str,
        s3_type: str,
        sftp_hostname: str,
        sftp_login: str,
        sftp_password: str,
        storage_type: str,
        archive_size_mb: Optional[int] | Omit = omit,
        enabled: bool | Omit = omit,
        ftp_prepend_folder: str | Omit = omit,
        ignore_empty_logs: bool | Omit = omit,
        s3_aws_region: int | Omit = omit,
        s3_bucket_location: str | Omit = omit,
        s3_host_bucket: str | Omit = omit,
        sftp_key_passphrase: str | Omit = omit,
        sftp_prepend_folder: str | Omit = omit,
        sftp_private_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Setup raw logs settings

        Args:
          all_resources_bucket: Name of the S3 bucket to which logs for all CDN resources are delivered.

          all_resources_folder:
              Parameter meaning depends on the value of the "`storage_type`" value:

              - If "`storage_type`": s3 - Name of the S3 bucket sub-folder to which logs for
                all CDN resources are delivered.
              - If "`storage_type`": ftp/sftp - Name of the folder (or path) to which logs for
                all CDN resources are delivered.

          folders: List of folders/buckets for receiving CDN resources logs.

          for_all_resources: Defines whether logs of all CDN resources are delivered to one folder/bucket or
              to separate ones.

              Possible values:

              - **true** - Logs of all CDN resources are delivered to one folder/bucket.
              - **false** - Logs of different CDN resources are delivered to separate
                folders/buckets.

          ftp_hostname: FTP storage hostname.

          ftp_login: FTP storage login.

          ftp_password: FTP storage password.

          s3_access_key_id: Access key ID for the S3 account.

              Access Key ID is 20 alpha-numeric characters like 022QF06E7MXBSH9DHM02

          s3_hostname: S3 storage hostname.

              It is required if "`s3_type`": other.

          s3_secret_key: Secret access key for the S3 account.

              Secret Access Key is 20-50 alpha-numeric-slash-plus characters like
              kWcrlUX5JEDGM/LtmEENI/aVmYvHNif5zB+d9+ct

          s3_type: Storage type compatible with S3.

              Possible values:

              - **amazon** – AWS S3 storage.
              - **other** – Other (not AWS) S3 compatible storage.

          sftp_hostname: SFTP storage hostname.

          sftp_login: SFTP storage login.

          sftp_password: SFTP storage password.

              It should be empty if "`sftp_private_key`" is set.

          storage_type: Storage type.

              Possible values:

              - **ftp**
              - **sftp**
              - **s3**

          archive_size_mb: The size of a single piece of the archive in MB. In case of **null** value logs
              are delivered without slicing.

          enabled: Enables or disables a log forwarding feature.

              Possible values:

              - **true** - log forwarding feature is active.
              - **false** - log forwarding feature is deactivated.

          ftp_prepend_folder: Name of the FTP prepend folder for log delivery.

              **Null** is allowed.

          ignore_empty_logs: Enables or disables the forwarding of empty logs.

              Possible values:

              - **true** - Empty logs are not sent.
              - **false** - Empty logs are sent.

          s3_aws_region: Amazon AWS region.

          s3_bucket_location: Location of S3 storage.

              Restrictions:

              - Maximum of 255 symbols.
              - Latin letters (A-Z, a-z), digits (0-9), dots, colons, dashes, and underscores
                (.:\\__-).

          s3_host_bucket: S3 bucket hostname.

              Restrictions:

              - Maximum of 255 symbols.
              - Latin letters (A-Z, a-z,) digits (0-9,) dots, colons, dashes, and underscores.
              - Required if "`s3_type`": other.

          sftp_key_passphrase: Passphrase for SFTP private key.

              Restrictions:

              - Should be set if private key encoded with passphrase.
              - Should be empty if "`sftp_password`" is set.

          sftp_prepend_folder: Name of the SFTP prepend folder for log delivery.

              **Null** is allowed.

          sftp_private_key: Private key for SFTP authorization.

              Possible values:

              - **RSA**
              - **ED25519**

              It should be empty if "`sftp_password`" is set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/cdn/raw_log_settings"
            if self._client._base_url_overridden
            else "https://api.gcore.com//cdn/raw_log_settings",
            body=await async_maybe_transform(
                {
                    "all_resources_bucket": all_resources_bucket,
                    "all_resources_folder": all_resources_folder,
                    "folders": folders,
                    "for_all_resources": for_all_resources,
                    "ftp_hostname": ftp_hostname,
                    "ftp_login": ftp_login,
                    "ftp_password": ftp_password,
                    "s3_access_key_id": s3_access_key_id,
                    "s3_hostname": s3_hostname,
                    "s3_secret_key": s3_secret_key,
                    "s3_type": s3_type,
                    "sftp_hostname": sftp_hostname,
                    "sftp_login": sftp_login,
                    "sftp_password": sftp_password,
                    "storage_type": storage_type,
                    "archive_size_mb": archive_size_mb,
                    "enabled": enabled,
                    "ftp_prepend_folder": ftp_prepend_folder,
                    "ignore_empty_logs": ignore_empty_logs,
                    "s3_aws_region": s3_aws_region,
                    "s3_bucket_location": s3_bucket_location,
                    "s3_host_bucket": s3_host_bucket,
                    "sftp_key_passphrase": sftp_key_passphrase,
                    "sftp_prepend_folder": sftp_prepend_folder,
                    "sftp_private_key": sftp_private_key,
                },
                setting_create_params.SettingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def update(
        self,
        *,
        all_resources_bucket: str,
        all_resources_folder: str,
        folders: Iterable[setting_update_params.Folder],
        for_all_resources: bool,
        ftp_hostname: str,
        ftp_login: str,
        ftp_password: str,
        s3_access_key_id: str,
        s3_hostname: str,
        s3_secret_key: str,
        s3_type: str,
        sftp_hostname: str,
        sftp_login: str,
        sftp_password: str,
        storage_type: str,
        archive_size_mb: Optional[int] | Omit = omit,
        enabled: bool | Omit = omit,
        ftp_prepend_folder: str | Omit = omit,
        ignore_empty_logs: bool | Omit = omit,
        s3_aws_region: int | Omit = omit,
        s3_bucket_location: str | Omit = omit,
        s3_host_bucket: str | Omit = omit,
        sftp_key_passphrase: str | Omit = omit,
        sftp_prepend_folder: str | Omit = omit,
        sftp_private_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        PATCH method is not allowed.

        Args:
          all_resources_bucket: Name of the S3 bucket to which logs for all CDN resources are delivered.

          all_resources_folder:
              Parameter meaning depends on the value of the "`storage_type`" value:

              - If "`storage_type`": s3 - Name of the S3 bucket sub-folder to which logs for
                all CDN resources are delivered.
              - If "`storage_type`": ftp/sftp - Name of the folder (or path) to which logs for
                all CDN resources are delivered.

          folders: List of folders/buckets for receiving CDN resources logs.

          for_all_resources: Defines whether logs of all CDN resources are delivered to one folder/bucket or
              to separate ones.

              Possible values:

              - **true** - Logs of all CDN resources are delivered to one folder/bucket.
              - **false** - Logs of different CDN resources are delivered to separate
                folders/buckets.

          ftp_hostname: FTP storage hostname.

          ftp_login: FTP storage login.

          ftp_password: FTP storage password.

          s3_access_key_id: Access key ID for the S3 account.

              Access Key ID is 20 alpha-numeric characters like 022QF06E7MXBSH9DHM02

          s3_hostname: S3 storage hostname.

              It is required if "`s3_type`": other.

          s3_secret_key: Secret access key for the S3 account.

              Secret Access Key is 20-50 alpha-numeric-slash-plus characters like
              kWcrlUX5JEDGM/LtmEENI/aVmYvHNif5zB+d9+ct

          s3_type: Storage type compatible with S3.

              Possible values:

              - **amazon** – AWS S3 storage.
              - **other** – Other (not AWS) S3 compatible storage.

          sftp_hostname: SFTP storage hostname.

          sftp_login: SFTP storage login.

          sftp_password: SFTP storage password.

              It should be empty if "`sftp_private_key`" is set.

          storage_type: Storage type.

              Possible values:

              - **ftp**
              - **sftp**
              - **s3**

          archive_size_mb: The size of a single piece of the archive in MB. In case of **null** value logs
              are delivered without slicing.

          enabled: Enables or disables a log forwarding feature.

              Possible values:

              - **true** - log forwarding feature is active.
              - **false** - log forwarding feature is deactivated.

          ftp_prepend_folder: Name of the FTP prepend folder for log delivery.

              **Null** is allowed.

          ignore_empty_logs: Enables or disables the forwarding of empty logs.

              Possible values:

              - **true** - Empty logs are not sent.
              - **false** - Empty logs are sent.

          s3_aws_region: Amazon AWS region.

          s3_bucket_location: Location of S3 storage.

              Restrictions:

              - Maximum of 255 symbols.
              - Latin letters (A-Z, a-z), digits (0-9), dots, colons, dashes, and underscores
                (.:\\__-).

          s3_host_bucket: S3 bucket hostname.

              Restrictions:

              - Maximum of 255 symbols.
              - Latin letters (A-Z, a-z,) digits (0-9,) dots, colons, dashes, and underscores.
              - Required if "`s3_type`": other.

          sftp_key_passphrase: Passphrase for SFTP private key.

              Restrictions:

              - Should be set if private key encoded with passphrase.
              - Should be empty if "`sftp_password`" is set.

          sftp_prepend_folder: Name of the SFTP prepend folder for log delivery.

              **Null** is allowed.

          sftp_private_key: Private key for SFTP authorization.

              Possible values:

              - **RSA**
              - **ED25519**

              It should be empty if "`sftp_password`" is set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            "/cdn/raw_log_settings"
            if self._client._base_url_overridden
            else "https://api.gcore.com//cdn/raw_log_settings",
            body=await async_maybe_transform(
                {
                    "all_resources_bucket": all_resources_bucket,
                    "all_resources_folder": all_resources_folder,
                    "folders": folders,
                    "for_all_resources": for_all_resources,
                    "ftp_hostname": ftp_hostname,
                    "ftp_login": ftp_login,
                    "ftp_password": ftp_password,
                    "s3_access_key_id": s3_access_key_id,
                    "s3_hostname": s3_hostname,
                    "s3_secret_key": s3_secret_key,
                    "s3_type": s3_type,
                    "sftp_hostname": sftp_hostname,
                    "sftp_login": sftp_login,
                    "sftp_password": sftp_password,
                    "storage_type": storage_type,
                    "archive_size_mb": archive_size_mb,
                    "enabled": enabled,
                    "ftp_prepend_folder": ftp_prepend_folder,
                    "ignore_empty_logs": ignore_empty_logs,
                    "s3_aws_region": s3_aws_region,
                    "s3_bucket_location": s3_bucket_location,
                    "s3_host_bucket": s3_host_bucket,
                    "sftp_key_passphrase": sftp_key_passphrase,
                    "sftp_prepend_folder": sftp_prepend_folder,
                    "sftp_private_key": sftp_private_key,
                },
                setting_update_params.SettingUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def delete(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete the raw logs delivery configuration from the system permanently.

        Notes:

        - **Deactivation Requirement**: Set the `enabled` attribute to `false` before
          deletion.
        - **Irreversibility**: This action is irreversible. Once deleted, the raw logs
          delivery configuration cannot be recovered.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            "/cdn/raw_log_settings"
            if self._client._base_url_overridden
            else "https://api.gcore.com//cdn/raw_log_settings",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogSettings:
        """Get information about raw logs feature settings."""
        return await self._get(
            "/cdn/raw_log_settings"
            if self._client._base_url_overridden
            else "https://api.gcore.com//cdn/raw_log_settings",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogSettings,
        )


class SettingsResourceWithRawResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

        self.create = to_raw_response_wrapper(
            settings.create,
        )
        self.update = to_raw_response_wrapper(
            settings.update,
        )
        self.delete = to_raw_response_wrapper(
            settings.delete,
        )
        self.get = to_raw_response_wrapper(
            settings.get,
        )


class AsyncSettingsResourceWithRawResponse:
    def __init__(self, settings: AsyncSettingsResource) -> None:
        self._settings = settings

        self.create = async_to_raw_response_wrapper(
            settings.create,
        )
        self.update = async_to_raw_response_wrapper(
            settings.update,
        )
        self.delete = async_to_raw_response_wrapper(
            settings.delete,
        )
        self.get = async_to_raw_response_wrapper(
            settings.get,
        )


class SettingsResourceWithStreamingResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

        self.create = to_streamed_response_wrapper(
            settings.create,
        )
        self.update = to_streamed_response_wrapper(
            settings.update,
        )
        self.delete = to_streamed_response_wrapper(
            settings.delete,
        )
        self.get = to_streamed_response_wrapper(
            settings.get,
        )


class AsyncSettingsResourceWithStreamingResponse:
    def __init__(self, settings: AsyncSettingsResource) -> None:
        self._settings = settings

        self.create = async_to_streamed_response_wrapper(
            settings.create,
        )
        self.update = async_to_streamed_response_wrapper(
            settings.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            settings.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            settings.get,
        )
