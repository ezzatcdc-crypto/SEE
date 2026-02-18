import json
from pathlib import Path
from tempfile import TemporaryDirectory
from see_core.engine import run_core

def test_same_pack_same_commitment():
    pack = {"a": 1}

    with TemporaryDirectory() as td:
        td = Path(td)
        p = td / "pack.json"
        p.write_text(json.dumps(pack))

        out1 = td / "o1"
        out2 = td / "o2"
        out1.mkdir()
        out2.mkdir()

        r1 = run_core(p, out1)
        r2 = run_core(p, out2)

        assert r1["run_commitment"] == r2["run_commitment"]
