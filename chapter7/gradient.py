'''
Use gradient ascent to find the maximum value of a
single-variable function

Gradient ascent always takes us to the closest peak.
'''
from sympy import Derivative, Symbol, sympify, SympifyError, solve

def grad_ascent(x0: float, f1x: Derivative, x: Symbol) -> float:
  # Check if f1x=0 has a solution
  if not solve(f1x):
    raise Exception('Cannot continue, solution for {0}=0 does not exist'.format(f1x))

  epsilon = 1e-6
  step_size = 1e-4
  x_old = x0
  num_f1x = f1x.subs({x:x_old}).evalf() # type: ignore
  x_new = x_old + step_size*num_f1x # type: ignore

  while abs(x_old - x_new) > epsilon:
    x_old = x_new
    num_f1x = f1x.subs({x:x_old}).evalf() # type: ignore
    x_new = x_old + step_size*num_f1x # type: ignore

  return x_new


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
    value_max = grad_ascent(var0, d, var)

    print('{0}: {1}'.format(var.name, value_max))
    print('Maximum value: {0}'.format(f.subs({var:value_max})))