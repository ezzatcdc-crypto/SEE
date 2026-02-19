# POSTCORE_PUBLISH Bundle Packaging Profile Contract v1.1

## 1. Scope

1.1 This contract SHALL define a deterministic bundle packaging profile applied strictly after POSTCORE_REPORTING.  
1.2 This contract SHALL NOT modify POSTCORE_PUBLISH v1.0 contracts.  
1.3 This contract SHALL NOT modify CORE behavior.  
1.4 This contract SHALL NOT introduce transport behavior.  
1.5 This contract SHALL NOT introduce runtime state.

## 2. Inputs

2.1 Inputs SHALL be limited to finalized POSTCORE_REPORTING output bundles.  
2.2 Inputs SHALL be treated as immutable.  
2.3 No CORE artifact SHALL be directly accessed.

## 3. Outputs

3.1 Output SHALL be a publishable bundle archive.  
3.2 Output SHALL be a non-SEE artifact.  
3.3 Output SHALL NOT be ingestible by CORE.  
3.4 Output SHALL NOT alter any upstream artifact.

## 4. Archive Format

4.1 Archive format SHALL be TAR (POSIX ustar subset).  
4.2 PAX headers SHALL NOT be used.  
4.3 GNU extensions SHALL NOT be used.  
4.4 Only regular files and directories SHALL be permitted.  
4.5 Symbolic links SHALL NOT be permitted.  
4.6 Special files SHALL NOT be permitted.

## 5. Canonicalization

5.1 File ordering within the archive SHALL be lexicographically sorted by UTF-8 path.  
5.2 Directory traversal order SHALL be lexicographically sorted.  
5.3 All paths SHALL be relative.  
5.4 All paths SHALL use "/" separators.  
5.5 No path SHALL contain "..".  
5.6 No absolute paths SHALL be permitted.  
5.7 No root directory entry SHALL be included.

## 6. Metadata Normalization

6.1 File mode SHALL be fixed to 0644 for files.  
6.2 Directory mode SHALL be fixed to 0755 for directories.  
6.3 UID SHALL be 0.  
6.4 GID SHALL be 0.  
6.5 Uname SHALL be empty.  
6.6 Gname SHALL be empty.  
6.7 mtime SHALL be 0 for all entries.  

## 7. Hashing

7.1 The packaging process SHALL emit `publish_bundle_manifest.json`.  
7.2 `publish_bundle_manifest.json` SHALL include:

- `publish_bundle_archive_name` (string)
- `publish_bundle_archive_size_bytes` (number)
- `publish_bundle_archive_hash_alg` (string)
- `publish_bundle_archive_hash` (string)

7.3 `publish_bundle_archive_hash_alg` SHALL equal `sha256`.  
7.4 `publish_bundle_archive_hash` SHALL be lowercase hex.  
7.5 `publish_bundle_archive_hash` SHALL be computed over the full bytes of the TAR archive.  
7.6 The TAR bytes SHALL be taken exactly as emitted.

## 8. Manifest Determinism

8.1 `publish_bundle_manifest.json` SHALL be deterministic JSON.  
8.2 JSON keys SHALL be lexicographically ordered.  
8.3 No insignificant whitespace SHALL be emitted.  
8.4 Numbers SHALL be base-10 without leading zeros.  
8.5 Encoding SHALL be UTF-8 with LF line endings only.  
8.6 The manifest SHALL contain no timestamps.  
8.7 The manifest SHALL contain no environment identifiers.

## 9. Determinism

9.1 For identical inputs, the TAR bytes SHALL be identical.  
9.2 For identical inputs, all emitted hashes SHALL be identical.  
9.3 Packaging SHALL ignore host filesystem metadata.  
9.4 Packaging SHALL NOT depend on locale, timezone, clock, or environment variables.

## 10. Prohibitions

10.1 Packaging SHALL NOT consult external mutable state.  
10.2 Packaging SHALL NOT persist caches or runtime state.  
10.3 Packaging SHALL NOT perform encryption.  
10.4 Packaging SHALL NOT perform signing.  
10.5 Outputs SHALL NOT be SEE artifacts and SHALL NOT be CORE artifacts.  
10.6 Packaging SHALL NOT signal status back to CORE.  
10.7 Packaging SHALL NOT introduce bidirectional coupling.

## 11. Failure Semantics

11.1 On any rule violation, packaging SHALL fail.  
11.2 On failure, no archive SHALL remain.  
11.3 On failure, no manifest SHALL remain.  
