# POSTCORE End-to-End Deterministic Pipeline Contract v1.0

## 1. Scope

1.1 This contract SHALL define deterministic constraints across the full POSTCORE pipeline:
- POSTCORE_REPORTING
- POSTCORE_PUBLISH
- POSTCORE_MONITORING

1.2 This contract SHALL NOT modify individual layer contracts.  
1.3 This contract SHALL NOT introduce runtime coupling between layers.

## 2. Pipeline Definition

2.1 The deterministic pipeline SHALL be defined as:

CORE Run Artifacts
→ POSTCORE_REPORTING
→ POSTCORE_PUBLISH
→ POSTCORE_MONITORING

2.2 Each stage SHALL consume only the immediate predecessor's output.  
2.3 No stage SHALL access CORE artifacts except POSTCORE_REPORTING.

## 3. End-to-End Determinism

3.1 For identical CORE run artifact bytes, the entire pipeline SHALL produce identical:
- report outputs
- publication bundles
- monitoring manifests

3.2 Determinism SHALL be evaluated over full output bytes of:
- `report.md`
- `report_manifest.json`
- `publication_bundle.zip`
- `publication_manifest.json`
- `monitoring_manifest.json`

3.3 Byte-level equality SHALL be required.

## 4. Idempotence

4.1 Re-executing any stage with identical inputs SHALL produce byte-identical outputs.  
4.2 Re-executing the entire pipeline SHALL produce byte-identical final outputs.

## 5. Identity Continuity

5.1 `run_id` SHALL remain unchanged throughout all stages.  
5.2 `publication_id` SHALL remain unchanged after generation.  
5.3 `monitoring_id` SHALL be deterministically derived from `publication_id`.

## 6. Hash Continuity

6.1 `publication_bundle.zip` hash SHALL remain stable for identical report inputs.  
6.2 `observed_bundle_hash` in monitoring SHALL match the computed hash exactly.  
6.3 No stage SHALL alter upstream hashes.

## 7. No Hidden State

7.1 No stage SHALL consult environment variables to influence output.  
7.2 No stage SHALL consult system time for output generation.  
7.3 No stage SHALL consult network or external services during output generation.  
7.4 No stage SHALL maintain cross-run mutable state.

## 8. Output Root Isolation

8.1 Each stage SHALL emit outputs into a distinct directory root.  
8.2 Directory roots SHALL NOT overlap.  
8.3 No stage SHALL modify another stage's output root.

## 9. Failure Determinism

9.1 If a stage rejects input under its contract, it SHALL emit no outputs.  
9.2 Rejection SHALL be deterministic for identical inputs.  
9.3 Rejection SHALL NOT alter upstream artifacts.

## 10. Prohibitions

10.1 This contract SHALL NOT introduce new layers.  
10.2 This contract SHALL NOT weaken determinism defined in individual layer contracts.  
10.3 Outputs under this contract SHALL NOT be SEE artifacts and SHALL NOT be CORE artifacts.

