# 3: Exploring Hénon’s Function
# one transformation function
# as you create more points, they start lying along curved lines

import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.lines import Line2D


def transform(point: tuple[float,float]) ->  tuple[float,float]:
  x,y  = point

  x1 = y + 1 - 1.4*x**2
  y1 = 0.3*x

  return x1, y1


def draw_curve(n: int) -> tuple[list[float],list[float]]:
  # We start with (0, 0)
  p = (0.0, 0.0)
  x = [p[0]]
  y = [p[1]]

  for i in range(n):
    p = transform(p)
    x.append(p[0])
    y.append(p[1])

  return x, y


def update_points(i: int, x: list[float], y: list[float], plot: Line2D) -> tuple[Line2D]:
    plot.set_data(x[:i], y[:i])
    return plot,


if __name__ == '__main__':
  n = int(input('Enter the number of iterations to the Hénon function: '))
  x, y = draw_curve(n)

  # Plot the points
  fig = plt.gcf()
  ax = plt.axes(xlim = (min(x), max(x)),
                ylim = (min(y), max(y)))

  plot = plt.plot([], [], 'o')[0]
  anim = animation.FuncAnimation(fig, update_points,
                                 fargs=(x, y, plot),
                                 frames = len(x),
                                 interval = 25)

  plt.title('The Hénon function with {0} points'.format(n))
  plt.show()