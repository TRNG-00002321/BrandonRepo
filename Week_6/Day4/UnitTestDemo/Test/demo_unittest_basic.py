import sys
import unittest
from src.Calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator

    def test_add(self):
        n1=1
        n2=2
        expectedResult=3

        result = self.calculator.add(self, 1,2)
        self.assertEqual(3, 3)


    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(self,1,0)


    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError) as context:
            self.calculator.divide(self,1,0)
        self.assertEqual(str(context.exception), "division by zero")


    @unittest.skip("Demonstrating unconditional skipping")
    def test_unconditional_skip(self):
        self.fail("This test should not run")


    @unittest.skipIf(sys.platform == 'win32', "Skipping on Windows")
    def test_linux_only_feature(self):
        self.assertTrue(True)  # This test runs only on non-Windows platforms

    @unittest.expectedFailure
    def test_known_bug(self):
        self.assertEqual(1, 2, "This test is expected to fail due to a known bug")


    def tearDown(self):
        self.calculator = None