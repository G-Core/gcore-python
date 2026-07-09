# Custom code. This file is not generated and is preserved across codegen runs.
# It isolates hand-written *_and_poll convenience methods from generated code to
# eliminate merge conflicts.

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterable, cast
from typing_extensions import Literal, overload

import httpx

from ..._types import NOT_GIVEN, Body, Omit, Query, Headers, NotGiven, omit
from ..._utils import required_args
from ...types.cloud.volume import Volume
from ...types.cloud.task_id_list import TaskIDList
from ...types.cloud.tag_update_map_param import TagUpdateMapParam

if TYPE_CHECKING:
    from ..._client import Gcore, AsyncGcore


class VolumesResourceCustomMixin:
    if TYPE_CHECKING:
        # Provided by the concrete generated resource class this mixin is
        # combined with; declared here so client-derived locals keep their
        # real types and other resource methods resolve via __getattr__.
        _client: Gcore

        def __getattr__(self, name: str) -> Any: ...

    @overload
    def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        image_id: str,
        name: str,
        size: int,
        source: Literal["image"],
        attachment_tag: str | Omit = omit,
        instance_id_to_attach_to: str | Omit = omit,
        lifecycle_policy_ids: Iterable[int] | Omit = omit,
        tags: TagUpdateMapParam | Omit = omit,
        type_name: Literal["cold", "ssd_hiiops", "ssd_local", "ssd_lowlatency", "standard", "ultra"] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Volume:
        """Create a new volume in the project and region and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.

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
    def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        snapshot_id: str,
        source: Literal["snapshot"],
        attachment_tag: str | Omit = omit,
        instance_id_to_attach_to: str | Omit = omit,
        lifecycle_policy_ids: Iterable[int] | Omit = omit,
        size: int | Omit = omit,
        tags: TagUpdateMapParam | Omit = omit,
        type_name: Literal["cold", "ssd_hiiops", "ssd_local", "ssd_lowlatency", "standard", "ultra"] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Volume:
        """Create a new volume in the project and region and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.

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
    def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        size: int,
        source: Literal["new-volume"],
        attachment_tag: str | Omit = omit,
        instance_id_to_attach_to: str | Omit = omit,
        lifecycle_policy_ids: Iterable[int] | Omit = omit,
        tags: TagUpdateMapParam | Omit = omit,
        type_name: Literal["cold", "ssd_hiiops", "ssd_local", "ssd_lowlatency", "standard", "ultra"] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Volume:
        """Create a new volume in the project and region and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.

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
    def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        image_id: str | Omit = omit,
        name: str,
        size: int | Omit = omit,
        source: Literal["image"] | Literal["snapshot"] | Literal["new-volume"],
        attachment_tag: str | Omit = omit,
        instance_id_to_attach_to: str | Omit = omit,
        lifecycle_policy_ids: Iterable[int] | Omit = omit,
        tags: TagUpdateMapParam | Omit = omit,
        type_name: Literal["cold", "ssd_hiiops", "ssd_local", "ssd_lowlatency", "standard", "ultra"] | Omit = omit,
        snapshot_id: str | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Volume:
        """Create a new volume in the project and region and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method."""
        response: TaskIDList = self.create(  # type: ignore
            project_id=project_id,
            region_id=region_id,
            image_id=image_id,
            name=name,
            size=size,
            source=source,
            attachment_tag=attachment_tag,
            instance_id_to_attach_to=instance_id_to_attach_to,
            lifecycle_policy_ids=lifecycle_policy_ids,
            tags=tags,
            type_name=type_name,
            snapshot_id=snapshot_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks:  # type: ignore
            raise ValueError("Expected at least one task to be created")
        task = self._client.cloud.tasks.poll(
            task_id=response.tasks[0],  # type: ignore
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        if (
            task.created_resources is None
            or task.created_resources.volumes is None
            or len(task.created_resources.volumes) != 1
        ):
            raise ValueError("Task completed but created_resources or volumes is missing or invalid")
        created_volume_id = task.created_resources.volumes[0]
        return cast(
            Volume,
            self.get(
                volume_id=created_volume_id,
                project_id=project_id,
                region_id=region_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
        )

    def delete_and_poll(
        self,
        volume_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        snapshots: str | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> None:
        """Delete a volume and all its snapshots and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method."""
        response = self.delete(
            volume_id=volume_id,
            project_id=project_id,
            region_id=region_id,
            snapshots=snapshots,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks:
            raise ValueError("Expected at least one task to be created")
        self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )

    def attach_to_instance_and_poll(
        self,
        volume_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        instance_id: str,
        attachment_tag: str | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> None:
        """Attach the volume to instance and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method."""
        response = self.attach_to_instance(
            volume_id=volume_id,
            project_id=project_id,
            region_id=region_id,
            instance_id=instance_id,
            attachment_tag=attachment_tag,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks:
            raise ValueError("Expected at least one task to be created")
        self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )

    def detach_from_instance_and_poll(
        self,
        volume_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        instance_id: str,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> None:
        """Detach the volume from instance and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method."""
        response = self.detach_from_instance(
            volume_id=volume_id,
            project_id=project_id,
            region_id=region_id,
            instance_id=instance_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks:
            raise ValueError("Expected at least one task to be created")
        self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )

    def resize_and_poll(
        self,
        volume_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        size: int,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Volume:
        """Increase the size of a volume and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method."""
        response = self.resize(
            volume_id=volume_id,
            project_id=project_id,
            region_id=region_id,
            size=size,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks:
            raise ValueError("Expected at least one task to be created")
        self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        return cast(
            Volume,
            self.get(
                volume_id=volume_id,
                project_id=project_id,
                region_id=region_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
        )


class AsyncVolumesResourceCustomMixin:
    if TYPE_CHECKING:
        # Provided by the concrete generated resource class this mixin is
        # combined with; declared here so client-derived locals keep their
        # real types and other resource methods resolve via __getattr__.
        _client: AsyncGcore

        def __getattr__(self, name: str) -> Any: ...

    @overload
    async def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        image_id: str,
        name: str,
        size: int,
        source: Literal["image"],
        attachment_tag: str | Omit = omit,
        instance_id_to_attach_to: str | Omit = omit,
        lifecycle_policy_ids: Iterable[int] | Omit = omit,
        tags: TagUpdateMapParam | Omit = omit,
        type_name: Literal["cold", "ssd_hiiops", "ssd_local", "ssd_lowlatency", "standard", "ultra"] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Volume:
        """Create a new volume in the project and region and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.

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
    async def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        snapshot_id: str,
        source: Literal["snapshot"],
        attachment_tag: str | Omit = omit,
        instance_id_to_attach_to: str | Omit = omit,
        lifecycle_policy_ids: Iterable[int] | Omit = omit,
        size: int | Omit = omit,
        tags: TagUpdateMapParam | Omit = omit,
        type_name: Literal["cold", "ssd_hiiops", "ssd_local", "ssd_lowlatency", "standard", "ultra"] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Volume:
        """Create a new volume in the project and region and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.

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
    async def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        size: int,
        source: Literal["new-volume"],
        attachment_tag: str | Omit = omit,
        instance_id_to_attach_to: str | Omit = omit,
        lifecycle_policy_ids: Iterable[int] | Omit = omit,
        tags: TagUpdateMapParam | Omit = omit,
        type_name: Literal["cold", "ssd_hiiops", "ssd_local", "ssd_lowlatency", "standard", "ultra"] | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Volume:
        """Create a new volume in the project and region and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method.

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
    async def create_and_poll(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        image_id: str | Omit = omit,
        name: str,
        size: int | Omit = omit,
        source: Literal["image"] | Literal["snapshot"] | Literal["new-volume"],
        attachment_tag: str | Omit = omit,
        instance_id_to_attach_to: str | Omit = omit,
        lifecycle_policy_ids: Iterable[int] | Omit = omit,
        tags: TagUpdateMapParam | Omit = omit,
        type_name: Literal["cold", "ssd_hiiops", "ssd_local", "ssd_lowlatency", "standard", "ultra"] | Omit = omit,
        snapshot_id: str | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Volume:
        """Create a new volume in the project and region and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method."""
        response: TaskIDList = await self.create(  # type: ignore
            project_id=project_id,
            region_id=region_id,
            image_id=image_id,
            name=name,
            size=size,
            source=source,
            attachment_tag=attachment_tag,
            instance_id_to_attach_to=instance_id_to_attach_to,
            lifecycle_policy_ids=lifecycle_policy_ids,
            tags=tags,
            type_name=type_name,
            snapshot_id=snapshot_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks:  # type: ignore
            raise ValueError("Expected at least one task to be created")
        task = await self._client.cloud.tasks.poll(
            task_id=response.tasks[0],  # type: ignore
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        if (
            task.created_resources is None
            or task.created_resources.volumes is None
            or len(task.created_resources.volumes) != 1
        ):
            raise ValueError("Task completed but created_resources or volumes is missing or invalid")
        created_volume_id = task.created_resources.volumes[0]
        return cast(
            Volume,
            await self.get(
                volume_id=created_volume_id,
                project_id=project_id,
                region_id=region_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
        )

    async def delete_and_poll(
        self,
        volume_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        snapshots: str | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> None:
        """Delete a volume and all its snapshots and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method."""
        response = await self.delete(
            volume_id=volume_id,
            project_id=project_id,
            region_id=region_id,
            snapshots=snapshots,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks:
            raise ValueError("Expected at least one task to be created")
        await self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )

    async def attach_to_instance_and_poll(
        self,
        volume_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        instance_id: str,
        attachment_tag: str | Omit = omit,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> None:
        """Attach the volume to instance and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method."""
        response = await self.attach_to_instance(
            volume_id=volume_id,
            project_id=project_id,
            region_id=region_id,
            instance_id=instance_id,
            attachment_tag=attachment_tag,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks:
            raise ValueError("Expected at least one task to be created")
        await self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )

    async def detach_from_instance_and_poll(
        self,
        volume_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        instance_id: str,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> None:
        """Detach the volume from instance and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method."""
        response = await self.detach_from_instance(
            volume_id=volume_id,
            project_id=project_id,
            region_id=region_id,
            instance_id=instance_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks:
            raise ValueError("Expected at least one task to be created")
        await self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )

    async def resize_and_poll(
        self,
        volume_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        size: int,
        polling_interval_seconds: int | Omit = omit,
        polling_timeout_seconds: int | Omit = omit,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Volume:
        """Increase the size of a volume and poll for the result. Only the first task will be polled. If you need to poll more tasks, use the `tasks.poll` method."""
        response = await self.resize(
            volume_id=volume_id,
            project_id=project_id,
            region_id=region_id,
            size=size,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        if not response.tasks:
            raise ValueError("Expected at least one task to be created")
        await self._client.cloud.tasks.poll(
            task_id=response.tasks[0],
            extra_headers=extra_headers,
            polling_interval_seconds=polling_interval_seconds,
            polling_timeout_seconds=polling_timeout_seconds,
        )
        return cast(
            Volume,
            await self.get(
                volume_id=volume_id,
                project_id=project_id,
                region_id=region_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
        )
