# 4: Solving Single-Variable Inequalities1

from sympy import Poly, Symbol, pprint
from sympy import solve_poly_inequality, solve_univariate_inequality, sympify, solve_rational_inequalities

x = Symbol('x')


def isolve(inequality):
  x = Symbol('x')
  ineq_obj = inequality
  lhs = ineq_obj.lhs

  if lhs.is_polynomial():
    p = Poly(lhs, x)
    rel = ineq_obj.rel_op
    result = solve_poly_inequality(p, rel)

    return result

  if lhs.is_rational_function():
    numer, denom = lhs.as_numer_denom()

    p1 = Poly(numer)
    p2 = Poly(denom)
    rel = ineq_obj.rel_op
    result = solve_rational_inequalities([[((p1, p2), rel)]])

    return result

  ineq_obj = inequality
  result = solve_univariate_inequality(ineq_obj, x, relational=False)

  return result

if __name__ == '__main__':
  equation = input('Enter the inequality expression: ')
  result = isolve(sympify(equation))
  pprint(result)



