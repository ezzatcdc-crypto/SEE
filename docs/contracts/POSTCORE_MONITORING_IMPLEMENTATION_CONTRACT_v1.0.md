# POSTCORE_MONITORING Implementation Contract v1.0 (Schema + Interfaces Only)

## 1. Scope

1.1 This contract SHALL define only schemas and interfaces for POSTCORE_MONITORING.  
1.2 This contract SHALL NOT define evaluation logic beyond interface shape and required fields.  
1.3 This contract SHALL apply strictly post-POSTCORE_PUBLISH.

## 2. Inputs

2.1 Implementations SHALL accept as input only a publication output set reference.  
2.2 Inputs SHALL be read-only.  
2.3 Implementations SHALL reject any input that is not a publication output set reference.

## 3. Output Classification

3.1 Implementations SHALL emit exactly one monitoring output set per accepted input.  
3.2 Outputs SHALL NOT be SEE artifacts.  
3.3 Outputs SHALL NOT be CORE artifacts.  
3.4 Outputs SHALL NOT be eligible for CORE ingestion.

## 4. Interface Requirements

4.1 Implementations SHALL expose exactly one invocation interface named `monitor`.  
4.2 `monitor` SHALL accept a single argument `publication_ref`.  
4.3 `monitor` SHALL return a single value `monitoring_ref`.

## 5. Publication Reference Schema

5.1 `publication_ref` SHALL conform to the following schema:

- `publication_id` (string) SHALL be present.  
- `publications_root` (string) SHALL be present.  
- `bundle` (string) SHALL be present and SHALL reference `publication_bundle.zip` by relative path.  
- `manifest` (string) SHALL be present and SHALL reference `publication_manifest.json` by relative path.  
- `schema_version` (string) SHALL be present.

## 6. Monitoring Reference Schema

6.1 `monitoring_ref` SHALL conform to the following schema:

- `monitoring_id` (string) SHALL be present.  
- `monitoring_root` (string) SHALL be present.  
- `manifest` (string) SHALL be present and SHALL reference `monitoring_manifest.json` by relative path.  
- `schema_version` (string) SHALL be present.

## 7. monitoring_manifest.json Minimum

7.1 `monitoring_manifest.json` SHALL be valid JSON encoded in UTF-8.  
7.2 `monitoring_manifest.json` SHALL contain, at minimum:

- `schema_version` (string)
- `monitoring_id` (string)
- `source_publication_id` (string)
- `observed_bundle_hash` (string)
- `status` (string)

## 8. Prohibitions

8.1 Implementations SHALL NOT modify publication inputs.  
8.2 Implementations SHALL NOT consult external mutable state to satisfy this contract.  
8.3 Implementations SHALL NOT write into CORE storage or registry.  
8.4 Implementations SHALL NOT participate in admission, authorization, or ingestion.

