from sympy import Limit, Symbol, S, sin
x = Symbol('x')

r = Limit(1/x, x, S.Infinity)
print(r)

l = Limit(1/x, x, S.Infinity)
print(l.doit())

l2 = Limit(sin(x)/x, x, 0).doit()
print(l2)

n = Symbol('n')
l3 = Limit((1+1/n)**n, n, S.Infinity).doit()
print(l3)

p = Symbol('p', positive=True)
r = Symbol('r', positive=True)
t = Symbol('t', positive=True)
l4 = Limit(p*(1+r/n)**(n*t), n, S.Infinity).doit()
print(l4)