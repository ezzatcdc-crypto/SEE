# POSTCORE_PUBLISH Implementation Contract v1.0 (Schema + Interfaces Only)

## 1. Scope

1.1 This contract SHALL define only schemas and interfaces for POSTCORE_PUBLISH.  
1.2 This contract SHALL NOT define execution behavior beyond interface shape and required fields.  
1.3 This contract SHALL apply strictly post-POSTCORE_REPORTING.

## 2. Inputs

2.1 Implementations SHALL accept as input only a POSTCORE_REPORTING report set reference.  
2.2 Inputs SHALL be read-only.  
2.3 Implementations SHALL reject any input that is not a report set reference.

## 3. Output Classification

3.1 Implementations SHALL emit exactly one publication output set per accepted input.  
3.2 Outputs SHALL NOT be SEE artifacts.  
3.3 Outputs SHALL NOT be CORE artifacts.  
3.4 Outputs SHALL NOT be eligible for CORE ingestion.

## 4. Interface Requirements

4.1 Implementations SHALL expose exactly one invocation interface named `publish`.  
4.2 `publish` SHALL accept a single argument `report_set_ref`.  
4.3 `publish` SHALL return a single value `publication_ref`.

## 5. Report Set Reference Schema

5.1 `report_set_ref` SHALL conform to the following schema:

- `report_id` (string) SHALL be present.  
- `reports_root` (string) SHALL be present.  
- `manifest` (string) SHALL be present and SHALL equal `report_manifest.json` or a relative path to it.  
- `primary_report` (string) SHALL be present and SHALL equal `report.md` or a relative path to it.  
- `schema_version` (string) SHALL be present.

## 6. Publication Reference Schema

6.1 `publication_ref` SHALL conform to the following schema:

- `publication_id` (string) SHALL be present.  
- `publications_root` (string) SHALL be present.  
- `bundle` (string) SHALL be present and SHALL equal `publication_bundle.zip` or a relative path to it.  
- `manifest` (string) SHALL be present and SHALL equal `publication_manifest.json` or a relative path to it.  
- `schema_version` (string) SHALL be present.

## 7. publication_manifest.json Minimum

7.1 `publication_manifest.json` SHALL be valid JSON encoded in UTF-8.  
7.2 `publication_manifest.json` SHALL contain, at minimum:

- `schema_version` (string)
- `publication_id` (string)
- `source_report_id` (string)
- `bundle` (string) and SHALL equal `publication_bundle.zip`
- `bundle_hash` (string)

## 8. Prohibitions

8.1 Implementations SHALL NOT modify report inputs.  
8.2 Implementations SHALL NOT consult external mutable state to satisfy this contract.  
8.3 Implementations SHALL NOT write into CORE storage or registry.  
8.4 Implementations SHALL NOT participate in admission, authorization, or ingestion.

