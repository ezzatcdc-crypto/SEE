from __future__ import annotations

import hashlib
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

from .canonical import canonicalize_structured_pack_for_hash, dumps_canonical_json


@dataclass(frozen=False)
class IngestionRejection(Exception):
    code: str

    def __str__(self) -> str:
        return self.code


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def validate_and_commit_hash(
    pack: Dict[str, Any],
    *,
    executing_engine_id: str,
    executing_engine_version: str,
    allowed_cut_rules: Optional[List[str]] = None,
) -> Tuple[bytes, str]:
    try:
        basis = canonicalize_structured_pack_for_hash(pack)
    except ValueError as e:
        raise IngestionRejection(str(e)) from e

    er = pack["engine_reference"]
    if er["engine_id"] != executing_engine_id or er["engine_version"] != executing_engine_version:
        raise IngestionRejection("engine_reference_mismatch")

    if allowed_cut_rules is not None:
        allowed = set(allowed_cut_rules)
        for r in pack["declared_cut_rules"]:
            if r not in allowed:
                raise IngestionRejection("unknown_cut_rule")

    payload_bytes = dumps_canonical_json(basis)
    digest = sha256_hex(payload_bytes)

    if pack["pack_id"] != digest:
        raise IngestionRejection("hash_commitment_mismatch")
    if pack["hash_commitment"]["payload_digest"] != digest:
        raise IngestionRejection("hash_commitment_mismatch")

    return payload_bytes, digest
