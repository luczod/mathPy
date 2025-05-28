'''
3: Area Between Two Curves

F(b) - F(a)
'''

from sympy import  Integral, Symbol, sympify, SympifyError
from typing import Any

def find_area(f1x: Any, f2x: Any,var: Symbol, a: float, b: float) -> float:
    a = Integral(f1x - f2x, (var, a, b)).doit() # type: ignore
    return a

if __name__ == '__main__':

    f1x = input('Enter the upper function in one variable: ')
    f2x = input('Enter the lower upper function in one variable: ')
    var = input('Enter the variable: ')
    a = float(input('Enter the lower bound of the enclosed region (a): '))
    b = float(input('Enter the upper bound of the enclosed region (b): '))
    try:
        func_upper = sympify(f1x)
        func_lower = sympify(f2x)
    except SympifyError:
        print('One of the functions entered is invalid')
    else:
        var = Symbol(var)
        print('Area enclosed by {0} and {1} is: {2} '.format(func_upper, func_lower, find_area(func_upper, func_lower, var, a, b)))
