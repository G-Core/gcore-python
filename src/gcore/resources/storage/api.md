# Storage

## Locations

Types:

```python
from gcore.types.storage import Location
```

Methods:

- <code title="get /storage/v4/locations">client.storage.locations.<a href="./src/gcore/resources/storage/locations.py">list</a>(\*\*<a href="src/gcore/types/storage/location_list_params.py">params</a>) -> <a href="./src/gcore/types/storage/location.py">SyncOffsetPage[Location]</a></code>

## ObjectStorages

Types:

```python
from gcore.types.storage import S3Storage, S3StorageCreated
```

Methods:

- <code title="post /storage/v4/object_storages">client.storage.object_storages.<a href="./src/gcore/resources/storage/object_storages/object_storages.py">create</a>(\*\*<a href="src/gcore/types/storage/object_storage_create_params.py">params</a>) -> <a href="./src/gcore/types/storage/s3_storage_created.py">S3StorageCreated</a></code>
- <code title="get /storage/v4/object_storages">client.storage.object_storages.<a href="./src/gcore/resources/storage/object_storages/object_storages.py">list</a>(\*\*<a href="src/gcore/types/storage/object_storage_list_params.py">params</a>) -> <a href="./src/gcore/types/storage/s3_storage.py">SyncOffsetPage[S3Storage]</a></code>
- <code title="delete /storage/v4/object_storages/{storage_id}">client.storage.object_storages.<a href="./src/gcore/resources/storage/object_storages/object_storages.py">delete</a>(storage_id) -> None</code>
- <code title="get /storage/v4/object_storages/{storage_id}">client.storage.object_storages.<a href="./src/gcore/resources/storage/object_storages/object_storages.py">get</a>(storage_id) -> <a href="./src/gcore/types/storage/s3_storage.py">S3Storage</a></code>
- <code title="post /storage/v4/object_storages/{storage_id}/restore">client.storage.object_storages.<a href="./src/gcore/resources/storage/object_storages/object_storages.py">restore</a>(storage_id) -> None</code>

### AccessKeys

Types:

```python
from gcore.types.storage.object_storages import AccessKey, AccessKeyCreated
```

Methods:

- <code title="post /storage/v4/object_storages/{storage_id}/access_keys">client.storage.object_storages.access_keys.<a href="./src/gcore/resources/storage/object_storages/access_keys.py">create</a>(storage_id) -> <a href="./src/gcore/types/storage/object_storages/access_key_created.py">AccessKeyCreated</a></code>
- <code title="get /storage/v4/object_storages/{storage_id}/access_keys">client.storage.object_storages.access_keys.<a href="./src/gcore/resources/storage/object_storages/access_keys.py">list</a>(storage_id, \*\*<a href="src/gcore/types/storage/object_storages/access_key_list_params.py">params</a>) -> <a href="./src/gcore/types/storage/object_storages/access_key.py">SyncOffsetPage[AccessKey]</a></code>
- <code title="delete /storage/v4/object_storages/{storage_id}/access_keys/{access_key}">client.storage.object_storages.access_keys.<a href="./src/gcore/resources/storage/object_storages/access_keys.py">delete</a>(access_key, \*, storage_id) -> None</code>
- <code title="get /storage/v4/object_storages/{storage_id}/access_keys/{access_key}">client.storage.object_storages.access_keys.<a href="./src/gcore/resources/storage/object_storages/access_keys.py">get</a>(access_key, \*, storage_id) -> <a href="./src/gcore/types/storage/object_storages/access_key.py">AccessKey</a></code>

### Buckets

Types:

```python
from gcore.types.storage.object_storages import Bucket
```

Methods:

- <code title="post /storage/v4/object_storages/{storage_id}/buckets">client.storage.object_storages.buckets.<a href="./src/gcore/resources/storage/object_storages/buckets.py">create</a>(storage_id, \*\*<a href="src/gcore/types/storage/object_storages/bucket_create_params.py">params</a>) -> <a href="./src/gcore/types/storage/object_storages/bucket.py">Bucket</a></code>
- <code title="patch /storage/v4/object_storages/{storage_id}/buckets/{bucket_name}">client.storage.object_storages.buckets.<a href="./src/gcore/resources/storage/object_storages/buckets.py">update</a>(bucket_name, \*, storage_id, \*\*<a href="src/gcore/types/storage/object_storages/bucket_update_params.py">params</a>) -> <a href="./src/gcore/types/storage/object_storages/bucket.py">Bucket</a></code>
- <code title="get /storage/v4/object_storages/{storage_id}/buckets">client.storage.object_storages.buckets.<a href="./src/gcore/resources/storage/object_storages/buckets.py">list</a>(storage_id, \*\*<a href="src/gcore/types/storage/object_storages/bucket_list_params.py">params</a>) -> <a href="./src/gcore/types/storage/object_storages/bucket.py">SyncOffsetPage[Bucket]</a></code>
- <code title="delete /storage/v4/object_storages/{storage_id}/buckets/{bucket_name}">client.storage.object_storages.buckets.<a href="./src/gcore/resources/storage/object_storages/buckets.py">delete</a>(bucket_name, \*, storage_id) -> None</code>
- <code title="get /storage/v4/object_storages/{storage_id}/buckets/{bucket_name}">client.storage.object_storages.buckets.<a href="./src/gcore/resources/storage/object_storages/buckets.py">get</a>(bucket_name, \*, storage_id) -> <a href="./src/gcore/types/storage/object_storages/bucket.py">Bucket</a></code>

## SftpStorages

Types:

```python
from gcore.types.storage import SftpStorage
```

Methods:

- <code title="post /storage/v4/sftp_storages">client.storage.sftp_storages.<a href="./src/gcore/resources/storage/sftp_storages.py">create</a>(\*\*<a href="src/gcore/types/storage/sftp_storage_create_params.py">params</a>) -> <a href="./src/gcore/types/storage/sftp_storage.py">SftpStorage</a></code>
- <code title="patch /storage/v4/sftp_storages/{storage_id}">client.storage.sftp_storages.<a href="./src/gcore/resources/storage/sftp_storages.py">update</a>(storage_id, \*\*<a href="src/gcore/types/storage/sftp_storage_update_params.py">params</a>) -> <a href="./src/gcore/types/storage/sftp_storage.py">SftpStorage</a></code>
- <code title="get /storage/v4/sftp_storages">client.storage.sftp_storages.<a href="./src/gcore/resources/storage/sftp_storages.py">list</a>(\*\*<a href="src/gcore/types/storage/sftp_storage_list_params.py">params</a>) -> <a href="./src/gcore/types/storage/sftp_storage.py">SyncOffsetPage[SftpStorage]</a></code>
- <code title="delete /storage/v4/sftp_storages/{storage_id}">client.storage.sftp_storages.<a href="./src/gcore/resources/storage/sftp_storages.py">delete</a>(storage_id) -> None</code>
- <code title="get /storage/v4/sftp_storages/{storage_id}">client.storage.sftp_storages.<a href="./src/gcore/resources/storage/sftp_storages.py">get</a>(storage_id) -> <a href="./src/gcore/types/storage/sftp_storage.py">SftpStorage</a></code>

## SSHKeys

Types:

```python
from gcore.types.storage import SSHKey
```

Methods:

- <code title="post /storage/v4/ssh_keys">client.storage.ssh_keys.<a href="./src/gcore/resources/storage/ssh_keys.py">create</a>(\*\*<a href="src/gcore/types/storage/ssh_key_create_params.py">params</a>) -> <a href="./src/gcore/types/storage/ssh_key.py">SSHKey</a></code>
- <code title="get /storage/v4/ssh_keys">client.storage.ssh_keys.<a href="./src/gcore/resources/storage/ssh_keys.py">list</a>(\*\*<a href="src/gcore/types/storage/ssh_key_list_params.py">params</a>) -> <a href="./src/gcore/types/storage/ssh_key.py">SyncOffsetPage[SSHKey]</a></code>
- <code title="delete /storage/v4/ssh_keys/{ssh_key_id}">client.storage.ssh_keys.<a href="./src/gcore/resources/storage/ssh_keys.py">delete</a>(ssh_key_id) -> None</code>
- <code title="get /storage/v4/ssh_keys/{ssh_key_id}">client.storage.ssh_keys.<a href="./src/gcore/resources/storage/ssh_keys.py">get</a>(ssh_key_id) -> <a href="./src/gcore/types/storage/ssh_key.py">SSHKey</a></code>

## Statistics

Types:

```python
from gcore.types.storage import UsageSeries, UsageTotal, StatisticGetUsageSeriesResponse
```

Methods:

- <code title="post /storage/stats/v1/storage/usage/total">client.storage.statistics.<a href="./src/gcore/resources/storage/statistics.py">get_usage_aggregated</a>(\*\*<a href="src/gcore/types/storage/statistic_get_usage_aggregated_params.py">params</a>) -> <a href="./src/gcore/types/storage/usage_total.py">UsageTotal</a></code>
- <code title="post /storage/stats/v1/storage/usage/series">client.storage.statistics.<a href="./src/gcore/resources/storage/statistics.py">get_usage_series</a>(\*\*<a href="src/gcore/types/storage/statistic_get_usage_series_params.py">params</a>) -> <a href="./src/gcore/types/storage/statistic_get_usage_series_response.py">StatisticGetUsageSeriesResponse</a></code>
