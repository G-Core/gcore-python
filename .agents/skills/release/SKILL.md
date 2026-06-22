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
  Bash(gh release view * --repo G-Core/gcore-go *),
  Bash(gh release list --repo G-Core/gcore-go *),
  Bash(sleep *)
---

# Release Skill — G-Core/gcore-python

## Constraints

- **Repository**: `G-Core/gcore-python` (hardcoded, do not use for other repos)
- **Allowed tools**: `gh` CLI (scoped to `G-Core/gcore-python` + read-only
  `G-Core/gcore-go` releases) and `Read`
- **Never**: modify source code, force-push, delete branches, or merge without
  explicit user confirmation
- **Release PRs** are created by `release-please` (the stock
  `googleapis/release-please-action` running in `.github/workflows/release-please.yml`,
  authenticated with `RELEASE_PLEASE_TOKEN`), from a head branch starting with
  `release-please--branches--main` (e.g. `release-please--branches--main--changes--next`),
  with title `release: {version}`. The author is the token's user, not
  `stainless-app[bot]` (the legacy Stainless App is no longer used).

## Workflow

Execute steps 1-6 in order. Present findings at each step before proceeding.

### Step 1 — Discover the Release PR

```bash
gh pr list --repo G-Core/gcore-python --state open \
  --json number,title,author,url,createdAt,headRefName
```

Find the open PR whose title starts with `release: ` and whose head branch starts
with `release-please--branches--main` (release-please opens it; do not rely on the
author being `stainless-app`).

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

### Step 2.5 — Check Go SDK Release (Cross-SDK Sync)

Check whether `G-Core/gcore-go` already has a release for the same
version. Both SDKs are generated from the same API specs and share version
numbers, so matching releases cover the same underlying API changes.

```bash
gh release view v{VERSION} --repo G-Core/gcore-go --json tagName,body
```

- If a matching release **exists**, extract its Part 1 (everything before the
  `## {VERSION}` auto-generated changelog heading). Store it as the **Go
  reference notes** for use in Step 4.
- If the release **does not exist** (exit code ≠ 0), proceed without reference.
  This is expected when the Python SDK releases first.

Do **not** display the Go notes to the user — they are an internal
reference for wording alignment only.

### Step 3 — Check CI Status

```bash
gh pr checks {N} --repo G-Core/gcore-python --json name,state,bucket
```

**Ignore `detect-breaking-changes`** when evaluating CI status — it is
informational only. Breaking API changes are expected in release PRs and
documented in the changelog. If it fails, note it for the user but do not
treat it as a blocker.

After excluding `detect-breaking-changes`:

- **All checks pass** — report CI green, proceed.
- **Some checks pending** — warn user, ask: wait or proceed?
- **Any check fails** — show failing checks, do not offer to merge.

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
- **Cross-SDK alignment**: If Go reference notes were fetched in Step 2.5,
  use them as a wording guide for overlapping API changes. For each change that
  appears in both SDKs, match the Go description's phrasing and structure
  while substituting Python identifiers (`snake_case` methods, `Optional[T]`
  instead of `param.Opt[T]`, etc.). Python-only changes (SDK internals,
  Python-specific fixes) have no Go counterpart — write those fresh.
- **Do not copy** the auto-generated changelog verbatim. Aggregate related
  changes. Skip noise.
- **Omit `codegen metadata` and `aggregated API specs update`** entries unless
  they introduce a specific user-visible change visible in the diff.
- **Omit doc-only changes** — if a diff only updates comments, docstrings, or
  descriptions (e.g., `"IPv4"` → `"IPv4 or IPv6"` in a docstring, or adding a
  description to a service/resource for Terraform enablement) with no API
  behavioral change (no new fields, methods, types, or changed signatures),
  do **not** surface it in Part 1. These are internal metadata updates, not
  user-facing SDK changes.

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

After merge, `release-please` (the stock action) auto-creates the tag and GitHub Release.

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
| `detect-breaking-changes` fails | Informational only. Report to user, proceed with merge |
| CI failing (other checks) | Show failures, do not merge |
| CI pending | Warn, ask user preference |
| Merge conflict | Report, suggest manual resolution |
| Merge fails | Report error, stop |
| Release not found after merge | Retry once after 10s, then report |
| Go SDK release not found | Proceed without cross-SDK reference |
| `gh` CLI not authenticated | Report, suggest `gh auth login` |
