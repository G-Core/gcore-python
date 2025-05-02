# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .container_probe_exec_create_param import ContainerProbeExecCreateParam
from .container_probe_http_get_create_param import ContainerProbeHTTPGetCreateParam
from .container_probe_tcp_socket_create_param import ContainerProbeTcpSocketCreateParam

__all__ = ["ContainerProbeCreateParam"]


class ContainerProbeCreateParam(TypedDict, total=False):
    exec: Optional[ContainerProbeExecCreateParam]
    """
    '#/components/schemas/ContainerProbeSerializerV2/properties/exec/anyOf/0'
    "$.components.schemas.ContainerProbeSerializerV2.properties.exec.anyOf[0]"
    """

    failure_threshold: int
    """
    '#/components/schemas/ContainerProbeSerializerV2/properties/failure_threshold'
    "$.components.schemas.ContainerProbeSerializerV2.properties.failure_threshold"
    """

    http_get: Optional[ContainerProbeHTTPGetCreateParam]
    """
    '#/components/schemas/ContainerProbeSerializerV2/properties/http_get/anyOf/0'
    "$.components.schemas.ContainerProbeSerializerV2.properties.http_get.anyOf[0]"
    """

    initial_delay_seconds: int
    """
    '#/components/schemas/ContainerProbeSerializerV2/properties/initial_delay_seconds'
    "$.components.schemas.ContainerProbeSerializerV2.properties.initial_delay_seconds"
    """

    period_seconds: int
    """
    '#/components/schemas/ContainerProbeSerializerV2/properties/period_seconds'
    "$.components.schemas.ContainerProbeSerializerV2.properties.period_seconds"
    """

    success_threshold: int
    """
    '#/components/schemas/ContainerProbeSerializerV2/properties/success_threshold'
    "$.components.schemas.ContainerProbeSerializerV2.properties.success_threshold"
    """

    tcp_socket: Optional[ContainerProbeTcpSocketCreateParam]
    """
    '#/components/schemas/ContainerProbeSerializerV2/properties/tcp_socket/anyOf/0'
    "$.components.schemas.ContainerProbeSerializerV2.properties.tcp_socket.anyOf[0]"
    """

    timeout_seconds: int
    """
    '#/components/schemas/ContainerProbeSerializerV2/properties/timeout_seconds'
    "$.components.schemas.ContainerProbeSerializerV2.properties.timeout_seconds"
    """
