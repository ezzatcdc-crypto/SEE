# RFC-SEE-CORE-ARTIFACTS-001 v1.0 — CORE Artifact Schema & Determinism Contract
Authority: SEE Constitution v1.0; RFC-SEE-CORE-001 v1.0; RFC-SEE-LAB-001 v1.2; SEE Constitution Addendum A (Articles A1–A15); Freeze scope acknowledged.

## 1. Deterministic serialization rule (JSON-to-bytes)

1.1. All SEE CORE artifacts defined by this RFC SHALL be serialized and hashed using RFC 8785 — JSON Canonicalization Scheme (JCS).
1.2. The canonical byte sequence for hashing SHALL be the UTF-8 encoding of the JCS-canonicalized JSON text.
1.3. Canonicalization SHALL follow RFC 8785 exactly, including:

1.3.1. Object member ordering: lexicographic ordering by Unicode code point of member names.

1.3.2. Whitespace: no insignificant whitespace beyond that mandated by JCS.

1.3.3. String escaping: as mandated by JCS; strings SHALL be valid Unicode JSON strings.

1.3.4. Number encoding: as mandated by JCS; numbers SHALL be represented in the shortest round-trippable decimal form required by JCS; NaN and Infinity SHALL NOT appear.
1.4. Artifact producers SHALL NOT emit duplicate object member names at any level.
1.5. Any artifact violating 1.1–1.4 SHALL be invalid.

## 2. Hashing & binding model

2.1. The hash algorithm SHALL be SHA-256.
2.2. The token format for hashes SHALL be lowercase hexadecimal of the 32-byte SHA-256 digest (64 hex characters).
2.3. run_manifest_hash SHALL be computed as SHA-256 over the JCS-canonical UTF-8 bytes of run_manifest.json with run_manifest_hash field omitted.
2.4. Cross-artifact chaining SHALL be defined as follows:

2.4.1. run_manifest.json SHALL contain artifacts, a mapping from artifact name to SHA-256 hash of that artifact’s JCS-canonical bytes.

2.4.2. Every non-manifest artifact defined by this RFC SHALL include run_manifest_hash and SHALL be invalid if it does not match the SHA-256 hash computed per 2.3.

2.4.3. Every artifact hash recorded in run_manifest.json.artifacts SHALL be computed from the artifact content as serialized per Section 1.
2.5. No other cross-artifact chaining mechanism SHALL be required.

## 3. Top-level envelope decision

3.1. A common top-level envelope applicable to all artifacts is forbidden.
3.2. Each artifact SHALL have its own top-level schema and required fields as specified in Sections 4–10 and the JSON Schemas in this RFC.
3.3. Fields not explicitly permitted by the JSON Schemas in this RFC SHALL NOT appear.

## 4. Admission and rejection constraints

4.1. CORE validity SHALL be created only at Structured Pack ingestion.
4.2. On ingestion rejection, SEE SHALL produce no state and SHALL produce no artifacts.
4.3. Any record of non-admission SHALL be outside SEE and SHALL NOT be a SEE artifact.

## 5. Artifact set and production conditions

5.1. On successful execution after admission, CORE SHALL produce all of the following artifacts:

5.1.1. run_manifest.json

5.1.2. data_snapshot.json

5.1.3. indicators.json

5.1.4. patterns_drift.json

5.1.5. timeline.json

5.1.6. registry/index.json (only if CORE maintains a registry; if produced, it SHALL conform to this RFC)

5.2. On failure after admission:

5.2.1. CORE SHALL produce run_manifest.json only.

5.2.2. run_manifest.json.status SHALL be "FAILED".

5.2.3. run_manifest.json SHALL include failure, as defined in the schema, and SHALL include artifacts either absent or empty.

5.2.4. No other artifacts defined by this RFC SHALL be produced.

## 6. Common field rules (where applicable)

6.1. schema_version SHALL be present in every produced artifact defined by this RFC.
6.2. engine SHALL be present only in run_manifest.json and SHALL NOT appear in other artifacts.
6.3. doctrine SHALL be present only in run_manifest.json and SHALL NOT appear in other artifacts.
6.4. run_id SHALL be present in every produced artifact defined by this RFC.
6.5. run_manifest_hash SHALL be present in every produced artifact defined by this RFC except run_manifest.json.
6.6. run_manifest.json SHALL include run_manifest_hash as defined in Section 2 and the schema.

## 7. Timestamp rules

7.1. All timestamps, where permitted, SHALL be strings in RFC 3339 format with UTC timezone indicator Z.
7.2. Timestamps SHALL NOT include local offsets.
7.3. Timestamps SHALL be permitted only in fields explicitly defined in the JSON Schemas of this RFC.
7.4. No timestamp field SHALL be used as an ordering key unless explicitly stated by this RFC.

## 8. Deterministic ordering rules (arrays and event ordering)

8.1. Arrays in all artifacts defined by this RFC SHALL be deterministically ordered as specified below; producers SHALL NOT emit semantically unordered arrays.
8.2. timeline.json.events SHALL be sorted by:

8.2.1. t ascending (lexicographic RFC 3339 Z timestamps), then

8.2.2. event_id ascending (lexicographic), then

8.2.3. kind ascending (lexicographic).
8.3. indicators.json.indicators SHALL be sorted by indicator_id ascending (lexicographic).
8.4. patterns_drift.json.patterns SHALL be sorted by pattern_id ascending (lexicographic).
8.5. data_snapshot.json.sources (if present) SHALL be sorted by source_id ascending (lexicographic).
8.6. Any artifact violating required array order SHALL be invalid.

## 9. Versioning rules

9.1. schema_version values SHALL be semantic versions in the form MAJOR.MINOR.
9.2. This RFC defines schema_version for each artifact as 1.0.
9.3. A producer conforming to this RFC SHALL set each artifact’s schema_version to 1.0.
9.4. run_manifest.json.engine.version and run_manifest.json.doctrine.version SHALL be required and SHALL be semantic versions in the form MAJOR.MINOR.PATCH or MAJOR.MINOR.
9.5. Backward compatibility expectations:

9.5.1. A consumer claiming support for schema_version 1.0 SHALL accept artifacts that conform to the schemas in this RFC.

9.5.2. A producer SHALL NOT emit a different schema_version under this RFC.

## 10. JSON Schemas (draft-07)

Schemas are authoritative and MUST be used for validation:

- schemas/run_manifest.json.schema.json
- schemas/data_snapshot.json.schema.json
- schemas/indicators.json.schema.json
- schemas/patterns_drift.json.schema.json
- schemas/timeline.json.schema.json
- schemas/registry/index.json.schema.json
