# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore._utils import parse_datetime
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage
from gcore.types.waap import WaapInsightSilence

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInsightSilences:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        insight_silence = client.waap.domains.insight_silences.create(
            domain_id=0,
            author="author",
            comment="comment",
            insight_type="insight_type",
            labels={"foo": "string"},
        )
        assert_matches_type(WaapInsightSilence, insight_silence, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        insight_silence = client.waap.domains.insight_silences.create(
            domain_id=0,
            author="author",
            comment="comment",
            insight_type="insight_type",
            labels={"foo": "string"},
            expire_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(WaapInsightSilence, insight_silence, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.waap.domains.insight_silences.with_raw_response.create(
            domain_id=0,
            author="author",
            comment="comment",
            insight_type="insight_type",
            labels={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight_silence = response.parse()
        assert_matches_type(WaapInsightSilence, insight_silence, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.waap.domains.insight_silences.with_streaming_response.create(
            domain_id=0,
            author="author",
            comment="comment",
            insight_type="insight_type",
            labels={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight_silence = response.parse()
            assert_matches_type(WaapInsightSilence, insight_silence, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        insight_silence = client.waap.domains.insight_silences.update(
            silence_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id=0,
            author="author",
            comment="comment",
            expire_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(WaapInsightSilence, insight_silence, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gcore) -> None:
        insight_silence = client.waap.domains.insight_silences.update(
            silence_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id=0,
            author="author",
            comment="comment",
            expire_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            labels={"foo": "string"},
        )
        assert_matches_type(WaapInsightSilence, insight_silence, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.waap.domains.insight_silences.with_raw_response.update(
            silence_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id=0,
            author="author",
            comment="comment",
            expire_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight_silence = response.parse()
        assert_matches_type(WaapInsightSilence, insight_silence, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.waap.domains.insight_silences.with_streaming_response.update(
            silence_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id=0,
            author="author",
            comment="comment",
            expire_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight_silence = response.parse()
            assert_matches_type(WaapInsightSilence, insight_silence, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `silence_id` but received ''"):
            client.waap.domains.insight_silences.with_raw_response.update(
                silence_id="",
                domain_id=0,
                author="author",
                comment="comment",
                expire_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            )

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        insight_silence = client.waap.domains.insight_silences.list(
            domain_id=0,
        )
        assert_matches_type(SyncOffsetPage[WaapInsightSilence], insight_silence, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        insight_silence = client.waap.domains.insight_silences.list(
            domain_id=0,
            id=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e", "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            author="author",
            comment="comment",
            insight_type=["string", "string"],
            limit=0,
            offset=0,
            ordering="id",
        )
        assert_matches_type(SyncOffsetPage[WaapInsightSilence], insight_silence, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.waap.domains.insight_silences.with_raw_response.list(
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight_silence = response.parse()
        assert_matches_type(SyncOffsetPage[WaapInsightSilence], insight_silence, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.waap.domains.insight_silences.with_streaming_response.list(
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight_silence = response.parse()
            assert_matches_type(SyncOffsetPage[WaapInsightSilence], insight_silence, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        insight_silence = client.waap.domains.insight_silences.delete(
            silence_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id=0,
        )
        assert insight_silence is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.waap.domains.insight_silences.with_raw_response.delete(
            silence_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight_silence = response.parse()
        assert insight_silence is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.waap.domains.insight_silences.with_streaming_response.delete(
            silence_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight_silence = response.parse()
            assert insight_silence is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `silence_id` but received ''"):
            client.waap.domains.insight_silences.with_raw_response.delete(
                silence_id="",
                domain_id=0,
            )

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        insight_silence = client.waap.domains.insight_silences.get(
            silence_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id=0,
        )
        assert_matches_type(WaapInsightSilence, insight_silence, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.waap.domains.insight_silences.with_raw_response.get(
            silence_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight_silence = response.parse()
        assert_matches_type(WaapInsightSilence, insight_silence, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.waap.domains.insight_silences.with_streaming_response.get(
            silence_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight_silence = response.parse()
            assert_matches_type(WaapInsightSilence, insight_silence, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `silence_id` but received ''"):
            client.waap.domains.insight_silences.with_raw_response.get(
                silence_id="",
                domain_id=0,
            )


class TestAsyncInsightSilences:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        insight_silence = await async_client.waap.domains.insight_silences.create(
            domain_id=0,
            author="author",
            comment="comment",
            insight_type="insight_type",
            labels={"foo": "string"},
        )
        assert_matches_type(WaapInsightSilence, insight_silence, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        insight_silence = await async_client.waap.domains.insight_silences.create(
            domain_id=0,
            author="author",
            comment="comment",
            insight_type="insight_type",
            labels={"foo": "string"},
            expire_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(WaapInsightSilence, insight_silence, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.domains.insight_silences.with_raw_response.create(
            domain_id=0,
            author="author",
            comment="comment",
            insight_type="insight_type",
            labels={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight_silence = await response.parse()
        assert_matches_type(WaapInsightSilence, insight_silence, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.domains.insight_silences.with_streaming_response.create(
            domain_id=0,
            author="author",
            comment="comment",
            insight_type="insight_type",
            labels={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight_silence = await response.parse()
            assert_matches_type(WaapInsightSilence, insight_silence, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        insight_silence = await async_client.waap.domains.insight_silences.update(
            silence_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id=0,
            author="author",
            comment="comment",
            expire_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(WaapInsightSilence, insight_silence, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGcore) -> None:
        insight_silence = await async_client.waap.domains.insight_silences.update(
            silence_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id=0,
            author="author",
            comment="comment",
            expire_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            labels={"foo": "string"},
        )
        assert_matches_type(WaapInsightSilence, insight_silence, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.domains.insight_silences.with_raw_response.update(
            silence_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id=0,
            author="author",
            comment="comment",
            expire_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight_silence = await response.parse()
        assert_matches_type(WaapInsightSilence, insight_silence, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.domains.insight_silences.with_streaming_response.update(
            silence_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id=0,
            author="author",
            comment="comment",
            expire_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight_silence = await response.parse()
            assert_matches_type(WaapInsightSilence, insight_silence, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `silence_id` but received ''"):
            await async_client.waap.domains.insight_silences.with_raw_response.update(
                silence_id="",
                domain_id=0,
                author="author",
                comment="comment",
                expire_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        insight_silence = await async_client.waap.domains.insight_silences.list(
            domain_id=0,
        )
        assert_matches_type(AsyncOffsetPage[WaapInsightSilence], insight_silence, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        insight_silence = await async_client.waap.domains.insight_silences.list(
            domain_id=0,
            id=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e", "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            author="author",
            comment="comment",
            insight_type=["string", "string"],
            limit=0,
            offset=0,
            ordering="id",
        )
        assert_matches_type(AsyncOffsetPage[WaapInsightSilence], insight_silence, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.domains.insight_silences.with_raw_response.list(
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight_silence = await response.parse()
        assert_matches_type(AsyncOffsetPage[WaapInsightSilence], insight_silence, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.domains.insight_silences.with_streaming_response.list(
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight_silence = await response.parse()
            assert_matches_type(AsyncOffsetPage[WaapInsightSilence], insight_silence, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        insight_silence = await async_client.waap.domains.insight_silences.delete(
            silence_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id=0,
        )
        assert insight_silence is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.domains.insight_silences.with_raw_response.delete(
            silence_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight_silence = await response.parse()
        assert insight_silence is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.domains.insight_silences.with_streaming_response.delete(
            silence_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight_silence = await response.parse()
            assert insight_silence is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `silence_id` but received ''"):
            await async_client.waap.domains.insight_silences.with_raw_response.delete(
                silence_id="",
                domain_id=0,
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        insight_silence = await async_client.waap.domains.insight_silences.get(
            silence_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id=0,
        )
        assert_matches_type(WaapInsightSilence, insight_silence, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.waap.domains.insight_silences.with_raw_response.get(
            silence_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight_silence = await response.parse()
        assert_matches_type(WaapInsightSilence, insight_silence, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.waap.domains.insight_silences.with_streaming_response.get(
            silence_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            domain_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight_silence = await response.parse()
            assert_matches_type(WaapInsightSilence, insight_silence, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `silence_id` but received ''"):
            await async_client.waap.domains.insight_silences.with_raw_response.get(
                silence_id="",
                domain_id=0,
            )
