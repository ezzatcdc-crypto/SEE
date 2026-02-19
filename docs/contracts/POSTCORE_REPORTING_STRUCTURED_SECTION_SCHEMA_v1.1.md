# POSTCORE_REPORTING Structured Section Schema Contract v1.1

## 1. Scope

1.1 This contract SHALL define a deterministic structured section schema for `report.md`.  
1.2 This contract SHALL extend POSTCORE_REPORTING v1.0 without modifying its determinism constraints.  
1.3 This contract SHALL NOT modify CORE behavior.

## 2. Section Model

2.1 `report.md` SHALL be representable as a sequence of structured sections.  
2.2 Each section SHALL contain:
- `section_id` (string)
- `section_title` (string)
- `section_level` (integer)
- `content` (string)

2.3 `section_id` SHALL be unique within a report.  
2.4 `section_level` SHALL correspond to Markdown heading depth (`#` = 1, `##` = 2, etc.).

## 3. Canonical Section Ordering

3.1 Sections SHALL appear in the order defined by the Mapping Contract.  
3.2 Section ordering SHALL be deterministic.  
3.3 Sections SHALL NOT be reordered by runtime conditions.

## 4. Section Identity Rules

4.1 `section_id` SHALL be derived deterministically from:
- `run_id`
- canonical section title
- section index

4.2 `section_id` SHALL be encoded as lowercase hex of a `sha256` digest.  
4.3 Section identity derivation SHALL be deterministic.

## 5. Section Content Rules

5.1 `content` SHALL contain only deterministic data derived from CORE artifacts.  
5.2 No section SHALL include environment-derived metadata.  
5.3 No section SHALL include timestamps unless present in CORE artifacts.

## 6. Serialization

6.1 Structured section representation MAY be emitted as JSON.  
6.2 JSON serialization SHALL be UTF-8 encoded.  
6.3 JSON object keys SHALL be ordered lexicographically by UTF-8 codepoint.  
6.4 JSON output SHALL NOT contain randomized fields.

## 7. Prohibitions

7.1 This contract SHALL NOT introduce shared runtime state.  
7.2 This contract SHALL NOT weaken determinism.  
7.3 Outputs SHALL NOT be SEE artifacts and SHALL NOT be CORE artifacts.

