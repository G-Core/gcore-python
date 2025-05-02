# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ..logging import Logging
from .container import Container
from ...._models import BaseModel
from ..inference_probes import InferenceProbes
from ..ingress_opts_out import IngressOptsOut

__all__ = ["Inference"]


class Inference(BaseModel):
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

    ingress_opts: Optional[IngressOptsOut] = None
    """Ingress options for the inference instance"""

    listening_port: int
    """Listening port for the inference instance."""

    logging: Optional[Logging] = None
    """Logging configuration for the inference instance"""

    name: str
    """Inference instance name."""

    probes: Optional[InferenceProbes] = None
    """Probes configured for all containers of the inference instance."""

    project_id: int
    """Project ID. If not provided, your default project ID will be used."""

    status: Literal["ACTIVE", "DELETING", "DEPLOYING", "DISABLED", "PARTIALLYDEPLOYED"]
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
    - `DELETING` - The instance is being deleted.
    """

    timeout: Optional[int] = None
    """
    Specifies the duration in seconds without any requests after which the
    containers will be downscaled to their minimum scale value as defined by
    `scale.min`. If set, this helps in optimizing resource usage by reducing the
    number of container instances during periods of inactivity.
    """
