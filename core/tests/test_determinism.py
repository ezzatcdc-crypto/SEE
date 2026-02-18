import json
import hashlib
import pytest

from see_core.ingestion import ingest_structured_pack
from see_core.canonical import dumps_canonical_json


ENGINE_ID = "SEE-CORE"
ENGINE_VERSION = "1.0"


def _sha256_hex(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def _pack_base():
    basis = {
        "schema_version": "1.0",
        "measurement_universe": {
            "universe_id": "0" * 64,
            "as_of": "2026-02-18T00:00:00Z",
            "dimensions": ["Energy", "Flow"],
        },
        "measurements": [
            {"dimension": "Energy", "timestamp": "2026-02-18T00:00:00Z", "value": 1},
            {"dimension": "Flow", "timestamp": "2026-02-18T00:00:01Z", "value": 2},
        ],
        "declared_cut_rules": ["تشغيل≠تحول", "تعويض بيئي≠استقرار"],
        "engine_reference": {"engine_id": ENGINE_ID, "engine_version": ENGINE_VERSION},
        "hash_commitment": {"algorithm": "SHA-256"},
    }
    payload = dumps_canonical_json(basis)
    digest = _sha256_hex(payload)

    return {
        "schema_version": "1.0",
        "pack_id": digest,
        "measurement_universe": basis["measurement_universe"],
        "measurements": basis["measurements"],
        "declared_cut_rules": basis["declared_cut_rules"],
        "engine_reference": basis["engine_reference"],
        "hash_commitment": {"algorithm": "SHA-256", "payload_digest": digest},
    }


def _raw(pack):
    return json.dumps(pack, ensure_ascii=False, separators=(",", ":")).encode("utf-8")


def test_identical_pack_yields_identical_digest():
    p1 = _pack_base()
    p2 = _pack_base()
    _obj1, d1 = ingest_structured_pack(
        _raw(p1),
        executing_engine_id=ENGINE_ID,
        executing_engine_version=ENGINE_VERSION,
        allowed_cut_rules=p1["declared_cut_rules"],
    )
    _obj2, d2 = ingest_structured_pack(
        _raw(p2),
        executing_engine_id=ENGINE_ID,
        executing_engine_version=ENGINE_VERSION,
        allowed_cut_rules=p2["declared_cut_rules"],
    )
    assert d1 == d2


def test_extra_top_level_field_rejected():
    p = _pack_base()
    p["x"] = 1
    with pytest.raises(Exception) as e:
        ingest_structured_pack(
            _raw(p),
            executing_engine_id=ENGINE_ID,
            executing_engine_version=ENGINE_VERSION,
            allowed_cut_rules=p["declared_cut_rules"],
        )
    assert str(e.value) == "disallowed_field"


def test_dimension_outside_universe_rejected():
    p = _pack_base()
    p["measurements"][0]["dimension"] = "Nexus"
    with pytest.raises(Exception) as e:
        ingest_structured_pack(
            _raw(p),
            executing_engine_id=ENGINE_ID,
            executing_engine_version=ENGINE_VERSION,
            allowed_cut_rules=p["declared_cut_rules"],
        )
    assert str(e.value) == "dimension_outside_universe"


def test_measurement_ordering_violation_rejected():
    p = _pack_base()
    p["measurements"] = list(reversed(p["measurements"]))
    with pytest.raises(Exception) as e:
        ingest_structured_pack(
            _raw(p),
            executing_engine_id=ENGINE_ID,
            executing_engine_version=ENGINE_VERSION,
            allowed_cut_rules=p["declared_cut_rules"],
        )
    assert str(e.value) == "ordering_violation"


def test_timestamp_variation_normalizes_and_digest_stays_same():
    p = _pack_base()
    p["measurements"][0]["timestamp"] = "2026-02-18T00:00:00.123Z"
    _obj, d = ingest_structured_pack(
        _raw(p),
        executing_engine_id=ENGINE_ID,
        executing_engine_version=ENGINE_VERSION,
        allowed_cut_rules=p["declared_cut_rules"],
    )
    assert d == p["pack_id"]
