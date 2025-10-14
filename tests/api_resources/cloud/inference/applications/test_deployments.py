# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cloud import TaskIDList
from gcore.types.cloud.inference.applications import (
    InferenceApplicationDeployment,
    InferenceApplicationDeploymentList,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDeployments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        deployment = client.cloud.inference.applications.deployments.create(
            project_id=1,
            application_name="demo-app",
            components_configuration={
                "model": {
                    "exposed": True,
                    "flavor": "inference-16vcpu-232gib-1xh100-80gb",
                    "scale": {
                        "max": 1,
                        "min": 1,
                    },
                }
            },
            name="name",
            regions=[1, 2],
        )
        assert_matches_type(TaskIDList, deployment, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        deployment = client.cloud.inference.applications.deployments.create(
            project_id=1,
            application_name="demo-app",
            components_configuration={
                "model": {
                    "exposed": True,
                    "flavor": "inference-16vcpu-232gib-1xh100-80gb",
                    "scale": {
                        "max": 1,
                        "min": 1,
                    },
                    "parameter_overrides": {"foo": {"value": "value"}},
                }
            },
            name="name",
            regions=[1, 2],
            api_keys=["key1", "key2"],
        )
        assert_matches_type(TaskIDList, deployment, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.cloud.inference.applications.deployments.with_raw_response.create(
            project_id=1,
            application_name="demo-app",
            components_configuration={
                "model": {
                    "exposed": True,
                    "flavor": "inference-16vcpu-232gib-1xh100-80gb",
                    "scale": {
                        "max": 1,
                        "min": 1,
                    },
                }
            },
            name="name",
            regions=[1, 2],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = response.parse()
        assert_matches_type(TaskIDList, deployment, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.cloud.inference.applications.deployments.with_streaming_response.create(
            project_id=1,
            application_name="demo-app",
            components_configuration={
                "model": {
                    "exposed": True,
                    "flavor": "inference-16vcpu-232gib-1xh100-80gb",
                    "scale": {
                        "max": 1,
                        "min": 1,
                    },
                }
            },
            name="name",
            regions=[1, 2],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = response.parse()
            assert_matches_type(TaskIDList, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        deployment = client.cloud.inference.applications.deployments.update(
            deployment_name="deployment_name",
            project_id=1,
        )
        assert_matches_type(TaskIDList, deployment, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gcore) -> None:
        deployment = client.cloud.inference.applications.deployments.update(
            deployment_name="deployment_name",
            project_id=1,
            api_keys=["key1", "key2"],
            components_configuration={
                "model": {
                    "exposed": True,
                    "flavor": "flavor",
                    "parameter_overrides": {"foo": {"value": "value"}},
                    "scale": {
                        "max": 2,
                        "min": 0,
                    },
                }
            },
            regions=[1, 2],
        )
        assert_matches_type(TaskIDList, deployment, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.cloud.inference.applications.deployments.with_raw_response.update(
            deployment_name="deployment_name",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = response.parse()
        assert_matches_type(TaskIDList, deployment, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.cloud.inference.applications.deployments.with_streaming_response.update(
            deployment_name="deployment_name",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = response.parse()
            assert_matches_type(TaskIDList, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_name` but received ''"):
            client.cloud.inference.applications.deployments.with_raw_response.update(
                deployment_name="",
                project_id=1,
            )

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        deployment = client.cloud.inference.applications.deployments.list(
            project_id=1,
        )
        assert_matches_type(InferenceApplicationDeploymentList, deployment, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.inference.applications.deployments.with_raw_response.list(
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = response.parse()
        assert_matches_type(InferenceApplicationDeploymentList, deployment, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.inference.applications.deployments.with_streaming_response.list(
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = response.parse()
            assert_matches_type(InferenceApplicationDeploymentList, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        deployment = client.cloud.inference.applications.deployments.delete(
            deployment_name="deployment_name",
            project_id=1,
        )
        assert_matches_type(TaskIDList, deployment, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cloud.inference.applications.deployments.with_raw_response.delete(
            deployment_name="deployment_name",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = response.parse()
        assert_matches_type(TaskIDList, deployment, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cloud.inference.applications.deployments.with_streaming_response.delete(
            deployment_name="deployment_name",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = response.parse()
            assert_matches_type(TaskIDList, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_name` but received ''"):
            client.cloud.inference.applications.deployments.with_raw_response.delete(
                deployment_name="",
                project_id=1,
            )

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        deployment = client.cloud.inference.applications.deployments.get(
            deployment_name="deployment_name",
            project_id=1,
        )
        assert_matches_type(InferenceApplicationDeployment, deployment, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cloud.inference.applications.deployments.with_raw_response.get(
            deployment_name="deployment_name",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = response.parse()
        assert_matches_type(InferenceApplicationDeployment, deployment, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cloud.inference.applications.deployments.with_streaming_response.get(
            deployment_name="deployment_name",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = response.parse()
            assert_matches_type(InferenceApplicationDeployment, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_name` but received ''"):
            client.cloud.inference.applications.deployments.with_raw_response.get(
                deployment_name="",
                project_id=1,
            )


class TestAsyncDeployments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        deployment = await async_client.cloud.inference.applications.deployments.create(
            project_id=1,
            application_name="demo-app",
            components_configuration={
                "model": {
                    "exposed": True,
                    "flavor": "inference-16vcpu-232gib-1xh100-80gb",
                    "scale": {
                        "max": 1,
                        "min": 1,
                    },
                }
            },
            name="name",
            regions=[1, 2],
        )
        assert_matches_type(TaskIDList, deployment, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        deployment = await async_client.cloud.inference.applications.deployments.create(
            project_id=1,
            application_name="demo-app",
            components_configuration={
                "model": {
                    "exposed": True,
                    "flavor": "inference-16vcpu-232gib-1xh100-80gb",
                    "scale": {
                        "max": 1,
                        "min": 1,
                    },
                    "parameter_overrides": {"foo": {"value": "value"}},
                }
            },
            name="name",
            regions=[1, 2],
            api_keys=["key1", "key2"],
        )
        assert_matches_type(TaskIDList, deployment, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.inference.applications.deployments.with_raw_response.create(
            project_id=1,
            application_name="demo-app",
            components_configuration={
                "model": {
                    "exposed": True,
                    "flavor": "inference-16vcpu-232gib-1xh100-80gb",
                    "scale": {
                        "max": 1,
                        "min": 1,
                    },
                }
            },
            name="name",
            regions=[1, 2],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = await response.parse()
        assert_matches_type(TaskIDList, deployment, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.inference.applications.deployments.with_streaming_response.create(
            project_id=1,
            application_name="demo-app",
            components_configuration={
                "model": {
                    "exposed": True,
                    "flavor": "inference-16vcpu-232gib-1xh100-80gb",
                    "scale": {
                        "max": 1,
                        "min": 1,
                    },
                }
            },
            name="name",
            regions=[1, 2],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = await response.parse()
            assert_matches_type(TaskIDList, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        deployment = await async_client.cloud.inference.applications.deployments.update(
            deployment_name="deployment_name",
            project_id=1,
        )
        assert_matches_type(TaskIDList, deployment, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGcore) -> None:
        deployment = await async_client.cloud.inference.applications.deployments.update(
            deployment_name="deployment_name",
            project_id=1,
            api_keys=["key1", "key2"],
            components_configuration={
                "model": {
                    "exposed": True,
                    "flavor": "flavor",
                    "parameter_overrides": {"foo": {"value": "value"}},
                    "scale": {
                        "max": 2,
                        "min": 0,
                    },
                }
            },
            regions=[1, 2],
        )
        assert_matches_type(TaskIDList, deployment, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.inference.applications.deployments.with_raw_response.update(
            deployment_name="deployment_name",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = await response.parse()
        assert_matches_type(TaskIDList, deployment, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.inference.applications.deployments.with_streaming_response.update(
            deployment_name="deployment_name",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = await response.parse()
            assert_matches_type(TaskIDList, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_name` but received ''"):
            await async_client.cloud.inference.applications.deployments.with_raw_response.update(
                deployment_name="",
                project_id=1,
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        deployment = await async_client.cloud.inference.applications.deployments.list(
            project_id=1,
        )
        assert_matches_type(InferenceApplicationDeploymentList, deployment, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.inference.applications.deployments.with_raw_response.list(
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = await response.parse()
        assert_matches_type(InferenceApplicationDeploymentList, deployment, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.inference.applications.deployments.with_streaming_response.list(
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = await response.parse()
            assert_matches_type(InferenceApplicationDeploymentList, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        deployment = await async_client.cloud.inference.applications.deployments.delete(
            deployment_name="deployment_name",
            project_id=1,
        )
        assert_matches_type(TaskIDList, deployment, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.inference.applications.deployments.with_raw_response.delete(
            deployment_name="deployment_name",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = await response.parse()
        assert_matches_type(TaskIDList, deployment, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.inference.applications.deployments.with_streaming_response.delete(
            deployment_name="deployment_name",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = await response.parse()
            assert_matches_type(TaskIDList, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_name` but received ''"):
            await async_client.cloud.inference.applications.deployments.with_raw_response.delete(
                deployment_name="",
                project_id=1,
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        deployment = await async_client.cloud.inference.applications.deployments.get(
            deployment_name="deployment_name",
            project_id=1,
        )
        assert_matches_type(InferenceApplicationDeployment, deployment, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.inference.applications.deployments.with_raw_response.get(
            deployment_name="deployment_name",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = await response.parse()
        assert_matches_type(InferenceApplicationDeployment, deployment, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.inference.applications.deployments.with_streaming_response.get(
            deployment_name="deployment_name",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = await response.parse()
            assert_matches_type(InferenceApplicationDeployment, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_name` but received ''"):
            await async_client.cloud.inference.applications.deployments.with_raw_response.get(
                deployment_name="",
                project_id=1,
            )
