''' tests for calculator class '''

from calculator import Calculator


def test_addition():
  assert Calculator.add(10, 20) == 30

def test_subtraction():
  assert Calculator.subtract(10, 20) == -10

def test_multiplication():
  assert Calculator.multiply(10, 20) == 200

def test_division():
  assert Calculator.divide(10, 20) == 0.5
