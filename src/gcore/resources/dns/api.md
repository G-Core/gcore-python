# DNS

Types:

```python
from gcore.types.dns import DNSGetAccountOverviewResponse, DNSLookupResponse
```

Methods:

- <code title="get /dns/v2/platform/info">client.dns.<a href="./src/gcore/resources/dns/dns.py">get_account_overview</a>() -> <a href="./src/gcore/types/dns/dns_get_account_overview_response.py">DNSGetAccountOverviewResponse</a></code>
- <code title="get /dns/v2/lookup">client.dns.<a href="./src/gcore/resources/dns/dns.py">lookup</a>(\*\*<a href="src/gcore/types/dns/dns_lookup_params.py">params</a>) -> <a href="./src/gcore/types/dns/dns_lookup_response.py">DNSLookupResponse</a></code>

## Locations

Types:

```python
from gcore.types.dns import (
    DNSLocationTranslations,
    LocationListResponse,
    LocationListContinentsResponse,
    LocationListCountriesResponse,
    LocationListRegionsResponse,
)
```

Methods:

- <code title="get /dns/v2/locations">client.dns.locations.<a href="./src/gcore/resources/dns/locations.py">list</a>() -> <a href="./src/gcore/types/dns/location_list_response.py">LocationListResponse</a></code>
- <code title="get /dns/v2/locations/continents">client.dns.locations.<a href="./src/gcore/resources/dns/locations.py">list_continents</a>() -> <a href="./src/gcore/types/dns/location_list_continents_response.py">LocationListContinentsResponse</a></code>
- <code title="get /dns/v2/locations/countries">client.dns.locations.<a href="./src/gcore/resources/dns/locations.py">list_countries</a>() -> <a href="./src/gcore/types/dns/location_list_countries_response.py">LocationListCountriesResponse</a></code>
- <code title="get /dns/v2/locations/regions">client.dns.locations.<a href="./src/gcore/resources/dns/locations.py">list_regions</a>() -> <a href="./src/gcore/types/dns/location_list_regions_response.py">LocationListRegionsResponse</a></code>

## Metrics

Types:

```python
from gcore.types.dns import MetricListResponse
```

Methods:

- <code title="get /dns/v2/monitor/metrics">client.dns.metrics.<a href="./src/gcore/resources/dns/metrics.py">list</a>(\*\*<a href="src/gcore/types/dns/metric_list_params.py">params</a>) -> str</code>

## Pickers

Types:

```python
from gcore.types.dns import DNSLabelName, PickerListResponse
```

Methods:

- <code title="get /dns/v2/pickers">client.dns.pickers.<a href="./src/gcore/resources/dns/pickers/pickers.py">list</a>() -> <a href="./src/gcore/types/dns/picker_list_response.py">PickerListResponse</a></code>

### Presets

Types:

```python
from gcore.types.dns.pickers import PresetListResponse
```

Methods:

- <code title="get /dns/v2/pickers/presets">client.dns.pickers.presets.<a href="./src/gcore/resources/dns/pickers/presets.py">list</a>() -> <a href="./src/gcore/types/dns/pickers/preset_list_response.py">PresetListResponse</a></code>

## Zones

Types:

```python
from gcore.types.dns import (
    DNSNameServer,
    ZoneCreateResponse,
    ZoneListResponse,
    ZoneCheckDelegationStatusResponse,
    ZoneExportResponse,
    ZoneGetResponse,
    ZoneGetStatisticsResponse,
    ZoneImportResponse,
)
```

Methods:

- <code title="post /dns/v2/zones">client.dns.zones.<a href="./src/gcore/resources/dns/zones/zones.py">create</a>(\*\*<a href="src/gcore/types/dns/zone_create_params.py">params</a>) -> <a href="./src/gcore/types/dns/zone_create_response.py">ZoneCreateResponse</a></code>
- <code title="get /dns/v2/zones">client.dns.zones.<a href="./src/gcore/resources/dns/zones/zones.py">list</a>(\*\*<a href="src/gcore/types/dns/zone_list_params.py">params</a>) -> <a href="./src/gcore/types/dns/zone_list_response.py">ZoneListResponse</a></code>
- <code title="delete /dns/v2/zones/{name}">client.dns.zones.<a href="./src/gcore/resources/dns/zones/zones.py">delete</a>(name) -> object</code>
- <code title="get /dns/v2/analyze/{name}/delegation-status">client.dns.zones.<a href="./src/gcore/resources/dns/zones/zones.py">check_delegation_status</a>(name) -> <a href="./src/gcore/types/dns/zone_check_delegation_status_response.py">ZoneCheckDelegationStatusResponse</a></code>
- <code title="patch /dns/v2/zones/{name}/disable">client.dns.zones.<a href="./src/gcore/resources/dns/zones/zones.py">disable</a>(name) -> object</code>
- <code title="patch /dns/v2/zones/{name}/enable">client.dns.zones.<a href="./src/gcore/resources/dns/zones/zones.py">enable</a>(name) -> object</code>
- <code title="get /dns/v2/zones/{zoneName}/export">client.dns.zones.<a href="./src/gcore/resources/dns/zones/zones.py">export</a>(zone_name) -> <a href="./src/gcore/types/dns/zone_export_response.py">ZoneExportResponse</a></code>
- <code title="get /dns/v2/zones/{name}">client.dns.zones.<a href="./src/gcore/resources/dns/zones/zones.py">get</a>(name) -> <a href="./src/gcore/types/dns/zone_get_response.py">ZoneGetResponse</a></code>
- <code title="get /dns/v2/zones/{name}/statistics">client.dns.zones.<a href="./src/gcore/resources/dns/zones/zones.py">get_statistics</a>(name, \*\*<a href="src/gcore/types/dns/zone_get_statistics_params.py">params</a>) -> <a href="./src/gcore/types/dns/zone_get_statistics_response.py">ZoneGetStatisticsResponse</a></code>
- <code title="post /dns/v2/zones/{zoneName}/import">client.dns.zones.<a href="./src/gcore/resources/dns/zones/zones.py">import\_</a>(zone_name, \*\*<a href="src/gcore/types/dns/zone_import_params.py">params</a>) -> <a href="./src/gcore/types/dns/zone_import_response.py">ZoneImportResponse</a></code>
- <code title="put /dns/v2/zones/{name}">client.dns.zones.<a href="./src/gcore/resources/dns/zones/zones.py">replace</a>(path_name, \*\*<a href="src/gcore/types/dns/zone_replace_params.py">params</a>) -> object</code>

### Dnssec

Types:

```python
from gcore.types.dns.zones import DnssecUpdateResponse, DnssecGetResponse
```

Methods:

- <code title="patch /dns/v2/zones/{name}/dnssec">client.dns.zones.dnssec.<a href="./src/gcore/resources/dns/zones/dnssec.py">update</a>(name, \*\*<a href="src/gcore/types/dns/zones/dnssec_update_params.py">params</a>) -> <a href="./src/gcore/types/dns/zones/dnssec_update_response.py">DnssecUpdateResponse</a></code>
- <code title="get /dns/v2/zones/{name}/dnssec">client.dns.zones.dnssec.<a href="./src/gcore/resources/dns/zones/dnssec.py">get</a>(name) -> <a href="./src/gcore/types/dns/zones/dnssec_get_response.py">DnssecGetResponse</a></code>

### Rrsets

Types:

```python
from gcore.types.dns.zones import (
    DNSFailoverLog,
    DNSOutputRrset,
    RrsetListResponse,
    RrsetGetFailoverLogsResponse,
)
```

Methods:

- <code title="post /dns/v2/zones/{zoneName}/{rrsetName}/{rrsetType}">client.dns.zones.rrsets.<a href="./src/gcore/resources/dns/zones/rrsets.py">create</a>(rrset_type, \*, zone_name, rrset_name, \*\*<a href="src/gcore/types/dns/zones/rrset_create_params.py">params</a>) -> <a href="./src/gcore/types/dns/zones/dns_output_rrset.py">DNSOutputRrset</a></code>
- <code title="get /dns/v2/zones/{zoneName}/rrsets">client.dns.zones.rrsets.<a href="./src/gcore/resources/dns/zones/rrsets.py">list</a>(zone_name, \*\*<a href="src/gcore/types/dns/zones/rrset_list_params.py">params</a>) -> <a href="./src/gcore/types/dns/zones/rrset_list_response.py">RrsetListResponse</a></code>
- <code title="delete /dns/v2/zones/{zoneName}/{rrsetName}/{rrsetType}">client.dns.zones.rrsets.<a href="./src/gcore/resources/dns/zones/rrsets.py">delete</a>(rrset_type, \*, zone_name, rrset_name) -> object</code>
- <code title="get /dns/v2/zones/{zoneName}/{rrsetName}/{rrsetType}">client.dns.zones.rrsets.<a href="./src/gcore/resources/dns/zones/rrsets.py">get</a>(rrset_type, \*, zone_name, rrset_name) -> <a href="./src/gcore/types/dns/zones/dns_output_rrset.py">DNSOutputRrset</a></code>
- <code title="get /dns/v2/zones/{zoneName}/{rrsetName}/{rrsetType}/failover/log">client.dns.zones.rrsets.<a href="./src/gcore/resources/dns/zones/rrsets.py">get_failover_logs</a>(rrset_type, \*, zone_name, rrset_name, \*\*<a href="src/gcore/types/dns/zones/rrset_get_failover_logs_params.py">params</a>) -> <a href="./src/gcore/types/dns/zones/rrset_get_failover_logs_response.py">RrsetGetFailoverLogsResponse</a></code>
- <code title="put /dns/v2/zones/{zoneName}/{rrsetName}/{rrsetType}">client.dns.zones.rrsets.<a href="./src/gcore/resources/dns/zones/rrsets.py">replace</a>(rrset_type, \*, zone_name, rrset_name, \*\*<a href="src/gcore/types/dns/zones/rrset_replace_params.py">params</a>) -> <a href="./src/gcore/types/dns/zones/dns_output_rrset.py">DNSOutputRrset</a></code>

## NetworkMappings

Types:

```python
from gcore.types.dns import (
    DNSMappingEntry,
    DNSNetworkMapping,
    NetworkMappingCreateResponse,
    NetworkMappingListResponse,
    NetworkMappingImportResponse,
)
```

Methods:

- <code title="post /dns/v2/network-mappings">client.dns.network_mappings.<a href="./src/gcore/resources/dns/network_mappings.py">create</a>(\*\*<a href="src/gcore/types/dns/network_mapping_create_params.py">params</a>) -> <a href="./src/gcore/types/dns/network_mapping_create_response.py">NetworkMappingCreateResponse</a></code>
- <code title="get /dns/v2/network-mappings">client.dns.network_mappings.<a href="./src/gcore/resources/dns/network_mappings.py">list</a>(\*\*<a href="src/gcore/types/dns/network_mapping_list_params.py">params</a>) -> <a href="./src/gcore/types/dns/network_mapping_list_response.py">NetworkMappingListResponse</a></code>
- <code title="delete /dns/v2/network-mappings/{id}">client.dns.network_mappings.<a href="./src/gcore/resources/dns/network_mappings.py">delete</a>(id) -> object</code>
- <code title="get /dns/v2/network-mappings/{id}">client.dns.network_mappings.<a href="./src/gcore/resources/dns/network_mappings.py">get</a>(id) -> <a href="./src/gcore/types/dns/dns_network_mapping.py">DNSNetworkMapping</a></code>
- <code title="get /dns/v2/network-mappings/{name}">client.dns.network_mappings.<a href="./src/gcore/resources/dns/network_mappings.py">get_by_name</a>(name) -> <a href="./src/gcore/types/dns/dns_network_mapping.py">DNSNetworkMapping</a></code>
- <code title="post /dns/v2/network-mappings/import">client.dns.network*mappings.<a href="./src/gcore/resources/dns/network_mappings.py">import*</a>() -> <a href="./src/gcore/types/dns/network_mapping_import_response.py">NetworkMappingImportResponse</a></code>
- <code title="put /dns/v2/network-mappings/{id}">client.dns.network_mappings.<a href="./src/gcore/resources/dns/network_mappings.py">replace</a>(id, \*\*<a href="src/gcore/types/dns/network_mapping_replace_params.py">params</a>) -> object</code>
