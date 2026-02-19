# POSTCORE_REPORTING Formats Contract v1.0 (Formats + Canonical Ordering Rules)

## 1. Scope

1.1 This contract SHALL define only output formats and canonical ordering rules for POSTCORE_REPORTING reports.  
1.2 This contract SHALL apply strictly post-CORE.  
1.3 This contract SHALL NOT define artifact-to-section mapping rules.  
1.4 This contract SHALL NOT define rendering styles beyond deterministic structure requirements.

## 2. Report Set Structure

2.1 A report set SHALL contain exactly one primary file named `report.md`.  
2.2 A report set MAY contain auxiliary files in a directory named `assets/`.  
2.3 If `assets/` exists, `report.md` SHALL reference auxiliary files using relative paths only.  
2.4 A report set SHALL contain a manifest file named `report_manifest.json`.

## 3. report_manifest.json Requirements

3.1 `report_manifest.json` SHALL be valid JSON encoded in UTF-8.  
3.2 `report_manifest.json` SHALL contain, at minimum, the following keys:

- `schema_version` (string)
- `report_id` (string)
- `generated_from_run_id` (string)
- `primary_report` (string) and SHALL equal `report.md`
- `aux_files` (array of strings)

3.3 `aux_files` SHALL list relative paths under `assets/` only.  
3.4 `aux_files` SHALL be ordered lexicographically by UTF-8 codepoint.

## 4. report.md Requirements

4.1 `report.md` SHALL be UTF-8 encoded.  
4.2 `report.md` line endings SHALL be LF.  
4.3 `report.md` SHALL use Markdown heading syntax with `#` for the document title and `##` for top-level sections.  
4.4 The first line of `report.md` SHALL be a single title line beginning with `# `.  
4.5 `report.md` SHALL include only deterministic content derived from CORE artifacts.

## 5. Canonical Text Serialization

5.1 All scalar values rendered into `report.md` SHALL be serialized deterministically.  
5.2 Strings SHALL be rendered exactly as present in the source artifact, without locale transforms.  
5.3 Numbers SHALL be rendered in base-10 without thousands separators.  
5.4 Booleans SHALL be rendered as `true` or `false`.  
5.5 Null SHALL be rendered as `null`.

## 6. Canonical Ordering Rules

6.1 All lists rendered into `report.md` that are not explicitly order-preserving by their source SHALL be sorted lexicographically by UTF-8 codepoint of their canonical string representation.  
6.2 All maps rendered into `report.md` SHALL be ordered by lexicographic UTF-8 codepoint of full key path.  
6.3 If multiple ordering rules could apply, the more specific rule SHALL take precedence over the more general rule.

## 7. Path and Naming Constraints

7.1 Filenames SHALL be case-sensitive and SHALL use ASCII only.  
7.2 Filenames SHALL NOT contain spaces.  
7.3 Directory separators SHALL be `/`.  
7.4 Implementations SHALL NOT emit absolute paths in any output.  
7.5 Implementations SHALL NOT emit OS-specific path prefixes.

## 8. Prohibitions

8.1 Implementations SHALL NOT consult external mutable state to determine formatting or ordering.  
8.2 Implementations SHALL NOT consult current time for formatting or ordering content beyond what is present in CORE artifacts.  
8.3 Implementations SHALL NOT modify any CORE artifact.  
8.4 Outputs SHALL NOT be SEE artifacts and SHALL NOT be CORE artifacts.

