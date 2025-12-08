# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ..logging import Logging
from ...._models import BaseModel
from .probe_config import ProbeConfig

__all__ = [
    "InferenceDeployment",
    "Container",
    "ContainerDeployStatus",
    "ContainerScale",
    "ContainerScaleTriggers",
    "ContainerScaleTriggersCPU",
    "ContainerScaleTriggersGPUMemory",
    "ContainerScaleTriggersGPUUtilization",
    "ContainerScaleTriggersHTTP",
    "ContainerScaleTriggersMemory",
    "ContainerScaleTriggersSqs",
    "IngressOpts",
    "ObjectReference",
    "Probes",
]


class ContainerDeployStatus(BaseModel):
    """Status of the containers deployment"""

    ready: int
    """Number of ready instances"""

    total: int
    """Total number of instances"""


class ContainerScaleTriggersCPU(BaseModel):
    """CPU trigger configuration"""

    threshold: int
    """Threshold value for the trigger in percentage"""


class ContainerScaleTriggersGPUMemory(BaseModel):
    """GPU memory trigger configuration.

    Calculated by `DCGM_FI_DEV_MEM_COPY_UTIL` metric
    """

    threshold: int
    """Threshold value for the trigger in percentage"""


class ContainerScaleTriggersGPUUtilization(BaseModel):
    """GPU utilization trigger configuration.

    Calculated by `DCGM_FI_DEV_GPU_UTIL` metric
    """

    threshold: int
    """Threshold value for the trigger in percentage"""


class ContainerScaleTriggersHTTP(BaseModel):
    """HTTP trigger configuration"""

    rate: int
    """Request count per 'window' seconds for the http trigger"""

    window: int
    """Time window for rate calculation in seconds"""


class ContainerScaleTriggersMemory(BaseModel):
    """Memory trigger configuration"""

    threshold: int
    """Threshold value for the trigger in percentage"""


class ContainerScaleTriggersSqs(BaseModel):
    """SQS trigger configuration"""

    activation_queue_length: int
    """Number of messages for activation"""

    aws_endpoint: Optional[str] = None
    """Custom AWS endpoint"""

    aws_region: str
    """AWS region"""

    queue_length: int
    """Number of messages for one replica"""

    queue_url: str
    """SQS queue URL"""

    scale_on_delayed: bool
    """Scale on delayed messages"""

    scale_on_flight: bool
    """Scale on in-flight messages"""

    secret_name: str
    """Auth secret name"""


class ContainerScaleTriggers(BaseModel):
    """Triggers for scaling actions"""

    cpu: Optional[ContainerScaleTriggersCPU] = None
    """CPU trigger configuration"""

    gpu_memory: Optional[ContainerScaleTriggersGPUMemory] = None
    """GPU memory trigger configuration.

    Calculated by `DCGM_FI_DEV_MEM_COPY_UTIL` metric
    """

    gpu_utilization: Optional[ContainerScaleTriggersGPUUtilization] = None
    """GPU utilization trigger configuration.

    Calculated by `DCGM_FI_DEV_GPU_UTIL` metric
    """

    http: Optional[ContainerScaleTriggersHTTP] = None
    """HTTP trigger configuration"""

    memory: Optional[ContainerScaleTriggersMemory] = None
    """Memory trigger configuration"""

    sqs: Optional[ContainerScaleTriggersSqs] = None
    """SQS trigger configuration"""


class ContainerScale(BaseModel):
    """Scale for the container"""

    cooldown_period: Optional[int] = None
    """Cooldown period between scaling actions in seconds"""

    max: int
    """Maximum scale for the container"""

    min: int
    """Minimum scale for the container"""

    polling_interval: Optional[int] = None
    """Polling interval for scaling triggers in seconds"""

    triggers: ContainerScaleTriggers
    """Triggers for scaling actions"""


class Container(BaseModel):
    address: Optional[str] = None
    """Address of the inference instance"""

    deploy_status: ContainerDeployStatus
    """Status of the containers deployment"""

    error_message: Optional[str] = None
    """Error message if the container deployment failed"""

    region_id: int
    """Region name for the container"""

    scale: ContainerScale
    """Scale for the container"""


class IngressOpts(BaseModel):
    """Ingress options for the inference instance"""

    disable_response_buffering: bool
    """Disable response buffering if true.

    A client usually has a much slower connection and can not consume the response
    data as fast as it is produced by an upstream application. Ingress tries to
    buffer the whole response in order to release the upstream application as soon
    as possible.By default, the response buffering is enabled.
    """


class ObjectReference(BaseModel):
    kind: Literal["AppDeployment"]
    """Kind of the inference object to be referenced"""

    name: str
    """Name of the inference object to be referenced"""


class Probes(BaseModel):
    """Probes configured for all containers of the inference instance."""

    liveness_probe: Optional[ProbeConfig] = None
    """Liveness probe configuration"""

    readiness_probe: Optional[ProbeConfig] = None
    """Readiness probe configuration"""

    startup_probe: Optional[ProbeConfig] = None
    """Startup probe configuration"""


class InferenceDeployment(BaseModel):
    address: Optional[str] = None
    """Address of the inference instance"""

    auth_enabled: bool
    """`true` if instance uses API key authentication.

    `"Authorization": "Bearer *****"` or `"X-Api-Key": "*****"` header is required
    for the requests to the instance if enabled.
    """

    command: Optional[str] = None
    """Command to be executed when running a container from an image."""

    containers: List[Container]
    """List of containers for the inference instance"""

    created_at: Optional[str] = None
    """Inference instance creation date in ISO 8601 format."""

    credentials_name: str
    """Registry credentials name"""

    description: str
    """Inference instance description."""

    envs: Optional[Dict[str, str]] = None
    """Environment variables for the inference instance"""

    flavor_name: str
    """Flavor name for the inference instance"""

    image: str
    """Docker image for the inference instance.

    This field should contain the image name and tag in the format 'name:tag', e.g.,
    'nginx:latest'. It defaults to Docker Hub as the image registry, but any
    accessible Docker image URL can be specified.
    """

    ingress_opts: Optional[IngressOpts] = None
    """Ingress options for the inference instance"""

    listening_port: int
    """Listening port for the inference instance."""

    logging: Optional[Logging] = None
    """Logging configuration for the inference instance"""

    name: str
    """Inference instance name."""

    object_references: List[ObjectReference]
    """Indicates to which parent object this inference belongs to."""

    probes: Optional[Probes] = None
    """Probes configured for all containers of the inference instance."""

    project_id: int
    """Project ID. If not provided, your default project ID will be used."""

    status: Literal["ACTIVE", "DELETING", "DEPLOYING", "DISABLED", "PARTIALLYDEPLOYED", "PENDING"]
    """Inference instance status.

    Value can be one of the following:

    - `DEPLOYING` - The instance is being deployed. Containers are not yet created.
    - `PARTIALLYDEPLOYED` - All containers have been created, but some may not be
      ready yet. Instances stuck in this state typically indicate either image being
      pulled, or a failure of some kind. In the latter case, the `error_message`
      field of the respective container object in the `containers` collection
      explains the failure reason.
    - `ACTIVE` - The instance is running and ready to accept requests.
    - `DISABLED` - The instance is disabled and not accepting any requests.
    - `PENDING` - The instance is running but scaled to zero. It will be
      automatically scaled up when a request is made.
    - `DELETING` - The instance is being deleted.
    """

    timeout: Optional[int] = None
    """
    Specifies the duration in seconds without any requests after which the
    containers will be downscaled to their minimum scale value as defined by
    `scale.min`. If set, this helps in optimizing resource usage by reducing the
    number of container instances during periods of inactivity.
    """

    api_keys: Optional[List[str]] = None
    """List of API keys for the inference instance"""
