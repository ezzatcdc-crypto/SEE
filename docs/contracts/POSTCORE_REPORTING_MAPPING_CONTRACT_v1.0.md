# POSTCORE_REPORTING Mapping Contract v1.0 (Artifact → Report Mapping Rules)

## 1. Scope

1.1 This contract SHALL define only deterministic mapping rules from CORE artifacts to report sections.  
1.2 This contract SHALL apply strictly post-CORE.  
1.3 This contract SHALL NOT define CORE behavior, admission behavior, or ingestion behavior.  
1.4 This contract SHALL NOT define formatting, styling, or presentation layout beyond section names and ordering.

## 2. Inputs

2.1 Implementations SHALL accept as inputs only CORE artifacts emitted by CORE for a single run.  
2.2 Implementations SHALL treat all inputs as immutable.  
2.3 Implementations SHALL reject any non-CORE artifact input.

## 3. Output

3.1 Implementations SHALL emit exactly one report set per CORE run input set.  
3.2 The report set SHALL contain a single primary report document named `report.md`.  
3.3 The report set MAY contain auxiliary files; auxiliary files SHALL be referenced by `report.md`.  
3.4 Report outputs SHALL NOT be SEE artifacts and SHALL NOT be CORE artifacts.

## 4. Deterministic Section Ordering

4.1 `report.md` SHALL contain the following top-level sections in the specified order:

- `Run Identity`
- `Artifact Inventory`
- `Indicators`
- `Patterns Drift`
- `Timeline`
- `Data Snapshot Summary`

4.2 Implementations SHALL NOT reorder sections.  
4.3 Implementations SHALL NOT omit a section if its source artifact exists.  
4.4 If a source artifact is absent, the corresponding section SHALL still exist and SHALL contain only the token `ABSENT`.

## 5. Section Mapping Rules

### 5.1 Run Identity

5.1.1 `Run Identity` SHALL be derived from `run_manifest.json`.  
5.1.2 The section SHALL include, at minimum, `run_id` and `generated_at` if present in `run_manifest.json`.  
5.1.3 If `run_manifest.json` is absent, the section SHALL contain only `ABSENT`.

### 5.2 Artifact Inventory

5.2.1 `Artifact Inventory` SHALL be derived from `registry/index.json`.  
5.2.2 The section SHALL list artifact logical names and relative paths exactly as present in `registry/index.json`.  
5.2.3 The section SHALL NOT infer artifacts not listed in `registry/index.json`.  
5.2.4 If `registry/index.json` is absent, the section SHALL contain only `ABSENT`.

### 5.3 Indicators

5.3.1 `Indicators` SHALL be derived from `indicators.json`.  
5.3.2 The section SHALL include a deterministic key-ordered listing of indicator keys.  
5.3.3 Ordering SHALL be lexicographic by UTF-8 codepoint of the full key path.  
5.3.4 If `indicators.json` is absent, the section SHALL contain only `ABSENT`.

### 5.4 Patterns Drift

5.4.1 `Patterns Drift` SHALL be derived from `patterns_drift.json`.  
5.4.2 The section SHALL include a deterministic key-ordered listing of drift keys.  
5.4.3 Ordering SHALL be lexicographic by UTF-8 codepoint of the full key path.  
5.4.4 If `patterns_drift.json` is absent, the section SHALL contain only `ABSENT`.

### 5.5 Timeline

5.5.1 `Timeline` SHALL be derived from `timeline.json`.  
5.5.2 If `timeline.json` contains an ordered list, the section SHALL preserve the list order exactly.  
5.5.3 If `timeline.json` is a mapping, keys SHALL be ordered lexicographically by UTF-8 codepoint.  
5.5.4 If `timeline.json` is absent, the section SHALL contain only `ABSENT`.

### 5.6 Data Snapshot Summary

5.6.1 `Data Snapshot Summary` SHALL be derived from `data_snapshot.json`.  
5.6.2 The section SHALL include only top-level keys present in `data_snapshot.json`.  
5.6.3 Top-level keys SHALL be ordered lexicographically by UTF-8 codepoint.  
5.6.4 The section SHALL NOT include full raw payload values unless the value is a scalar (string/number/boolean/null).  
5.6.5 If `data_snapshot.json` is absent, the section SHALL contain only `ABSENT`.

## 6. Prohibitions

6.1 Implementations SHALL NOT modify or write into any CORE artifact location.  
6.2 Implementations SHALL NOT write into CORE registry or index.  
6.3 Implementations SHALL NOT consult external mutable state to decide section content or ordering.  
6.4 Implementations SHALL NOT consult current time for content beyond what is already present in CORE artifacts.

