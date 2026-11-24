from __future__ import annotations

import json

import httpx
import respx
import pytest

from gcore import Gcore, AsyncGcore
from gcore.types.cloud import PlacementGroupListParams

_URL = "http://127.0.0.1:4010"
_PATH = "/cloud/v1/projects/7/placement_groups"
_MEMBERS = ["00000000-0000-4000-8000-000000000011", "00000000-0000-4000-8000-000000000012"]


@pytest.mark.parametrize("asynchronous", [False, True], ids=["sync", "async"])
@pytest.mark.parametrize("filter_by_region", [False, True])
async def test_list_across_regions_keeps_filters_on_each_page(asynchronous: bool, filter_by_region: bool) -> None:
    params: PlacementGroupListParams = {
        "limit": 1,
        "offset": 0,
        "member_ids": _MEMBERS,
        "name": {"prefix": ["web-", "prod-"], "contains": ["app"]},
        "policies": ["affinity", "anti-affinity"],
    }
    if filter_by_region:
        params["region_ids"] = [3, 5]

    queries: list[httpx.QueryParams] = []

    def page(request: httpx.Request) -> httpx.Response:
        queries.append(request.url.params)
        offset = int(request.url.params["offset"])
        return httpx.Response(
            200,
            json={
                "count": 2,
                "results": [
                    {
                        "id": f"group-{offset}",
                        "name": "prod-app",
                        "policy": "affinity",
                        "region_id": 3 + 2 * offset,
                        "managed_by": None if offset == 0 else {"type": "system"},
                        "member_ids": _MEMBERS,
                        "created_at": "2026-11-19T12:00:00Z",
                        "updated_at": "2026-11-19T12:00:00Z",
                    }
                ],
            },
        )

    with respx.mock(base_url=_URL) as router:
        route = router.get(_PATH).mock(side_effect=page)
        if asynchronous:
            async with AsyncGcore(api_key="test", base_url=_URL, cloud_project_id=7, cloud_region_id=99) as client:
                groups = [group async for group in client.cloud.placement_groups.list(**params)]
        else:
            with Gcore(api_key="test", base_url=_URL, cloud_project_id=7, cloud_region_id=99) as client:
                groups = list(client.cloud.placement_groups.list(**params))

        assert [group.region_id for group in groups] == [3, 5]
        assert groups[0].managed_by is None
        assert groups[1].managed_by is not None and groups[1].managed_by.type == "system"
        assert groups[0].member_ids == _MEMBERS
        assert route.call_count == 2
        for offset, options in enumerate(queries):
            assert options == httpx.QueryParams(
                {
                    "limit": "1",
                    "offset": str(offset),
                    "member_ids": _MEMBERS,
                    "name[prefix]": ["web-", "prod-"],
                    "name[contains]": "app",
                    "policies": ["affinity", "anti-affinity"],
                    **({"region_ids": ["3", "5"]} if filter_by_region else {}),
                }
            )


@pytest.mark.parametrize("asynchronous", [False, True], ids=["sync", "async"])
async def test_create_sends_body_region_without_a_client_default(
    asynchronous: bool, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.delenv("GCORE_CLOUD_REGION_ID", raising=False)
    with respx.mock(base_url=_URL) as router:
        create = router.post(_PATH).mock(return_value=httpx.Response(200, json={"tasks": ["task-1"]}))
        if asynchronous:
            async with AsyncGcore(api_key="test", base_url=_URL, cloud_project_id=7) as client:
                result = await client.cloud.placement_groups.create(name="web", policy="soft-affinity", region_id=5)
        else:
            with Gcore(api_key="test", base_url=_URL, cloud_project_id=7) as client:
                result = client.cloud.placement_groups.create(name="web", policy="soft-affinity", region_id=5)

        assert result.tasks == ["task-1"]
        assert create.call_count == 1
        assert not create.calls.last.request.url.query
        assert json.loads(create.calls.last.request.content) == {
            "region_id": 5,
            "name": "web",
            "policy": "soft-affinity",
        }
