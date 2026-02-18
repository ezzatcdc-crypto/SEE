# RFC-SEE-CORE-ARTIFACTS-001 v1.0 — Compliance Checklist (CORE Artifacts)

[Derived From: RFC-SEE-CORE-ARTIFACTS-001 v1.0 → §1–§10 + JSON Schemas]

This checklist defines mandatory compliance checks for all artifacts governed by RFC-SEE-CORE-ARTIFACTS-001 v1.0.

---

## 0) Scope & Gate Conditions

### 0.1 Admission gate
- If Structured Pack ingestion is rejected: NO artifacts SHALL be produced.
[Derived From: RFC-SEE-CORE-ARTIFACTS-001 v1.0 → §4.2–§4.3]

### 0.2 Post-admission failure gate
- If failure occurs after admission: ONLY run_manifest.json SHALL be produced.
- run_manifest.json.status SHALL be "FAILED".
- run_manifest.json.failure SHALL be present.
- No other artifacts in §5.1 SHALL be produced.
[Derived From: RFC-SEE-CORE-ARTIFACTS-001 v1.0 → §5.2.1–§5.2.4]

---

## 1) Schema Validation (Draft-07)

For each produced artifact file, validate against its JSON Schema:

- run_manifest.json → schemas/run_manifest.json.schema.json
- data_snapshot.json → schemas/data_snapshot.json.schema.json
- indicators.json → schemas/indicators.json.schema.json
- patterns_drift.json → schemas/patterns_drift.json.schema.json
- timeline.json → schemas/timeline.json.schema.json
- registry/index.json → schemas/registry/index.json.schema.json (conditional)
[Derived From: RFC-SEE-CORE-ARTIFACTS-001 v1.0 → §10 + schemas]

### 1.1 additionalProperties
- additionalProperties SHALL be false everywhere (no extra fields).
[Derived From: RFC-SEE-CORE-ARTIFACTS-001 v1.0 → §3.3 + schemas]

### 1.2 Required fields
- All schema "required" properties MUST exist.
- All "const" constraints MUST match (schema_version="1.0").
[Derived From: RFC-SEE-CORE-ARTIFACTS-001 v1.0 → §6.1, §9.2–§9.3 + schemas]

---

## 2) Deterministic Serialization (JCS)

### 2.1 Canonicalization requirement
- Each artifact MUST be canonicalized exactly per RFC 8785 (JCS).
- Hash input bytes MUST be UTF-8 of JCS-canonical JSON text.
[Derived From: RFC-SEE-CORE-ARTIFACTS-001 v1.0 → §1.1–§1.3]

### 2.2 Forbidden JSON forms
- Duplicate object member names SHALL NOT appear at any level.
- NaN and Infinity SHALL NOT appear.
[Derived From: RFC-SEE-CORE-ARTIFACTS-001 v1.0 → §1.4–§1.5]

---

## 3) Hashing & Binding

### 3.1 Hash algorithm and token format
- SHA-256 ONLY.
- Hash token MUST be lowercase 64 hex chars.
[Derived From: RFC-SEE-CORE-ARTIFACTS-001 v1.0 → §2.1–§2.2]

### 3.2 run_manifest_hash computation rule
- run_manifest_hash MUST equal SHA-256 over JCS-canonical UTF-8 bytes of run_manifest.json with run_manifest_hash field omitted.
[Derived From: RFC-SEE-CORE-ARTIFACTS-001 v1.0 → §2.3]

### 3.3 Cross-artifact chaining (manifest map)
- run_manifest.json.artifacts MUST map artifact filename → SHA-256 hash of that artifact’s JCS bytes.
- Each recorded hash MUST match recomputed SHA-256(JCS(artifact)).
[Derived From: RFC-SEE-CORE-ARTIFACTS-001 v1.0 → §2.4.1, §2.4.3]

### 3.4 Non-manifest binding to run_manifest_hash
- Every non-manifest artifact MUST include run_manifest_hash.
- run_manifest_hash in each non-manifest artifact MUST match §3.2.
[Derived From: RFC-SEE-CORE-ARTIFACTS-001 v1.0 → §2.4.2, §6.5]

### 3.5 No other chaining required
- No additional chaining mechanism SHALL be required.
[Derived From: RFC-SEE-CORE-ARTIFACTS-001 v1.0 → §2.5]

---

## 4) Envelope Prohibition

- A common top-level envelope applicable to all artifacts is forbidden.
- Only fields permitted by the artifact-specific schemas may appear.
[Derived From: RFC-SEE-CORE-ARTIFACTS-001 v1.0 → §3.1–§3.3]

---

## 5) Common Field Placement Rules

### 5.1 schema_version
- schema_version MUST exist in every produced artifact.
- schema_version MUST equal "1.0".
[Derived From: RFC-SEE-CORE-ARTIFACTS-001 v1.0 → §6.1, §9.2–§9.3]

### 5.2 run_id
- run_id MUST exist in every produced artifact.
[Derived From: RFC-SEE-CORE-ARTIFACTS-001 v1.0 → §6.4]

### 5.3 engine / doctrine exclusivity
- engine MUST appear only in run_manifest.json and MUST NOT appear in other artifacts.
- doctrine MUST appear only in run_manifest.json and MUST NOT appear in other artifacts.
[Derived From: RFC-SEE-CORE-ARTIFACTS-001 v1.0 → §6.2–§6.3]

### 5.4 run_manifest_hash presence
- run_manifest_hash MUST appear in every produced artifact except run_manifest.json.
[Derived From: RFC-SEE-CORE-ARTIFACTS-001 v1.0 → §6.5]

---

## 6) Timestamp Compliance

### 6.1 Format requirement
- All timestamps, where permitted, MUST be RFC 3339 format with UTC indicator "Z".
- Local offsets SHALL NOT appear.
[Derived From: RFC-SEE-CORE-ARTIFACTS-001 v1.0 → §7.1–§7.2]

### 6.2 Schema-only timestamp fields
- Timestamps may appear ONLY in schema-defined fields.
[Derived From: RFC-SEE-CORE-ARTIFACTS-001 v1.0 → §7.3]

### 6.3 Ordering keys restriction
- No timestamp field SHALL be used as an ordering key unless explicitly stated.
[Derived From: RFC-SEE-CORE-ARTIFACTS-001 v1.0 → §7.4]

---

## 7) Deterministic Array Ordering

Any violation renders the artifact INVALID.

### 7.1 timeline.json.events
Sort by:
1) t ascending (lexicographic RFC 3339 Z timestamps)
2) event_id ascending (lexicographic)
3) kind ascending (lexicographic)
[Derived From: RFC-SEE-CORE-ARTIFACTS-001 v1.0 → §8.2.1–§8.2.3]

### 7.2 indicators.json.indicators
Sort by indicator_id ascending (lexicographic).
[Derived From: RFC-SEE-CORE-ARTIFACTS-001 v1.0 → §8.3]

### 7.3 patterns_drift.json.patterns
Sort by pattern_id ascending (lexicographic).
[Derived From: RFC-SEE-CORE-ARTIFACTS-001 v1.0 → §8.4]

### 7.4 data_snapshot.json.sources (if present)
Sort by source_id ascending (lexicographic).
[Derived From: RFC-SEE-CORE-ARTIFACTS-001 v1.0 → §8.5]

---

## 8) Versioning Constraints

### 8.1 Artifact schema_version
- Producer MUST set schema_version="1.0" for artifacts under this RFC.
- Producer SHALL NOT emit a different schema_version under this RFC.
[Derived From: RFC-SEE-CORE-ARTIFACTS-001 v1.0 → §9.2–§9.5.2]

### 8.2 engine.version and doctrine.version
- In run_manifest.json: engine.version and doctrine.version required.
- Must be semantic versions: MAJOR.MINOR(.PATCH) or MAJOR.MINOR.
[Derived From: RFC-SEE-CORE-ARTIFACTS-001 v1.0 → §9.4]

