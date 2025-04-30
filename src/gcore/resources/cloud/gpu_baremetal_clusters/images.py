# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
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
from ....types.cloud.gpu_image import GPUImage
from ....types.cloud.task_id_list import TaskIDList
from ....types.cloud.gpu_image_list import GPUImageList
from ....types.cloud.gpu_baremetal_clusters import image_upload_params

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

    def list(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GPUImageList:
        """
        List bare metal GPU images

        Args:
          project_id: '#/paths/%2Fcloud%2Fv3%2Fgpu%2Fbaremetal%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2Fimages/get/parameters/0/schema'
              "$.paths['/cloud/v3/gpu/baremetal/{project_id}/{region_id}/images'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv3%2Fgpu%2Fbaremetal%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2Fimages/get/parameters/1/schema'
              "$.paths['/cloud/v3/gpu/baremetal/{project_id}/{region_id}/images'].get.parameters[1].schema"

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
            f"/cloud/v3/gpu/baremetal/{project_id}/{region_id}/images",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GPUImageList,
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
        Delete bare metal GPU image by ID

        Args:
          project_id: '#/paths/%2Fcloud%2Fv3%2Fgpu%2Fbaremetal%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2Fimages%2F%7Bimage_id%7D/delete/parameters/0/schema'
              "$.paths['/cloud/v3/gpu/baremetal/{project_id}/{region_id}/images/{image_id}']['delete'].parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv3%2Fgpu%2Fbaremetal%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2Fimages%2F%7Bimage_id%7D/delete/parameters/1/schema'
              "$.paths['/cloud/v3/gpu/baremetal/{project_id}/{region_id}/images/{image_id}']['delete'].parameters[1].schema"

          image_id: '#/paths/%2Fcloud%2Fv3%2Fgpu%2Fbaremetal%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2Fimages%2F%7Bimage_id%7D/delete/parameters/2/schema'
              "$.paths['/cloud/v3/gpu/baremetal/{project_id}/{region_id}/images/{image_id}']['delete'].parameters[2].schema"

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
            f"/cloud/v3/gpu/baremetal/{project_id}/{region_id}/images/{image_id}",
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GPUImage:
        """
        Get bare metal GPU image by ID

        Args:
          project_id: '#/paths/%2Fcloud%2Fv3%2Fgpu%2Fbaremetal%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2Fimages%2F%7Bimage_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v3/gpu/baremetal/{project_id}/{region_id}/images/{image_id}'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv3%2Fgpu%2Fbaremetal%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2Fimages%2F%7Bimage_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v3/gpu/baremetal/{project_id}/{region_id}/images/{image_id}'].get.parameters[1].schema"

          image_id: '#/paths/%2Fcloud%2Fv3%2Fgpu%2Fbaremetal%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2Fimages%2F%7Bimage_id%7D/get/parameters/2/schema'
              "$.paths['/cloud/v3/gpu/baremetal/{project_id}/{region_id}/images/{image_id}'].get.parameters[2].schema"

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
            f"/cloud/v3/gpu/baremetal/{project_id}/{region_id}/images/{image_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GPUImage,
        )

    def upload(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        url: str,
        architecture: Optional[Literal["aarch64", "x86_64"]] | NotGiven = NOT_GIVEN,
        cow_format: bool | NotGiven = NOT_GIVEN,
        hw_firmware_type: Optional[Literal["bios", "uefi"]] | NotGiven = NOT_GIVEN,
        os_distro: Optional[str] | NotGiven = NOT_GIVEN,
        os_type: Optional[Literal["linux", "windows"]] | NotGiven = NOT_GIVEN,
        os_version: Optional[str] | NotGiven = NOT_GIVEN,
        ssh_key: Literal["allow", "deny", "required"] | NotGiven = NOT_GIVEN,
        tags: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Upload new bare metal GPU image

        Args:
          project_id: '#/paths/%2Fcloud%2Fv3%2Fgpu%2Fbaremetal%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2Fimages/post/parameters/0/schema'
              "$.paths['/cloud/v3/gpu/baremetal/{project_id}/{region_id}/images'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv3%2Fgpu%2Fbaremetal%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2Fimages/post/parameters/1/schema'
              "$.paths['/cloud/v3/gpu/baremetal/{project_id}/{region_id}/images'].post.parameters[1].schema"

          name: '#/components/schemas/UploadBaremetalGpuImageSerializer/properties/name'
              "$.components.schemas.UploadBaremetalGpuImageSerializer.properties.name"

          url: '#/components/schemas/UploadBaremetalGpuImageSerializer/properties/url/anyOf/0'
              "$.components.schemas.UploadBaremetalGpuImageSerializer.properties.url.anyOf[0]"

          architecture: '#/components/schemas/UploadBaremetalGpuImageSerializer/properties/architecture/anyOf/0'
              "$.components.schemas.UploadBaremetalGpuImageSerializer.properties.architecture.anyOf[0]"

          cow_format: '#/components/schemas/UploadBaremetalGpuImageSerializer/properties/cow_format'
              "$.components.schemas.UploadBaremetalGpuImageSerializer.properties.cow_format"

          hw_firmware_type: '#/components/schemas/UploadBaremetalGpuImageSerializer/properties/hw_firmware_type/anyOf/0'
              "$.components.schemas.UploadBaremetalGpuImageSerializer.properties.hw_firmware_type.anyOf[0]"

          os_distro: '#/components/schemas/UploadBaremetalGpuImageSerializer/properties/os_distro/anyOf/0'
              "$.components.schemas.UploadBaremetalGpuImageSerializer.properties.os_distro.anyOf[0]"

          os_type: '#/components/schemas/UploadBaremetalGpuImageSerializer/properties/os_type/anyOf/0'
              "$.components.schemas.UploadBaremetalGpuImageSerializer.properties.os_type.anyOf[0]"

          os_version: '#/components/schemas/UploadBaremetalGpuImageSerializer/properties/os_version/anyOf/0'
              "$.components.schemas.UploadBaremetalGpuImageSerializer.properties.os_version.anyOf[0]"

          ssh_key: '#/components/schemas/UploadBaremetalGpuImageSerializer/properties/ssh_key'
              "$.components.schemas.UploadBaremetalGpuImageSerializer.properties.ssh_key"

          tags: '#/components/schemas/UploadBaremetalGpuImageSerializer/properties/tags'
              "$.components.schemas.UploadBaremetalGpuImageSerializer.properties.tags"

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
            f"/cloud/v3/gpu/baremetal/{project_id}/{region_id}/images",
            body=maybe_transform(
                {
                    "name": name,
                    "url": url,
                    "architecture": architecture,
                    "cow_format": cow_format,
                    "hw_firmware_type": hw_firmware_type,
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

    async def list(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GPUImageList:
        """
        List bare metal GPU images

        Args:
          project_id: '#/paths/%2Fcloud%2Fv3%2Fgpu%2Fbaremetal%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2Fimages/get/parameters/0/schema'
              "$.paths['/cloud/v3/gpu/baremetal/{project_id}/{region_id}/images'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv3%2Fgpu%2Fbaremetal%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2Fimages/get/parameters/1/schema'
              "$.paths['/cloud/v3/gpu/baremetal/{project_id}/{region_id}/images'].get.parameters[1].schema"

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
            f"/cloud/v3/gpu/baremetal/{project_id}/{region_id}/images",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GPUImageList,
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
        Delete bare metal GPU image by ID

        Args:
          project_id: '#/paths/%2Fcloud%2Fv3%2Fgpu%2Fbaremetal%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2Fimages%2F%7Bimage_id%7D/delete/parameters/0/schema'
              "$.paths['/cloud/v3/gpu/baremetal/{project_id}/{region_id}/images/{image_id}']['delete'].parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv3%2Fgpu%2Fbaremetal%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2Fimages%2F%7Bimage_id%7D/delete/parameters/1/schema'
              "$.paths['/cloud/v3/gpu/baremetal/{project_id}/{region_id}/images/{image_id}']['delete'].parameters[1].schema"

          image_id: '#/paths/%2Fcloud%2Fv3%2Fgpu%2Fbaremetal%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2Fimages%2F%7Bimage_id%7D/delete/parameters/2/schema'
              "$.paths['/cloud/v3/gpu/baremetal/{project_id}/{region_id}/images/{image_id}']['delete'].parameters[2].schema"

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
            f"/cloud/v3/gpu/baremetal/{project_id}/{region_id}/images/{image_id}",
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GPUImage:
        """
        Get bare metal GPU image by ID

        Args:
          project_id: '#/paths/%2Fcloud%2Fv3%2Fgpu%2Fbaremetal%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2Fimages%2F%7Bimage_id%7D/get/parameters/0/schema'
              "$.paths['/cloud/v3/gpu/baremetal/{project_id}/{region_id}/images/{image_id}'].get.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv3%2Fgpu%2Fbaremetal%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2Fimages%2F%7Bimage_id%7D/get/parameters/1/schema'
              "$.paths['/cloud/v3/gpu/baremetal/{project_id}/{region_id}/images/{image_id}'].get.parameters[1].schema"

          image_id: '#/paths/%2Fcloud%2Fv3%2Fgpu%2Fbaremetal%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2Fimages%2F%7Bimage_id%7D/get/parameters/2/schema'
              "$.paths['/cloud/v3/gpu/baremetal/{project_id}/{region_id}/images/{image_id}'].get.parameters[2].schema"

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
            f"/cloud/v3/gpu/baremetal/{project_id}/{region_id}/images/{image_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GPUImage,
        )

    async def upload(
        self,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        name: str,
        url: str,
        architecture: Optional[Literal["aarch64", "x86_64"]] | NotGiven = NOT_GIVEN,
        cow_format: bool | NotGiven = NOT_GIVEN,
        hw_firmware_type: Optional[Literal["bios", "uefi"]] | NotGiven = NOT_GIVEN,
        os_distro: Optional[str] | NotGiven = NOT_GIVEN,
        os_type: Optional[Literal["linux", "windows"]] | NotGiven = NOT_GIVEN,
        os_version: Optional[str] | NotGiven = NOT_GIVEN,
        ssh_key: Literal["allow", "deny", "required"] | NotGiven = NOT_GIVEN,
        tags: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskIDList:
        """
        Upload new bare metal GPU image

        Args:
          project_id: '#/paths/%2Fcloud%2Fv3%2Fgpu%2Fbaremetal%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2Fimages/post/parameters/0/schema'
              "$.paths['/cloud/v3/gpu/baremetal/{project_id}/{region_id}/images'].post.parameters[0].schema"

          region_id: '#/paths/%2Fcloud%2Fv3%2Fgpu%2Fbaremetal%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2Fimages/post/parameters/1/schema'
              "$.paths['/cloud/v3/gpu/baremetal/{project_id}/{region_id}/images'].post.parameters[1].schema"

          name: '#/components/schemas/UploadBaremetalGpuImageSerializer/properties/name'
              "$.components.schemas.UploadBaremetalGpuImageSerializer.properties.name"

          url: '#/components/schemas/UploadBaremetalGpuImageSerializer/properties/url/anyOf/0'
              "$.components.schemas.UploadBaremetalGpuImageSerializer.properties.url.anyOf[0]"

          architecture: '#/components/schemas/UploadBaremetalGpuImageSerializer/properties/architecture/anyOf/0'
              "$.components.schemas.UploadBaremetalGpuImageSerializer.properties.architecture.anyOf[0]"

          cow_format: '#/components/schemas/UploadBaremetalGpuImageSerializer/properties/cow_format'
              "$.components.schemas.UploadBaremetalGpuImageSerializer.properties.cow_format"

          hw_firmware_type: '#/components/schemas/UploadBaremetalGpuImageSerializer/properties/hw_firmware_type/anyOf/0'
              "$.components.schemas.UploadBaremetalGpuImageSerializer.properties.hw_firmware_type.anyOf[0]"

          os_distro: '#/components/schemas/UploadBaremetalGpuImageSerializer/properties/os_distro/anyOf/0'
              "$.components.schemas.UploadBaremetalGpuImageSerializer.properties.os_distro.anyOf[0]"

          os_type: '#/components/schemas/UploadBaremetalGpuImageSerializer/properties/os_type/anyOf/0'
              "$.components.schemas.UploadBaremetalGpuImageSerializer.properties.os_type.anyOf[0]"

          os_version: '#/components/schemas/UploadBaremetalGpuImageSerializer/properties/os_version/anyOf/0'
              "$.components.schemas.UploadBaremetalGpuImageSerializer.properties.os_version.anyOf[0]"

          ssh_key: '#/components/schemas/UploadBaremetalGpuImageSerializer/properties/ssh_key'
              "$.components.schemas.UploadBaremetalGpuImageSerializer.properties.ssh_key"

          tags: '#/components/schemas/UploadBaremetalGpuImageSerializer/properties/tags'
              "$.components.schemas.UploadBaremetalGpuImageSerializer.properties.tags"

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
            f"/cloud/v3/gpu/baremetal/{project_id}/{region_id}/images",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "url": url,
                    "architecture": architecture,
                    "cow_format": cow_format,
                    "hw_firmware_type": hw_firmware_type,
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

        self.list = to_raw_response_wrapper(
            images.list,
        )
        self.delete = to_raw_response_wrapper(
            images.delete,
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

        self.list = async_to_raw_response_wrapper(
            images.list,
        )
        self.delete = async_to_raw_response_wrapper(
            images.delete,
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

        self.list = to_streamed_response_wrapper(
            images.list,
        )
        self.delete = to_streamed_response_wrapper(
            images.delete,
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

        self.list = async_to_streamed_response_wrapper(
            images.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            images.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            images.get,
        )
        self.upload = async_to_streamed_response_wrapper(
            images.upload,
        )
