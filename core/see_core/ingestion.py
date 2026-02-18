import json
from pathlib import Path


class IngestionError(Exception):
    pass


def ingest(pack_path: Path) -> dict:
    """
    CORE ingestion boundary.
    Validity is created ONLY here.
    """

    if not pack_path.exists():
        raise IngestionError(f"PACK_NOT_FOUND: {pack_path}")

    try:
        pack = json.loads(pack_path.read_text(encoding="utf-8"))
    except Exception as e:
        raise IngestionError(f"PACK_INVALID_JSON: {e}") from e

    # Minimal non-semantic structural check (placeholder for the real schema contract)
    if not isinstance(pack, dict):
        raise IngestionError("PACK_ROOT_NOT_OBJECT")

    # The ingestion layer is the only place that may accept/reject.
    # Anything else (Template/SPB) is eligibility only.

    return pack
