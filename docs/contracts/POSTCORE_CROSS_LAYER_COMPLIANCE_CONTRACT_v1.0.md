# POSTCORE Cross-Layer Compliance Contract v1.0

## 1. Scope

1.1 This contract SHALL define compliance constraints across POSTCORE_REPORTING, POSTCORE_PUBLISH, and POSTCORE_MONITORING.  
1.2 This contract SHALL NOT modify any individual layer contract.  
1.3 This contract SHALL NOT introduce runtime coupling between layers.

## 2. Layer Isolation

2.1 POSTCORE_REPORTING SHALL consume only CORE artifacts.  
2.2 POSTCORE_PUBLISH SHALL consume only POSTCORE_REPORTING report sets.  
2.3 POSTCORE_MONITORING SHALL consume only POSTCORE_PUBLISH publication output sets.  
2.4 No layer SHALL consume artifacts from a later layer.  
2.5 No layer SHALL bypass its immediate predecessor.

## 3. Deterministic Flow Constraint

3.1 For identical CORE run artifacts, the combined output of:
- POSTCORE_REPORTING
- POSTCORE_PUBLISH
- POSTCORE_MONITORING

SHALL be identical across executions.

3.2 Any nondeterminism detected at a downstream layer SHALL be treated as non-compliance.

## 4. Artifact Boundary Integrity

4.1 Each layer SHALL treat its input set as immutable.  
4.2 Each layer SHALL emit outputs into a distinct output root.  
4.3 Output roots SHALL NOT overlap between layers.  
4.4 No layer SHALL write into the output root of another layer.

## 5. Identity Propagation

5.1 `run_id` from CORE SHALL propagate unchanged into:
- report manifests
- publication manifests
- monitoring manifests

5.2 `publication_id` SHALL propagate unchanged into monitoring manifests.  
5.3 Identity values SHALL NOT be transformed, normalized, or regenerated downstream.

## 6. Hash Continuity

6.1 If a layer emits a hash over its primary artifact, that hash SHALL be referenced unchanged by downstream layers when applicable.  
6.2 Downstream layers SHALL NOT recompute upstream hashes except for verification.  
6.3 Verification SHALL NOT modify the referenced artifact.

## 7. No Backward Influence

7.1 POSTCORE_PUBLISH SHALL NOT influence POSTCORE_REPORTING outputs.  
7.2 POSTCORE_MONITORING SHALL NOT influence POSTCORE_PUBLISH outputs.  
7.3 No downstream layer SHALL alter upstream state.

## 8. Compliance Failure Handling

8.1 If a layer detects a violation of this contract, it SHALL reject processing and SHALL emit no outputs.  
8.2 Rejection under this contract SHALL NOT alter upstream artifacts.  
8.3 Rejection SHALL NOT generate SEE artifacts.

## 9. Prohibitions

9.1 This contract SHALL NOT introduce shared runtime state between layers.  
9.2 This contract SHALL NOT introduce bidirectional coupling.  
9.3 This contract SHALL NOT weaken determinism at any layer.  
9.4 Outputs under this contract SHALL NOT be SEE artifacts and SHALL NOT be CORE artifacts.

