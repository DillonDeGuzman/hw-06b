"""One unittest per documented case; the same suite runs before and after repair."""
import unittest
from itertools import permutations
from Triangle import classifyTriangle

# Keep the starter program's public spelling: Isoceles.
CASES = []

def add(label, sides, expected):
    CASES.append((f"T{len(CASES) + 1:03d}", label, sides, expected))

def arrangements(label, sides, expected):
    for index, values in enumerate(sorted(set(permutations(sides))), 1):
        add(f"{label}_{index}", values, expected)

# The three original examples are retained explicitly.
add("starter_right_a", (3, 4, 5), "Right")
add("starter_right_b", (5, 3, 4), "Right")
add("starter_equilateral", (1, 1, 1), "Equilateral")
arrangements("right_order", (3, 4, 5), "Right")
arrangements("right_larger", (5, 12, 13), "Right")
arrangements("scalene_order", (4, 5, 6), "Scalene")
arrangements("isosceles_order", (5, 5, 8), "Isoceles")
arrangements("degenerate", (1, 2, 3), "NotATriangle")
arrangements("too_long", (1, 2, 4), "NotATriangle")
arrangements("equal_pair_invalid", (2, 2, 5), "NotATriangle")
add("equilateral_middle", (100, 100, 100), "Equilateral")
add("equilateral_max", (200, 200, 200), "Equilateral")
add("just_valid", (2, 3, 4), "Scalene")
add("max_scalene", (198, 199, 200), "Scalene")
add("max_isosceles", (199, 200, 200), "Isoceles")
arrangements("right_max", (120, 160, 200), "Right")
# Repeat invalid values in each parameter position to test each guard.
for label, value in [("zero", 0), ("negative", -1), ("above_max", 201),
                     ("float", 3.0), ("fraction", 2.5), ("string", "3"),
                     ("none", None), ("boolean", True), ("list", [3]),
                     ("complex", 3+0j)]:
    for position in range(3):
        sides = [3, 3, 3]
        sides[position] = value
        add(f"{label}_position_{position + 1}", tuple(sides), "InvalidInput")
add("all_zero", (0, 0, 0), "InvalidInput")

class TestTriangles(unittest.TestCase):
    """Generated methods make the unittest count match the report row count."""

def make_test(sides, expected):
    def test(self):
        self.assertEqual(classifyTriangle(*sides), expected, repr(sides))
    return test

for test_id, label, sides, expected in CASES:
    setattr(TestTriangles, f"test_{test_id}_{label}", make_test(sides, expected))

if __name__ == "__main__":
    unittest.main(verbosity=2)
