# POSTCORE_REPORTING Comparative Integrity Hash Contract v1.1

## 1. Scope

1.1 This contract SHALL define deterministic integrity hashing for comparative reporting outputs.  
1.2 This contract SHALL extend comparative reporting v1.1 without modifying single-run integrity hashing.  
1.3 This contract SHALL NOT modify CORE behavior.

## 2. Integrity Fields

2.1 `comparative_report_manifest.json` SHALL include the following keys:

- `comparative_report_hash_alg` (string)
- `comparative_report_hash` (string)

2.2 `comparative_report_hash_alg` SHALL equal `sha256`.  
2.3 `comparative_report_hash` SHALL be lowercase hex.

## 3. Hash Basis

3.1 `comparative_report_hash` SHALL be computed over the full bytes of `comparative_report.md`.  
3.2 `comparative_report.md` bytes SHALL be taken exactly as emitted.  
3.3 If `comparative_report.json` exists, `comparative_report_manifest.json` MAY also include:

- `comparative_report_json_hash_alg` (string)
- `comparative_report_json_hash` (string)

3.4 If present, `comparative_report_json_hash_alg` SHALL equal `sha256`.  
3.5 If present, `comparative_report_json_hash` SHALL be lowercase hex and SHALL be computed over full bytes of `comparative_report.json`.

## 4. Determinism

4.1 For identical inputs, all comparative integrity hashes SHALL be identical.  
4.2 Integrity hashing SHALL NOT introduce nondeterminism.

## 5. Prohibitions

5.1 Implementations SHALL NOT consult current time to compute integrity hashes.  
5.2 Implementations SHALL NOT consult external mutable state to compute integrity hashes.  
5.3 This contract SHALL NOT weaken determinism.  
5.4 Outputs SHALL NOT be SEE artifacts and SHALL NOT be CORE artifacts.

