# Storage

Types:

```python
from gcore.types.storage import Storage
```

Methods:

- <code title="post /storage/provisioning/v2/storage">client.storage.<a href="./src/gcore/resources/storage/storage.py">create</a>(\*\*<a href="src/gcore/types/storage/storage_create_params.py">params</a>) -> <a href="./src/gcore/types/storage/storage.py">Storage</a></code>
- <code title="patch /storage/provisioning/v2/storage/{storage_id}">client.storage.<a href="./src/gcore/resources/storage/storage.py">update</a>(storage_id, \*\*<a href="src/gcore/types/storage/storage_update_params.py">params</a>) -> <a href="./src/gcore/types/storage/storage.py">Storage</a></code>
- <code title="get /storage/provisioning/v3/storage">client.storage.<a href="./src/gcore/resources/storage/storage.py">list</a>(\*\*<a href="src/gcore/types/storage/storage_list_params.py">params</a>) -> <a href="./src/gcore/types/storage/storage.py">SyncOffsetPage[Storage]</a></code>
- <code title="delete /storage/provisioning/v1/storage/{storage_id}">client.storage.<a href="./src/gcore/resources/storage/storage.py">delete</a>(storage_id) -> None</code>
- <code title="get /storage/provisioning/v1/storage/{storage_id}">client.storage.<a href="./src/gcore/resources/storage/storage.py">get</a>(storage_id) -> <a href="./src/gcore/types/storage/storage.py">Storage</a></code>
- <code title="post /storage/provisioning/v1/storage/{storage_id}/key/{key_id}/link">client.storage.<a href="./src/gcore/resources/storage/storage.py">link_ssh_key</a>(key_id, \*, storage_id) -> None</code>
- <code title="post /storage/provisioning/v1/storage/{storage_id}/restore">client.storage.<a href="./src/gcore/resources/storage/storage.py">restore</a>(storage_id, \*\*<a href="src/gcore/types/storage/storage_restore_params.py">params</a>) -> None</code>
- <code title="post /storage/provisioning/v1/storage/{storage_id}/key/{key_id}/unlink">client.storage.<a href="./src/gcore/resources/storage/storage.py">unlink_ssh_key</a>(key_id, \*, storage_id) -> None</code>

## Locations

Types:

```python
from gcore.types.storage import Location
```

Methods:

- <code title="get /storage/provisioning/v2/locations">client.storage.locations.<a href="./src/gcore/resources/storage/locations.py">list</a>(\*\*<a href="src/gcore/types/storage/location_list_params.py">params</a>) -> <a href="./src/gcore/types/storage/location.py">SyncOffsetPage[Location]</a></code>

## Statistics

Types:

```python
from gcore.types.storage import UsageSeries, UsageTotal, StatisticGetUsageSeriesResponse
```

Methods:

- <code title="post /storage/stats/v1/storage/usage/total">client.storage.statistics.<a href="./src/gcore/resources/storage/statistics.py">get_usage_aggregated</a>(\*\*<a href="src/gcore/types/storage/statistic_get_usage_aggregated_params.py">params</a>) -> <a href="./src/gcore/types/storage/usage_total.py">UsageTotal</a></code>
- <code title="post /storage/stats/v1/storage/usage/series">client.storage.statistics.<a href="./src/gcore/resources/storage/statistics.py">get_usage_series</a>(\*\*<a href="src/gcore/types/storage/statistic_get_usage_series_params.py">params</a>) -> <a href="./src/gcore/types/storage/statistic_get_usage_series_response.py">StatisticGetUsageSeriesResponse</a></code>

## Credentials

Methods:

- <code title="post /storage/provisioning/v1/storage/{storage_id}/credentials">client.storage.credentials.<a href="./src/gcore/resources/storage/credentials.py">recreate</a>(storage_id, \*\*<a href="src/gcore/types/storage/credential_recreate_params.py">params</a>) -> <a href="./src/gcore/types/storage/storage.py">Storage</a></code>

## Buckets

Types:

```python
from gcore.types.storage import Bucket
```

Methods:

- <code title="post /storage/provisioning/v1/storage/{storage_id}/s3/bucket/{bucket_name}">client.storage.buckets.<a href="./src/gcore/resources/storage/buckets/buckets.py">create</a>(bucket_name, \*, storage_id) -> None</code>
- <code title="get /storage/provisioning/v2/storage/{storage_id}/s3/buckets">client.storage.buckets.<a href="./src/gcore/resources/storage/buckets/buckets.py">list</a>(storage_id, \*\*<a href="src/gcore/types/storage/bucket_list_params.py">params</a>) -> <a href="./src/gcore/types/storage/bucket.py">SyncOffsetPage[Bucket]</a></code>
- <code title="delete /storage/provisioning/v1/storage/{storage_id}/s3/bucket/{bucket_name}">client.storage.buckets.<a href="./src/gcore/resources/storage/buckets/buckets.py">delete</a>(bucket_name, \*, storage_id) -> None</code>

### Cors

Types:

```python
from gcore.types.storage.buckets import BucketCors
```

Methods:

- <code title="post /storage/provisioning/v1/storage/{storage_id}/s3/bucket/{bucket_name}/cors">client.storage.buckets.cors.<a href="./src/gcore/resources/storage/buckets/cors.py">create</a>(bucket_name, \*, storage_id, \*\*<a href="src/gcore/types/storage/buckets/cor_create_params.py">params</a>) -> None</code>
- <code title="get /storage/provisioning/v1/storage/{storage_id}/s3/bucket/{bucket_name}/cors">client.storage.buckets.cors.<a href="./src/gcore/resources/storage/buckets/cors.py">get</a>(bucket_name, \*, storage_id) -> <a href="./src/gcore/types/storage/buckets/bucket_cors.py">BucketCors</a></code>

### Lifecycle

Methods:

- <code title="post /storage/provisioning/v1/storage/{storage_id}/s3/bucket/{bucket_name}/lifecycle">client.storage.buckets.lifecycle.<a href="./src/gcore/resources/storage/buckets/lifecycle.py">create</a>(bucket_name, \*, storage_id, \*\*<a href="src/gcore/types/storage/buckets/lifecycle_create_params.py">params</a>) -> None</code>
- <code title="delete /storage/provisioning/v1/storage/{storage_id}/s3/bucket/{bucket_name}/lifecycle">client.storage.buckets.lifecycle.<a href="./src/gcore/resources/storage/buckets/lifecycle.py">delete</a>(bucket_name, \*, storage_id) -> None</code>

### Policy

Types:

```python
from gcore.types.storage.buckets import BucketPolicy, PolicyGetResponse
```

Methods:

- <code title="post /storage/provisioning/v1/storage/{storage_id}/s3/bucket/{bucket_name}/policy">client.storage.buckets.policy.<a href="./src/gcore/resources/storage/buckets/policy.py">create</a>(bucket_name, \*, storage_id) -> None</code>
- <code title="delete /storage/provisioning/v1/storage/{storage_id}/s3/bucket/{bucket_name}/policy">client.storage.buckets.policy.<a href="./src/gcore/resources/storage/buckets/policy.py">delete</a>(bucket_name, \*, storage_id) -> None</code>
- <code title="get /storage/provisioning/v1/storage/{storage_id}/s3/bucket/{bucket_name}/policy">client.storage.buckets.policy.<a href="./src/gcore/resources/storage/buckets/policy.py">get</a>(bucket_name, \*, storage_id) -> <a href="./src/gcore/types/storage/buckets/policy_get_response.py">PolicyGetResponse</a></code>
