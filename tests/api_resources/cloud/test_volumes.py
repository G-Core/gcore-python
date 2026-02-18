# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage
from gcore.types.cloud import (
    Volume,
    TaskIDList,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVolumes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: Gcore) -> None:
        volume = client.cloud.volumes.create(
            project_id=1,
            region_id=1,
            image_id="169942e0-9b53-42df-95ef-1a8b6525c2bd",
            name="volume-1",
            size=10,
            source="image",
        )
        assert_matches_type(TaskIDList, volume, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Gcore) -> None:
        volume = client.cloud.volumes.create(
            project_id=1,
            region_id=1,
            image_id="169942e0-9b53-42df-95ef-1a8b6525c2bd",
            name="volume-1",
            size=10,
            source="image",
            attachment_tag="device-tag",
            instance_id_to_attach_to="88f3e0bd-ca86-4cf7-be8b-dd2988e23c2d",
            lifecycle_policy_ids=[1, 2],
            tags={"foo": "my-tag-value"},
            type_name="standard",
        )
        assert_matches_type(TaskIDList, volume, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: Gcore) -> None:
        response = client.cloud.volumes.with_raw_response.create(
            project_id=1,
            region_id=1,
            image_id="169942e0-9b53-42df-95ef-1a8b6525c2bd",
            name="volume-1",
            size=10,
            source="image",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = response.parse()
        assert_matches_type(TaskIDList, volume, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: Gcore) -> None:
        with client.cloud.volumes.with_streaming_response.create(
            project_id=1,
            region_id=1,
            image_id="169942e0-9b53-42df-95ef-1a8b6525c2bd",
            name="volume-1",
            size=10,
            source="image",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = response.parse()
            assert_matches_type(TaskIDList, volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_2(self, client: Gcore) -> None:
        volume = client.cloud.volumes.create(
            project_id=1,
            region_id=1,
            name="volume-1",
            snapshot_id="88f3e0bd-ca86-4cf7-be8b-dd2988e23c2d",
            source="snapshot",
        )
        assert_matches_type(TaskIDList, volume, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Gcore) -> None:
        volume = client.cloud.volumes.create(
            project_id=1,
            region_id=1,
            name="volume-1",
            snapshot_id="88f3e0bd-ca86-4cf7-be8b-dd2988e23c2d",
            source="snapshot",
            attachment_tag="device-tag",
            instance_id_to_attach_to="88f3e0bd-ca86-4cf7-be8b-dd2988e23c2d",
            lifecycle_policy_ids=[1, 2],
            size=10,
            tags={"foo": "my-tag-value"},
            type_name="standard",
        )
        assert_matches_type(TaskIDList, volume, path=["response"])

    @parametrize
    def test_raw_response_create_overload_2(self, client: Gcore) -> None:
        response = client.cloud.volumes.with_raw_response.create(
            project_id=1,
            region_id=1,
            name="volume-1",
            snapshot_id="88f3e0bd-ca86-4cf7-be8b-dd2988e23c2d",
            source="snapshot",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = response.parse()
        assert_matches_type(TaskIDList, volume, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_2(self, client: Gcore) -> None:
        with client.cloud.volumes.with_streaming_response.create(
            project_id=1,
            region_id=1,
            name="volume-1",
            snapshot_id="88f3e0bd-ca86-4cf7-be8b-dd2988e23c2d",
            source="snapshot",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = response.parse()
            assert_matches_type(TaskIDList, volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_3(self, client: Gcore) -> None:
        volume = client.cloud.volumes.create(
            project_id=1,
            region_id=1,
            name="volume-1",
            size=10,
            source="new-volume",
        )
        assert_matches_type(TaskIDList, volume, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_3(self, client: Gcore) -> None:
        volume = client.cloud.volumes.create(
            project_id=1,
            region_id=1,
            name="volume-1",
            size=10,
            source="new-volume",
            attachment_tag="device-tag",
            instance_id_to_attach_to="88f3e0bd-ca86-4cf7-be8b-dd2988e23c2d",
            lifecycle_policy_ids=[1, 2],
            tags={"foo": "my-tag-value"},
            type_name="standard",
        )
        assert_matches_type(TaskIDList, volume, path=["response"])

    @parametrize
    def test_raw_response_create_overload_3(self, client: Gcore) -> None:
        response = client.cloud.volumes.with_raw_response.create(
            project_id=1,
            region_id=1,
            name="volume-1",
            size=10,
            source="new-volume",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = response.parse()
        assert_matches_type(TaskIDList, volume, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_3(self, client: Gcore) -> None:
        with client.cloud.volumes.with_streaming_response.create(
            project_id=1,
            region_id=1,
            name="volume-1",
            size=10,
            source="new-volume",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = response.parse()
            assert_matches_type(TaskIDList, volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        volume = client.cloud.volumes.update(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(Volume, volume, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gcore) -> None:
        volume = client.cloud.volumes.update(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
            name="some_name",
            tags={"foo": "my-tag-value"},
        )
        assert_matches_type(Volume, volume, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.cloud.volumes.with_raw_response.update(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = response.parse()
        assert_matches_type(Volume, volume, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.cloud.volumes.with_streaming_response.update(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = response.parse()
            assert_matches_type(Volume, volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `volume_id` but received ''"):
            client.cloud.volumes.with_raw_response.update(
                volume_id="",
                project_id=1,
                region_id=1,
            )

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        volume = client.cloud.volumes.list(
            project_id=1,
            region_id=1,
        )
        assert_matches_type(SyncOffsetPage[Volume], volume, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        volume = client.cloud.volumes.list(
            project_id=1,
            region_id=1,
            bootable=False,
            cluster_id="t12345",
            has_attachments=True,
            id_part="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            instance_id="169942e0-9b53-42df-95ef-1a8b6525c2bd",
            limit=1000,
            name_part="test",
            offset=0,
            tag_key=["key1", "key2"],
            tag_key_value="tag_key_value",
        )
        assert_matches_type(SyncOffsetPage[Volume], volume, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.volumes.with_raw_response.list(
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = response.parse()
        assert_matches_type(SyncOffsetPage[Volume], volume, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.volumes.with_streaming_response.list(
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = response.parse()
            assert_matches_type(SyncOffsetPage[Volume], volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        volume = client.cloud.volumes.delete(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(TaskIDList, volume, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Gcore) -> None:
        volume = client.cloud.volumes.delete(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
            snapshots="726ecfcc-7fd0-4e30-a86e-7892524aa483,726ecfcc-7fd0-4e30-a86e-7892524aa484",
        )
        assert_matches_type(TaskIDList, volume, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cloud.volumes.with_raw_response.delete(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = response.parse()
        assert_matches_type(TaskIDList, volume, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cloud.volumes.with_streaming_response.delete(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = response.parse()
            assert_matches_type(TaskIDList, volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `volume_id` but received ''"):
            client.cloud.volumes.with_raw_response.delete(
                volume_id="",
                project_id=1,
                region_id=1,
            )

    @parametrize
    def test_method_attach_to_instance(self, client: Gcore) -> None:
        volume = client.cloud.volumes.attach_to_instance(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
            instance_id="169942e0-9b53-42df-95ef-1a8b6525c2bd",
        )
        assert_matches_type(TaskIDList, volume, path=["response"])

    @parametrize
    def test_method_attach_to_instance_with_all_params(self, client: Gcore) -> None:
        volume = client.cloud.volumes.attach_to_instance(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
            instance_id="169942e0-9b53-42df-95ef-1a8b6525c2bd",
            attachment_tag="boot",
        )
        assert_matches_type(TaskIDList, volume, path=["response"])

    @parametrize
    def test_raw_response_attach_to_instance(self, client: Gcore) -> None:
        response = client.cloud.volumes.with_raw_response.attach_to_instance(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
            instance_id="169942e0-9b53-42df-95ef-1a8b6525c2bd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = response.parse()
        assert_matches_type(TaskIDList, volume, path=["response"])

    @parametrize
    def test_streaming_response_attach_to_instance(self, client: Gcore) -> None:
        with client.cloud.volumes.with_streaming_response.attach_to_instance(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
            instance_id="169942e0-9b53-42df-95ef-1a8b6525c2bd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = response.parse()
            assert_matches_type(TaskIDList, volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_attach_to_instance(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `volume_id` but received ''"):
            client.cloud.volumes.with_raw_response.attach_to_instance(
                volume_id="",
                project_id=1,
                region_id=1,
                instance_id="169942e0-9b53-42df-95ef-1a8b6525c2bd",
            )

    @parametrize
    def test_method_change_type(self, client: Gcore) -> None:
        volume = client.cloud.volumes.change_type(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
            volume_type="ssd_hiiops",
        )
        assert_matches_type(Volume, volume, path=["response"])

    @parametrize
    def test_raw_response_change_type(self, client: Gcore) -> None:
        response = client.cloud.volumes.with_raw_response.change_type(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
            volume_type="ssd_hiiops",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = response.parse()
        assert_matches_type(Volume, volume, path=["response"])

    @parametrize
    def test_streaming_response_change_type(self, client: Gcore) -> None:
        with client.cloud.volumes.with_streaming_response.change_type(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
            volume_type="ssd_hiiops",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = response.parse()
            assert_matches_type(Volume, volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_change_type(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `volume_id` but received ''"):
            client.cloud.volumes.with_raw_response.change_type(
                volume_id="",
                project_id=1,
                region_id=1,
                volume_type="ssd_hiiops",
            )

    @parametrize
    def test_method_detach_from_instance(self, client: Gcore) -> None:
        volume = client.cloud.volumes.detach_from_instance(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
            instance_id="169942e0-9b53-42df-95ef-1a8b6525c2bd",
        )
        assert_matches_type(TaskIDList, volume, path=["response"])

    @parametrize
    def test_raw_response_detach_from_instance(self, client: Gcore) -> None:
        response = client.cloud.volumes.with_raw_response.detach_from_instance(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
            instance_id="169942e0-9b53-42df-95ef-1a8b6525c2bd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = response.parse()
        assert_matches_type(TaskIDList, volume, path=["response"])

    @parametrize
    def test_streaming_response_detach_from_instance(self, client: Gcore) -> None:
        with client.cloud.volumes.with_streaming_response.detach_from_instance(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
            instance_id="169942e0-9b53-42df-95ef-1a8b6525c2bd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = response.parse()
            assert_matches_type(TaskIDList, volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_detach_from_instance(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `volume_id` but received ''"):
            client.cloud.volumes.with_raw_response.detach_from_instance(
                volume_id="",
                project_id=1,
                region_id=1,
                instance_id="169942e0-9b53-42df-95ef-1a8b6525c2bd",
            )

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        volume = client.cloud.volumes.get(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(Volume, volume, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cloud.volumes.with_raw_response.get(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = response.parse()
        assert_matches_type(Volume, volume, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cloud.volumes.with_streaming_response.get(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = response.parse()
            assert_matches_type(Volume, volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `volume_id` but received ''"):
            client.cloud.volumes.with_raw_response.get(
                volume_id="",
                project_id=1,
                region_id=1,
            )

    @parametrize
    def test_method_resize(self, client: Gcore) -> None:
        volume = client.cloud.volumes.resize(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
            size=100,
        )
        assert_matches_type(TaskIDList, volume, path=["response"])

    @parametrize
    def test_raw_response_resize(self, client: Gcore) -> None:
        response = client.cloud.volumes.with_raw_response.resize(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
            size=100,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = response.parse()
        assert_matches_type(TaskIDList, volume, path=["response"])

    @parametrize
    def test_streaming_response_resize(self, client: Gcore) -> None:
        with client.cloud.volumes.with_streaming_response.resize(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
            size=100,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = response.parse()
            assert_matches_type(TaskIDList, volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_resize(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `volume_id` but received ''"):
            client.cloud.volumes.with_raw_response.resize(
                volume_id="",
                project_id=1,
                region_id=1,
                size=100,
            )

    @parametrize
    def test_method_revert_to_last_snapshot(self, client: Gcore) -> None:
        volume = client.cloud.volumes.revert_to_last_snapshot(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
        )
        assert volume is None

    @parametrize
    def test_raw_response_revert_to_last_snapshot(self, client: Gcore) -> None:
        response = client.cloud.volumes.with_raw_response.revert_to_last_snapshot(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = response.parse()
        assert volume is None

    @parametrize
    def test_streaming_response_revert_to_last_snapshot(self, client: Gcore) -> None:
        with client.cloud.volumes.with_streaming_response.revert_to_last_snapshot(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = response.parse()
            assert volume is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_revert_to_last_snapshot(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `volume_id` but received ''"):
            client.cloud.volumes.with_raw_response.revert_to_last_snapshot(
                volume_id="",
                project_id=1,
                region_id=1,
            )


class TestAsyncVolumes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncGcore) -> None:
        volume = await async_client.cloud.volumes.create(
            project_id=1,
            region_id=1,
            image_id="169942e0-9b53-42df-95ef-1a8b6525c2bd",
            name="volume-1",
            size=10,
            source="image",
        )
        assert_matches_type(TaskIDList, volume, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncGcore) -> None:
        volume = await async_client.cloud.volumes.create(
            project_id=1,
            region_id=1,
            image_id="169942e0-9b53-42df-95ef-1a8b6525c2bd",
            name="volume-1",
            size=10,
            source="image",
            attachment_tag="device-tag",
            instance_id_to_attach_to="88f3e0bd-ca86-4cf7-be8b-dd2988e23c2d",
            lifecycle_policy_ids=[1, 2],
            tags={"foo": "my-tag-value"},
            type_name="standard",
        )
        assert_matches_type(TaskIDList, volume, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.volumes.with_raw_response.create(
            project_id=1,
            region_id=1,
            image_id="169942e0-9b53-42df-95ef-1a8b6525c2bd",
            name="volume-1",
            size=10,
            source="image",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = await response.parse()
        assert_matches_type(TaskIDList, volume, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.volumes.with_streaming_response.create(
            project_id=1,
            region_id=1,
            image_id="169942e0-9b53-42df-95ef-1a8b6525c2bd",
            name="volume-1",
            size=10,
            source="image",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = await response.parse()
            assert_matches_type(TaskIDList, volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncGcore) -> None:
        volume = await async_client.cloud.volumes.create(
            project_id=1,
            region_id=1,
            name="volume-1",
            snapshot_id="88f3e0bd-ca86-4cf7-be8b-dd2988e23c2d",
            source="snapshot",
        )
        assert_matches_type(TaskIDList, volume, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncGcore) -> None:
        volume = await async_client.cloud.volumes.create(
            project_id=1,
            region_id=1,
            name="volume-1",
            snapshot_id="88f3e0bd-ca86-4cf7-be8b-dd2988e23c2d",
            source="snapshot",
            attachment_tag="device-tag",
            instance_id_to_attach_to="88f3e0bd-ca86-4cf7-be8b-dd2988e23c2d",
            lifecycle_policy_ids=[1, 2],
            size=10,
            tags={"foo": "my-tag-value"},
            type_name="standard",
        )
        assert_matches_type(TaskIDList, volume, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.volumes.with_raw_response.create(
            project_id=1,
            region_id=1,
            name="volume-1",
            snapshot_id="88f3e0bd-ca86-4cf7-be8b-dd2988e23c2d",
            source="snapshot",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = await response.parse()
        assert_matches_type(TaskIDList, volume, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.volumes.with_streaming_response.create(
            project_id=1,
            region_id=1,
            name="volume-1",
            snapshot_id="88f3e0bd-ca86-4cf7-be8b-dd2988e23c2d",
            source="snapshot",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = await response.parse()
            assert_matches_type(TaskIDList, volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_3(self, async_client: AsyncGcore) -> None:
        volume = await async_client.cloud.volumes.create(
            project_id=1,
            region_id=1,
            name="volume-1",
            size=10,
            source="new-volume",
        )
        assert_matches_type(TaskIDList, volume, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_3(self, async_client: AsyncGcore) -> None:
        volume = await async_client.cloud.volumes.create(
            project_id=1,
            region_id=1,
            name="volume-1",
            size=10,
            source="new-volume",
            attachment_tag="device-tag",
            instance_id_to_attach_to="88f3e0bd-ca86-4cf7-be8b-dd2988e23c2d",
            lifecycle_policy_ids=[1, 2],
            tags={"foo": "my-tag-value"},
            type_name="standard",
        )
        assert_matches_type(TaskIDList, volume, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_3(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.volumes.with_raw_response.create(
            project_id=1,
            region_id=1,
            name="volume-1",
            size=10,
            source="new-volume",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = await response.parse()
        assert_matches_type(TaskIDList, volume, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_3(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.volumes.with_streaming_response.create(
            project_id=1,
            region_id=1,
            name="volume-1",
            size=10,
            source="new-volume",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = await response.parse()
            assert_matches_type(TaskIDList, volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        volume = await async_client.cloud.volumes.update(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(Volume, volume, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGcore) -> None:
        volume = await async_client.cloud.volumes.update(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
            name="some_name",
            tags={"foo": "my-tag-value"},
        )
        assert_matches_type(Volume, volume, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.volumes.with_raw_response.update(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = await response.parse()
        assert_matches_type(Volume, volume, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.volumes.with_streaming_response.update(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = await response.parse()
            assert_matches_type(Volume, volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `volume_id` but received ''"):
            await async_client.cloud.volumes.with_raw_response.update(
                volume_id="",
                project_id=1,
                region_id=1,
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        volume = await async_client.cloud.volumes.list(
            project_id=1,
            region_id=1,
        )
        assert_matches_type(AsyncOffsetPage[Volume], volume, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        volume = await async_client.cloud.volumes.list(
            project_id=1,
            region_id=1,
            bootable=False,
            cluster_id="t12345",
            has_attachments=True,
            id_part="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            instance_id="169942e0-9b53-42df-95ef-1a8b6525c2bd",
            limit=1000,
            name_part="test",
            offset=0,
            tag_key=["key1", "key2"],
            tag_key_value="tag_key_value",
        )
        assert_matches_type(AsyncOffsetPage[Volume], volume, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.volumes.with_raw_response.list(
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = await response.parse()
        assert_matches_type(AsyncOffsetPage[Volume], volume, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.volumes.with_streaming_response.list(
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = await response.parse()
            assert_matches_type(AsyncOffsetPage[Volume], volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        volume = await async_client.cloud.volumes.delete(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(TaskIDList, volume, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncGcore) -> None:
        volume = await async_client.cloud.volumes.delete(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
            snapshots="726ecfcc-7fd0-4e30-a86e-7892524aa483,726ecfcc-7fd0-4e30-a86e-7892524aa484",
        )
        assert_matches_type(TaskIDList, volume, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.volumes.with_raw_response.delete(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = await response.parse()
        assert_matches_type(TaskIDList, volume, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.volumes.with_streaming_response.delete(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = await response.parse()
            assert_matches_type(TaskIDList, volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `volume_id` but received ''"):
            await async_client.cloud.volumes.with_raw_response.delete(
                volume_id="",
                project_id=1,
                region_id=1,
            )

    @parametrize
    async def test_method_attach_to_instance(self, async_client: AsyncGcore) -> None:
        volume = await async_client.cloud.volumes.attach_to_instance(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
            instance_id="169942e0-9b53-42df-95ef-1a8b6525c2bd",
        )
        assert_matches_type(TaskIDList, volume, path=["response"])

    @parametrize
    async def test_method_attach_to_instance_with_all_params(self, async_client: AsyncGcore) -> None:
        volume = await async_client.cloud.volumes.attach_to_instance(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
            instance_id="169942e0-9b53-42df-95ef-1a8b6525c2bd",
            attachment_tag="boot",
        )
        assert_matches_type(TaskIDList, volume, path=["response"])

    @parametrize
    async def test_raw_response_attach_to_instance(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.volumes.with_raw_response.attach_to_instance(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
            instance_id="169942e0-9b53-42df-95ef-1a8b6525c2bd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = await response.parse()
        assert_matches_type(TaskIDList, volume, path=["response"])

    @parametrize
    async def test_streaming_response_attach_to_instance(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.volumes.with_streaming_response.attach_to_instance(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
            instance_id="169942e0-9b53-42df-95ef-1a8b6525c2bd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = await response.parse()
            assert_matches_type(TaskIDList, volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_attach_to_instance(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `volume_id` but received ''"):
            await async_client.cloud.volumes.with_raw_response.attach_to_instance(
                volume_id="",
                project_id=1,
                region_id=1,
                instance_id="169942e0-9b53-42df-95ef-1a8b6525c2bd",
            )

    @parametrize
    async def test_method_change_type(self, async_client: AsyncGcore) -> None:
        volume = await async_client.cloud.volumes.change_type(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
            volume_type="ssd_hiiops",
        )
        assert_matches_type(Volume, volume, path=["response"])

    @parametrize
    async def test_raw_response_change_type(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.volumes.with_raw_response.change_type(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
            volume_type="ssd_hiiops",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = await response.parse()
        assert_matches_type(Volume, volume, path=["response"])

    @parametrize
    async def test_streaming_response_change_type(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.volumes.with_streaming_response.change_type(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
            volume_type="ssd_hiiops",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = await response.parse()
            assert_matches_type(Volume, volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_change_type(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `volume_id` but received ''"):
            await async_client.cloud.volumes.with_raw_response.change_type(
                volume_id="",
                project_id=1,
                region_id=1,
                volume_type="ssd_hiiops",
            )

    @parametrize
    async def test_method_detach_from_instance(self, async_client: AsyncGcore) -> None:
        volume = await async_client.cloud.volumes.detach_from_instance(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
            instance_id="169942e0-9b53-42df-95ef-1a8b6525c2bd",
        )
        assert_matches_type(TaskIDList, volume, path=["response"])

    @parametrize
    async def test_raw_response_detach_from_instance(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.volumes.with_raw_response.detach_from_instance(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
            instance_id="169942e0-9b53-42df-95ef-1a8b6525c2bd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = await response.parse()
        assert_matches_type(TaskIDList, volume, path=["response"])

    @parametrize
    async def test_streaming_response_detach_from_instance(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.volumes.with_streaming_response.detach_from_instance(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
            instance_id="169942e0-9b53-42df-95ef-1a8b6525c2bd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = await response.parse()
            assert_matches_type(TaskIDList, volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_detach_from_instance(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `volume_id` but received ''"):
            await async_client.cloud.volumes.with_raw_response.detach_from_instance(
                volume_id="",
                project_id=1,
                region_id=1,
                instance_id="169942e0-9b53-42df-95ef-1a8b6525c2bd",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        volume = await async_client.cloud.volumes.get(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(Volume, volume, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.volumes.with_raw_response.get(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = await response.parse()
        assert_matches_type(Volume, volume, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.volumes.with_streaming_response.get(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = await response.parse()
            assert_matches_type(Volume, volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `volume_id` but received ''"):
            await async_client.cloud.volumes.with_raw_response.get(
                volume_id="",
                project_id=1,
                region_id=1,
            )

    @parametrize
    async def test_method_resize(self, async_client: AsyncGcore) -> None:
        volume = await async_client.cloud.volumes.resize(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
            size=100,
        )
        assert_matches_type(TaskIDList, volume, path=["response"])

    @parametrize
    async def test_raw_response_resize(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.volumes.with_raw_response.resize(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
            size=100,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = await response.parse()
        assert_matches_type(TaskIDList, volume, path=["response"])

    @parametrize
    async def test_streaming_response_resize(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.volumes.with_streaming_response.resize(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
            size=100,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = await response.parse()
            assert_matches_type(TaskIDList, volume, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_resize(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `volume_id` but received ''"):
            await async_client.cloud.volumes.with_raw_response.resize(
                volume_id="",
                project_id=1,
                region_id=1,
                size=100,
            )

    @parametrize
    async def test_method_revert_to_last_snapshot(self, async_client: AsyncGcore) -> None:
        volume = await async_client.cloud.volumes.revert_to_last_snapshot(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
        )
        assert volume is None

    @parametrize
    async def test_raw_response_revert_to_last_snapshot(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.volumes.with_raw_response.revert_to_last_snapshot(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = await response.parse()
        assert volume is None

    @parametrize
    async def test_streaming_response_revert_to_last_snapshot(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.volumes.with_streaming_response.revert_to_last_snapshot(
            volume_id="726ecfcc-7fd0-4e30-a86e-7892524aa483",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = await response.parse()
            assert volume is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_revert_to_last_snapshot(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `volume_id` but received ''"):
            await async_client.cloud.volumes.with_raw_response.revert_to_last_snapshot(
                volume_id="",
                project_id=1,
                region_id=1,
            )
