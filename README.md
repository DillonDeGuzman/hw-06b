# hw-06b

Triangle classification testing and targeted defect repairs.

Run with Python 3 (no external dependencies):

```sh
python3 -m unittest TestTriangle
```

Original run: **19/81 passed**, 50 failures, 12 errors.
Repaired run: **81/81 passed**.

See [the assignment summary](ASSIGNMENT_SUMMARY.md) for both full test reports, the summary matrix, assumptions, defect descriptions, and submission checklist. Complete the personal reflection and honor pledge before submitting.

- [Repaired source](Triangle.py)
- [Test suite](TestTriangle.py)
- [Final test output](results/final_unittest.txt)
- [Original files](originals/)

The Git history preserves the original files before expanded tests and then targeted fixes. To reproduce a report for the current implementation, run `python3 make_report.py final`. Original-run reports were captured before repairs and should be preserved.
