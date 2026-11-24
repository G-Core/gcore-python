from __future__ import annotations

from typing import Any, Dict, Callable

import httpx
import respx
import pytest

from gcore import Gcore, AsyncGcore, NotFoundError

base_url = "http://127.0.0.1:4010"
RESOURCE_ID = "00000000-0000-4000-8000-000000000001"

_TASK: Dict[str, Any] = {
    "id": "task-1",
    "state": "FINISHED",
    "task_type": "update",
    "created_on": "2026-07-01T13:37:14",
    "created_resources": {"ports": [RESOURCE_ID]},
}


def _port(**fields: Any) -> Dict[str, Any]:
    value: Dict[str, Any] = {
        "id": RESOURCE_ID,
        "allowed_address_pairs": [],
        "ip_assignments": [],
        "port_security_enabled": True,
        "security_group_ids": [],
        "tags": {},
    }
    value.update(fields)
    return value


class _API:
    def __init__(self, resource: Dict[str, Any] | None) -> None:
        self.resource = resource
        self.resource_gets = 0
        self.get_body = b""

    def handle(self, request: httpx.Request) -> httpx.Response:
        if request.method == "GET" and "/tasks/" in request.url.path:
            return httpx.Response(200, json=_TASK)
        if request.method == "GET":
            self.resource_gets += 1
            self.get_body = request.content
            if self.resource is None:
                return httpx.Response(404, json={"message": "not found"})
            return httpx.Response(200, json=self.resource)
        return httpx.Response(200, json={"tasks": ["task-1"]})


def _run(api: _API, invoke: Callable[[Gcore], Any]) -> Any:
    client = Gcore(base_url=base_url, api_key="test", _strict_response_validation=False)
    with respx.mock(base_url=base_url) as router:
        router.route(url__regex=r".+").mock(side_effect=api.handle)
        return invoke(client)


async def _run_async(api: _API, invoke: Callable[[AsyncGcore], Any]) -> Any:
    client = AsyncGcore(base_url=base_url, api_key="test", _strict_response_validation=False)
    with respx.mock(base_url=base_url) as router:
        router.route(url__regex=r".+").mock(side_effect=api.handle)
        return await invoke(client)


def test_port_update_returns_first_get_even_when_fields_differ() -> None:
    api = _API(_port(tags={"old": "value"}))
    port = _run(
        api,
        lambda client: client.cloud.ports.update_and_poll(
            RESOURCE_ID,
            project_id=1,
            tags={"new": "value"},
            extra_body={"extension": True},
        ),
    )
    assert (port.tags, api.resource_gets, api.get_body) == ({"old": "value"}, 1, b"")


async def test_port_update_returns_first_get_even_when_fields_differ_async() -> None:
    api = _API(_port(tags={"old": "value"}))
    port = await _run_async(
        api,
        lambda client: client.cloud.ports.update_and_poll(
            RESOURCE_ID,
            project_id=1,
            tags={"new": "value"},
            extra_body={"extension": True},
        ),
    )
    assert (port.tags, api.resource_gets, api.get_body) == ({"old": "value"}, 1, b"")


def test_port_create_propagates_first_get_404() -> None:
    api = _API(None)
    with pytest.raises(NotFoundError):
        _run(api, lambda client: client.cloud.ports.create_and_poll(project_id=1, region_id=1))
    assert api.resource_gets == 1


async def test_port_create_propagates_first_get_404_async() -> None:
    api = _API(None)
    with pytest.raises(NotFoundError):
        await _run_async(api, lambda client: client.cloud.ports.create_and_poll(project_id=1, region_id=1))
    assert api.resource_gets == 1
