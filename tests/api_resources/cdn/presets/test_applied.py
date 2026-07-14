# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cdn.presets import AppliedPreset, AppliedPresetFields, AppliedApplyResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestApplied:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_apply(self, client: Gcore) -> None:
        applied = client.cdn.presets.applied.apply(
            preset_id=0,
            object_id=7531,
        )
        assert_matches_type(AppliedApplyResponse, applied, path=["response"])

    @parametrize
    def test_raw_response_apply(self, client: Gcore) -> None:
        response = client.cdn.presets.applied.with_raw_response.apply(
            preset_id=0,
            object_id=7531,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        applied = response.parse()
        assert_matches_type(AppliedApplyResponse, applied, path=["response"])

    @parametrize
    def test_streaming_response_apply(self, client: Gcore) -> None:
        with client.cdn.presets.applied.with_streaming_response.apply(
            preset_id=0,
            object_id=7531,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            applied = response.parse()
            assert_matches_type(AppliedApplyResponse, applied, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_objects(self, client: Gcore) -> None:
        applied = client.cdn.presets.applied.get_objects(
            0,
        )
        assert_matches_type(AppliedPreset, applied, path=["response"])

    @parametrize
    def test_raw_response_get_objects(self, client: Gcore) -> None:
        response = client.cdn.presets.applied.with_raw_response.get_objects(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        applied = response.parse()
        assert_matches_type(AppliedPreset, applied, path=["response"])

    @parametrize
    def test_streaming_response_get_objects(self, client: Gcore) -> None:
        with client.cdn.presets.applied.with_streaming_response.get_objects(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            applied = response.parse()
            assert_matches_type(AppliedPreset, applied, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_resource_preset(self, client: Gcore) -> None:
        applied = client.cdn.presets.applied.get_resource_preset(
            0,
        )
        assert_matches_type(AppliedPresetFields, applied, path=["response"])

    @parametrize
    def test_raw_response_get_resource_preset(self, client: Gcore) -> None:
        response = client.cdn.presets.applied.with_raw_response.get_resource_preset(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        applied = response.parse()
        assert_matches_type(AppliedPresetFields, applied, path=["response"])

    @parametrize
    def test_streaming_response_get_resource_preset(self, client: Gcore) -> None:
        with client.cdn.presets.applied.with_streaming_response.get_resource_preset(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            applied = response.parse()
            assert_matches_type(AppliedPresetFields, applied, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_rule_preset(self, client: Gcore) -> None:
        applied = client.cdn.presets.applied.get_rule_preset(
            rule_id=0,
            resource_id=0,
        )
        assert_matches_type(AppliedPresetFields, applied, path=["response"])

    @parametrize
    def test_raw_response_get_rule_preset(self, client: Gcore) -> None:
        response = client.cdn.presets.applied.with_raw_response.get_rule_preset(
            rule_id=0,
            resource_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        applied = response.parse()
        assert_matches_type(AppliedPresetFields, applied, path=["response"])

    @parametrize
    def test_streaming_response_get_rule_preset(self, client: Gcore) -> None:
        with client.cdn.presets.applied.with_streaming_response.get_rule_preset(
            rule_id=0,
            resource_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            applied = response.parse()
            assert_matches_type(AppliedPresetFields, applied, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unapply(self, client: Gcore) -> None:
        applied = client.cdn.presets.applied.unapply(
            object_id=0,
            preset_id=0,
        )
        assert applied is None

    @parametrize
    def test_raw_response_unapply(self, client: Gcore) -> None:
        response = client.cdn.presets.applied.with_raw_response.unapply(
            object_id=0,
            preset_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        applied = response.parse()
        assert applied is None

    @parametrize
    def test_streaming_response_unapply(self, client: Gcore) -> None:
        with client.cdn.presets.applied.with_streaming_response.unapply(
            object_id=0,
            preset_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            applied = response.parse()
            assert applied is None

        assert cast(Any, response.is_closed) is True


class TestAsyncApplied:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_apply(self, async_client: AsyncGcore) -> None:
        applied = await async_client.cdn.presets.applied.apply(
            preset_id=0,
            object_id=7531,
        )
        assert_matches_type(AppliedApplyResponse, applied, path=["response"])

    @parametrize
    async def test_raw_response_apply(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.presets.applied.with_raw_response.apply(
            preset_id=0,
            object_id=7531,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        applied = await response.parse()
        assert_matches_type(AppliedApplyResponse, applied, path=["response"])

    @parametrize
    async def test_streaming_response_apply(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.presets.applied.with_streaming_response.apply(
            preset_id=0,
            object_id=7531,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            applied = await response.parse()
            assert_matches_type(AppliedApplyResponse, applied, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_objects(self, async_client: AsyncGcore) -> None:
        applied = await async_client.cdn.presets.applied.get_objects(
            0,
        )
        assert_matches_type(AppliedPreset, applied, path=["response"])

    @parametrize
    async def test_raw_response_get_objects(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.presets.applied.with_raw_response.get_objects(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        applied = await response.parse()
        assert_matches_type(AppliedPreset, applied, path=["response"])

    @parametrize
    async def test_streaming_response_get_objects(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.presets.applied.with_streaming_response.get_objects(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            applied = await response.parse()
            assert_matches_type(AppliedPreset, applied, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_resource_preset(self, async_client: AsyncGcore) -> None:
        applied = await async_client.cdn.presets.applied.get_resource_preset(
            0,
        )
        assert_matches_type(AppliedPresetFields, applied, path=["response"])

    @parametrize
    async def test_raw_response_get_resource_preset(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.presets.applied.with_raw_response.get_resource_preset(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        applied = await response.parse()
        assert_matches_type(AppliedPresetFields, applied, path=["response"])

    @parametrize
    async def test_streaming_response_get_resource_preset(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.presets.applied.with_streaming_response.get_resource_preset(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            applied = await response.parse()
            assert_matches_type(AppliedPresetFields, applied, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_rule_preset(self, async_client: AsyncGcore) -> None:
        applied = await async_client.cdn.presets.applied.get_rule_preset(
            rule_id=0,
            resource_id=0,
        )
        assert_matches_type(AppliedPresetFields, applied, path=["response"])

    @parametrize
    async def test_raw_response_get_rule_preset(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.presets.applied.with_raw_response.get_rule_preset(
            rule_id=0,
            resource_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        applied = await response.parse()
        assert_matches_type(AppliedPresetFields, applied, path=["response"])

    @parametrize
    async def test_streaming_response_get_rule_preset(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.presets.applied.with_streaming_response.get_rule_preset(
            rule_id=0,
            resource_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            applied = await response.parse()
            assert_matches_type(AppliedPresetFields, applied, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unapply(self, async_client: AsyncGcore) -> None:
        applied = await async_client.cdn.presets.applied.unapply(
            object_id=0,
            preset_id=0,
        )
        assert applied is None

    @parametrize
    async def test_raw_response_unapply(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.presets.applied.with_raw_response.unapply(
            object_id=0,
            preset_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        applied = await response.parse()
        assert applied is None

    @parametrize
    async def test_streaming_response_unapply(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.presets.applied.with_streaming_response.unapply(
            object_id=0,
            preset_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            applied = await response.parse()
            assert applied is None

        assert cast(Any, response.is_closed) is True
