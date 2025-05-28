'''
Function F(x), such that F'(x) = f(x). That is, the integral of a function is
another function whose derivative is the original function f(x)
'''

from sympy import Integral, Symbol, exp, sqrt, pi,S

x = Symbol('x')
k = Symbol('k')
result = Integral(k*x, x) # type: ignore
print(result.doit())

definite = Integral(k*x, (x, 0, 2)).doit() # type: ignore
print(definite)

definite = Integral(x, (x, 2, 4)).doit()
print(definite)


p = exp(-(x - 10)**2/2)/sqrt(2*pi) # type: ignore
probability_density_function= Integral(p, (x, S.NegativeInfinity, S.Infinity)).doit().evalf()
print(probability_density_function)