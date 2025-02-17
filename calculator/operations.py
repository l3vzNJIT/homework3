''' define arithmetic operations '''


def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  if b == 0:
    raise ValueError("Dividing by zero is undefined")
  else:
    return a / b
