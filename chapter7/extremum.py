'''
The term extremum (plural extrema) refers to the points where the func-
tion attains a local or global maximum or minimum
'''

from sympy import Symbol, solve, Derivative
x = Symbol('x')
f = x**5 - 30*x**3 + 50*x # type: ignore
d1 = Derivative(f, x).doit()

critical_points = solve(d1)
A = critical_points[2]
B = critical_points[0]
C = critical_points[1]
D = critical_points[3]
print(critical_points)

d2 = Derivative(f, x, 2).doit()
d2.subs({x:B}).evalf()
d2.subs({x:C}).evalf()
d2.subs({x:A}).evalf()
d2.subs({x:D}).evalf()
print(d2.subs({x:D}).evalf()) # type: ignore

