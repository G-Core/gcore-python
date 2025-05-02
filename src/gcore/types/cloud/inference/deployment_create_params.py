# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from ..ingress_opts_param import IngressOptsParam
from ..laas_index_retention_policy_param import LaasIndexRetentionPolicyParam
from ..container_probe_config_create_param import ContainerProbeConfigCreateParam

__all__ = [
    "DeploymentCreateParams",
    "Container",
    "ContainerScale",
    "ContainerScaleTriggers",
    "ContainerScaleTriggersCPU",
    "ContainerScaleTriggersGPUMemory",
    "ContainerScaleTriggersGPUUtilization",
    "ContainerScaleTriggersHTTP",
    "ContainerScaleTriggersMemory",
    "ContainerScaleTriggersSqs",
    "Logging",
    "Probes",
]


class DeploymentCreateParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    containers: Required[Iterable[Container]]
    """List of containers for the inference instance."""

    flavor_name: Required[str]
    """Flavor name for the inference instance."""

    image: Required[str]
    """Docker image for the inference instance.

    This field should contain the image name and tag in the format 'name:tag', e.g.,
    'nginx:latest'. It defaults to Docker Hub as the image registry, but any
    accessible Docker image URL can be specified.
    """

    listening_port: Required[int]
    """Listening port for the inference instance."""

    name: Required[str]
    """Inference instance name."""

    auth_enabled: bool
    """Set to `true` to enable API key authentication for the inference instance.

    `"Authorization": "Bearer *****"` or `"X-Api-Key": "*****"` header is required
    for the requests to the instance if enabled
    """

    command: Optional[List[str]]
    """Command to be executed when running a container from an image."""

    credentials_name: Optional[str]
    """Registry credentials name"""

    description: Optional[str]
    """Inference instance description."""

    envs: Dict[str, str]
    """Environment variables for the inference instance."""

    ingress_opts: Optional[IngressOptsParam]
    """Ingress options for the inference instance"""

    logging: Optional[Logging]
    """Logging configuration for the inference instance"""

    probes: Optional[Probes]
    """Probes configured for all containers of the inference instance.

    If probes are not provided, and the image_name is from a the Model Catalog
    registry, the default probes will be used.
    """

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

    Calculated by DCGM_FI_DEV_MEM_COPY_UTIL metric
    """

    gpu_utilization: Optional[ContainerScaleTriggersGPUUtilization]
    """GPU utilization trigger configuration.

    Calculated by DCGM_FI_DEV_GPU_UTIL metric
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

    cooldown_period: Optional[int]
    """Cooldown period between scaling actions in seconds"""

    polling_interval: Optional[int]
    """Polling interval for scaling triggers in seconds"""

    triggers: ContainerScaleTriggers
    """Triggers for scaling actions"""


class Container(TypedDict, total=False):
    region_id: Required[int]
    """Region id for the container"""

    scale: Required[ContainerScale]
    """Scale for the container"""


class Logging(TypedDict, total=False):
    destination_region_id: Optional[int]
    """ID of the region in which the logs will be stored"""

    enabled: bool
    """Enable or disable log streaming"""

    retention_policy: Optional[LaasIndexRetentionPolicyParam]
    """Logs retention policy"""

    topic_name: Optional[str]
    """The topic name to stream logs to"""


class Probes(TypedDict, total=False):
    liveness_probe: Optional[ContainerProbeConfigCreateParam]
    """Liveness probe configuration"""

    readiness_probe: Optional[ContainerProbeConfigCreateParam]
    """Readiness probe configuration"""

    startup_probe: Optional[ContainerProbeConfigCreateParam]
    """Startup probe configuration"""
