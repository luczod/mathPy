# 1: Verify the Continuity of a Function at a Point
from sympy import Limit, Symbol, sympify
from typing import Any

def check_continuity(func: Any, var: Symbol, point: float):
  l1 = Limit(func, var, point, dir='+').doit()
  l2 = Limit(func, var, point, dir='-').doit()
  f_val = func.subs({var:point})

  if l1 == l2 and f_val == l1:
    print("The function {0} is continuous at {1}".format(func, point))
    return

  return print("The function {0} is NOT continuous at {1}".format(func, point))


if __name__ == '__main__':
  func = input('Enter a function in one variable: ')
  var = input('Enter the variable: ')
  point = float(input('Enter the point to check the continuity at: '))

  func = sympify(func)
  var = Symbol(var)

  check_continuity(func,var, point)
