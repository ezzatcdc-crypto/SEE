# POSTCORE_PUBLISH Bundle Determinism Contract v1.0

## 1. Scope

1.1 This contract SHALL define deterministic rules for constructing `publication_bundle.zip`.  
1.2 This contract SHALL apply strictly post-POSTCORE_REPORTING.  
1.3 This contract SHALL NOT define distribution targets or transport behavior.

## 2. Inputs

2.1 Implementations SHALL accept as input only a valid report set as defined by POSTCORE_PUBLISH layer specification.  
2.2 Inputs SHALL be treated as read-only.  
2.3 Implementations SHALL reject inputs that do not include `report.md` and `report_manifest.json`.

## 3. Bundle Contents

3.1 `publication_bundle.zip` SHALL contain `report.md` and `report_manifest.json`.  
3.2 If `assets/` exists in the report set, the bundle SHALL include `assets/` and its full contents.  
3.3 The bundle SHALL NOT contain any additional files.  
3.4 The bundle SHALL preserve file bytes exactly as in the input report set.

## 4. Canonical Path Rules

4.1 All archived paths SHALL be relative.  
4.2 Archived paths SHALL use `/` separators.  
4.3 Archived paths SHALL NOT begin with `/` and SHALL NOT contain `..` segments.  
4.4 `report.md` SHALL be archived at path `report.md`.  
4.5 `report_manifest.json` SHALL be archived at path `report_manifest.json`.  
4.6 Asset files SHALL be archived under `assets/` preserving their relative paths under `assets/`.

## 5. Canonical Ordering Rules

5.1 Zip entry ordering SHALL be deterministic.  
5.2 Entries SHALL be ordered lexicographically by UTF-8 codepoint of the full archived path.  
5.3 Directories, if represented as explicit entries, SHALL be ordered using the same rule and SHALL appear before files within the same prefix.

## 6. Zip Metadata Rules

6.1 Zip entry timestamps SHALL be set to a fixed constant value.  
6.2 The fixed constant SHALL be `1980-01-01T00:00:00Z`.  
6.3 Zip entry permissions and attributes SHALL be normalized and SHALL NOT be environment-derived.  
6.4 Compression method SHALL be fixed and SHALL be applied consistently to all entries.  
6.5 If compression is used, the compression level SHALL be fixed.

## 7. Hashing Rules

7.1 Implementations SHALL compute `bundle_hash` over the full bytes of `publication_bundle.zip`.  
7.2 `bundle_hash` SHALL be encoded as lowercase hex.  
7.3 The hash algorithm identifier SHALL be declared in `publication_manifest.json` as `bundle_hash_alg`.  
7.4 `bundle_hash_alg` SHALL be present and SHALL equal `sha256`.

## 8. Idempotence

8.1 For identical input report set bytes, implementations SHALL emit identical `publication_bundle.zip` bytes.  
8.2 Implementations SHALL be idempotent with respect to their outputs.

## 9. Prohibitions

9.1 Implementations SHALL NOT consult current time for bundle construction.  
9.2 Implementations SHALL NOT consult external mutable state for bundle construction.  
9.3 Implementations SHALL NOT include randomized fields, nonces, or environment-derived metadata in the bundle.  
9.4 Outputs SHALL NOT be SEE artifacts and SHALL NOT be CORE artifacts.

