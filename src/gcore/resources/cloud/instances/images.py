# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ....types.cloud.image import Image
from ....types.cloud.instances import (
    image_get_params,
    image_list_params,
    image_update_params,
    image_upload_params,
    image_create_from_volume_params,
)
from ....types.cloud.image_list import ImageList
from ....types.cloud.task_id_list import TaskIDList
from ....types.cloud.tag_update_list_param import TagUpdateListParam

__all__ = ["ImagesResource", "AsyncImagesResource"]


class ImagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ImagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return ImagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ImagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
        """
        return ImagesResourceWithStreamingResponse(self)

    def update(
        self,
        image_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        hw_firmware_type: Literal["bios", "uefi"] | NotGiven = NOT_GIVEN,
        hw_machine_type: Literal["pc", "q35"] | NotGiven = NOT_GIVEN,
        is_baremetal: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        os_type: Literal["linux", "windows"] | NotGiven = NOT_GIVEN,
        ssh_key: Literal["allow", "deny", "required"] | NotGiven = NOT_GIVEN,
        tags: TagUpdateListParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Image:
        """
        Update image fields

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fimages%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bimage_id%7D/patch/parameters/0/schema'
              "$.paths['/cloud/v1/images/{project_id}/{region_id}/{image_id}'].patch.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fimages%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bimage_id%7D/patch/parameters/1/schema'
              "$.paths['/cloud/v1/images/{project_id}/{region_id}/{image_id}'].patch.parameters[1].schema"

          image_id: '#/paths/%2Fcloud%2Fv1%2Fimages%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bimage_id%7D/patch/parameters/2/schema'
              "$.paths['/cloud/v1/images/{project_id}/{region_id}/{image_id}'].patch.parameters[2].schema"

          hw_firmware_type: '#/components/schemas/UpdateImageSerializer/properties/hw_firmware_type'
              "$.components.schemas.UpdateImageSerializer.properties.hw_firmware_type"

          hw_machine_type: '#/components/schemas/UpdateImageSerializer/properties/hw_machine_type'
              "$.components.schemas.UpdateImageSerializer.properties.hw_machine_type"

          is_baremetal: '#/components/schemas/UpdateImageSerializer/properties/is_baremetal'
              "$.components.schemas.UpdateImageSerializer.properties.is_baremetal"

          name: '#/components/schemas/UpdateImageSerializer/properties/name'
              "$.components.schemas.UpdateImageSerializer.properties.name"

          os_type: '#/components/schemas/UpdateImageSerializer/properties/os_type'
              "$.components.schemas.UpdateImageSerializer.properties.os_type"

          ssh_key: '#/components/schemas/UpdateImageSerializer/properties/ssh_key'
              "$.components.schemas.UpdateImageSerializer.properties.ssh_key"

          tags: '#/components/schemas/UpdateImageSerializer/properties/tags'
              "$.components.schemas.UpdateImageSerializer.properties.tags"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not image_id:
            raise ValueError(f"Expected a non-empty value for `image_id` but received {image_id!r}")
        return self._patch(
            f"/cloud/v1/images/{project_id}/{region_id}/{image_id}",
            body=maybe_transform(
                {
                    "hw_firmware_type": hw_firmware_type,
                    "hw_machine_type": hw_machine_type,
                    "is_baremetal": is_baremetal,
                    "name": name,
                    "os_type": os_type,
                    "ssh_key": ssh_key,
                    "tags": tags,
                },
                image_update_params.ImageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Image,
        )

    def list(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        include_prices: bool | NotGiven = NOT_GIVEN,
        private: str | NotGiven = NOT_GIVEN,
        tag_key: List[str] | NotGiven = NOT_GIVEN,
        tag_key_value: str | NotGiven = NOT_GIVEN,
        visibility: Literal["private", "public", "shared"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ImageList:
        """Retrieve an available images list.

        Returned entities owned by the project and
        public OR shared with the client

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fimages%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/images/{project_id}/{region_id}'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fimages%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v1/images/{project_id}/{region_id}'].get.parameters[1].schema"

          include_prices: '#/paths/%2Fcloud%2Fv1%2Fimages%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/2'
              "$.paths['/cloud/v1/images/{project_id}/{region_id}'].get.parameters[2]"

          private: '#/paths/%2Fcloud%2Fv1%2Fimages%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/3'
              "$.paths['/cloud/v1/images/{project_id}/{region_id}'].get.parameters[3]"

          tag_key: '#/paths/%2Fcloud%2Fv1%2Fimages%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/4'
              "$.paths['/cloud/v1/images/{project_id}/{region_id}'].get.parameters[4]"

          tag_key_value: '#/paths/%2Fcloud%2Fv1%2Fimages%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/5'
              "$.paths['/cloud/v1/images/{project_id}/{region_id}'].get.parameters[5]"

          visibility: '#/paths/%2Fcloud%2Fv1%2Fimages%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/6'
              "$.paths['/cloud/v1/images/{project_id}/{region_id}'].get.parameters[6]"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return self._get(
            f"/cloud/v1/images/{project_id}/{region_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_prices": include_prices,
                        "private": private,
                        "tag_key": tag_key,
                        "tag_key_value": tag_key_value,
                        "visibility": visibility,
                    },
                    image_list_params.ImageListParams,
                ),
            ),
            cast_to=ImageList,
        )

    def delete(
        self,
        image_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Delete the image

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fimages%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bimage_id%7D/delete/parameters/0/schema'
              "$.paths['/cloud/v1/images/{project_id}/{region_id}/{image_id}']['delete'].parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fimages%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bimage_id%7D/delete/parameters/1/schema'
              "$.paths['/cloud/v1/images/{project_id}/{region_id}/{image_id}']['delete'].parameters[1].schema"

          image_id: '#/paths/%2Fcloud%2Fv1%2Fimages%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bimage_id%7D/delete/parameters/2/schema'
              "$.paths['/cloud/v1/images/{project_id}/{region_id}/{image_id}']['delete'].parameters[2].schema"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not image_id:
            raise ValueError(f"Expected a non-empty value for `image_id` but received {image_id!r}")
        return self._delete(
            f"/cloud/v1/images/{project_id}/{region_id}/{image_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def create_from_volume(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        volume_id: str,
        architecture: Literal["aarch64", "x86_64"] | NotGiven = NOT_GIVEN,
        hw_firmware_type: Optional[Literal["bios", "uefi"]] | NotGiven = NOT_GIVEN,
        hw_machine_type: Optional[Literal["pc", "q35"]] | NotGiven = NOT_GIVEN,
        is_baremetal: bool | NotGiven = NOT_GIVEN,
        os_type: Literal["linux", "windows"] | NotGiven = NOT_GIVEN,
        source: Literal["volume"] | NotGiven = NOT_GIVEN,
        ssh_key: Literal["allow", "deny", "required"] | NotGiven = NOT_GIVEN,
        tags: TagUpdateListParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Create image from volume

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fimages%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
              "$.paths['/cloud/v1/images/{project_id}/{region_id}'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fimages%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
              "$.paths['/cloud/v1/images/{project_id}/{region_id}'].post.parameters[1].schema"

          name: '#/components/schemas/ImageCreateFromVolumeSerializer/properties/name'
              "$.components.schemas.ImageCreateFromVolumeSerializer.properties.name"

          volume_id: '#/components/schemas/ImageCreateFromVolumeSerializer/properties/volume_id'
              "$.components.schemas.ImageCreateFromVolumeSerializer.properties.volume_id"

          architecture: '#/components/schemas/ImageCreateFromVolumeSerializer/properties/architecture'
              "$.components.schemas.ImageCreateFromVolumeSerializer.properties.architecture"

          hw_firmware_type: '#/components/schemas/ImageCreateFromVolumeSerializer/properties/hw_firmware_type/anyOf/0'
              "$.components.schemas.ImageCreateFromVolumeSerializer.properties.hw_firmware_type.anyOf[0]"

          hw_machine_type: '#/components/schemas/ImageCreateFromVolumeSerializer/properties/hw_machine_type/anyOf/0'
              "$.components.schemas.ImageCreateFromVolumeSerializer.properties.hw_machine_type.anyOf[0]"

          is_baremetal: '#/components/schemas/ImageCreateFromVolumeSerializer/properties/is_baremetal'
              "$.components.schemas.ImageCreateFromVolumeSerializer.properties.is_baremetal"

          os_type: '#/components/schemas/ImageCreateFromVolumeSerializer/properties/os_type'
              "$.components.schemas.ImageCreateFromVolumeSerializer.properties.os_type"

          source: '#/components/schemas/ImageCreateFromVolumeSerializer/properties/source'
              "$.components.schemas.ImageCreateFromVolumeSerializer.properties.source"

          ssh_key: '#/components/schemas/ImageCreateFromVolumeSerializer/properties/ssh_key'
              "$.components.schemas.ImageCreateFromVolumeSerializer.properties.ssh_key"

          tags: '#/components/schemas/ImageCreateFromVolumeSerializer/properties/tags'
              "$.components.schemas.ImageCreateFromVolumeSerializer.properties.tags"

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
            f"/cloud/v1/images/{project_id}/{region_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "volume_id": volume_id,
                    "architecture": architecture,
                    "hw_firmware_type": hw_firmware_type,
                    "hw_machine_type": hw_machine_type,
                    "is_baremetal": is_baremetal,
                    "os_type": os_type,
                    "source": source,
                    "ssh_key": ssh_key,
                    "tags": tags,
                },
                image_create_from_volume_params.ImageCreateFromVolumeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    def get(
        self,
        image_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        include_prices: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Image:
        """
        Get image

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fimages%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bimage_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/images/{project_id}/{region_id}/{image_id}'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fimages%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bimage_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v1/images/{project_id}/{region_id}/{image_id}'].get.parameters[1].schema"

          image_id: '#/paths/%2Fcloud%2Fv1%2Fimages%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bimage_id%7D/get/parameters/2/schema'
              "$.paths['/cloud/v1/images/{project_id}/{region_id}/{image_id}'].get.parameters[2].schema"

          include_prices: '#/paths/%2Fcloud%2Fv1%2Fimages%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bimage_id%7D/get/parameters/3'
              "$.paths['/cloud/v1/images/{project_id}/{region_id}/{image_id}'].get.parameters[3]"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not image_id:
            raise ValueError(f"Expected a non-empty value for `image_id` but received {image_id!r}")
        return self._get(
            f"/cloud/v1/images/{project_id}/{region_id}/{image_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"include_prices": include_prices}, image_get_params.ImageGetParams),
            ),
            cast_to=Image,
        )

    def upload(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        url: str,
        architecture: Literal["aarch64", "x86_64"] | NotGiven = NOT_GIVEN,
        cow_format: bool | NotGiven = NOT_GIVEN,
        hw_firmware_type: Optional[Literal["bios", "uefi"]] | NotGiven = NOT_GIVEN,
        hw_machine_type: Optional[Literal["pc", "q35"]] | NotGiven = NOT_GIVEN,
        is_baremetal: bool | NotGiven = NOT_GIVEN,
        os_distro: Optional[str] | NotGiven = NOT_GIVEN,
        os_type: Literal["linux", "windows"] | NotGiven = NOT_GIVEN,
        os_version: Optional[str] | NotGiven = NOT_GIVEN,
        ssh_key: Literal["allow", "deny", "required"] | NotGiven = NOT_GIVEN,
        tags: TagUpdateListParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Upload image

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fdownloadimage%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
              "$.paths['/cloud/v1/downloadimage/{project_id}/{region_id}'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fdownloadimage%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
              "$.paths['/cloud/v1/downloadimage/{project_id}/{region_id}'].post.parameters[1].schema"

          name: '#/components/schemas/ImageDownloadSerializer/properties/name'
              "$.components.schemas.ImageDownloadSerializer.properties.name"

          url: '#/components/schemas/ImageDownloadSerializer/properties/url'
              "$.components.schemas.ImageDownloadSerializer.properties.url"

          architecture: '#/components/schemas/ImageDownloadSerializer/properties/architecture'
              "$.components.schemas.ImageDownloadSerializer.properties.architecture"

          cow_format: '#/components/schemas/ImageDownloadSerializer/properties/cow_format'
              "$.components.schemas.ImageDownloadSerializer.properties.cow_format"

          hw_firmware_type: '#/components/schemas/ImageDownloadSerializer/properties/hw_firmware_type/anyOf/0'
              "$.components.schemas.ImageDownloadSerializer.properties.hw_firmware_type.anyOf[0]"

          hw_machine_type: '#/components/schemas/ImageDownloadSerializer/properties/hw_machine_type/anyOf/0'
              "$.components.schemas.ImageDownloadSerializer.properties.hw_machine_type.anyOf[0]"

          is_baremetal: '#/components/schemas/ImageDownloadSerializer/properties/is_baremetal'
              "$.components.schemas.ImageDownloadSerializer.properties.is_baremetal"

          os_distro: '#/components/schemas/ImageDownloadSerializer/properties/os_distro/anyOf/0'
              "$.components.schemas.ImageDownloadSerializer.properties.os_distro.anyOf[0]"

          os_type: '#/components/schemas/ImageDownloadSerializer/properties/os_type'
              "$.components.schemas.ImageDownloadSerializer.properties.os_type"

          os_version: '#/components/schemas/ImageDownloadSerializer/properties/os_version/anyOf/0'
              "$.components.schemas.ImageDownloadSerializer.properties.os_version.anyOf[0]"

          ssh_key: '#/components/schemas/ImageDownloadSerializer/properties/ssh_key'
              "$.components.schemas.ImageDownloadSerializer.properties.ssh_key"

          tags: '#/components/schemas/ImageDownloadSerializer/properties/tags'
              "$.components.schemas.ImageDownloadSerializer.properties.tags"

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
            f"/cloud/v1/downloadimage/{project_id}/{region_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "url": url,
                    "architecture": architecture,
                    "cow_format": cow_format,
                    "hw_firmware_type": hw_firmware_type,
                    "hw_machine_type": hw_machine_type,
                    "is_baremetal": is_baremetal,
                    "os_distro": os_distro,
                    "os_type": os_type,
                    "os_version": os_version,
                    "ssh_key": ssh_key,
                    "tags": tags,
                },
                image_upload_params.ImageUploadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )


class AsyncImagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncImagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncImagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncImagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gcore-python#with_streaming_response
        """
        return AsyncImagesResourceWithStreamingResponse(self)

    async def update(
        self,
        image_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        hw_firmware_type: Literal["bios", "uefi"] | NotGiven = NOT_GIVEN,
        hw_machine_type: Literal["pc", "q35"] | NotGiven = NOT_GIVEN,
        is_baremetal: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        os_type: Literal["linux", "windows"] | NotGiven = NOT_GIVEN,
        ssh_key: Literal["allow", "deny", "required"] | NotGiven = NOT_GIVEN,
        tags: TagUpdateListParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Image:
        """
        Update image fields

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fimages%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bimage_id%7D/patch/parameters/0/schema'
              "$.paths['/cloud/v1/images/{project_id}/{region_id}/{image_id}'].patch.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fimages%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bimage_id%7D/patch/parameters/1/schema'
              "$.paths['/cloud/v1/images/{project_id}/{region_id}/{image_id}'].patch.parameters[1].schema"

          image_id: '#/paths/%2Fcloud%2Fv1%2Fimages%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bimage_id%7D/patch/parameters/2/schema'
              "$.paths['/cloud/v1/images/{project_id}/{region_id}/{image_id}'].patch.parameters[2].schema"

          hw_firmware_type: '#/components/schemas/UpdateImageSerializer/properties/hw_firmware_type'
              "$.components.schemas.UpdateImageSerializer.properties.hw_firmware_type"

          hw_machine_type: '#/components/schemas/UpdateImageSerializer/properties/hw_machine_type'
              "$.components.schemas.UpdateImageSerializer.properties.hw_machine_type"

          is_baremetal: '#/components/schemas/UpdateImageSerializer/properties/is_baremetal'
              "$.components.schemas.UpdateImageSerializer.properties.is_baremetal"

          name: '#/components/schemas/UpdateImageSerializer/properties/name'
              "$.components.schemas.UpdateImageSerializer.properties.name"

          os_type: '#/components/schemas/UpdateImageSerializer/properties/os_type'
              "$.components.schemas.UpdateImageSerializer.properties.os_type"

          ssh_key: '#/components/schemas/UpdateImageSerializer/properties/ssh_key'
              "$.components.schemas.UpdateImageSerializer.properties.ssh_key"

          tags: '#/components/schemas/UpdateImageSerializer/properties/tags'
              "$.components.schemas.UpdateImageSerializer.properties.tags"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not image_id:
            raise ValueError(f"Expected a non-empty value for `image_id` but received {image_id!r}")
        return await self._patch(
            f"/cloud/v1/images/{project_id}/{region_id}/{image_id}",
            body=await async_maybe_transform(
                {
                    "hw_firmware_type": hw_firmware_type,
                    "hw_machine_type": hw_machine_type,
                    "is_baremetal": is_baremetal,
                    "name": name,
                    "os_type": os_type,
                    "ssh_key": ssh_key,
                    "tags": tags,
                },
                image_update_params.ImageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Image,
        )

    async def list(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        include_prices: bool | NotGiven = NOT_GIVEN,
        private: str | NotGiven = NOT_GIVEN,
        tag_key: List[str] | NotGiven = NOT_GIVEN,
        tag_key_value: str | NotGiven = NOT_GIVEN,
        visibility: Literal["private", "public", "shared"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ImageList:
        """Retrieve an available images list.

        Returned entities owned by the project and
        public OR shared with the client

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fimages%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/images/{project_id}/{region_id}'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fimages%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v1/images/{project_id}/{region_id}'].get.parameters[1].schema"

          include_prices: '#/paths/%2Fcloud%2Fv1%2Fimages%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/2'
              "$.paths['/cloud/v1/images/{project_id}/{region_id}'].get.parameters[2]"

          private: '#/paths/%2Fcloud%2Fv1%2Fimages%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/3'
              "$.paths['/cloud/v1/images/{project_id}/{region_id}'].get.parameters[3]"

          tag_key: '#/paths/%2Fcloud%2Fv1%2Fimages%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/4'
              "$.paths['/cloud/v1/images/{project_id}/{region_id}'].get.parameters[4]"

          tag_key_value: '#/paths/%2Fcloud%2Fv1%2Fimages%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/5'
              "$.paths['/cloud/v1/images/{project_id}/{region_id}'].get.parameters[5]"

          visibility: '#/paths/%2Fcloud%2Fv1%2Fimages%2F%7Bproject_id%7D%2F%7Bregion_id%7D/get/parameters/6'
              "$.paths['/cloud/v1/images/{project_id}/{region_id}'].get.parameters[6]"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        return await self._get(
            f"/cloud/v1/images/{project_id}/{region_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "include_prices": include_prices,
                        "private": private,
                        "tag_key": tag_key,
                        "tag_key_value": tag_key_value,
                        "visibility": visibility,
                    },
                    image_list_params.ImageListParams,
                ),
            ),
            cast_to=ImageList,
        )

    async def delete(
        self,
        image_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Delete the image

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fimages%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bimage_id%7D/delete/parameters/0/schema'
              "$.paths['/cloud/v1/images/{project_id}/{region_id}/{image_id}']['delete'].parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fimages%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bimage_id%7D/delete/parameters/1/schema'
              "$.paths['/cloud/v1/images/{project_id}/{region_id}/{image_id}']['delete'].parameters[1].schema"

          image_id: '#/paths/%2Fcloud%2Fv1%2Fimages%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bimage_id%7D/delete/parameters/2/schema'
              "$.paths['/cloud/v1/images/{project_id}/{region_id}/{image_id}']['delete'].parameters[2].schema"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not image_id:
            raise ValueError(f"Expected a non-empty value for `image_id` but received {image_id!r}")
        return await self._delete(
            f"/cloud/v1/images/{project_id}/{region_id}/{image_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def create_from_volume(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        volume_id: str,
        architecture: Literal["aarch64", "x86_64"] | NotGiven = NOT_GIVEN,
        hw_firmware_type: Optional[Literal["bios", "uefi"]] | NotGiven = NOT_GIVEN,
        hw_machine_type: Optional[Literal["pc", "q35"]] | NotGiven = NOT_GIVEN,
        is_baremetal: bool | NotGiven = NOT_GIVEN,
        os_type: Literal["linux", "windows"] | NotGiven = NOT_GIVEN,
        source: Literal["volume"] | NotGiven = NOT_GIVEN,
        ssh_key: Literal["allow", "deny", "required"] | NotGiven = NOT_GIVEN,
        tags: TagUpdateListParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Create image from volume

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fimages%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
              "$.paths['/cloud/v1/images/{project_id}/{region_id}'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fimages%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
              "$.paths['/cloud/v1/images/{project_id}/{region_id}'].post.parameters[1].schema"

          name: '#/components/schemas/ImageCreateFromVolumeSerializer/properties/name'
              "$.components.schemas.ImageCreateFromVolumeSerializer.properties.name"

          volume_id: '#/components/schemas/ImageCreateFromVolumeSerializer/properties/volume_id'
              "$.components.schemas.ImageCreateFromVolumeSerializer.properties.volume_id"

          architecture: '#/components/schemas/ImageCreateFromVolumeSerializer/properties/architecture'
              "$.components.schemas.ImageCreateFromVolumeSerializer.properties.architecture"

          hw_firmware_type: '#/components/schemas/ImageCreateFromVolumeSerializer/properties/hw_firmware_type/anyOf/0'
              "$.components.schemas.ImageCreateFromVolumeSerializer.properties.hw_firmware_type.anyOf[0]"

          hw_machine_type: '#/components/schemas/ImageCreateFromVolumeSerializer/properties/hw_machine_type/anyOf/0'
              "$.components.schemas.ImageCreateFromVolumeSerializer.properties.hw_machine_type.anyOf[0]"

          is_baremetal: '#/components/schemas/ImageCreateFromVolumeSerializer/properties/is_baremetal'
              "$.components.schemas.ImageCreateFromVolumeSerializer.properties.is_baremetal"

          os_type: '#/components/schemas/ImageCreateFromVolumeSerializer/properties/os_type'
              "$.components.schemas.ImageCreateFromVolumeSerializer.properties.os_type"

          source: '#/components/schemas/ImageCreateFromVolumeSerializer/properties/source'
              "$.components.schemas.ImageCreateFromVolumeSerializer.properties.source"

          ssh_key: '#/components/schemas/ImageCreateFromVolumeSerializer/properties/ssh_key'
              "$.components.schemas.ImageCreateFromVolumeSerializer.properties.ssh_key"

          tags: '#/components/schemas/ImageCreateFromVolumeSerializer/properties/tags'
              "$.components.schemas.ImageCreateFromVolumeSerializer.properties.tags"

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
            f"/cloud/v1/images/{project_id}/{region_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "volume_id": volume_id,
                    "architecture": architecture,
                    "hw_firmware_type": hw_firmware_type,
                    "hw_machine_type": hw_machine_type,
                    "is_baremetal": is_baremetal,
                    "os_type": os_type,
                    "source": source,
                    "ssh_key": ssh_key,
                    "tags": tags,
                },
                image_create_from_volume_params.ImageCreateFromVolumeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )

    async def get(
        self,
        image_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        include_prices: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Image:
        """
        Get image

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fimages%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bimage_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v1/images/{project_id}/{region_id}/{image_id}'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fimages%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bimage_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v1/images/{project_id}/{region_id}/{image_id}'].get.parameters[1].schema"

          image_id: '#/paths/%2Fcloud%2Fv1%2Fimages%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bimage_id%7D/get/parameters/2/schema'
              "$.paths['/cloud/v1/images/{project_id}/{region_id}/{image_id}'].get.parameters[2].schema"

          include_prices: '#/paths/%2Fcloud%2Fv1%2Fimages%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bimage_id%7D/get/parameters/3'
              "$.paths['/cloud/v1/images/{project_id}/{region_id}/{image_id}'].get.parameters[3]"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not image_id:
            raise ValueError(f"Expected a non-empty value for `image_id` but received {image_id!r}")
        return await self._get(
            f"/cloud/v1/images/{project_id}/{region_id}/{image_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"include_prices": include_prices}, image_get_params.ImageGetParams),
            ),
            cast_to=Image,
        )

    async def upload(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        url: str,
        architecture: Literal["aarch64", "x86_64"] | NotGiven = NOT_GIVEN,
        cow_format: bool | NotGiven = NOT_GIVEN,
        hw_firmware_type: Optional[Literal["bios", "uefi"]] | NotGiven = NOT_GIVEN,
        hw_machine_type: Optional[Literal["pc", "q35"]] | NotGiven = NOT_GIVEN,
        is_baremetal: bool | NotGiven = NOT_GIVEN,
        os_distro: Optional[str] | NotGiven = NOT_GIVEN,
        os_type: Literal["linux", "windows"] | NotGiven = NOT_GIVEN,
        os_version: Optional[str] | NotGiven = NOT_GIVEN,
        ssh_key: Literal["allow", "deny", "required"] | NotGiven = NOT_GIVEN,
        tags: TagUpdateListParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Upload image

        Args:
          project_id: '#/paths/%2Fcloud%2Fv1%2Fdownloadimage%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
              "$.paths['/cloud/v1/downloadimage/{project_id}/{region_id}'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv1%2Fdownloadimage%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
              "$.paths['/cloud/v1/downloadimage/{project_id}/{region_id}'].post.parameters[1].schema"

          name: '#/components/schemas/ImageDownloadSerializer/properties/name'
              "$.components.schemas.ImageDownloadSerializer.properties.name"

          url: '#/components/schemas/ImageDownloadSerializer/properties/url'
              "$.components.schemas.ImageDownloadSerializer.properties.url"

          architecture: '#/components/schemas/ImageDownloadSerializer/properties/architecture'
              "$.components.schemas.ImageDownloadSerializer.properties.architecture"

          cow_format: '#/components/schemas/ImageDownloadSerializer/properties/cow_format'
              "$.components.schemas.ImageDownloadSerializer.properties.cow_format"

          hw_firmware_type: '#/components/schemas/ImageDownloadSerializer/properties/hw_firmware_type/anyOf/0'
              "$.components.schemas.ImageDownloadSerializer.properties.hw_firmware_type.anyOf[0]"

          hw_machine_type: '#/components/schemas/ImageDownloadSerializer/properties/hw_machine_type/anyOf/0'
              "$.components.schemas.ImageDownloadSerializer.properties.hw_machine_type.anyOf[0]"

          is_baremetal: '#/components/schemas/ImageDownloadSerializer/properties/is_baremetal'
              "$.components.schemas.ImageDownloadSerializer.properties.is_baremetal"

          os_distro: '#/components/schemas/ImageDownloadSerializer/properties/os_distro/anyOf/0'
              "$.components.schemas.ImageDownloadSerializer.properties.os_distro.anyOf[0]"

          os_type: '#/components/schemas/ImageDownloadSerializer/properties/os_type'
              "$.components.schemas.ImageDownloadSerializer.properties.os_type"

          os_version: '#/components/schemas/ImageDownloadSerializer/properties/os_version/anyOf/0'
              "$.components.schemas.ImageDownloadSerializer.properties.os_version.anyOf[0]"

          ssh_key: '#/components/schemas/ImageDownloadSerializer/properties/ssh_key'
              "$.components.schemas.ImageDownloadSerializer.properties.ssh_key"

          tags: '#/components/schemas/ImageDownloadSerializer/properties/tags'
              "$.components.schemas.ImageDownloadSerializer.properties.tags"

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
            f"/cloud/v1/downloadimage/{project_id}/{region_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "url": url,
                    "architecture": architecture,
                    "cow_format": cow_format,
                    "hw_firmware_type": hw_firmware_type,
                    "hw_machine_type": hw_machine_type,
                    "is_baremetal": is_baremetal,
                    "os_distro": os_distro,
                    "os_type": os_type,
                    "os_version": os_version,
                    "ssh_key": ssh_key,
                    "tags": tags,
                },
                image_upload_params.ImageUploadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskIDList,
        )


class ImagesResourceWithRawResponse:
    def __init__(self, images: ImagesResource) -> None:
        self._images = images

        self.update = to_raw_response_wrapper(
            images.update,
        )
        self.list = to_raw_response_wrapper(
            images.list,
        )
        self.delete = to_raw_response_wrapper(
            images.delete,
        )
        self.create_from_volume = to_raw_response_wrapper(
            images.create_from_volume,
        )
        self.get = to_raw_response_wrapper(
            images.get,
        )
        self.upload = to_raw_response_wrapper(
            images.upload,
        )


class AsyncImagesResourceWithRawResponse:
    def __init__(self, images: AsyncImagesResource) -> None:
        self._images = images

        self.update = async_to_raw_response_wrapper(
            images.update,
        )
        self.list = async_to_raw_response_wrapper(
            images.list,
        )
        self.delete = async_to_raw_response_wrapper(
            images.delete,
        )
        self.create_from_volume = async_to_raw_response_wrapper(
            images.create_from_volume,
        )
        self.get = async_to_raw_response_wrapper(
            images.get,
        )
        self.upload = async_to_raw_response_wrapper(
            images.upload,
        )


class ImagesResourceWithStreamingResponse:
    def __init__(self, images: ImagesResource) -> None:
        self._images = images

        self.update = to_streamed_response_wrapper(
            images.update,
        )
        self.list = to_streamed_response_wrapper(
            images.list,
        )
        self.delete = to_streamed_response_wrapper(
            images.delete,
        )
        self.create_from_volume = to_streamed_response_wrapper(
            images.create_from_volume,
        )
        self.get = to_streamed_response_wrapper(
            images.get,
        )
        self.upload = to_streamed_response_wrapper(
            images.upload,
        )


class AsyncImagesResourceWithStreamingResponse:
    def __init__(self, images: AsyncImagesResource) -> None:
        self._images = images

        self.update = async_to_streamed_response_wrapper(
            images.update,
        )
        self.list = async_to_streamed_response_wrapper(
            images.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            images.delete,
        )
        self.create_from_volume = async_to_streamed_response_wrapper(
            images.create_from_volume,
        )
        self.get = async_to_streamed_response_wrapper(
            images.get,
        )
        self.upload = async_to_streamed_response_wrapper(
            images.upload,
        )
