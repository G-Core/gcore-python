# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["WaapTrafficType"]

WaapTrafficType: TypeAlias = Literal[
    "policy_allowed",
    "policy_blocked",
    "custom_rule_allowed",
    "custom_blocked",
    "legit_requests",
    "sanctioned",
    "dynamic",
    "api",
    "static",
    "ajax",
    "redirects",
    "monitor",
    "err_40x",
    "err_50x",
    "passed_to_origin",
    "timeout",
    "other",
    "ddos",
    "legit",
    "monitored",
]
