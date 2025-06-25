# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, overload

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import required_args, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncOffsetPage, AsyncOffsetPage
from ...types.cloud import (
    volume_list_params,
    volume_create_params,
    volume_delete_params,
    volume_resize_params,
    volume_update_params,
    volume_change_type_params,
    volume_attach_to_instance_params,
    volume_detach_from_instance_params,
)
from ..._base_client import AsyncPaginator, make_request_options
from ...types.cloud.volume import Volume
from ...types.cloud.task_id_list import TaskIDList
from ...types.cloud.tag_update_map_param import TagUpdateMapParam

__all__ = ["VolumesResource", "AsyncVolumesResource"]


class VolumesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VolumesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return VolumesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VolumesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return VolumesResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        image_id: str,
        name: str,
        size: int,
        source: Literal["image"],
        attachment_tag: str | NotGiven = NOT_GIVEN,
        instance_id_to_attach_to: str | NotGiven = NOT_GIVEN,
        lifecycle_policy_ids: Iterable[int] | NotGiven = NOT_GIVEN,
        tags: TagUpdateMapParam | NotGiven = NOT_GIVEN,
        type_name: Literal["cold", "ssd_hiiops", "ssd_local", "ssd_lowlatency", "standard", "ultra"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """Create a new volume in the project and region.

        The volume can be created from
        scratch, from an image, or from a snapshot. Optionally attach the volume to an
        instance during creation.

        Args:
          project_id: Project ID

          region_id: Region ID

          image_id: Image ID

          name: Volume name

          size: Volume size in GiB

          source: Volume source type

          attachment_tag: Block device attachment tag (not exposed in the user tags). Only used in
              conjunction with `instance_id_to_attach_to`

          instance_id_to_attach_to: `instance_id` to attach newly-created volume to

          lifecycle_policy_ids: List of lifecycle policy IDs (snapshot creation schedules) to associate with the
              volume

          tags: Key-value tags to associate with the resource. A tag is a key-value pair that
              can be associated with a resource, enabling efficient filtering and grouping for
              better organization and management. Some tags are read-only and cannot be
              modified by the user. Tags are also integrated with cost reports, allowing cost
              data to be filtered based on tag keys or values.

          type_name: Volume type. Defaults to `standard`. If not specified for source `snapshot`,
              volume type will be derived from the snapshot volume.

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
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        snapshot_id: str,
        source: Literal["snapshot"],
        attachment_tag: str | NotGiven = NOT_GIVEN,
        instance_id_to_attach_to: str | NotGiven = NOT_GIVEN,
        lifecycle_policy_ids: Iterable[int] | NotGiven = NOT_GIVEN,
        size: int | NotGiven = NOT_GIVEN,
        tags: TagUpdateMapParam | NotGiven = NOT_GIVEN,
        type_name: Literal["cold", "ssd_hiiops", "ssd_local", "ssd_lowlatency", "standard", "ultra"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """Create a new volume in the project and region.

        The volume can be created from
        scratch, from an image, or from a snapshot. Optionally attach the volume to an
        instance during creation.

        Args:
          project_id: Project ID

          region_id: Region ID

          name: Volume name

          snapshot_id: Snapshot ID

          source: Volume source type

          attachment_tag: Block device attachment tag (not exposed in the user tags). Only used in
              conjunction with `instance_id_to_attach_to`

          instance_id_to_attach_to: `instance_id` to attach newly-created volume to

          lifecycle_policy_ids: List of lifecycle policy IDs (snapshot creation schedules) to associate with the
              volume

          size: Volume size in GiB. If specified, value must be equal to respective snapshot
              size

          tags: Key-value tags to associate with the resource. A tag is a key-value pair that
              can be associated with a resource, enabling efficient filtering and grouping for
              better organization and management. Some tags are read-only and cannot be
              modified by the user. Tags are also integrated with cost reports, allowing cost
              data to be filtered based on tag keys or values.

          type_name: Volume type. Defaults to `standard`. If not specified for source `snapshot`,
              volume type will be derived from the snapshot volume.

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
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        size: int,
        source: Literal["new-volume"],
        attachment_tag: str | NotGiven = NOT_GIVEN,
        instance_id_to_attach_to: str | NotGiven = NOT_GIVEN,
        lifecycle_policy_ids: Iterable[int] | NotGiven = NOT_GIVEN,
        tags: TagUpdateMapParam | NotGiven = NOT_GIVEN,
        type_name: Literal["cold", "ssd_hiiops", "ssd_local", "ssd_lowlatency", "standard", "ultra"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """Create a new volume in the project and region.

        The volume can be created from
        scratch, from an image, or from a snapshot. Optionally attach the volume to an
        instance during creation.

        Args:
          project_id: Project ID

          region_id: Region ID

          name: Volume name

          size: Volume size in GiB

          source: Volume source type

          attachment_tag: Block device attachment tag (not exposed in the user tags). Only used in
              conjunction with `instance_id_to_attach_to`

          instance_id_to_attach_to: `instance_id` to attach newly-created volume to

          lifecycle_policy_ids: List of lifecycle policy IDs (snapshot creation schedules) to associate with the
              volume

          tags: Key-value tags to associate with the resource. A tag is a key-value pair that
              can be associated with a resource, enabling efficient filtering and grouping for
              better organization and management. Some tags are read-only and cannot be
              modified by the user. Tags are also integrated with cost reports, allowing cost
              data to be filtered based on tag keys or values.

          type_name: Volume type. Defaults to `standard`. If not specified for source `snapshot`,
              volume type will be derived from the snapshot volume.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["image_id", "name", "size", "source"], ["name", "snapshot_id", "source"], ["name", "size", "source"]
    )
    def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        image_id: str | NotGiven = NOT_GIVEN,
        name: str,
        size: int | NotGiven = NOT_GIVEN,
        source: Literal["image"] | Literal["snapshot"] | Literal["new-volume"],
        attachment_tag: str | NotGiven = NOT_GIVEN,
        instance_id_to_attach_to: str | NotGiven = NOT_GIVEN,
        lifecycle_policy_ids: Iterable[int] | NotGiven = NOT_GIVEN,
        tags: TagUpdateMapParam | NotGiven = NOT_GIVEN,
        type_name: Literal["cold", "ssd_hiiops", "ssd_local", "ssd_lowlatency", "standard", "ultra"]
        | NotGiven = NOT_GIVEN,
        snapshot_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return self._post(
            f"/cloud/v1/volumes/{project_id}/{region_id}",
            body=maybe_transform(
                {
                    "image_id": image_id,
                    "name": name,
                    "size": size,
                    "source": source,
                    "attachment_tag": attachment_tag,
                    "instance_id_to_attach_to": instance_id_to_attach_to,
                    "lifecycle_policy_ids": lifecycle_policy_ids,
                    "tags": tags,
                    "type_name": type_name,
                    "snapshot_id": snapshot_id,
                },
                volume_create_params.VolumeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def update(
        self,
        volume_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str | NotGiven = NOT_GIVEN,
        tags: Optional[TagUpdateMapParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Volume:
        """
        Rename a volume or update tags

        Args:
          project_id: Project ID

          region_id: Region ID

          volume_id: Volume ID

          name: Name

          tags: Update key-value tags using JSON Merge Patch semantics (RFC 7386). Provide
              key-value pairs to add or update tags. Set tag values to `null` to remove tags.
              Unspecified tags remain unchanged. Read-only tags are always preserved and
              cannot be modified. **Examples:**

              - **Add/update tags:**
                `{'tags': {'environment': 'production', 'team': 'backend'}}` adds new tags or
                updates existing ones.
              - **Delete tags:** `{'tags': {'`old_tag`': null}}` removes specific tags.
              - **Remove all tags:** `{'tags': null}` removes all user-managed tags (read-only
                tags are preserved).
              - **Partial update:** `{'tags': {'environment': 'staging'}}` only updates
                specified tags.
              - **Mixed operations:**
                `{'tags': {'environment': 'production', '`cost_center`': 'engineering', '`deprecated_tag`': null}}`
                adds/updates 'environment' and '`cost_center`' while removing
                '`deprecated_tag`', preserving other existing tags.
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
        if not volume_id:
            raise ValueError(f"Expected a non-empty value for `volume_id` but received {volume_id!r}")
        return self._patch(
            f"/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "tags": tags,
                },
                volume_update_params.VolumeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Volume,
        )

    def list(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        bootable: bool | NotGiven = NOT_GIVEN,
        cluster_id: str | NotGiven = NOT_GIVEN,
        has_attachments: bool | NotGiven = NOT_GIVEN,
        id_part: str | NotGiven = NOT_GIVEN,
        instance_id: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name_part: str | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        tag_key: List[str] | NotGiven = NOT_GIVEN,
        tag_key_value: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[Volume]:
        """Retrieve a list of volumes in the project and region.

        The list can be filtered
        by various parameters like bootable status, metadata/tags, attachments, instance
        ID, name, and ID.

        Args:
          project_id: Project ID

          region_id: Region ID

          bootable: Filter by bootable field

          cluster_id: Filter volumes by k8s cluster ID

          has_attachments: Filter by the presence of attachments

          id_part: Filter the volume list result by the ID part of the volume

          instance_id: Filter volumes by instance ID

          limit: Optional. Limit the number of returned items

          name_part: Filter volumes by `name_part` inclusion in volume name.Any substring can be used
              and volumes will be returned with names containing the substring.

          offset: Optional. Offset value is used to exclude the first set of records from the
              result

          tag_key: Optional. Filter by tag keys. ?`tag_key`=key1&`tag_key`=key2

          tag_key_value: Optional. Filter by tag key-value pairs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return self._get_api_list(
            f"/cloud/v1/volumes/{project_id}/{region_id}",
            page=SyncOffsetPage[Volume],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "bootable": bootable,
                        "cluster_id": cluster_id,
                        "has_attachments": has_attachments,
                        "id_part": id_part,
                        "instance_id": instance_id,
                        "limit": limit,
                        "name_part": name_part,
                        "offset": offset,
                        "tag_key": tag_key,
                        "tag_key_value": tag_key_value,
                    },
                    volume_list_params.VolumeListParams,
                ),
            ),
            model=Volume,
        )

    def delete(
        self,
        volume_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        snapshots: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """Delete a volume and all its snapshots.

        The volume must be in an available state
        to be deleted.

        Args:
          project_id: Project ID

          region_id: Region ID

          volume_id: Volume ID

          snapshots: Comma separated list of snapshot IDs to be deleted with the volume.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not volume_id:
            raise ValueError(f"Expected a non-empty value for `volume_id` but received {volume_id!r}")
        return self._delete(
            f"/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"snapshots": snapshots}, volume_delete_params.VolumeDeleteParams),
            ),
            cast_to=TaskIDList,
        )

    def attach_to_instance(
        self,
        volume_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        instance_id: str,
        attachment_tag: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """Attach the volume to instance.

        Note: ultra volume can only be attached to an
        instance with shared flavor

        Args:
          project_id: Project ID

          region_id: Region ID

          volume_id: Volume ID

          instance_id: Instance ID.

          attachment_tag: Block device attachment tag (not exposed in the normal tags).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not volume_id:
            raise ValueError(f"Expected a non-empty value for `volume_id` but received {volume_id!r}")
        return self._post(
            f"/cloud/v2/volumes/{project_id}/{region_id}/{volume_id}/attach",
            body=maybe_transform(
                {
                    "instance_id": instance_id,
                    "attachment_tag": attachment_tag,
                },
                volume_attach_to_instance_params.VolumeAttachToInstanceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def change_type(
        self,
        volume_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        volume_type: Literal["ssd_hiiops", "standard"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Volume:
        """Change the type of a volume.

        The volume must not have any snapshots to change
        its type.

        Args:
          project_id: Project ID

          region_id: Region ID

          volume_id: Volume ID

          volume_type: New volume type name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not volume_id:
            raise ValueError(f"Expected a non-empty value for `volume_id` but received {volume_id!r}")
        return self._post(
            f"/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}/retype",
            body=maybe_transform({"volume_type": volume_type}, volume_change_type_params.VolumeChangeTypeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Volume,
        )

    def detach_from_instance(
        self,
        volume_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        instance_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Detach the volume from instance

        Args:
          project_id: Project ID

          region_id: Region ID

          volume_id: Volume ID

          instance_id: Instance ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not volume_id:
            raise ValueError(f"Expected a non-empty value for `volume_id` but received {volume_id!r}")
        return self._post(
            f"/cloud/v2/volumes/{project_id}/{region_id}/{volume_id}/detach",
            body=maybe_transform(
                {"instance_id": instance_id}, volume_detach_from_instance_params.VolumeDetachFromInstanceParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def get(
        self,
        volume_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Volume:
        """
        Retrieve detailed information about a specific volume.

        Args:
          project_id: Project ID

          region_id: Region ID

          volume_id: Volume ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not volume_id:
            raise ValueError(f"Expected a non-empty value for `volume_id` but received {volume_id!r}")
        return self._get(
            f"/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Volume,
        )

    def resize(
        self,
        volume_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        size: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """Increase the size of a volume.

        The new size must be greater than the current
        size.

        Args:
          project_id: Project ID

          region_id: Region ID

          volume_id: Volume ID

          size: New volume size in GiB

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not volume_id:
            raise ValueError(f"Expected a non-empty value for `volume_id` but received {volume_id!r}")
        return self._post(
            f"/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}/extend",
            body=maybe_transform({"size": size}, volume_resize_params.VolumeResizeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def revert_to_last_snapshot(
        self,
        volume_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Revert a volume to its last snapshot.

        The volume must be in an available state
        to be reverted.

        Args:
          project_id: Project ID

          region_id: Region ID

          volume_id: Volume ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not volume_id:
            raise ValueError(f"Expected a non-empty value for `volume_id` but received {volume_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}/revert",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncVolumesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVolumesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVolumesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVolumesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncVolumesResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        image_id: str,
        name: str,
        size: int,
        source: Literal["image"],
        attachment_tag: str | NotGiven = NOT_GIVEN,
        instance_id_to_attach_to: str | NotGiven = NOT_GIVEN,
        lifecycle_policy_ids: Iterable[int] | NotGiven = NOT_GIVEN,
        tags: TagUpdateMapParam | NotGiven = NOT_GIVEN,
        type_name: Literal["cold", "ssd_hiiops", "ssd_local", "ssd_lowlatency", "standard", "ultra"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """Create a new volume in the project and region.

        The volume can be created from
        scratch, from an image, or from a snapshot. Optionally attach the volume to an
        instance during creation.

        Args:
          project_id: Project ID

          region_id: Region ID

          image_id: Image ID

          name: Volume name

          size: Volume size in GiB

          source: Volume source type

          attachment_tag: Block device attachment tag (not exposed in the user tags). Only used in
              conjunction with `instance_id_to_attach_to`

          instance_id_to_attach_to: `instance_id` to attach newly-created volume to

          lifecycle_policy_ids: List of lifecycle policy IDs (snapshot creation schedules) to associate with the
              volume

          tags: Key-value tags to associate with the resource. A tag is a key-value pair that
              can be associated with a resource, enabling efficient filtering and grouping for
              better organization and management. Some tags are read-only and cannot be
              modified by the user. Tags are also integrated with cost reports, allowing cost
              data to be filtered based on tag keys or values.

          type_name: Volume type. Defaults to `standard`. If not specified for source `snapshot`,
              volume type will be derived from the snapshot volume.

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
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        snapshot_id: str,
        source: Literal["snapshot"],
        attachment_tag: str | NotGiven = NOT_GIVEN,
        instance_id_to_attach_to: str | NotGiven = NOT_GIVEN,
        lifecycle_policy_ids: Iterable[int] | NotGiven = NOT_GIVEN,
        size: int | NotGiven = NOT_GIVEN,
        tags: TagUpdateMapParam | NotGiven = NOT_GIVEN,
        type_name: Literal["cold", "ssd_hiiops", "ssd_local", "ssd_lowlatency", "standard", "ultra"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """Create a new volume in the project and region.

        The volume can be created from
        scratch, from an image, or from a snapshot. Optionally attach the volume to an
        instance during creation.

        Args:
          project_id: Project ID

          region_id: Region ID

          name: Volume name

          snapshot_id: Snapshot ID

          source: Volume source type

          attachment_tag: Block device attachment tag (not exposed in the user tags). Only used in
              conjunction with `instance_id_to_attach_to`

          instance_id_to_attach_to: `instance_id` to attach newly-created volume to

          lifecycle_policy_ids: List of lifecycle policy IDs (snapshot creation schedules) to associate with the
              volume

          size: Volume size in GiB. If specified, value must be equal to respective snapshot
              size

          tags: Key-value tags to associate with the resource. A tag is a key-value pair that
              can be associated with a resource, enabling efficient filtering and grouping for
              better organization and management. Some tags are read-only and cannot be
              modified by the user. Tags are also integrated with cost reports, allowing cost
              data to be filtered based on tag keys or values.

          type_name: Volume type. Defaults to `standard`. If not specified for source `snapshot`,
              volume type will be derived from the snapshot volume.

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
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        size: int,
        source: Literal["new-volume"],
        attachment_tag: str | NotGiven = NOT_GIVEN,
        instance_id_to_attach_to: str | NotGiven = NOT_GIVEN,
        lifecycle_policy_ids: Iterable[int] | NotGiven = NOT_GIVEN,
        tags: TagUpdateMapParam | NotGiven = NOT_GIVEN,
        type_name: Literal["cold", "ssd_hiiops", "ssd_local", "ssd_lowlatency", "standard", "ultra"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """Create a new volume in the project and region.

        The volume can be created from
        scratch, from an image, or from a snapshot. Optionally attach the volume to an
        instance during creation.

        Args:
          project_id: Project ID

          region_id: Region ID

          name: Volume name

          size: Volume size in GiB

          source: Volume source type

          attachment_tag: Block device attachment tag (not exposed in the user tags). Only used in
              conjunction with `instance_id_to_attach_to`

          instance_id_to_attach_to: `instance_id` to attach newly-created volume to

          lifecycle_policy_ids: List of lifecycle policy IDs (snapshot creation schedules) to associate with the
              volume

          tags: Key-value tags to associate with the resource. A tag is a key-value pair that
              can be associated with a resource, enabling efficient filtering and grouping for
              better organization and management. Some tags are read-only and cannot be
              modified by the user. Tags are also integrated with cost reports, allowing cost
              data to be filtered based on tag keys or values.

          type_name: Volume type. Defaults to `standard`. If not specified for source `snapshot`,
              volume type will be derived from the snapshot volume.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["image_id", "name", "size", "source"], ["name", "snapshot_id", "source"], ["name", "size", "source"]
    )
    async def create(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        image_id: str | NotGiven = NOT_GIVEN,
        name: str,
        size: int | NotGiven = NOT_GIVEN,
        source: Literal["image"] | Literal["snapshot"] | Literal["new-volume"],
        attachment_tag: str | NotGiven = NOT_GIVEN,
        instance_id_to_attach_to: str | NotGiven = NOT_GIVEN,
        lifecycle_policy_ids: Iterable[int] | NotGiven = NOT_GIVEN,
        tags: TagUpdateMapParam | NotGiven = NOT_GIVEN,
        type_name: Literal["cold", "ssd_hiiops", "ssd_local", "ssd_lowlatency", "standard", "ultra"]
        | NotGiven = NOT_GIVEN,
        snapshot_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return await self._post(
            f"/cloud/v1/volumes/{project_id}/{region_id}",
            body=await async_maybe_transform(
                {
                    "image_id": image_id,
                    "name": name,
                    "size": size,
                    "source": source,
                    "attachment_tag": attachment_tag,
                    "instance_id_to_attach_to": instance_id_to_attach_to,
                    "lifecycle_policy_ids": lifecycle_policy_ids,
                    "tags": tags,
                    "type_name": type_name,
                    "snapshot_id": snapshot_id,
                },
                volume_create_params.VolumeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def update(
        self,
        volume_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str | NotGiven = NOT_GIVEN,
        tags: Optional[TagUpdateMapParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Volume:
        """
        Rename a volume or update tags

        Args:
          project_id: Project ID

          region_id: Region ID

          volume_id: Volume ID

          name: Name

          tags: Update key-value tags using JSON Merge Patch semantics (RFC 7386). Provide
              key-value pairs to add or update tags. Set tag values to `null` to remove tags.
              Unspecified tags remain unchanged. Read-only tags are always preserved and
              cannot be modified. **Examples:**

              - **Add/update tags:**
                `{'tags': {'environment': 'production', 'team': 'backend'}}` adds new tags or
                updates existing ones.
              - **Delete tags:** `{'tags': {'`old_tag`': null}}` removes specific tags.
              - **Remove all tags:** `{'tags': null}` removes all user-managed tags (read-only
                tags are preserved).
              - **Partial update:** `{'tags': {'environment': 'staging'}}` only updates
                specified tags.
              - **Mixed operations:**
                `{'tags': {'environment': 'production', '`cost_center`': 'engineering', '`deprecated_tag`': null}}`
                adds/updates 'environment' and '`cost_center`' while removing
                '`deprecated_tag`', preserving other existing tags.
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
        if not volume_id:
            raise ValueError(f"Expected a non-empty value for `volume_id` but received {volume_id!r}")
        return await self._patch(
            f"/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "tags": tags,
                },
                volume_update_params.VolumeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Volume,
        )

    def list(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        bootable: bool | NotGiven = NOT_GIVEN,
        cluster_id: str | NotGiven = NOT_GIVEN,
        has_attachments: bool | NotGiven = NOT_GIVEN,
        id_part: str | NotGiven = NOT_GIVEN,
        instance_id: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name_part: str | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        tag_key: List[str] | NotGiven = NOT_GIVEN,
        tag_key_value: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Volume, AsyncOffsetPage[Volume]]:
        """Retrieve a list of volumes in the project and region.

        The list can be filtered
        by various parameters like bootable status, metadata/tags, attachments, instance
        ID, name, and ID.

        Args:
          project_id: Project ID

          region_id: Region ID

          bootable: Filter by bootable field

          cluster_id: Filter volumes by k8s cluster ID

          has_attachments: Filter by the presence of attachments

          id_part: Filter the volume list result by the ID part of the volume

          instance_id: Filter volumes by instance ID

          limit: Optional. Limit the number of returned items

          name_part: Filter volumes by `name_part` inclusion in volume name.Any substring can be used
              and volumes will be returned with names containing the substring.

          offset: Optional. Offset value is used to exclude the first set of records from the
              result

          tag_key: Optional. Filter by tag keys. ?`tag_key`=key1&`tag_key`=key2

          tag_key_value: Optional. Filter by tag key-value pairs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return self._get_api_list(
            f"/cloud/v1/volumes/{project_id}/{region_id}",
            page=AsyncOffsetPage[Volume],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "bootable": bootable,
                        "cluster_id": cluster_id,
                        "has_attachments": has_attachments,
                        "id_part": id_part,
                        "instance_id": instance_id,
                        "limit": limit,
                        "name_part": name_part,
                        "offset": offset,
                        "tag_key": tag_key,
                        "tag_key_value": tag_key_value,
                    },
                    volume_list_params.VolumeListParams,
                ),
            ),
            model=Volume,
        )

    async def delete(
        self,
        volume_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        snapshots: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """Delete a volume and all its snapshots.

        The volume must be in an available state
        to be deleted.

        Args:
          project_id: Project ID

          region_id: Region ID

          volume_id: Volume ID

          snapshots: Comma separated list of snapshot IDs to be deleted with the volume.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not volume_id:
            raise ValueError(f"Expected a non-empty value for `volume_id` but received {volume_id!r}")
        return await self._delete(
            f"/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"snapshots": snapshots}, volume_delete_params.VolumeDeleteParams),
            ),
            cast_to=TaskIDList,
        )

    async def attach_to_instance(
        self,
        volume_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        instance_id: str,
        attachment_tag: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """Attach the volume to instance.

        Note: ultra volume can only be attached to an
        instance with shared flavor

        Args:
          project_id: Project ID

          region_id: Region ID

          volume_id: Volume ID

          instance_id: Instance ID.

          attachment_tag: Block device attachment tag (not exposed in the normal tags).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not volume_id:
            raise ValueError(f"Expected a non-empty value for `volume_id` but received {volume_id!r}")
        return await self._post(
            f"/cloud/v2/volumes/{project_id}/{region_id}/{volume_id}/attach",
            body=await async_maybe_transform(
                {
                    "instance_id": instance_id,
                    "attachment_tag": attachment_tag,
                },
                volume_attach_to_instance_params.VolumeAttachToInstanceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def change_type(
        self,
        volume_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        volume_type: Literal["ssd_hiiops", "standard"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Volume:
        """Change the type of a volume.

        The volume must not have any snapshots to change
        its type.

        Args:
          project_id: Project ID

          region_id: Region ID

          volume_id: Volume ID

          volume_type: New volume type name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not volume_id:
            raise ValueError(f"Expected a non-empty value for `volume_id` but received {volume_id!r}")
        return await self._post(
            f"/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}/retype",
            body=await async_maybe_transform(
                {"volume_type": volume_type}, volume_change_type_params.VolumeChangeTypeParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Volume,
        )

    async def detach_from_instance(
        self,
        volume_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        instance_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Detach the volume from instance

        Args:
          project_id: Project ID

          region_id: Region ID

          volume_id: Volume ID

          instance_id: Instance ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not volume_id:
            raise ValueError(f"Expected a non-empty value for `volume_id` but received {volume_id!r}")
        return await self._post(
            f"/cloud/v2/volumes/{project_id}/{region_id}/{volume_id}/detach",
            body=await async_maybe_transform(
                {"instance_id": instance_id}, volume_detach_from_instance_params.VolumeDetachFromInstanceParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def get(
        self,
        volume_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Volume:
        """
        Retrieve detailed information about a specific volume.

        Args:
          project_id: Project ID

          region_id: Region ID

          volume_id: Volume ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not volume_id:
            raise ValueError(f"Expected a non-empty value for `volume_id` but received {volume_id!r}")
        return await self._get(
            f"/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Volume,
        )

    async def resize(
        self,
        volume_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        size: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """Increase the size of a volume.

        The new size must be greater than the current
        size.

        Args:
          project_id: Project ID

          region_id: Region ID

          volume_id: Volume ID

          size: New volume size in GiB

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not volume_id:
            raise ValueError(f"Expected a non-empty value for `volume_id` but received {volume_id!r}")
        return await self._post(
            f"/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}/extend",
            body=await async_maybe_transform({"size": size}, volume_resize_params.VolumeResizeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def revert_to_last_snapshot(
        self,
        volume_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Revert a volume to its last snapshot.

        The volume must be in an available state
        to be reverted.

        Args:
          project_id: Project ID

          region_id: Region ID

          volume_id: Volume ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not volume_id:
            raise ValueError(f"Expected a non-empty value for `volume_id` but received {volume_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}/revert",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class VolumesResourceWithRawResponse:
    def __init__(self, volumes: VolumesResource) -> None:
        self._volumes = volumes

        self.create = to_raw_response_wrapper(
            volumes.create,
        )
        self.update = to_raw_response_wrapper(
            volumes.update,
        )
        self.list = to_raw_response_wrapper(
            volumes.list,
        )
        self.delete = to_raw_response_wrapper(
            volumes.delete,
        )
        self.attach_to_instance = to_raw_response_wrapper(
            volumes.attach_to_instance,
        )
        self.change_type = to_raw_response_wrapper(
            volumes.change_type,
        )
        self.detach_from_instance = to_raw_response_wrapper(
            volumes.detach_from_instance,
        )
        self.get = to_raw_response_wrapper(
            volumes.get,
        )
        self.resize = to_raw_response_wrapper(
            volumes.resize,
        )
        self.revert_to_last_snapshot = to_raw_response_wrapper(
            volumes.revert_to_last_snapshot,
        )


class AsyncVolumesResourceWithRawResponse:
    def __init__(self, volumes: AsyncVolumesResource) -> None:
        self._volumes = volumes

        self.create = async_to_raw_response_wrapper(
            volumes.create,
        )
        self.update = async_to_raw_response_wrapper(
            volumes.update,
        )
        self.list = async_to_raw_response_wrapper(
            volumes.list,
        )
        self.delete = async_to_raw_response_wrapper(
            volumes.delete,
        )
        self.attach_to_instance = async_to_raw_response_wrapper(
            volumes.attach_to_instance,
        )
        self.change_type = async_to_raw_response_wrapper(
            volumes.change_type,
        )
        self.detach_from_instance = async_to_raw_response_wrapper(
            volumes.detach_from_instance,
        )
        self.get = async_to_raw_response_wrapper(
            volumes.get,
        )
        self.resize = async_to_raw_response_wrapper(
            volumes.resize,
        )
        self.revert_to_last_snapshot = async_to_raw_response_wrapper(
            volumes.revert_to_last_snapshot,
        )


class VolumesResourceWithStreamingResponse:
    def __init__(self, volumes: VolumesResource) -> None:
        self._volumes = volumes

        self.create = to_streamed_response_wrapper(
            volumes.create,
        )
        self.update = to_streamed_response_wrapper(
            volumes.update,
        )
        self.list = to_streamed_response_wrapper(
            volumes.list,
        )
        self.delete = to_streamed_response_wrapper(
            volumes.delete,
        )
        self.attach_to_instance = to_streamed_response_wrapper(
            volumes.attach_to_instance,
        )
        self.change_type = to_streamed_response_wrapper(
            volumes.change_type,
        )
        self.detach_from_instance = to_streamed_response_wrapper(
            volumes.detach_from_instance,
        )
        self.get = to_streamed_response_wrapper(
            volumes.get,
        )
        self.resize = to_streamed_response_wrapper(
            volumes.resize,
        )
        self.revert_to_last_snapshot = to_streamed_response_wrapper(
            volumes.revert_to_last_snapshot,
        )


class AsyncVolumesResourceWithStreamingResponse:
    def __init__(self, volumes: AsyncVolumesResource) -> None:
        self._volumes = volumes

        self.create = async_to_streamed_response_wrapper(
            volumes.create,
        )
        self.update = async_to_streamed_response_wrapper(
            volumes.update,
        )
        self.list = async_to_streamed_response_wrapper(
            volumes.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            volumes.delete,
        )
        self.attach_to_instance = async_to_streamed_response_wrapper(
            volumes.attach_to_instance,
        )
        self.change_type = async_to_streamed_response_wrapper(
            volumes.change_type,
        )
        self.detach_from_instance = async_to_streamed_response_wrapper(
            volumes.detach_from_instance,
        )
        self.get = async_to_streamed_response_wrapper(
            volumes.get,
        )
        self.resize = async_to_streamed_response_wrapper(
            volumes.resize,
        )
        self.revert_to_last_snapshot = async_to_streamed_response_wrapper(
            volumes.revert_to_last_snapshot,
        )
