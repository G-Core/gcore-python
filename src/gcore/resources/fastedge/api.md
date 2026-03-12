# Fastedge

Types:

```python
from gcore.types.fastedge import Client
```

Methods:

- <code title="get /fastedge/v1/me">client.fastedge.<a href="./src/gcore/resources/fastedge/fastedge.py">get_account_overview</a>() -> <a href="./src/gcore/types/fastedge/client.py">Client</a></code>

## Templates

Types:

```python
from gcore.types.fastedge import Template, TemplateParameter, TemplateShort
```

Methods:

- <code title="post /fastedge/v1/template">client.fastedge.templates.<a href="./src/gcore/resources/fastedge/templates.py">create</a>(\*\*<a href="src/gcore/types/fastedge/template_create_params.py">params</a>) -> <a href="./src/gcore/types/fastedge/template_short.py">TemplateShort</a></code>
- <code title="get /fastedge/v1/template">client.fastedge.templates.<a href="./src/gcore/resources/fastedge/templates.py">list</a>(\*\*<a href="src/gcore/types/fastedge/template_list_params.py">params</a>) -> <a href="./src/gcore/types/fastedge/template_short.py">SyncOffsetPageFastedgeTemplates[TemplateShort]</a></code>

## Secrets

Types:

```python
from gcore.types.fastedge import Secret, SecretShort, SecretCreateResponse, SecretListResponse
```

Methods:

- <code title="post /fastedge/v1/secrets">client.fastedge.secrets.<a href="./src/gcore/resources/fastedge/secrets.py">create</a>(\*\*<a href="src/gcore/types/fastedge/secret_create_params.py">params</a>) -> <a href="./src/gcore/types/fastedge/secret_create_response.py">SecretCreateResponse</a></code>
- <code title="get /fastedge/v1/secrets">client.fastedge.secrets.<a href="./src/gcore/resources/fastedge/secrets.py">list</a>(\*\*<a href="src/gcore/types/fastedge/secret_list_params.py">params</a>) -> <a href="./src/gcore/types/fastedge/secret_list_response.py">SecretListResponse</a></code>

## Binaries

Types:

```python
from gcore.types.fastedge import Binary, BinaryShort, BinaryListResponse
```

Methods:

- <code title="post /fastedge/v1/binaries/raw">client.fastedge.binaries.<a href="./src/gcore/resources/fastedge/binaries.py">create</a>(body, \*\*<a href="src/gcore/types/fastedge/binary_create_params.py">params</a>) -> <a href="./src/gcore/types/fastedge/binary_short.py">BinaryShort</a></code>
- <code title="get /fastedge/v1/binaries">client.fastedge.binaries.<a href="./src/gcore/resources/fastedge/binaries.py">list</a>() -> <a href="./src/gcore/types/fastedge/binary_list_response.py">BinaryListResponse</a></code>

## Statistics

Types:

```python
from gcore.types.fastedge import (
    CallStatus,
    DurationStats,
    StatisticGetCallSeriesResponse,
    StatisticGetDurationSeriesResponse,
)
```

Methods:

- <code title="get /fastedge/v1/stats/calls">client.fastedge.statistics.<a href="./src/gcore/resources/fastedge/statistics.py">get_call_series</a>(\*\*<a href="src/gcore/types/fastedge/statistic_get_call_series_params.py">params</a>) -> <a href="./src/gcore/types/fastedge/statistic_get_call_series_response.py">StatisticGetCallSeriesResponse</a></code>
- <code title="get /fastedge/v1/stats/app_duration">client.fastedge.statistics.<a href="./src/gcore/resources/fastedge/statistics.py">get_duration_series</a>(\*\*<a href="src/gcore/types/fastedge/statistic_get_duration_series_params.py">params</a>) -> <a href="./src/gcore/types/fastedge/statistic_get_duration_series_response.py">StatisticGetDurationSeriesResponse</a></code>

## Apps

Types:

```python
from gcore.types.fastedge import App, AppShort
```

Methods:

- <code title="post /fastedge/v1/apps">client.fastedge.apps.<a href="./src/gcore/resources/fastedge/apps.py">create</a>(\*\*<a href="src/gcore/types/fastedge/app_create_params.py">params</a>) -> <a href="./src/gcore/types/fastedge/app_short.py">AppShort</a></code>
- <code title="get /fastedge/v1/apps">client.fastedge.apps.<a href="./src/gcore/resources/fastedge/apps.py">list</a>(\*\*<a href="src/gcore/types/fastedge/app_list_params.py">params</a>) -> <a href="./src/gcore/types/fastedge/app_short.py">SyncOffsetPageFastedgeApps[AppShort]</a></code>

### Logs

Types:

```python
from gcore.types.fastedge.apps import Log
```

## KvStores

Types:

```python
from gcore.types.fastedge import KvStore, KvStoreShort, KvStoreCreateResponse, KvStoreListResponse
```

Methods:

- <code title="post /fastedge/v1/kv">client.fastedge.kv_stores.<a href="./src/gcore/resources/fastedge/kv_stores.py">create</a>(\*\*<a href="src/gcore/types/fastedge/kv_store_create_params.py">params</a>) -> <a href="./src/gcore/types/fastedge/kv_store_create_response.py">KvStoreCreateResponse</a></code>
- <code title="get /fastedge/v1/kv">client.fastedge.kv_stores.<a href="./src/gcore/resources/fastedge/kv_stores.py">list</a>(\*\*<a href="src/gcore/types/fastedge/kv_store_list_params.py">params</a>) -> <a href="./src/gcore/types/fastedge/kv_store_list_response.py">KvStoreListResponse</a></code>
