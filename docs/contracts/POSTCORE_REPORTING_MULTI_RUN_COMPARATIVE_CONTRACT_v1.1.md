# POSTCORE_REPORTING Multi-Run Comparative Reporting Contract v1.1

## 1. Scope

1.1 This contract SHALL define deterministic comparative reporting across multiple CORE runs.  
1.2 This contract SHALL apply strictly post-CORE.  
1.3 This contract SHALL NOT modify any single-run POSTCORE_REPORTING v1.0 or v1.1 contract.  
1.4 This contract SHALL NOT consume Structured Packs.

## 2. Inputs

2.1 Implementations SHALL accept as inputs only two or more CORE run artifact sets.  
2.2 Each run artifact set SHALL be treated as read-only.  
2.3 Implementations SHALL reject any input that is not a CORE run artifact set.

## 3. Output

3.1 Implementations SHALL emit exactly one comparative report set per invocation.  
3.2 The comparative report set SHALL include:
- `comparative_report.md`
- `comparative_report_manifest.json`

3.3 Outputs SHALL NOT be SEE artifacts and SHALL NOT be CORE artifacts.

## 4. Canonical Run Ordering

4.1 Input runs SHALL be ordered deterministically by `run_id` lexicographic UTF-8 codepoint.  
4.2 If `run_id` is absent, implementations SHALL reject and SHALL emit no outputs.  
4.3 If duplicate `run_id` values exist, implementations SHALL reject and SHALL emit no outputs.

## 5. Comparative Sections

5.1 `comparative_report.md` SHALL contain the following top-level sections in the specified order:

- `Run Set Identity`
- `Indicator Key Diff`
- `Patterns Drift Key Diff`
- `Timeline Shape Diff`
- `Snapshot Key Diff`

5.2 Each section SHALL be derived only from the corresponding artifacts within each run set:
- `indicators.json`
- `patterns_drift.json`
- `timeline.json`
- `data_snapshot.json`

5.3 If an artifact is absent for a given run, that run SHALL be treated as having `ABSENT` for that artifact.

## 6. Diff Semantics

6.1 Diffs SHALL be key-presence diffs only.  
6.2 Diffs SHALL NOT compute numeric deltas or interpret values.  
6.3 For each compared artifact type, implementations SHALL compute:
- `present_in_all`
- `present_in_some`
- `absent_in_all`

6.4 Key lists SHALL be ordered lexicographically by UTF-8 codepoint of full key path.

## 7. Manifest Requirements

7.1 `comparative_report_manifest.json` SHALL be valid JSON encoded in UTF-8.  
7.2 It SHALL contain, at minimum:
- `schema_version` (string) and SHALL equal `1.1`
- `run_ids` (array of strings) in canonical run order
- `primary_report` (string) and SHALL equal `comparative_report.md`

## 8. Determinism

8.1 For identical input run artifact bytes, outputs SHALL be byte-identical.  
8.2 Implementations SHALL NOT consult external mutable state.  
8.3 Implementations SHALL NOT consult current time.

