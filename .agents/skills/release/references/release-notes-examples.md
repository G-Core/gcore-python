# Release Notes Examples

Real examples from this repository showing the target format. Use these as
style references when generating human-readable release notes (Part 1).

## Example 1: v0.32.0 (multiple product areas, breaking changes inline)

```markdown
We're excited to announce version 0.32.0!

### **CDN**

* **CDN Resources**
  * ⚠ BREAKING CHANGE: `origin` in `CDNResourceCreateParams` changed from required `str` to optional — exactly one of `origin` or `origin_group` must be provided
  * ⚠ BREAKING CHANGE: `origin_group` in `CDNResourceCreateParams` changed from required `int` to optional

* **Logs Uploader**
  * Added `endpoint` field to S3 OSS config — custom S3 endpoint now supported in `LogsUploaderTarget` and related params

### **Cloud**

* **Load Balancers**
  * Added `admin_state_up` field across all load balancer, listener, pool, and health monitor response and param types
  * ⚠ BREAKING CHANGE: `secret_id` in listener create params changed type for correct enum handling
  * Fixed `secret_id` type mismatch in `listeners.create_and_poll()` — aligned to `Literal[""]` to match `create()` signature

* **Managed Kubernetes**
  * Added `include_capacity` param to `K8sFlavorListParams` for flavor capacity info
  * Added `CLUSTER_REBUILD` and `CLUSTER_SERVER_REBUILD` task states
  * ⚠ BREAKING CHANGE: `K8sClusterKubeconfig.created_at` and `expires_at` changed from nullable to required

### **FastEdge**

* ⚠ BREAKING CHANGE: `App.stores` type changed from `Dict[str, int]` to `Dict[str, AppStore]` — stores now carry `id`, `name`, and `comment`
* ⚠ BREAKING CHANGE: `KvStore` response restructured — `id` field removed, `name` is now primary identifier, `updated` renamed to `updated_at`, added `revision` and `size` fields
* ⚠ BREAKING CHANGE: `kv_stores.new()` return type changed from `KvStore` to `KvStoreCreateResponse`
* ⚠ BREAKING CHANGE: `kv_stores.get()` return type changed from `KvStoreGetResponse` to `KvStore`
* ⚠ BREAKING CHANGE: Removed `KvStoreStats` and `KvStoreGetResponse` types
* ⚠ BREAKING CHANGE: Removed `app_limit`, `daily_limit`, `hourly_limit` fields from `Client` type
* Renamed "KV Storage" to "Edge Storage" across all endpoints
* Added `store` as new `TemplateParameterDataType` enum value

### **WAAP**

* **Analytics**
  * Added `decision` and `optional_action` fields to `WaapRequestDetails` and `WaapRequestSummary`
  * Added `domain_id` field to `WaapRequestSummary`
  * Deprecated `domain_statistics.get_traffic_series()` — use `GET /v1/analytics/traffic` instead

### **Other**

* Fixed lint compatibility with Python 3.14
```

## Example 2: v0.31.0 (breaking renames, SDK improvements)

```markdown
We're excited to announce version 0.31.0!

### **CDN**

* **API Naming**
  * ⚠ BREAKING CHANGE: Renamed all `Cdn*` types to `CDN*` for consistent Python naming conventions - `CdnResource` is now `CDNResource`, `CdnAccount` is now `CDNAccount`, `CdnAccountLimits` is now `CDNAccountLimits`, etc.
  * ⚠ BREAKING CHANGE: Renamed `resources` service to `cdn_resources` - access CDN resources via `client.cdn.cdn_resources` instead of `client.cdn.resources`

* **User-Agent ACL**
  * Added regex pattern support - you can now use regular expressions in User-Agent ACL rules with `~` (case-sensitive) or `~*` (case-insensitive) prefix

### **WAAP**

* **Analytics**
  * Deprecated `get_requests_series()` method - use the new `/v1/analytics/requests` endpoint instead
  * Updated action filter values - changed from "block", "captcha", "handshake", "monitor" to "allow", "block", "captcha", "handshake"

### **Other**

* Added custom JSON encoder for extended type support - automatically handles `datetime` objects and `pydantic.BaseModel` instances when serializing request bodies
```

## Example 3: v0.30.0 (Cloud-focused, v2 API migrations)

```markdown
We're excited to announce version 0.30.0!

### **Cloud**

* **Floating IPs**
  * ⚠ BREAKING CHANGE: Migrated `update()` to v2 API endpoint - now uses `/v2/floatingips/` and returns `TaskIDList` instead of `FloatingIP`
  * ⚠ BREAKING CHANGE: Added `port_id` and `fixed_ip_address` parameters to `update()` - use these for assignment operations instead of the deprecated `assign()` method
  * Added `update_and_poll()` method - updates a floating IP and waits for the operation to complete, returns `FloatingIP`

* **Security Groups**
  * ⚠ BREAKING CHANGE: Migrated to v2 API endpoints - `create()` and `update()` methods now use `/v2/security_groups/` endpoints and return `TaskIDList` instead of `SecurityGroup`
  * ⚠ BREAKING CHANGE: Simplified `create()` parameters - `name`, `description`, `rules`, and `tags` are now top-level parameters; removed nested `security_group` wrapper
  * ⚠ BREAKING CHANGE: Removed `instances` parameter from `create()` - use dedicated instance methods to assign security groups to instances
  * ⚠ BREAKING CHANGE: Changed `update()` to use declarative rules - `changed_rules` replaced with `rules` parameter; specify the complete desired state instead of create/delete actions
  * ⚠ BREAKING CHANGE: Added `description` parameter to `update()` - can now update security group description
  * Added `create_and_poll()` method - creates a security group and waits for the operation to complete, returns `SecurityGroup`
  * Added `update_and_poll()` method - updates a security group and waits for the operation to complete, returns `SecurityGroup`

* **Tasks**
  * Added `update_floating_ip` and `update_router` task types to `task_type` filter - filter tasks by these new operation types in `list()` method
```

## Style Rules (inferred from examples)

1. **Opening line**: Always `We're excited to announce version {VERSION}!`
2. **Product area headers**: `### **{Area}**` — bold inside h3
3. **Sub-area items**: `* **{Sub-area}**` — bold bullet, followed by indented child bullets
4. **When a product area has no sub-areas** (e.g., FastEdge above): list items directly under the product header without a sub-area bullet
5. **Breaking changes**: Inline with `⚠ BREAKING CHANGE:` prefix, include old type/value -> new type/value
6. **Deprecations**: Use format ``Deprecated `method()` — use `alternative()` instead``
7. **New fields/methods**: Use format ``Added `field_name` field to `TypeName` — description``
8. **Fixes**: Use format `Fixed {what} — {detail}`
9. **Type references**: Always use backtick-wrapped Python identifiers (e.g., `Optional[str]`, `Dict[str, int]`, `CDNResource`)
10. **Method references**: Use `snake_case` for methods (e.g., `create_and_poll()`, `get_traffic_series()`)
11. **Descriptions**: Short, specific, user-actionable. No commit hashes in Part 1.
12. **Product area order**: Alphabetical. Place "Other" last.
13. **Sub-area order**: Alphabetical within each product area.
