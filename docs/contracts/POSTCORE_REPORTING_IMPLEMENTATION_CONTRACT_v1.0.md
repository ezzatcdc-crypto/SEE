# POSTCORE_REPORTING Implementation Contract v1.0 (Schema + Interfaces Only)

## 1. Scope

1.1 This contract SHALL define only schemas and interfaces for POSTCORE_REPORTING.  
1.2 This contract SHALL NOT define execution behavior, mapping rules, or formatting rules.  
1.3 This contract SHALL apply strictly post-CORE and SHALL assume CORE run completion.

## 2. Inputs

2.1 Implementations SHALL accept as input only a CORE run artifact set.  
2.2 Inputs SHALL be read-only.  
2.3 Implementations SHALL reject any input that is not a CORE artifact set.

## 3. Output Classification

3.1 Implementations MAY emit reports.  
3.2 Outputs SHALL NOT be SEE artifacts.  
3.3 Outputs SHALL NOT be CORE artifacts.  
3.4 Outputs SHALL NOT be eligible for CORE ingestion.

## 4. Interface Requirements

4.1 Implementations SHALL expose exactly one invocation interface named `generate_report`.  
4.2 `generate_report` SHALL accept a single argument `core_run_ref`.  
4.3 `core_run_ref` SHALL be a locator reference to a CORE run artifact set.  
4.4 `generate_report` SHALL return a single value `report_ref`.  
4.5 `report_ref` SHALL be a locator reference to the emitted report output set.

## 5. Core Run Reference Schema

5.1 `core_run_ref` SHALL conform to the following schema:

- `run_id` (string) SHALL be present.  
- `artifacts_root` (string) SHALL be present.  
- `artifacts_index` (string) SHALL be present.  
- `schema_version` (string) SHALL be present.

## 6. Report Reference Schema

6.1 `report_ref` SHALL conform to the following schema:

- `report_id` (string) SHALL be present.  
- `reports_root` (string) SHALL be present.  
- `manifest` (string) SHALL be present.  
- `schema_version` (string) SHALL be present.

## 7. Prohibitions

7.1 Implementations SHALL NOT modify CORE artifacts.  
7.2 Implementations SHALL NOT write into CORE storage or registry.  
7.3 Implementations SHALL NOT participate in admission, authorization, or ingestion.  
7.4 Implementations SHALL NOT share runtime state with CORE.  
7.5 Implementations SHALL NOT require external mutable state to satisfy this contract.

