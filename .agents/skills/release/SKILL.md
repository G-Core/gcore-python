---
name: release
description: >
  Release workflow for the G-Core/gcore-python SDK repository. Invoke with /release
  to discover the open Stainless release PR, analyze its diff and changelog,
  check CI status, merge with user confirmation, and generate human-readable
  release notes on the GitHub Release.
disable-model-invocation: true
allowed-tools: >
  Read,
  Bash(gh pr list --repo G-Core/gcore-python *),
  Bash(gh pr view * --repo G-Core/gcore-python *),
  Bash(gh pr diff * --repo G-Core/gcore-python *),
  Bash(gh pr checks * --repo G-Core/gcore-python *),
  Bash(gh pr merge * --repo G-Core/gcore-python *),
  Bash(gh release view --repo G-Core/gcore-python *),
  Bash(gh release edit * --repo G-Core/gcore-python *),
  Bash(sleep *)
---

# Release Skill — G-Core/gcore-python

## Constraints

- **Repository**: `G-Core/gcore-python` (hardcoded, do not use for other repos)
- **Allowed tools**: `gh` CLI (scoped to `G-Core/gcore-python`) and `Read`
- **Never**: modify source code, force-push, delete branches, or merge without
  explicit user confirmation
- **Release PRs** are created by `stainless-app[bot]` with title `release: {version}`

## Workflow

Execute steps 1-6 in order. Present findings at each step before proceeding.

### Step 1 — Discover the Release PR

```bash
gh pr list --repo G-Core/gcore-python --state open --app stainless-app \
  --json number,title,author,url,createdAt
```

Find the PR whose title starts with `release: `.

- If **no open release PR** exists, inform the user and stop.
- If found, display: PR number, title (contains version), URL, creation date.

### Step 2 — Analyze the Release

Fetch all three in parallel:

1. PR body containing the auto-generated changelog (Part 2). Parse it to extract:
   - Version number and date
   - Breaking changes, Features, Bug Fixes, Refactors, Chores, Documentation

   ```bash
   gh pr view {N} --repo G-Core/gcore-python --json body,title,number,url
   ```

2. The actual code diff. Analyze for Python API-level changes:
   - New/removed/renamed types, fields, methods
   - Changed field types (e.g., `str` -> `Optional[str]`, `int` -> `Literal[""]`)
   - New service methods (e.g., `create_and_poll()`)
   - Changed return types
   - Note: deprecation warnings (`warnings.warn`, `@deprecated`) are informational
     only — the methods still exist in the SDK. Do **not** surface these as
     user-facing changes in release notes unless the deprecation is new in this
     release AND accompanied by a replacement in the same release.

   ```bash
   gh pr diff {N} --repo G-Core/gcore-python
   ```

3. List of changed files. Use commit scopes and file paths to infer product areas:

   ```bash
   gh pr diff {N} --repo G-Core/gcore-python --name-only
   ```

   | File path prefix | Product Area |
   |---|---|
   | `resources/cdn/`, `types/cdn/` | **CDN** |
   | `resources/cloud/`, `types/cloud/` | **Cloud** |
   | `resources/security/`, `types/security/` | **DDoS Protection** |
   | `resources/dns/`, `types/dns/` | **DNS** |
   | `resources/fastedge/`, `types/fastedge/` | **FastEdge** |
   | `resources/iam/`, `types/iam/` | **IAM** |
   | `resources/storage/`, `types/storage/` | **Object Storage** |
   | `resources/streaming/`, `types/streaming/` | **Streaming** |
   | `resources/waap/`, `types/waap/` | **WAAP** |
   | `_client.py`, `_base_client.py`, `_utils/`, `_models.py`, `_streaming.py`, `pagination.py`, `lib/` | **Other** |

   For canonical sub-product names within each product area, consult
   `references/products.md`. Always use the exact names listed there.

   These are heuristics. When a scope or path does not clearly map, use
   judgment based on the commit scope, file path, and diff context.

   Within a product area, split into distinct **sub-areas** by resource type.
   Do not lump unrelated resources into a single sub-area.

### Step 3 — Check CI Status

```bash
gh pr checks {N} --repo G-Core/gcore-python --json name,state,bucket
```

Exit codes: `0` = all pass, `8` = pending, `1` = failure.

| Status | Action |
|---|---|
| exit `0` / all checks pass | Report **CI green**, proceed |
| exit `8` / pending | Warn user checks are running. Ask: wait or proceed? |
| exit `1` / failure | Show failing checks. **Do not offer to merge.** |

### Step 4 — Generate Human-Readable Release Notes

Read `references/release-notes-examples.md` for style reference and examples.
Read `references/products.md` for canonical product and sub-product names.

Using the changelog (Step 2.1) and diff analysis (Step 2.2), generate the
human-readable summary (Part 1) following this structure:

```markdown
We're excited to announce version {VERSION}!

### **{Product Area}**

* **{Sub-area}**
  * Added `{field/method}` to `{Type}` — {description}
  * ⚠ BREAKING CHANGE: `{Type.field}` changed from `{old}` to `{new}`
  * Deprecated `{service.method()}` — use `{alternative}` instead
  * Fixed {description} — {detail}
```

#### Part 1 Rules

- **Group by product area** (alphabetically: CDN, Cloud, DDoS Protection,
  DNS, FastEdge, IAM, Object Storage, Streaming, WAAP). Place **Other** last.
  Only include areas that have changes.
- **Within each area, group by sub-area** alphabetically (e.g., Bare Metal,
  GPU Bare Metal, Managed Kubernetes, Load Balancers). Use the canonical names
  from `references/products.md`. If changes do not fit a sub-area, list
  directly under the product area.
- **Breaking changes** get `⚠ BREAKING CHANGE:` prefix inline. Always specify
  old value/type and new value/type.
- **Deprecations**: ``Deprecated `method()` — use `alternative()` instead``
- **Additions**: ``Added `name` field/method to `Type` — description``
- **Fixes**: `Fixed {what} — {detail}`
- **Always use backtick-wrapped Python identifiers** for types, fields, methods.
  Types use `PascalCase`, methods/fields use `snake_case`.
- **No commit hashes or links** in Part 1 (those are in Part 2).
- **Do not copy** the auto-generated changelog verbatim. Aggregate related
  changes. Skip noise.
- **Omit `codegen metadata` and `aggregated API specs update`** entries unless
  they introduce a specific user-visible change visible in the diff.

Display the generated Part 1 to the user. Ask if they want to edit or approve.

### Step 5 — Merge the Release PR

Present to the user:
1. CI status (from Step 3)
2. Generated release notes preview (Part 1 from Step 4)
3. Auto-generated changelog (Part 2 from PR body)
4. Recommended merge method: **rebase**

**Ask for explicit confirmation before merging.**

If user declines or wants changes, return to Step 4.

Once confirmed, merge via Bash:
```bash
gh pr merge {PR_NUMBER} --repo G-Core/gcore-python --rebase
```

If merge fails, report the error and stop.

### Step 6 — Update the GitHub Release

After merge, `stainless-app[bot]` auto-creates a GitHub Release.

1. Fetch the latest release. Verify `tagName` matches expected version
   `v{VERSION}`. If not found, `sleep 10` and retry once.

   ```bash
   gh release view --repo G-Core/gcore-python --json tagName,body,url
   ```

2. Build the final release body by combining Part 1 and the existing Part 2:

   ```
   {Part 1 — human-readable summary}


   {Part 2 — auto-generated changelog already in release body}
   ```

3. Update the release via Bash:
   ```bash
   gh release edit v{VERSION} \
     --repo G-Core/gcore-python \
     --notes "$(cat <<'RELEASE_EOF'
   {combined release notes}
   RELEASE_EOF
   )"
   ```

4. Display the release URL and confirm completion.

## Failure Modes

| Situation | Action |
|---|---|
| No open release PR | Inform user, stop |
| CI failing | Show failures, do not merge |
| CI pending | Warn, ask user preference |
| Merge conflict | Report, suggest manual resolution |
| Merge fails | Report error, stop |
| Release not found after merge | Retry once after 10s, then report |
| `gh` CLI not authenticated | Report, suggest `gh auth login` |
