import json
from hashlib import sha256
from pathlib import Path

def _stable(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()

def run_core(pack_path: Path, out_dir: Path):
    pack = json.loads(pack_path.read_text())
    commitment = sha256(_stable(pack)).hexdigest()

    run_dir = out_dir / "runs" / commitment
    run_dir.mkdir(parents=True)

    data_snapshot = {"structured_pack": pack}
    indicators = {"indicators": []}
    patterns_drift = {"patterns": [], "drift": []}
    timeline = {"timeline": []}

    for name, payload in {
        "data_snapshot.json": data_snapshot,
        "indicators.json": indicators,
        "patterns_drift.json": patterns_drift,
        "timeline.json": timeline,
    }.items():
        (run_dir / name).write_bytes(_stable(payload))

    manifest = {
        "run_commitment": commitment,
        "artifacts": sorted([
            "data_snapshot.json",
            "indicators.json",
            "patterns_drift.json",
            "timeline.json"
        ])
    }

    (run_dir / "run_manifest.json").write_bytes(_stable(manifest))

    return {"run_commitment": commitment}
