import unittest
from factorial import factorial
from fibonacci import fibonacci
from student import Student
from two_sum import Solution as TwoSum
from valid_parentheses import Solution as Brackets
from average import average


class ProgramTests(unittest.TestCase):
    def test_factorial_base(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
    def test_factorial_normal(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(13), 6227020800)
    def test_factorial_negative(self):
        with self.assertRaises(ValueError): factorial(-1)
    def test_factorial_type(self):
        for value in (2.5, "3", True):
            with self.assertRaises(TypeError): factorial(value)
    def test_fibonacci_base(self):
        self.assertEqual(fibonacci(0), [])
        self.assertEqual(fibonacci(1), [0])
    def test_fibonacci_normal(self):
        self.assertEqual(fibonacci(7), [0, 1, 1, 2, 3, 5, 8])
    def test_fibonacci_invalid(self):
        with self.assertRaises(ValueError): fibonacci(-1)
        with self.assertRaises(TypeError): fibonacci(2.5)
    def test_student(self):
        s = Student("472", "Harshvardhan Singh", 85.5)
        self.assertEqual((s.roll, s.name, s.marks),
                         ("472", "Harshvardhan Singh", 85.5))
    def test_two_sum_examples(self):
        solver = TwoSum()
        self.assertEqual(solver.twoSum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(solver.twoSum([3, 2, 4], 6), [1, 2])
    def test_two_sum_duplicates(self):
        self.assertEqual(TwoSum().twoSum([3, 3], 6), [0, 1])
    def test_two_sum_negative(self):
        self.assertEqual(TwoSum().twoSum([-3, 4, 3], 0), [0, 2])
    def test_two_sum_no_pair(self):
        with self.assertRaises(ValueError): TwoSum().twoSum([1], 2)
    def test_brackets_valid(self):
        for s in ("()", "()[]{}", "([])"):
            self.assertTrue(Brackets().isValid(s))
    def test_brackets_invalid(self):
        for s in ("(]", "([)]", ")", "("):
            self.assertFalse(Brackets().isValid(s))
    def test_brackets_extension(self):
        self.assertTrue(Brackets().isValid(""))
        self.assertFalse(Brackets().isValid("a"))
    def test_average_fraction(self):
        self.assertEqual(average([1, 2]), 1.5)
    def test_average_normal(self):
        self.assertEqual(average([10, 20, 30]), 20.0)
    def test_average_negative(self):
        self.assertEqual(average([-2, -4]), -3.0)
    def test_average_single(self):
        self.assertEqual(average([5]), 5.0)
    def test_average_zeros(self):
        self.assertEqual(average([0, 0]), 0.0)
    def test_average_empty(self):
        with self.assertRaises(ValueError): average([])


if __name__ == "__main__":
    unittest.main()
