from sympy import Symbol, solve

x = Symbol('x')
y = Symbol('y')

expr1 = 2*x + 3*y - 6 # type: ignore
expr2 = 3*x + 2*y - 12 # type: ignore
result = solve((expr1, expr2), dict=True)

print(result)