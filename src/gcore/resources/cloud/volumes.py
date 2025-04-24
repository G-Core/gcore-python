# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable
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

__all__ = ["VolumesResource", "AsyncVolumesResource"]


class VolumesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VolumesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return VolumesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VolumesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
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
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        type_name: Literal["cold", "ssd_hiiops", "ssd_local", "ssd_lowlatency", "standard", "ultra"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Create volume

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].post.parameters[1].schema"

          image_id: '#/components/schemas/CreateVolumeFromImageSerializer/properties/image_id'
              "$.components.schemas.CreateVolumeFromImageSerializer.properties.image_id"

          name: '#/components/schemas/CreateVolumeFromImageSerializer/properties/name'
              "$.components.schemas.CreateVolumeFromImageSerializer.properties.name"

          size: '#/components/schemas/CreateVolumeFromImageSerializer/properties/size'
              "$.components.schemas.CreateVolumeFromImageSerializer.properties.size"

          source: '#/components/schemas/CreateVolumeFromImageSerializer/properties/source'
              "$.components.schemas.CreateVolumeFromImageSerializer.properties.source"

          attachment_tag: '#/components/schemas/CreateVolumeFromImageSerializer/properties/attachment_tag'
              "$.components.schemas.CreateVolumeFromImageSerializer.properties.attachment_tag"

          instance_id_to_attach_to: '#/components/schemas/CreateVolumeFromImageSerializer/properties/instance_id_to_attach_to'
              "$.components.schemas.CreateVolumeFromImageSerializer.properties.instance_id_to_attach_to"

          lifecycle_policy_ids: '#/components/schemas/CreateVolumeFromImageSerializer/properties/lifecycle_policy_ids'
              "$.components.schemas.CreateVolumeFromImageSerializer.properties.lifecycle_policy_ids"

          metadata: '#/components/schemas/CreateVolumeFromImageSerializer/properties/metadata'
              "$.components.schemas.CreateVolumeFromImageSerializer.properties.metadata"

          type_name: '#/components/schemas/CreateVolumeFromImageSerializer/properties/type_name'
              "$.components.schemas.CreateVolumeFromImageSerializer.properties.type_name"

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
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        size: int | NotGiven = NOT_GIVEN,
        type_name: Literal["cold", "ssd_hiiops", "ssd_local", "ssd_lowlatency", "standard", "ultra"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Create volume

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].post.parameters[1].schema"

          name: '#/components/schemas/CreateVolumeFromSnapshotSerializer/properties/name'
              "$.components.schemas.CreateVolumeFromSnapshotSerializer.properties.name"

          snapshot_id: '#/components/schemas/CreateVolumeFromSnapshotSerializer/properties/snapshot_id'
              "$.components.schemas.CreateVolumeFromSnapshotSerializer.properties.snapshot_id"

          source: '#/components/schemas/CreateVolumeFromSnapshotSerializer/properties/source'
              "$.components.schemas.CreateVolumeFromSnapshotSerializer.properties.source"

          attachment_tag: '#/components/schemas/CreateVolumeFromSnapshotSerializer/properties/attachment_tag'
              "$.components.schemas.CreateVolumeFromSnapshotSerializer.properties.attachment_tag"

          instance_id_to_attach_to: '#/components/schemas/CreateVolumeFromSnapshotSerializer/properties/instance_id_to_attach_to'
              "$.components.schemas.CreateVolumeFromSnapshotSerializer.properties.instance_id_to_attach_to"

          lifecycle_policy_ids: '#/components/schemas/CreateVolumeFromSnapshotSerializer/properties/lifecycle_policy_ids'
              "$.components.schemas.CreateVolumeFromSnapshotSerializer.properties.lifecycle_policy_ids"

          metadata: '#/components/schemas/CreateVolumeFromSnapshotSerializer/properties/metadata'
              "$.components.schemas.CreateVolumeFromSnapshotSerializer.properties.metadata"

          size: '#/components/schemas/CreateVolumeFromSnapshotSerializer/properties/size'
              "$.components.schemas.CreateVolumeFromSnapshotSerializer.properties.size"

          type_name: '#/components/schemas/CreateVolumeFromSnapshotSerializer/properties/type_name'
              "$.components.schemas.CreateVolumeFromSnapshotSerializer.properties.type_name"

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
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        type_name: Literal["cold", "ssd_hiiops", "ssd_local", "ssd_lowlatency", "standard", "ultra"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Create volume

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].post.parameters[1].schema"

          name: '#/components/schemas/CreateNewVolumeSerializer/properties/name'
              "$.components.schemas.CreateNewVolumeSerializer.properties.name"

          size: '#/components/schemas/CreateNewVolumeSerializer/properties/size'
              "$.components.schemas.CreateNewVolumeSerializer.properties.size"

          source: '#/components/schemas/CreateNewVolumeSerializer/properties/source'
              "$.components.schemas.CreateNewVolumeSerializer.properties.source"

          attachment_tag: '#/components/schemas/CreateNewVolumeSerializer/properties/attachment_tag'
              "$.components.schemas.CreateNewVolumeSerializer.properties.attachment_tag"

          instance_id_to_attach_to: '#/components/schemas/CreateNewVolumeSerializer/properties/instance_id_to_attach_to'
              "$.components.schemas.CreateNewVolumeSerializer.properties.instance_id_to_attach_to"

          lifecycle_policy_ids: '#/components/schemas/CreateNewVolumeSerializer/properties/lifecycle_policy_ids'
              "$.components.schemas.CreateNewVolumeSerializer.properties.lifecycle_policy_ids"

          metadata: '#/components/schemas/CreateNewVolumeSerializer/properties/metadata'
              "$.components.schemas.CreateNewVolumeSerializer.properties.metadata"

          type_name: '#/components/schemas/CreateNewVolumeSerializer/properties/type_name'
              "$.components.schemas.CreateNewVolumeSerializer.properties.type_name"

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
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
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
            project_id = self._client._get_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_region_id_path_param()
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
                    "metadata": metadata,
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
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Volume:
        """
        Rename volume

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D/patch/parameters/0/schema'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}'].patch.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D/patch/parameters/1/schema'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}'].patch.parameters[1].schema"

          volume_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D/patch/parameters/2/schema'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}'].patch.parameters[2].schema"

          name: '#/components/schemas/NameSerializer/properties/name'
              "$.components.schemas.NameSerializer.properties.name"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_region_id_path_param()
        if not volume_id:
            raise ValueError(f"Expected a non-empty value for `volume_id` but received {volume_id!r}")
        return self._patch(
            f"/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}",
            body=maybe_transform({"name": name}, volume_update_params.VolumeUpdateParams),
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
        metadata_k: List[str] | NotGiven = NOT_GIVEN,
        metadata_kv: str | NotGiven = NOT_GIVEN,
        name_part: str | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[Volume]:
        """
        List volumes

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].get.parameters[1].schema"

          bootable: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/2'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].get.parameters[2]"

          cluster_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/3'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].get.parameters[3]"

          has_attachments: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/4'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].get.parameters[4]"

          id_part: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/5'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].get.parameters[5]"

          instance_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/6'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].get.parameters[6]"

          limit: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/7'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].get.parameters[7]"

          metadata_k: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/8'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].get.parameters[8]"

          metadata_kv: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/9'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].get.parameters[9]"

          name_part: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/10'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].get.parameters[10]"

          offset: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/11'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].get.parameters[11]"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_region_id_path_param()
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
                        "metadata_k": metadata_k,
                        "metadata_kv": metadata_kv,
                        "name_part": name_part,
                        "offset": offset,
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
        """
        Delete volume

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D/delete/parameters/0/schema'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}']['delete'].parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D/delete/parameters/1/schema'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}']['delete'].parameters[1].schema"

          volume_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D/delete/parameters/2/schema'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}']['delete'].parameters[2].schema"

          snapshots: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D/delete/parameters/3'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}']['delete'].parameters[3]"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_region_id_path_param()
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
          project_id: '#/paths/%2Fcloud%2Fv2%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D%2Fattach/post/parameters/0/schema'
              "$.paths['/cloud/v2/volumes/{project_id}/{region_id}/{volume_id}/attach'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv2%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D%2Fattach/post/parameters/1/schema'
              "$.paths['/cloud/v2/volumes/{project_id}/{region_id}/{volume_id}/attach'].post.parameters[1].schema"

          volume_id: '#/paths/%2Fcloud%2Fv2%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D%2Fattach/post/parameters/2/schema'
              "$.paths['/cloud/v2/volumes/{project_id}/{region_id}/{volume_id}/attach'].post.parameters[2].schema"

          instance_id: '#/components/schemas/AttachVolumeToInstanceSerializer/properties/instance_id'
              "$.components.schemas.AttachVolumeToInstanceSerializer.properties.instance_id"

          attachment_tag: '#/components/schemas/AttachVolumeToInstanceSerializer/properties/attachment_tag'
              "$.components.schemas.AttachVolumeToInstanceSerializer.properties.attachment_tag"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_region_id_path_param()
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
        """
        Change volume type

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D%2Fretype/post/parameters/0/schema'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}/retype'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D%2Fretype/post/parameters/1/schema'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}/retype'].post.parameters[1].schema"

          volume_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D%2Fretype/post/parameters/2/schema'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}/retype'].post.parameters[2].schema"

          volume_type: '#/components/schemas/VolumeRetypeSerializer/properties/volume_type'
              "$.components.schemas.VolumeRetypeSerializer.properties.volume_type"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_region_id_path_param()
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
          project_id: '#/paths/%2Fcloud%2Fv2%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D%2Fdetach/post/parameters/0/schema'
              "$.paths['/cloud/v2/volumes/{project_id}/{region_id}/{volume_id}/detach'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv2%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D%2Fdetach/post/parameters/1/schema'
              "$.paths['/cloud/v2/volumes/{project_id}/{region_id}/{volume_id}/detach'].post.parameters[1].schema"

          volume_id: '#/paths/%2Fcloud%2Fv2%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D%2Fdetach/post/parameters/2/schema'
              "$.paths['/cloud/v2/volumes/{project_id}/{region_id}/{volume_id}/detach'].post.parameters[2].schema"

          instance_id: '#/components/schemas/InstanceIdSerializer/properties/instance_id'
              "$.components.schemas.InstanceIdSerializer.properties.instance_id"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_region_id_path_param()
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
        Get volume

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}'].get.parameters[1].schema"

          volume_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D/get/parameters/2/schema'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}'].get.parameters[2].schema"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_region_id_path_param()
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
        """
        Extend volume

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D%2Fextend/post/parameters/0/schema'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}/extend'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D%2Fextend/post/parameters/1/schema'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}/extend'].post.parameters[1].schema"

          volume_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D%2Fextend/post/parameters/2/schema'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}/extend'].post.parameters[2].schema"

          size: '#/components/schemas/SizeSerializer/properties/size'
              "$.components.schemas.SizeSerializer.properties.size"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_region_id_path_param()
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
        """
        Revert volume to it's last snapshot

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D%2Frevert/post/parameters/0/schema'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}/revert'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D%2Frevert/post/parameters/1/schema'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}/revert'].post.parameters[1].schema"

          volume_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D%2Frevert/post/parameters/2/schema'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}/revert'].post.parameters[2].schema"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_region_id_path_param()
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

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVolumesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVolumesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
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
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        type_name: Literal["cold", "ssd_hiiops", "ssd_local", "ssd_lowlatency", "standard", "ultra"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Create volume

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].post.parameters[1].schema"

          image_id: '#/components/schemas/CreateVolumeFromImageSerializer/properties/image_id'
              "$.components.schemas.CreateVolumeFromImageSerializer.properties.image_id"

          name: '#/components/schemas/CreateVolumeFromImageSerializer/properties/name'
              "$.components.schemas.CreateVolumeFromImageSerializer.properties.name"

          size: '#/components/schemas/CreateVolumeFromImageSerializer/properties/size'
              "$.components.schemas.CreateVolumeFromImageSerializer.properties.size"

          source: '#/components/schemas/CreateVolumeFromImageSerializer/properties/source'
              "$.components.schemas.CreateVolumeFromImageSerializer.properties.source"

          attachment_tag: '#/components/schemas/CreateVolumeFromImageSerializer/properties/attachment_tag'
              "$.components.schemas.CreateVolumeFromImageSerializer.properties.attachment_tag"

          instance_id_to_attach_to: '#/components/schemas/CreateVolumeFromImageSerializer/properties/instance_id_to_attach_to'
              "$.components.schemas.CreateVolumeFromImageSerializer.properties.instance_id_to_attach_to"

          lifecycle_policy_ids: '#/components/schemas/CreateVolumeFromImageSerializer/properties/lifecycle_policy_ids'
              "$.components.schemas.CreateVolumeFromImageSerializer.properties.lifecycle_policy_ids"

          metadata: '#/components/schemas/CreateVolumeFromImageSerializer/properties/metadata'
              "$.components.schemas.CreateVolumeFromImageSerializer.properties.metadata"

          type_name: '#/components/schemas/CreateVolumeFromImageSerializer/properties/type_name'
              "$.components.schemas.CreateVolumeFromImageSerializer.properties.type_name"

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
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        size: int | NotGiven = NOT_GIVEN,
        type_name: Literal["cold", "ssd_hiiops", "ssd_local", "ssd_lowlatency", "standard", "ultra"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Create volume

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].post.parameters[1].schema"

          name: '#/components/schemas/CreateVolumeFromSnapshotSerializer/properties/name'
              "$.components.schemas.CreateVolumeFromSnapshotSerializer.properties.name"

          snapshot_id: '#/components/schemas/CreateVolumeFromSnapshotSerializer/properties/snapshot_id'
              "$.components.schemas.CreateVolumeFromSnapshotSerializer.properties.snapshot_id"

          source: '#/components/schemas/CreateVolumeFromSnapshotSerializer/properties/source'
              "$.components.schemas.CreateVolumeFromSnapshotSerializer.properties.source"

          attachment_tag: '#/components/schemas/CreateVolumeFromSnapshotSerializer/properties/attachment_tag'
              "$.components.schemas.CreateVolumeFromSnapshotSerializer.properties.attachment_tag"

          instance_id_to_attach_to: '#/components/schemas/CreateVolumeFromSnapshotSerializer/properties/instance_id_to_attach_to'
              "$.components.schemas.CreateVolumeFromSnapshotSerializer.properties.instance_id_to_attach_to"

          lifecycle_policy_ids: '#/components/schemas/CreateVolumeFromSnapshotSerializer/properties/lifecycle_policy_ids'
              "$.components.schemas.CreateVolumeFromSnapshotSerializer.properties.lifecycle_policy_ids"

          metadata: '#/components/schemas/CreateVolumeFromSnapshotSerializer/properties/metadata'
              "$.components.schemas.CreateVolumeFromSnapshotSerializer.properties.metadata"

          size: '#/components/schemas/CreateVolumeFromSnapshotSerializer/properties/size'
              "$.components.schemas.CreateVolumeFromSnapshotSerializer.properties.size"

          type_name: '#/components/schemas/CreateVolumeFromSnapshotSerializer/properties/type_name'
              "$.components.schemas.CreateVolumeFromSnapshotSerializer.properties.type_name"

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
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        type_name: Literal["cold", "ssd_hiiops", "ssd_local", "ssd_lowlatency", "standard", "ultra"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Create volume

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].post.parameters[1].schema"

          name: '#/components/schemas/CreateNewVolumeSerializer/properties/name'
              "$.components.schemas.CreateNewVolumeSerializer.properties.name"

          size: '#/components/schemas/CreateNewVolumeSerializer/properties/size'
              "$.components.schemas.CreateNewVolumeSerializer.properties.size"

          source: '#/components/schemas/CreateNewVolumeSerializer/properties/source'
              "$.components.schemas.CreateNewVolumeSerializer.properties.source"

          attachment_tag: '#/components/schemas/CreateNewVolumeSerializer/properties/attachment_tag'
              "$.components.schemas.CreateNewVolumeSerializer.properties.attachment_tag"

          instance_id_to_attach_to: '#/components/schemas/CreateNewVolumeSerializer/properties/instance_id_to_attach_to'
              "$.components.schemas.CreateNewVolumeSerializer.properties.instance_id_to_attach_to"

          lifecycle_policy_ids: '#/components/schemas/CreateNewVolumeSerializer/properties/lifecycle_policy_ids'
              "$.components.schemas.CreateNewVolumeSerializer.properties.lifecycle_policy_ids"

          metadata: '#/components/schemas/CreateNewVolumeSerializer/properties/metadata'
              "$.components.schemas.CreateNewVolumeSerializer.properties.metadata"

          type_name: '#/components/schemas/CreateNewVolumeSerializer/properties/type_name'
              "$.components.schemas.CreateNewVolumeSerializer.properties.type_name"

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
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
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
            project_id = self._client._get_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_region_id_path_param()
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
                    "metadata": metadata,
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
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Volume:
        """
        Rename volume

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D/patch/parameters/0/schema'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}'].patch.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D/patch/parameters/1/schema'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}'].patch.parameters[1].schema"

          volume_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D/patch/parameters/2/schema'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}'].patch.parameters[2].schema"

          name: '#/components/schemas/NameSerializer/properties/name'
              "$.components.schemas.NameSerializer.properties.name"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_region_id_path_param()
        if not volume_id:
            raise ValueError(f"Expected a non-empty value for `volume_id` but received {volume_id!r}")
        return await self._patch(
            f"/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}",
            body=await async_maybe_transform({"name": name}, volume_update_params.VolumeUpdateParams),
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
        metadata_k: List[str] | NotGiven = NOT_GIVEN,
        metadata_kv: str | NotGiven = NOT_GIVEN,
        name_part: str | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Volume, AsyncOffsetPage[Volume]]:
        """
        List volumes

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].get.parameters[1].schema"

          bootable: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/2'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].get.parameters[2]"

          cluster_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/3'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].get.parameters[3]"

          has_attachments: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/4'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].get.parameters[4]"

          id_part: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/5'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].get.parameters[5]"

          instance_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/6'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].get.parameters[6]"

          limit: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/7'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].get.parameters[7]"

          metadata_k: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/8'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].get.parameters[8]"

          metadata_kv: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/9'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].get.parameters[9]"

          name_part: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/10'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].get.parameters[10]"

          offset: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/11'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}'].get.parameters[11]"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_region_id_path_param()
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
                        "metadata_k": metadata_k,
                        "metadata_kv": metadata_kv,
                        "name_part": name_part,
                        "offset": offset,
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
        """
        Delete volume

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D/delete/parameters/0/schema'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}']['delete'].parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D/delete/parameters/1/schema'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}']['delete'].parameters[1].schema"

          volume_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D/delete/parameters/2/schema'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}']['delete'].parameters[2].schema"

          snapshots: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D/delete/parameters/3'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}']['delete'].parameters[3]"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_region_id_path_param()
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
          project_id: '#/paths/%2Fcloud%2Fv2%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D%2Fattach/post/parameters/0/schema'
              "$.paths['/cloud/v2/volumes/{project_id}/{region_id}/{volume_id}/attach'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv2%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D%2Fattach/post/parameters/1/schema'
              "$.paths['/cloud/v2/volumes/{project_id}/{region_id}/{volume_id}/attach'].post.parameters[1].schema"

          volume_id: '#/paths/%2Fcloud%2Fv2%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D%2Fattach/post/parameters/2/schema'
              "$.paths['/cloud/v2/volumes/{project_id}/{region_id}/{volume_id}/attach'].post.parameters[2].schema"

          instance_id: '#/components/schemas/AttachVolumeToInstanceSerializer/properties/instance_id'
              "$.components.schemas.AttachVolumeToInstanceSerializer.properties.instance_id"

          attachment_tag: '#/components/schemas/AttachVolumeToInstanceSerializer/properties/attachment_tag'
              "$.components.schemas.AttachVolumeToInstanceSerializer.properties.attachment_tag"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_region_id_path_param()
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
        """
        Change volume type

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D%2Fretype/post/parameters/0/schema'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}/retype'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D%2Fretype/post/parameters/1/schema'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}/retype'].post.parameters[1].schema"

          volume_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D%2Fretype/post/parameters/2/schema'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}/retype'].post.parameters[2].schema"

          volume_type: '#/components/schemas/VolumeRetypeSerializer/properties/volume_type'
              "$.components.schemas.VolumeRetypeSerializer.properties.volume_type"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_region_id_path_param()
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
          project_id: '#/paths/%2Fcloud%2Fv2%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D%2Fdetach/post/parameters/0/schema'
              "$.paths['/cloud/v2/volumes/{project_id}/{region_id}/{volume_id}/detach'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv2%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D%2Fdetach/post/parameters/1/schema'
              "$.paths['/cloud/v2/volumes/{project_id}/{region_id}/{volume_id}/detach'].post.parameters[1].schema"

          volume_id: '#/paths/%2Fcloud%2Fv2%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D%2Fdetach/post/parameters/2/schema'
              "$.paths['/cloud/v2/volumes/{project_id}/{region_id}/{volume_id}/detach'].post.parameters[2].schema"

          instance_id: '#/components/schemas/InstanceIdSerializer/properties/instance_id'
              "$.components.schemas.InstanceIdSerializer.properties.instance_id"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_region_id_path_param()
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
        Get volume

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}'].get.parameters[1].schema"

          volume_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D/get/parameters/2/schema'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}'].get.parameters[2].schema"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_region_id_path_param()
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
        """
        Extend volume

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D%2Fextend/post/parameters/0/schema'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}/extend'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D%2Fextend/post/parameters/1/schema'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}/extend'].post.parameters[1].schema"

          volume_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D%2Fextend/post/parameters/2/schema'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}/extend'].post.parameters[2].schema"

          size: '#/components/schemas/SizeSerializer/properties/size'
              "$.components.schemas.SizeSerializer.properties.size"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_region_id_path_param()
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
        """
        Revert volume to it's last snapshot

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D%2Frevert/post/parameters/0/schema'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}/revert'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D%2Frevert/post/parameters/1/schema'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}/revert'].post.parameters[1].schema"

          volume_id: '#/paths/%2Fcloud%2Fv1%2Fvolumes%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bvolume_id%7D%2Frevert/post/parameters/2/schema'
              "$.paths['/cloud/v1/volumes/{project_id}/{region_id}/{volume_id}/revert'].post.parameters[2].schema"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_region_id_path_param()
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
