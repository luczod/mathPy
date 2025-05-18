# 2: Exploring a Quadratic Function Visually
import matplotlib.pyplot as plt
from numpy.typing import ArrayLike

# Assume values of x
x_values = [-12,-9,-8,-5,-3, 3, 5, 8, 9, 12]
y_values = []

for x in x_values:
  # Calculate the value of the quadratic function
  y = x**2 + 2*x + 1
  y_values.append(y)
  print('x={0} y={1}'.format(x, y))


def create_graph(x_axis: ArrayLike, y_axis: ArrayLike):
  plt.plot(x_axis, y_axis, marker='o')
  plt.show()


create_graph(x_values, y_values)
# nonlinear