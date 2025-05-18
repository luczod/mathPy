# 3: Enhanced Projectile Trajectory Comparison Program

from matplotlib import pyplot as plt
from numpy.typing import ArrayLike
import math

def draw_graph(x: ArrayLike, y: ArrayLike):
  plt.plot(x, y)
  plt.xlabel('x-coordinate')
  plt.ylabel('y-coordinate')
  plt.title('Projectile motion of a ball')


def frange(start: float, final: float, interval: float) -> list[float]:
  numbers = []
  while start < final:
    numbers.append(start)
    start = start + interval

  return numbers


def draw_trajectory(u: float, theta: float):
  # convert degrees to radians
  theta = math.radians(theta)
  # gravity
  G = 9.8

  # Time of flight
  t_flight = 2*u*math.sin(theta)/G
  print("time of flight: {0:.2f} segundos".format(t_flight))

  # Total Distance
  s_x = u*math.cos(theta)*t_flight
  print("maximum horizontal distance: {0:.2f} metros".format(s_x))

  s_y = u*math.sin(theta)*t_flight - 1/2*G*t_flight**2
  print("maximum vertical distance: {0} metros".format(s_y))

  # Find time intervals
  intervals = frange(0, t_flight, 0.001)
  # List of x and y coordinates
  x = []
  y = []

  for t in intervals:
    x.append(u*math.cos(theta)*t)
    y.append(u*math.sin(theta)*t - 0.5*G*t*t)

  draw_graph(x, y)


if __name__ == '__main__':
  try:
    u = float(input('Enter the initial velocity (m/s): '))
    theta = float(input('Enter the angle of projection (degrees): '))
  except ValueError:
    print('You entered an invalid input')
  else:
    draw_trajectory(u, theta)
    plt.show()