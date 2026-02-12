# Waap

Types:

```python
from gcore.types.waap import WaapGetAccountOverviewResponse
```

Methods:

- <code title="get /waap/v1/clients/me">client.waap.<a href="./src/gcore/resources/waap/waap.py">get_account_overview</a>() -> <a href="./src/gcore/types/waap/waap_get_account_overview_response.py">WaapGetAccountOverviewResponse</a></code>

## Statistics

Types:

```python
from gcore.types.waap import WaapStatisticItem, WaapStatisticsSeries
```

Methods:

- <code title="get /waap/v1/statistics/series">client.waap.statistics.<a href="./src/gcore/resources/waap/statistics.py">get_usage_series</a>(\*\*<a href="src/gcore/types/waap/statistic_get_usage_series_params.py">params</a>) -> <a href="./src/gcore/types/waap/waap_statistics_series.py">WaapStatisticsSeries</a></code>

## Domains

Types:

```python
from gcore.types.waap import (
    WaapDetailedDomain,
    WaapDomainAPISettings,
    WaapDomainDDOSSettings,
    WaapDomainSettingsModel,
    WaapPolicyMode,
    WaapRuleSet,
    WaapSummaryDomain,
    DomainListRuleSetsResponse,
)
```

Methods:

- <code title="patch /waap/v1/domains/{domain_id}">client.waap.domains.<a href="./src/gcore/resources/waap/domains/domains.py">update</a>(domain_id, \*\*<a href="src/gcore/types/waap/domain_update_params.py">params</a>) -> None</code>
- <code title="get /waap/v1/domains">client.waap.domains.<a href="./src/gcore/resources/waap/domains/domains.py">list</a>(\*\*<a href="src/gcore/types/waap/domain_list_params.py">params</a>) -> <a href="./src/gcore/types/waap/waap_summary_domain.py">SyncOffsetPage[WaapSummaryDomain]</a></code>
- <code title="delete /waap/v1/domains/{domain_id}">client.waap.domains.<a href="./src/gcore/resources/waap/domains/domains.py">delete</a>(domain_id) -> None</code>
- <code title="get /waap/v1/domains/{domain_id}">client.waap.domains.<a href="./src/gcore/resources/waap/domains/domains.py">get</a>(domain_id) -> <a href="./src/gcore/types/waap/waap_detailed_domain.py">WaapDetailedDomain</a></code>
- <code title="get /waap/v1/domains/{domain_id}/rule-sets">client.waap.domains.<a href="./src/gcore/resources/waap/domains/domains.py">list_rule_sets</a>(domain_id) -> <a href="./src/gcore/types/waap/domain_list_rule_sets_response.py">DomainListRuleSetsResponse</a></code>
- <code title="patch /waap/v1/domains/{domain_id}/policies/{policy_id}/toggle">client.waap.domains.<a href="./src/gcore/resources/waap/domains/domains.py">toggle_policy</a>(policy_id, \*, domain_id) -> <a href="./src/gcore/types/waap/waap_policy_mode.py">WaapPolicyMode</a></code>

### Settings

Methods:

- <code title="patch /waap/v1/domains/{domain_id}/settings">client.waap.domains.settings.<a href="./src/gcore/resources/waap/domains/settings.py">update</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/setting_update_params.py">params</a>) -> None</code>
- <code title="get /waap/v1/domains/{domain_id}/settings">client.waap.domains.settings.<a href="./src/gcore/resources/waap/domains/settings.py">get</a>(domain_id) -> <a href="./src/gcore/types/waap/waap_domain_settings_model.py">WaapDomainSettingsModel</a></code>

### APIPaths

Types:

```python
from gcore.types.waap.domains import WaapAPIPath
```

Methods:

- <code title="post /waap/v1/domains/{domain_id}/api-paths">client.waap.domains.api_paths.<a href="./src/gcore/resources/waap/domains/api_paths.py">create</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/api_path_create_params.py">params</a>) -> <a href="./src/gcore/types/waap/domains/waap_api_path.py">WaapAPIPath</a></code>
- <code title="patch /waap/v1/domains/{domain_id}/api-paths/{path_id}">client.waap.domains.api_paths.<a href="./src/gcore/resources/waap/domains/api_paths.py">update</a>(path_id, \*, domain_id, \*\*<a href="src/gcore/types/waap/domains/api_path_update_params.py">params</a>) -> None</code>
- <code title="get /waap/v1/domains/{domain_id}/api-paths">client.waap.domains.api_paths.<a href="./src/gcore/resources/waap/domains/api_paths.py">list</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/api_path_list_params.py">params</a>) -> <a href="./src/gcore/types/waap/domains/waap_api_path.py">SyncOffsetPage[WaapAPIPath]</a></code>
- <code title="delete /waap/v1/domains/{domain_id}/api-paths/{path_id}">client.waap.domains.api_paths.<a href="./src/gcore/resources/waap/domains/api_paths.py">delete</a>(path_id, \*, domain_id) -> None</code>
- <code title="get /waap/v1/domains/{domain_id}/api-paths/{path_id}">client.waap.domains.api_paths.<a href="./src/gcore/resources/waap/domains/api_paths.py">get</a>(path_id, \*, domain_id) -> <a href="./src/gcore/types/waap/domains/waap_api_path.py">WaapAPIPath</a></code>

### APIPathGroups

Types:

```python
from gcore.types.waap.domains import APIPathGroupList
```

Methods:

- <code title="get /waap/v1/domains/{domain_id}/api-path-groups">client.waap.domains.api_path_groups.<a href="./src/gcore/resources/waap/domains/api_path_groups.py">list</a>(domain_id) -> <a href="./src/gcore/types/waap/domains/api_path_group_list.py">APIPathGroupList</a></code>

### APIDiscovery

Types:

```python
from gcore.types.waap.domains import WaapAPIDiscoverySettings, WaapAPIScanResult, WaapTaskID
```

Methods:

- <code title="get /waap/v1/domains/{domain_id}/api-discovery/scan-results/{scan_id}">client.waap.domains.api_discovery.<a href="./src/gcore/resources/waap/domains/api_discovery.py">get_scan_result</a>(scan_id, \*, domain_id) -> <a href="./src/gcore/types/waap/domains/waap_api_scan_result.py">WaapAPIScanResult</a></code>
- <code title="get /waap/v1/domains/{domain_id}/api-discovery/settings">client.waap.domains.api_discovery.<a href="./src/gcore/resources/waap/domains/api_discovery.py">get_settings</a>(domain_id) -> <a href="./src/gcore/types/waap/domains/waap_api_discovery_settings.py">WaapAPIDiscoverySettings</a></code>
- <code title="get /waap/v1/domains/{domain_id}/api-discovery/scan-results">client.waap.domains.api_discovery.<a href="./src/gcore/resources/waap/domains/api_discovery.py">list_scan_results</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/api_discovery_list_scan_results_params.py">params</a>) -> <a href="./src/gcore/types/waap/domains/waap_api_scan_result.py">SyncOffsetPage[WaapAPIScanResult]</a></code>
- <code title="post /waap/v1/domains/{domain_id}/api-discovery/scan">client.waap.domains.api_discovery.<a href="./src/gcore/resources/waap/domains/api_discovery.py">scan_openapi</a>(domain_id) -> <a href="./src/gcore/types/waap/domains/waap_task_id.py">WaapTaskID</a></code>
- <code title="patch /waap/v1/domains/{domain_id}/api-discovery/settings">client.waap.domains.api_discovery.<a href="./src/gcore/resources/waap/domains/api_discovery.py">update_settings</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/api_discovery_update_settings_params.py">params</a>) -> <a href="./src/gcore/types/waap/domains/waap_api_discovery_settings.py">WaapAPIDiscoverySettings</a></code>
- <code title="post /waap/v1/domains/{domain_id}/api-discovery/upload">client.waap.domains.api_discovery.<a href="./src/gcore/resources/waap/domains/api_discovery.py">upload_openapi</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/api_discovery_upload_openapi_params.py">params</a>) -> <a href="./src/gcore/types/waap/domains/waap_task_id.py">WaapTaskID</a></code>

### Insights

Types:

```python
from gcore.types.waap.domains import WaapInsight
```

Methods:

- <code title="get /waap/v1/domains/{domain_id}/insights">client.waap.domains.insights.<a href="./src/gcore/resources/waap/domains/insights.py">list</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/insight_list_params.py">params</a>) -> <a href="./src/gcore/types/waap/domains/waap_insight.py">SyncOffsetPage[WaapInsight]</a></code>
- <code title="get /waap/v1/domains/{domain_id}/insights/{insight_id}">client.waap.domains.insights.<a href="./src/gcore/resources/waap/domains/insights.py">get</a>(insight_id, \*, domain_id) -> <a href="./src/gcore/types/waap/domains/waap_insight.py">WaapInsight</a></code>
- <code title="put /waap/v1/domains/{domain_id}/insights/{insight_id}">client.waap.domains.insights.<a href="./src/gcore/resources/waap/domains/insights.py">replace</a>(insight_id, \*, domain_id, \*\*<a href="src/gcore/types/waap/domains/insight_replace_params.py">params</a>) -> <a href="./src/gcore/types/waap/domains/waap_insight.py">WaapInsight</a></code>

### InsightSilences

Types:

```python
from gcore.types.waap.domains import WaapInsightSilence
```

Methods:

- <code title="post /waap/v1/domains/{domain_id}/insight-silences">client.waap.domains.insight_silences.<a href="./src/gcore/resources/waap/domains/insight_silences.py">create</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/insight_silence_create_params.py">params</a>) -> <a href="./src/gcore/types/waap/domains/waap_insight_silence.py">WaapInsightSilence</a></code>
- <code title="patch /waap/v1/domains/{domain_id}/insight-silences/{silence_id}">client.waap.domains.insight_silences.<a href="./src/gcore/resources/waap/domains/insight_silences.py">update</a>(silence_id, \*, domain_id, \*\*<a href="src/gcore/types/waap/domains/insight_silence_update_params.py">params</a>) -> <a href="./src/gcore/types/waap/domains/waap_insight_silence.py">WaapInsightSilence</a></code>
- <code title="get /waap/v1/domains/{domain_id}/insight-silences">client.waap.domains.insight_silences.<a href="./src/gcore/resources/waap/domains/insight_silences.py">list</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/insight_silence_list_params.py">params</a>) -> <a href="./src/gcore/types/waap/domains/waap_insight_silence.py">SyncOffsetPage[WaapInsightSilence]</a></code>
- <code title="delete /waap/v1/domains/{domain_id}/insight-silences/{silence_id}">client.waap.domains.insight_silences.<a href="./src/gcore/resources/waap/domains/insight_silences.py">delete</a>(silence_id, \*, domain_id) -> None</code>
- <code title="get /waap/v1/domains/{domain_id}/insight-silences/{silence_id}">client.waap.domains.insight_silences.<a href="./src/gcore/resources/waap/domains/insight_silences.py">get</a>(silence_id, \*, domain_id) -> <a href="./src/gcore/types/waap/domains/waap_insight_silence.py">WaapInsightSilence</a></code>

### Statistics

Types:

```python
from gcore.types.waap.domains import (
    WaapBlockedStatistics,
    WaapCountStatistics,
    WaapDDOSAttack,
    WaapDDOSInfo,
    WaapEventStatistics,
    WaapRequestDetails,
    WaapRequestSummary,
    WaapTrafficMetrics,
    StatisticGetTrafficSeriesResponse,
)
```

Methods:

- <code title="get /waap/v1/domains/{domain_id}/ddos-attacks">client.waap.domains.statistics.<a href="./src/gcore/resources/waap/domains/statistics.py">get_ddos_attacks</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/statistic_get_ddos_attacks_params.py">params</a>) -> <a href="./src/gcore/types/waap/domains/waap_ddos_attack.py">SyncOffsetPage[WaapDDOSAttack]</a></code>
- <code title="get /waap/v1/domains/{domain_id}/ddos-info">client.waap.domains.statistics.<a href="./src/gcore/resources/waap/domains/statistics.py">get_ddos_info</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/statistic_get_ddos_info_params.py">params</a>) -> <a href="./src/gcore/types/waap/domains/waap_ddos_info.py">SyncOffsetPage[WaapDDOSInfo]</a></code>
- <code title="get /waap/v1/domains/{domain_id}/stats">client.waap.domains.statistics.<a href="./src/gcore/resources/waap/domains/statistics.py">get_events_aggregated</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/statistic_get_events_aggregated_params.py">params</a>) -> <a href="./src/gcore/types/waap/domains/waap_event_statistics.py">WaapEventStatistics</a></code>
- <code title="get /waap/v1/domains/{domain_id}/requests/{request_id}/details">client.waap.domains.statistics.<a href="./src/gcore/resources/waap/domains/statistics.py">get_request_details</a>(request_id, \*, domain_id) -> <a href="./src/gcore/types/waap/domains/waap_request_details.py">WaapRequestDetails</a></code>
- <code title="get /waap/v1/domains/{domain_id}/requests">client.waap.domains.statistics.<a href="./src/gcore/resources/waap/domains/statistics.py">get_requests_series</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/statistic_get_requests_series_params.py">params</a>) -> <a href="./src/gcore/types/waap/domains/waap_request_summary.py">SyncOffsetPage[WaapRequestSummary]</a></code>
- <code title="get /waap/v1/domains/{domain_id}/traffic">client.waap.domains.statistics.<a href="./src/gcore/resources/waap/domains/statistics.py">get_traffic_series</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/statistic_get_traffic_series_params.py">params</a>) -> <a href="./src/gcore/types/waap/domains/statistic_get_traffic_series_response.py">StatisticGetTrafficSeriesResponse</a></code>

### CustomRules

Types:

```python
from gcore.types.waap.domains import WaapCustomRule
```

Methods:

- <code title="post /waap/v1/domains/{domain_id}/custom-rules">client.waap.domains.custom_rules.<a href="./src/gcore/resources/waap/domains/custom_rules.py">create</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/custom_rule_create_params.py">params</a>) -> <a href="./src/gcore/types/waap/domains/waap_custom_rule.py">WaapCustomRule</a></code>
- <code title="patch /waap/v1/domains/{domain_id}/custom-rules/{rule_id}">client.waap.domains.custom_rules.<a href="./src/gcore/resources/waap/domains/custom_rules.py">update</a>(rule_id, \*, domain_id, \*\*<a href="src/gcore/types/waap/domains/custom_rule_update_params.py">params</a>) -> None</code>
- <code title="get /waap/v1/domains/{domain_id}/custom-rules">client.waap.domains.custom_rules.<a href="./src/gcore/resources/waap/domains/custom_rules.py">list</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/custom_rule_list_params.py">params</a>) -> <a href="./src/gcore/types/waap/domains/waap_custom_rule.py">SyncOffsetPage[WaapCustomRule]</a></code>
- <code title="delete /waap/v1/domains/{domain_id}/custom-rules/{rule_id}">client.waap.domains.custom_rules.<a href="./src/gcore/resources/waap/domains/custom_rules.py">delete</a>(rule_id, \*, domain_id) -> None</code>
- <code title="post /waap/v1/domains/{domain_id}/custom-rules/bulk_delete">client.waap.domains.custom_rules.<a href="./src/gcore/resources/waap/domains/custom_rules.py">delete_multiple</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/custom_rule_delete_multiple_params.py">params</a>) -> None</code>
- <code title="get /waap/v1/domains/{domain_id}/custom-rules/{rule_id}">client.waap.domains.custom_rules.<a href="./src/gcore/resources/waap/domains/custom_rules.py">get</a>(rule_id, \*, domain_id) -> <a href="./src/gcore/types/waap/domains/waap_custom_rule.py">WaapCustomRule</a></code>
- <code title="patch /waap/v1/domains/{domain_id}/custom-rules/{rule_id}/{action}">client.waap.domains.custom_rules.<a href="./src/gcore/resources/waap/domains/custom_rules.py">toggle</a>(action, \*, domain_id, rule_id) -> None</code>

### FirewallRules

Types:

```python
from gcore.types.waap.domains import WaapFirewallRule
```

Methods:

- <code title="post /waap/v1/domains/{domain_id}/firewall-rules">client.waap.domains.firewall_rules.<a href="./src/gcore/resources/waap/domains/firewall_rules.py">create</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/firewall_rule_create_params.py">params</a>) -> <a href="./src/gcore/types/waap/domains/waap_firewall_rule.py">WaapFirewallRule</a></code>
- <code title="patch /waap/v1/domains/{domain_id}/firewall-rules/{rule_id}">client.waap.domains.firewall_rules.<a href="./src/gcore/resources/waap/domains/firewall_rules.py">update</a>(rule_id, \*, domain_id, \*\*<a href="src/gcore/types/waap/domains/firewall_rule_update_params.py">params</a>) -> None</code>
- <code title="get /waap/v1/domains/{domain_id}/firewall-rules">client.waap.domains.firewall_rules.<a href="./src/gcore/resources/waap/domains/firewall_rules.py">list</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/firewall_rule_list_params.py">params</a>) -> <a href="./src/gcore/types/waap/domains/waap_firewall_rule.py">SyncOffsetPage[WaapFirewallRule]</a></code>
- <code title="delete /waap/v1/domains/{domain_id}/firewall-rules/{rule_id}">client.waap.domains.firewall_rules.<a href="./src/gcore/resources/waap/domains/firewall_rules.py">delete</a>(rule_id, \*, domain_id) -> None</code>
- <code title="post /waap/v1/domains/{domain_id}/firewall-rules/bulk_delete">client.waap.domains.firewall_rules.<a href="./src/gcore/resources/waap/domains/firewall_rules.py">delete_multiple</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/firewall_rule_delete_multiple_params.py">params</a>) -> None</code>
- <code title="get /waap/v1/domains/{domain_id}/firewall-rules/{rule_id}">client.waap.domains.firewall_rules.<a href="./src/gcore/resources/waap/domains/firewall_rules.py">get</a>(rule_id, \*, domain_id) -> <a href="./src/gcore/types/waap/domains/waap_firewall_rule.py">WaapFirewallRule</a></code>
- <code title="patch /waap/v1/domains/{domain_id}/firewall-rules/{rule_id}/{action}">client.waap.domains.firewall_rules.<a href="./src/gcore/resources/waap/domains/firewall_rules.py">toggle</a>(action, \*, domain_id, rule_id) -> None</code>

### AdvancedRules

Types:

```python
from gcore.types.waap.domains import WaapAdvancedRule
```

Methods:

- <code title="post /waap/v1/domains/{domain_id}/advanced-rules">client.waap.domains.advanced_rules.<a href="./src/gcore/resources/waap/domains/advanced_rules.py">create</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/advanced_rule_create_params.py">params</a>) -> <a href="./src/gcore/types/waap/domains/waap_advanced_rule.py">WaapAdvancedRule</a></code>
- <code title="patch /waap/v1/domains/{domain_id}/advanced-rules/{rule_id}">client.waap.domains.advanced_rules.<a href="./src/gcore/resources/waap/domains/advanced_rules.py">update</a>(rule_id, \*, domain_id, \*\*<a href="src/gcore/types/waap/domains/advanced_rule_update_params.py">params</a>) -> None</code>
- <code title="get /waap/v1/domains/{domain_id}/advanced-rules">client.waap.domains.advanced_rules.<a href="./src/gcore/resources/waap/domains/advanced_rules.py">list</a>(domain_id, \*\*<a href="src/gcore/types/waap/domains/advanced_rule_list_params.py">params</a>) -> <a href="./src/gcore/types/waap/domains/waap_advanced_rule.py">SyncOffsetPage[WaapAdvancedRule]</a></code>
- <code title="delete /waap/v1/domains/{domain_id}/advanced-rules/{rule_id}">client.waap.domains.advanced_rules.<a href="./src/gcore/resources/waap/domains/advanced_rules.py">delete</a>(rule_id, \*, domain_id) -> None</code>
- <code title="get /waap/v1/domains/{domain_id}/advanced-rules/{rule_id}">client.waap.domains.advanced_rules.<a href="./src/gcore/resources/waap/domains/advanced_rules.py">get</a>(rule_id, \*, domain_id) -> <a href="./src/gcore/types/waap/domains/waap_advanced_rule.py">WaapAdvancedRule</a></code>
- <code title="patch /waap/v1/domains/{domain_id}/advanced-rules/{rule_id}/{action}">client.waap.domains.advanced_rules.<a href="./src/gcore/resources/waap/domains/advanced_rules.py">toggle</a>(action, \*, domain_id, rule_id) -> None</code>

## CustomPageSets

Types:

```python
from gcore.types.waap import WaapCustomPagePreview, WaapCustomPageSet
```

Methods:

- <code title="post /waap/v1/custom-page-sets">client.waap.custom_page_sets.<a href="./src/gcore/resources/waap/custom_page_sets.py">create</a>(\*\*<a href="src/gcore/types/waap/custom_page_set_create_params.py">params</a>) -> <a href="./src/gcore/types/waap/waap_custom_page_set.py">WaapCustomPageSet</a></code>
- <code title="patch /waap/v1/custom-page-sets/{set_id}">client.waap.custom_page_sets.<a href="./src/gcore/resources/waap/custom_page_sets.py">update</a>(set_id, \*\*<a href="src/gcore/types/waap/custom_page_set_update_params.py">params</a>) -> None</code>
- <code title="get /waap/v1/custom-page-sets">client.waap.custom_page_sets.<a href="./src/gcore/resources/waap/custom_page_sets.py">list</a>(\*\*<a href="src/gcore/types/waap/custom_page_set_list_params.py">params</a>) -> <a href="./src/gcore/types/waap/waap_custom_page_set.py">SyncOffsetPage[WaapCustomPageSet]</a></code>
- <code title="delete /waap/v1/custom-page-sets/{set_id}">client.waap.custom_page_sets.<a href="./src/gcore/resources/waap/custom_page_sets.py">delete</a>(set_id) -> None</code>
- <code title="get /waap/v1/custom-page-sets/{set_id}">client.waap.custom_page_sets.<a href="./src/gcore/resources/waap/custom_page_sets.py">get</a>(set_id) -> <a href="./src/gcore/types/waap/waap_custom_page_set.py">WaapCustomPageSet</a></code>
- <code title="post /waap/v1/preview-custom-page">client.waap.custom_page_sets.<a href="./src/gcore/resources/waap/custom_page_sets.py">preview</a>(\*\*<a href="src/gcore/types/waap/custom_page_set_preview_params.py">params</a>) -> <a href="./src/gcore/types/waap/waap_custom_page_preview.py">WaapCustomPagePreview</a></code>

## AdvancedRules

Types:

```python
from gcore.types.waap import WaapAdvancedRuleDescriptor, WaapAdvancedRuleDescriptorList
```

Methods:

- <code title="get /waap/v1/advanced-rules/descriptor">client.waap.advanced_rules.<a href="./src/gcore/resources/waap/advanced_rules.py">list</a>() -> <a href="./src/gcore/types/waap/waap_advanced_rule_descriptor_list.py">WaapAdvancedRuleDescriptorList</a></code>

## Tags

Types:

```python
from gcore.types.waap import WaapTag
```

Methods:

- <code title="get /waap/v1/tags">client.waap.tags.<a href="./src/gcore/resources/waap/tags.py">list</a>(\*\*<a href="src/gcore/types/waap/tag_list_params.py">params</a>) -> <a href="./src/gcore/types/waap/waap_tag.py">SyncOffsetPage[WaapTag]</a></code>

## Organizations

Types:

```python
from gcore.types.waap import WaapOrganization
```

Methods:

- <code title="get /waap/v1/organizations">client.waap.organizations.<a href="./src/gcore/resources/waap/organizations.py">list</a>(\*\*<a href="src/gcore/types/waap/organization_list_params.py">params</a>) -> <a href="./src/gcore/types/waap/waap_organization.py">SyncOffsetPage[WaapOrganization]</a></code>

## Insights

Types:

```python
from gcore.types.waap import WaapInsightType
```

Methods:

- <code title="get /waap/v1/security-insights/types">client.waap.insights.<a href="./src/gcore/resources/waap/insights.py">list_types</a>(\*\*<a href="src/gcore/types/waap/insight_list_types_params.py">params</a>) -> <a href="./src/gcore/types/waap/waap_insight_type.py">SyncOffsetPage[WaapInsightType]</a></code>

## IPInfo

Types:

```python
from gcore.types.waap import (
    WaapIPCountryAttack,
    WaapIPDDOSInfoModel,
    WaapIPInfo,
    WaapRuleBlockedRequests,
    WaapTimeSeriesAttack,
    WaapTopSession,
    WaapTopURL,
    WaapTopUserAgent,
    IPInfoGetAttackTimeSeriesResponse,
    IPInfoGetBlockedRequestsResponse,
    IPInfoGetTopURLsResponse,
    IPInfoGetTopUserAgentsResponse,
    IPInfoGetTopUserSessionsResponse,
    IPInfoListAttackedCountriesResponse,
)
```

Methods:

- <code title="get /waap/v1/ip-info/attack-time-series">client.waap.ip_info.<a href="./src/gcore/resources/waap/ip_info/ip_info.py">get_attack_time_series</a>(\*\*<a href="src/gcore/types/waap/ip_info_get_attack_time_series_params.py">params</a>) -> <a href="./src/gcore/types/waap/ip_info_get_attack_time_series_response.py">IPInfoGetAttackTimeSeriesResponse</a></code>
- <code title="get /waap/v1/ip-info/blocked-requests">client.waap.ip_info.<a href="./src/gcore/resources/waap/ip_info/ip_info.py">get_blocked_requests</a>(\*\*<a href="src/gcore/types/waap/ip_info_get_blocked_requests_params.py">params</a>) -> <a href="./src/gcore/types/waap/ip_info_get_blocked_requests_response.py">IPInfoGetBlockedRequestsResponse</a></code>
- <code title="get /waap/v1/ip-info/ddos">client.waap.ip_info.<a href="./src/gcore/resources/waap/ip_info/ip_info.py">get_ddos_attack_series</a>(\*\*<a href="src/gcore/types/waap/ip_info_get_ddos_attack_series_params.py">params</a>) -> <a href="./src/gcore/types/waap/waap_ip_ddos_info_model.py">WaapIPDDOSInfoModel</a></code>
- <code title="get /waap/v1/ip-info/ip-info">client.waap.ip_info.<a href="./src/gcore/resources/waap/ip_info/ip_info.py">get_ip_info</a>(\*\*<a href="src/gcore/types/waap/ip_info_get_ip_info_params.py">params</a>) -> <a href="./src/gcore/types/waap/waap_ip_info.py">WaapIPInfo</a></code>
- <code title="get /waap/v1/ip-info/top-urls">client.waap.ip_info.<a href="./src/gcore/resources/waap/ip_info/ip_info.py">get_top_urls</a>(\*\*<a href="src/gcore/types/waap/ip_info_get_top_urls_params.py">params</a>) -> <a href="./src/gcore/types/waap/ip_info_get_top_urls_response.py">IPInfoGetTopURLsResponse</a></code>
- <code title="get /waap/v1/ip-info/top-user-agents">client.waap.ip_info.<a href="./src/gcore/resources/waap/ip_info/ip_info.py">get_top_user_agents</a>(\*\*<a href="src/gcore/types/waap/ip_info_get_top_user_agents_params.py">params</a>) -> <a href="./src/gcore/types/waap/ip_info_get_top_user_agents_response.py">IPInfoGetTopUserAgentsResponse</a></code>
- <code title="get /waap/v1/ip-info/top-sessions">client.waap.ip_info.<a href="./src/gcore/resources/waap/ip_info/ip_info.py">get_top_user_sessions</a>(\*\*<a href="src/gcore/types/waap/ip_info_get_top_user_sessions_params.py">params</a>) -> <a href="./src/gcore/types/waap/ip_info_get_top_user_sessions_response.py">IPInfoGetTopUserSessionsResponse</a></code>
- <code title="get /waap/v1/ip-info/attack-map">client.waap.ip_info.<a href="./src/gcore/resources/waap/ip_info/ip_info.py">list_attacked_countries</a>(\*\*<a href="src/gcore/types/waap/ip_info_list_attacked_countries_params.py">params</a>) -> <a href="./src/gcore/types/waap/ip_info_list_attacked_countries_response.py">IPInfoListAttackedCountriesResponse</a></code>

### Metrics

Types:

```python
from gcore.types.waap.ip_info import WaapIPInfoCounts
```

Methods:

- <code title="get /waap/v1/ip-info/counts">client.waap.ip_info.metrics.<a href="./src/gcore/resources/waap/ip_info/metrics.py">list</a>(\*\*<a href="src/gcore/types/waap/ip_info/metric_list_params.py">params</a>) -> <a href="./src/gcore/types/waap/ip_info/waap_ip_info_counts.py">WaapIPInfoCounts</a></code>
