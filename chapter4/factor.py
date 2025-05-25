from sympy import Symbol, factor, expand, pprint

x = Symbol("x")
y = Symbol("y")

expr = x**3 + 3 * x**2 * y + 3 * x * y**2 + y**3  # type: ignore
factors = factor(expr)
# print(factors)
# print(expand(factors))

pprint(factors)
pprint(expand(factors))
