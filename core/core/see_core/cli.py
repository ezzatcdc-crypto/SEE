import argparse
from pathlib import Path
from .engine import run_core

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--pack", required=True)
    p.add_argument("--out", required=True)
    args = p.parse_args()
    result = run_core(Path(args.pack), Path(args.out))
    print(result)
