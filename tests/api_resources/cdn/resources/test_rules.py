# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gcore import Gcore, AsyncGcore
from tests.utils import assert_matches_type
from gcore.types.cdn.resources import (
    CdnResourceRule,
    RuleListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gcore) -> None:
        rule = client.cdn.resources.rules.create(
            resource_id=0,
            name="My first rule",
            rule="/folder/images/*.png",
            rule_type=0,
        )
        assert_matches_type(CdnResourceRule, rule, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gcore) -> None:
        rule = client.cdn.resources.rules.create(
            resource_id=0,
            name="My first rule",
            rule="/folder/images/*.png",
            rule_type=0,
            active=True,
            options={
                "allowed_http_methods": {
                    "enabled": True,
                    "value": ["GET", "POST"],
                },
                "bot_protection": {
                    "bot_challenge": {"enabled": True},
                    "enabled": True,
                },
                "brotli_compression": {
                    "enabled": True,
                    "value": ["text/html", "text/plain"],
                },
                "browser_cache_settings": {
                    "enabled": True,
                    "value": "3600s",
                },
                "cache_http_headers": {
                    "enabled": False,
                    "value": [
                        "vary",
                        "content-length",
                        "last-modified",
                        "connection",
                        "accept-ranges",
                        "content-type",
                        "content-encoding",
                        "etag",
                        "cache-control",
                        "expires",
                        "keep-alive",
                        "server",
                    ],
                },
                "cors": {
                    "enabled": True,
                    "value": ["domain.com", "domain2.com"],
                    "always": True,
                },
                "country_acl": {
                    "enabled": True,
                    "excepted_values": ["GB", "DE"],
                    "policy_type": "allow",
                },
                "disable_cache": {
                    "enabled": True,
                    "value": False,
                },
                "disable_proxy_force_ranges": {
                    "enabled": True,
                    "value": True,
                },
                "edge_cache_settings": {
                    "enabled": True,
                    "custom_values": {"100": "43200s"},
                    "default": "321669910225",
                    "value": "43200s",
                },
                "fastedge": {
                    "enabled": True,
                    "on_request_body": {
                        "app_id": "1001",
                        "enabled": True,
                        "execute_on_edge": True,
                        "execute_on_shield": False,
                        "interrupt_on_error": True,
                    },
                    "on_request_headers": {
                        "app_id": "1001",
                        "enabled": True,
                        "execute_on_edge": True,
                        "execute_on_shield": False,
                        "interrupt_on_error": True,
                    },
                    "on_response_body": {
                        "app_id": "1001",
                        "enabled": True,
                        "execute_on_edge": True,
                        "execute_on_shield": False,
                        "interrupt_on_error": True,
                    },
                    "on_response_headers": {
                        "app_id": "1001",
                        "enabled": True,
                        "execute_on_edge": True,
                        "execute_on_shield": False,
                        "interrupt_on_error": True,
                    },
                },
                "fetch_compressed": {
                    "enabled": True,
                    "value": False,
                },
                "follow_origin_redirect": {
                    "codes": [302, 308],
                    "enabled": True,
                },
                "force_return": {
                    "body": "http://example.com/redirect_address",
                    "code": 301,
                    "enabled": True,
                    "time_interval": {
                        "end_time": "20:00",
                        "start_time": "09:00",
                        "time_zone": "CET",
                    },
                },
                "forward_host_header": {
                    "enabled": False,
                    "value": False,
                },
                "gzip_on": {
                    "enabled": True,
                    "value": True,
                },
                "host_header": {
                    "enabled": True,
                    "value": "host.com",
                },
                "ignore_cookie": {
                    "enabled": True,
                    "value": True,
                },
                "ignore_query_string": {
                    "enabled": True,
                    "value": False,
                },
                "image_stack": {
                    "enabled": True,
                    "avif_enabled": True,
                    "png_lossless": True,
                    "quality": 80,
                    "webp_enabled": False,
                },
                "ip_address_acl": {
                    "enabled": True,
                    "excepted_values": ["192.168.1.100/32"],
                    "policy_type": "deny",
                },
                "limit_bandwidth": {
                    "enabled": True,
                    "limit_type": "static",
                    "buffer": 200,
                    "speed": 100,
                },
                "proxy_cache_key": {
                    "enabled": True,
                    "value": "$scheme$uri",
                },
                "proxy_cache_methods_set": {
                    "enabled": True,
                    "value": False,
                },
                "proxy_connect_timeout": {
                    "enabled": True,
                    "value": "4s",
                },
                "proxy_read_timeout": {
                    "enabled": True,
                    "value": "10s",
                },
                "query_params_blacklist": {
                    "enabled": True,
                    "value": ["some", "blacklisted", "query"],
                },
                "query_params_whitelist": {
                    "enabled": True,
                    "value": ["some", "whitelisted", "query"],
                },
                "query_string_forwarding": {
                    "enabled": True,
                    "forward_from_file_types": ["m3u8", "mpd"],
                    "forward_to_file_types": ["ts", "mp4"],
                    "forward_except_keys": ["debug_info"],
                    "forward_only_keys": ["auth_token", "session_id"],
                },
                "redirect_http_to_https": {
                    "enabled": True,
                    "value": True,
                },
                "redirect_https_to_http": {
                    "enabled": False,
                    "value": True,
                },
                "referrer_acl": {
                    "enabled": True,
                    "excepted_values": ["example.com", "*.example.net"],
                    "policy_type": "deny",
                },
                "request_limiter": {
                    "enabled": True,
                    "rate": 5,
                    "rate_unit": "r/s",
                },
                "response_headers_hiding_policy": {
                    "enabled": True,
                    "excepted": ["my-header"],
                    "mode": "hide",
                },
                "rewrite": {
                    "body": "/(.*) /additional_path/$1",
                    "enabled": True,
                    "flag": "break",
                },
                "secure_key": {
                    "enabled": True,
                    "key": "secretkey",
                    "type": 2,
                },
                "slice": {
                    "enabled": True,
                    "value": True,
                },
                "sni": {
                    "custom_hostname": "custom.example.com",
                    "enabled": True,
                    "sni_type": "custom",
                },
                "stale": {
                    "enabled": True,
                    "value": ["http_404", "http_500"],
                },
                "static_response_headers": {
                    "enabled": True,
                    "value": [
                        {
                            "name": "X-Example",
                            "value": ["Value_1"],
                            "always": True,
                        },
                        {
                            "name": "X-Example-Multiple",
                            "value": ["Value_1", "Value_2", "Value_3"],
                            "always": False,
                        },
                    ],
                },
                "static_headers": {
                    "enabled": True,
                    "value": {
                        "X-Example": "Value_1",
                        "X-Example-Multiple": ["Value_2", "Value_3"],
                    },
                },
                "static_request_headers": {
                    "enabled": True,
                    "value": {
                        "Header-One": "Value 1",
                        "Header-Two": "Value 2",
                    },
                },
                "user_agent_acl": {
                    "enabled": True,
                    "excepted_values": ["UserAgent Value", ""],
                    "policy_type": "allow",
                },
                "waap": {
                    "enabled": True,
                    "value": True,
                },
                "websockets": {
                    "enabled": True,
                    "value": True,
                },
            },
            origin_group=None,
            override_origin_protocol="HTTPS",
            weight=1,
        )
        assert_matches_type(CdnResourceRule, rule, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gcore) -> None:
        response = client.cdn.resources.rules.with_raw_response.create(
            resource_id=0,
            name="My first rule",
            rule="/folder/images/*.png",
            rule_type=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(CdnResourceRule, rule, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gcore) -> None:
        with client.cdn.resources.rules.with_streaming_response.create(
            resource_id=0,
            name="My first rule",
            rule="/folder/images/*.png",
            rule_type=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(CdnResourceRule, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gcore) -> None:
        rule = client.cdn.resources.rules.update(
            rule_id=0,
            resource_id=0,
        )
        assert_matches_type(CdnResourceRule, rule, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gcore) -> None:
        rule = client.cdn.resources.rules.update(
            rule_id=0,
            resource_id=0,
            active=True,
            name="My first rule",
            options={
                "allowed_http_methods": {
                    "enabled": True,
                    "value": ["GET", "POST"],
                },
                "bot_protection": {
                    "bot_challenge": {"enabled": True},
                    "enabled": True,
                },
                "brotli_compression": {
                    "enabled": True,
                    "value": ["text/html", "text/plain"],
                },
                "browser_cache_settings": {
                    "enabled": True,
                    "value": "3600s",
                },
                "cache_http_headers": {
                    "enabled": False,
                    "value": [
                        "vary",
                        "content-length",
                        "last-modified",
                        "connection",
                        "accept-ranges",
                        "content-type",
                        "content-encoding",
                        "etag",
                        "cache-control",
                        "expires",
                        "keep-alive",
                        "server",
                    ],
                },
                "cors": {
                    "enabled": True,
                    "value": ["domain.com", "domain2.com"],
                    "always": True,
                },
                "country_acl": {
                    "enabled": True,
                    "excepted_values": ["GB", "DE"],
                    "policy_type": "allow",
                },
                "disable_cache": {
                    "enabled": True,
                    "value": False,
                },
                "disable_proxy_force_ranges": {
                    "enabled": True,
                    "value": True,
                },
                "edge_cache_settings": {
                    "enabled": True,
                    "custom_values": {"100": "43200s"},
                    "default": "321669910225",
                    "value": "43200s",
                },
                "fastedge": {
                    "enabled": True,
                    "on_request_body": {
                        "app_id": "1001",
                        "enabled": True,
                        "execute_on_edge": True,
                        "execute_on_shield": False,
                        "interrupt_on_error": True,
                    },
                    "on_request_headers": {
                        "app_id": "1001",
                        "enabled": True,
                        "execute_on_edge": True,
                        "execute_on_shield": False,
                        "interrupt_on_error": True,
                    },
                    "on_response_body": {
                        "app_id": "1001",
                        "enabled": True,
                        "execute_on_edge": True,
                        "execute_on_shield": False,
                        "interrupt_on_error": True,
                    },
                    "on_response_headers": {
                        "app_id": "1001",
                        "enabled": True,
                        "execute_on_edge": True,
                        "execute_on_shield": False,
                        "interrupt_on_error": True,
                    },
                },
                "fetch_compressed": {
                    "enabled": True,
                    "value": False,
                },
                "follow_origin_redirect": {
                    "codes": [302, 308],
                    "enabled": True,
                },
                "force_return": {
                    "body": "http://example.com/redirect_address",
                    "code": 301,
                    "enabled": True,
                    "time_interval": {
                        "end_time": "20:00",
                        "start_time": "09:00",
                        "time_zone": "CET",
                    },
                },
                "forward_host_header": {
                    "enabled": False,
                    "value": False,
                },
                "gzip_on": {
                    "enabled": True,
                    "value": True,
                },
                "host_header": {
                    "enabled": True,
                    "value": "host.com",
                },
                "ignore_cookie": {
                    "enabled": True,
                    "value": True,
                },
                "ignore_query_string": {
                    "enabled": True,
                    "value": False,
                },
                "image_stack": {
                    "enabled": True,
                    "avif_enabled": True,
                    "png_lossless": True,
                    "quality": 80,
                    "webp_enabled": False,
                },
                "ip_address_acl": {
                    "enabled": True,
                    "excepted_values": ["192.168.1.100/32"],
                    "policy_type": "deny",
                },
                "limit_bandwidth": {
                    "enabled": True,
                    "limit_type": "static",
                    "buffer": 200,
                    "speed": 100,
                },
                "proxy_cache_key": {
                    "enabled": True,
                    "value": "$scheme$uri",
                },
                "proxy_cache_methods_set": {
                    "enabled": True,
                    "value": False,
                },
                "proxy_connect_timeout": {
                    "enabled": True,
                    "value": "4s",
                },
                "proxy_read_timeout": {
                    "enabled": True,
                    "value": "10s",
                },
                "query_params_blacklist": {
                    "enabled": True,
                    "value": ["some", "blacklisted", "query"],
                },
                "query_params_whitelist": {
                    "enabled": True,
                    "value": ["some", "whitelisted", "query"],
                },
                "query_string_forwarding": {
                    "enabled": True,
                    "forward_from_file_types": ["m3u8", "mpd"],
                    "forward_to_file_types": ["ts", "mp4"],
                    "forward_except_keys": ["debug_info"],
                    "forward_only_keys": ["auth_token", "session_id"],
                },
                "redirect_http_to_https": {
                    "enabled": True,
                    "value": True,
                },
                "redirect_https_to_http": {
                    "enabled": False,
                    "value": True,
                },
                "referrer_acl": {
                    "enabled": True,
                    "excepted_values": ["example.com", "*.example.net"],
                    "policy_type": "deny",
                },
                "request_limiter": {
                    "enabled": True,
                    "rate": 5,
                    "rate_unit": "r/s",
                },
                "response_headers_hiding_policy": {
                    "enabled": True,
                    "excepted": ["my-header"],
                    "mode": "hide",
                },
                "rewrite": {
                    "body": "/(.*) /additional_path/$1",
                    "enabled": True,
                    "flag": "break",
                },
                "secure_key": {
                    "enabled": True,
                    "key": "secretkey",
                    "type": 2,
                },
                "slice": {
                    "enabled": True,
                    "value": True,
                },
                "sni": {
                    "custom_hostname": "custom.example.com",
                    "enabled": True,
                    "sni_type": "custom",
                },
                "stale": {
                    "enabled": True,
                    "value": ["http_404", "http_500"],
                },
                "static_response_headers": {
                    "enabled": True,
                    "value": [
                        {
                            "name": "X-Example",
                            "value": ["Value_1"],
                            "always": True,
                        },
                        {
                            "name": "X-Example-Multiple",
                            "value": ["Value_1", "Value_2", "Value_3"],
                            "always": False,
                        },
                    ],
                },
                "static_headers": {
                    "enabled": True,
                    "value": {
                        "X-Example": "Value_1",
                        "X-Example-Multiple": ["Value_2", "Value_3"],
                    },
                },
                "static_request_headers": {
                    "enabled": True,
                    "value": {
                        "Header-One": "Value 1",
                        "Header-Two": "Value 2",
                    },
                },
                "user_agent_acl": {
                    "enabled": True,
                    "excepted_values": ["UserAgent Value", ""],
                    "policy_type": "allow",
                },
                "waap": {
                    "enabled": True,
                    "value": True,
                },
                "websockets": {
                    "enabled": True,
                    "value": True,
                },
            },
            origin_group=None,
            override_origin_protocol="HTTPS",
            rule="/folder/images/*.png",
            rule_type=0,
            weight=1,
        )
        assert_matches_type(CdnResourceRule, rule, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gcore) -> None:
        response = client.cdn.resources.rules.with_raw_response.update(
            rule_id=0,
            resource_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(CdnResourceRule, rule, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gcore) -> None:
        with client.cdn.resources.rules.with_streaming_response.update(
            rule_id=0,
            resource_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(CdnResourceRule, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gcore) -> None:
        rule = client.cdn.resources.rules.list(
            0,
        )
        assert_matches_type(RuleListResponse, rule, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gcore) -> None:
        response = client.cdn.resources.rules.with_raw_response.list(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleListResponse, rule, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gcore) -> None:
        with client.cdn.resources.rules.with_streaming_response.list(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleListResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gcore) -> None:
        rule = client.cdn.resources.rules.delete(
            rule_id=0,
            resource_id=0,
        )
        assert rule is None

    @parametrize
    def test_raw_response_delete(self, client: Gcore) -> None:
        response = client.cdn.resources.rules.with_raw_response.delete(
            rule_id=0,
            resource_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert rule is None

    @parametrize
    def test_streaming_response_delete(self, client: Gcore) -> None:
        with client.cdn.resources.rules.with_streaming_response.delete(
            rule_id=0,
            resource_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert rule is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Gcore) -> None:
        rule = client.cdn.resources.rules.get(
            rule_id=0,
            resource_id=0,
        )
        assert_matches_type(CdnResourceRule, rule, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Gcore) -> None:
        response = client.cdn.resources.rules.with_raw_response.get(
            rule_id=0,
            resource_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(CdnResourceRule, rule, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Gcore) -> None:
        with client.cdn.resources.rules.with_streaming_response.get(
            rule_id=0,
            resource_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(CdnResourceRule, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_replace(self, client: Gcore) -> None:
        rule = client.cdn.resources.rules.replace(
            rule_id=0,
            resource_id=0,
            rule="/folder/images/*.png",
            rule_type=0,
        )
        assert_matches_type(CdnResourceRule, rule, path=["response"])

    @parametrize
    def test_method_replace_with_all_params(self, client: Gcore) -> None:
        rule = client.cdn.resources.rules.replace(
            rule_id=0,
            resource_id=0,
            rule="/folder/images/*.png",
            rule_type=0,
            active=True,
            name="My first rule",
            options={
                "allowed_http_methods": {
                    "enabled": True,
                    "value": ["GET", "POST"],
                },
                "bot_protection": {
                    "bot_challenge": {"enabled": True},
                    "enabled": True,
                },
                "brotli_compression": {
                    "enabled": True,
                    "value": ["text/html", "text/plain"],
                },
                "browser_cache_settings": {
                    "enabled": True,
                    "value": "3600s",
                },
                "cache_http_headers": {
                    "enabled": False,
                    "value": [
                        "vary",
                        "content-length",
                        "last-modified",
                        "connection",
                        "accept-ranges",
                        "content-type",
                        "content-encoding",
                        "etag",
                        "cache-control",
                        "expires",
                        "keep-alive",
                        "server",
                    ],
                },
                "cors": {
                    "enabled": True,
                    "value": ["domain.com", "domain2.com"],
                    "always": True,
                },
                "country_acl": {
                    "enabled": True,
                    "excepted_values": ["GB", "DE"],
                    "policy_type": "allow",
                },
                "disable_cache": {
                    "enabled": True,
                    "value": False,
                },
                "disable_proxy_force_ranges": {
                    "enabled": True,
                    "value": True,
                },
                "edge_cache_settings": {
                    "enabled": True,
                    "custom_values": {"100": "43200s"},
                    "default": "321669910225",
                    "value": "43200s",
                },
                "fastedge": {
                    "enabled": True,
                    "on_request_body": {
                        "app_id": "1001",
                        "enabled": True,
                        "execute_on_edge": True,
                        "execute_on_shield": False,
                        "interrupt_on_error": True,
                    },
                    "on_request_headers": {
                        "app_id": "1001",
                        "enabled": True,
                        "execute_on_edge": True,
                        "execute_on_shield": False,
                        "interrupt_on_error": True,
                    },
                    "on_response_body": {
                        "app_id": "1001",
                        "enabled": True,
                        "execute_on_edge": True,
                        "execute_on_shield": False,
                        "interrupt_on_error": True,
                    },
                    "on_response_headers": {
                        "app_id": "1001",
                        "enabled": True,
                        "execute_on_edge": True,
                        "execute_on_shield": False,
                        "interrupt_on_error": True,
                    },
                },
                "fetch_compressed": {
                    "enabled": True,
                    "value": False,
                },
                "follow_origin_redirect": {
                    "codes": [302, 308],
                    "enabled": True,
                },
                "force_return": {
                    "body": "http://example.com/redirect_address",
                    "code": 301,
                    "enabled": True,
                    "time_interval": {
                        "end_time": "20:00",
                        "start_time": "09:00",
                        "time_zone": "CET",
                    },
                },
                "forward_host_header": {
                    "enabled": False,
                    "value": False,
                },
                "gzip_on": {
                    "enabled": True,
                    "value": True,
                },
                "host_header": {
                    "enabled": True,
                    "value": "host.com",
                },
                "ignore_cookie": {
                    "enabled": True,
                    "value": True,
                },
                "ignore_query_string": {
                    "enabled": True,
                    "value": False,
                },
                "image_stack": {
                    "enabled": True,
                    "avif_enabled": True,
                    "png_lossless": True,
                    "quality": 80,
                    "webp_enabled": False,
                },
                "ip_address_acl": {
                    "enabled": True,
                    "excepted_values": ["192.168.1.100/32"],
                    "policy_type": "deny",
                },
                "limit_bandwidth": {
                    "enabled": True,
                    "limit_type": "static",
                    "buffer": 200,
                    "speed": 100,
                },
                "proxy_cache_key": {
                    "enabled": True,
                    "value": "$scheme$uri",
                },
                "proxy_cache_methods_set": {
                    "enabled": True,
                    "value": False,
                },
                "proxy_connect_timeout": {
                    "enabled": True,
                    "value": "4s",
                },
                "proxy_read_timeout": {
                    "enabled": True,
                    "value": "10s",
                },
                "query_params_blacklist": {
                    "enabled": True,
                    "value": ["some", "blacklisted", "query"],
                },
                "query_params_whitelist": {
                    "enabled": True,
                    "value": ["some", "whitelisted", "query"],
                },
                "query_string_forwarding": {
                    "enabled": True,
                    "forward_from_file_types": ["m3u8", "mpd"],
                    "forward_to_file_types": ["ts", "mp4"],
                    "forward_except_keys": ["debug_info"],
                    "forward_only_keys": ["auth_token", "session_id"],
                },
                "redirect_http_to_https": {
                    "enabled": True,
                    "value": True,
                },
                "redirect_https_to_http": {
                    "enabled": False,
                    "value": True,
                },
                "referrer_acl": {
                    "enabled": True,
                    "excepted_values": ["example.com", "*.example.net"],
                    "policy_type": "deny",
                },
                "request_limiter": {
                    "enabled": True,
                    "rate": 5,
                    "rate_unit": "r/s",
                },
                "response_headers_hiding_policy": {
                    "enabled": True,
                    "excepted": ["my-header"],
                    "mode": "hide",
                },
                "rewrite": {
                    "body": "/(.*) /additional_path/$1",
                    "enabled": True,
                    "flag": "break",
                },
                "secure_key": {
                    "enabled": True,
                    "key": "secretkey",
                    "type": 2,
                },
                "slice": {
                    "enabled": True,
                    "value": True,
                },
                "sni": {
                    "custom_hostname": "custom.example.com",
                    "enabled": True,
                    "sni_type": "custom",
                },
                "stale": {
                    "enabled": True,
                    "value": ["http_404", "http_500"],
                },
                "static_response_headers": {
                    "enabled": True,
                    "value": [
                        {
                            "name": "X-Example",
                            "value": ["Value_1"],
                            "always": True,
                        },
                        {
                            "name": "X-Example-Multiple",
                            "value": ["Value_1", "Value_2", "Value_3"],
                            "always": False,
                        },
                    ],
                },
                "static_headers": {
                    "enabled": True,
                    "value": {
                        "X-Example": "Value_1",
                        "X-Example-Multiple": ["Value_2", "Value_3"],
                    },
                },
                "static_request_headers": {
                    "enabled": True,
                    "value": {
                        "Header-One": "Value 1",
                        "Header-Two": "Value 2",
                    },
                },
                "user_agent_acl": {
                    "enabled": True,
                    "excepted_values": ["UserAgent Value", ""],
                    "policy_type": "allow",
                },
                "waap": {
                    "enabled": True,
                    "value": True,
                },
                "websockets": {
                    "enabled": True,
                    "value": True,
                },
            },
            origin_group=None,
            override_origin_protocol="HTTPS",
            weight=1,
        )
        assert_matches_type(CdnResourceRule, rule, path=["response"])

    @parametrize
    def test_raw_response_replace(self, client: Gcore) -> None:
        response = client.cdn.resources.rules.with_raw_response.replace(
            rule_id=0,
            resource_id=0,
            rule="/folder/images/*.png",
            rule_type=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(CdnResourceRule, rule, path=["response"])

    @parametrize
    def test_streaming_response_replace(self, client: Gcore) -> None:
        with client.cdn.resources.rules.with_streaming_response.replace(
            rule_id=0,
            resource_id=0,
            rule="/folder/images/*.png",
            rule_type=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(CdnResourceRule, rule, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRules:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGcore) -> None:
        rule = await async_client.cdn.resources.rules.create(
            resource_id=0,
            name="My first rule",
            rule="/folder/images/*.png",
            rule_type=0,
        )
        assert_matches_type(CdnResourceRule, rule, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGcore) -> None:
        rule = await async_client.cdn.resources.rules.create(
            resource_id=0,
            name="My first rule",
            rule="/folder/images/*.png",
            rule_type=0,
            active=True,
            options={
                "allowed_http_methods": {
                    "enabled": True,
                    "value": ["GET", "POST"],
                },
                "bot_protection": {
                    "bot_challenge": {"enabled": True},
                    "enabled": True,
                },
                "brotli_compression": {
                    "enabled": True,
                    "value": ["text/html", "text/plain"],
                },
                "browser_cache_settings": {
                    "enabled": True,
                    "value": "3600s",
                },
                "cache_http_headers": {
                    "enabled": False,
                    "value": [
                        "vary",
                        "content-length",
                        "last-modified",
                        "connection",
                        "accept-ranges",
                        "content-type",
                        "content-encoding",
                        "etag",
                        "cache-control",
                        "expires",
                        "keep-alive",
                        "server",
                    ],
                },
                "cors": {
                    "enabled": True,
                    "value": ["domain.com", "domain2.com"],
                    "always": True,
                },
                "country_acl": {
                    "enabled": True,
                    "excepted_values": ["GB", "DE"],
                    "policy_type": "allow",
                },
                "disable_cache": {
                    "enabled": True,
                    "value": False,
                },
                "disable_proxy_force_ranges": {
                    "enabled": True,
                    "value": True,
                },
                "edge_cache_settings": {
                    "enabled": True,
                    "custom_values": {"100": "43200s"},
                    "default": "321669910225",
                    "value": "43200s",
                },
                "fastedge": {
                    "enabled": True,
                    "on_request_body": {
                        "app_id": "1001",
                        "enabled": True,
                        "execute_on_edge": True,
                        "execute_on_shield": False,
                        "interrupt_on_error": True,
                    },
                    "on_request_headers": {
                        "app_id": "1001",
                        "enabled": True,
                        "execute_on_edge": True,
                        "execute_on_shield": False,
                        "interrupt_on_error": True,
                    },
                    "on_response_body": {
                        "app_id": "1001",
                        "enabled": True,
                        "execute_on_edge": True,
                        "execute_on_shield": False,
                        "interrupt_on_error": True,
                    },
                    "on_response_headers": {
                        "app_id": "1001",
                        "enabled": True,
                        "execute_on_edge": True,
                        "execute_on_shield": False,
                        "interrupt_on_error": True,
                    },
                },
                "fetch_compressed": {
                    "enabled": True,
                    "value": False,
                },
                "follow_origin_redirect": {
                    "codes": [302, 308],
                    "enabled": True,
                },
                "force_return": {
                    "body": "http://example.com/redirect_address",
                    "code": 301,
                    "enabled": True,
                    "time_interval": {
                        "end_time": "20:00",
                        "start_time": "09:00",
                        "time_zone": "CET",
                    },
                },
                "forward_host_header": {
                    "enabled": False,
                    "value": False,
                },
                "gzip_on": {
                    "enabled": True,
                    "value": True,
                },
                "host_header": {
                    "enabled": True,
                    "value": "host.com",
                },
                "ignore_cookie": {
                    "enabled": True,
                    "value": True,
                },
                "ignore_query_string": {
                    "enabled": True,
                    "value": False,
                },
                "image_stack": {
                    "enabled": True,
                    "avif_enabled": True,
                    "png_lossless": True,
                    "quality": 80,
                    "webp_enabled": False,
                },
                "ip_address_acl": {
                    "enabled": True,
                    "excepted_values": ["192.168.1.100/32"],
                    "policy_type": "deny",
                },
                "limit_bandwidth": {
                    "enabled": True,
                    "limit_type": "static",
                    "buffer": 200,
                    "speed": 100,
                },
                "proxy_cache_key": {
                    "enabled": True,
                    "value": "$scheme$uri",
                },
                "proxy_cache_methods_set": {
                    "enabled": True,
                    "value": False,
                },
                "proxy_connect_timeout": {
                    "enabled": True,
                    "value": "4s",
                },
                "proxy_read_timeout": {
                    "enabled": True,
                    "value": "10s",
                },
                "query_params_blacklist": {
                    "enabled": True,
                    "value": ["some", "blacklisted", "query"],
                },
                "query_params_whitelist": {
                    "enabled": True,
                    "value": ["some", "whitelisted", "query"],
                },
                "query_string_forwarding": {
                    "enabled": True,
                    "forward_from_file_types": ["m3u8", "mpd"],
                    "forward_to_file_types": ["ts", "mp4"],
                    "forward_except_keys": ["debug_info"],
                    "forward_only_keys": ["auth_token", "session_id"],
                },
                "redirect_http_to_https": {
                    "enabled": True,
                    "value": True,
                },
                "redirect_https_to_http": {
                    "enabled": False,
                    "value": True,
                },
                "referrer_acl": {
                    "enabled": True,
                    "excepted_values": ["example.com", "*.example.net"],
                    "policy_type": "deny",
                },
                "request_limiter": {
                    "enabled": True,
                    "rate": 5,
                    "rate_unit": "r/s",
                },
                "response_headers_hiding_policy": {
                    "enabled": True,
                    "excepted": ["my-header"],
                    "mode": "hide",
                },
                "rewrite": {
                    "body": "/(.*) /additional_path/$1",
                    "enabled": True,
                    "flag": "break",
                },
                "secure_key": {
                    "enabled": True,
                    "key": "secretkey",
                    "type": 2,
                },
                "slice": {
                    "enabled": True,
                    "value": True,
                },
                "sni": {
                    "custom_hostname": "custom.example.com",
                    "enabled": True,
                    "sni_type": "custom",
                },
                "stale": {
                    "enabled": True,
                    "value": ["http_404", "http_500"],
                },
                "static_response_headers": {
                    "enabled": True,
                    "value": [
                        {
                            "name": "X-Example",
                            "value": ["Value_1"],
                            "always": True,
                        },
                        {
                            "name": "X-Example-Multiple",
                            "value": ["Value_1", "Value_2", "Value_3"],
                            "always": False,
                        },
                    ],
                },
                "static_headers": {
                    "enabled": True,
                    "value": {
                        "X-Example": "Value_1",
                        "X-Example-Multiple": ["Value_2", "Value_3"],
                    },
                },
                "static_request_headers": {
                    "enabled": True,
                    "value": {
                        "Header-One": "Value 1",
                        "Header-Two": "Value 2",
                    },
                },
                "user_agent_acl": {
                    "enabled": True,
                    "excepted_values": ["UserAgent Value", ""],
                    "policy_type": "allow",
                },
                "waap": {
                    "enabled": True,
                    "value": True,
                },
                "websockets": {
                    "enabled": True,
                    "value": True,
                },
            },
            origin_group=None,
            override_origin_protocol="HTTPS",
            weight=1,
        )
        assert_matches_type(CdnResourceRule, rule, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.resources.rules.with_raw_response.create(
            resource_id=0,
            name="My first rule",
            rule="/folder/images/*.png",
            rule_type=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(CdnResourceRule, rule, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.resources.rules.with_streaming_response.create(
            resource_id=0,
            name="My first rule",
            rule="/folder/images/*.png",
            rule_type=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(CdnResourceRule, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGcore) -> None:
        rule = await async_client.cdn.resources.rules.update(
            rule_id=0,
            resource_id=0,
        )
        assert_matches_type(CdnResourceRule, rule, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGcore) -> None:
        rule = await async_client.cdn.resources.rules.update(
            rule_id=0,
            resource_id=0,
            active=True,
            name="My first rule",
            options={
                "allowed_http_methods": {
                    "enabled": True,
                    "value": ["GET", "POST"],
                },
                "bot_protection": {
                    "bot_challenge": {"enabled": True},
                    "enabled": True,
                },
                "brotli_compression": {
                    "enabled": True,
                    "value": ["text/html", "text/plain"],
                },
                "browser_cache_settings": {
                    "enabled": True,
                    "value": "3600s",
                },
                "cache_http_headers": {
                    "enabled": False,
                    "value": [
                        "vary",
                        "content-length",
                        "last-modified",
                        "connection",
                        "accept-ranges",
                        "content-type",
                        "content-encoding",
                        "etag",
                        "cache-control",
                        "expires",
                        "keep-alive",
                        "server",
                    ],
                },
                "cors": {
                    "enabled": True,
                    "value": ["domain.com", "domain2.com"],
                    "always": True,
                },
                "country_acl": {
                    "enabled": True,
                    "excepted_values": ["GB", "DE"],
                    "policy_type": "allow",
                },
                "disable_cache": {
                    "enabled": True,
                    "value": False,
                },
                "disable_proxy_force_ranges": {
                    "enabled": True,
                    "value": True,
                },
                "edge_cache_settings": {
                    "enabled": True,
                    "custom_values": {"100": "43200s"},
                    "default": "321669910225",
                    "value": "43200s",
                },
                "fastedge": {
                    "enabled": True,
                    "on_request_body": {
                        "app_id": "1001",
                        "enabled": True,
                        "execute_on_edge": True,
                        "execute_on_shield": False,
                        "interrupt_on_error": True,
                    },
                    "on_request_headers": {
                        "app_id": "1001",
                        "enabled": True,
                        "execute_on_edge": True,
                        "execute_on_shield": False,
                        "interrupt_on_error": True,
                    },
                    "on_response_body": {
                        "app_id": "1001",
                        "enabled": True,
                        "execute_on_edge": True,
                        "execute_on_shield": False,
                        "interrupt_on_error": True,
                    },
                    "on_response_headers": {
                        "app_id": "1001",
                        "enabled": True,
                        "execute_on_edge": True,
                        "execute_on_shield": False,
                        "interrupt_on_error": True,
                    },
                },
                "fetch_compressed": {
                    "enabled": True,
                    "value": False,
                },
                "follow_origin_redirect": {
                    "codes": [302, 308],
                    "enabled": True,
                },
                "force_return": {
                    "body": "http://example.com/redirect_address",
                    "code": 301,
                    "enabled": True,
                    "time_interval": {
                        "end_time": "20:00",
                        "start_time": "09:00",
                        "time_zone": "CET",
                    },
                },
                "forward_host_header": {
                    "enabled": False,
                    "value": False,
                },
                "gzip_on": {
                    "enabled": True,
                    "value": True,
                },
                "host_header": {
                    "enabled": True,
                    "value": "host.com",
                },
                "ignore_cookie": {
                    "enabled": True,
                    "value": True,
                },
                "ignore_query_string": {
                    "enabled": True,
                    "value": False,
                },
                "image_stack": {
                    "enabled": True,
                    "avif_enabled": True,
                    "png_lossless": True,
                    "quality": 80,
                    "webp_enabled": False,
                },
                "ip_address_acl": {
                    "enabled": True,
                    "excepted_values": ["192.168.1.100/32"],
                    "policy_type": "deny",
                },
                "limit_bandwidth": {
                    "enabled": True,
                    "limit_type": "static",
                    "buffer": 200,
                    "speed": 100,
                },
                "proxy_cache_key": {
                    "enabled": True,
                    "value": "$scheme$uri",
                },
                "proxy_cache_methods_set": {
                    "enabled": True,
                    "value": False,
                },
                "proxy_connect_timeout": {
                    "enabled": True,
                    "value": "4s",
                },
                "proxy_read_timeout": {
                    "enabled": True,
                    "value": "10s",
                },
                "query_params_blacklist": {
                    "enabled": True,
                    "value": ["some", "blacklisted", "query"],
                },
                "query_params_whitelist": {
                    "enabled": True,
                    "value": ["some", "whitelisted", "query"],
                },
                "query_string_forwarding": {
                    "enabled": True,
                    "forward_from_file_types": ["m3u8", "mpd"],
                    "forward_to_file_types": ["ts", "mp4"],
                    "forward_except_keys": ["debug_info"],
                    "forward_only_keys": ["auth_token", "session_id"],
                },
                "redirect_http_to_https": {
                    "enabled": True,
                    "value": True,
                },
                "redirect_https_to_http": {
                    "enabled": False,
                    "value": True,
                },
                "referrer_acl": {
                    "enabled": True,
                    "excepted_values": ["example.com", "*.example.net"],
                    "policy_type": "deny",
                },
                "request_limiter": {
                    "enabled": True,
                    "rate": 5,
                    "rate_unit": "r/s",
                },
                "response_headers_hiding_policy": {
                    "enabled": True,
                    "excepted": ["my-header"],
                    "mode": "hide",
                },
                "rewrite": {
                    "body": "/(.*) /additional_path/$1",
                    "enabled": True,
                    "flag": "break",
                },
                "secure_key": {
                    "enabled": True,
                    "key": "secretkey",
                    "type": 2,
                },
                "slice": {
                    "enabled": True,
                    "value": True,
                },
                "sni": {
                    "custom_hostname": "custom.example.com",
                    "enabled": True,
                    "sni_type": "custom",
                },
                "stale": {
                    "enabled": True,
                    "value": ["http_404", "http_500"],
                },
                "static_response_headers": {
                    "enabled": True,
                    "value": [
                        {
                            "name": "X-Example",
                            "value": ["Value_1"],
                            "always": True,
                        },
                        {
                            "name": "X-Example-Multiple",
                            "value": ["Value_1", "Value_2", "Value_3"],
                            "always": False,
                        },
                    ],
                },
                "static_headers": {
                    "enabled": True,
                    "value": {
                        "X-Example": "Value_1",
                        "X-Example-Multiple": ["Value_2", "Value_3"],
                    },
                },
                "static_request_headers": {
                    "enabled": True,
                    "value": {
                        "Header-One": "Value 1",
                        "Header-Two": "Value 2",
                    },
                },
                "user_agent_acl": {
                    "enabled": True,
                    "excepted_values": ["UserAgent Value", ""],
                    "policy_type": "allow",
                },
                "waap": {
                    "enabled": True,
                    "value": True,
                },
                "websockets": {
                    "enabled": True,
                    "value": True,
                },
            },
            origin_group=None,
            override_origin_protocol="HTTPS",
            rule="/folder/images/*.png",
            rule_type=0,
            weight=1,
        )
        assert_matches_type(CdnResourceRule, rule, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.resources.rules.with_raw_response.update(
            rule_id=0,
            resource_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(CdnResourceRule, rule, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.resources.rules.with_streaming_response.update(
            rule_id=0,
            resource_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(CdnResourceRule, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGcore) -> None:
        rule = await async_client.cdn.resources.rules.list(
            0,
        )
        assert_matches_type(RuleListResponse, rule, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.resources.rules.with_raw_response.list(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleListResponse, rule, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.resources.rules.with_streaming_response.list(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleListResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGcore) -> None:
        rule = await async_client.cdn.resources.rules.delete(
            rule_id=0,
            resource_id=0,
        )
        assert rule is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.resources.rules.with_raw_response.delete(
            rule_id=0,
            resource_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert rule is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.resources.rules.with_streaming_response.delete(
            rule_id=0,
            resource_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert rule is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncGcore) -> None:
        rule = await async_client.cdn.resources.rules.get(
            rule_id=0,
            resource_id=0,
        )
        assert_matches_type(CdnResourceRule, rule, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.resources.rules.with_raw_response.get(
            rule_id=0,
            resource_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(CdnResourceRule, rule, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.resources.rules.with_streaming_response.get(
            rule_id=0,
            resource_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(CdnResourceRule, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_replace(self, async_client: AsyncGcore) -> None:
        rule = await async_client.cdn.resources.rules.replace(
            rule_id=0,
            resource_id=0,
            rule="/folder/images/*.png",
            rule_type=0,
        )
        assert_matches_type(CdnResourceRule, rule, path=["response"])

    @parametrize
    async def test_method_replace_with_all_params(self, async_client: AsyncGcore) -> None:
        rule = await async_client.cdn.resources.rules.replace(
            rule_id=0,
            resource_id=0,
            rule="/folder/images/*.png",
            rule_type=0,
            active=True,
            name="My first rule",
            options={
                "allowed_http_methods": {
                    "enabled": True,
                    "value": ["GET", "POST"],
                },
                "bot_protection": {
                    "bot_challenge": {"enabled": True},
                    "enabled": True,
                },
                "brotli_compression": {
                    "enabled": True,
                    "value": ["text/html", "text/plain"],
                },
                "browser_cache_settings": {
                    "enabled": True,
                    "value": "3600s",
                },
                "cache_http_headers": {
                    "enabled": False,
                    "value": [
                        "vary",
                        "content-length",
                        "last-modified",
                        "connection",
                        "accept-ranges",
                        "content-type",
                        "content-encoding",
                        "etag",
                        "cache-control",
                        "expires",
                        "keep-alive",
                        "server",
                    ],
                },
                "cors": {
                    "enabled": True,
                    "value": ["domain.com", "domain2.com"],
                    "always": True,
                },
                "country_acl": {
                    "enabled": True,
                    "excepted_values": ["GB", "DE"],
                    "policy_type": "allow",
                },
                "disable_cache": {
                    "enabled": True,
                    "value": False,
                },
                "disable_proxy_force_ranges": {
                    "enabled": True,
                    "value": True,
                },
                "edge_cache_settings": {
                    "enabled": True,
                    "custom_values": {"100": "43200s"},
                    "default": "321669910225",
                    "value": "43200s",
                },
                "fastedge": {
                    "enabled": True,
                    "on_request_body": {
                        "app_id": "1001",
                        "enabled": True,
                        "execute_on_edge": True,
                        "execute_on_shield": False,
                        "interrupt_on_error": True,
                    },
                    "on_request_headers": {
                        "app_id": "1001",
                        "enabled": True,
                        "execute_on_edge": True,
                        "execute_on_shield": False,
                        "interrupt_on_error": True,
                    },
                    "on_response_body": {
                        "app_id": "1001",
                        "enabled": True,
                        "execute_on_edge": True,
                        "execute_on_shield": False,
                        "interrupt_on_error": True,
                    },
                    "on_response_headers": {
                        "app_id": "1001",
                        "enabled": True,
                        "execute_on_edge": True,
                        "execute_on_shield": False,
                        "interrupt_on_error": True,
                    },
                },
                "fetch_compressed": {
                    "enabled": True,
                    "value": False,
                },
                "follow_origin_redirect": {
                    "codes": [302, 308],
                    "enabled": True,
                },
                "force_return": {
                    "body": "http://example.com/redirect_address",
                    "code": 301,
                    "enabled": True,
                    "time_interval": {
                        "end_time": "20:00",
                        "start_time": "09:00",
                        "time_zone": "CET",
                    },
                },
                "forward_host_header": {
                    "enabled": False,
                    "value": False,
                },
                "gzip_on": {
                    "enabled": True,
                    "value": True,
                },
                "host_header": {
                    "enabled": True,
                    "value": "host.com",
                },
                "ignore_cookie": {
                    "enabled": True,
                    "value": True,
                },
                "ignore_query_string": {
                    "enabled": True,
                    "value": False,
                },
                "image_stack": {
                    "enabled": True,
                    "avif_enabled": True,
                    "png_lossless": True,
                    "quality": 80,
                    "webp_enabled": False,
                },
                "ip_address_acl": {
                    "enabled": True,
                    "excepted_values": ["192.168.1.100/32"],
                    "policy_type": "deny",
                },
                "limit_bandwidth": {
                    "enabled": True,
                    "limit_type": "static",
                    "buffer": 200,
                    "speed": 100,
                },
                "proxy_cache_key": {
                    "enabled": True,
                    "value": "$scheme$uri",
                },
                "proxy_cache_methods_set": {
                    "enabled": True,
                    "value": False,
                },
                "proxy_connect_timeout": {
                    "enabled": True,
                    "value": "4s",
                },
                "proxy_read_timeout": {
                    "enabled": True,
                    "value": "10s",
                },
                "query_params_blacklist": {
                    "enabled": True,
                    "value": ["some", "blacklisted", "query"],
                },
                "query_params_whitelist": {
                    "enabled": True,
                    "value": ["some", "whitelisted", "query"],
                },
                "query_string_forwarding": {
                    "enabled": True,
                    "forward_from_file_types": ["m3u8", "mpd"],
                    "forward_to_file_types": ["ts", "mp4"],
                    "forward_except_keys": ["debug_info"],
                    "forward_only_keys": ["auth_token", "session_id"],
                },
                "redirect_http_to_https": {
                    "enabled": True,
                    "value": True,
                },
                "redirect_https_to_http": {
                    "enabled": False,
                    "value": True,
                },
                "referrer_acl": {
                    "enabled": True,
                    "excepted_values": ["example.com", "*.example.net"],
                    "policy_type": "deny",
                },
                "request_limiter": {
                    "enabled": True,
                    "rate": 5,
                    "rate_unit": "r/s",
                },
                "response_headers_hiding_policy": {
                    "enabled": True,
                    "excepted": ["my-header"],
                    "mode": "hide",
                },
                "rewrite": {
                    "body": "/(.*) /additional_path/$1",
                    "enabled": True,
                    "flag": "break",
                },
                "secure_key": {
                    "enabled": True,
                    "key": "secretkey",
                    "type": 2,
                },
                "slice": {
                    "enabled": True,
                    "value": True,
                },
                "sni": {
                    "custom_hostname": "custom.example.com",
                    "enabled": True,
                    "sni_type": "custom",
                },
                "stale": {
                    "enabled": True,
                    "value": ["http_404", "http_500"],
                },
                "static_response_headers": {
                    "enabled": True,
                    "value": [
                        {
                            "name": "X-Example",
                            "value": ["Value_1"],
                            "always": True,
                        },
                        {
                            "name": "X-Example-Multiple",
                            "value": ["Value_1", "Value_2", "Value_3"],
                            "always": False,
                        },
                    ],
                },
                "static_headers": {
                    "enabled": True,
                    "value": {
                        "X-Example": "Value_1",
                        "X-Example-Multiple": ["Value_2", "Value_3"],
                    },
                },
                "static_request_headers": {
                    "enabled": True,
                    "value": {
                        "Header-One": "Value 1",
                        "Header-Two": "Value 2",
                    },
                },
                "user_agent_acl": {
                    "enabled": True,
                    "excepted_values": ["UserAgent Value", ""],
                    "policy_type": "allow",
                },
                "waap": {
                    "enabled": True,
                    "value": True,
                },
                "websockets": {
                    "enabled": True,
                    "value": True,
                },
            },
            origin_group=None,
            override_origin_protocol="HTTPS",
            weight=1,
        )
        assert_matches_type(CdnResourceRule, rule, path=["response"])

    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncGcore) -> None:
        response = await async_client.cdn.resources.rules.with_raw_response.replace(
            rule_id=0,
            resource_id=0,
            rule="/folder/images/*.png",
            rule_type=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(CdnResourceRule, rule, path=["response"])

    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncGcore) -> None:
        async with async_client.cdn.resources.rules.with_streaming_response.replace(
            rule_id=0,
            resource_id=0,
            rule="/folder/images/*.png",
            rule_type=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(CdnResourceRule, rule, path=["response"])

        assert cast(Any, response.is_closed) is True
