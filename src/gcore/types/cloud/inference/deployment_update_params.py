# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from ..ingress_opts_param import IngressOptsParam
from ..laas_index_retention_policy_param import LaasIndexRetentionPolicyParam
from ..container_probe_config_create_param import ContainerProbeConfigCreateParam

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
    "Logging",
    "Probes",
]


class DeploymentUpdateParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv3%2Finference%2F%7Bproject_id%7D%2Fdeployments%2F%7Bdeployment_name%7D/patch/parameters/0/schema'
    "$.paths['/cloud/v3/inference/{project_id}/deployments/{deployment_name}'].patch.parameters[0].schema"
    """

    auth_enabled: Optional[bool]
    """
    '#/components/schemas/InferenceInstanceInUpdateSerializerV3/properties/auth_enabled/anyOf/0'
    "$.components.schemas.InferenceInstanceInUpdateSerializerV3.properties.auth_enabled.anyOf[0]"
    """

    command: Optional[List[str]]
    """
    '#/components/schemas/InferenceInstanceInUpdateSerializerV3/properties/command/anyOf/0'
    "$.components.schemas.InferenceInstanceInUpdateSerializerV3.properties.command.anyOf[0]"
    """

    containers: Optional[Iterable[Container]]
    """
    '#/components/schemas/InferenceInstanceInUpdateSerializerV3/properties/containers/anyOf/0'
    "$.components.schemas.InferenceInstanceInUpdateSerializerV3.properties.containers.anyOf[0]"
    """

    credentials_name: Optional[str]
    """
    '#/components/schemas/InferenceInstanceInUpdateSerializerV3/properties/credentials_name/anyOf/0'
    "$.components.schemas.InferenceInstanceInUpdateSerializerV3.properties.credentials_name.anyOf[0]"
    """

    description: Optional[str]
    """
    '#/components/schemas/InferenceInstanceInUpdateSerializerV3/properties/description/anyOf/0'
    "$.components.schemas.InferenceInstanceInUpdateSerializerV3.properties.description.anyOf[0]"
    """

    envs: Optional[Dict[str, str]]
    """
    '#/components/schemas/InferenceInstanceInUpdateSerializerV3/properties/envs/anyOf/0'
    "$.components.schemas.InferenceInstanceInUpdateSerializerV3.properties.envs.anyOf[0]"
    """

    flavor_name: Optional[str]
    """
    '#/components/schemas/InferenceInstanceInUpdateSerializerV3/properties/flavor_name/anyOf/0'
    "$.components.schemas.InferenceInstanceInUpdateSerializerV3.properties.flavor_name.anyOf[0]"
    """

    image: Optional[str]
    """
    '#/components/schemas/InferenceInstanceInUpdateSerializerV3/properties/image/anyOf/0'
    "$.components.schemas.InferenceInstanceInUpdateSerializerV3.properties.image.anyOf[0]"
    """

    ingress_opts: Optional[IngressOptsParam]
    """
    '#/components/schemas/InferenceInstanceInUpdateSerializerV3/properties/ingress_opts/anyOf/0'
    "$.components.schemas.InferenceInstanceInUpdateSerializerV3.properties.ingress_opts.anyOf[0]"
    """

    listening_port: Optional[int]
    """
    '#/components/schemas/InferenceInstanceInUpdateSerializerV3/properties/listening_port/anyOf/0'
    "$.components.schemas.InferenceInstanceInUpdateSerializerV3.properties.listening_port.anyOf[0]"
    """

    logging: Optional[Logging]
    """
    '#/components/schemas/InferenceInstanceInUpdateSerializerV3/properties/logging/anyOf/0'
    "$.components.schemas.InferenceInstanceInUpdateSerializerV3.properties.logging.anyOf[0]"
    """

    probes: Optional[Probes]
    """
    '#/components/schemas/InferenceInstanceInUpdateSerializerV3/properties/probes/anyOf/0'
    "$.components.schemas.InferenceInstanceInUpdateSerializerV3.properties.probes.anyOf[0]"
    """

    api_timeout: Annotated[Optional[int], PropertyInfo(alias="timeout")]
    """
    '#/components/schemas/InferenceInstanceInUpdateSerializerV3/properties/timeout/anyOf/0'
    "$.components.schemas.InferenceInstanceInUpdateSerializerV3.properties.timeout.anyOf[0]"
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
    '#/components/schemas/ContainerScaleUpdateSerializerV3/properties/max'
    "$.components.schemas.ContainerScaleUpdateSerializerV3.properties.max"
    """

    min: Required[int]
    """
    '#/components/schemas/ContainerScaleUpdateSerializerV3/properties/min'
    "$.components.schemas.ContainerScaleUpdateSerializerV3.properties.min"
    """

    cooldown_period: int
    """
    '#/components/schemas/ContainerScaleUpdateSerializerV3/properties/cooldown_period'
    "$.components.schemas.ContainerScaleUpdateSerializerV3.properties.cooldown_period"
    """

    polling_interval: int
    """
    '#/components/schemas/ContainerScaleUpdateSerializerV3/properties/polling_interval'
    "$.components.schemas.ContainerScaleUpdateSerializerV3.properties.polling_interval"
    """

    triggers: ContainerScaleTriggers
    """
    '#/components/schemas/ContainerScaleUpdateSerializerV3/properties/triggers'
    "$.components.schemas.ContainerScaleUpdateSerializerV3.properties.triggers"
    """


class Container(TypedDict, total=False):
    region_id: Required[Optional[int]]
    """
    '#/components/schemas/ContainerInUpdateSerializerV3/properties/region_id/anyOf/0'
    "$.components.schemas.ContainerInUpdateSerializerV3.properties.region_id.anyOf[0]"
    """

    scale: Required[Optional[ContainerScale]]
    """
    '#/components/schemas/ContainerInUpdateSerializerV3/properties/scale/anyOf/0'
    "$.components.schemas.ContainerInUpdateSerializerV3.properties.scale.anyOf[0]"
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
