import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # Addition tests
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -7), -12)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(2.5, 3.1), 5.6)
        self.assertEqual(self.calc.add(1e10, 1e10), 2e10)

    # Subtraction tests
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(-5, -7), 2)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(2.5, 1.2), 1.3)
        self.assertEqual(self.calc.subtract(1e10, 1e9), 9e9)

    # Multiplication tests
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)
        self.assertEqual(self.calc.multiply(1e5, 1e5), 1e10)

    # Division tests
    def test_division(self):
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertEqual(self.calc.divide(-6, -3), 2)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(0, 5), 0)
        self.assertEqual(self.calc.divide(1e10, 1e5), 1e5)

    def test_division_by_zero(self):
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(0, 0))
        self.assertIsNone(self.calc.divide(-10, 0))

    def test_division_float_zero(self):
        # Test with float zero as denominator
        self.assertIsNone(self.calc.divide(5, 0.0))
        self.assertIsNone(self.calc.divide(0, 0.0))
        self.assertIsNone(self.calc.divide(-10, 0.0))

    # Optional: Test with very large and very small numbers
    def test_large_and_small_numbers(self):
        self.assertAlmostEqual(self.calc.add(1e-10, 1e-10), 2e-10)
        self.assertAlmostEqual(self.calc.multiply(1e-10, 1e10), 1.0)
        self.assertAlmostEqual(self.calc.divide(1e-10, 1e10), 1e-20)

if __name__ == '__main__':
    unittest.main()