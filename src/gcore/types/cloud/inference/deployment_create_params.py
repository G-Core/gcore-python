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
    """
    '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments/post/parameters/0/schema'
    "$.paths['/cloud/v3/inference/{project_id}/deployments'].post.parameters[0].schema"
    """

    containers: Required[Iterable[Container]]
    """
    '#/components/schemas/InferenceInstanceInSerializerV3/properties/containers'
    "$.components.schemas.InferenceInstanceInSerializerV3.properties.containers"
    """

    flavor_name: Required[str]
    """
    '#/components/schemas/InferenceInstanceInSerializerV3/properties/flavor_name'
    "$.components.schemas.InferenceInstanceInSerializerV3.properties.flavor_name"
    """

    image: Required[str]
    """
    '#/components/schemas/InferenceInstanceInSerializerV3/properties/image'
    "$.components.schemas.InferenceInstanceInSerializerV3.properties.image"
    """

    listening_port: Required[int]
    """
    '#/components/schemas/InferenceInstanceInSerializerV3/properties/listening_port'
    "$.components.schemas.InferenceInstanceInSerializerV3.properties.listening_port"
    """

    name: Required[str]
    """
    '#/components/schemas/InferenceInstanceInSerializerV3/properties/name'
    "$.components.schemas.InferenceInstanceInSerializerV3.properties.name"
    """

    auth_enabled: bool
    """
    '#/components/schemas/InferenceInstanceInSerializerV3/properties/auth_enabled'
    "$.components.schemas.InferenceInstanceInSerializerV3.properties.auth_enabled"
    """

    command: Optional[List[str]]
    """
    '#/components/schemas/InferenceInstanceInSerializerV3/properties/command/anyOf/0'
    "$.components.schemas.InferenceInstanceInSerializerV3.properties.command.anyOf[0]"
    """

    credentials_name: Optional[str]
    """
    '#/components/schemas/InferenceInstanceInSerializerV3/properties/credentials_name/anyOf/0'
    "$.components.schemas.InferenceInstanceInSerializerV3.properties.credentials_name.anyOf[0]"
    """

    description: Optional[str]
    """
    '#/components/schemas/InferenceInstanceInSerializerV3/properties/description/anyOf/0'
    "$.components.schemas.InferenceInstanceInSerializerV3.properties.description.anyOf[0]"
    """

    envs: Dict[str, str]
    """
    '#/components/schemas/InferenceInstanceInSerializerV3/properties/envs'
    "$.components.schemas.InferenceInstanceInSerializerV3.properties.envs"
    """

    ingress_opts: Optional[IngressOptsParam]
    """
    '#/components/schemas/InferenceInstanceInSerializerV3/properties/ingress_opts/anyOf/0'
    "$.components.schemas.InferenceInstanceInSerializerV3.properties.ingress_opts.anyOf[0]"
    """

    logging: Optional[Logging]
    """
    '#/components/schemas/InferenceInstanceInSerializerV3/properties/logging/anyOf/0'
    "$.components.schemas.InferenceInstanceInSerializerV3.properties.logging.anyOf[0]"
    """

    probes: Optional[Probes]
    """
    '#/components/schemas/InferenceInstanceInSerializerV3/properties/probes/anyOf/0'
    "$.components.schemas.InferenceInstanceInSerializerV3.properties.probes.anyOf[0]"
    """

    api_timeout: Annotated[Optional[int], PropertyInfo(alias="timeout")]
    """
    '#/components/schemas/InferenceInstanceInSerializerV3/properties/timeout/anyOf/0'
    "$.components.schemas.InferenceInstanceInSerializerV3.properties.timeout.anyOf[0]"
    """


class ContainerScaleTriggersCPU(TypedDict, total=False):
    threshold: Required[int]
    """
    '#/components/schemas/ContainerScaleTriggersThresholdSerializer/properties/threshold'
    "$.components.schemas.ContainerScaleTriggersThresholdSerializer.properties.threshold"
    """


class ContainerScaleTriggersGPUMemory(TypedDict, total=False):
    threshold: Required[int]
    """
    '#/components/schemas/ContainerScaleTriggersThresholdSerializer/properties/threshold'
    "$.components.schemas.ContainerScaleTriggersThresholdSerializer.properties.threshold"
    """


class ContainerScaleTriggersGPUUtilization(TypedDict, total=False):
    threshold: Required[int]
    """
    '#/components/schemas/ContainerScaleTriggersThresholdSerializer/properties/threshold'
    "$.components.schemas.ContainerScaleTriggersThresholdSerializer.properties.threshold"
    """


class ContainerScaleTriggersHTTP(TypedDict, total=False):
    rate: Required[int]
    """
    '#/components/schemas/ContainerScaleTriggersRateSerializer/properties/rate'
    "$.components.schemas.ContainerScaleTriggersRateSerializer.properties.rate"
    """

    window: Required[int]
    """
    '#/components/schemas/ContainerScaleTriggersRateSerializer/properties/window'
    "$.components.schemas.ContainerScaleTriggersRateSerializer.properties.window"
    """


class ContainerScaleTriggersMemory(TypedDict, total=False):
    threshold: Required[int]
    """
    '#/components/schemas/ContainerScaleTriggersThresholdSerializer/properties/threshold'
    "$.components.schemas.ContainerScaleTriggersThresholdSerializer.properties.threshold"
    """


class ContainerScaleTriggersSqs(TypedDict, total=False):
    activation_queue_length: Required[int]
    """
    '#/components/schemas/ContainerScaleTriggersSqsSerializer/properties/activation_queue_length'
    "$.components.schemas.ContainerScaleTriggersSqsSerializer.properties.activation_queue_length"
    """

    aws_region: Required[str]
    """
    '#/components/schemas/ContainerScaleTriggersSqsSerializer/properties/aws_region'
    "$.components.schemas.ContainerScaleTriggersSqsSerializer.properties.aws_region"
    """

    queue_length: Required[int]
    """
    '#/components/schemas/ContainerScaleTriggersSqsSerializer/properties/queue_length'
    "$.components.schemas.ContainerScaleTriggersSqsSerializer.properties.queue_length"
    """

    queue_url: Required[str]
    """
    '#/components/schemas/ContainerScaleTriggersSqsSerializer/properties/queue_url'
    "$.components.schemas.ContainerScaleTriggersSqsSerializer.properties.queue_url"
    """

    secret_name: Required[str]
    """
    '#/components/schemas/ContainerScaleTriggersSqsSerializer/properties/secret_name'
    "$.components.schemas.ContainerScaleTriggersSqsSerializer.properties.secret_name"
    """

    aws_endpoint: Optional[str]
    """
    '#/components/schemas/ContainerScaleTriggersSqsSerializer/properties/aws_endpoint/anyOf/0'
    "$.components.schemas.ContainerScaleTriggersSqsSerializer.properties.aws_endpoint.anyOf[0]"
    """

    scale_on_delayed: bool
    """
    '#/components/schemas/ContainerScaleTriggersSqsSerializer/properties/scale_on_delayed'
    "$.components.schemas.ContainerScaleTriggersSqsSerializer.properties.scale_on_delayed"
    """

    scale_on_flight: bool
    """
    '#/components/schemas/ContainerScaleTriggersSqsSerializer/properties/scale_on_flight'
    "$.components.schemas.ContainerScaleTriggersSqsSerializer.properties.scale_on_flight"
    """


class ContainerScaleTriggers(TypedDict, total=False):
    cpu: Optional[ContainerScaleTriggersCPU]
    """
    '#/components/schemas/ContainerScaleTriggersSerializer/properties/cpu/anyOf/0'
    "$.components.schemas.ContainerScaleTriggersSerializer.properties.cpu.anyOf[0]"
    """

    gpu_memory: Optional[ContainerScaleTriggersGPUMemory]
    """
    '#/components/schemas/ContainerScaleTriggersSerializer/properties/gpu_memory/anyOf/0'
    "$.components.schemas.ContainerScaleTriggersSerializer.properties.gpu_memory.anyOf[0]"
    """

    gpu_utilization: Optional[ContainerScaleTriggersGPUUtilization]
    """
    '#/components/schemas/ContainerScaleTriggersSerializer/properties/gpu_utilization/anyOf/0'
    "$.components.schemas.ContainerScaleTriggersSerializer.properties.gpu_utilization.anyOf[0]"
    """

    http: Optional[ContainerScaleTriggersHTTP]
    """
    '#/components/schemas/ContainerScaleTriggersSerializer/properties/http/anyOf/0'
    "$.components.schemas.ContainerScaleTriggersSerializer.properties.http.anyOf[0]"
    """

    memory: Optional[ContainerScaleTriggersMemory]
    """
    '#/components/schemas/ContainerScaleTriggersSerializer/properties/memory/anyOf/0'
    "$.components.schemas.ContainerScaleTriggersSerializer.properties.memory.anyOf[0]"
    """

    sqs: Optional[ContainerScaleTriggersSqs]
    """
    '#/components/schemas/ContainerScaleTriggersSerializer/properties/sqs/anyOf/0'
    "$.components.schemas.ContainerScaleTriggersSerializer.properties.sqs.anyOf[0]"
    """


class ContainerScale(TypedDict, total=False):
    max: Required[int]
    """
    '#/components/schemas/ContainerScaleSerializerV3/properties/max'
    "$.components.schemas.ContainerScaleSerializerV3.properties.max"
    """

    min: Required[int]
    """
    '#/components/schemas/ContainerScaleSerializerV3/properties/min'
    "$.components.schemas.ContainerScaleSerializerV3.properties.min"
    """

    cooldown_period: Optional[int]
    """
    '#/components/schemas/ContainerScaleSerializerV3/properties/cooldown_period/anyOf/0'
    "$.components.schemas.ContainerScaleSerializerV3.properties.cooldown_period.anyOf[0]"
    """

    polling_interval: Optional[int]
    """
    '#/components/schemas/ContainerScaleSerializerV3/properties/polling_interval/anyOf/0'
    "$.components.schemas.ContainerScaleSerializerV3.properties.polling_interval.anyOf[0]"
    """

    triggers: ContainerScaleTriggers
    """
    '#/components/schemas/ContainerScaleSerializerV3/properties/triggers'
    "$.components.schemas.ContainerScaleSerializerV3.properties.triggers"
    """


class Container(TypedDict, total=False):
    region_id: Required[int]
    """
    '#/components/schemas/ContainerInSerializerV3/properties/region_id'
    "$.components.schemas.ContainerInSerializerV3.properties.region_id"
    """

    scale: Required[ContainerScale]
    """
    '#/components/schemas/ContainerInSerializerV3/properties/scale'
    "$.components.schemas.ContainerInSerializerV3.properties.scale"
    """


class Logging(TypedDict, total=False):
    destination_region_id: Optional[int]
    """
    '#/components/schemas/LoggingInSerializer/properties/destination_region_id/anyOf/0'
    "$.components.schemas.LoggingInSerializer.properties.destination_region_id.anyOf[0]"
    """

    enabled: bool
    """
    '#/components/schemas/LoggingInSerializer/properties/enabled'
    "$.components.schemas.LoggingInSerializer.properties.enabled"
    """

    retention_policy: Optional[LaasIndexRetentionPolicyParam]
    """
    '#/components/schemas/LoggingInSerializer/properties/retention_policy/anyOf/0'
    "$.components.schemas.LoggingInSerializer.properties.retention_policy.anyOf[0]"
    """

    topic_name: Optional[str]
    """
    '#/components/schemas/LoggingInSerializer/properties/topic_name/anyOf/0'
    "$.components.schemas.LoggingInSerializer.properties.topic_name.anyOf[0]"
    """


class Probes(TypedDict, total=False):
    liveness_probe: Optional[ContainerProbeConfigCreateParam]
    """
    '#/components/schemas/InferenceInstanceProbesSerializerV2/properties/liveness_probe/anyOf/0'
    "$.components.schemas.InferenceInstanceProbesSerializerV2.properties.liveness_probe.anyOf[0]"
    """

    readiness_probe: Optional[ContainerProbeConfigCreateParam]
    """
    '#/components/schemas/InferenceInstanceProbesSerializerV2/properties/readiness_probe/anyOf/0'
    "$.components.schemas.InferenceInstanceProbesSerializerV2.properties.readiness_probe.anyOf[0]"
    """

    startup_probe: Optional[ContainerProbeConfigCreateParam]
    """
    '#/components/schemas/InferenceInstanceProbesSerializerV2/properties/startup_probe/anyOf/0'
    "$.components.schemas.InferenceInstanceProbesSerializerV2.properties.startup_probe.anyOf[0]"
    """
