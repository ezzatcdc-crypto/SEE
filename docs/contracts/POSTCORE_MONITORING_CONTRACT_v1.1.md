# POSTCORE_MONITORING Contract v1.1

## 1. Scope

1.1 This contract SHALL define deterministic monitoring declarations for post-publish outputs.  
1.2 This contract SHALL apply strictly after POSTCORE_PUBLISH outputs are emitted.  
1.3 This contract SHALL NOT modify POSTCORE stack v1.0 or any frozen document.  
1.4 This contract SHALL NOT modify CORE behavior.  
1.5 This contract SHALL NOT introduce transport execution behavior.  
1.6 This contract SHALL NOT introduce runtime state.

## 2. Purpose

2.1 Monitoring declarations SHALL represent observability intent only.  
2.2 Monitoring declarations SHALL NOT execute monitoring probes.  
2.3 Monitoring declarations SHALL NOT imply runtime enforcement.

## 3. Inputs

3.1 Inputs SHALL be limited to finalized POSTCORE_PUBLISH outputs and manifests.  
3.2 Inputs SHALL be treated as immutable.  
3.3 No CORE artifact SHALL be directly accessed.

## 4. Output Artifact

4.1 The process SHALL emit `postcore_monitoring_plan.json`.  
4.2 The output SHALL be a non-SEE artifact.  
4.3 The output SHALL NOT be ingestible by CORE.  
4.4 The output SHALL NOT alter upstream artifacts.

## 5. Schema

5.1 `postcore_monitoring_plan.json` SHALL be deterministic JSON.  
5.2 JSON keys SHALL be lexicographically ordered.  
5.3 Encoding SHALL be UTF-8 with LF line endings only.  
5.4 No insignificant whitespace SHALL be emitted.

5.5 The document SHALL contain:

- `monitoring_plan_version` (string)  
- `publish_bundle_archive_hash` (string)  
- `monitoring_targets` (array)

5.6 `monitoring_plan_version` SHALL equal "v1.1".  
5.7 `publish_bundle_archive_hash` SHALL equal the SHA-256 hash from `publish_bundle_manifest.json`.  
5.8 `monitoring_targets` SHALL be lexicographically sorted by `target_id`.

## 6. Monitoring Target Object

6.1 Each monitoring target object SHALL contain:

- `target_id` (string)  
- `target_type` (string)  
- `target_locator` (string)  
- `expected_hash_alg` (string)  
- `expected_hash` (string)

6.2 `target_id` SHALL be unique within the array.  
6.3 `target_type` SHALL be declarative only.  
6.4 `target_locator` SHALL be a deterministic identifier string.  
6.5 `expected_hash_alg` SHALL equal `sha256`.  
6.6 `expected_hash` SHALL be lowercase hex.

## 7. Determinism

7.1 For identical inputs, the monitoring plan SHALL be identical.  
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
9.2 On failure, no monitoring plan SHALL remain.  
9.3 Failure SHALL NOT modify any input artifact.

