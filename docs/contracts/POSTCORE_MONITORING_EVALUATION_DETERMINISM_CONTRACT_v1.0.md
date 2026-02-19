# POSTCORE_MONITORING Evaluation Determinism Contract v1.0

## 1. Scope

1.1 This contract SHALL define deterministic evaluation rules for POSTCORE_MONITORING.  
1.2 This contract SHALL apply strictly post-POSTCORE_PUBLISH.  
1.3 This contract SHALL NOT define transport behavior or external probe behavior.

## 2. Inputs

2.1 Implementations SHALL evaluate only the publication output set contents.  
2.2 Implementations SHALL treat inputs as immutable.  
2.3 Implementations SHALL reject evaluation if required publication files are absent.

## 3. Required Publication Files

3.1 The following files SHALL be required:

- `publication_bundle.zip`
- `publication_manifest.json`

3.2 If any required file is absent, evaluation SHALL be rejected and SHALL emit no monitoring outputs.

## 4. Bundle Verification Rules

4.1 Implementations SHALL compute a deterministic hash of `publication_bundle.zip` bytes.  
4.2 The hash algorithm SHALL be `sha256`.  
4.3 The computed hash SHALL be encoded as lowercase hex and recorded as `observed_bundle_hash`.  
4.4 Implementations SHALL NOT normalize, rewrite, or repackage the bundle during evaluation.

## 5. Manifest Consistency Rules

5.1 Implementations SHALL parse `publication_manifest.json` as UTF-8 JSON.  
5.2 If parsing fails, evaluation SHALL be rejected and SHALL emit no monitoring outputs.  
5.3 If `publication_manifest.json.bundle_hash` is present, implementations SHALL compare it to `observed_bundle_hash`.  
5.4 If the values differ, evaluation SHALL be considered failed.

## 6. Deterministic Status Assignment

6.1 Implementations SHALL assign `status` deterministically based only on Section 4 and Section 5 results.  
6.2 If required files are present, JSON parses, and the hash comparison (when applicable) matches, `status` SHALL be `OK`.  
6.3 If required files are present and JSON parses but the hash comparison (when applicable) differs, `status` SHALL be `MISMATCH`.  
6.4 If evaluation is rejected under Section 3 or Section 5.2, implementations SHALL emit no monitoring outputs.

## 7. Output Constraints

7.1 `monitoring_manifest.json.status` SHALL be one of: `OK`, `MISMATCH`.  
7.2 Implementations SHALL NOT emit additional status values under this contract.

## 8. Prohibitions

8.1 Implementations SHALL NOT consult external mutable state to perform evaluation.  
8.2 Implementations SHALL NOT consult current time to perform evaluation.  
8.3 Implementations SHALL NOT perform network calls or external probes to perform evaluation.  
8.4 Outputs SHALL NOT be SEE artifacts and SHALL NOT be CORE artifacts.

