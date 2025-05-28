'''
Use gradient ascent to find the angle at which the projectile
has maximum range for a fixed velocity, 25 m/s
'''
import math
from sympy import Derivative, Symbol, sin

def grad_ascent(x0: float, f1x: Derivative, x: Symbol) -> float:
  epsilon = 1e-6 # small positive value close to 0
  step_size = 1e-4
  x_old = x0
  num_f1x = f1x.subs({x:x_old}).evalf() # type: ignore
  x_new = x_old + step_size*num_f1x # type: ignore

  while abs(x_old - x_new) > epsilon:
    x_old = x_new
    x_new = x_old + step_size*f1x.subs({x:x_old}).evalf()  # type: ignore

  return x_new


def find_max_theta(R: float, theta: Symbol) -> float:
  # Calculate the first derivative
  R1theta = Derivative(R, theta).doit()
  theta0 = 1e-3
  theta_max = grad_ascent(theta0, R1theta, theta)

  return theta_max


if __name__ == '__main__':
  g = 9.8
  # Assume initial velocity
  u = 25

  # Expression for range
  theta = Symbol('theta')
  R = u**2*sin(2*theta)/g # type: ignore

  theta_max = find_max_theta(R, theta)
  print('Theta: {0}'.format(math.degrees(theta_max)))
  print('Maximum Range: {0}'.format(R.subs({theta:theta_max})))