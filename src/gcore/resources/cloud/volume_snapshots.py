# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.cloud import volume_snapshot_create_params, volume_snapshot_update_params
from ..._base_client import make_request_options
from ...types.cloud.snapshot import Snapshot
from ...types.cloud.task_id_list import TaskIDList
from ...types.cloud.tag_update_map_param import TagUpdateMapParam

__all__ = ["VolumeSnapshotsResource", "AsyncVolumeSnapshotsResource"]


class VolumeSnapshotsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VolumeSnapshotsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return VolumeSnapshotsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VolumeSnapshotsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return VolumeSnapshotsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        volume_id: str,
        description: str | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Create a new snapshot from a volume.

        Args:
          name: Snapshot name

          volume_id: Volume ID to make snapshot of

          description: Snapshot description

          tags: Key-value tags to associate with the resource. A tag is a key-value pair that
              can be associated with a resource, enabling efficient filtering and grouping for
              better organization and management. Both tag keys and values have a maximum
              length of 255 characters. Some tags are read-only and cannot be modified by the
              user. Tags are also integrated with cost reports, allowing cost data to be
              filtered based on tag keys or values.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return self._post(
            f"/cloud/v1/snapshots/{project_id}/{region_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "volume_id": volume_id,
                    "description": description,
                    "tags": tags,
                },
                volume_snapshot_create_params.VolumeSnapshotCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def update(
        self,
        snapshot_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str | Omit = omit,
        tags: Optional[TagUpdateMapParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Snapshot:
        """
        Rename snapshot or update tags.

        Args:
          project_id: Project ID

          region_id: Region ID

          snapshot_id: Unique identifier of the snapshot

          name: Display name for the snapshot (3-63 chars). Used in customer portal and API.
              Does not affect snapshot data.

          tags: Update key-value tags using JSON Merge Patch semantics (RFC 7386). Provide
              key-value pairs to add or update tags. Set tag values to `null` to remove tags.
              Unspecified tags remain unchanged. Read-only tags are always preserved and
              cannot be modified.

              **Examples:**

              - **Add/update tags:**
                `{'tags': {'environment': 'production', 'team': 'backend'}}` adds new tags or
                updates existing ones.
              - **Delete tags:** `{'tags': {'old_tag': null}}` removes specific tags.
              - **Remove all tags:** `{'tags': null}` removes all user-managed tags (read-only
                tags are preserved).
              - **Partial update:** `{'tags': {'environment': 'staging'}}` only updates
                specified tags.
              - **Mixed operations:**
                `{'tags': {'environment': 'production', 'cost_center': 'engineering', 'deprecated_tag': null}}`
                adds/updates 'environment' and 'cost_center' while removing 'deprecated_tag',
                preserving other existing tags.
              - **Replace all:** first delete existing tags with null values, then add new
                ones in the same request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not snapshot_id:
            raise ValueError(f"Expected a non-empty value for `snapshot_id` but received {snapshot_id!r}")
        return self._patch(
            f"/cloud/v1/snapshots/{project_id}/{region_id}/{snapshot_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "tags": tags,
                },
                volume_snapshot_update_params.VolumeSnapshotUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Snapshot,
        )

    def delete(
        self,
        snapshot_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Delete a specific snapshot.

        Args:
          project_id: Project ID

          region_id: Region ID

          snapshot_id: Unique identifier of the snapshot

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not snapshot_id:
            raise ValueError(f"Expected a non-empty value for `snapshot_id` but received {snapshot_id!r}")
        return self._delete(
            f"/cloud/v1/snapshots/{project_id}/{region_id}/{snapshot_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def get(
        self,
        snapshot_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Snapshot:
        """
        Get detailed information about a specific snapshot.

        Args:
          project_id: Project ID

          region_id: Region ID

          snapshot_id: Unique identifier of the snapshot

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not snapshot_id:
            raise ValueError(f"Expected a non-empty value for `snapshot_id` but received {snapshot_id!r}")
        return self._get(
            f"/cloud/v1/snapshots/{project_id}/{region_id}/{snapshot_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Snapshot,
        )


class AsyncVolumeSnapshotsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVolumeSnapshotsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVolumeSnapshotsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVolumeSnapshotsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncVolumeSnapshotsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        volume_id: str,
        description: str | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Create a new snapshot from a volume.

        Args:
          name: Snapshot name

          volume_id: Volume ID to make snapshot of

          description: Snapshot description

          tags: Key-value tags to associate with the resource. A tag is a key-value pair that
              can be associated with a resource, enabling efficient filtering and grouping for
              better organization and management. Both tag keys and values have a maximum
              length of 255 characters. Some tags are read-only and cannot be modified by the
              user. Tags are also integrated with cost reports, allowing cost data to be
              filtered based on tag keys or values.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return await self._post(
            f"/cloud/v1/snapshots/{project_id}/{region_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "volume_id": volume_id,
                    "description": description,
                    "tags": tags,
                },
                volume_snapshot_create_params.VolumeSnapshotCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def update(
        self,
        snapshot_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str | Omit = omit,
        tags: Optional[TagUpdateMapParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Snapshot:
        """
        Rename snapshot or update tags.

        Args:
          project_id: Project ID

          region_id: Region ID

          snapshot_id: Unique identifier of the snapshot

          name: Display name for the snapshot (3-63 chars). Used in customer portal and API.
              Does not affect snapshot data.

          tags: Update key-value tags using JSON Merge Patch semantics (RFC 7386). Provide
              key-value pairs to add or update tags. Set tag values to `null` to remove tags.
              Unspecified tags remain unchanged. Read-only tags are always preserved and
              cannot be modified.

              **Examples:**

              - **Add/update tags:**
                `{'tags': {'environment': 'production', 'team': 'backend'}}` adds new tags or
                updates existing ones.
              - **Delete tags:** `{'tags': {'old_tag': null}}` removes specific tags.
              - **Remove all tags:** `{'tags': null}` removes all user-managed tags (read-only
                tags are preserved).
              - **Partial update:** `{'tags': {'environment': 'staging'}}` only updates
                specified tags.
              - **Mixed operations:**
                `{'tags': {'environment': 'production', 'cost_center': 'engineering', 'deprecated_tag': null}}`
                adds/updates 'environment' and 'cost_center' while removing 'deprecated_tag',
                preserving other existing tags.
              - **Replace all:** first delete existing tags with null values, then add new
                ones in the same request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not snapshot_id:
            raise ValueError(f"Expected a non-empty value for `snapshot_id` but received {snapshot_id!r}")
        return await self._patch(
            f"/cloud/v1/snapshots/{project_id}/{region_id}/{snapshot_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "tags": tags,
                },
                volume_snapshot_update_params.VolumeSnapshotUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Snapshot,
        )

    async def delete(
        self,
        snapshot_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskIDList:
        """
        Delete a specific snapshot.

        Args:
          project_id: Project ID

          region_id: Region ID

          snapshot_id: Unique identifier of the snapshot

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not snapshot_id:
            raise ValueError(f"Expected a non-empty value for `snapshot_id` but received {snapshot_id!r}")
        return await self._delete(
            f"/cloud/v1/snapshots/{project_id}/{region_id}/{snapshot_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def get(
        self,
        snapshot_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Snapshot:
        """
        Get detailed information about a specific snapshot.

        Args:
          project_id: Project ID

          region_id: Region ID

          snapshot_id: Unique identifier of the snapshot

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not snapshot_id:
            raise ValueError(f"Expected a non-empty value for `snapshot_id` but received {snapshot_id!r}")
        return await self._get(
            f"/cloud/v1/snapshots/{project_id}/{region_id}/{snapshot_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Snapshot,
        )


class VolumeSnapshotsResourceWithRawResponse:
    def __init__(self, volume_snapshots: VolumeSnapshotsResource) -> None:
        self._volume_snapshots = volume_snapshots

        self.create = to_raw_response_wrapper(
            volume_snapshots.create,
        )
        self.update = to_raw_response_wrapper(
            volume_snapshots.update,
        )
        self.delete = to_raw_response_wrapper(
            volume_snapshots.delete,
        )
        self.get = to_raw_response_wrapper(
            volume_snapshots.get,
        )


class AsyncVolumeSnapshotsResourceWithRawResponse:
    def __init__(self, volume_snapshots: AsyncVolumeSnapshotsResource) -> None:
        self._volume_snapshots = volume_snapshots

        self.create = async_to_raw_response_wrapper(
            volume_snapshots.create,
        )
        self.update = async_to_raw_response_wrapper(
            volume_snapshots.update,
        )
        self.delete = async_to_raw_response_wrapper(
            volume_snapshots.delete,
        )
        self.get = async_to_raw_response_wrapper(
            volume_snapshots.get,
        )


class VolumeSnapshotsResourceWithStreamingResponse:
    def __init__(self, volume_snapshots: VolumeSnapshotsResource) -> None:
        self._volume_snapshots = volume_snapshots

        self.create = to_streamed_response_wrapper(
            volume_snapshots.create,
        )
        self.update = to_streamed_response_wrapper(
            volume_snapshots.update,
        )
        self.delete = to_streamed_response_wrapper(
            volume_snapshots.delete,
        )
        self.get = to_streamed_response_wrapper(
            volume_snapshots.get,
        )


class AsyncVolumeSnapshotsResourceWithStreamingResponse:
    def __init__(self, volume_snapshots: AsyncVolumeSnapshotsResource) -> None:
        self._volume_snapshots = volume_snapshots

        self.create = async_to_streamed_response_wrapper(
            volume_snapshots.create,
        )
        self.update = async_to_streamed_response_wrapper(
            volume_snapshots.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            volume_snapshots.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            volume_snapshots.get,
        )
