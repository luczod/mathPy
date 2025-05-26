"""
The derivative of a function y = f(x) expresses the rate of change in the
dependent variable, y, with respect to the independent variable, x. It's
denoted as either f'(x) or dy/dx.
"""

from sympy import Symbol, Derivative, pprint
t = Symbol('t')
St = 5*t**2 + 2*t + 8 # type: ignore
result = Derivative(St, t)
d = result.doit().subs({t: 1})
print(result)
print(result.doit())
print(d)


x = Symbol('x')
f = (x**3 + x**2 + x)*(x**2+x) # type: ignore
d = Derivative(f, x).doit()
pprint(d)