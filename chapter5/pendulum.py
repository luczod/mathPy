'''
the amount of time it takes for the pendulum to
complete one full swing

T = 2*pi*sqrt(L/g)
'''

from sympy import FiniteSet, pi


def time_period(length: int, g: float) -> float:
  # g = 9.8
  T = 2*pi*(length/g)**0.5
  return T

if __name__ == '__main__':
  # centimeters
  L = FiniteSet(15, 18, 21, 22.5, 25)
  g_values = FiniteSet(9.8, 9.78, 9.83)
  print('{0:^15}{1:^15}{2:^15}'.format('Length(cm)', 'Gravity(m/s^2)', 'Time Period(s)'))

  for elem in L*g_values: # type: ignore
    l = elem[0]
    g = elem[1]
    t = time_period(l/100, g)

    print('{0:^15}{1:^15}{2:^15.3f}'.format(float(l), float(g), float(t)))