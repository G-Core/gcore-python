# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ResourceUsageStats"]


class ResourceUsageStats(BaseModel):
    api_1_example: Optional[object] = FieldInfo(alias="1 (example)", default=None)
    """ID of CDN resource for which statistics data is shown."""

    backblaze_bytes: Optional[List[int]] = None
    """BackBlaze bytes from Backblaze origin.

    Represented by two values:

    - 1543622400 — Time in the UNIX timestamp when statistics were received.
    - 17329220573 — Bytes.
    """

    metrics: Optional[object] = None
    """Types of statistics data.

    Possible values:

    - **`upstream_bytes`** – Traffic in bytes from an origin server to CDN servers
      or to origin shielding when used.
    - **`sent_bytes`** – Traffic in bytes from CDN servers to clients.
    - **`shield_bytes`** – Traffic in bytes from origin shielding to CDN servers.
    - **`backblaze_bytes`** - Traffic in bytes from Backblaze origin.
    - **`total_bytes`** – `shield_bytes`, `upstream_bytes` and `sent_bytes`
      combined.
    - **`cdn_bytes`** – `sent_bytes` and `shield_bytes` combined.
    - **requests** – Number of requests to edge servers.
    - **`responses_2xx`** – Number of 2xx response codes.
    - **`responses_3xx`** – Number of 3xx response codes.
    - **`responses_4xx`** – Number of 4xx response codes.
    - **`responses_5xx`** – Number of 5xx response codes.
    - **`responses_hit`** – Number of responses with the header Cache: HIT.
    - **`responses_miss`** – Number of responses with the header Cache: MISS.
    - **`response_types`** – Statistics by content type. It returns a number of
      responses for content with different MIME types.
    - **`cache_hit_traffic_ratio`** – Formula: 1 - `upstream_bytes` / `sent_bytes`.
      We deduct the non-cached traffic from the total traffic amount.
    - **`cache_hit_requests_ratio`** – Formula: `responses_hit` / requests. The
      share of sending cached content.
    - **`shield_traffic_ratio`** – Formula: (`shield_bytes` - `upstream_bytes`) /
      `shield_bytes`. The efficiency of the Origin Shielding: how much more traffic
      is sent from the Origin Shielding than from the origin.
    - **`image_processed`** - Number of images transformed on the Image optimization
      service.
    - **`request_time`** - Time elapsed between the first bytes of a request were
      processed and logging after the last bytes were sent to a user.
    - **`upstream_response_time`** - Number of milliseconds it took to receive a
      response from an origin. If upstream `response_time_` contains several
      indications for one request (in case of more than 1 origin), we summarize
      them. In case of aggregating several queries, the average of this amount is
      calculated.

    Metrics **`upstream_response_time`** and **`request_time`** should be requested
    separately from other metrics
    """

    region: Optional[object] = None
    """Regions for which data is displayed.

    Possible values:

    - **na** – North America
    - **eu** – Europe
    - **cis** – Commonwealth of Independent States
    - **asia** – Asia
    - **au** – Australia
    - **latam** – Latin America
    - **me** – Middle East
    - **africa** - Africa
    - **sa** - South America
    """

    resource: Optional[object] = None
    """Resources IDs by which statistics data is grouped."""

    sent_bytes: Optional[List[int]] = None
    """Bytes from CDN servers to the end-users.

    Represented by two values:

    - 1543622400 — Time in the UNIX timestamp when statistics were received.
    - 17329220573 — Bytes.
    """

    total_bytes: Optional[List[int]] = None
    """Upstream bytes and `sent_bytes` combined.

    Represented by two values:

    - 1543622400 — Time in the UNIX timestamp when statistics were received.
    - 17329220573 — Bytes.
    """

    upstream_bytes: Optional[List[int]] = None
    """Bytes from the upstream to the CDN servers.

    Represented by two values:

    - 1543622400 — Time in the UNIX timestamp when statistics were received.
    - 17329220573 — Bytes.
    """
