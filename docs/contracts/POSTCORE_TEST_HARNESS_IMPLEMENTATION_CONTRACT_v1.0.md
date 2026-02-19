# POSTCORE_TEST_HARNESS Implementation Contract v1.0 (Schema + Interfaces Only)

## 1. Scope

1.1 This contract SHALL define only schemas and interfaces for POSTCORE_TEST_HARNESS.  
1.2 This contract SHALL NOT define test logic beyond interface shape and required fields.  
1.3 This contract SHALL apply strictly post-POSTCORE pipeline completion.

## 2. Inputs

2.1 Implementations SHALL accept as input only one or more output set references from:
- POSTCORE_REPORTING, and/or
- POSTCORE_PUBLISH, and/or
- POSTCORE_MONITORING.

2.2 Inputs SHALL be read-only.  
2.3 Implementations SHALL reject any input that is not a valid output set reference.

## 3. Outputs

3.1 Implementations SHALL emit exactly one test result set per invocation.  
3.2 Outputs SHALL NOT be SEE artifacts.  
3.3 Outputs SHALL NOT be CORE artifacts.  
3.4 Outputs SHALL NOT be eligible for CORE ingestion.

## 4. Interface Requirements

4.1 Implementations SHALL expose exactly one invocation interface named `run_tests`.  
4.2 `run_tests` SHALL accept a single argument `inputs`.  
4.3 `inputs` SHALL be an array of output set references.  
4.4 `run_tests` SHALL return a single value `test_result_ref`.

## 5. Output Set Reference Schema

5.1 Each element of `inputs` SHALL conform to the following schema:

- `set_type` (string) SHALL be one of: `REPORT_SET`, `PUBLICATION_SET`, `MONITORING_SET`  
- `set_id` (string) SHALL be present  
- `root` (string) SHALL be present  
- `manifest` (string) SHALL be present  
- `schema_version` (string) SHALL be present

## 6. Test Result Reference Schema

6.1 `test_result_ref` SHALL conform to the following schema:

- `test_run_id` (string) SHALL be present  
- `results_root` (string) SHALL be present  
- `manifest` (string) SHALL be present and SHALL reference `test_manifest.json` by relative path  
- `schema_version` (string) SHALL be present

## 7. test_manifest.json Minimum

7.1 `test_manifest.json` SHALL be valid JSON encoded in UTF-8.  
7.2 `test_manifest.json` SHALL contain, at minimum:

- `schema_version` (string)
- `test_run_id` (string)
- `inputs` (array)
- `results` (array)

## 8. Prohibitions

8.1 Implementations SHALL NOT modify any input set.  
8.2 Implementations SHALL NOT consult external mutable state to satisfy this contract.  
8.3 Implementations SHALL NOT write into CORE storage or registry.  
8.4 Implementations SHALL NOT participate in admission, authorization, or ingestion.

