# Module 2: AI-Assisted Programming & GitHub
Harshvardhan Singh | Roll no. 25BCON0472

## Overview
Assignments 4-8: C-to-Python conversion, AI-assisted documentation,
Cursor rules, two Easy LeetCode solutions, debugging and unit testing.
C examples were prepared because no original C files were supplied.
Student marks (85.5) are demonstration data, not an academic result.

## Requirements
Python 3.10+; standard library only. Optional GCC for the C examples.

## Run
```sh
python factorial.py
python fibonacci.py
python student.py
python average.py
python -m unittest discover -s tests -v
```

## Files
- factorial.py, fibonacci.py, student.py: converted Python examples.
- c_sources/: corresponding compilable C examples.
- two_sum.py, valid_parentheses.py: LeetCode-compatible Solution classes.
- buggy_average.py: deliberately incorrect example.
- average.py: corrected arithmetic mean.
- tests/test_programs.py: 21 test methods, including edge cases.
- .cursorrules: legacy rules file requested by the assignment.
- .cursor/rules/python.mdc: equivalent current project rule.
- evidence/: actual local runs and a reproducible bug demonstration.

## Behaviour
Factorial accepts non-negative integers; Python integers grow as needed.
Fibonacci returns the first n terms starting at 0, including [] for n=0.
The average function accepts numeric sequences and rejects empty input.
Two Sum assumes exactly one solution as in the LeetCode task; outside
that contract it raises ValueError when no pair exists.

## Verification and remaining work
All 21 local test methods passed. C examples compiled with warnings enabled.
No GitHub push, Cursor UI session, or LeetCode submission was performed.
See COMPLETION_STEPS.md for the remaining account-based steps.
