'''
# 4: Finding the Length of a Curve

F(b) - F(a)
'''

from sympy import  Integral, Derivative, Symbol, sympify, sqrt, SympifyError
from typing import Any

def find_area(fx: Any, var: Symbol, a: float, b: float) -> float:
    deriv = Derivative(fx, var).doit()
    # the length of arc
    length = Integral(sqrt(1+deriv**2), (var, a, b)).doit().evalf() # type: ignore

    return length # type: ignore

if __name__ == '__main__':

    f1x = input('Enter the function in one variable: ')
    var = input('Enter the variable: ')
    a = float(input('Enter x of first point (a): '))
    b = float(input('Enter x of second point (b): '))
    try:
        func = sympify(f1x)
    except SympifyError:
        print('One of the functions entered is invalid')
    else:
        var = Symbol(var)
        y1 = func.subs({ var: a })
        pointer1 = (a, int(y1) )
        y2 = func.subs({ var: b })
        pointer2 = (b, int(y2) )

        print('Area enclosed by {0} and {1} is: {2:.3f} '.format(pointer1, pointer2, find_area(func, var, a, b)))