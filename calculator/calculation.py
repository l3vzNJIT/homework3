'''
Define an abstract calculation class
'''


class Calculation:
  '''
  A calculation contains operands, result, and a method for computing the result
  '''

  def __init__(self, a, b, operation):
    # initialize an object of type Calculation
    self.a = a
    self.b = b
    self.operation = operation

  @staticmethod
  def create(a, b, operation):
    # create a Calculation object
    return Calculation(a, b, operation)

  def perform(self):
    # call the Calculation's operation function
    return self.operation(self.a, self.b)

  def __repr__(self):
    # pretty print the Calculation
    return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"
