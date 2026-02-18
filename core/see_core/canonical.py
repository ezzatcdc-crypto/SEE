from __future__ import annotations

import json
import math
import re
from datetime import datetime, timezone
from typing import Any, Dict, List, Tuple


_HEX64_RE = re.compile(r"^[0-9a-f]{64}$")


def _is_hex64(s: str) -> bool:
    return bool(_HEX64_RE.match(s))


def _parse_iso8601_utc(ts: str) -> datetime:
    if not isinstance(ts, str) or len(ts) < 20:
        raise ValueError("timestamp_invalid")

    t = ts
    if t.endswith("Z"):
        t = t[:-1] + "+00:00"

    try:
        dt = datetime.fromisoformat(t)
    except Exception as e:
        raise ValueError("timestamp_invalid") from e

    if dt.tzinfo is None:
        raise ValueError("timestamp_not_utc")

    return dt.astimezone(timezone.utc)


def normalize_timestamp(ts: str) -> str:
    dt = _parse_iso8601_utc(ts)
    dt = dt.replace(microsecond=0)
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def _require_finite_number(x: Any) -> float:
    if not isinstance(x, (int, float)):
        raise ValueError("value_not_number")
    xf = float(x)
    if not math.isfinite(xf):
        raise ValueError("value_not_finite")
    return xf


def _sort_unique_strs(items: Any, err_code: str) -> List[str]:
    if not isinstance(items, list) or len(items) == 0:
        raise ValueError(err_code)

    out: List[str] = []
    for v in items:
        if not isinstance(v, str) or v == "":
            raise ValueError(err_code)
        out.append(v)

    out_sorted = sorted(out)
    if out_sorted != out:
        raise ValueError("ordering_violation")
    if len(set(out_sorted)) != len(out_sorted):
        raise ValueError("duplicate_value")
    return out_sorted


def _require_keys_exact(obj: Dict[str, Any], allowed_keys: List[str]) -> None:
    kset = set(obj.keys())
    aset = set(allowed_keys)
    if kset != aset:
        if not aset.issubset(kset):
            raise ValueError("missing_required_field")
        raise ValueError("disallowed_field")


def _canonical_number(n: float) -> Any:
    if float(int(n)) == float(n):
        return int(n)
    return n


def canonicalize_structured_pack_for_hash(pack: Dict[str, Any]) -> Dict[str, Any]:
    if not isinstance(pack, dict):
        raise ValueError("pack_not_object")

    top_order = [
        "schema_version",
        "pack_id",
        "measurement_universe",
        "measurements",
        "declared_cut_rules",
        "engine_reference",
        "hash_commitment",
    ]
    _require_keys_exact(pack, top_order)

    if pack.get("schema_version") != "1.0":
        raise ValueError("schema_version_mismatch")

    pack_id = pack.get("pack_id")
    if not isinstance(pack_id, str) or not _is_hex64(pack_id):
        raise ValueError("pack_id_invalid")

    mu = pack.get("measurement_universe")
    if not isinstance(mu, dict):
        raise ValueError("measurement_universe_invalid")
    _require_keys_exact(mu, ["universe_id", "as_of", "dimensions"])

    universe_id = mu.get("universe_id")
    if not isinstance(universe_id, str) or not _is_hex64(universe_id):
        raise ValueError("universe_id_invalid")

    as_of_norm = normalize_timestamp(mu.get("as_of"))
    dims = _sort_unique_strs(mu.get("dimensions"), "dimensions_invalid")
    dims_set = set(dims)

    measurements = pack.get("measurements")
    if not isinstance(measurements, list) or len(measurements) == 0:
        raise ValueError("measurements_empty")

    canonical_measurements: List[Dict[str, Any]] = []
    last_key: Tuple[str, str] | None = None
    seen_keys: set[Tuple[str, str]] = set()

    for m in measurements:
        if not isinstance(m, dict):
            raise ValueError("measurement_invalid")
        _require_keys_exact(m, ["dimension", "timestamp", "value"])

        dim = m.get("dimension")
        if not isinstance(dim, str) or dim == "":
            raise ValueError("dimension_invalid")
        if dim not in dims_set:
            raise ValueError("dimension_outside_universe")

        ts_norm = normalize_timestamp(m.get("timestamp"))
        val = _require_finite_number(m.get("value"))

        key = (dim, ts_norm)
        if key in seen_keys:
            raise ValueError("duplicate_measurement_key")
        seen_keys.add(key)

        if last_key is not None and key < last_key:
            raise ValueError("ordering_violation")
        last_key = key

        canonical_measurements.append(
            {
                "dimension": dim,
                "timestamp": ts_norm,
                "value": _canonical_number(val),
            }
        )

    dcr = _sort_unique_strs(pack.get("declared_cut_rules"), "declared_cut_rules_invalid")

    er = pack.get("engine_reference")
    if not isinstance(er, dict):
        raise ValueError("engine_reference_invalid")
    _require_keys_exact(er, ["engine_id", "engine_version"])

    engine_id = er.get("engine_id")
    engine_version = er.get("engine_version")
    if not isinstance(engine_id, str) or engine_id == "":
        raise ValueError("engine_id_invalid")
    if not isinstance(engine_version, str) or engine_version == "":
        raise ValueError("engine_version_invalid")

    hc = pack.get("hash_commitment")
    if not isinstance(hc, dict):
        raise ValueError("hash_commitment_invalid")
    _require_keys_exact(hc, ["algorithm", "payload_digest"])

    if hc.get("algorithm") != "SHA-256":
        raise ValueError("hash_algorithm_mismatch")

    payload_digest = hc.get("payload_digest")
    if not isinstance(payload_digest, str) or not _is_hex64(payload_digest):
        raise ValueError("payload_digest_invalid")

    # Hash basis: remove pack_id and hash_commitment.payload_digest
    return {
        "schema_version": "1.0",
        "measurement_universe": {
            "universe_id": universe_id,
            "as_of": as_of_norm,
            "dimensions": dims,
        },
        "measurements": canonical_measurements,
        "declared_cut_rules": dcr,
        "engine_reference": {"engine_id": engine_id, "engine_version": engine_version},
        "hash_commitment": {"algorithm": "SHA-256"},
    }


def dumps_canonical_json(obj: Any) -> bytes:
    s = json.dumps(obj, ensure_ascii=False, separators=(",", ":"), sort_keys=False)
    return s.encode("utf-8")
