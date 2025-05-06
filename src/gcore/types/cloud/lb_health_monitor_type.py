# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["LbHealthMonitorType"]

LbHealthMonitorType: TypeAlias = Literal["HTTP", "HTTPS", "K8S", "PING", "TCP", "TLS-HELLO", "UDP-CONNECT"]
