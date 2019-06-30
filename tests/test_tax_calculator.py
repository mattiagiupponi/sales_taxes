from utils.calculator import Calculator
from utils.settings import STANDARD_TAX_IN_PERCENTAGE, IMPORTED_PRODUCT_TAX_IN_PERCENTAGE
import unittest


class TestTaxCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
        self.single_normal_product = {
            "quantity": 1,
            "category": ['food'],
            "product_name": "chocolate bar",
            "price": 0.85
        }
        self.single_normal_product_multiple_quantity = {
            "quantity": 2,
            "category": ['food'],
            "product_name": "chocolate bar",
            "price": 0.85
        }
        self.single_normal_product_with_all_taxes = {
            "quantity": 1,
            "category": ["retail"],
            "product_name": "music CD",
            "price": 14.99
        }
        self.single_exempt_product = {
            "quantity": 1,
            "category": ["book"],
            "product_name": "book",
            "price": 12.49
        }
        self.single_imported_product = {
            "quantity": 1,
            "category": ["imported", "food"],
            "product_name": "imported box of chocolates",
            "price": 10.00
        }
        self.single_perfume = {
            "product_name": "imported bottle of perfume",
            "quantity": 1,
            "price": 47.50,
            "category": ["imported"]
        }
        self.multiple_product_input_1 = [{
                "quantity": 1,
                "category": ["book"],
                "product_name": "book",
                "price": 12.49
            }, {
                "quantity": 1,
                "category": ["music"],
                "product_name": "music CD",
                "price": 14.99
            }, {
                "quantity": 1,
                "category": ["food"],
                "product_name": "chocolate bar",
                "price": 0.85
            }]

        self.multiple_product_input_2 = [{
                "quantity": 1,
                "category": ["imported", "food"],
                "price": 10.00,
                "product_name": "imported box of chocolates"
            }, {
                "quantity": 1,
                "category": ["imported"],
                "price": 47.50,
                "product_name": "imported bottle of perfume"
            }]
        self.multiple_product_input_3 = [{
                "quantity": 1,
                "category": ["imported", "perfume"],
                "price": 27.99,
                "product_name": "imported bottle of perfume"
            }, {
                "quantity": 1,
                "category": ["perfume"],
                "price": 18.99,
                "product_name": "bottle of perfume"
            }, {
                "quantity": 1,
                "category": ["medical"],
                "price": 9.75,
                "product_name": "packet of headache pills"
            }, {
                "quantity": 1,
                "category": ["food", "imported"],
                "price": 11.25,
                "product_name": "imported box of chocolates"
            }]

    def tearDown(self):
        self.calculator = Calculator()

    def test_tax_calculator_for_normal_product(self):
        expected_price = 0.85
        expected_tax = 0
        actual_price = self.calculator.single_product(self.single_normal_product)
        self.assertEqual(expected_price, actual_price.total)
        self.assertEqual(expected_tax, actual_price.tax)

    def test_tax_calculator_for_normal_product_multiple_quantity(self):
        expected_price = 1.70
        expected_tax = 0
        actual_price = self.calculator.single_product(self.single_normal_product_multiple_quantity)
        self.assertEqual(expected_price, actual_price.total)
        self.assertEqual(expected_tax, actual_price.tax)

    def test_tax_calculator_for_normal_product_with_taxes(self):
        expected_price = 16.49
        expected_tax = 1.50
        actual_price = self.calculator.single_product(self.single_normal_product_with_all_taxes)
        print(actual_price)
        self.assertEqual(expected_tax, actual_price.tax)
        self.assertEqual(expected_price, actual_price.total)

    def test_tax_calculator_for_exempt_product(self):
        expected_price = 12.49
        expected_tax = 0
        actual_price = self.calculator.single_product(self.single_exempt_product)
        self.assertEqual(expected_price, actual_price.total)
        self.assertEqual(expected_tax, actual_price.tax)

    def test_tax_calculator_for_single_perfume(self):
        expected_price = 54.65
        expected_tax = 7.15
        actual_price = self.calculator.single_product(self.single_perfume)
        self.assertEqual(expected_price, actual_price.total)
        self.assertEqual(expected_tax, actual_price.tax)

    def test_tax_calculator_for_imported_product(self):
        expected_price = 10.50
        expected_tax = 0.50
        actual_price = self.calculator.single_product(self.single_imported_product)
        self.assertEqual(expected_price, actual_price.total)
        self.assertEqual(expected_tax, actual_price.tax)

    def test_calculate_total_for_multiple_product_input_1(self):
        expected_price_list = [
            '1 book: 12.49', '1 music CD: 16.49', '1 chocolate bar: 0.85', 'Sales Taxes: 1.5', 'Total: 29.83'
        ]
        actual_list = self.calculator.multiple_product(self.multiple_product_input_1)
        self.assertEqual(expected_price_list, actual_list)

    def test_calculate_total_for_multiple_product_input_2(self):
        expected_price_list = [
            "1 imported box of chocolates: 10.5", "1 imported bottle of perfume: 54.65", "Sales Taxes: 7.65",
            "Total: 65.15"
        ]

        actual_list = self.calculator.multiple_product(self.multiple_product_input_2)
        self.assertEqual(expected_price_list, actual_list)

    def test_calculate_total_for_multiple_product_input_3(self):
        expected_price_list = [
            "1 imported bottle of perfume: 32.19", "1 bottle of perfume: 20.89",
            "1 packet of headache pills: 9.75", "1 imported box of chocolates: 11.8",
            "Sales Taxes: 6.65", "Total: 74.63"
        ]

        actual_list = self.calculator.multiple_product(self.multiple_product_input_3)
        self.assertEqual(expected_price_list, actual_list)

    def test_calculate_total(self):
        expected = 0.85
        actual = self.calculator._calculate_total(self.single_normal_product)
        self.assertEqual(expected, actual)

    def test_calculate_total_multiple_product(self):
        expected = 1.70
        actual = self.calculator._calculate_total(self.single_normal_product_multiple_quantity)
        self.assertEqual(expected, actual)

    def test_calculate_total_imported_product(self):
        expected = 10.00
        actual = self.calculator._calculate_total(self.single_imported_product)
        self.assertEqual(expected, actual)

    def test_calculate_tax(self):
        expected = 1.00
        actual = self.calculator._calculate_tax(self.single_imported_product, STANDARD_TAX_IN_PERCENTAGE)
        self.assertEqual(expected, actual)

    def test_calculate_import_tax(self):
        expected = 0.5
        actual = self.calculator.add_import_tax(self.single_imported_product)
        self.assertEqual(expected, actual)

    def test_calculate_import_tax_with_normal_product(self):
        expected = 0
        actual = self.calculator.add_import_tax(self.single_normal_product)
        self.assertEqual(expected, actual)

    def test_calculate_standard_tax(self):
        expected = 0
        actual = self.calculator.add_standard_tax(self.single_imported_product)
        self.assertEqual(expected, actual)

    def test_calculate_standard_tax_with_normal_product(self):
        expected = 4.75
        actual = self.calculator.add_standard_tax(self.single_perfume)
        self.assertEqual(expected, actual)

    def test_exception_raise(self):

        with self.assertRaises(Exception) as context:
            self.calculator.single_product({"key": "value"})

        self.assertEqual('Mandatory param/s is/are missing', context.exception.args[0])
