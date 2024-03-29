from utils.settings import STANDARD_TAX_IN_PERCENTAGE, NO_TAX_PRODUCT_CATEGORY,\
    IMPORTED_PRODUCT_TAX_IN_PERCENTAGE
from collections import namedtuple
from utils.helper import sales_round
from decimal import Decimal, ROUND_HALF_UP


class Calculator:
    """
    Calculator (no init required)

    # Functions available:
    Given a list of dictionary, will return a string of detail information about the products
     - multiple_product(list_of_product):
      - Input -> List of dictionary
       - mandatory keys price, quantity, category, product_name
      - Output -> List of string with quantity, price and total price + all summary information

    Given a single product, will return a named_tuple with total price + tax fee
     - single_product(product):
      - Input -> Dict: Dictionary
      - Output -> Named tuple: total product price + tax_fee
      - Raise an Exception if some of mandatory params are missing

    Calculate the standard tax value if the product is not one of the excluded category
     - add_standard_tax(product)
      - Input -> Dict: product
      - Output -> Float: The value of the tax calculated

    Calculate the import tax value if the product is not one of the excluded category
     - add_import_tax(product)
      - Input -> Dict: product
      - Output -> Float: The value of the tax calculated
    """

    def __init__(self):
        self.product_info = namedtuple("Product", ["tax", "total"])
        self.normal_tax = 0.0
        self.imported_tax = 0.0
        self.product_price = 0.0
        self.total_price = 0.0
        self.total_tax = 0.0

    def multiple_product(self, list_of_product):
        output = []
        for product in list_of_product:
            receipt = product
            values = self.single_product(product)
            output.append("{} {}: {}".format(receipt["quantity"], receipt["product_name"], values.total))
            self.total_price += values.total
            self.total_tax += values.tax
        output.append("Sales Taxes: {}".format(self.total_tax))
        output.append("Total: {}".format(self.total_price))
        return output

    def single_product(self, product):
        if not self._missing_key(product):
            self.normal_tax = self.add_standard_tax(product)
            self.imported_tax = self.add_import_tax(product)
            total_tax = self.normal_tax + self.imported_tax
            rounded_tax = sales_round(Decimal(total_tax).quantize(Decimal('0.05'), rounding=ROUND_HALF_UP))

            self.product_price = self._calculate_total(product)

            return self.product_info(
                tax=rounded_tax,
                total=round(self.product_price + rounded_tax, 2)
            )
        raise Exception("Mandatory param/s is/are missing")

    def add_standard_tax(self, product):
        for category in product['category']:
            if category in NO_TAX_PRODUCT_CATEGORY:
                return 0
        return self._calculate_tax(product, STANDARD_TAX_IN_PERCENTAGE)

    def add_import_tax(self, product):
        if "imported" in product['category']:
            # imported as value should be used as a environment variable or substituted
            # when deployed with an orchestrator such as Marathon or Kubernetes, for this exercise
            # is hard coded in the application
            return self._calculate_tax(product, IMPORTED_PRODUCT_TAX_IN_PERCENTAGE)
        return 0

    def _calculate_tax(self, product, tax_value):
        return (self._calculate_total(product) * tax_value) / 100

    def _missing_key(self, input_product):
        mandatory_params = ["price", "quantity", "category", "product_name"]
        return any([True for param in mandatory_params if param not in input_product.keys()])
    
    def _calculate_total(self, product):
        return product["price"] * product["quantity"]
