# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cloud import GPUImage, TaskIDList, GPUImageList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestImages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        image = client.cloud.gpu_virtual.clusters.images.list(
            project_id=1,
            region_id=7,
        )
        assert_matches_type(GPUImageList, image, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.gpu_virtual.clusters.images.with_raw_response.list(
            project_id=1,
            region_id=7,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = response.parse()
        assert_matches_type(GPUImageList, image, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.gpu_virtual.clusters.images.with_streaming_response.list(
            project_id=1,
            region_id=7,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = response.parse()
            assert_matches_type(GPUImageList, image, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        image = client.cloud.gpu_virtual.clusters.images.delete(
            image_id="8cab6f28-09ca-4201-b3f7-23c7893f4bd6",
            project_id=1,
            region_id=7,
        )
        assert_matches_type(TaskIDList, image, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cloud.gpu_virtual.clusters.images.with_raw_response.delete(
            image_id="8cab6f28-09ca-4201-b3f7-23c7893f4bd6",
            project_id=1,
            region_id=7,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = response.parse()
        assert_matches_type(TaskIDList, image, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cloud.gpu_virtual.clusters.images.with_streaming_response.delete(
            image_id="8cab6f28-09ca-4201-b3f7-23c7893f4bd6",
            project_id=1,
            region_id=7,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = response.parse()
            assert_matches_type(TaskIDList, image, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `image_id` but received ''"):
            client.cloud.gpu_virtual.clusters.images.with_raw_response.delete(
                image_id="",
                project_id=1,
                region_id=7,
            )

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        image = client.cloud.gpu_virtual.clusters.images.get(
            image_id="8cab6f28-09ca-4201-b3f7-23c7893f4bd6",
            project_id=1,
            region_id=7,
        )
        assert_matches_type(GPUImage, image, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cloud.gpu_virtual.clusters.images.with_raw_response.get(
            image_id="8cab6f28-09ca-4201-b3f7-23c7893f4bd6",
            project_id=1,
            region_id=7,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = response.parse()
        assert_matches_type(GPUImage, image, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cloud.gpu_virtual.clusters.images.with_streaming_response.get(
            image_id="8cab6f28-09ca-4201-b3f7-23c7893f4bd6",
            project_id=1,
            region_id=7,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = response.parse()
            assert_matches_type(GPUImage, image, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `image_id` but received ''"):
            client.cloud.gpu_virtual.clusters.images.with_raw_response.get(
                image_id="",
                project_id=1,
                region_id=7,
            )

    @parametrize
    def test_method_upload(self, client: Gcore) -> None:
        image = client.cloud.gpu_virtual.clusters.images.upload(
            project_id=1,
            region_id=7,
            name="ubuntu-23.10-x64",
            url="http://mirror.noris.net/cirros/0.4.0/cirros-0.4.0-x86_64-disk.img",
        )
        assert_matches_type(TaskIDList, image, path=["response"])

    @parametrize
    def test_method_upload_with_all_params(self, client: Gcore) -> None:
        image = client.cloud.gpu_virtual.clusters.images.upload(
            project_id=1,
            region_id=7,
            name="ubuntu-23.10-x64",
            url="http://mirror.noris.net/cirros/0.4.0/cirros-0.4.0-x86_64-disk.img",
            architecture="x86_64",
            cow_format=True,
            hw_firmware_type="bios",
            os_distro="os_distro",
            os_type="linux",
            os_version="19.04",
            ssh_key="allow",
            tags={"my-tag": "my-tag-value"},
        )
        assert_matches_type(TaskIDList, image, path=["response"])

    @parametrize
    def test_raw_response_upload(self, client: Gcore) -> None:
        response = client.cloud.gpu_virtual.clusters.images.with_raw_response.upload(
            project_id=1,
            region_id=7,
            name="ubuntu-23.10-x64",
            url="http://mirror.noris.net/cirros/0.4.0/cirros-0.4.0-x86_64-disk.img",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = response.parse()
        assert_matches_type(TaskIDList, image, path=["response"])

    @parametrize
    def test_streaming_response_upload(self, client: Gcore) -> None:
        with client.cloud.gpu_virtual.clusters.images.with_streaming_response.upload(
            project_id=1,
            region_id=7,
            name="ubuntu-23.10-x64",
            url="http://mirror.noris.net/cirros/0.4.0/cirros-0.4.0-x86_64-disk.img",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = response.parse()
            assert_matches_type(TaskIDList, image, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncImages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        image = await async_client.cloud.gpu_virtual.clusters.images.list(
            project_id=1,
            region_id=7,
        )
        assert_matches_type(GPUImageList, image, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.gpu_virtual.clusters.images.with_raw_response.list(
            project_id=1,
            region_id=7,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = await response.parse()
        assert_matches_type(GPUImageList, image, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.gpu_virtual.clusters.images.with_streaming_response.list(
            project_id=1,
            region_id=7,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = await response.parse()
            assert_matches_type(GPUImageList, image, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        image = await async_client.cloud.gpu_virtual.clusters.images.delete(
            image_id="8cab6f28-09ca-4201-b3f7-23c7893f4bd6",
            project_id=1,
            region_id=7,
        )
        assert_matches_type(TaskIDList, image, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.gpu_virtual.clusters.images.with_raw_response.delete(
            image_id="8cab6f28-09ca-4201-b3f7-23c7893f4bd6",
            project_id=1,
            region_id=7,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = await response.parse()
        assert_matches_type(TaskIDList, image, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.gpu_virtual.clusters.images.with_streaming_response.delete(
            image_id="8cab6f28-09ca-4201-b3f7-23c7893f4bd6",
            project_id=1,
            region_id=7,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = await response.parse()
            assert_matches_type(TaskIDList, image, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `image_id` but received ''"):
            await async_client.cloud.gpu_virtual.clusters.images.with_raw_response.delete(
                image_id="",
                project_id=1,
                region_id=7,
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        image = await async_client.cloud.gpu_virtual.clusters.images.get(
            image_id="8cab6f28-09ca-4201-b3f7-23c7893f4bd6",
            project_id=1,
            region_id=7,
        )
        assert_matches_type(GPUImage, image, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.gpu_virtual.clusters.images.with_raw_response.get(
            image_id="8cab6f28-09ca-4201-b3f7-23c7893f4bd6",
            project_id=1,
            region_id=7,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = await response.parse()
        assert_matches_type(GPUImage, image, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.gpu_virtual.clusters.images.with_streaming_response.get(
            image_id="8cab6f28-09ca-4201-b3f7-23c7893f4bd6",
            project_id=1,
            region_id=7,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = await response.parse()
            assert_matches_type(GPUImage, image, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `image_id` but received ''"):
            await async_client.cloud.gpu_virtual.clusters.images.with_raw_response.get(
                image_id="",
                project_id=1,
                region_id=7,
            )

    @parametrize
    async def test_method_upload(self, async_client: AsyncGcore) -> None:
        image = await async_client.cloud.gpu_virtual.clusters.images.upload(
            project_id=1,
            region_id=7,
            name="ubuntu-23.10-x64",
            url="http://mirror.noris.net/cirros/0.4.0/cirros-0.4.0-x86_64-disk.img",
        )
        assert_matches_type(TaskIDList, image, path=["response"])

    @parametrize
    async def test_method_upload_with_all_params(self, async_client: AsyncGcore) -> None:
        image = await async_client.cloud.gpu_virtual.clusters.images.upload(
            project_id=1,
            region_id=7,
            name="ubuntu-23.10-x64",
            url="http://mirror.noris.net/cirros/0.4.0/cirros-0.4.0-x86_64-disk.img",
            architecture="x86_64",
            cow_format=True,
            hw_firmware_type="bios",
            os_distro="os_distro",
            os_type="linux",
            os_version="19.04",
            ssh_key="allow",
            tags={"my-tag": "my-tag-value"},
        )
        assert_matches_type(TaskIDList, image, path=["response"])

    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.gpu_virtual.clusters.images.with_raw_response.upload(
            project_id=1,
            region_id=7,
            name="ubuntu-23.10-x64",
            url="http://mirror.noris.net/cirros/0.4.0/cirros-0.4.0-x86_64-disk.img",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = await response.parse()
        assert_matches_type(TaskIDList, image, path=["response"])

    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.gpu_virtual.clusters.images.with_streaming_response.upload(
            project_id=1,
            region_id=7,
            name="ubuntu-23.10-x64",
            url="http://mirror.noris.net/cirros/0.4.0/cirros-0.4.0-x86_64-disk.img",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = await response.parse()
            assert_matches_type(TaskIDList, image, path=["response"])

        assert cast(Any, response.is_closed) is True
