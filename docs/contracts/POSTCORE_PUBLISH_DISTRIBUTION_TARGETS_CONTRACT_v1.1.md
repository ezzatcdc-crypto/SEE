# POSTCORE_PUBLISH Distribution Targets Contract v1.1

## 1. Scope

1.1 This contract SHALL define deterministic distribution target declarations for publishable bundles.  
1.2 This contract SHALL apply strictly after POSTCORE_PUBLISH bundle packaging.  
1.3 This contract SHALL NOT modify POSTCORE_PUBLISH v1.0 contracts.  
1.4 This contract SHALL NOT modify CORE behavior.  
1.5 This contract SHALL NOT introduce transport execution behavior.

## 2. Purpose

2.1 Distribution targets SHALL represent declarative publication intents only.  
2.2 Distribution targets SHALL NOT perform network transmission.  
2.3 Distribution targets SHALL NOT imply runtime delivery.

## 3. Inputs

3.1 Inputs SHALL be limited to finalized publish bundle archives and their manifests.  
3.2 Inputs SHALL be treated as immutable.  
3.3 No CORE artifact SHALL be directly accessed.

## 4. Output Artifact

4.1 The process SHALL emit `publish_distribution_targets.json`.  
4.2 The output SHALL be a non-SEE artifact.  
4.3 The output SHALL NOT be ingestible by CORE.  
4.4 The output SHALL NOT alter upstream artifacts.

## 5. Schema

5.1 `publish_distribution_targets.json` SHALL be deterministic JSON.  
5.2 JSON keys SHALL be lexicographically ordered.  
5.3 Encoding SHALL be UTF-8 with LF line endings only.  
5.4 No insignificant whitespace SHALL be emitted.  

5.5 The document SHALL contain:

- `distribution_targets_version` (string)  
- `publish_bundle_archive_hash` (string)  
- `targets` (array)

5.6 `distribution_targets_version` SHALL equal "v1.1".  
5.7 `publish_bundle_archive_hash` SHALL equal the SHA-256 hash from `publish_bundle_manifest.json`.  
5.8 `targets` SHALL be lexicographically sorted by `target_id`.

## 6. Target Object

6.1 Each target object SHALL contain:

- `target_id` (string)  
- `target_type` (string)  
- `target_locator` (string)

6.2 `target_id` SHALL be unique within the array.  
6.3 `target_type` SHALL be a declarative classification only.  
6.4 `target_locator` SHALL be a deterministic string identifier.  
6.5 No secret credentials SHALL be included.

## 7. Determinism

7.1 For identical inputs, the distribution targets artifact SHALL be identical.  
7.2 Ordering SHALL be deterministic.  
7.3 Generation SHALL NOT depend on system clock.  
7.4 Generation SHALL NOT depend on locale or environment variables.  

## 8. Prohibitions

8.1 This contract SHALL NOT execute transport.  
8.2 This contract SHALL NOT initiate network communication.  
8.3 This contract SHALL NOT persist runtime state.  
8.4 This contract SHALL NOT perform retries or delivery logic.  
8.5 Outputs SHALL NOT be SEE artifacts and SHALL NOT be CORE artifacts.  
8.6 This contract SHALL NOT introduce bidirectional coupling.  

## 9. Failure Semantics

9.1 On schema violation, generation SHALL fail.  
9.2 On failure, no distribution artifact SHALL remain.  
9.3 Failure SHALL NOT modify any input artifact.  
