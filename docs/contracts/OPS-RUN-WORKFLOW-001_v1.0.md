# OPS-RUN-WORKFLOW-001 v1.0 — Operational Run Workflow Scaffold (Orchestration Only)

## 1. Scope
1. This contract SHALL define deterministic orchestration only.
2. It SHALL NOT modify CORE.
3. It SHALL NOT introduce new layers.
4. It SHALL NOT introduce runtime state.

## 2. Outputs
1. All outputs SHALL be written under:
   OUTPUT_ROOT/RUN_ID/
2. orchestration.log SHALL be emitted.
3. orchestration.json MAY be emitted.
4. No SEE authority SHALL be claimed.

## 3. Determinism
1. Workflow SHALL be repeatable.
2. If OUTPUT_ROOT/RUN_ID exists and is non-empty → refuse execution.
3. No hidden state SHALL exist.

## 4. Orchestration Order
S1 — SNAPSHOT
S2 — CORE RUN
S3 — POSTCORE REPORTING
S4 — POSTCORE PUBLISH (optional)
S5 — POSTCORE MONITORING (optional)

## 5. Prohibitions
1. SHALL NOT modify core/.
2. SHALL NOT write outside OUTPUT_ROOT/RUN_ID/.
3. SHALL NOT perform governance logic.
