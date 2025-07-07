# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage
from gcore.types.cloud import TaskIDList
from gcore.types.cloud.inference import (
    InferenceDeployment,
    InferenceDeploymentAPIKey,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDeployments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        deployment = client.cloud.inference.deployments.create(
            project_id=1,
            containers=[
                {
                    "region_id": 1,
                    "scale": {
                        "max": 3,
                        "min": 1,
                    },
                }
            ],
            flavor_name="inference-16vcpu-232gib-1xh100-80gb",
            image="nginx:latest",
            listening_port=80,
            name="my-instance",
        )
        assert_matches_type(TaskIDList, deployment, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        deployment = client.cloud.inference.deployments.create(
            project_id=1,
            containers=[
                {
                    "region_id": 1,
                    "scale": {
                        "max": 3,
                        "min": 1,
                        "cooldown_period": 60,
                        "polling_interval": 30,
                        "triggers": {
                            "cpu": {"threshold": 80},
                            "gpu_memory": {"threshold": 80},
                            "gpu_utilization": {"threshold": 80},
                            "http": {
                                "rate": 1,
                                "window": 60,
                            },
                            "memory": {"threshold": 70},
                            "sqs": {
                                "activation_queue_length": 1,
                                "aws_region": "us-east-1",
                                "queue_length": 10,
                                "queue_url": "https://sqs.us-east-1.amazonaws.com/123456789012/MyQueue",
                                "secret_name": "x",
                                "aws_endpoint": "aws_endpoint",
                                "scale_on_delayed": True,
                                "scale_on_flight": True,
                            },
                        },
                    },
                }
            ],
            flavor_name="inference-16vcpu-232gib-1xh100-80gb",
            image="nginx:latest",
            listening_port=80,
            name="my-instance",
            api_keys=["key1", "key2"],
            auth_enabled=False,
            command=["nginx", "-g", "daemon off;"],
            credentials_name="dockerhub",
            description="My first instance",
            envs={
                "DEBUG_MODE": "False",
                "KEY": "12345",
            },
            ingress_opts={"disable_response_buffering": True},
            logging={
                "destination_region_id": 1,
                "enabled": True,
                "retention_policy": {"period": 42},
                "topic_name": "my-log-name",
            },
            probes={
                "liveness_probe": {
                    "enabled": True,
                    "probe": {
                        "exec": {"command": ["ls", "-l"]},
                        "failure_threshold": 3,
                        "http_get": {
                            "port": 80,
                            "headers": {"Authorization": "Bearer token 123"},
                            "host": "127.0.0.1",
                            "path": "/healthz",
                            "schema": "HTTP",
                        },
                        "initial_delay_seconds": 0,
                        "period_seconds": 5,
                        "success_threshold": 1,
                        "tcp_socket": {"port": 80},
                        "timeout_seconds": 1,
                    },
                },
                "readiness_probe": {
                    "enabled": True,
                    "probe": {
                        "exec": {"command": ["ls", "-l"]},
                        "failure_threshold": 3,
                        "http_get": {
                            "port": 80,
                            "headers": {"Authorization": "Bearer token 123"},
                            "host": "127.0.0.1",
                            "path": "/healthz",
                            "schema": "HTTP",
                        },
                        "initial_delay_seconds": 0,
                        "period_seconds": 5,
                        "success_threshold": 1,
                        "tcp_socket": {"port": 80},
                        "timeout_seconds": 1,
                    },
                },
                "startup_probe": {
                    "enabled": True,
                    "probe": {
                        "exec": {"command": ["ls", "-l"]},
                        "failure_threshold": 3,
                        "http_get": {
                            "port": 80,
                            "headers": {"Authorization": "Bearer token 123"},
                            "host": "127.0.0.1",
                            "path": "/healthz",
                            "schema": "HTTP",
                        },
                        "initial_delay_seconds": 0,
                        "period_seconds": 5,
                        "success_threshold": 1,
                        "tcp_socket": {"port": 80},
                        "timeout_seconds": 1,
                    },
                },
            },
            api_timeout=120,
        )
        assert_matches_type(TaskIDList, deployment, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.cloud.inference.deployments.with_raw_response.create(
            project_id=1,
            containers=[
                {
                    "region_id": 1,
                    "scale": {
                        "max": 3,
                        "min": 1,
                    },
                }
            ],
            flavor_name="inference-16vcpu-232gib-1xh100-80gb",
            image="nginx:latest",
            listening_port=80,
            name="my-instance",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = response.parse()
        assert_matches_type(TaskIDList, deployment, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.cloud.inference.deployments.with_streaming_response.create(
            project_id=1,
            containers=[
                {
                    "region_id": 1,
                    "scale": {
                        "max": 3,
                        "min": 1,
                    },
                }
            ],
            flavor_name="inference-16vcpu-232gib-1xh100-80gb",
            image="nginx:latest",
            listening_port=80,
            name="my-instance",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = response.parse()
            assert_matches_type(TaskIDList, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        deployment = client.cloud.inference.deployments.update(
            deployment_name="my-instance",
            project_id=1,
        )
        assert_matches_type(TaskIDList, deployment, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gcore) -> None:
        deployment = client.cloud.inference.deployments.update(
            deployment_name="my-instance",
            project_id=1,
            api_keys=["key1", "key2"],
            auth_enabled=False,
            command=["nginx", "-g", "daemon off;"],
            containers=[
                {
                    "region_id": 0,
                    "scale": {
                        "max": 3,
                        "min": 1,
                        "cooldown_period": 60,
                        "polling_interval": 30,
                        "triggers": {
                            "cpu": {"threshold": 75},
                            "gpu_memory": {"threshold": 80},
                            "gpu_utilization": {"threshold": 80},
                            "http": {
                                "rate": 1,
                                "window": 60,
                            },
                            "memory": {"threshold": 80},
                            "sqs": {
                                "activation_queue_length": 1,
                                "aws_region": "us-east-1",
                                "queue_length": 10,
                                "queue_url": "https://sqs.us-east-1.amazonaws.com/123456789012/MyQueue",
                                "secret_name": "x",
                                "aws_endpoint": "aws_endpoint",
                                "scale_on_delayed": True,
                                "scale_on_flight": True,
                            },
                        },
                    },
                }
            ],
            credentials_name="dockerhub",
            description="My first instance",
            envs={
                "DEBUG_MODE": "False",
                "KEY": "12345",
            },
            flavor_name="inference-16vcpu-232gib-1xh100-80gb",
            image="nginx:latest",
            ingress_opts={"disable_response_buffering": True},
            listening_port=80,
            logging={
                "destination_region_id": 1,
                "enabled": True,
                "retention_policy": {"period": 42},
                "topic_name": "my-log-name",
            },
            probes={
                "liveness_probe": {
                    "enabled": True,
                    "probe": {
                        "exec": {"command": ["ls", "-l"]},
                        "failure_threshold": 3,
                        "http_get": {
                            "headers": {"Authorization": "Bearer token 123"},
                            "host": "127.0.0.1",
                            "path": "/healthz",
                            "port": 80,
                            "schema": "HTTP",
                        },
                        "initial_delay_seconds": 0,
                        "period_seconds": 5,
                        "success_threshold": 1,
                        "tcp_socket": {"port": 80},
                        "timeout_seconds": 1,
                    },
                },
                "readiness_probe": {
                    "enabled": True,
                    "probe": {
                        "exec": {"command": ["ls", "-l"]},
                        "failure_threshold": 3,
                        "http_get": {
                            "headers": {"Authorization": "Bearer token 123"},
                            "host": "127.0.0.1",
                            "path": "/healthz",
                            "port": 80,
                            "schema": "HTTP",
                        },
                        "initial_delay_seconds": 0,
                        "period_seconds": 5,
                        "success_threshold": 1,
                        "tcp_socket": {"port": 80},
                        "timeout_seconds": 1,
                    },
                },
                "startup_probe": {
                    "enabled": True,
                    "probe": {
                        "exec": {"command": ["ls", "-l"]},
                        "failure_threshold": 3,
                        "http_get": {
                            "headers": {"Authorization": "Bearer token 123"},
                            "host": "127.0.0.1",
                            "path": "/healthz",
                            "port": 80,
                            "schema": "HTTP",
                        },
                        "initial_delay_seconds": 0,
                        "period_seconds": 5,
                        "success_threshold": 1,
                        "tcp_socket": {"port": 80},
                        "timeout_seconds": 1,
                    },
                },
            },
            api_timeout=120,
        )
        assert_matches_type(TaskIDList, deployment, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.cloud.inference.deployments.with_raw_response.update(
            deployment_name="my-instance",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = response.parse()
        assert_matches_type(TaskIDList, deployment, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.cloud.inference.deployments.with_streaming_response.update(
            deployment_name="my-instance",
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
            client.cloud.inference.deployments.with_raw_response.update(
                deployment_name="",
                project_id=1,
            )

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        deployment = client.cloud.inference.deployments.list(
            project_id=1,
        )
        assert_matches_type(SyncOffsetPage[InferenceDeployment], deployment, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        deployment = client.cloud.inference.deployments.list(
            project_id=1,
            limit=1000,
            offset=0,
        )
        assert_matches_type(SyncOffsetPage[InferenceDeployment], deployment, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.inference.deployments.with_raw_response.list(
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = response.parse()
        assert_matches_type(SyncOffsetPage[InferenceDeployment], deployment, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.inference.deployments.with_streaming_response.list(
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = response.parse()
            assert_matches_type(SyncOffsetPage[InferenceDeployment], deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        deployment = client.cloud.inference.deployments.delete(
            deployment_name="my-instance",
            project_id=1,
        )
        assert_matches_type(TaskIDList, deployment, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cloud.inference.deployments.with_raw_response.delete(
            deployment_name="my-instance",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = response.parse()
        assert_matches_type(TaskIDList, deployment, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cloud.inference.deployments.with_streaming_response.delete(
            deployment_name="my-instance",
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
            client.cloud.inference.deployments.with_raw_response.delete(
                deployment_name="",
                project_id=1,
            )

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        deployment = client.cloud.inference.deployments.get(
            deployment_name="my-instance",
            project_id=1,
        )
        assert_matches_type(InferenceDeployment, deployment, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cloud.inference.deployments.with_raw_response.get(
            deployment_name="my-instance",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = response.parse()
        assert_matches_type(InferenceDeployment, deployment, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cloud.inference.deployments.with_streaming_response.get(
            deployment_name="my-instance",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = response.parse()
            assert_matches_type(InferenceDeployment, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_name` but received ''"):
            client.cloud.inference.deployments.with_raw_response.get(
                deployment_name="",
                project_id=1,
            )

    @parametrize
    def test_method_get_api_key(self, client: Gcore) -> None:
        deployment = client.cloud.inference.deployments.get_api_key(
            deployment_name="my-instance",
            project_id=1,
        )
        assert_matches_type(InferenceDeploymentAPIKey, deployment, path=["response"])

    @parametrize
    def test_raw_response_get_api_key(self, client: Gcore) -> None:
        response = client.cloud.inference.deployments.with_raw_response.get_api_key(
            deployment_name="my-instance",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = response.parse()
        assert_matches_type(InferenceDeploymentAPIKey, deployment, path=["response"])

    @parametrize
    def test_streaming_response_get_api_key(self, client: Gcore) -> None:
        with client.cloud.inference.deployments.with_streaming_response.get_api_key(
            deployment_name="my-instance",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = response.parse()
            assert_matches_type(InferenceDeploymentAPIKey, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_api_key(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_name` but received ''"):
            client.cloud.inference.deployments.with_raw_response.get_api_key(
                deployment_name="",
                project_id=1,
            )

    @parametrize
    def test_method_start(self, client: Gcore) -> None:
        deployment = client.cloud.inference.deployments.start(
            deployment_name="my-instance",
            project_id=1,
        )
        assert deployment is None

    @parametrize
    def test_raw_response_start(self, client: Gcore) -> None:
        response = client.cloud.inference.deployments.with_raw_response.start(
            deployment_name="my-instance",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = response.parse()
        assert deployment is None

    @parametrize
    def test_streaming_response_start(self, client: Gcore) -> None:
        with client.cloud.inference.deployments.with_streaming_response.start(
            deployment_name="my-instance",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = response.parse()
            assert deployment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_start(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_name` but received ''"):
            client.cloud.inference.deployments.with_raw_response.start(
                deployment_name="",
                project_id=1,
            )

    @parametrize
    def test_method_stop(self, client: Gcore) -> None:
        deployment = client.cloud.inference.deployments.stop(
            deployment_name="my-instance",
            project_id=1,
        )
        assert deployment is None

    @parametrize
    def test_raw_response_stop(self, client: Gcore) -> None:
        response = client.cloud.inference.deployments.with_raw_response.stop(
            deployment_name="my-instance",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = response.parse()
        assert deployment is None

    @parametrize
    def test_streaming_response_stop(self, client: Gcore) -> None:
        with client.cloud.inference.deployments.with_streaming_response.stop(
            deployment_name="my-instance",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = response.parse()
            assert deployment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_stop(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_name` but received ''"):
            client.cloud.inference.deployments.with_raw_response.stop(
                deployment_name="",
                project_id=1,
            )


class TestAsyncDeployments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        deployment = await async_client.cloud.inference.deployments.create(
            project_id=1,
            containers=[
                {
                    "region_id": 1,
                    "scale": {
                        "max": 3,
                        "min": 1,
                    },
                }
            ],
            flavor_name="inference-16vcpu-232gib-1xh100-80gb",
            image="nginx:latest",
            listening_port=80,
            name="my-instance",
        )
        assert_matches_type(TaskIDList, deployment, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        deployment = await async_client.cloud.inference.deployments.create(
            project_id=1,
            containers=[
                {
                    "region_id": 1,
                    "scale": {
                        "max": 3,
                        "min": 1,
                        "cooldown_period": 60,
                        "polling_interval": 30,
                        "triggers": {
                            "cpu": {"threshold": 80},
                            "gpu_memory": {"threshold": 80},
                            "gpu_utilization": {"threshold": 80},
                            "http": {
                                "rate": 1,
                                "window": 60,
                            },
                            "memory": {"threshold": 70},
                            "sqs": {
                                "activation_queue_length": 1,
                                "aws_region": "us-east-1",
                                "queue_length": 10,
                                "queue_url": "https://sqs.us-east-1.amazonaws.com/123456789012/MyQueue",
                                "secret_name": "x",
                                "aws_endpoint": "aws_endpoint",
                                "scale_on_delayed": True,
                                "scale_on_flight": True,
                            },
                        },
                    },
                }
            ],
            flavor_name="inference-16vcpu-232gib-1xh100-80gb",
            image="nginx:latest",
            listening_port=80,
            name="my-instance",
            api_keys=["key1", "key2"],
            auth_enabled=False,
            command=["nginx", "-g", "daemon off;"],
            credentials_name="dockerhub",
            description="My first instance",
            envs={
                "DEBUG_MODE": "False",
                "KEY": "12345",
            },
            ingress_opts={"disable_response_buffering": True},
            logging={
                "destination_region_id": 1,
                "enabled": True,
                "retention_policy": {"period": 42},
                "topic_name": "my-log-name",
            },
            probes={
                "liveness_probe": {
                    "enabled": True,
                    "probe": {
                        "exec": {"command": ["ls", "-l"]},
                        "failure_threshold": 3,
                        "http_get": {
                            "port": 80,
                            "headers": {"Authorization": "Bearer token 123"},
                            "host": "127.0.0.1",
                            "path": "/healthz",
                            "schema": "HTTP",
                        },
                        "initial_delay_seconds": 0,
                        "period_seconds": 5,
                        "success_threshold": 1,
                        "tcp_socket": {"port": 80},
                        "timeout_seconds": 1,
                    },
                },
                "readiness_probe": {
                    "enabled": True,
                    "probe": {
                        "exec": {"command": ["ls", "-l"]},
                        "failure_threshold": 3,
                        "http_get": {
                            "port": 80,
                            "headers": {"Authorization": "Bearer token 123"},
                            "host": "127.0.0.1",
                            "path": "/healthz",
                            "schema": "HTTP",
                        },
                        "initial_delay_seconds": 0,
                        "period_seconds": 5,
                        "success_threshold": 1,
                        "tcp_socket": {"port": 80},
                        "timeout_seconds": 1,
                    },
                },
                "startup_probe": {
                    "enabled": True,
                    "probe": {
                        "exec": {"command": ["ls", "-l"]},
                        "failure_threshold": 3,
                        "http_get": {
                            "port": 80,
                            "headers": {"Authorization": "Bearer token 123"},
                            "host": "127.0.0.1",
                            "path": "/healthz",
                            "schema": "HTTP",
                        },
                        "initial_delay_seconds": 0,
                        "period_seconds": 5,
                        "success_threshold": 1,
                        "tcp_socket": {"port": 80},
                        "timeout_seconds": 1,
                    },
                },
            },
            api_timeout=120,
        )
        assert_matches_type(TaskIDList, deployment, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.inference.deployments.with_raw_response.create(
            project_id=1,
            containers=[
                {
                    "region_id": 1,
                    "scale": {
                        "max": 3,
                        "min": 1,
                    },
                }
            ],
            flavor_name="inference-16vcpu-232gib-1xh100-80gb",
            image="nginx:latest",
            listening_port=80,
            name="my-instance",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = await response.parse()
        assert_matches_type(TaskIDList, deployment, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.inference.deployments.with_streaming_response.create(
            project_id=1,
            containers=[
                {
                    "region_id": 1,
                    "scale": {
                        "max": 3,
                        "min": 1,
                    },
                }
            ],
            flavor_name="inference-16vcpu-232gib-1xh100-80gb",
            image="nginx:latest",
            listening_port=80,
            name="my-instance",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = await response.parse()
            assert_matches_type(TaskIDList, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        deployment = await async_client.cloud.inference.deployments.update(
            deployment_name="my-instance",
            project_id=1,
        )
        assert_matches_type(TaskIDList, deployment, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGcore) -> None:
        deployment = await async_client.cloud.inference.deployments.update(
            deployment_name="my-instance",
            project_id=1,
            api_keys=["key1", "key2"],
            auth_enabled=False,
            command=["nginx", "-g", "daemon off;"],
            containers=[
                {
                    "region_id": 0,
                    "scale": {
                        "max": 3,
                        "min": 1,
                        "cooldown_period": 60,
                        "polling_interval": 30,
                        "triggers": {
                            "cpu": {"threshold": 75},
                            "gpu_memory": {"threshold": 80},
                            "gpu_utilization": {"threshold": 80},
                            "http": {
                                "rate": 1,
                                "window": 60,
                            },
                            "memory": {"threshold": 80},
                            "sqs": {
                                "activation_queue_length": 1,
                                "aws_region": "us-east-1",
                                "queue_length": 10,
                                "queue_url": "https://sqs.us-east-1.amazonaws.com/123456789012/MyQueue",
                                "secret_name": "x",
                                "aws_endpoint": "aws_endpoint",
                                "scale_on_delayed": True,
                                "scale_on_flight": True,
                            },
                        },
                    },
                }
            ],
            credentials_name="dockerhub",
            description="My first instance",
            envs={
                "DEBUG_MODE": "False",
                "KEY": "12345",
            },
            flavor_name="inference-16vcpu-232gib-1xh100-80gb",
            image="nginx:latest",
            ingress_opts={"disable_response_buffering": True},
            listening_port=80,
            logging={
                "destination_region_id": 1,
                "enabled": True,
                "retention_policy": {"period": 42},
                "topic_name": "my-log-name",
            },
            probes={
                "liveness_probe": {
                    "enabled": True,
                    "probe": {
                        "exec": {"command": ["ls", "-l"]},
                        "failure_threshold": 3,
                        "http_get": {
                            "headers": {"Authorization": "Bearer token 123"},
                            "host": "127.0.0.1",
                            "path": "/healthz",
                            "port": 80,
                            "schema": "HTTP",
                        },
                        "initial_delay_seconds": 0,
                        "period_seconds": 5,
                        "success_threshold": 1,
                        "tcp_socket": {"port": 80},
                        "timeout_seconds": 1,
                    },
                },
                "readiness_probe": {
                    "enabled": True,
                    "probe": {
                        "exec": {"command": ["ls", "-l"]},
                        "failure_threshold": 3,
                        "http_get": {
                            "headers": {"Authorization": "Bearer token 123"},
                            "host": "127.0.0.1",
                            "path": "/healthz",
                            "port": 80,
                            "schema": "HTTP",
                        },
                        "initial_delay_seconds": 0,
                        "period_seconds": 5,
                        "success_threshold": 1,
                        "tcp_socket": {"port": 80},
                        "timeout_seconds": 1,
                    },
                },
                "startup_probe": {
                    "enabled": True,
                    "probe": {
                        "exec": {"command": ["ls", "-l"]},
                        "failure_threshold": 3,
                        "http_get": {
                            "headers": {"Authorization": "Bearer token 123"},
                            "host": "127.0.0.1",
                            "path": "/healthz",
                            "port": 80,
                            "schema": "HTTP",
                        },
                        "initial_delay_seconds": 0,
                        "period_seconds": 5,
                        "success_threshold": 1,
                        "tcp_socket": {"port": 80},
                        "timeout_seconds": 1,
                    },
                },
            },
            api_timeout=120,
        )
        assert_matches_type(TaskIDList, deployment, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.inference.deployments.with_raw_response.update(
            deployment_name="my-instance",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = await response.parse()
        assert_matches_type(TaskIDList, deployment, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.inference.deployments.with_streaming_response.update(
            deployment_name="my-instance",
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
            await async_client.cloud.inference.deployments.with_raw_response.update(
                deployment_name="",
                project_id=1,
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        deployment = await async_client.cloud.inference.deployments.list(
            project_id=1,
        )
        assert_matches_type(AsyncOffsetPage[InferenceDeployment], deployment, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        deployment = await async_client.cloud.inference.deployments.list(
            project_id=1,
            limit=1000,
            offset=0,
        )
        assert_matches_type(AsyncOffsetPage[InferenceDeployment], deployment, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.inference.deployments.with_raw_response.list(
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = await response.parse()
        assert_matches_type(AsyncOffsetPage[InferenceDeployment], deployment, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.inference.deployments.with_streaming_response.list(
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = await response.parse()
            assert_matches_type(AsyncOffsetPage[InferenceDeployment], deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        deployment = await async_client.cloud.inference.deployments.delete(
            deployment_name="my-instance",
            project_id=1,
        )
        assert_matches_type(TaskIDList, deployment, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.inference.deployments.with_raw_response.delete(
            deployment_name="my-instance",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = await response.parse()
        assert_matches_type(TaskIDList, deployment, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.inference.deployments.with_streaming_response.delete(
            deployment_name="my-instance",
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
            await async_client.cloud.inference.deployments.with_raw_response.delete(
                deployment_name="",
                project_id=1,
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        deployment = await async_client.cloud.inference.deployments.get(
            deployment_name="my-instance",
            project_id=1,
        )
        assert_matches_type(InferenceDeployment, deployment, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.inference.deployments.with_raw_response.get(
            deployment_name="my-instance",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = await response.parse()
        assert_matches_type(InferenceDeployment, deployment, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.inference.deployments.with_streaming_response.get(
            deployment_name="my-instance",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = await response.parse()
            assert_matches_type(InferenceDeployment, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_name` but received ''"):
            await async_client.cloud.inference.deployments.with_raw_response.get(
                deployment_name="",
                project_id=1,
            )

    @parametrize
    async def test_method_get_api_key(self, async_client: AsyncGcore) -> None:
        deployment = await async_client.cloud.inference.deployments.get_api_key(
            deployment_name="my-instance",
            project_id=1,
        )
        assert_matches_type(InferenceDeploymentAPIKey, deployment, path=["response"])

    @parametrize
    async def test_raw_response_get_api_key(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.inference.deployments.with_raw_response.get_api_key(
            deployment_name="my-instance",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = await response.parse()
        assert_matches_type(InferenceDeploymentAPIKey, deployment, path=["response"])

    @parametrize
    async def test_streaming_response_get_api_key(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.inference.deployments.with_streaming_response.get_api_key(
            deployment_name="my-instance",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = await response.parse()
            assert_matches_type(InferenceDeploymentAPIKey, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_api_key(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_name` but received ''"):
            await async_client.cloud.inference.deployments.with_raw_response.get_api_key(
                deployment_name="",
                project_id=1,
            )

    @parametrize
    async def test_method_start(self, async_client: AsyncGcore) -> None:
        deployment = await async_client.cloud.inference.deployments.start(
            deployment_name="my-instance",
            project_id=1,
        )
        assert deployment is None

    @parametrize
    async def test_raw_response_start(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.inference.deployments.with_raw_response.start(
            deployment_name="my-instance",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = await response.parse()
        assert deployment is None

    @parametrize
    async def test_streaming_response_start(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.inference.deployments.with_streaming_response.start(
            deployment_name="my-instance",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = await response.parse()
            assert deployment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_start(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_name` but received ''"):
            await async_client.cloud.inference.deployments.with_raw_response.start(
                deployment_name="",
                project_id=1,
            )

    @parametrize
    async def test_method_stop(self, async_client: AsyncGcore) -> None:
        deployment = await async_client.cloud.inference.deployments.stop(
            deployment_name="my-instance",
            project_id=1,
        )
        assert deployment is None

    @parametrize
    async def test_raw_response_stop(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.inference.deployments.with_raw_response.stop(
            deployment_name="my-instance",
            project_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = await response.parse()
        assert deployment is None

    @parametrize
    async def test_streaming_response_stop(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.inference.deployments.with_streaming_response.stop(
            deployment_name="my-instance",
            project_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = await response.parse()
            assert deployment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_stop(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_name` but received ''"):
            await async_client.cloud.inference.deployments.with_raw_response.stop(
                deployment_name="",
                project_id=1,
            )
