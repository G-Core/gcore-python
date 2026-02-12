# CDN

Types:

```python
from gcore.types.cdn import (
    AlibabaRegions,
    AwsRegions,
    CDNAccount,
    CDNAccountLimits,
    CDNAvailableFeatures,
    PurgeStatus,
    CDNListPurgeStatusesResponse,
)
```

Methods:

- <code title="get /cdn/clients/me/limits">client.cdn.<a href="./src/gcore/resources/cdn/cdn.py">get_account_limits</a>() -> <a href="./src/gcore/types/cdn/cdn_account_limits.py">CDNAccountLimits</a></code>
- <code title="get /cdn/clients/me">client.cdn.<a href="./src/gcore/resources/cdn/cdn.py">get_account_overview</a>() -> <a href="./src/gcore/types/cdn/cdn_account.py">CDNAccount</a></code>
- <code title="get /cdn/clients/me/features">client.cdn.<a href="./src/gcore/resources/cdn/cdn.py">get_available_features</a>() -> <a href="./src/gcore/types/cdn/cdn_available_features.py">CDNAvailableFeatures</a></code>
- <code title="get /cdn/alibaba_regions">client.cdn.<a href="./src/gcore/resources/cdn/cdn.py">list_alibaba_regions</a>() -> <a href="./src/gcore/types/cdn/alibaba_regions.py">AlibabaRegions</a></code>
- <code title="get /cdn/aws_regions">client.cdn.<a href="./src/gcore/resources/cdn/cdn.py">list_aws_regions</a>() -> <a href="./src/gcore/types/cdn/aws_regions.py">AwsRegions</a></code>
- <code title="get /cdn/purge_statuses">client.cdn.<a href="./src/gcore/resources/cdn/cdn.py">list_purge_statuses</a>(\*\*<a href="src/gcore/types/cdn/cdn_list_purge_statuses_params.py">params</a>) -> <a href="./src/gcore/types/cdn/cdn_list_purge_statuses_response.py">CDNListPurgeStatusesResponse</a></code>
- <code title="patch /cdn/clients/me">client.cdn.<a href="./src/gcore/resources/cdn/cdn.py">update_account</a>(\*\*<a href="src/gcore/types/cdn/cdn_update_account_params.py">params</a>) -> <a href="./src/gcore/types/cdn/cdn_account.py">CDNAccount</a></code>

## CDNResources

Types:

```python
from gcore.types.cdn import CDNResource, CDNResourceList
```

Methods:

- <code title="post /cdn/resources">client.cdn.cdn_resources.<a href="./src/gcore/resources/cdn/cdn_resources/cdn_resources.py">create</a>(\*\*<a href="src/gcore/types/cdn/cdn_resource_create_params.py">params</a>) -> <a href="./src/gcore/types/cdn/cdn_resource.py">CDNResource</a></code>
- <code title="patch /cdn/resources/{resource_id}">client.cdn.cdn_resources.<a href="./src/gcore/resources/cdn/cdn_resources/cdn_resources.py">update</a>(resource_id, \*\*<a href="src/gcore/types/cdn/cdn_resource_update_params.py">params</a>) -> <a href="./src/gcore/types/cdn/cdn_resource.py">CDNResource</a></code>
- <code title="get /cdn/resources">client.cdn.cdn_resources.<a href="./src/gcore/resources/cdn/cdn_resources/cdn_resources.py">list</a>(\*\*<a href="src/gcore/types/cdn/cdn_resource_list_params.py">params</a>) -> <a href="./src/gcore/types/cdn/cdn_resource_list.py">CDNResourceList</a></code>
- <code title="delete /cdn/resources/{resource_id}">client.cdn.cdn_resources.<a href="./src/gcore/resources/cdn/cdn_resources/cdn_resources.py">delete</a>(resource_id) -> None</code>
- <code title="get /cdn/resources/{resource_id}">client.cdn.cdn_resources.<a href="./src/gcore/resources/cdn/cdn_resources/cdn_resources.py">get</a>(resource_id) -> <a href="./src/gcore/types/cdn/cdn_resource.py">CDNResource</a></code>
- <code title="post /cdn/resources/{resource_id}/prefetch">client.cdn.cdn_resources.<a href="./src/gcore/resources/cdn/cdn_resources/cdn_resources.py">prefetch</a>(resource_id, \*\*<a href="src/gcore/types/cdn/cdn_resource_prefetch_params.py">params</a>) -> None</code>
- <code title="post /cdn/resources/{resource_id}/ssl/le/pre-validate">client.cdn.cdn_resources.<a href="./src/gcore/resources/cdn/cdn_resources/cdn_resources.py">prevalidate_ssl_le_certificate</a>(resource_id) -> None</code>
- <code title="post /cdn/resources/{resource_id}/purge">client.cdn.cdn_resources.<a href="./src/gcore/resources/cdn/cdn_resources/cdn_resources.py">purge</a>(resource_id, \*\*<a href="src/gcore/types/cdn/cdn_resource_purge_params.py">params</a>) -> None</code>
- <code title="put /cdn/resources/{resource_id}">client.cdn.cdn_resources.<a href="./src/gcore/resources/cdn/cdn_resources/cdn_resources.py">replace</a>(resource_id, \*\*<a href="src/gcore/types/cdn/cdn_resource_replace_params.py">params</a>) -> <a href="./src/gcore/types/cdn/cdn_resource.py">CDNResource</a></code>

### Shield

Types:

```python
from gcore.types.cdn.cdn_resources import OriginShielding, OriginShieldingReplaced
```

Methods:

- <code title="get /cdn/resources/{resource_id}/shielding_v2">client.cdn.cdn_resources.shield.<a href="./src/gcore/resources/cdn/cdn_resources/shield.py">get</a>(resource_id) -> <a href="./src/gcore/types/cdn/cdn_resources/origin_shielding.py">OriginShielding</a></code>
- <code title="put /cdn/resources/{resource_id}/shielding_v2">client.cdn.cdn_resources.shield.<a href="./src/gcore/resources/cdn/cdn_resources/shield.py">replace</a>(resource_id, \*\*<a href="src/gcore/types/cdn/cdn_resources/shield_replace_params.py">params</a>) -> <a href="./src/gcore/types/cdn/cdn_resources/origin_shielding_replaced.py">object</a></code>

### Rules

Types:

```python
from gcore.types.cdn.cdn_resources import CDNResourceRule, RuleListResponse
```

Methods:

- <code title="post /cdn/resources/{resource_id}/rules">client.cdn.cdn_resources.rules.<a href="./src/gcore/resources/cdn/cdn_resources/rules.py">create</a>(resource_id, \*\*<a href="src/gcore/types/cdn/cdn_resources/rule_create_params.py">params</a>) -> <a href="./src/gcore/types/cdn/cdn_resources/cdn_resource_rule.py">CDNResourceRule</a></code>
- <code title="patch /cdn/resources/{resource_id}/rules/{rule_id}">client.cdn.cdn_resources.rules.<a href="./src/gcore/resources/cdn/cdn_resources/rules.py">update</a>(rule_id, \*, resource_id, \*\*<a href="src/gcore/types/cdn/cdn_resources/rule_update_params.py">params</a>) -> <a href="./src/gcore/types/cdn/cdn_resources/cdn_resource_rule.py">CDNResourceRule</a></code>
- <code title="get /cdn/resources/{resource_id}/rules">client.cdn.cdn_resources.rules.<a href="./src/gcore/resources/cdn/cdn_resources/rules.py">list</a>(resource_id) -> <a href="./src/gcore/types/cdn/cdn_resources/rule_list_response.py">RuleListResponse</a></code>
- <code title="delete /cdn/resources/{resource_id}/rules/{rule_id}">client.cdn.cdn_resources.rules.<a href="./src/gcore/resources/cdn/cdn_resources/rules.py">delete</a>(rule_id, \*, resource_id) -> None</code>
- <code title="get /cdn/resources/{resource_id}/rules/{rule_id}">client.cdn.cdn_resources.rules.<a href="./src/gcore/resources/cdn/cdn_resources/rules.py">get</a>(rule_id, \*, resource_id) -> <a href="./src/gcore/types/cdn/cdn_resources/cdn_resource_rule.py">CDNResourceRule</a></code>
- <code title="put /cdn/resources/{resource_id}/rules/{rule_id}">client.cdn.cdn_resources.rules.<a href="./src/gcore/resources/cdn/cdn_resources/rules.py">replace</a>(rule_id, \*, resource_id, \*\*<a href="src/gcore/types/cdn/cdn_resources/rule_replace_params.py">params</a>) -> <a href="./src/gcore/types/cdn/cdn_resources/cdn_resource_rule.py">CDNResourceRule</a></code>

## Shields

Types:

```python
from gcore.types.cdn import ShieldListResponse
```

Methods:

- <code title="get /cdn/shieldingpop_v2">client.cdn.shields.<a href="./src/gcore/resources/cdn/shields.py">list</a>() -> <a href="./src/gcore/types/cdn/shield_list_response.py">ShieldListResponse</a></code>

## OriginGroups

Types:

```python
from gcore.types.cdn import OriginGroups, OriginGroupsList
```

Methods:

- <code title="post /cdn/origin_groups">client.cdn.origin_groups.<a href="./src/gcore/resources/cdn/origin_groups.py">create</a>(\*\*<a href="src/gcore/types/cdn/origin_group_create_params.py">params</a>) -> <a href="./src/gcore/types/cdn/origin_groups.py">OriginGroups</a></code>
- <code title="patch /cdn/origin_groups/{origin_group_id}">client.cdn.origin_groups.<a href="./src/gcore/resources/cdn/origin_groups.py">update</a>(origin_group_id, \*\*<a href="src/gcore/types/cdn/origin_group_update_params.py">params</a>) -> <a href="./src/gcore/types/cdn/origin_groups.py">OriginGroups</a></code>
- <code title="get /cdn/origin_groups">client.cdn.origin_groups.<a href="./src/gcore/resources/cdn/origin_groups.py">list</a>(\*\*<a href="src/gcore/types/cdn/origin_group_list_params.py">params</a>) -> <a href="./src/gcore/types/cdn/origin_groups_list.py">OriginGroupsList</a></code>
- <code title="delete /cdn/origin_groups/{origin_group_id}">client.cdn.origin_groups.<a href="./src/gcore/resources/cdn/origin_groups.py">delete</a>(origin_group_id) -> None</code>
- <code title="get /cdn/origin_groups/{origin_group_id}">client.cdn.origin_groups.<a href="./src/gcore/resources/cdn/origin_groups.py">get</a>(origin_group_id) -> <a href="./src/gcore/types/cdn/origin_groups.py">OriginGroups</a></code>
- <code title="put /cdn/origin_groups/{origin_group_id}">client.cdn.origin_groups.<a href="./src/gcore/resources/cdn/origin_groups.py">replace</a>(origin_group_id, \*\*<a href="src/gcore/types/cdn/origin_group_replace_params.py">params</a>) -> <a href="./src/gcore/types/cdn/origin_groups.py">OriginGroups</a></code>

## RuleTemplates

Types:

```python
from gcore.types.cdn import RuleTemplate, RuleTemplateList
```

Methods:

- <code title="post /cdn/resources/rule_templates">client.cdn.rule_templates.<a href="./src/gcore/resources/cdn/rule_templates.py">create</a>(\*\*<a href="src/gcore/types/cdn/rule_template_create_params.py">params</a>) -> <a href="./src/gcore/types/cdn/rule_template.py">RuleTemplate</a></code>
- <code title="patch /cdn/resources/rule_templates/{rule_template_id}">client.cdn.rule_templates.<a href="./src/gcore/resources/cdn/rule_templates.py">update</a>(rule_template_id, \*\*<a href="src/gcore/types/cdn/rule_template_update_params.py">params</a>) -> <a href="./src/gcore/types/cdn/rule_template.py">RuleTemplate</a></code>
- <code title="get /cdn/resources/rule_templates">client.cdn.rule_templates.<a href="./src/gcore/resources/cdn/rule_templates.py">list</a>() -> <a href="./src/gcore/types/cdn/rule_template_list.py">RuleTemplateList</a></code>
- <code title="delete /cdn/resources/rule_templates/{rule_template_id}">client.cdn.rule_templates.<a href="./src/gcore/resources/cdn/rule_templates.py">delete</a>(rule_template_id) -> None</code>
- <code title="get /cdn/resources/rule_templates/{rule_template_id}">client.cdn.rule_templates.<a href="./src/gcore/resources/cdn/rule_templates.py">get</a>(rule_template_id) -> <a href="./src/gcore/types/cdn/rule_template.py">RuleTemplate</a></code>
- <code title="put /cdn/resources/rule_templates/{rule_template_id}">client.cdn.rule_templates.<a href="./src/gcore/resources/cdn/rule_templates.py">replace</a>(rule_template_id, \*\*<a href="src/gcore/types/cdn/rule_template_replace_params.py">params</a>) -> <a href="./src/gcore/types/cdn/rule_template.py">RuleTemplate</a></code>

## Certificates

Types:

```python
from gcore.types.cdn import SslDetail, SslDetailList, SslRequestStatus
```

Methods:

- <code title="post /cdn/sslData">client.cdn.certificates.<a href="./src/gcore/resources/cdn/certificates.py">create</a>(\*\*<a href="src/gcore/types/cdn/certificate_create_params.py">params</a>) -> None</code>
- <code title="get /cdn/sslData">client.cdn.certificates.<a href="./src/gcore/resources/cdn/certificates.py">list</a>(\*\*<a href="src/gcore/types/cdn/certificate_list_params.py">params</a>) -> <a href="./src/gcore/types/cdn/ssl_detail_list.py">SslDetailList</a></code>
- <code title="delete /cdn/sslData/{ssl_id}">client.cdn.certificates.<a href="./src/gcore/resources/cdn/certificates.py">delete</a>(ssl_id) -> None</code>
- <code title="post /cdn/sslData/{cert_id}/force-retry">client.cdn.certificates.<a href="./src/gcore/resources/cdn/certificates.py">force_retry</a>(cert_id) -> None</code>
- <code title="get /cdn/sslData/{ssl_id}">client.cdn.certificates.<a href="./src/gcore/resources/cdn/certificates.py">get</a>(ssl_id) -> <a href="./src/gcore/types/cdn/ssl_detail.py">SslDetail</a></code>
- <code title="get /cdn/sslData/{cert_id}/status">client.cdn.certificates.<a href="./src/gcore/resources/cdn/certificates.py">get_status</a>(cert_id, \*\*<a href="src/gcore/types/cdn/certificate_get_status_params.py">params</a>) -> <a href="./src/gcore/types/cdn/ssl_request_status.py">SslRequestStatus</a></code>
- <code title="post /cdn/sslData/{cert_id}/renew">client.cdn.certificates.<a href="./src/gcore/resources/cdn/certificates.py">renew</a>(cert_id) -> None</code>
- <code title="put /cdn/sslData/{ssl_id}">client.cdn.certificates.<a href="./src/gcore/resources/cdn/certificates.py">replace</a>(ssl_id, \*\*<a href="src/gcore/types/cdn/certificate_replace_params.py">params</a>) -> <a href="./src/gcore/types/cdn/ssl_detail.py">SslDetail</a></code>

## TrustedCaCertificates

Types:

```python
from gcore.types.cdn import CaCertificate, CaCertificateList
```

Methods:

- <code title="post /cdn/sslCertificates">client.cdn.trusted_ca_certificates.<a href="./src/gcore/resources/cdn/trusted_ca_certificates.py">create</a>(\*\*<a href="src/gcore/types/cdn/trusted_ca_certificate_create_params.py">params</a>) -> <a href="./src/gcore/types/cdn/ca_certificate.py">CaCertificate</a></code>
- <code title="get /cdn/sslCertificates">client.cdn.trusted_ca_certificates.<a href="./src/gcore/resources/cdn/trusted_ca_certificates.py">list</a>(\*\*<a href="src/gcore/types/cdn/trusted_ca_certificate_list_params.py">params</a>) -> <a href="./src/gcore/types/cdn/ca_certificate_list.py">CaCertificateList</a></code>
- <code title="delete /cdn/sslCertificates/{id}">client.cdn.trusted_ca_certificates.<a href="./src/gcore/resources/cdn/trusted_ca_certificates.py">delete</a>(id) -> None</code>
- <code title="get /cdn/sslCertificates/{id}">client.cdn.trusted_ca_certificates.<a href="./src/gcore/resources/cdn/trusted_ca_certificates.py">get</a>(id) -> <a href="./src/gcore/types/cdn/ca_certificate.py">CaCertificate</a></code>
- <code title="put /cdn/sslCertificates/{id}">client.cdn.trusted_ca_certificates.<a href="./src/gcore/resources/cdn/trusted_ca_certificates.py">replace</a>(id, \*\*<a href="src/gcore/types/cdn/trusted_ca_certificate_replace_params.py">params</a>) -> <a href="./src/gcore/types/cdn/ca_certificate.py">CaCertificate</a></code>

## AuditLogs

Types:

```python
from gcore.types.cdn import CDNAuditLogEntry
```

Methods:

- <code title="get /cdn/activity_log/requests">client.cdn.audit_logs.<a href="./src/gcore/resources/cdn/audit_logs.py">list</a>(\*\*<a href="src/gcore/types/cdn/audit_log_list_params.py">params</a>) -> <a href="./src/gcore/types/cdn/cdn_audit_log_entry.py">SyncOffsetPage[CDNAuditLogEntry]</a></code>
- <code title="get /cdn/activity_log/requests/{log_id}">client.cdn.audit_logs.<a href="./src/gcore/resources/cdn/audit_logs.py">get</a>(log_id) -> <a href="./src/gcore/types/cdn/cdn_audit_log_entry.py">CDNAuditLogEntry</a></code>

## Logs

Types:

```python
from gcore.types.cdn import CDNLogEntry
```

Methods:

- <code title="get /cdn/advanced/v1/logs">client.cdn.logs.<a href="./src/gcore/resources/cdn/logs.py">list</a>(\*\*<a href="src/gcore/types/cdn/log_list_params.py">params</a>) -> SyncOffsetPageCDNLogs[Data]</code>
- <code title="get /cdn/advanced/v1/logs/download">client.cdn.logs.<a href="./src/gcore/resources/cdn/logs.py">download</a>(\*\*<a href="src/gcore/types/cdn/log_download_params.py">params</a>) -> BinaryAPIResponse</code>

## LogsUploader

Types:

```python
from gcore.types.cdn import LogsUploaderValidation
```

### Policies

Types:

```python
from gcore.types.cdn.logs_uploader import (
    LogsUploaderPolicy,
    LogsUploaderPolicyList,
    PolicyListFieldsResponse,
)
```

Methods:

- <code title="post /cdn/logs_uploader/policies">client.cdn.logs_uploader.policies.<a href="./src/gcore/resources/cdn/logs_uploader/policies.py">create</a>(\*\*<a href="src/gcore/types/cdn/logs_uploader/policy_create_params.py">params</a>) -> <a href="./src/gcore/types/cdn/logs_uploader/logs_uploader_policy.py">LogsUploaderPolicy</a></code>
- <code title="patch /cdn/logs_uploader/policies/{id}">client.cdn.logs_uploader.policies.<a href="./src/gcore/resources/cdn/logs_uploader/policies.py">update</a>(id, \*\*<a href="src/gcore/types/cdn/logs_uploader/policy_update_params.py">params</a>) -> <a href="./src/gcore/types/cdn/logs_uploader/logs_uploader_policy.py">LogsUploaderPolicy</a></code>
- <code title="get /cdn/logs_uploader/policies">client.cdn.logs_uploader.policies.<a href="./src/gcore/resources/cdn/logs_uploader/policies.py">list</a>(\*\*<a href="src/gcore/types/cdn/logs_uploader/policy_list_params.py">params</a>) -> <a href="./src/gcore/types/cdn/logs_uploader/logs_uploader_policy_list.py">LogsUploaderPolicyList</a></code>
- <code title="delete /cdn/logs_uploader/policies/{id}">client.cdn.logs_uploader.policies.<a href="./src/gcore/resources/cdn/logs_uploader/policies.py">delete</a>(id) -> None</code>
- <code title="get /cdn/logs_uploader/policies/{id}">client.cdn.logs_uploader.policies.<a href="./src/gcore/resources/cdn/logs_uploader/policies.py">get</a>(id) -> <a href="./src/gcore/types/cdn/logs_uploader/logs_uploader_policy.py">LogsUploaderPolicy</a></code>
- <code title="get /cdn/logs_uploader/policies/fields">client.cdn.logs_uploader.policies.<a href="./src/gcore/resources/cdn/logs_uploader/policies.py">list_fields</a>() -> <a href="./src/gcore/types/cdn/logs_uploader/policy_list_fields_response.py">PolicyListFieldsResponse</a></code>
- <code title="put /cdn/logs_uploader/policies/{id}">client.cdn.logs_uploader.policies.<a href="./src/gcore/resources/cdn/logs_uploader/policies.py">replace</a>(id, \*\*<a href="src/gcore/types/cdn/logs_uploader/policy_replace_params.py">params</a>) -> <a href="./src/gcore/types/cdn/logs_uploader/logs_uploader_policy.py">LogsUploaderPolicy</a></code>

### Targets

Types:

```python
from gcore.types.cdn.logs_uploader import LogsUploaderTarget, LogsUploaderTargetList
```

Methods:

- <code title="post /cdn/logs_uploader/targets">client.cdn.logs_uploader.targets.<a href="./src/gcore/resources/cdn/logs_uploader/targets.py">create</a>(\*\*<a href="src/gcore/types/cdn/logs_uploader/target_create_params.py">params</a>) -> <a href="./src/gcore/types/cdn/logs_uploader/logs_uploader_target.py">LogsUploaderTarget</a></code>
- <code title="patch /cdn/logs_uploader/targets/{id}">client.cdn.logs_uploader.targets.<a href="./src/gcore/resources/cdn/logs_uploader/targets.py">update</a>(id, \*\*<a href="src/gcore/types/cdn/logs_uploader/target_update_params.py">params</a>) -> <a href="./src/gcore/types/cdn/logs_uploader/logs_uploader_target.py">LogsUploaderTarget</a></code>
- <code title="get /cdn/logs_uploader/targets">client.cdn.logs_uploader.targets.<a href="./src/gcore/resources/cdn/logs_uploader/targets.py">list</a>(\*\*<a href="src/gcore/types/cdn/logs_uploader/target_list_params.py">params</a>) -> <a href="./src/gcore/types/cdn/logs_uploader/logs_uploader_target_list.py">LogsUploaderTargetList</a></code>
- <code title="delete /cdn/logs_uploader/targets/{id}">client.cdn.logs_uploader.targets.<a href="./src/gcore/resources/cdn/logs_uploader/targets.py">delete</a>(id) -> None</code>
- <code title="get /cdn/logs_uploader/targets/{id}">client.cdn.logs_uploader.targets.<a href="./src/gcore/resources/cdn/logs_uploader/targets.py">get</a>(id) -> <a href="./src/gcore/types/cdn/logs_uploader/logs_uploader_target.py">LogsUploaderTarget</a></code>
- <code title="put /cdn/logs_uploader/targets/{id}">client.cdn.logs_uploader.targets.<a href="./src/gcore/resources/cdn/logs_uploader/targets.py">replace</a>(id, \*\*<a href="src/gcore/types/cdn/logs_uploader/target_replace_params.py">params</a>) -> <a href="./src/gcore/types/cdn/logs_uploader/logs_uploader_target.py">LogsUploaderTarget</a></code>
- <code title="post /cdn/logs_uploader/targets/{id}/validate">client.cdn.logs_uploader.targets.<a href="./src/gcore/resources/cdn/logs_uploader/targets.py">validate</a>(id) -> <a href="./src/gcore/types/cdn/logs_uploader_validation.py">LogsUploaderValidation</a></code>

### Configs

Types:

```python
from gcore.types.cdn.logs_uploader import LogsUploaderConfig, LogsUploaderConfigList
```

Methods:

- <code title="post /cdn/logs_uploader/configs">client.cdn.logs_uploader.configs.<a href="./src/gcore/resources/cdn/logs_uploader/configs.py">create</a>(\*\*<a href="src/gcore/types/cdn/logs_uploader/config_create_params.py">params</a>) -> <a href="./src/gcore/types/cdn/logs_uploader/logs_uploader_config.py">LogsUploaderConfig</a></code>
- <code title="patch /cdn/logs_uploader/configs/{id}">client.cdn.logs_uploader.configs.<a href="./src/gcore/resources/cdn/logs_uploader/configs.py">update</a>(id, \*\*<a href="src/gcore/types/cdn/logs_uploader/config_update_params.py">params</a>) -> <a href="./src/gcore/types/cdn/logs_uploader/logs_uploader_config.py">LogsUploaderConfig</a></code>
- <code title="get /cdn/logs_uploader/configs">client.cdn.logs_uploader.configs.<a href="./src/gcore/resources/cdn/logs_uploader/configs.py">list</a>(\*\*<a href="src/gcore/types/cdn/logs_uploader/config_list_params.py">params</a>) -> <a href="./src/gcore/types/cdn/logs_uploader/logs_uploader_config_list.py">LogsUploaderConfigList</a></code>
- <code title="delete /cdn/logs_uploader/configs/{id}">client.cdn.logs_uploader.configs.<a href="./src/gcore/resources/cdn/logs_uploader/configs.py">delete</a>(id) -> None</code>
- <code title="get /cdn/logs_uploader/configs/{id}">client.cdn.logs_uploader.configs.<a href="./src/gcore/resources/cdn/logs_uploader/configs.py">get</a>(id) -> <a href="./src/gcore/types/cdn/logs_uploader/logs_uploader_config.py">LogsUploaderConfig</a></code>
- <code title="put /cdn/logs_uploader/configs/{id}">client.cdn.logs_uploader.configs.<a href="./src/gcore/resources/cdn/logs_uploader/configs.py">replace</a>(id, \*\*<a href="src/gcore/types/cdn/logs_uploader/config_replace_params.py">params</a>) -> <a href="./src/gcore/types/cdn/logs_uploader/logs_uploader_config.py">LogsUploaderConfig</a></code>
- <code title="post /cdn/logs_uploader/configs/{id}/validate">client.cdn.logs_uploader.configs.<a href="./src/gcore/resources/cdn/logs_uploader/configs.py">validate</a>(id) -> <a href="./src/gcore/types/cdn/logs_uploader_validation.py">LogsUploaderValidation</a></code>

## Statistics

Types:

```python
from gcore.types.cdn import (
    LogsAggregatedStats,
    ResourceAggregatedStats,
    ResourceUsageStats,
    ShieldAggregatedStats,
    UsageSeriesStats,
)
```

Methods:

- <code title="get /cdn/statistics/raw_logs_usage/aggregated">client.cdn.statistics.<a href="./src/gcore/resources/cdn/statistics.py">get_logs_usage_aggregated</a>(\*\*<a href="src/gcore/types/cdn/statistic_get_logs_usage_aggregated_params.py">params</a>) -> <a href="./src/gcore/types/cdn/logs_aggregated_stats.py">LogsAggregatedStats</a></code>
- <code title="get /cdn/statistics/raw_logs_usage/series">client.cdn.statistics.<a href="./src/gcore/resources/cdn/statistics.py">get_logs_usage_series</a>(\*\*<a href="src/gcore/types/cdn/statistic_get_logs_usage_series_params.py">params</a>) -> <a href="./src/gcore/types/cdn/usage_series_stats.py">UsageSeriesStats</a></code>
- <code title="get /cdn/statistics/aggregate/stats">client.cdn.statistics.<a href="./src/gcore/resources/cdn/statistics.py">get_resource_usage_aggregated</a>(\*\*<a href="src/gcore/types/cdn/statistic_get_resource_usage_aggregated_params.py">params</a>) -> <a href="./src/gcore/types/cdn/resource_aggregated_stats.py">ResourceAggregatedStats</a></code>
- <code title="get /cdn/statistics/series">client.cdn.statistics.<a href="./src/gcore/resources/cdn/statistics.py">get_resource_usage_series</a>(\*\*<a href="src/gcore/types/cdn/statistic_get_resource_usage_series_params.py">params</a>) -> <a href="./src/gcore/types/cdn/resource_usage_stats.py">ResourceUsageStats</a></code>
- <code title="get /cdn/statistics/shield_usage/aggregated">client.cdn.statistics.<a href="./src/gcore/resources/cdn/statistics.py">get_shield_usage_aggregated</a>(\*\*<a href="src/gcore/types/cdn/statistic_get_shield_usage_aggregated_params.py">params</a>) -> <a href="./src/gcore/types/cdn/shield_aggregated_stats.py">ShieldAggregatedStats</a></code>
- <code title="get /cdn/statistics/shield_usage/series">client.cdn.statistics.<a href="./src/gcore/resources/cdn/statistics.py">get_shield_usage_series</a>(\*\*<a href="src/gcore/types/cdn/statistic_get_shield_usage_series_params.py">params</a>) -> <a href="./src/gcore/types/cdn/usage_series_stats.py">UsageSeriesStats</a></code>

## NetworkCapacity

Types:

```python
from gcore.types.cdn import NetworkCapacity
```

Methods:

- <code title="get /cdn/advanced/v1/capacity">client.cdn.network_capacity.<a href="./src/gcore/resources/cdn/network_capacity.py">list</a>() -> <a href="./src/gcore/types/cdn/network_capacity.py">NetworkCapacity</a></code>

## Metrics

Types:

```python
from gcore.types.cdn import CDNMetrics, CDNMetricsGroups, CDNMetricsValues
```

Methods:

- <code title="post /cdn/advanced/v1/metrics">client.cdn.metrics.<a href="./src/gcore/resources/cdn/metrics.py">list</a>(\*\*<a href="src/gcore/types/cdn/metric_list_params.py">params</a>) -> <a href="./src/gcore/types/cdn/cdn_metrics.py">CDNMetrics</a></code>

## IPRanges

Types:

```python
from gcore.types.cdn import PublicIPList, PublicNetworkList
```

Methods:

- <code title="get /cdn/public-net-list">client.cdn.ip_ranges.<a href="./src/gcore/resources/cdn/ip_ranges.py">list</a>(\*\*<a href="src/gcore/types/cdn/ip_range_list_params.py">params</a>) -> <a href="./src/gcore/types/cdn/public_network_list.py">PublicNetworkList</a></code>
- <code title="get /cdn/public-ip-list">client.cdn.ip_ranges.<a href="./src/gcore/resources/cdn/ip_ranges.py">list_ips</a>(\*\*<a href="src/gcore/types/cdn/ip_range_list_ips_params.py">params</a>) -> <a href="./src/gcore/types/cdn/public_ip_list.py">PublicIPList</a></code>
