'''
Default range of x values was automatically
chosen: -10 to 10.

'''

from sympy.plotting import plot
from sympy import Symbol

x = Symbol('x')
# plot(2*x+3)
# plot((2*x + 3), (x, -5, 5))
plot(2*x + 3, (x, -5, 5), title='A Line', xlabel='x', ylabel='2x+3') # type: ignore