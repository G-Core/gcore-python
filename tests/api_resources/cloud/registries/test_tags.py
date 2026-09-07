# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTags:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        tag = client.cloud.registries.tags.delete(
            tag_name="latest",
            project_id=1,
            region_id=1,
            registry_id=1,
            repository_name="nginx",
            digest="sha256:5414002a0c147f8e41da0d0764b5074480012852d5d9a0ef8bd2fec904e62b7c",
        )
        assert tag is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cloud.registries.tags.with_raw_response.delete(
            tag_name="latest",
            project_id=1,
            region_id=1,
            registry_id=1,
            repository_name="nginx",
            digest="sha256:5414002a0c147f8e41da0d0764b5074480012852d5d9a0ef8bd2fec904e62b7c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert tag is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cloud.registries.tags.with_streaming_response.delete(
            tag_name="latest",
            project_id=1,
            region_id=1,
            registry_id=1,
            repository_name="nginx",
            digest="sha256:5414002a0c147f8e41da0d0764b5074480012852d5d9a0ef8bd2fec904e62b7c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert tag is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repository_name` but received ''"):
            client.cloud.registries.tags.with_raw_response.delete(
                tag_name="latest",
                project_id=1,
                region_id=1,
                registry_id=1,
                repository_name="",
                digest="sha256:5414002a0c147f8e41da0d0764b5074480012852d5d9a0ef8bd2fec904e62b7c",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `digest` but received ''"):
            client.cloud.registries.tags.with_raw_response.delete(
                tag_name="latest",
                project_id=1,
                region_id=1,
                registry_id=1,
                repository_name="nginx",
                digest="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tag_name` but received ''"):
            client.cloud.registries.tags.with_raw_response.delete(
                tag_name="",
                project_id=1,
                region_id=1,
                registry_id=1,
                repository_name="nginx",
                digest="sha256:5414002a0c147f8e41da0d0764b5074480012852d5d9a0ef8bd2fec904e62b7c",
            )


class TestAsyncTags:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        tag = await async_client.cloud.registries.tags.delete(
            tag_name="latest",
            project_id=1,
            region_id=1,
            registry_id=1,
            repository_name="nginx",
            digest="sha256:5414002a0c147f8e41da0d0764b5074480012852d5d9a0ef8bd2fec904e62b7c",
        )
        assert tag is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.registries.tags.with_raw_response.delete(
            tag_name="latest",
            project_id=1,
            region_id=1,
            registry_id=1,
            repository_name="nginx",
            digest="sha256:5414002a0c147f8e41da0d0764b5074480012852d5d9a0ef8bd2fec904e62b7c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert tag is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.registries.tags.with_streaming_response.delete(
            tag_name="latest",
            project_id=1,
            region_id=1,
            registry_id=1,
            repository_name="nginx",
            digest="sha256:5414002a0c147f8e41da0d0764b5074480012852d5d9a0ef8bd2fec904e62b7c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert tag is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `repository_name` but received ''"):
            await async_client.cloud.registries.tags.with_raw_response.delete(
                tag_name="latest",
                project_id=1,
                region_id=1,
                registry_id=1,
                repository_name="",
                digest="sha256:5414002a0c147f8e41da0d0764b5074480012852d5d9a0ef8bd2fec904e62b7c",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `digest` but received ''"):
            await async_client.cloud.registries.tags.with_raw_response.delete(
                tag_name="latest",
                project_id=1,
                region_id=1,
                registry_id=1,
                repository_name="nginx",
                digest="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tag_name` but received ''"):
            await async_client.cloud.registries.tags.with_raw_response.delete(
                tag_name="",
                project_id=1,
                region_id=1,
                registry_id=1,
                repository_name="nginx",
                digest="sha256:5414002a0c147f8e41da0d0764b5074480012852d5d9a0ef8bd2fec904e62b7c",
            )
