# POSTCORE Deterministic Verification Harness Contract v1.1

## 1. Scope

1.1 This contract SHALL define a deterministic verification harness specification for POSTCORE outputs.  
1.2 This contract SHALL apply strictly after POSTCORE_RELEASE_PROFILE outputs are emitted.  
1.3 This contract SHALL NOT modify any frozen document.  
1.4 This contract SHALL NOT modify CORE behavior.  
1.5 This contract SHALL NOT introduce transport execution behavior.  
1.6 This contract SHALL NOT introduce runtime state.

## 2. Purpose

2.1 The verification harness SHALL define deterministic verification expectations only.  
2.2 The verification harness SHALL NOT execute verification actions.  
2.3 The verification harness SHALL remain a non-SEE artifact.

## 3. Inputs

3.1 Inputs SHALL be limited to finalized POSTCORE artifacts, including:

- postcore_release_profile.json (if present)  
- postcore_integrity_index.json (if present)  
- postcore_audit_trace.json (if present)  
- publish_bundle_manifest.json (if present)

3.2 Inputs SHALL be treated as immutable.  
3.3 No CORE artifact SHALL be directly accessed.

## 4. Output Artifact

4.1 The process SHALL emit `postcore_verification_harness.json`.  
4.2 The output SHALL be a non-SEE artifact.  
4.3 The output SHALL NOT be ingestible by CORE.  
4.4 The output SHALL NOT alter upstream artifacts.

## 5. Schema

5.1 `postcore_verification_harness.json` SHALL be deterministic JSON.  
5.2 JSON keys SHALL be lexicographically ordered.  
5.3 Encoding SHALL be UTF-8 with LF line endings only.  
5.4 No insignificant whitespace SHALL be emitted.

5.5 The document SHALL contain:

- `verification_harness_version` (string)  
- `publish_bundle_archive_hash` (string)  
- `expected_artifacts` (array)

5.6 `verification_harness_version` SHALL equal "v1.1".  
5.7 `publish_bundle_archive_hash` SHALL equal the SHA-256 hash from `publish_bundle_manifest.json`.  
5.8 `expected_artifacts` SHALL be lexicographically sorted by `artifact_id`.

## 6. Expected Artifact Object

6.1 Each object in `expected_artifacts` SHALL contain:

- `artifact_id` (string)  
- `artifact_name` (string)  
- `expected_hash_alg` (string)  
- `expected_hash` (string)

6.2 `artifact_id` SHALL be unique within the array.  
6.3 `expected_hash_alg` SHALL equal `sha256`.  
6.4 `expected_hash` SHALL be lowercase hex.  
6.5 `expected_hash` SHALL be computed over full bytes of the referenced artifact.  
6.6 Artifact bytes SHALL be taken exactly as emitted.

## 7. Determinism

7.1 For identical inputs, the verification harness SHALL be identical.  
7.2 Ordering SHALL be deterministic.  
7.3 Generation SHALL NOT depend on system clock.  
7.4 Generation SHALL NOT depend on locale or environment variables.

## 8. Prohibitions

8.1 This contract SHALL NOT execute verification actions.  
8.2 This contract SHALL NOT initiate network communication.  
8.3 This contract SHALL NOT persist runtime state.  
8.4 This contract SHALL NOT perform encryption.  
8.5 This contract SHALL NOT perform signing.  
8.6 Outputs SHALL NOT be SEE artifacts and SHALL NOT be CORE artifacts.  
8.7 This contract SHALL NOT introduce bidirectional coupling.

## 9. Failure Semantics

9.1 On schema violation, generation SHALL fail.  
9.2 On failure, no verification harness SHALL remain.  
9.3 Failure SHALL NOT modify any input artifact.
