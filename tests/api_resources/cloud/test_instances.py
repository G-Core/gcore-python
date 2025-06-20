# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore._utils import parse_datetime
from gcore.pagination import SyncOffsetPage, AsyncOffsetPage
from gcore.types.cloud import (
    Console,
    Instance,
    TaskIDList,
    InstanceInterface,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInstances:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        instance = client.cloud.instances.create(
            project_id=1,
            region_id=1,
            flavor="g2-standard-32-64",
            interfaces=[{"type": "external"}],
            volumes=[
                {
                    "size": 20,
                    "source": "new-volume",
                }
            ],
        )
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        instance = client.cloud.instances.create(
            project_id=1,
            region_id=1,
            flavor="g2-standard-32-64",
            interfaces=[
                {
                    "type": "external",
                    "interface_name": "eth0",
                    "ip_family": "ipv4",
                    "security_groups": [{"id": "ae74714c-c380-48b4-87f8-758d656cdad6"}],
                }
            ],
            volumes=[
                {
                    "size": 20,
                    "source": "new-volume",
                    "attachment_tag": "boot",
                    "delete_on_termination": False,
                    "name": "boot-volume",
                    "tags": {"my-tag": "my-tag-value"},
                    "type_name": "ssd_hiiops",
                }
            ],
            allow_app_ports=True,
            configuration={},
            name="my-instance",
            name_template="name_template",
            password="password",
            security_groups=[{"id": "ae74714c-c380-48b4-87f8-758d656cdad6"}],
            servergroup_id="servergroup_id",
            ssh_key_name="my-ssh-key",
            tags={"my-tag": "my-tag-value"},
            user_data="user_data",
            username="username",
        )
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.cloud.instances.with_raw_response.create(
            project_id=1,
            region_id=1,
            flavor="g2-standard-32-64",
            interfaces=[{"type": "external"}],
            volumes=[
                {
                    "size": 20,
                    "source": "new-volume",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.cloud.instances.with_streaming_response.create(
            project_id=1,
            region_id=1,
            flavor="g2-standard-32-64",
            interfaces=[{"type": "external"}],
            volumes=[
                {
                    "size": 20,
                    "source": "new-volume",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(TaskIDList, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        instance = client.cloud.instances.update(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            name="my-resource",
        )
        assert_matches_type(Instance, instance, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.cloud.instances.with_raw_response.update(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            name="my-resource",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(Instance, instance, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.cloud.instances.with_streaming_response.update(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            name="my-resource",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(Instance, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.cloud.instances.with_raw_response.update(
                instance_id="",
                project_id=0,
                region_id=0,
                name="my-resource",
            )

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        instance = client.cloud.instances.list(
            project_id=1,
            region_id=1,
        )
        assert_matches_type(SyncOffsetPage[Instance], instance, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gcore) -> None:
        instance = client.cloud.instances.list(
            project_id=1,
            region_id=1,
            available_floating=True,
            changes_before=parse_datetime("2025-10-01T12:00:00Z"),
            changes_since=parse_datetime("2025-10-01T12:00:00Z"),
            exclude_flavor_prefix="g1-",
            exclude_secgroup="secgroup_name",
            flavor_id="g2-standard-32-64",
            flavor_prefix="g2-",
            include_ai=False,
            include_baremetal=False,
            include_k8s=True,
            ip="192.168.0.1",
            limit=1000,
            name="name",
            offset=0,
            only_isolated=True,
            only_with_fixed_external_ip=True,
            order_by="name.asc",
            profile_name="profile_name",
            protection_status="Active",
            status="ACTIVE",
            tag_key_value="tag_key_value",
            tag_value=["value1", "value2"],
            type_ddos_profile="advanced",
            uuid="b5b4d65d-945f-4b98-ab6f-332319c724ef",
            with_ddos=True,
            with_interfaces_name=True,
        )
        assert_matches_type(SyncOffsetPage[Instance], instance, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cloud.instances.with_raw_response.list(
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(SyncOffsetPage[Instance], instance, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cloud.instances.with_streaming_response.list(
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(SyncOffsetPage[Instance], instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        instance = client.cloud.instances.delete(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Gcore) -> None:
        instance = client.cloud.instances.delete(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            delete_floatings=True,
            floatings="floatings",
            reserved_fixed_ips="reserved_fixed_ips",
            volumes="volume_id_1,volume_id_2",
        )
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cloud.instances.with_raw_response.delete(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cloud.instances.with_streaming_response.delete(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(TaskIDList, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.cloud.instances.with_raw_response.delete(
                instance_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    def test_method_action_overload_1(self, client: Gcore) -> None:
        instance = client.cloud.instances.action(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            action="start",
        )
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    def test_method_action_with_all_params_overload_1(self, client: Gcore) -> None:
        instance = client.cloud.instances.action(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            action="start",
            activate_profile=True,
        )
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    def test_raw_response_action_overload_1(self, client: Gcore) -> None:
        response = client.cloud.instances.with_raw_response.action(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            action="start",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    def test_streaming_response_action_overload_1(self, client: Gcore) -> None:
        with client.cloud.instances.with_streaming_response.action(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            action="start",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(TaskIDList, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_action_overload_1(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.cloud.instances.with_raw_response.action(
                instance_id="",
                project_id=0,
                region_id=0,
                action="start",
            )

    @parametrize
    def test_method_action_overload_2(self, client: Gcore) -> None:
        instance = client.cloud.instances.action(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            action="stop",
        )
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    def test_raw_response_action_overload_2(self, client: Gcore) -> None:
        response = client.cloud.instances.with_raw_response.action(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            action="stop",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    def test_streaming_response_action_overload_2(self, client: Gcore) -> None:
        with client.cloud.instances.with_streaming_response.action(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            action="stop",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(TaskIDList, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_action_overload_2(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.cloud.instances.with_raw_response.action(
                instance_id="",
                project_id=0,
                region_id=0,
                action="stop",
            )

    @parametrize
    def test_method_add_to_placement_group(self, client: Gcore) -> None:
        instance = client.cloud.instances.add_to_placement_group(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            servergroup_id="47003067-550a-6f17-93b6-81ee16ba061e",
        )
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    def test_raw_response_add_to_placement_group(self, client: Gcore) -> None:
        response = client.cloud.instances.with_raw_response.add_to_placement_group(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            servergroup_id="47003067-550a-6f17-93b6-81ee16ba061e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    def test_streaming_response_add_to_placement_group(self, client: Gcore) -> None:
        with client.cloud.instances.with_streaming_response.add_to_placement_group(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            servergroup_id="47003067-550a-6f17-93b6-81ee16ba061e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(TaskIDList, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_add_to_placement_group(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.cloud.instances.with_raw_response.add_to_placement_group(
                instance_id="",
                project_id=0,
                region_id=0,
                servergroup_id="47003067-550a-6f17-93b6-81ee16ba061e",
            )

    @parametrize
    def test_method_assign_security_group(self, client: Gcore) -> None:
        instance = client.cloud.instances.assign_security_group(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        )
        assert instance is None

    @parametrize
    def test_method_assign_security_group_with_all_params(self, client: Gcore) -> None:
        instance = client.cloud.instances.assign_security_group(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            name="some_name",
            ports_security_group_names=[
                {
                    "port_id": None,
                    "security_group_names": ["some_name"],
                },
                {
                    "port_id": "ee2402d0-f0cd-4503-9b75-69be1d11c5f1",
                    "security_group_names": ["name1", "name2"],
                },
            ],
        )
        assert instance is None

    @parametrize
    def test_raw_response_assign_security_group(self, client: Gcore) -> None:
        response = client.cloud.instances.with_raw_response.assign_security_group(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert instance is None

    @parametrize
    def test_streaming_response_assign_security_group(self, client: Gcore) -> None:
        with client.cloud.instances.with_streaming_response.assign_security_group(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert instance is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_assign_security_group(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.cloud.instances.with_raw_response.assign_security_group(
                instance_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    def test_method_disable_port_security(self, client: Gcore) -> None:
        instance = client.cloud.instances.disable_port_security(
            port_id="port_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(InstanceInterface, instance, path=["response"])

    @parametrize
    def test_raw_response_disable_port_security(self, client: Gcore) -> None:
        response = client.cloud.instances.with_raw_response.disable_port_security(
            port_id="port_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(InstanceInterface, instance, path=["response"])

    @parametrize
    def test_streaming_response_disable_port_security(self, client: Gcore) -> None:
        with client.cloud.instances.with_streaming_response.disable_port_security(
            port_id="port_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(InstanceInterface, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_disable_port_security(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `port_id` but received ''"):
            client.cloud.instances.with_raw_response.disable_port_security(
                port_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    def test_method_enable_port_security(self, client: Gcore) -> None:
        instance = client.cloud.instances.enable_port_security(
            port_id="port_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(InstanceInterface, instance, path=["response"])

    @parametrize
    def test_raw_response_enable_port_security(self, client: Gcore) -> None:
        response = client.cloud.instances.with_raw_response.enable_port_security(
            port_id="port_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(InstanceInterface, instance, path=["response"])

    @parametrize
    def test_streaming_response_enable_port_security(self, client: Gcore) -> None:
        with client.cloud.instances.with_streaming_response.enable_port_security(
            port_id="port_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(InstanceInterface, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_enable_port_security(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `port_id` but received ''"):
            client.cloud.instances.with_raw_response.enable_port_security(
                port_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        instance = client.cloud.instances.get(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(Instance, instance, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cloud.instances.with_raw_response.get(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(Instance, instance, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cloud.instances.with_streaming_response.get(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(Instance, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.cloud.instances.with_raw_response.get(
                instance_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    def test_method_get_console(self, client: Gcore) -> None:
        instance = client.cloud.instances.get_console(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(Console, instance, path=["response"])

    @parametrize
    def test_method_get_console_with_all_params(self, client: Gcore) -> None:
        instance = client.cloud.instances.get_console(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            console_type="console_type",
        )
        assert_matches_type(Console, instance, path=["response"])

    @parametrize
    def test_raw_response_get_console(self, client: Gcore) -> None:
        response = client.cloud.instances.with_raw_response.get_console(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(Console, instance, path=["response"])

    @parametrize
    def test_streaming_response_get_console(self, client: Gcore) -> None:
        with client.cloud.instances.with_streaming_response.get_console(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(Console, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_console(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.cloud.instances.with_raw_response.get_console(
                instance_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    def test_method_remove_from_placement_group(self, client: Gcore) -> None:
        instance = client.cloud.instances.remove_from_placement_group(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    def test_raw_response_remove_from_placement_group(self, client: Gcore) -> None:
        response = client.cloud.instances.with_raw_response.remove_from_placement_group(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    def test_streaming_response_remove_from_placement_group(self, client: Gcore) -> None:
        with client.cloud.instances.with_streaming_response.remove_from_placement_group(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(TaskIDList, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_remove_from_placement_group(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.cloud.instances.with_raw_response.remove_from_placement_group(
                instance_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    def test_method_resize(self, client: Gcore) -> None:
        instance = client.cloud.instances.resize(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            flavor_id="g1s-shared-1-0.5",
        )
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    def test_raw_response_resize(self, client: Gcore) -> None:
        response = client.cloud.instances.with_raw_response.resize(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            flavor_id="g1s-shared-1-0.5",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    def test_streaming_response_resize(self, client: Gcore) -> None:
        with client.cloud.instances.with_streaming_response.resize(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            flavor_id="g1s-shared-1-0.5",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(TaskIDList, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_resize(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.cloud.instances.with_raw_response.resize(
                instance_id="",
                project_id=0,
                region_id=0,
                flavor_id="g1s-shared-1-0.5",
            )

    @parametrize
    def test_method_unassign_security_group(self, client: Gcore) -> None:
        instance = client.cloud.instances.unassign_security_group(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        )
        assert instance is None

    @parametrize
    def test_method_unassign_security_group_with_all_params(self, client: Gcore) -> None:
        instance = client.cloud.instances.unassign_security_group(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            name="some_name",
            ports_security_group_names=[
                {
                    "port_id": None,
                    "security_group_names": ["some_name"],
                },
                {
                    "port_id": "ee2402d0-f0cd-4503-9b75-69be1d11c5f1",
                    "security_group_names": ["name1", "name2"],
                },
            ],
        )
        assert instance is None

    @parametrize
    def test_raw_response_unassign_security_group(self, client: Gcore) -> None:
        response = client.cloud.instances.with_raw_response.unassign_security_group(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert instance is None

    @parametrize
    def test_streaming_response_unassign_security_group(self, client: Gcore) -> None:
        with client.cloud.instances.with_streaming_response.unassign_security_group(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert instance is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_unassign_security_group(self, client: Gcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.cloud.instances.with_raw_response.unassign_security_group(
                instance_id="",
                project_id=0,
                region_id=0,
            )


class TestAsyncInstances:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        instance = await async_client.cloud.instances.create(
            project_id=1,
            region_id=1,
            flavor="g2-standard-32-64",
            interfaces=[{"type": "external"}],
            volumes=[
                {
                    "size": 20,
                    "source": "new-volume",
                }
            ],
        )
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        instance = await async_client.cloud.instances.create(
            project_id=1,
            region_id=1,
            flavor="g2-standard-32-64",
            interfaces=[
                {
                    "type": "external",
                    "interface_name": "eth0",
                    "ip_family": "ipv4",
                    "security_groups": [{"id": "ae74714c-c380-48b4-87f8-758d656cdad6"}],
                }
            ],
            volumes=[
                {
                    "size": 20,
                    "source": "new-volume",
                    "attachment_tag": "boot",
                    "delete_on_termination": False,
                    "name": "boot-volume",
                    "tags": {"my-tag": "my-tag-value"},
                    "type_name": "ssd_hiiops",
                }
            ],
            allow_app_ports=True,
            configuration={},
            name="my-instance",
            name_template="name_template",
            password="password",
            security_groups=[{"id": "ae74714c-c380-48b4-87f8-758d656cdad6"}],
            servergroup_id="servergroup_id",
            ssh_key_name="my-ssh-key",
            tags={"my-tag": "my-tag-value"},
            user_data="user_data",
            username="username",
        )
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.instances.with_raw_response.create(
            project_id=1,
            region_id=1,
            flavor="g2-standard-32-64",
            interfaces=[{"type": "external"}],
            volumes=[
                {
                    "size": 20,
                    "source": "new-volume",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.instances.with_streaming_response.create(
            project_id=1,
            region_id=1,
            flavor="g2-standard-32-64",
            interfaces=[{"type": "external"}],
            volumes=[
                {
                    "size": 20,
                    "source": "new-volume",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(TaskIDList, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        instance = await async_client.cloud.instances.update(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            name="my-resource",
        )
        assert_matches_type(Instance, instance, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.instances.with_raw_response.update(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            name="my-resource",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(Instance, instance, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.instances.with_streaming_response.update(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            name="my-resource",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(Instance, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.cloud.instances.with_raw_response.update(
                instance_id="",
                project_id=0,
                region_id=0,
                name="my-resource",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        instance = await async_client.cloud.instances.list(
            project_id=1,
            region_id=1,
        )
        assert_matches_type(AsyncOffsetPage[Instance], instance, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGcore) -> None:
        instance = await async_client.cloud.instances.list(
            project_id=1,
            region_id=1,
            available_floating=True,
            changes_before=parse_datetime("2025-10-01T12:00:00Z"),
            changes_since=parse_datetime("2025-10-01T12:00:00Z"),
            exclude_flavor_prefix="g1-",
            exclude_secgroup="secgroup_name",
            flavor_id="g2-standard-32-64",
            flavor_prefix="g2-",
            include_ai=False,
            include_baremetal=False,
            include_k8s=True,
            ip="192.168.0.1",
            limit=1000,
            name="name",
            offset=0,
            only_isolated=True,
            only_with_fixed_external_ip=True,
            order_by="name.asc",
            profile_name="profile_name",
            protection_status="Active",
            status="ACTIVE",
            tag_key_value="tag_key_value",
            tag_value=["value1", "value2"],
            type_ddos_profile="advanced",
            uuid="b5b4d65d-945f-4b98-ab6f-332319c724ef",
            with_ddos=True,
            with_interfaces_name=True,
        )
        assert_matches_type(AsyncOffsetPage[Instance], instance, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.instances.with_raw_response.list(
            project_id=1,
            region_id=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(AsyncOffsetPage[Instance], instance, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.instances.with_streaming_response.list(
            project_id=1,
            region_id=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(AsyncOffsetPage[Instance], instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        instance = await async_client.cloud.instances.delete(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncGcore) -> None:
        instance = await async_client.cloud.instances.delete(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            delete_floatings=True,
            floatings="floatings",
            reserved_fixed_ips="reserved_fixed_ips",
            volumes="volume_id_1,volume_id_2",
        )
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.instances.with_raw_response.delete(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.instances.with_streaming_response.delete(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(TaskIDList, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.cloud.instances.with_raw_response.delete(
                instance_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    async def test_method_action_overload_1(self, async_client: AsyncGcore) -> None:
        instance = await async_client.cloud.instances.action(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            action="start",
        )
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    async def test_method_action_with_all_params_overload_1(self, async_client: AsyncGcore) -> None:
        instance = await async_client.cloud.instances.action(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            action="start",
            activate_profile=True,
        )
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    async def test_raw_response_action_overload_1(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.instances.with_raw_response.action(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            action="start",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    async def test_streaming_response_action_overload_1(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.instances.with_streaming_response.action(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            action="start",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(TaskIDList, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_action_overload_1(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.cloud.instances.with_raw_response.action(
                instance_id="",
                project_id=0,
                region_id=0,
                action="start",
            )

    @parametrize
    async def test_method_action_overload_2(self, async_client: AsyncGcore) -> None:
        instance = await async_client.cloud.instances.action(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            action="stop",
        )
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    async def test_raw_response_action_overload_2(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.instances.with_raw_response.action(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            action="stop",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    async def test_streaming_response_action_overload_2(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.instances.with_streaming_response.action(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            action="stop",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(TaskIDList, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_action_overload_2(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.cloud.instances.with_raw_response.action(
                instance_id="",
                project_id=0,
                region_id=0,
                action="stop",
            )

    @parametrize
    async def test_method_add_to_placement_group(self, async_client: AsyncGcore) -> None:
        instance = await async_client.cloud.instances.add_to_placement_group(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            servergroup_id="47003067-550a-6f17-93b6-81ee16ba061e",
        )
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    async def test_raw_response_add_to_placement_group(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.instances.with_raw_response.add_to_placement_group(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            servergroup_id="47003067-550a-6f17-93b6-81ee16ba061e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    async def test_streaming_response_add_to_placement_group(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.instances.with_streaming_response.add_to_placement_group(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            servergroup_id="47003067-550a-6f17-93b6-81ee16ba061e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(TaskIDList, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_add_to_placement_group(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.cloud.instances.with_raw_response.add_to_placement_group(
                instance_id="",
                project_id=0,
                region_id=0,
                servergroup_id="47003067-550a-6f17-93b6-81ee16ba061e",
            )

    @parametrize
    async def test_method_assign_security_group(self, async_client: AsyncGcore) -> None:
        instance = await async_client.cloud.instances.assign_security_group(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        )
        assert instance is None

    @parametrize
    async def test_method_assign_security_group_with_all_params(self, async_client: AsyncGcore) -> None:
        instance = await async_client.cloud.instances.assign_security_group(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            name="some_name",
            ports_security_group_names=[
                {
                    "port_id": None,
                    "security_group_names": ["some_name"],
                },
                {
                    "port_id": "ee2402d0-f0cd-4503-9b75-69be1d11c5f1",
                    "security_group_names": ["name1", "name2"],
                },
            ],
        )
        assert instance is None

    @parametrize
    async def test_raw_response_assign_security_group(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.instances.with_raw_response.assign_security_group(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert instance is None

    @parametrize
    async def test_streaming_response_assign_security_group(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.instances.with_streaming_response.assign_security_group(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert instance is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_assign_security_group(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.cloud.instances.with_raw_response.assign_security_group(
                instance_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    async def test_method_disable_port_security(self, async_client: AsyncGcore) -> None:
        instance = await async_client.cloud.instances.disable_port_security(
            port_id="port_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(InstanceInterface, instance, path=["response"])

    @parametrize
    async def test_raw_response_disable_port_security(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.instances.with_raw_response.disable_port_security(
            port_id="port_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(InstanceInterface, instance, path=["response"])

    @parametrize
    async def test_streaming_response_disable_port_security(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.instances.with_streaming_response.disable_port_security(
            port_id="port_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(InstanceInterface, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_disable_port_security(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `port_id` but received ''"):
            await async_client.cloud.instances.with_raw_response.disable_port_security(
                port_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    async def test_method_enable_port_security(self, async_client: AsyncGcore) -> None:
        instance = await async_client.cloud.instances.enable_port_security(
            port_id="port_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(InstanceInterface, instance, path=["response"])

    @parametrize
    async def test_raw_response_enable_port_security(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.instances.with_raw_response.enable_port_security(
            port_id="port_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(InstanceInterface, instance, path=["response"])

    @parametrize
    async def test_streaming_response_enable_port_security(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.instances.with_streaming_response.enable_port_security(
            port_id="port_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(InstanceInterface, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_enable_port_security(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `port_id` but received ''"):
            await async_client.cloud.instances.with_raw_response.enable_port_security(
                port_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        instance = await async_client.cloud.instances.get(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(Instance, instance, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.instances.with_raw_response.get(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(Instance, instance, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.instances.with_streaming_response.get(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(Instance, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.cloud.instances.with_raw_response.get(
                instance_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    async def test_method_get_console(self, async_client: AsyncGcore) -> None:
        instance = await async_client.cloud.instances.get_console(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(Console, instance, path=["response"])

    @parametrize
    async def test_method_get_console_with_all_params(self, async_client: AsyncGcore) -> None:
        instance = await async_client.cloud.instances.get_console(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            console_type="console_type",
        )
        assert_matches_type(Console, instance, path=["response"])

    @parametrize
    async def test_raw_response_get_console(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.instances.with_raw_response.get_console(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(Console, instance, path=["response"])

    @parametrize
    async def test_streaming_response_get_console(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.instances.with_streaming_response.get_console(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(Console, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_console(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.cloud.instances.with_raw_response.get_console(
                instance_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    async def test_method_remove_from_placement_group(self, async_client: AsyncGcore) -> None:
        instance = await async_client.cloud.instances.remove_from_placement_group(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        )
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    async def test_raw_response_remove_from_placement_group(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.instances.with_raw_response.remove_from_placement_group(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    async def test_streaming_response_remove_from_placement_group(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.instances.with_streaming_response.remove_from_placement_group(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(TaskIDList, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_remove_from_placement_group(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.cloud.instances.with_raw_response.remove_from_placement_group(
                instance_id="",
                project_id=0,
                region_id=0,
            )

    @parametrize
    async def test_method_resize(self, async_client: AsyncGcore) -> None:
        instance = await async_client.cloud.instances.resize(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            flavor_id="g1s-shared-1-0.5",
        )
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    async def test_raw_response_resize(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.instances.with_raw_response.resize(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            flavor_id="g1s-shared-1-0.5",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(TaskIDList, instance, path=["response"])

    @parametrize
    async def test_streaming_response_resize(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.instances.with_streaming_response.resize(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            flavor_id="g1s-shared-1-0.5",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(TaskIDList, instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_resize(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.cloud.instances.with_raw_response.resize(
                instance_id="",
                project_id=0,
                region_id=0,
                flavor_id="g1s-shared-1-0.5",
            )

    @parametrize
    async def test_method_unassign_security_group(self, async_client: AsyncGcore) -> None:
        instance = await async_client.cloud.instances.unassign_security_group(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        )
        assert instance is None

    @parametrize
    async def test_method_unassign_security_group_with_all_params(self, async_client: AsyncGcore) -> None:
        instance = await async_client.cloud.instances.unassign_security_group(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
            name="some_name",
            ports_security_group_names=[
                {
                    "port_id": None,
                    "security_group_names": ["some_name"],
                },
                {
                    "port_id": "ee2402d0-f0cd-4503-9b75-69be1d11c5f1",
                    "security_group_names": ["name1", "name2"],
                },
            ],
        )
        assert instance is None

    @parametrize
    async def test_raw_response_unassign_security_group(self, async_client: AsyncGcore) -> None:
        response = await async_client.cloud.instances.with_raw_response.unassign_security_group(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert instance is None

    @parametrize
    async def test_streaming_response_unassign_security_group(self, async_client: AsyncGcore) -> None:
        async with async_client.cloud.instances.with_streaming_response.unassign_security_group(
            instance_id="instance_id",
            project_id=0,
            region_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert instance is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_unassign_security_group(self, async_client: AsyncGcore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.cloud.instances.with_raw_response.unassign_security_group(
                instance_id="",
                project_id=0,
                region_id=0,
            )
