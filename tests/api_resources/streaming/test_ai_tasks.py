# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.pagination import SyncPageStreamingAI, AsyncPageStreamingAI
from gcore.types.streaming import (
    AITask,
    AITaskGetResponse,
    AITaskCancelResponse,
    AITaskCreateResponse,
    AITaskGetAISettingsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAITasks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason='Skipping test due to 422 Unprocessable Entity {"error":"Feature is disabled. Contact support to enable."}'
    )
    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        ai_task = client.streaming.ai_tasks.create(
            task_name="transcription",
            url="url",
        )
        assert_matches_type(AITaskCreateResponse, ai_task, path=["response"])

    @pytest.mark.skip(
        reason='Skipping test due to 422 Unprocessable Entity {"error":"Feature is disabled. Contact support to enable."}'
    )
    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        ai_task = client.streaming.ai_tasks.create(
            task_name="transcription",
            url="url",
            audio_language="audio_language",
            category="sport",
            client_entity_data="client_entity_data",
            client_user_id="client_user_id",
            subtitles_language="subtitles_language",
        )
        assert_matches_type(AITaskCreateResponse, ai_task, path=["response"])

    @pytest.mark.skip(
        reason='Skipping test due to 422 Unprocessable Entity {"error":"Feature is disabled. Contact support to enable."}'
    )
    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.streaming.ai_tasks.with_raw_response.create(
            task_name="transcription",
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_task = response.parse()
        assert_matches_type(AITaskCreateResponse, ai_task, path=["response"])

    @pytest.mark.skip(
        reason='Skipping test due to 422 Unprocessable Entity {"error":"Feature is disabled. Contact support to enable."}'
    )
    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.streaming.ai_tasks.with_streaming_response.create(
            task_name="transcription",
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_task = response.parse()
            assert_matches_type(AITaskCreateResponse, ai_task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        ai_task = client.streaming.ai_tasks.list()
        assert_matches_type(SyncPageStreamingAI[AITask], ai_task, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        ai_task = client.streaming.ai_tasks.list(
            date_created="date_created",
            limit=0,
            ordering="task_id",
            page=0,
            search="search",
            status="FAILURE",
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            task_name="transcription",
        )
        assert_matches_type(SyncPageStreamingAI[AITask], ai_task, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.streaming.ai_tasks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_task = response.parse()
        assert_matches_type(SyncPageStreamingAI[AITask], ai_task, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.streaming.ai_tasks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_task = response.parse()
            assert_matches_type(SyncPageStreamingAI[AITask], ai_task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_cancel(self, client: Gcore) -> None:
        ai_task = client.streaming.ai_tasks.cancel(
            "task_id",
        )
        assert_matches_type(AITaskCancelResponse, ai_task, path=["response"])

    @parametrize
    def test_raw_response_cancel(self, client: Gcore) -> None:
        response = client.streaming.ai_tasks.with_raw_response.cancel(
            "task_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_task = response.parse()
        assert_matches_type(AITaskCancelResponse, ai_task, path=["response"])

    @parametrize
    def test_streaming_response_cancel(self, client: Gcore) -> None:
        with client.streaming.ai_tasks.with_streaming_response.cancel(
            "task_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_task = response.parse()
            assert_matches_type(AITaskCancelResponse, ai_task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.streaming.ai_tasks.with_raw_response.cancel(
                "",
            )

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        ai_task = client.streaming.ai_tasks.get(
            "task_id",
        )
        assert_matches_type(AITaskGetResponse, ai_task, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.streaming.ai_tasks.with_raw_response.get(
            "task_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_task = response.parse()
        assert_matches_type(AITaskGetResponse, ai_task, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.streaming.ai_tasks.with_streaming_response.get(
            "task_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_task = response.parse()
            assert_matches_type(AITaskGetResponse, ai_task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.streaming.ai_tasks.with_raw_response.get(
                "",
            )

    @parametrize
    def test_method_get_ai_settings(self, client: Gcore) -> None:
        ai_task = client.streaming.ai_tasks.get_ai_settings(
            type="language_support",
        )
        assert_matches_type(AITaskGetAISettingsResponse, ai_task, path=["response"])

    @parametrize
    def test_method_get_ai_settings_with_all_params(self, client: Gcore) -> None:
        ai_task = client.streaming.ai_tasks.get_ai_settings(
            type="language_support",
            audio_language="audio_language",
            subtitles_language="subtitles_language",
        )
        assert_matches_type(AITaskGetAISettingsResponse, ai_task, path=["response"])

    @parametrize
    def test_raw_response_get_ai_settings(self, client: Gcore) -> None:
        response = client.streaming.ai_tasks.with_raw_response.get_ai_settings(
            type="language_support",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_task = response.parse()
        assert_matches_type(AITaskGetAISettingsResponse, ai_task, path=["response"])

    @parametrize
    def test_streaming_response_get_ai_settings(self, client: Gcore) -> None:
        with client.streaming.ai_tasks.with_streaming_response.get_ai_settings(
            type="language_support",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_task = response.parse()
            assert_matches_type(AITaskGetAISettingsResponse, ai_task, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAITasks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(
        reason='Skipping test due to 422 Unprocessable Entity {"error":"Feature is disabled. Contact support to enable."}'
    )
    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        ai_task = await async_client.streaming.ai_tasks.create(
            task_name="transcription",
            url="url",
        )
        assert_matches_type(AITaskCreateResponse, ai_task, path=["response"])

    @pytest.mark.skip(
        reason='Skipping test due to 422 Unprocessable Entity {"error":"Feature is disabled. Contact support to enable."}'
    )
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        ai_task = await async_client.streaming.ai_tasks.create(
            task_name="transcription",
            url="url",
            audio_language="audio_language",
            category="sport",
            client_entity_data="client_entity_data",
            client_user_id="client_user_id",
            subtitles_language="subtitles_language",
        )
        assert_matches_type(AITaskCreateResponse, ai_task, path=["response"])

    @pytest.mark.skip(
        reason='Skipping test due to 422 Unprocessable Entity {"error":"Feature is disabled. Contact support to enable."}'
    )
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.ai_tasks.with_raw_response.create(
            task_name="transcription",
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_task = await response.parse()
        assert_matches_type(AITaskCreateResponse, ai_task, path=["response"])

    @pytest.mark.skip(
        reason='Skipping test due to 422 Unprocessable Entity {"error":"Feature is disabled. Contact support to enable."}'
    )
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.ai_tasks.with_streaming_response.create(
            task_name="transcription",
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_task = await response.parse()
            assert_matches_type(AITaskCreateResponse, ai_task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        ai_task = await async_client.streaming.ai_tasks.list()
        assert_matches_type(AsyncPageStreamingAI[AITask], ai_task, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        ai_task = await async_client.streaming.ai_tasks.list(
            date_created="date_created",
            limit=0,
            ordering="task_id",
            page=0,
            search="search",
            status="FAILURE",
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            task_name="transcription",
        )
        assert_matches_type(AsyncPageStreamingAI[AITask], ai_task, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.ai_tasks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_task = await response.parse()
        assert_matches_type(AsyncPageStreamingAI[AITask], ai_task, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.ai_tasks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_task = await response.parse()
            assert_matches_type(AsyncPageStreamingAI[AITask], ai_task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_cancel(self, async_client: AsyncGcore) -> None:
        ai_task = await async_client.streaming.ai_tasks.cancel(
            "task_id",
        )
        assert_matches_type(AITaskCancelResponse, ai_task, path=["response"])

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.ai_tasks.with_raw_response.cancel(
            "task_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_task = await response.parse()
        assert_matches_type(AITaskCancelResponse, ai_task, path=["response"])

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.ai_tasks.with_streaming_response.cancel(
            "task_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_task = await response.parse()
            assert_matches_type(AITaskCancelResponse, ai_task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.streaming.ai_tasks.with_raw_response.cancel(
                "",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        ai_task = await async_client.streaming.ai_tasks.get(
            "task_id",
        )
        assert_matches_type(AITaskGetResponse, ai_task, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.ai_tasks.with_raw_response.get(
            "task_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_task = await response.parse()
        assert_matches_type(AITaskGetResponse, ai_task, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.ai_tasks.with_streaming_response.get(
            "task_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_task = await response.parse()
            assert_matches_type(AITaskGetResponse, ai_task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.streaming.ai_tasks.with_raw_response.get(
                "",
            )

    @parametrize
    async def test_method_get_ai_settings(self, async_client: AsyncGcore) -> None:
        ai_task = await async_client.streaming.ai_tasks.get_ai_settings(
            type="language_support",
        )
        assert_matches_type(AITaskGetAISettingsResponse, ai_task, path=["response"])

    @parametrize
    async def test_method_get_ai_settings_with_all_params(self, async_client: AsyncGcore) -> None:
        ai_task = await async_client.streaming.ai_tasks.get_ai_settings(
            type="language_support",
            audio_language="audio_language",
            subtitles_language="subtitles_language",
        )
        assert_matches_type(AITaskGetAISettingsResponse, ai_task, path=["response"])

    @parametrize
    async def test_raw_response_get_ai_settings(self, async_client: AsyncGcore) -> None:
        response = await async_client.streaming.ai_tasks.with_raw_response.get_ai_settings(
            type="language_support",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_task = await response.parse()
        assert_matches_type(AITaskGetAISettingsResponse, ai_task, path=["response"])

    @parametrize
    async def test_streaming_response_get_ai_settings(self, async_client: AsyncGcore) -> None:
        async with async_client.streaming.ai_tasks.with_streaming_response.get_ai_settings(
            type="language_support",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_task = await response.parse()
            assert_matches_type(AITaskGetAISettingsResponse, ai_task, path=["response"])

        assert cast(Any, response.is_closed) is True
