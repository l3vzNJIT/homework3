'''
A simple arithmetic calculator main class
'''

from calculator.operations import add, subtract, multiply, divide
from calculator.calculation import Calculation
from calculator.calculations import Calculations

class Calculator:
  ''' class to tie together everything and be an interface for user '''
  @staticmethod
  def _perform_operation(a, b, operation):
    calculation = Calculation.create(a, b, operation)
    Calculations.add_calculation(calculation)
    return calculation.perform()

  @staticmethod
  def add(a, b):
    return Calculator._perform_operation(a, b, add)

  @staticmethod
  def subtract(a, b):
    return Calculator._perform_operation(a, b, subtract)

  @staticmethod
  def multiply(a, b):
    return Calculator._perform_operation(a, b, multiply)

  @staticmethod
  def divide(a, b):
    return Calculator._perform_operation(a, b, divide)
