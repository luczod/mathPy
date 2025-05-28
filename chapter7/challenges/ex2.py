# 2: Implement the Gradient Descent

from sympy import Derivative, Symbol, sympify, SympifyError, solve
from matplotlib import pyplot as plt
from typing import Any
from numpy.typing import ArrayLike

def frange(start: float, final: float, interval: float) -> list[float]:
  numbers = []

  while start < final:
    numbers.append(start)
    start = start + interval

  return numbers

def draw_graph(X_traversed: list[float], f: Any, var:Symbol):
  # First create the graph of the function itself
  x_val = frange(-1, 1, 0.01)
  f_val = [f.subs({var:x}) for x in x_val]
  plt.plot(x_val, f_val, 'bo')
  # calculate the function value at each of the intermediate
  # points traversed
  f_traversed = [f.subs({var:x}) for x in X_traversed]
  plt.plot(X_traversed, f_traversed, 'r.')
  plt.legend(['Function', 'Intermediate points'], loc='best')
  plt.show()

def grad_descent(x0: float, f1x: Derivative, x: Symbol) -> tuple[float, list[float]]:
  # Check if f1x=0 has a solution
  if not solve(f1x):
    raise Exception('Cannot continue, solution for {0}= 0 does not exist'.format(f1x))

  epsilon = 1e-6
  step_size = 1e-4
  x_old = x0
  num_f1x = f1x.subs({x:x_old}).evalf() # type: ignore x**2*cos(x) - x / 10
  x_new = x_old - step_size*num_f1x # type: ignore

  x_axis = []
  while abs(x_old - x_new) > epsilon:
    x_axis.append(x_old)
    x_old = x_new
    num_f1x = f1x.subs({x:x_old}).evalf() # type: ignore
    x_new = x_old - step_size*num_f1x # type: ignore

  return x_new, x_axis


if __name__ == '__main__':
  f = input('Enter a function in one variable: ')
  var = input('Enter the variable to differentiate with respect to: ')
  var0 = float(input('Enter the initial value of the variable: '))

  try:
    f = sympify(f)
  except SympifyError:
    print('Invalid function entered')
  else:
    var = Symbol(var)
    d = Derivative(f, var).doit()
    value_max,x_axis = grad_descent(var0, d, var)

    print('{0}: {1}'.format(var.name, value_max))
    print('Minimum value: {0}'.format(f.subs({var:value_max})))
    draw_graph(x_axis, f, var)