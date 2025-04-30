# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .container_probe_exec import ContainerProbeExec
from .container_probe_http_get import ContainerProbeHTTPGet
from .container_probe_tcp_socket import ContainerProbeTcpSocket

__all__ = ["ContainerProbe"]


class ContainerProbe(BaseModel):
    exec: Optional[ContainerProbeExec] = None
    """
    '#/components/schemas/ContainerProbeOutSerializerV2/properties/exec/anyOf/0'
    "$.components.schemas.ContainerProbeOutSerializerV2.properties.exec.anyOf[0]"
    """

    failure_threshold: int
    """
    '#/components/schemas/ContainerProbeOutSerializerV2/properties/failure_threshold'
    "$.components.schemas.ContainerProbeOutSerializerV2.properties.failure_threshold"
    """

    http_get: Optional[ContainerProbeHTTPGet] = None
    """
    '#/components/schemas/ContainerProbeOutSerializerV2/properties/http_get/anyOf/0'
    "$.components.schemas.ContainerProbeOutSerializerV2.properties.http_get.anyOf[0]"
    """

    initial_delay_seconds: int
    """
    '#/components/schemas/ContainerProbeOutSerializerV2/properties/initial_delay_seconds'
    "$.components.schemas.ContainerProbeOutSerializerV2.properties.initial_delay_seconds"
    """

    period_seconds: int
    """
    '#/components/schemas/ContainerProbeOutSerializerV2/properties/period_seconds'
    "$.components.schemas.ContainerProbeOutSerializerV2.properties.period_seconds"
    """

    success_threshold: int
    """
    '#/components/schemas/ContainerProbeOutSerializerV2/properties/success_threshold'
    "$.components.schemas.ContainerProbeOutSerializerV2.properties.success_threshold"
    """

    tcp_socket: Optional[ContainerProbeTcpSocket] = None
    """
    '#/components/schemas/ContainerProbeOutSerializerV2/properties/tcp_socket/anyOf/0'
    "$.components.schemas.ContainerProbeOutSerializerV2.properties.tcp_socket.anyOf[0]"
    """

    timeout_seconds: int
    """
    '#/components/schemas/ContainerProbeOutSerializerV2/properties/timeout_seconds'
    "$.components.schemas.ContainerProbeOutSerializerV2.properties.timeout_seconds"
    """
