'''
2: Implement the Gradient Descent
x**2 + 3*x + 2 | x | -4

Use gradient descent to find the minimum value of a
single variable function. This also checks for the existence
of a solution for the equation, f'(x)=0 and plots the intermediate
points traversed.

In math, domain and range are related to functions. The domain refers to all the possible input values (x-values) a function can accept,
while the range is the set of all possible output values (y-values) the function can produce
'''

from sympy import Derivative, Symbol, sympify, SympifyError, solve
from matplotlib import pyplot as plt
from typing import Any

def function_domain(start: float, final: float, interval: float) -> list[float]:
  numbers = []

  while start < final:
    numbers.append(start)
    start = start + interval

  return numbers

def draw_graph(X_traversed: list[float], func: Any, var: Symbol):
  # First create the graph of the function itself
  x_val = function_domain(-5, 1, 0.01)
  # x_val = function_domain(-1, 1, 0.01)
  f_val = [func.subs({ var: x }) for x in x_val]
  plt.plot(x_val, f_val, 'bo')

  # calculate the function value at each of the intermediate
  # points traversed
  f_traversed = [func.subs({ var: x }) for x in X_traversed]
  plt.plot(X_traversed, f_traversed, 'r.')
  plt.legend(['Function', 'Intermediate points'], loc='best')
  plt.show()

def grad_descent(x0: float, dx: Derivative, x: Symbol) -> tuple[float, list[float]]:
  # Check if f(x) = 0 has a solution
  if not solve(dx):
    raise Exception('Cannot continue, solution for {0}= 0 does not exist'.format(dx))

  epsilon = 1e-6
  step_size = 1e-4
  x_old = x0
  num_dx = dx.subs({ x: x_old }).evalf() # type: ignore
  x_new = x_old - step_size*num_dx # type: ignore

  x_axis = []
  while abs(x_old - x_new) > epsilon:
    x_axis.append(x_old)
    x_old = x_new
    num_dx = dx.subs({ x: x_old }).evalf() # type: ignore
    x_new = x_old - step_size*num_dx # type: ignore

  return x_new, x_axis


if __name__ == '__main__':
  func = input('Enter a function in one variable: ')
  var = input('Enter the variable to differentiate with respect to: ')
  var0 = float(input('Enter the initial value of the variable: '))

  try:
    func = sympify(func)
  except SympifyError:
    print('Invalid function entered')
  else:
    var = Symbol(var)
    d = Derivative(func, var).doit()
    value_min, x_axis = grad_descent(var0, d, var)

    print('{0}: {1}'.format(var.name, value_min))
    print('Minimum value: {0}'.format(func.subs({ var: value_min})))
    draw_graph(x_axis, func, var)