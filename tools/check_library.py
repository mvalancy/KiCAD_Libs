#!/usr/bin/env python3
"""
Integrity checks for this KiCad library.

There is nothing to build and no test suite here, so these check the three
ways the library can be wrong in a way that only bites the person who
installs it:

  --footprints   every .kicad_mod is a balanced s-expression. An unbalanced
                 one will not load in KiCad.
  --symbols      every .lib has its matching .dcm. Without it the symbol
                 descriptions and keywords silently disappear.
  --no-backups   no editor backups (.bak/.bck/~) are committed. Three were
                 in the tree before this script existed.
  --inventory    print what the library contains (informational).
"""
import argparse
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent


def balanced(text: str) -> bool:
    """S-expression paren balance, ignoring parens inside quoted strings."""
    depth = 0
    in_string = False
    escaped = False
    for ch in text:
        if escaped:
            escaped = False
            continue
        if ch == "\\":
            escaped = True
            continue
        if ch == '"':
            in_string = not in_string
            continue
        if in_string:
            continue
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
            if depth < 0:
                return False
    return depth == 0


def check_footprints() -> int:
    mods = sorted(ROOT.rglob("*.kicad_mod"))
    bad = [m for m in mods if not balanced(m.read_text(errors="replace"))]
    print(f"footprints: {len(mods)} checked, {len(bad)} unbalanced")
    for m in bad:
        print(f"  UNBALANCED {m.relative_to(ROOT)}")
    return 1 if bad else 0


def check_symbols() -> int:
    symbols = ROOT / "Symbols"
    problems = []
    libs = sorted(symbols.glob("*.lib"))
    for lib in libs:
        if not lib.with_suffix(".dcm").exists():
            problems.append(f"{lib.name} has no matching .dcm")
    for dcm in sorted(symbols.glob("*.dcm")):
        if not dcm.with_suffix(".lib").exists():
            problems.append(f"{dcm.name} has no matching .lib")
    print(f"symbols: {len(libs)} .lib checked, {len(problems)} problems")
    for p in problems:
        print(f"  {p}")
    return 1 if problems else 0


def check_no_backups() -> int:
    patterns = ("*.bak", "*.bck", "*~", "*-bak")
    found = [f for pat in patterns for f in ROOT.rglob(pat) if ".git" not in f.parts]
    print(f"backup files: {len(found)}")
    for f in found:
        print(f"  COMMITTED BACKUP {f.relative_to(ROOT)}")
    return 1 if found else 0


def inventory() -> int:
    print(f"footprints:  {len(list(ROOT.rglob('*.kicad_mod')))}")
    print(f".pretty dirs: {len(list(ROOT.glob('Footprints/*.pretty')))}")
    print(f"symbol libs: {len(list((ROOT / 'Symbols').glob('*.lib')))}")
    models = [f for ext in ('*.stp', '*.step', '*.STEP') for f in ROOT.rglob(ext)]
    print(f"3d models:   {len(models)}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--footprints", action="store_true")
    ap.add_argument("--symbols", action="store_true")
    ap.add_argument("--no-backups", action="store_true")
    ap.add_argument("--inventory", action="store_true")
    args = ap.parse_args()

    if args.footprints:
        return check_footprints()
    if args.symbols:
        return check_symbols()
    if args.no_backups:
        return check_no_backups()
    if args.inventory:
        return inventory()
    ap.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
