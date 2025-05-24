# 3: Summing a Series

from sympy import symbols,sympify, summation, pprint

def sum_series(equation, n_value):
  # a,d, n = symbols('a,d,n')
  n = symbols('n')
  s = summation(equation, (n, 1, n_value))
  pprint(s)


if __name__ == '__main__':
  equation = input('Enter the nth term: ')
  n = input('Enter the number of terms: ')
  sum_series(sympify(equation), int(n))