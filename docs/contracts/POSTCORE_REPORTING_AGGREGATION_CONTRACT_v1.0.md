# POSTCORE_REPORTING Aggregation Contract v1.0 (Multi-artifact Aggregation)

## 1. Scope

1.1 This contract SHALL define only deterministic aggregation rules across CORE run artifacts.  
1.2 This contract SHALL apply strictly post-CORE.  
1.3 This contract SHALL NOT define admission, ingestion, or CORE execution behavior.  
1.4 This contract SHALL NOT redefine mapping rules or formatting rules beyond aggregation constraints.

## 2. Inputs

2.1 Implementations SHALL accept as input a single CORE run artifact set.  
2.2 The input set SHALL be treated as read-only.  
2.3 Implementations SHALL reject any input set that contains non-CORE artifacts.

## 3. Output Set

3.1 Implementations SHALL emit exactly one report set per CORE run input set.  
3.2 The report set SHALL include `report.md` and `report_manifest.json`.  
3.3 The report set MAY include `assets/` as defined by the Formats Contract.

## 4. Aggregation Boundary

4.1 Aggregation SHALL be defined as composing report content from multiple CORE artifacts without modifying those artifacts.  
4.2 Aggregation SHALL NOT introduce derived values that are not explicitly present in at least one input CORE artifact.  
4.3 Aggregation MAY select, subset, and reorder content only as permitted by the Mapping Contract and Formats Contract.

## 5. Required Artifact Coverage

5.1 If present in the input set, the following artifacts SHALL be eligible for aggregation:

- `run_manifest.json`
- `registry/index.json`
- `indicators.json`
- `patterns_drift.json`
- `timeline.json`
- `data_snapshot.json`

5.2 Implementations SHALL NOT aggregate artifacts not listed in 5.1 unless such artifacts are present in `registry/index.json` and explicitly referenced by a future contract version.

## 6. Cross-artifact Consistency Rules

6.1 Implementations SHALL enforce a single `run_id` across all aggregated artifacts when `run_id` is present.  
6.2 If multiple `run_id` values are detected across artifacts, the implementation SHALL reject aggregation and SHALL emit no report set.  
6.3 Implementations SHALL NOT attempt to repair, infer, or reconcile conflicting identities.

## 7. Manifest Consistency Rules

7.1 `report_manifest.json.generated_from_run_id` SHALL equal the validated `run_id`.  
7.2 `report_manifest.json.aux_files` SHALL list only files actually present in the emitted `assets/` directory.  
7.3 `report_manifest.json.aux_files` SHALL be complete and SHALL NOT omit emitted auxiliary files.

## 8. De-duplication Rules

8.1 If the same logical content appears identically in multiple source artifacts, implementations MAY include it once.  
8.2 If de-duplication is applied, the implementation SHALL preserve deterministic selection rules.  
8.3 Deterministic selection SHALL be defined as choosing the source with lexicographically smallest relative path as listed in `registry/index.json`.

## 9. Reference Integrity Rules

9.1 Any reference from `report.md` to an auxiliary file SHALL resolve within the emitted report set.  
9.2 Implementations SHALL NOT emit dangling references.  
9.3 Implementations SHALL NOT reference files outside the report set.

## 10. Prohibitions

10.1 Implementations SHALL NOT modify CORE artifacts.  
10.2 Implementations SHALL NOT write into CORE storage or CORE registry.  
10.3 Implementations SHALL NOT consult external mutable state to decide inclusion, exclusion, or ordering.  
10.4 Implementations SHALL NOT consult current time for aggregation decisions beyond content already present in CORE artifacts.  
10.5 Outputs SHALL NOT be SEE artifacts and SHALL NOT be CORE artifacts.

