# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Secret"]


class Secret(BaseModel):
    id: str
    """Secret uuid"""

    name: str
    """Secret name"""

    secret_type: Literal["certificate", "opaque", "passphrase", "private", "public", "symmetric"]
    """Secret type, base64 encoded.

    symmetric - Used for storing byte arrays such as keys suitable for symmetric
    encryption; public - Used for storing the public key of an asymmetric keypair;
    private - Used for storing the private key of an asymmetric keypair;
    passphrase - Used for storing plain text passphrases; certificate - Used for
    storing cryptographic certificates such as X.509 certificates; opaque - Used for
    backwards compatibility with previous versions of the API
    """

    status: str
    """Status"""

    algorithm: Optional[str] = None
    """Metadata provided by a user or system for informational purposes.

    Defaults to None
    """

    bit_length: Optional[int] = None
    """Metadata provided by a user or system for informational purposes.

    Value must be greater than zero. Defaults to None
    """

    content_types: Optional[Dict[str, str]] = None
    """Describes the content-types that can be used to retrieve the payload.

    The content-type used with symmetric secrets is application/octet-stream
    """

    created: Optional[datetime] = None
    """Datetime when the secret was created. The format is 2020-01-01T12:00:00+00:00"""

    expiration: Optional[datetime] = None
    """Datetime when the secret will expire.

    The format is 2020-01-01T12:00:00+00:00. Defaults to None
    """

    mode: Optional[str] = None
    """Metadata provided by a user or system for informational purposes.

    Defaults to None
    """
