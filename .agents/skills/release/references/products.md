# Gcore Products — Canonical Names & File Path Heuristics

Authoritative list of product and sub-product names for release notes.
Order products alphabetically; place "Other" last. Order sub-products
alphabetically within each product.

## CDN

SDK paths: `resources/cdn/`, `types/cdn/`

| Sub-Product | File patterns |
|---|---|
| Activity Logs | `cdn/audit_logs*` |
| CDN Resources | `cdn/cdn_resources/cdn_resources*` (not rules, not shield) |
| CDN Service | `cdn/cdn.py` (service-level config) |
| IP Ranges | `cdn/ip_ranges*` |
| Logs | `cdn/logs.py`, `cdn/logs/` |
| Logs Uploader | `cdn/logs_uploader/` |
| Metrics | `cdn/metrics*` |
| Network Capacity | `cdn/network_capacity*` |
| Origin Groups | `cdn/origin_groups*` |
| Origin Shielding | `cdn/cdn_resources/shield*` |
| Regions | `cdn/regions/` |
| Rule Templates | `cdn/rule_templates*` |
| Rules | `cdn/cdn_resources/rules*` |
| SSL Certificates | `cdn/certificates*` |
| Statistics | `cdn/statistics*` |
| Trusted CA Certificates | `cdn/trusted_ca_certificates*` |

## Cloud

SDK paths: `resources/cloud/`, `types/cloud/`

| Sub-Product | File patterns |
|---|---|
| Bare Metal | `cloud/baremetal/` |
| Billing Reservations | `cloud/billing_reservations*` |
| Container as a Service | `cloud/containers/` |
| Cost Reports | `cloud/cost_reports*`, `cloud/usage_reports*` |
| Databases | `cloud/databases/` |
| Everywhere Inference | `cloud/inference/` (not `inference/applications/`) |
| Everywhere Inference Apps | `cloud/inference/applications/` |
| File Shares | `cloud/file_shares/` |
| Floating IPs | `cloud/floating_ips*` |
| GPU Bare Metal | `cloud/gpu_baremetal/`, `cloud/gpu_baremetal_clusters/` |
| GPU Virtual | `cloud/gpu_virtual/`, `cloud/gpu_virtual_clusters/` |
| Instances | `cloud/instances/` |
| IP Ranges | `cloud/ip_ranges*` |
| Load Balancers | `cloud/load_balancers/` |
| Managed Kubernetes | `cloud/k8s/` |
| Networks | `cloud/networks/` |
| Placement Groups | `cloud/placement_groups*` |
| Projects | `cloud/projects*` |
| Quotas | `cloud/quotas/` |
| Regions | `cloud/regions*` |
| Registries | `cloud/registries/` |
| Reserved IPs | `cloud/reserved_fixed_ips/` |
| Secrets | `cloud/secrets*` |
| Security Groups | `cloud/security_groups/` |
| SSH Keys | `cloud/ssh_keys*` |
| Tasks | `cloud/tasks*` |
| User Actions | `cloud/audit_logs*` |
| Users | `cloud/users/` |
| Volume Snapshots | `cloud/volume_snapshots*` |
| Volumes | `cloud/volumes*` |

## DDoS Protection

SDK paths: `resources/security/`, `types/security/`

| Sub-Product | File patterns |
|---|---|
| BGP Announces | `security/bgp_announces*` |
| Event Logs | `security/events*` |
| Profiles | `security/profiles*` (not `profile_templates*`) |
| Security Templates | `security/profile_templates*` |

## DNS

SDK paths: `resources/dns/`, `types/dns/`

| Sub-Product | File patterns |
|---|---|
| DNSSEC | `dns/zones/dnssec*` |
| Locations | `dns/locations*` |
| Metrics | `dns/metrics*` |
| Network Mappings | `dns/network_mappings*` |
| Pickers | `dns/pickers/` |
| RRsets | `dns/zones/rrsets*` |
| Zones | `dns/zones/zones*` |

## FastEdge

SDK paths: `resources/fastedge/`, `types/fastedge/`

| Sub-Product | File patterns |
|---|---|
| Apps | `fastedge/apps/` |
| Binaries | `fastedge/binaries*` |
| Edge Storage | `fastedge/kv_stores*` |
| Secrets | `fastedge/secrets*` |
| Statistics | `fastedge/statistics*` |
| Templates | `fastedge/templates*` |

## IAM

SDK paths: `resources/iam/`, `types/iam/`

| Sub-Product | File patterns |
|---|---|
| Account | `iam/iam.py` (service-level auth) |
| API Tokens | `iam/api_tokens*` |
| Users | `iam/users*` |

## Object Storage

SDK paths: `resources/storage/`, `types/storage/`

| Sub-Product | File patterns |
|---|---|
| Buckets | `storage/buckets/buckets*` (not `cors*`, `lifecycle*`, `policy*`) |
| CORS | `storage/buckets/cors*` |
| Credentials | `storage/credentials*` |
| Lifecycle | `storage/buckets/lifecycle*` |
| Locations | `storage/locations*` |
| Policies | `storage/buckets/policy*` |
| Statistics | `storage/statistics*` |

## Streaming

SDK paths: `resources/streaming/`, `types/streaming/`

| Sub-Product | File patterns |
|---|---|
| AI | `streaming/ai_tasks*` |
| Broadcasts | `streaming/broadcasts*` |
| Directories | `streaming/directories*` |
| Overlays | `streaming/streams/overlays*` |
| Players | `streaming/players*` |
| Playlists | `streaming/playlists/` |
| Quality Sets | `streaming/quality_sets*` |
| Restreams | `streaming/restreams*` |
| Statistics | `streaming/statistics*` |
| Streams | `streaming/streams/streams*` |
| Subtitles | `streaming/videos/subtitles*` |
| Videos | `streaming/videos/videos*` |

## WAAP

SDK paths: `resources/waap/`, `types/waap/`

| Sub-Product | File patterns |
|---|---|
| Advanced Rules | `waap/advanced_rules*`, `waap/domains/advanced_rules*` |
| Analytics | `waap/domains/statistics*`, `waap/statistics*`, `waap/domains/analytics/` |
| API Discovery | `waap/domains/api_discovery*`, `waap/domains/api_paths*`, `waap/domains/api_path_groups*` |
| Custom Page Sets | `waap/custom_page_sets*` |
| Custom Rules | `waap/domains/custom_rules*` |
| Domains | `waap/domains/domains*`, `waap/domains/settings*` |
| Firewall Rules | `waap/domains/firewall_rules*` |
| IP Spotlight | `waap/ip_info/` |
| Network Organizations | `waap/organizations*` |
| Security Insights | `waap/domains/insights*`, `waap/insights*`, `waap/domains/insight_silences*` |
| Tags | `waap/tags*` |
| WAAP Service | `waap/waap.py` |

## Other

Changes not specific to any product (SDK internals, utilities, shared code).

| File patterns |
|---|
| `.github/*`, `.stats.yml`, `pyproject.toml`, `requirements*.txt`, `README.md` |
| `_client.py`, `_base_client.py`, `_models.py`, `_streaming.py`, `pagination.py` |
| `_utils/`, `_compat.py`, `_constants.py`, `_exceptions.py`, `_files.py` |
| `lib/`, `_response.py`, `_types.py` |
