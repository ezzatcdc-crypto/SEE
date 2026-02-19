# POSTCORE_PUBLISH Immutable Retention Contract v1.1

## 1. Scope

1.1 This contract SHALL define deterministic immutable retention declarations for publish outputs.  
1.2 This contract SHALL apply strictly after bundle packaging, distribution target declaration, and signing envelope emission.  
1.3 This contract SHALL NOT modify POSTCORE_PUBLISH v1.0 contracts.  
1.4 This contract SHALL NOT modify CORE behavior.  
1.5 This contract SHALL NOT introduce transport execution behavior.  
1.6 This contract SHALL NOT introduce runtime state.

## 2. Purpose

2.1 Retention declarations SHALL represent immutability and retention intent only.  
2.2 Retention declarations SHALL NOT perform storage or replication actions.  
2.3 Retention declarations SHALL NOT imply runtime enforcement.

## 3. Inputs

3.1 Inputs SHALL be limited to:

- TAR publish bundle archive  
- publish_bundle_manifest.json  
- publish_distribution_targets.json (if present)  
- publish_signing_envelope.json (if present)

3.2 Inputs SHALL be treated as immutable.  
3.3 No CORE artifact SHALL be directly accessed.

## 4. Output Artifact

4.1 The process SHALL emit `publish_immutable_retention.json`.  
4.2 The output SHALL be a non-SEE artifact.  
4.3 The output SHALL NOT be ingestible by CORE.  
4.4 The output SHALL NOT alter upstream artifacts.

## 5. Schema

5.1 `publish_immutable_retention.json` SHALL be deterministic JSON.  
5.2 JSON keys SHALL be lexicographically ordered.  
5.3 Encoding SHALL be UTF-8 with LF line endings only.  
5.4 No insignificant whitespace SHALL be emitted.

5.5 The document SHALL contain:

- `immutable_retention_version` (string)  
- `publish_bundle_archive_hash` (string)  
- `retention_mode` (string)  
- `retention_policy_id` (string)  
- `immutability_required` (boolean)

5.6 `immutable_retention_version` SHALL equal "v1.1".  
5.7 `publish_bundle_archive_hash` SHALL equal the SHA-256 hash from `publish_bundle_manifest.json`.  
5.8 `retention_mode` SHALL be a declarative value only.  
5.9 `retention_policy_id` SHALL be a deterministic identifier string.  
5.10 `immutability_required` SHALL indicate intent only.

## 6. Determinism

6.1 For identical inputs, the retention artifact SHALL be identical.  
6.2 Ordering SHALL be deterministic.  
6.3 Generation SHALL NOT depend on system clock.  
6.4 Generation SHALL NOT depend on locale or environment variables.  

## 7. Prohibitions

7.1 This contract SHALL NOT execute storage operations.  
7.2 This contract SHALL NOT initiate network communication.  
7.3 This contract SHALL NOT persist runtime state.  
7.4 This contract SHALL NOT perform encryption.  
7.5 This contract SHALL NOT perform signing.  
7.6 Outputs SHALL NOT be SEE artifacts and SHALL NOT be CORE artifacts.  
7.7 This contract SHALL NOT introduce bidirectional coupling.  

## 8. Failure Semantics

8.1 On schema violation, generation SHALL fail.  
8.2 On failure, no retention artifact SHALL remain.  
8.3 Failure SHALL NOT modify any input artifact.  

