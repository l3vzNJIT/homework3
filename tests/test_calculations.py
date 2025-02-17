''' tests for the calculations class '''

import pytest
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, subtract

@pytest.fixture
def setup_calculations():
  Calculations.clear_history()
  Calculations.add_calculation(Calculation(10, 5, add))
  Calculations.add_calculation(Calculation(20, 3, subtract))

def test_add_calculation(setup_calculations):
  calc = Calculation(1, 1, add)
  Calculations.add_calculation(calc)
  assert Calculations.get_latest() == calc, "history failed to get added to"

def test_get_history(setup_calculations):
  history = Calculations.get_history()
  assert len(history) == 2, "history has wrong length"

def test_clear_history(setup_calculations):
  Calculations.clear_history()
  assert len(Calculations.get_history()) == 0, "history was not cleared"

def test_get_latest(setup_calculations):
  latest = Calculations.get_latest()
  assert latest.a == 20 and latest.b == 3, "wrong latest calculation"

def test_find_by_operation(setup_calculations):
  add_operations = Calculations.find_by_operation("add")
  assert len(add_operations) == 1, "find op add failed"

  subtract_operations = Calculations.find_by_operation("subtract")
  assert len(subtract_operations) == 1, "find op subtract failed"

def test_get_latest_with_empty_history():
  Calculations.clear_history()
  assert Calculations.get_latest() is None, "expected None for empty history"
