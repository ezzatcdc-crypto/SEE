# OPS-PACK-BUILDER-001 v1.0 — Local Pack Builder Tool (Non-SEE)

## 1. Scope
1. This contract SHALL define a local tool that constructs a CORE-ingestable Structured Pack JSON.
2. The tool SHALL be non-SEE and SHALL NOT claim SEE validity.
3. The tool SHALL NOT modify CORE.
4. The tool SHALL NOT introduce runtime state.

## 2. Inputs
1. The tool SHALL accept an input JSON document ("EMTE proposed pack") containing:
   a. measurements: list[object] with universe_id, window.end, value.
   b. cut_rules: list[string] (optional).
2. The tool SHALL treat all inputs as non-SEE data.

## 3. Output
1. The tool SHALL emit a Structured Pack JSON that matches CORE schema exactly.
2. The output SHALL be non-SEE until ingested by CORE.
3. The output digest SHALL be computed EXACTLY as:
   digest = sha256(dumps_canonical_json(canonicalize_structured_pack_for_hash(pack)))
4. The tool SHALL set:
   a. pack_id = digest
   b. hash_commitment.payload_digest = digest

## 4. Prohibitions
1. The tool SHALL NOT emit SEE artifacts.
2. The tool SHALL NOT perform governance logic.
3. The tool SHALL NOT write outside the user-specified output path.
