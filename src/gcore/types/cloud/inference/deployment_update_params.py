# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from ..laas_index_retention_policy_param import LaasIndexRetentionPolicyParam

__all__ = [
    "DeploymentUpdateParams",
    "Container",
    "ContainerScale",
    "ContainerScaleTriggers",
    "ContainerScaleTriggersCPU",
    "ContainerScaleTriggersGPUMemory",
    "ContainerScaleTriggersGPUUtilization",
    "ContainerScaleTriggersHTTP",
    "ContainerScaleTriggersMemory",
    "ContainerScaleTriggersSqs",
    "IngressOpts",
    "Logging",
    "Probes",
    "ProbesLivenessProbe",
    "ProbesLivenessProbeProbe",
    "ProbesLivenessProbeProbeExec",
    "ProbesLivenessProbeProbeHTTPGet",
    "ProbesLivenessProbeProbeTcpSocket",
    "ProbesReadinessProbe",
    "ProbesReadinessProbeProbe",
    "ProbesReadinessProbeProbeExec",
    "ProbesReadinessProbeProbeHTTPGet",
    "ProbesReadinessProbeProbeTcpSocket",
    "ProbesStartupProbe",
    "ProbesStartupProbeProbe",
    "ProbesStartupProbeProbeExec",
    "ProbesStartupProbeProbeHTTPGet",
    "ProbesStartupProbeProbeTcpSocket",
]


class DeploymentUpdateParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    api_keys: Optional[List[str]]
    """List of API keys for the inference instance.

    Multiple keys can be attached to one deployment.If `auth_enabled` and `api_keys`
    are both specified, a ValidationError will be raised.If `[]` is provided, the
    API keys will be removed and auth will be disabled on the deployment.
    """

    auth_enabled: bool
    """Set to `true` to enable API key authentication for the inference instance.

    `"Authorization": "Bearer ****\\**"` or `"X-Api-Key": "****\\**"` header is required
    for the requests to the instance if enabled. This field is deprecated and will
    be removed in the future. Use `api_keys` field instead.If `auth_enabled` and
    `api_keys` are both specified, a ValidationError will be raised.
    """

    command: Optional[List[str]]
    """Command to be executed when running a container from an image."""

    containers: Optional[Iterable[Container]]
    """List of containers for the inference instance."""

    credentials_name: Optional[str]
    """Registry credentials name"""

    description: Optional[str]
    """Inference instance description."""

    envs: Optional[Dict[str, str]]
    """Environment variables for the inference instance."""

    flavor_name: str
    """Flavor name for the inference instance."""

    image: Optional[str]
    """Docker image for the inference instance.

    This field should contain the image name and tag in the format 'name:tag', e.g.,
    'nginx:latest'. It defaults to Docker Hub as the image registry, but any
    accessible Docker image URL can be specified.
    """

    ingress_opts: Optional[IngressOpts]
    """Ingress options for the inference instance"""

    listening_port: Optional[int]
    """Listening port for the inference instance."""

    logging: Optional[Logging]
    """Logging configuration for the inference instance"""

    probes: Optional[Probes]
    """Probes configured for all containers of the inference instance."""

    api_timeout: Annotated[Optional[int], PropertyInfo(alias="timeout")]
    """
    Specifies the duration in seconds without any requests after which the
    containers will be downscaled to their minimum scale value as defined by
    `scale.min`. If set, this helps in optimizing resource usage by reducing the
    number of container instances during periods of inactivity. The default value
    when the parameter is not set is 120.
    """


class ContainerScaleTriggersCPU(TypedDict, total=False):
    threshold: Required[int]
    """Threshold value for the trigger in percentage"""


class ContainerScaleTriggersGPUMemory(TypedDict, total=False):
    threshold: Required[int]
    """Threshold value for the trigger in percentage"""


class ContainerScaleTriggersGPUUtilization(TypedDict, total=False):
    threshold: Required[int]
    """Threshold value for the trigger in percentage"""


class ContainerScaleTriggersHTTP(TypedDict, total=False):
    rate: Required[int]
    """Request count per 'window' seconds for the http trigger"""

    window: Required[int]
    """Time window for rate calculation in seconds"""


class ContainerScaleTriggersMemory(TypedDict, total=False):
    threshold: Required[int]
    """Threshold value for the trigger in percentage"""


class ContainerScaleTriggersSqs(TypedDict, total=False):
    activation_queue_length: Required[int]
    """Number of messages for activation"""

    aws_region: Required[str]
    """AWS region"""

    queue_length: Required[int]
    """Number of messages for one replica"""

    queue_url: Required[str]
    """SQS queue URL"""

    secret_name: Required[str]
    """Auth secret name"""

    aws_endpoint: Optional[str]
    """Custom AWS endpoint"""

    scale_on_delayed: bool
    """Scale on delayed messages"""

    scale_on_flight: bool
    """Scale on in-flight messages"""


class ContainerScaleTriggers(TypedDict, total=False):
    cpu: Optional[ContainerScaleTriggersCPU]
    """CPU trigger configuration"""

    gpu_memory: Optional[ContainerScaleTriggersGPUMemory]
    """GPU memory trigger configuration.

    Calculated by `DCGM_FI_DEV_MEM_COPY_UTIL` metric
    """

    gpu_utilization: Optional[ContainerScaleTriggersGPUUtilization]
    """GPU utilization trigger configuration.

    Calculated by `DCGM_FI_DEV_GPU_UTIL` metric
    """

    http: Optional[ContainerScaleTriggersHTTP]
    """HTTP trigger configuration"""

    memory: Optional[ContainerScaleTriggersMemory]
    """Memory trigger configuration"""

    sqs: Optional[ContainerScaleTriggersSqs]
    """SQS trigger configuration"""


class ContainerScale(TypedDict, total=False):
    max: Required[int]
    """Maximum scale for the container"""

    min: Required[int]
    """Minimum scale for the container"""

    cooldown_period: int
    """Cooldown period between scaling actions in seconds"""

    polling_interval: int
    """Polling interval for scaling triggers in seconds"""

    triggers: ContainerScaleTriggers
    """Triggers for scaling actions"""


class Container(TypedDict, total=False):
    region_id: Required[Optional[int]]
    """Region id for the container"""

    scale: Required[Optional[ContainerScale]]
    """Scale for the container"""


class IngressOpts(TypedDict, total=False):
    disable_response_buffering: bool
    """Disable response buffering if true.

    A client usually has a much slower connection and can not consume the response
    data as fast as it is produced by an upstream application. Ingress tries to
    buffer the whole response in order to release the upstream application as soon
    as possible.By default, the response buffering is enabled.
    """


class Logging(TypedDict, total=False):
    destination_region_id: Optional[int]
    """ID of the region in which the logs will be stored"""

    enabled: bool
    """Enable or disable log streaming"""

    retention_policy: Optional[LaasIndexRetentionPolicyParam]
    """Logs retention policy"""

    topic_name: Optional[str]
    """The topic name to stream logs to"""


class ProbesLivenessProbeProbeExec(TypedDict, total=False):
    command: List[str]
    """Command to be executed inside the running container."""


class ProbesLivenessProbeProbeHTTPGet(TypedDict, total=False):
    headers: Dict[str, str]
    """HTTP headers to be sent with the request."""

    host: str
    """Host name to send HTTP request to."""

    path: str
    """The endpoint to send the HTTP request to."""

    port: int
    """Port number the probe should connect to."""

    schema: str
    """Schema to use for the HTTP request."""


class ProbesLivenessProbeProbeTcpSocket(TypedDict, total=False):
    port: int
    """Port number to check if it's open."""


class ProbesLivenessProbeProbe(TypedDict, total=False):
    exec: Optional[ProbesLivenessProbeProbeExec]
    """Exec probe configuration"""

    failure_threshold: int
    """The number of consecutive probe failures that mark the container as unhealthy."""

    http_get: Optional[ProbesLivenessProbeProbeHTTPGet]
    """HTTP GET probe configuration"""

    initial_delay_seconds: int
    """The initial delay before starting the first probe."""

    period_seconds: int
    """How often (in seconds) to perform the probe."""

    success_threshold: int
    """The number of consecutive successful probes that mark the container as healthy."""

    tcp_socket: Optional[ProbesLivenessProbeProbeTcpSocket]
    """TCP socket probe configuration"""

    timeout_seconds: int
    """The timeout for each probe."""


class ProbesLivenessProbe(TypedDict, total=False):
    enabled: bool
    """Whether the probe is enabled or not."""

    probe: ProbesLivenessProbeProbe
    """Probe configuration (exec, `http_get` or `tcp_socket`)"""


class ProbesReadinessProbeProbeExec(TypedDict, total=False):
    command: List[str]
    """Command to be executed inside the running container."""


class ProbesReadinessProbeProbeHTTPGet(TypedDict, total=False):
    headers: Dict[str, str]
    """HTTP headers to be sent with the request."""

    host: str
    """Host name to send HTTP request to."""

    path: str
    """The endpoint to send the HTTP request to."""

    port: int
    """Port number the probe should connect to."""

    schema: str
    """Schema to use for the HTTP request."""


class ProbesReadinessProbeProbeTcpSocket(TypedDict, total=False):
    port: int
    """Port number to check if it's open."""


class ProbesReadinessProbeProbe(TypedDict, total=False):
    exec: Optional[ProbesReadinessProbeProbeExec]
    """Exec probe configuration"""

    failure_threshold: int
    """The number of consecutive probe failures that mark the container as unhealthy."""

    http_get: Optional[ProbesReadinessProbeProbeHTTPGet]
    """HTTP GET probe configuration"""

    initial_delay_seconds: int
    """The initial delay before starting the first probe."""

    period_seconds: int
    """How often (in seconds) to perform the probe."""

    success_threshold: int
    """The number of consecutive successful probes that mark the container as healthy."""

    tcp_socket: Optional[ProbesReadinessProbeProbeTcpSocket]
    """TCP socket probe configuration"""

    timeout_seconds: int
    """The timeout for each probe."""


class ProbesReadinessProbe(TypedDict, total=False):
    enabled: bool
    """Whether the probe is enabled or not."""

    probe: ProbesReadinessProbeProbe
    """Probe configuration (exec, `http_get` or `tcp_socket`)"""


class ProbesStartupProbeProbeExec(TypedDict, total=False):
    command: List[str]
    """Command to be executed inside the running container."""


class ProbesStartupProbeProbeHTTPGet(TypedDict, total=False):
    headers: Dict[str, str]
    """HTTP headers to be sent with the request."""

    host: str
    """Host name to send HTTP request to."""

    path: str
    """The endpoint to send the HTTP request to."""

    port: int
    """Port number the probe should connect to."""

    schema: str
    """Schema to use for the HTTP request."""


class ProbesStartupProbeProbeTcpSocket(TypedDict, total=False):
    port: int
    """Port number to check if it's open."""


class ProbesStartupProbeProbe(TypedDict, total=False):
    exec: Optional[ProbesStartupProbeProbeExec]
    """Exec probe configuration"""

    failure_threshold: int
    """The number of consecutive probe failures that mark the container as unhealthy."""

    http_get: Optional[ProbesStartupProbeProbeHTTPGet]
    """HTTP GET probe configuration"""

    initial_delay_seconds: int
    """The initial delay before starting the first probe."""

    period_seconds: int
    """How often (in seconds) to perform the probe."""

    success_threshold: int
    """The number of consecutive successful probes that mark the container as healthy."""

    tcp_socket: Optional[ProbesStartupProbeProbeTcpSocket]
    """TCP socket probe configuration"""

    timeout_seconds: int
    """The timeout for each probe."""


class ProbesStartupProbe(TypedDict, total=False):
    enabled: bool
    """Whether the probe is enabled or not."""

    probe: ProbesStartupProbeProbe
    """Probe configuration (exec, `http_get` or `tcp_socket`)"""


class Probes(TypedDict, total=False):
    liveness_probe: Optional[ProbesLivenessProbe]
    """Liveness probe configuration"""

    readiness_probe: Optional[ProbesReadinessProbe]
    """Readiness probe configuration"""

    startup_probe: Optional[ProbesStartupProbe]
    """Startup probe configuration"""
