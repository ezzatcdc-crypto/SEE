# POSTCORE_PUBLISH Signing Envelope Contract v1.1

## 1. Scope

1.1 This contract SHALL define a deterministic signing envelope for publish bundles.  
1.2 This contract SHALL apply strictly after bundle packaging and distribution target declaration.  
1.3 This contract SHALL NOT modify POSTCORE_PUBLISH v1.0 contracts.  
1.4 This contract SHALL NOT modify CORE behavior.  
1.5 This contract SHALL NOT introduce transport execution behavior.

## 2. Purpose

2.1 The signing envelope SHALL provide cryptographic attestation of a publish bundle.  
2.2 The signing envelope SHALL NOT alter the underlying bundle bytes.  
2.3 The signing envelope SHALL NOT modify bundle hash computation rules.

## 3. Inputs

3.1 Inputs SHALL be limited to:

- TAR publish bundle archive  
- publish_bundle_manifest.json  
- publish_distribution_targets.json (if present)

3.2 Inputs SHALL be treated as immutable.  
3.3 No CORE artifact SHALL be directly accessed.

## 4. Output Artifact

4.1 The process SHALL emit `publish_signing_envelope.json`.  
4.2 The output SHALL be a non-SEE artifact.  
4.3 The output SHALL NOT be ingestible by CORE.  
4.4 The output SHALL NOT alter upstream artifacts.

## 5. Schema

5.1 `publish_signing_envelope.json` SHALL be deterministic JSON.  
5.2 JSON keys SHALL be lexicographically ordered.  
5.3 Encoding SHALL be UTF-8 with LF line endings only.  
5.4 No insignificant whitespace SHALL be emitted.

5.5 The document SHALL contain:

- `signing_envelope_version` (string)  
- `publish_bundle_archive_hash` (string)  
- `signature_alg` (string)  
- `signature` (string)

5.6 `signing_envelope_version` SHALL equal "v1.1".  
5.7 `publish_bundle_archive_hash` SHALL equal the SHA-256 hash from `publish_bundle_manifest.json`.  

## 6. Signature Rules

6.1 `signature_alg` SHALL be explicitly declared.  
6.2 The algorithm identifier SHALL be deterministic.  
6.3 `signature` SHALL be lowercase hex or base64url without padding.  
6.4 The signature SHALL be computed strictly over the exact TAR archive bytes.  
6.5 The signing process SHALL NOT modify the TAR bytes.  
6.6 The signing process SHALL NOT re-hash using a different canonicalization rule.

## 7. Determinism

7.1 For identical inputs and identical signing key, the signature SHALL be identical.  
7.2 Signing SHALL NOT depend on system clock.  
7.3 Signing SHALL NOT depend on locale or environment variables.  
7.4 Non-deterministic signature schemes SHALL NOT be used unless explicitly normalized.  

## 8. Key Handling Constraints

8.1 Private keys SHALL NOT be embedded in any artifact.  
8.2 No secret material SHALL be written to disk by this contract.  
8.3 Key management SHALL remain external to SEE.  

## 9. Prohibitions

9.1 This contract SHALL NOT execute transport.  
9.2 This contract SHALL NOT initiate network communication.  
9.3 This contract SHALL NOT persist runtime state.  
9.4 Outputs SHALL NOT be SEE artifacts and SHALL NOT be CORE artifacts.  
9.5 This contract SHALL NOT introduce bidirectional coupling.  

## 10. Failure Semantics

10.1 On signature computation failure, generation SHALL fail.  
10.2 On failure, no signing envelope SHALL remain.  
10.3 Failure SHALL NOT modify any input artifact.  

