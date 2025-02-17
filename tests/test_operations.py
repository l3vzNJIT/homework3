''' tests for the operations module '''

import pytest
from calculator.operations import add, subtract, multiply, divide
from calculator.calculation import Calculation

def test_operation_add():
  calculation = Calculation(10, 5, add)
  assert calculation.perform() == 15

def test_operation_subtract():
  calculation = Calculation(10, 5, subtract)
  assert calculation.perform() == 5

def test_operation_multiply():
  calculation = Calculation(10, 5, multiply)
  assert calculation.perform() == 50

def test_operation_divide():
  calculation = Calculation(10, 5, divide)
  assert calculation.perform() == 2

def test_divide_by_zero():
  with pytest.raises(ValueError, match="Dividing by zero is undefined"):
    calculation = Calculation(10, 0, divide)
    calculation.perform()
