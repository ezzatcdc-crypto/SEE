# POSTCORE Release Profile Aggregation Contract v1.1

## 1. Scope

1.1 This contract SHALL define a deterministic release profile aggregation for POSTCORE outputs.  
1.2 This contract SHALL apply strictly after POSTCORE_CROSS_LAYER_INTEGRITY_INDEX outputs are emitted.  
1.3 This contract SHALL NOT modify any frozen document.  
1.4 This contract SHALL NOT modify CORE behavior.  
1.5 This contract SHALL NOT introduce transport execution behavior.  
1.6 This contract SHALL NOT introduce runtime state.

## 2. Purpose

2.1 The release profile SHALL provide a deterministic aggregate descriptor of a publish release.  
2.2 The release profile SHALL remain a non-SEE artifact.  
2.3 The release profile SHALL NOT imply governance or enforcement.

## 3. Inputs

3.1 Inputs SHALL be limited to finalized POSTCORE artifacts, including:

- publish bundle archive  
- publish_bundle_manifest.json  
- publish_distribution_targets.json (if present)  
- publish_signing_envelope.json (if present)  
- publish_immutable_retention.json (if present)  
- postcore_monitoring_plan.json (if present)  
- postcore_audit_trace.json (if present)  
- postcore_integrity_index.json (if present)

3.2 Inputs SHALL be treated as immutable.  
3.3 No CORE artifact SHALL be directly accessed.

## 4. Output Artifact

4.1 The process SHALL emit `postcore_release_profile.json`.  
4.2 The output SHALL be a non-SEE artifact.  
4.3 The output SHALL NOT be ingestible by CORE.  
4.4 The output SHALL NOT alter upstream artifacts.

## 5. Schema

5.1 `postcore_release_profile.json` SHALL be deterministic JSON.  
5.2 JSON keys SHALL be lexicographically ordered.  
5.3 Encoding SHALL be UTF-8 with LF line endings only.  
5.4 No insignificant whitespace SHALL be emitted.

5.5 The document SHALL contain:

- `release_profile_version` (string)  
- `publish_bundle_archive_hash` (string)  
- `release_artifacts` (array)

5.6 `release_profile_version` SHALL equal "v1.1".  
5.7 `publish_bundle_archive_hash` SHALL equal the SHA-256 hash from `publish_bundle_manifest.json`.  
5.8 `release_artifacts` SHALL be lexicographically sorted by `artifact_id`.

## 6. Artifact Entry Object

6.1 Each entry object in `release_artifacts` SHALL contain:

- `artifact_id` (string)  
- `artifact_name` (string)  
- `artifact_hash_alg` (string)  
- `artifact_hash` (string)

6.2 `artifact_id` SHALL be unique within the array.  
6.3 `artifact_hash_alg` SHALL equal `sha256`.  
6.4 `artifact_hash` SHALL be lowercase hex.  
6.5 Each `artifact_hash` SHALL be computed over full bytes of the referenced artifact.  
6.6 Artifact bytes SHALL be taken exactly as emitted.

## 7. Determinism

7.1 For identical inputs, the release profile SHALL be identical.  
7.2 Ordering SHALL be deterministic.  
7.3 Generation SHALL NOT depend on system clock.  
7.4 Generation SHALL NOT depend on locale or environment variables.

## 8. Prohibitions

8.1 This contract SHALL NOT execute probes or monitoring actions.  
8.2 This contract SHALL NOT initiate network communication.  
8.3 This contract SHALL NOT persist runtime state.  
8.4 This contract SHALL NOT perform encryption.  
8.5 This contract SHALL NOT perform signing.  
8.6 Outputs SHALL NOT be SEE artifacts and SHALL NOT be CORE artifacts.  
8.7 This contract SHALL NOT introduce bidirectional coupling.

## 9. Failure Semantics

9.1 On schema violation, generation SHALL fail.  
9.2 On failure, no release profile SHALL remain.  
9.3 Failure SHALL NOT modify any input artifact.
