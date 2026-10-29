"""Capture actual results from the current implementation (no fabricated rows)."""
import argparse
import csv
from pathlib import Path
from TestTriangle import CASES
from Triangle import classifyTriangle

parser = argparse.ArgumentParser()
parser.add_argument("run", choices=["initial", "final"])
args = parser.parse_args()
rows = []
for test_id, label, sides, expected in CASES:
    try:
        actual = classifyTriangle(*sides)
    except Exception as exc:
        actual = f"{type(exc).__name__}: {exc}"
    rows.append([test_id, repr(sides), expected, actual,
                 "Pass" if actual == expected else "Fail"])
out = Path(__file__).parent / "results"
out.mkdir(exist_ok=True)
with (out / f"{args.run}_report.csv").open("w", newline="") as stream:
    writer = csv.writer(stream)
    writer.writerow(["Test ID", "Input", "Expected Results", "Actual Result", "Pass or Fail"])
    writer.writerows(rows)
header = "| Test ID | Input | Expected Results | Actual Result | Pass or Fail |\n|---|---|---|---|---|\n"
body = "".join("| " + " | ".join(row) + " |\n" for row in rows)
passed = sum(row[-1] == "Pass" for row in rows)
(out / f"{args.run}_report.md").write_text(
    f"# {args.run.title()} test report\n\n{len(rows)} executed; {passed} passed; {len(rows)-passed} failed.\n\n" + header + body)
print(f"{args.run}: {len(rows)} executed; {passed} passed; {len(rows)-passed} failed")
