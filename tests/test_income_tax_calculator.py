import unittest
import sys
sys.path.append(".\sut")
from income_tax_calculator import IncomeTaxCalculator

class TestIncomeTaxCalculator(unittest.TestCase):
    def test_calculate_tax_for_age_less_than_65_and_income_less_than_or_equal_to_50000(self):
        calculator = IncomeTaxCalculator(40000, 59)
        self.assertEqual(calculator.calculate_tax(), 0.0)

    def test_calculate_tax_for_age_less_than_65_and_income_greater_than_50000(self):
        calculator = IncomeTaxCalculator(60000, 59)
        self.assertEqual(calculator.calculate_tax(), 1000.0)

    def test_calculate_tax_for_age_65_or_over_and_income_less_than_or_equal_to_60000(self):
        calculator = IncomeTaxCalculator(50000, 65)
        self.assertEqual(calculator.calculate_tax(), 0.0)

    def test_calculate_tax_for_age_65_or_over_and_income_greater_than_60000(self):
        calculator = IncomeTaxCalculator(70000, 65)
        self.assertEqual(calculator.calculate_tax(), 1000.0)

if __name__ == '__main__':
    unittest.main()