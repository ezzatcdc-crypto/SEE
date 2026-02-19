Local tool:
- Input: EMTE proposed pack (non-CORE shape)
- Output: CORE Structured Pack JSON (CORE schema) + correct pack_id/digest

Usage:
python ops/pack/build_core_pack_from_emte.py --in <in.json> --out <out.json> --engine-id SEE_CORE --engine-version v0

Ingestion:
python - <<'PY'
from see_core.ingestion import ingest_structured_pack
raw=open("<out.json>","rb").read()
artifacts = ingest_structured_pack(raw, executing_engine_id="SEE_CORE", executing_engine_version="v0")
print(sorted(artifacts.keys()))
PY
