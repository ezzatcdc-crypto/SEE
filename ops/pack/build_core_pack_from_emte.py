#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from typing import Any, Dict, List

import see_core.canonical as canon
import see_core.validation as v


def _sha256_hex(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def build_core_pack_from_emte(emte: Dict[str, Any], *, engine_id: str, engine_version: str) -> Dict[str, Any]:
    measurements_in = emte["measurements"]
    dimensions: List[str] = sorted({m["universe_id"] for m in measurements_in})

    cr = emte.get("cut_rules", [])
    if not isinstance(cr, list) or any(not isinstance(x, str) for x in cr):
        cr = []

    pack: Dict[str, Any] = {
        "schema_version": "1.0",
        "pack_id": "0" * 64,
        "measurement_universe": {
            "universe_id": _sha256_hex(("UNIVERSE::" + "|".join(dimensions)).encode("utf-8")),
            "as_of": max(m["window"]["end"] for m in measurements_in),
            "dimensions": dimensions,
        },
        "measurements": [],
        "declared_cut_rules": sorted(set(cr)),
        "engine_reference": {"engine_id": engine_id, "engine_version": engine_version},
        "hash_commitment": {"algorithm": "SHA-256", "payload_digest": "0" * 64},
    }

    for m in sorted(measurements_in, key=lambda x: (x["universe_id"], x["window"]["end"])):
        pack["measurements"].append(
            {
                "dimension": m["universe_id"],
                "timestamp": m["window"]["end"],
                "value": int(m["value"]),
            }
        )

    basis = canon.canonicalize_structured_pack_for_hash(pack)
    payload_bytes = canon.dumps_canonical_json(basis)
    digest = _sha256_hex(payload_bytes)

    pack["pack_id"] = digest
    pack["hash_commitment"]["payload_digest"] = digest

    v.validate_and_commit_hash(pack, executing_engine_id=engine_id, executing_engine_version=engine_version)
    return pack


def main() -> int:
    ap = argparse.ArgumentParser(prog="build_core_pack_from_emte")
    ap.add_argument("--in", dest="in_path", required=True)
    ap.add_argument("--out", dest="out_path", required=True)
    ap.add_argument("--engine-id", dest="engine_id", default="SEE_CORE")
    ap.add_argument("--engine-version", dest="engine_version", default="v0")
    args = ap.parse_args()

    emte = json.load(open(args.in_path, "r", encoding="utf-8"))
    pack = build_core_pack_from_emte(emte, engine_id=args.engine_id, engine_version=args.engine_version)

    with open(args.out_path, "w", encoding="utf-8") as f:
        json.dump(pack, f, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        f.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
