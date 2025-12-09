# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cloud import TaskIDList, LoadBalancerL7Policy, LoadBalancerL7PolicyList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestL7Policies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: Gcore) -> None:
        l7_policy = client.cloud.load_balancers.l7_policies.create(
            project_id=1,
            region_id=1,
            action="REDIRECT_TO_URL",
            listener_id="023f2e34-7806-443b-bfae-16c324569a3d",
            redirect_url="https://www.example.com",
        )
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Gcore) -> None:
        l7_policy = client.cloud.load_balancers.l7_policies.create(
            project_id=1,
            region_id=1,
            action="REDIRECT_TO_URL",
            listener_id="023f2e34-7806-443b-bfae-16c324569a3d",
            redirect_url="https://www.example.com",
            name="redirect-example.com",
            position=1,
            redirect_http_code=301,
            tags=["test_tag"],
        )
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: Gcore) -> None:
        response = client.cloud.load_balancers.l7_policies.with_raw_response.create(
            project_id=1,
            region_id=1,
            action="REDIRECT_TO_URL",
            listener_id="023f2e34-7806-443b-bfae-16c324569a3d",
            redirect_url="https://www.example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        l7_policy = response.parse()
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: Gcore) -> None:
        with client.cloud.load_balancers.l7_policies.with_streaming_response.create(
            project_id=1,
            region_id=1,
            action="REDIRECT_TO_URL",
            listener_id="023f2e34-7806-443b-bfae-16c324569a3d",
            redirect_url="https://www.example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            l7_policy = response.parse()
            assert_matches_type(TaskIDList, l7_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_2(self, client: Gcore) -> None:
        l7_policy = client.cloud.load_balancers.l7_policies.create(
            project_id=1,
            region_id=1,
            action="REDIRECT_PREFIX",
            listener_id="023f2e34-7806-443b-bfae-16c324569a3d",
            redirect_prefix="/api/v1/policies",
        )
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Gcore) -> None:
        l7_policy = client.cloud.load_balancers.l7_policies.create(
            project_id=1,
            region_id=1,
            action="REDIRECT_PREFIX",
            listener_id="023f2e34-7806-443b-bfae-16c324569a3d",
            redirect_prefix="/api/v1/policies",
            name="redirect-example.com",
            position=1,
            redirect_http_code=301,
            tags=["test_tag"],
        )
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    def test_raw_response_create_overload_2(self, client: Gcore) -> None:
        response = client.cloud.load_balancers.l7_policies.with_raw_response.create(
            project_id=1,
            region_id=1,
            action="REDIRECT_PREFIX",
            listener_id="023f2e34-7806-443b-bfae-16c324569a3d",
            redirect_prefix="/api/v1/policies",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        l7_policy = response.parse()
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_2(self, client: Gcore) -> None:
        with client.cloud.load_balancers.l7_policies.with_streaming_response.create(
            project_id=1,
            region_id=1,
            action="REDIRECT_PREFIX",
            listener_id="023f2e34-7806-443b-bfae-16c324569a3d",
            redirect_prefix="/api/v1/policies",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            l7_policy = response.parse()
            assert_matches_type(TaskIDList, l7_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_3(self, client: Gcore) -> None:
        l7_policy = client.cloud.load_balancers.l7_policies.create(
            project_id=1,
            region_id=1,
            action="REDIRECT_TO_POOL",
            listener_id="023f2e34-7806-443b-bfae-16c324569a3d",
            redirect_pool_id="00000000-0000-4000-8000-000000000000",
        )
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_3(self, client: Gcore) -> None:
        l7_policy = client.cloud.load_balancers.l7_policies.create(
            project_id=1,
            region_id=1,
            action="REDIRECT_TO_POOL",
            listener_id="023f2e34-7806-443b-bfae-16c324569a3d",
            redirect_pool_id="00000000-0000-4000-8000-000000000000",
            name="redirect-example.com",
            position=1,
            tags=["test_tag"],
        )
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    def test_raw_response_create_overload_3(self, client: Gcore) -> None:
        response = client.cloud.load_balancers.l7_policies.with_raw_response.create(
            project_id=1,
            region_id=1,
            action="REDIRECT_TO_POOL",
            listener_id="023f2e34-7806-443b-bfae-16c324569a3d",
            redirect_pool_id="00000000-0000-4000-8000-000000000000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        l7_policy = response.parse()
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_3(self, client: Gcore) -> None:
        with client.cloud.load_balancers.l7_policies.with_streaming_response.create(
            project_id=1,
            region_id=1,
            action="REDIRECT_TO_POOL",
            listener_id="023f2e34-7806-443b-bfae-16c324569a3d",
            redirect_pool_id="00000000-0000-4000-8000-000000000000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            l7_policy = response.parse()
            assert_matches_type(TaskIDList, l7_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_4(self, client: Gcore) -> None:
        l7_policy = client.cloud.load_balancers.l7_policies.create(
            project_id=1,
            region_id=1,
            action="REJECT",
            listener_id="023f2e34-7806-443b-bfae-16c324569a3d",
        )
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_4(self, client: Gcore) -> None:
        l7_policy = client.cloud.load_balancers.l7_policies.create(
            project_id=1,
            region_id=1,
            action="REJECT",
            listener_id="023f2e34-7806-443b-bfae-16c324569a3d",
            name="redirect-example.com",
            position=1,
            tags=["test_tag"],
        )
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    def test_raw_response_create_overload_4(self, client: Gcore) -> None:
        response = client.cloud.load_balancers.l7_policies.with_raw_response.create(
            project_id=1,
            region_id=1,
            action="REJECT",
            listener_id="023f2e34-7806-443b-bfae-16c324569a3d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        l7_policy = response.parse()
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_4(self, client: Gcore) -> None:
        with client.cloud.load_balancers.l7_policies.with_streaming_response.create(
            project_id=1,
            region_id=1,
            action="REJECT",
            listener_id="023f2e34-7806-443b-bfae-16c324569a3d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            l7_policy = response.parse()
            assert_matches_type(TaskIDList, l7_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_overload_1(self, client: Gcore) -> None:
        l7_policy = client.cloud.load_balancers.l7_policies.update(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            action="REDIRECT_TO_URL",
            redirect_url="https://www.example.com",
        )
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_1(self, client: Gcore) -> None:
        l7_policy = client.cloud.load_balancers.l7_policies.update(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            action="REDIRECT_TO_URL",
            redirect_url="https://www.example.com",
            name="redirect-example.com",
            position=1,
            redirect_http_code=301,
            tags=["test_tag"],
        )
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    def test_raw_response_update_overload_1(self, client: Gcore) -> None:
        response = client.cloud.load_balancers.l7_policies.with_raw_response.update(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            action="REDIRECT_TO_URL",
            redirect_url="https://www.example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        l7_policy = response.parse()
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_1(self, client: Gcore) -> None:
        with client.cloud.load_balancers.l7_policies.with_streaming_response.update(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            action="REDIRECT_TO_URL",
            redirect_url="https://www.example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            l7_policy = response.parse()
            assert_matches_type(TaskIDList, l7_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_overload_1(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `l7policy_id` but received ''"):
            client.cloud.load_balancers.l7_policies.with_raw_response.update(
                l7policy_id="",
                project_id=1,
                region_id=1,
                action="REDIRECT_TO_URL",
                redirect_url="https://www.example.com",
            )

    @parametrize
    def test_method_update_overload_2(self, client: Gcore) -> None:
        l7_policy = client.cloud.load_balancers.l7_policies.update(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            action="REDIRECT_PREFIX",
            redirect_prefix="/api/v1/policies",
        )
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_2(self, client: Gcore) -> None:
        l7_policy = client.cloud.load_balancers.l7_policies.update(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            action="REDIRECT_PREFIX",
            redirect_prefix="/api/v1/policies",
            name="redirect-example.com",
            position=1,
            redirect_http_code=301,
            tags=["test_tag"],
        )
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    def test_raw_response_update_overload_2(self, client: Gcore) -> None:
        response = client.cloud.load_balancers.l7_policies.with_raw_response.update(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            action="REDIRECT_PREFIX",
            redirect_prefix="/api/v1/policies",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        l7_policy = response.parse()
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_2(self, client: Gcore) -> None:
        with client.cloud.load_balancers.l7_policies.with_streaming_response.update(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            action="REDIRECT_PREFIX",
            redirect_prefix="/api/v1/policies",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            l7_policy = response.parse()
            assert_matches_type(TaskIDList, l7_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_overload_2(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `l7policy_id` but received ''"):
            client.cloud.load_balancers.l7_policies.with_raw_response.update(
                l7policy_id="",
                project_id=1,
                region_id=1,
                action="REDIRECT_PREFIX",
                redirect_prefix="/api/v1/policies",
            )

    @parametrize
    def test_method_update_overload_3(self, client: Gcore) -> None:
        l7_policy = client.cloud.load_balancers.l7_policies.update(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            action="REDIRECT_TO_POOL",
            redirect_pool_id="00000000-0000-4000-8000-000000000000",
        )
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_3(self, client: Gcore) -> None:
        l7_policy = client.cloud.load_balancers.l7_policies.update(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            action="REDIRECT_TO_POOL",
            redirect_pool_id="00000000-0000-4000-8000-000000000000",
            name="redirect-example.com",
            position=1,
            tags=["test_tag"],
        )
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    def test_raw_response_update_overload_3(self, client: Gcore) -> None:
        response = client.cloud.load_balancers.l7_policies.with_raw_response.update(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            action="REDIRECT_TO_POOL",
            redirect_pool_id="00000000-0000-4000-8000-000000000000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        l7_policy = response.parse()
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_3(self, client: Gcore) -> None:
        with client.cloud.load_balancers.l7_policies.with_streaming_response.update(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            action="REDIRECT_TO_POOL",
            redirect_pool_id="00000000-0000-4000-8000-000000000000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            l7_policy = response.parse()
            assert_matches_type(TaskIDList, l7_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_overload_3(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `l7policy_id` but received ''"):
            client.cloud.load_balancers.l7_policies.with_raw_response.update(
                l7policy_id="",
                project_id=1,
                region_id=1,
                action="REDIRECT_TO_POOL",
                redirect_pool_id="00000000-0000-4000-8000-000000000000",
            )

    @parametrize
    def test_method_update_overload_4(self, client: Gcore) -> None:
        l7_policy = client.cloud.load_balancers.l7_policies.update(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            action="REJECT",
        )
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_4(self, client: Gcore) -> None:
        l7_policy = client.cloud.load_balancers.l7_policies.update(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            action="REJECT",
            name="redirect-example.com",
            position=1,
            tags=["test_tag"],
        )
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    def test_raw_response_update_overload_4(self, client: Gcore) -> None:
        response = client.cloud.load_balancers.l7_policies.with_raw_response.update(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            action="REJECT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        l7_policy = response.parse()
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_4(self, client: Gcore) -> None:
        with client.cloud.load_balancers.l7_policies.with_streaming_response.update(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            action="REJECT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            l7_policy = response.parse()
            assert_matches_type(TaskIDList, l7_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_overload_4(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `l7policy_id` but received ''"):
            client.cloud.load_balancers.l7_policies.with_raw_response.update(
                l7policy_id="",
                project_id=1,
                region_id=1,
                action="REJECT",
            )

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        l7_policy = client.cloud.load_balancers.l7_policies.list(
            project_id=1,
            region_id=1,
        )
        assert_matches_type(LoadBalancerL7PolicyList, l7_policy, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.load_balancers.l7_policies.with_raw_response.list(
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        l7_policy = response.parse()
        assert_matches_type(LoadBalancerL7PolicyList, l7_policy, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.load_balancers.l7_policies.with_streaming_response.list(
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            l7_policy = response.parse()
            assert_matches_type(LoadBalancerL7PolicyList, l7_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        l7_policy = client.cloud.load_balancers.l7_policies.delete(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cloud.load_balancers.l7_policies.with_raw_response.delete(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        l7_policy = response.parse()
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cloud.load_balancers.l7_policies.with_streaming_response.delete(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            l7_policy = response.parse()
            assert_matches_type(TaskIDList, l7_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `l7policy_id` but received ''"):
            client.cloud.load_balancers.l7_policies.with_raw_response.delete(
                l7policy_id="",
                project_id=1,
                region_id=1,
            )

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        l7_policy = client.cloud.load_balancers.l7_policies.get(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(LoadBalancerL7Policy, l7_policy, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cloud.load_balancers.l7_policies.with_raw_response.get(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        l7_policy = response.parse()
        assert_matches_type(LoadBalancerL7Policy, l7_policy, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cloud.load_balancers.l7_policies.with_streaming_response.get(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            l7_policy = response.parse()
            assert_matches_type(LoadBalancerL7Policy, l7_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `l7policy_id` but received ''"):
            client.cloud.load_balancers.l7_policies.with_raw_response.get(
                l7policy_id="",
                project_id=1,
                region_id=1,
            )


class TestAsyncL7Policies:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncGcore) -> None:
        l7_policy = await async_client.cloud.load_balancers.l7_policies.create(
            project_id=1,
            region_id=1,
            action="REDIRECT_TO_URL",
            listener_id="023f2e34-7806-443b-bfae-16c324569a3d",
            redirect_url="https://www.example.com",
        )
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncGcore) -> None:
        l7_policy = await async_client.cloud.load_balancers.l7_policies.create(
            project_id=1,
            region_id=1,
            action="REDIRECT_TO_URL",
            listener_id="023f2e34-7806-443b-bfae-16c324569a3d",
            redirect_url="https://www.example.com",
            name="redirect-example.com",
            position=1,
            redirect_http_code=301,
            tags=["test_tag"],
        )
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.load_balancers.l7_policies.with_raw_response.create(
            project_id=1,
            region_id=1,
            action="REDIRECT_TO_URL",
            listener_id="023f2e34-7806-443b-bfae-16c324569a3d",
            redirect_url="https://www.example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        l7_policy = await response.parse()
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.load_balancers.l7_policies.with_streaming_response.create(
            project_id=1,
            region_id=1,
            action="REDIRECT_TO_URL",
            listener_id="023f2e34-7806-443b-bfae-16c324569a3d",
            redirect_url="https://www.example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            l7_policy = await response.parse()
            assert_matches_type(TaskIDList, l7_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncGcore) -> None:
        l7_policy = await async_client.cloud.load_balancers.l7_policies.create(
            project_id=1,
            region_id=1,
            action="REDIRECT_PREFIX",
            listener_id="023f2e34-7806-443b-bfae-16c324569a3d",
            redirect_prefix="/api/v1/policies",
        )
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncGcore) -> None:
        l7_policy = await async_client.cloud.load_balancers.l7_policies.create(
            project_id=1,
            region_id=1,
            action="REDIRECT_PREFIX",
            listener_id="023f2e34-7806-443b-bfae-16c324569a3d",
            redirect_prefix="/api/v1/policies",
            name="redirect-example.com",
            position=1,
            redirect_http_code=301,
            tags=["test_tag"],
        )
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.load_balancers.l7_policies.with_raw_response.create(
            project_id=1,
            region_id=1,
            action="REDIRECT_PREFIX",
            listener_id="023f2e34-7806-443b-bfae-16c324569a3d",
            redirect_prefix="/api/v1/policies",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        l7_policy = await response.parse()
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.load_balancers.l7_policies.with_streaming_response.create(
            project_id=1,
            region_id=1,
            action="REDIRECT_PREFIX",
            listener_id="023f2e34-7806-443b-bfae-16c324569a3d",
            redirect_prefix="/api/v1/policies",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            l7_policy = await response.parse()
            assert_matches_type(TaskIDList, l7_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_3(self, async_client: AsyncGcore) -> None:
        l7_policy = await async_client.cloud.load_balancers.l7_policies.create(
            project_id=1,
            region_id=1,
            action="REDIRECT_TO_POOL",
            listener_id="023f2e34-7806-443b-bfae-16c324569a3d",
            redirect_pool_id="00000000-0000-4000-8000-000000000000",
        )
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_3(self, async_client: AsyncGcore) -> None:
        l7_policy = await async_client.cloud.load_balancers.l7_policies.create(
            project_id=1,
            region_id=1,
            action="REDIRECT_TO_POOL",
            listener_id="023f2e34-7806-443b-bfae-16c324569a3d",
            redirect_pool_id="00000000-0000-4000-8000-000000000000",
            name="redirect-example.com",
            position=1,
            tags=["test_tag"],
        )
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_3(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.load_balancers.l7_policies.with_raw_response.create(
            project_id=1,
            region_id=1,
            action="REDIRECT_TO_POOL",
            listener_id="023f2e34-7806-443b-bfae-16c324569a3d",
            redirect_pool_id="00000000-0000-4000-8000-000000000000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        l7_policy = await response.parse()
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_3(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.load_balancers.l7_policies.with_streaming_response.create(
            project_id=1,
            region_id=1,
            action="REDIRECT_TO_POOL",
            listener_id="023f2e34-7806-443b-bfae-16c324569a3d",
            redirect_pool_id="00000000-0000-4000-8000-000000000000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            l7_policy = await response.parse()
            assert_matches_type(TaskIDList, l7_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_4(self, async_client: AsyncGcore) -> None:
        l7_policy = await async_client.cloud.load_balancers.l7_policies.create(
            project_id=1,
            region_id=1,
            action="REJECT",
            listener_id="023f2e34-7806-443b-bfae-16c324569a3d",
        )
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_4(self, async_client: AsyncGcore) -> None:
        l7_policy = await async_client.cloud.load_balancers.l7_policies.create(
            project_id=1,
            region_id=1,
            action="REJECT",
            listener_id="023f2e34-7806-443b-bfae-16c324569a3d",
            name="redirect-example.com",
            position=1,
            tags=["test_tag"],
        )
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_4(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.load_balancers.l7_policies.with_raw_response.create(
            project_id=1,
            region_id=1,
            action="REJECT",
            listener_id="023f2e34-7806-443b-bfae-16c324569a3d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        l7_policy = await response.parse()
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_4(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.load_balancers.l7_policies.with_streaming_response.create(
            project_id=1,
            region_id=1,
            action="REJECT",
            listener_id="023f2e34-7806-443b-bfae-16c324569a3d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            l7_policy = await response.parse()
            assert_matches_type(TaskIDList, l7_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_overload_1(self, async_client: AsyncGcore) -> None:
        l7_policy = await async_client.cloud.load_balancers.l7_policies.update(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            action="REDIRECT_TO_URL",
            redirect_url="https://www.example.com",
        )
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_1(self, async_client: AsyncGcore) -> None:
        l7_policy = await async_client.cloud.load_balancers.l7_policies.update(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            action="REDIRECT_TO_URL",
            redirect_url="https://www.example.com",
            name="redirect-example.com",
            position=1,
            redirect_http_code=301,
            tags=["test_tag"],
        )
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_1(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.load_balancers.l7_policies.with_raw_response.update(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            action="REDIRECT_TO_URL",
            redirect_url="https://www.example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        l7_policy = await response.parse()
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_1(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.load_balancers.l7_policies.with_streaming_response.update(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            action="REDIRECT_TO_URL",
            redirect_url="https://www.example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            l7_policy = await response.parse()
            assert_matches_type(TaskIDList, l7_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_overload_1(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `l7policy_id` but received ''"):
            await async_client.cloud.load_balancers.l7_policies.with_raw_response.update(
                l7policy_id="",
                project_id=1,
                region_id=1,
                action="REDIRECT_TO_URL",
                redirect_url="https://www.example.com",
            )

    @parametrize
    async def test_method_update_overload_2(self, async_client: AsyncGcore) -> None:
        l7_policy = await async_client.cloud.load_balancers.l7_policies.update(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            action="REDIRECT_PREFIX",
            redirect_prefix="/api/v1/policies",
        )
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_2(self, async_client: AsyncGcore) -> None:
        l7_policy = await async_client.cloud.load_balancers.l7_policies.update(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            action="REDIRECT_PREFIX",
            redirect_prefix="/api/v1/policies",
            name="redirect-example.com",
            position=1,
            redirect_http_code=301,
            tags=["test_tag"],
        )
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.load_balancers.l7_policies.with_raw_response.update(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            action="REDIRECT_PREFIX",
            redirect_prefix="/api/v1/policies",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        l7_policy = await response.parse()
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_2(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.load_balancers.l7_policies.with_streaming_response.update(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            action="REDIRECT_PREFIX",
            redirect_prefix="/api/v1/policies",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            l7_policy = await response.parse()
            assert_matches_type(TaskIDList, l7_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_overload_2(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `l7policy_id` but received ''"):
            await async_client.cloud.load_balancers.l7_policies.with_raw_response.update(
                l7policy_id="",
                project_id=1,
                region_id=1,
                action="REDIRECT_PREFIX",
                redirect_prefix="/api/v1/policies",
            )

    @parametrize
    async def test_method_update_overload_3(self, async_client: AsyncGcore) -> None:
        l7_policy = await async_client.cloud.load_balancers.l7_policies.update(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            action="REDIRECT_TO_POOL",
            redirect_pool_id="00000000-0000-4000-8000-000000000000",
        )
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_3(self, async_client: AsyncGcore) -> None:
        l7_policy = await async_client.cloud.load_balancers.l7_policies.update(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            action="REDIRECT_TO_POOL",
            redirect_pool_id="00000000-0000-4000-8000-000000000000",
            name="redirect-example.com",
            position=1,
            tags=["test_tag"],
        )
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_3(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.load_balancers.l7_policies.with_raw_response.update(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            action="REDIRECT_TO_POOL",
            redirect_pool_id="00000000-0000-4000-8000-000000000000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        l7_policy = await response.parse()
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_3(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.load_balancers.l7_policies.with_streaming_response.update(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            action="REDIRECT_TO_POOL",
            redirect_pool_id="00000000-0000-4000-8000-000000000000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            l7_policy = await response.parse()
            assert_matches_type(TaskIDList, l7_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_overload_3(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `l7policy_id` but received ''"):
            await async_client.cloud.load_balancers.l7_policies.with_raw_response.update(
                l7policy_id="",
                project_id=1,
                region_id=1,
                action="REDIRECT_TO_POOL",
                redirect_pool_id="00000000-0000-4000-8000-000000000000",
            )

    @parametrize
    async def test_method_update_overload_4(self, async_client: AsyncGcore) -> None:
        l7_policy = await async_client.cloud.load_balancers.l7_policies.update(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            action="REJECT",
        )
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_4(self, async_client: AsyncGcore) -> None:
        l7_policy = await async_client.cloud.load_balancers.l7_policies.update(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            action="REJECT",
            name="redirect-example.com",
            position=1,
            tags=["test_tag"],
        )
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_4(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.load_balancers.l7_policies.with_raw_response.update(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            action="REJECT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        l7_policy = await response.parse()
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_4(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.load_balancers.l7_policies.with_streaming_response.update(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
            action="REJECT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            l7_policy = await response.parse()
            assert_matches_type(TaskIDList, l7_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_overload_4(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `l7policy_id` but received ''"):
            await async_client.cloud.load_balancers.l7_policies.with_raw_response.update(
                l7policy_id="",
                project_id=1,
                region_id=1,
                action="REJECT",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        l7_policy = await async_client.cloud.load_balancers.l7_policies.list(
            project_id=1,
            region_id=1,
        )
        assert_matches_type(LoadBalancerL7PolicyList, l7_policy, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.load_balancers.l7_policies.with_raw_response.list(
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        l7_policy = await response.parse()
        assert_matches_type(LoadBalancerL7PolicyList, l7_policy, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.load_balancers.l7_policies.with_streaming_response.list(
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            l7_policy = await response.parse()
            assert_matches_type(LoadBalancerL7PolicyList, l7_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        l7_policy = await async_client.cloud.load_balancers.l7_policies.delete(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.load_balancers.l7_policies.with_raw_response.delete(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        l7_policy = await response.parse()
        assert_matches_type(TaskIDList, l7_policy, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.load_balancers.l7_policies.with_streaming_response.delete(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            l7_policy = await response.parse()
            assert_matches_type(TaskIDList, l7_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `l7policy_id` but received ''"):
            await async_client.cloud.load_balancers.l7_policies.with_raw_response.delete(
                l7policy_id="",
                project_id=1,
                region_id=1,
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        l7_policy = await async_client.cloud.load_balancers.l7_policies.get(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
        )
        assert_matches_type(LoadBalancerL7Policy, l7_policy, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.load_balancers.l7_policies.with_raw_response.get(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        l7_policy = await response.parse()
        assert_matches_type(LoadBalancerL7Policy, l7_policy, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.load_balancers.l7_policies.with_streaming_response.get(
            l7policy_id="023f2e34-7806-443b-bfae-16c324569a3d",
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            l7_policy = await response.parse()
            assert_matches_type(LoadBalancerL7Policy, l7_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `l7policy_id` but received ''"):
            await async_client.cloud.load_balancers.l7_policies.with_raw_response.get(
                l7policy_id="",
                project_id=1,
                region_id=1,
            )
