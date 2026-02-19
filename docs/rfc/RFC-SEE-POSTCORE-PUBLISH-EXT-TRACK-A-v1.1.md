# RFC-SEE-POSTCORE-PUBLISH-EXT-TRACK-A v1.1
## Deterministic Bundle Packaging Profile

Status: EXTENSION  
Layer: POSTCORE_PUBLISH  
Authority: Post-POSTCORE_REPORTING Only  

Scope

1. This extension SHALL define a deterministic packaging profile applied strictly after POSTCORE_REPORTING.
2. This extension SHALL NOT modify POSTCORE_PUBLISH v1.0 contracts.
3. This extension SHALL NOT modify any frozen authority.

Inputs

4. Inputs SHALL be limited to finalized POSTCORE_REPORTING output bundles.
5. Inputs SHALL be treated as immutable.
6. No CORE artifact SHALL be directly accessed.

Outputs

7. Output SHALL be a deterministic publishable bundle.
8. Output SHALL be a non-SEE artifact.
9. Output SHALL NOT be ingestible by CORE.
10. Output SHALL NOT alter any upstream artifact.

Archive Canonicalization Rules

11. Archive format SHALL be TAR (POSIX ustar subset) without extended headers.
12. PAX headers SHALL NOT be used.
13. GNU extensions SHALL NOT be used.
14. File ordering SHALL be lexicographically sorted by UTF-8 filename.
15. Directory traversal SHALL be lexicographically sorted.
16. File mode SHALL be fixed to 0644.
17. Directory mode SHALL be fixed to 0755.
18. UID SHALL be 0.
19. GID SHALL be 0.
20. Uname SHALL be empty.
21. Gname SHALL be empty.
22. mtime SHALL be 0.
23. Only regular files and directories SHALL be permitted.
24. Symbolic links SHALL NOT be permitted.
25. No special files SHALL be permitted.
26. All paths SHALL be relative and use "/" separators.
27. No path SHALL contain "..".
28. No absolute paths SHALL be permitted.
29. No root directory entry SHALL be included.

Content Rules

30. Text files SHALL be UTF-8 without BOM.
31. Line endings SHALL be LF only.
32. File content bytes SHALL NOT be modified.

Hashing

33. Final archive hash SHALL use SHA-256.
34. Hash SHALL be computed over exact TAR byte stream.
35. Hash SHALL be lowercase hexadecimal without prefix.

Manifest

36. A separate manifest SHALL be generated.
37. Manifest SHALL NOT be embedded inside TAR.
38. Manifest SHALL include archive filename.
39. Manifest SHALL include SHA-256 hash.
40. Manifest SHALL include total byte length.
41. Manifest SHALL include lexicographically sorted path list.
42. Manifest SHALL contain no timestamps.
43. Manifest SHALL be deterministic JSON.
44. JSON keys SHALL be lexicographically ordered.
45. No insignificant whitespace SHALL be emitted.
46. Numbers SHALL be base-10 without leading zeros.
47. Encoding SHALL be UTF-8 with LF only.

Prohibitions

48. No runtime state SHALL be introduced.
49. No shared state with CORE, LAB, or CONTROL SHALL exist.
50. No upstream influence SHALL occur.
51. No encryption SHALL occur.
52. No signing SHALL occur.
53. No transport behavior SHALL be introduced.
54. No SEE artifact SHALL be generated.

Determinism

55. Identical inputs SHALL produce identical archive bytes.
56. Identical inputs SHALL produce identical hash.
57. Output SHALL be reproducible across platforms.
58. Implementation SHALL ignore host filesystem metadata.
59. Implementation SHALL ignore timezone, locale, and environment variables.

Termination

60. On rule violation, packaging SHALL fail.
61. On failure, no archive SHALL remain.
62. On failure, no manifest SHALL remain.
63. This extension SHALL remain a stateless terminal transform.
