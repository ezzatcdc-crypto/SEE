# POSTCORE_PUBLISH Distribution Targets Contract v1.0

## 1. Scope

1.1 This contract SHALL define only deterministic classification of publication output destinations.  
1.2 This contract SHALL NOT define network transport, authentication, credentials, or delivery behavior.  
1.3 This contract SHALL apply strictly post-POSTCORE_REPORTING.

## 2. Target Set

2.1 A publication MAY be assigned to one or more targets from the following closed set:

- `LOCAL_FS`
- `GIT_REPO`
- `HTTP_ENDPOINT`
- `OBJECT_STORE`

2.2 Implementations SHALL NOT define additional target identifiers in this contract version.

## 3. Target Descriptor Schema

3.1 Each target assignment SHALL be represented as a JSON object encoded in UTF-8.  
3.2 Each target descriptor SHALL contain, at minimum:

- `target_type` (string) and SHALL be one of the closed set in 2.1
- `target_id` (string)
- `schema_version` (string)

3.3 Target descriptors MAY include additional keys.  
3.4 Additional keys SHALL be treated as opaque strings and SHALL NOT be interpreted by this contract.

## 4. Deterministic Target Ordering

4.1 If multiple targets are assigned, target descriptors SHALL be ordered deterministically.  
4.2 Ordering SHALL be lexicographic by UTF-8 codepoint of the tuple (`target_type`, `target_id`).  
4.3 Implementations SHALL NOT reorder targets using runtime or environment-derived criteria.

## 5. Publication Manifest Target Recording

5.1 `publication_manifest.json` MAY include a key `targets`.  
5.2 If present, `targets` SHALL be an array of target descriptors.  
5.3 If present, `targets` SHALL comply with Section 3 and Section 4.

## 6. Prohibitions

6.1 Implementations SHALL NOT perform delivery, upload, push, or network actions under this contract.  
6.2 Implementations SHALL NOT consult external mutable state to decide target membership or ordering.  
6.3 Outputs SHALL NOT be SEE artifacts and SHALL NOT be CORE artifacts.

