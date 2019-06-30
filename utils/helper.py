import math


def sales_round(value, base=.05):
    return base * round(float(value)/base)
