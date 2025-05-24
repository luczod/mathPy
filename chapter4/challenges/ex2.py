# 2: Graphical Equation Solver  2*x + 3*y - 6 2*x + 4*y - 12

from sympy import  symbols, sympify, solve, SympifyError
from sympy.plotting import plot

def plot_expression(expr1, expr2):
  x,y = symbols('x,y')
  solutions = solve(expr1, y)
  expr_y1 = solutions[0]
  solutions = solve(expr2, y)
  expr_y2 = solutions[0]

  soln = solve([expr1, expr2],(x,y))

  if not soln:
    print('No solution found')
  else:
    print(soln)

  p = plot(expr_y1, expr_y2, legend=True, show=False)
  p[0].line_color = 'b'
  p[1].line_color = 'r'
  p.show()

if __name__ == '__main__':
    expr1 = input('Enter your first expression in terms of x and y: ')
    expr2 = input('Enter your second expression in terms of x and y: ')
    try:
      expr1 = sympify(expr1)
      expr2 = sympify(expr2)
    except SympifyError:
      print('Invalid input')
    else:
      plot_expression(expr1, expr2)
