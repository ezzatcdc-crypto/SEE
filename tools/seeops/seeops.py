import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import typer
from jsonschema import Draft202012Validator

app = typer.Typer(add_completion=False, no_args_is_help=True)

ROOT = Path(__file__).resolve().parents[2]
SCHEMAS = ROOT / "schemas"

def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()

def canonical_json_bytes(obj: Any) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")

def sha256_prefixed(data: bytes) -> str:
    h = hashlib.sha256()
    h.update(data)
    return "sha256:" + h.hexdigest()

def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))

def write_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

def load_schema(schema_name: str) -> Any:
    p = SCHEMAS / schema_name
    if not p.exists():
        raise typer.BadParameter(f"Schema not found: {p}")
    return read_json(p)

def validate_instance(schema_name: str, instance_path: Path) -> Any:
    schema = load_schema(schema_name)
    inst = read_json(instance_path)
    v = Draft202012Validator(schema)
    errors = sorted(v.iter_errors(inst), key=lambda e: e.path)
    if errors:
        for e in errors[:50]:
            loc = ".".join([str(x) for x in e.path]) if e.path else "<root>"
            typer.echo(f"{loc}: {e.message}", err=True)
        raise typer.Exit(code=2)
    return inst

@app.command("version")
def version_cmd():
    typer.echo("seeops 0.2.0")

@app.command("hash-json")
def hash_json(path: str):
    p = Path(path)
    obj = read_json(p)
    typer.echo(sha256_prefixed(canonical_json_bytes(obj)))

@app.command("validate-json")
def validate_json(schema: str, path: str):
    validate_instance(schema, Path(path))
    typer.echo("OK")

@app.command("init-registry")
def init_registry(registry_id: str, version: str, out: str = "ops/concepts/registry"):
    obj = {
        "schema_version": "1.0",
        "registry_id": registry_id,
        "version": version,
        "issued_at": now_iso(),
        "concepts": [
            {
                "concept_id": "EXAMPLE_CONCEPT",
                "name": "Example Concept",
                "definition": "Replace this with the canonical definition."
            }
        ]
    }
    out_path = ROOT / out / registry_id / f"{version}.json"
    write_json(out_path, obj)
    validate_instance("ops_concept_registry.schema.json", out_path)
    typer.echo(str(out_path))
    typer.echo(sha256_prefixed(canonical_json_bytes(obj)))

@app.command("init-lab-snapshot")
def init_lab_snapshot(
    snapshot_id: str,
    version: str,
    paradigm_ref: str,
    concept_registry_path: str,
    out: str = "lab/config_snapshots",
):
    reg_path = Path(concept_registry_path)
    reg_obj = read_json(reg_path)
    reg_hash = sha256_prefixed(canonical_json_bytes(reg_obj))

    obj = {
        "schema_version": "1.0",
        "snapshot_id": snapshot_id,
        "version": version,
        "issued_at": now_iso(),
        "paradigm_ref": paradigm_ref,
        "concept_registry_hash": reg_hash,
        "indicator_map": [
            {
                "indicator_id": "EXAMPLE_INDICATOR",
                "concept_id": "EXAMPLE_CONCEPT",
                "rule_ref": "rules/example_rule@1.0",
                "units": "unitless",
                "window": "P30D"
            }
        ],
        "measurement_schema": {
            "measurements": [
                {
                    "measurement_id": "EXAMPLE_MEASUREMENT",
                    "indicator_id": "EXAMPLE_INDICATOR",
                    "dtype": "float",
                    "nullable": False
                }
            ]
        }
    }

    out_path = ROOT / out / snapshot_id / f"{version}.json"
    write_json(out_path, obj)
    validate_instance("lab_config_snapshot.schema.json", out_path)
    typer.echo(str(out_path))
    typer.echo(sha256_prefixed(canonical_json_bytes(obj)))

@app.command("make-manifest")
def make_manifest(
    run_id: str,
    structured_pack_path: str,
    concept_registry_hash: str,
    lab_config_hash: str,
    out: str = "control/packs",
):
    pack_path = Path(structured_pack_path)
    pack_hash = sha256_prefixed(pack_path.read_bytes())

    obj = {
        "schema_version": "1.0",
        "run_id": run_id,
        "issued_at": now_iso(),
        "structured_pack_path": str(pack_path),
        "structured_pack_hash": pack_hash,
        "concept_registry_hash": concept_registry_hash,
        "lab_config_hash": lab_config_hash
    }

    out_path = ROOT / out / run_id / "manifest.json"
    write_json(out_path, obj)
    validate_instance("control_pack_manifest.schema.json", out_path)
    typer.echo(str(out_path))
    typer.echo(sha256_prefixed(canonical_json_bytes(obj)))

if __name__ == "__main__":
    app()
