from __future__ import annotations

import json
from typing import Any, Dict, Optional, Tuple

from .validation import IngestionRejection, validate_and_commit_hash


def ingest_structured_pack(
    raw_json: bytes,
    *,
    executing_engine_id: str,
    executing_engine_version: str,
    allowed_cut_rules: Optional[list[str]] = None,
) -> Tuple[Dict[str, Any], str]:
    try:
        obj = json.loads(raw_json.decode("utf-8"))
    except Exception as e:
        raise IngestionRejection("pack_not_valid_json") from e

    if not isinstance(obj, dict):
        raise IngestionRejection("pack_not_object")

    _payload_bytes, digest = validate_and_commit_hash(
        obj,
        executing_engine_id=executing_engine_id,
        executing_engine_version=executing_engine_version,
        allowed_cut_rules=allowed_cut_rules,
    )
    return obj, digest
