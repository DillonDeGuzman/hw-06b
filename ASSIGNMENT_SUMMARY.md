# Assignment summary: Triangle testing and repair

## 1. Assignment Description

The objective of this assignment is to (a) develop a set of test cases for an existing triangle classification program, (b) use those test cases to find and fix defects in that program, and (c) report on testing results for the Triangle problem.

Preserve and commit the supplied Triangle.py and TestTriangle.py, expand only the test suite first, record its results against the original implementation, then repair the existing classification logic and execute the same suite again. Deliver both source files, before/after reports, final execution output, a summary matrix, a testing sufficiency strategy, and the repository name. The complete supplied instructions are preserved in ASSIGNMENT_INSTRUCTIONS.txt.

## 2. Author

Dillon DeGuzman — confirm your preferred name before submission.

## 3. Summary

The original implementation passed 19 of 81 tests. It produced 50 assertion failures and 12 errors. The repaired implementation passed all 81 of the same tests with no failures or errors. Seven distinct code defects were identified by tests and code inspection and repaired. Existing validation and classification branches were retained and corrected; the implementation was not replaced with another assignment's solution.

| Metric | Test Run 1: Original | Test Run 2: Repaired |
|---|---:|---:|
| Tests Planned | 81 | 81 |
| Tests Executed | 81 | 81 |
| Tests Passed | 19 | 81 |
| Defects Found | 7 | 0 new |
| Defects Fixed | 0 | 7 |

“Defects Found” counts distinct causes, not failed cases. All seven were identified through initial testing plus code inspection; some downstream defects were masked by earlier checks. “Defects Fixed” counts repairs applied since the preceding run. Initial exceptions count as unsuccessful executions in the report, while unittest distinguishes errors from assertion failures.

### Reflection — complete in your own words

[Describe what you personally learned, what worked, and what did not. Useful observations from these results: an early validation defect can hide downstream defects; passing invalid-input tests alone does not establish correctness; side-order permutations expose assumptions about parameter positions. Review and explain the changes yourself before submitting.]

## 5. Honor pledge

[Insert the exact pledge required by your course and sign it yourself only if accurate. Disclose AI assistance as required by your instructor. Code, tests, and report were prepared with Codex assistance; do not represent that assistance as unaided work.]

## 6. Detailed results

### Techniques and sufficiency strategy

The suite uses equivalence partitioning (triangle types, invalid triangles, and invalid inputs), boundary values (0, 1, 200, and 201), and permutations of representative side lengths. It retains the three starter examples. Degenerate and overlong sides exercise equality and strict triangle-inequality failures. Unequal, equilateral, and exactly-two-equal sides exercise each classification. Right-triangle examples include multiple triples and a hypotenuse of 200. Invalid types are placed independently in all three parameters.

The stopping criterion was coverage of every documented result category, every validation parameter, each equality arrangement, both triangle-inequality failure modes, and right triangles in all side orders, with regressions for the inspected defects and all planned tests passing. This supports confidence within the stated contract; it is not an exhaustive proof for every possible Python object or all 8,000,000 integer triples.

### Assumptions and constraints

- Inputs must be built-in integers from 1 through 200 inclusive. Zero is invalid despite an inconsistent starter comment suggesting “>= 0.”
- Booleans are invalid even though Python treats bool as an int subclass. Floats, including integer-valued floats, strings, None, lists, and complex numbers return InvalidInput without raising errors.
- Preserve the starter API's spelling Isoceles, plus Equilateral, Scalene, Right, NotATriangle, and InvalidInput.
- All pair sums must be strictly greater than the remaining side. Equal sums are degenerate and return NotATriangle.
- The right-triangle rule uses squared lengths. Side order must not change classification.
- Type and range validation precede geometric classification. No external packages are required.

### Defects and repairs

| ID | Original defect | Targeted repair | Representative coverage |
|---|---|---|---|
| D1 | b <= b is always true for ordinary numeric inputs | Compare b to zero | Starter valid cases; zero and negative b |
| D2 | Numeric comparisons precede type validation, and isinstance accepts bool | Validate exact integer types before comparisons | String, None, complex, list, float, and boolean in each position |
| D3 | Triangle checks incorrectly subtract two sides | Compare each side to the sum of the other two | Valid triangles and permutations of degenerate/overlong triangles |
| D4 | Equilateral repeats the a/b comparison and ignores c | Require a == b and b == c | (5, 5, 8) and its permutations |
| D5 | Right-triangle rule doubles values instead of squaring | Use the Pythagorean equality | (3, 4, 5), (5, 12, 13), (120, 160, 200) |
| D6 | Right-triangle check assumes c is the hypotenuse | Check all three possible hypotenuses | All permutations of each right triple |
| D7 | Scalene repeats a != b and omits a != c | Require all three pairs to differ | (5, 8, 5) and other isosceles arrangements |

### Inputs and execution evidence

All 81 inputs, expected results, actual results, and statuses appear below. TestTriangle.py is the single case source for both unittest and make_report.py. Each case becomes an individual unittest method, so the reported execution count matches the report rows. CSV copies are included for convenient inspection. Exceptions in the original program are recorded by type and message.

Run from the repository directory:

```sh
python3 -m unittest TestTriangle
```

The captured runs used `python3 -m unittest -v TestTriangle` to include individual case names. This is the assignment's unittest command with Python 3 selected explicitly and verbose output enabled. `results/initial_unittest.txt` preserves the failing original run; `results/final_unittest.txt` is the requested final output-file deliverable and ends with `Ran 81 tests` and `OK`.

### Test report: original implementation

| Test ID | Input | Expected Results | Actual Result | Pass or Fail |
|---|---|---|---|---|
| T001 | (3, 4, 5) | Right | InvalidInput | Fail |
| T002 | (5, 3, 4) | Right | InvalidInput | Fail |
| T003 | (1, 1, 1) | Equilateral | InvalidInput | Fail |
| T004 | (3, 4, 5) | Right | InvalidInput | Fail |
| T005 | (3, 5, 4) | Right | InvalidInput | Fail |
| T006 | (4, 3, 5) | Right | InvalidInput | Fail |
| T007 | (4, 5, 3) | Right | InvalidInput | Fail |
| T008 | (5, 3, 4) | Right | InvalidInput | Fail |
| T009 | (5, 4, 3) | Right | InvalidInput | Fail |
| T010 | (5, 12, 13) | Right | InvalidInput | Fail |
| T011 | (5, 13, 12) | Right | InvalidInput | Fail |
| T012 | (12, 5, 13) | Right | InvalidInput | Fail |
| T013 | (12, 13, 5) | Right | InvalidInput | Fail |
| T014 | (13, 5, 12) | Right | InvalidInput | Fail |
| T015 | (13, 12, 5) | Right | InvalidInput | Fail |
| T016 | (4, 5, 6) | Scalene | InvalidInput | Fail |
| T017 | (4, 6, 5) | Scalene | InvalidInput | Fail |
| T018 | (5, 4, 6) | Scalene | InvalidInput | Fail |
| T019 | (5, 6, 4) | Scalene | InvalidInput | Fail |
| T020 | (6, 4, 5) | Scalene | InvalidInput | Fail |
| T021 | (6, 5, 4) | Scalene | InvalidInput | Fail |
| T022 | (5, 5, 8) | Isoceles | InvalidInput | Fail |
| T023 | (5, 8, 5) | Isoceles | InvalidInput | Fail |
| T024 | (8, 5, 5) | Isoceles | InvalidInput | Fail |
| T025 | (1, 2, 3) | NotATriangle | InvalidInput | Fail |
| T026 | (1, 3, 2) | NotATriangle | InvalidInput | Fail |
| T027 | (2, 1, 3) | NotATriangle | InvalidInput | Fail |
| T028 | (2, 3, 1) | NotATriangle | InvalidInput | Fail |
| T029 | (3, 1, 2) | NotATriangle | InvalidInput | Fail |
| T030 | (3, 2, 1) | NotATriangle | InvalidInput | Fail |
| T031 | (1, 2, 4) | NotATriangle | InvalidInput | Fail |
| T032 | (1, 4, 2) | NotATriangle | InvalidInput | Fail |
| T033 | (2, 1, 4) | NotATriangle | InvalidInput | Fail |
| T034 | (2, 4, 1) | NotATriangle | InvalidInput | Fail |
| T035 | (4, 1, 2) | NotATriangle | InvalidInput | Fail |
| T036 | (4, 2, 1) | NotATriangle | InvalidInput | Fail |
| T037 | (2, 2, 5) | NotATriangle | InvalidInput | Fail |
| T038 | (2, 5, 2) | NotATriangle | InvalidInput | Fail |
| T039 | (5, 2, 2) | NotATriangle | InvalidInput | Fail |
| T040 | (100, 100, 100) | Equilateral | InvalidInput | Fail |
| T041 | (200, 200, 200) | Equilateral | InvalidInput | Fail |
| T042 | (2, 3, 4) | Scalene | InvalidInput | Fail |
| T043 | (198, 199, 200) | Scalene | InvalidInput | Fail |
| T044 | (199, 200, 200) | Isoceles | InvalidInput | Fail |
| T045 | (120, 160, 200) | Right | InvalidInput | Fail |
| T046 | (120, 200, 160) | Right | InvalidInput | Fail |
| T047 | (160, 120, 200) | Right | InvalidInput | Fail |
| T048 | (160, 200, 120) | Right | InvalidInput | Fail |
| T049 | (200, 120, 160) | Right | InvalidInput | Fail |
| T050 | (200, 160, 120) | Right | InvalidInput | Fail |
| T051 | (0, 3, 3) | InvalidInput | InvalidInput | Pass |
| T052 | (3, 0, 3) | InvalidInput | InvalidInput | Pass |
| T053 | (3, 3, 0) | InvalidInput | InvalidInput | Pass |
| T054 | (-1, 3, 3) | InvalidInput | InvalidInput | Pass |
| T055 | (3, -1, 3) | InvalidInput | InvalidInput | Pass |
| T056 | (3, 3, -1) | InvalidInput | InvalidInput | Pass |
| T057 | (201, 3, 3) | InvalidInput | InvalidInput | Pass |
| T058 | (3, 201, 3) | InvalidInput | InvalidInput | Pass |
| T059 | (3, 3, 201) | InvalidInput | InvalidInput | Pass |
| T060 | (3.0, 3, 3) | InvalidInput | InvalidInput | Pass |
| T061 | (3, 3.0, 3) | InvalidInput | InvalidInput | Pass |
| T062 | (3, 3, 3.0) | InvalidInput | InvalidInput | Pass |
| T063 | (2.5, 3, 3) | InvalidInput | InvalidInput | Pass |
| T064 | (3, 2.5, 3) | InvalidInput | InvalidInput | Pass |
| T065 | (3, 3, 2.5) | InvalidInput | InvalidInput | Pass |
| T066 | ('3', 3, 3) | InvalidInput | TypeError: '>' not supported between instances of 'str' and 'int' | Fail |
| T067 | (3, '3', 3) | InvalidInput | TypeError: '>' not supported between instances of 'str' and 'int' | Fail |
| T068 | (3, 3, '3') | InvalidInput | TypeError: '>' not supported between instances of 'str' and 'int' | Fail |
| T069 | (None, 3, 3) | InvalidInput | TypeError: '>' not supported between instances of 'NoneType' and 'int' | Fail |
| T070 | (3, None, 3) | InvalidInput | TypeError: '>' not supported between instances of 'NoneType' and 'int' | Fail |
| T071 | (3, 3, None) | InvalidInput | TypeError: '>' not supported between instances of 'NoneType' and 'int' | Fail |
| T072 | (True, 3, 3) | InvalidInput | InvalidInput | Pass |
| T073 | (3, True, 3) | InvalidInput | InvalidInput | Pass |
| T074 | (3, 3, True) | InvalidInput | InvalidInput | Pass |
| T075 | ([3], 3, 3) | InvalidInput | TypeError: '>' not supported between instances of 'list' and 'int' | Fail |
| T076 | (3, [3], 3) | InvalidInput | TypeError: '>' not supported between instances of 'list' and 'int' | Fail |
| T077 | (3, 3, [3]) | InvalidInput | TypeError: '>' not supported between instances of 'list' and 'int' | Fail |
| T078 | ((3+0j), 3, 3) | InvalidInput | TypeError: '>' not supported between instances of 'complex' and 'int' | Fail |
| T079 | (3, (3+0j), 3) | InvalidInput | TypeError: '>' not supported between instances of 'complex' and 'int' | Fail |
| T080 | (3, 3, (3+0j)) | InvalidInput | TypeError: '>' not supported between instances of 'complex' and 'int' | Fail |
| T081 | (0, 0, 0) | InvalidInput | InvalidInput | Pass |

### Test report: repaired implementation

| Test ID | Input | Expected Results | Actual Result | Pass or Fail |
|---|---|---|---|---|
| T001 | (3, 4, 5) | Right | Right | Pass |
| T002 | (5, 3, 4) | Right | Right | Pass |
| T003 | (1, 1, 1) | Equilateral | Equilateral | Pass |
| T004 | (3, 4, 5) | Right | Right | Pass |
| T005 | (3, 5, 4) | Right | Right | Pass |
| T006 | (4, 3, 5) | Right | Right | Pass |
| T007 | (4, 5, 3) | Right | Right | Pass |
| T008 | (5, 3, 4) | Right | Right | Pass |
| T009 | (5, 4, 3) | Right | Right | Pass |
| T010 | (5, 12, 13) | Right | Right | Pass |
| T011 | (5, 13, 12) | Right | Right | Pass |
| T012 | (12, 5, 13) | Right | Right | Pass |
| T013 | (12, 13, 5) | Right | Right | Pass |
| T014 | (13, 5, 12) | Right | Right | Pass |
| T015 | (13, 12, 5) | Right | Right | Pass |
| T016 | (4, 5, 6) | Scalene | Scalene | Pass |
| T017 | (4, 6, 5) | Scalene | Scalene | Pass |
| T018 | (5, 4, 6) | Scalene | Scalene | Pass |
| T019 | (5, 6, 4) | Scalene | Scalene | Pass |
| T020 | (6, 4, 5) | Scalene | Scalene | Pass |
| T021 | (6, 5, 4) | Scalene | Scalene | Pass |
| T022 | (5, 5, 8) | Isoceles | Isoceles | Pass |
| T023 | (5, 8, 5) | Isoceles | Isoceles | Pass |
| T024 | (8, 5, 5) | Isoceles | Isoceles | Pass |
| T025 | (1, 2, 3) | NotATriangle | NotATriangle | Pass |
| T026 | (1, 3, 2) | NotATriangle | NotATriangle | Pass |
| T027 | (2, 1, 3) | NotATriangle | NotATriangle | Pass |
| T028 | (2, 3, 1) | NotATriangle | NotATriangle | Pass |
| T029 | (3, 1, 2) | NotATriangle | NotATriangle | Pass |
| T030 | (3, 2, 1) | NotATriangle | NotATriangle | Pass |
| T031 | (1, 2, 4) | NotATriangle | NotATriangle | Pass |
| T032 | (1, 4, 2) | NotATriangle | NotATriangle | Pass |
| T033 | (2, 1, 4) | NotATriangle | NotATriangle | Pass |
| T034 | (2, 4, 1) | NotATriangle | NotATriangle | Pass |
| T035 | (4, 1, 2) | NotATriangle | NotATriangle | Pass |
| T036 | (4, 2, 1) | NotATriangle | NotATriangle | Pass |
| T037 | (2, 2, 5) | NotATriangle | NotATriangle | Pass |
| T038 | (2, 5, 2) | NotATriangle | NotATriangle | Pass |
| T039 | (5, 2, 2) | NotATriangle | NotATriangle | Pass |
| T040 | (100, 100, 100) | Equilateral | Equilateral | Pass |
| T041 | (200, 200, 200) | Equilateral | Equilateral | Pass |
| T042 | (2, 3, 4) | Scalene | Scalene | Pass |
| T043 | (198, 199, 200) | Scalene | Scalene | Pass |
| T044 | (199, 200, 200) | Isoceles | Isoceles | Pass |
| T045 | (120, 160, 200) | Right | Right | Pass |
| T046 | (120, 200, 160) | Right | Right | Pass |
| T047 | (160, 120, 200) | Right | Right | Pass |
| T048 | (160, 200, 120) | Right | Right | Pass |
| T049 | (200, 120, 160) | Right | Right | Pass |
| T050 | (200, 160, 120) | Right | Right | Pass |
| T051 | (0, 3, 3) | InvalidInput | InvalidInput | Pass |
| T052 | (3, 0, 3) | InvalidInput | InvalidInput | Pass |
| T053 | (3, 3, 0) | InvalidInput | InvalidInput | Pass |
| T054 | (-1, 3, 3) | InvalidInput | InvalidInput | Pass |
| T055 | (3, -1, 3) | InvalidInput | InvalidInput | Pass |
| T056 | (3, 3, -1) | InvalidInput | InvalidInput | Pass |
| T057 | (201, 3, 3) | InvalidInput | InvalidInput | Pass |
| T058 | (3, 201, 3) | InvalidInput | InvalidInput | Pass |
| T059 | (3, 3, 201) | InvalidInput | InvalidInput | Pass |
| T060 | (3.0, 3, 3) | InvalidInput | InvalidInput | Pass |
| T061 | (3, 3.0, 3) | InvalidInput | InvalidInput | Pass |
| T062 | (3, 3, 3.0) | InvalidInput | InvalidInput | Pass |
| T063 | (2.5, 3, 3) | InvalidInput | InvalidInput | Pass |
| T064 | (3, 2.5, 3) | InvalidInput | InvalidInput | Pass |
| T065 | (3, 3, 2.5) | InvalidInput | InvalidInput | Pass |
| T066 | ('3', 3, 3) | InvalidInput | InvalidInput | Pass |
| T067 | (3, '3', 3) | InvalidInput | InvalidInput | Pass |
| T068 | (3, 3, '3') | InvalidInput | InvalidInput | Pass |
| T069 | (None, 3, 3) | InvalidInput | InvalidInput | Pass |
| T070 | (3, None, 3) | InvalidInput | InvalidInput | Pass |
| T071 | (3, 3, None) | InvalidInput | InvalidInput | Pass |
| T072 | (True, 3, 3) | InvalidInput | InvalidInput | Pass |
| T073 | (3, True, 3) | InvalidInput | InvalidInput | Pass |
| T074 | (3, 3, True) | InvalidInput | InvalidInput | Pass |
| T075 | ([3], 3, 3) | InvalidInput | InvalidInput | Pass |
| T076 | (3, [3], 3) | InvalidInput | InvalidInput | Pass |
| T077 | (3, 3, [3]) | InvalidInput | InvalidInput | Pass |
| T078 | ((3+0j), 3, 3) | InvalidInput | InvalidInput | Pass |
| T079 | (3, (3+0j), 3) | InvalidInput | InvalidInput | Pass |
| T080 | (3, 3, (3+0j)) | InvalidInput | InvalidInput | Pass |
| T081 | (0, 0, 0) | InvalidInput | InvalidInput | Pass |

### Repository and submission checklist

Repository name: **hw-06b**. Intended GitHub location: https://github.com/DillonDeGuzman/hw-06b.

- Triangle.py: repaired classification source.
- TestTriangle.py: expanded suite used unchanged for both runs.
- results/final_unittest.txt: final execution output; accepted by the instructions as an alternative to a screenshot.
- ASSIGNMENT_SUMMARY.md: this report, including both complete results tables and the summary matrix.
- originals/: untouched downloaded source and starter tests.
- Git history: original code commit, expanded-tests/initial-results commit, then repair/final-results commit.

Before submission, complete the reflection and honor pledge, confirm the author name, and ensure the instructor can access the repository. Upload the required files to the course submission system and provide the repository name/link. Course-site submission is not performed by this repository.
