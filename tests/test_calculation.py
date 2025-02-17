"""
tests for the central calculation class
"""

import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide


@pytest.mark.parametrize("a, b, operation, expected", [
  (10, 5, add, 15),
  (10, 5, subtract, 5),
  (10, 5, multiply, 50),
  (10, 2, divide, 5),
  (10.5, 0.5, add, 11.0),
  (10.5, 0.5, subtract, 10.0),
  (10.5, 2, multiply, 21.0),
  (10, 0.5, divide, 20),
])

def test_calculation_operations(a, b, operation, expected):
  calc = Calculation(a, b, operation)
  assert calc.perform() == expected, f"Failed {operation.__name__} operation with {a} and {b}"

def test_calculation_repr():
  calc = Calculation(10, 5, add)
  expected_repr = "Calculation(10, 5, add)"
  assert repr(calc) == expected_repr, "The __repr__ method output does not match the expected string."

def test_divide_by_zero():
  calc = Calculation(10, 0, divide)
  with pytest.raises(ValueError, match="Dividing by zero is undefined"):
    calc.perform()
