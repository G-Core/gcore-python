# Release Notes Examples

Real examples from this repository showing the target format. Use these as
style references when generating human-readable release notes (Part 1).

## Example 1: v0.32.0 (multiple product areas, grouped breaking changes)

```markdown
We're excited to announce version 0.32.0!

### **CDN**

* **CDN Resources**
  * ⚠ BREAKING CHANGE: `CDNResourceCreateParams` fields `origin` and `origin_group` are now optional — exactly one must be provided

* **Logs Uploader**
  * Added `endpoint` field to S3 OSS config — custom S3 endpoint now supported in `LogsUploaderTarget` and related params

### **Cloud**

* **Load Balancers**
  * ⚠ BREAKING CHANGE: `secret_id` in listener create params changed type for correct enum handling
  * Added `admin_state_up` field across all load balancer, listener, pool, and health monitor response and param types
  * Fixed `secret_id` type mismatch in `listeners.create_and_poll()` — aligned to `Literal[""]` to match `create()` signature

* **Managed Kubernetes**
  * ⚠ BREAKING CHANGE: `K8sClusterKubeconfig.created_at` and `expires_at` changed from nullable to required
  * Added `include_capacity` param to `K8sFlavorListParams` for flavor capacity info
  * Added `CLUSTER_REBUILD` and `CLUSTER_SERVER_REBUILD` task states

### **FastEdge**

* ⚠ BREAKING CHANGE: Edge Storage API changes
  * `App.stores` changed from `Dict[str, int]` to `Dict[str, AppStore]` — stores now carry `id`, `name`, and `comment`
  * `KvStore` restructured — `id` removed, `name` is now the primary identifier, `updated` renamed to `updated_at`, `revision` and `size` added
  * `kv_stores.new()` and `kv_stores.get()` now return `KvStoreCreateResponse` and `KvStore`
  * Removed `KvStoreStats`, `KvStoreGetResponse`, and the `app_limit`, `daily_limit`, `hourly_limit` fields from `Client`
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
  * ⚠ BREAKING CHANGE: Renamed types and services for consistent Python naming
    * All `Cdn*` types are now `CDN*` (for example, `CdnResource` is now `CDNResource`)
    * The `resources` service is now `cdn_resources` — use `client.cdn.cdn_resources` instead of `client.cdn.resources`

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
  * ⚠ BREAKING CHANGE: `update()` migrated to the v2 API endpoint
    * Now uses `/v2/floatingips/` and returns `TaskIDList` instead of `FloatingIP`
    * New `port_id` and `fixed_ip_address` params replace the deprecated `assign()` method
  * Added `update_and_poll()` method - updates a floating IP and waits for the operation to complete, returns `FloatingIP`

* **Security Groups**
  * ⚠ BREAKING CHANGE: Security groups migrated to v2 API endpoints
    * `create()` and `update()` now use `/v2/security_groups/` and return `TaskIDList` instead of `SecurityGroup`
    * `create()` takes `name`, `description`, `rules`, and `tags` as top-level params; the nested `security_group` wrapper and the `instances` param are removed
    * `update()` uses declarative `rules` instead of `changed_rules` and accepts `description`
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
5. **Breaking changes**: One `⚠ BREAKING CHANGE:` bullet per sub-area with a short summary; details go in nested bullets without the prefix. Include old type/value -> new type/value. Never repeat the prefix on each bullet
6. **Deprecations**: Use format ``Deprecated `method()` — use `alternative()` instead``
7. **New fields/methods**: Use format ``Added `field_name` field to `TypeName` — description``
8. **Fixes**: Use format `Fixed {what} — {detail}`
9. **Type references**: Always use backtick-wrapped Python identifiers (e.g., `Optional[str]`, `Dict[str, int]`, `CDNResource`)
10. **Method references**: Use `snake_case` for methods (e.g., `create_and_poll()`, `get_traffic_series()`)
11. **Descriptions**: Short, specific, user-actionable. No commit hashes in Part 1.
12. **Product area order**: Alphabetical. Place "Other" last.
13. **Sub-area order**: Alphabetical within each product area.

## Breaking Changes Example

Preferred (one marker, nested details, few identifiers):

```markdown
* **Users**
  * ⚠ BREAKING CHANGE: User methods and response models now follow the IAM v2 API
    * `get()` now returns `User` instead of `UserGetResponse`
    * `update()` now returns `UserUpdated` instead of `User`
  * Added `get_me()` — returns the authenticated user's profile, clients, and roles
```

Avoid (prefix on every bullet, too many types):

```markdown
* **Users**
  * ⚠ BREAKING CHANGE: `get()` now returns `User` instead of `UserGetResponse`
  * ⚠ BREAKING CHANGE: `update()` now returns `UserUpdated` instead of `User`
  * ⚠ BREAKING CHANGE: Removed `UserGetResponse`, `UserStats`, and `UserLimits` types
```
