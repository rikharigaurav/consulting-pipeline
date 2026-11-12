#!/usr/bin/env python3
"""Build docs/project-log.xlsx from the append-only CSVs in log/.

Deterministic on purpose: no model in this path, so no invented rows.
Run at every gate.  Usage: python scripts/log_compile.py [repo_root]
"""
import csv, sys, pathlib
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment

SHEETS = [
    ("timeline",    "Timeline"),
    ("gates",       "Gate Log"),
    ("claims",      "Claims"),
    ("conflicts",   "Conflicts"),
    ("scope-stops", "Scope Stops"),
    ("limitations", "Limitations"),
    ("files",       "Files"),
]
HDR_FILL = PatternFill("solid", fgColor="1A2430")
HDR_FONT = Font(bold=True, color="FFFFFF", size=10)


def main(root="."):
    root = pathlib.Path(root)
    logs, out = root / "log", root / "docs"
    out.mkdir(exist_ok=True)
    wb = Workbook()
    wb.remove(wb.active)
    rejected = []

    for stem, title in SHEETS:
        ws = wb.create_sheet(title)
        path = logs / f"{stem}.csv"
        if not path.exists():
            ws["A1"] = f"no {stem}.csv yet"
            continue
        with path.open(newline="", encoding="utf-8") as fh:
            rows = list(csv.reader(fh))
        width = len(rows[0]) if rows else 0
        for r in rows:
            if width and len(r) != width:
                rejected.append([stem, ",".join(r)])   # G: never drop silently
                continue
            ws.append(r)
        for c in ws[1]:
            c.fill, c.font = HDR_FILL, HDR_FONT
        ws.freeze_panes = "A2"
        if width:
            ws.auto_filter.ref = ws.dimensions
        for col in ws.columns:
            longest = max((len(str(c.value or "")) for c in col), default=0)
            ws.column_dimensions[col[0].column_letter].width = min(max(longest + 2, 10), 52)
            for c in col:
                c.alignment = Alignment(vertical="top", wrap_text=True)

    ws = wb.create_sheet("Rejected")
    ws.append(["source", "raw line"])
    for row in rejected:
        ws.append(row)
    for c in ws[1]:
        c.fill, c.font = HDR_FILL, HDR_FONT

    dest = out / "project-log.xlsx"
    wb.save(dest)
    print(f"wrote {dest} ({len(rejected)} rejected rows)")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
