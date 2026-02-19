# POSTCORE_REPORTING Canonical JSON Export Contract v1.1

## 1. Scope

1.1 This contract SHALL define a deterministic canonical JSON export for POSTCORE_REPORTING outputs.  
1.2 This contract SHALL extend POSTCORE_REPORTING v1.0 without modifying its determinism constraints.  
1.3 This contract SHALL NOT modify CORE behavior.

## 2. Export Artifact

2.1 Implementations MAY emit an auxiliary file named `report.json`.  
2.2 If emitted, `report.json` SHALL be considered a report auxiliary file.  
2.3 `report.json` SHALL be referenced from `report.md` and listed in `report_manifest.json.aux_files`.

## 3. report.json Schema

3.1 `report.json` SHALL be valid JSON encoded in UTF-8.  
3.2 `report.json` SHALL contain, at minimum:

- `schema_version` (string) and SHALL equal `1.1`
- `run_id` (string)
- `sections` (array)

3.3 Each element of `sections` SHALL contain, at minimum:

- `section_id` (string)
- `section_title` (string)
- `section_level` (integer)
- `content` (string)

## 4. Canonical Key Ordering

4.1 All JSON object keys SHALL be ordered lexicographically by UTF-8 codepoint.  
4.2 No additional keys SHALL be emitted unless explicitly defined by a future contract version.

## 5. Canonical Value Encoding

5.1 Strings SHALL be emitted exactly as in the source content.  
5.2 Numbers SHALL be base-10 without separators.  
5.3 Booleans SHALL be `true` or `false`.  
5.4 Null SHALL be `null`.  
5.5 JSON serialization SHALL NOT include NaN or Infinity values.

## 6. Deterministic Section Ordering

6.1 `sections` order SHALL match the section order in `report.md`.  
6.2 Section ordering SHALL remain deterministic for identical inputs.

## 7. Prohibitions

7.1 Implementations SHALL NOT consult external mutable state to emit `report.json`.  
7.2 Implementations SHALL NOT consult current time to emit `report.json`.  
7.3 This contract SHALL NOT weaken determinism.  
7.4 Outputs SHALL NOT be SEE artifacts and SHALL NOT be CORE artifacts.

