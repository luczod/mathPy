'''
Animate the trajectory of an object in projectile motion
'''

from matplotlib import pyplot as plt
from matplotlib import animation
import matplotlib.patches as patches
from matplotlib.patches import Circle
import math

G = 9.8

def get_intervals(u: float, theta: float) -> list[float]:
  t_flight = 2*u*math.sin(theta)/G
  intervals = []
  start = 0
  interval = 0.005

  while start < t_flight:
    intervals.append(start)
    start = start + interval

  return intervals


def update_position(i: int, circle: Circle, intervals:list[float], u: float, theta: float):
  t = intervals[i]
  x = u*math.cos(theta)*t
  y = u*math.sin(theta)*t - 0.5*G*t*t
  circle.center = x, y
  return circle


def create_animation(u: float, theta: float):
  intervals = get_intervals(u, theta)

  xmin = 0
  xmax = u*math.cos(theta)*intervals[-1]
  ymin = 0
  t_max = u*math.sin(theta)/G
  ymax = u*math.sin(theta)*t_max - 0.5*G*t_max**2

  fig = plt.gcf()
  ax = plt.axes(xlim=(xmin, xmax), ylim=(ymin, ymax))
  ax.set_aspect('equal')
  circle = patches.Circle((xmin, ymin), 1.0)
  ax.add_patch(circle)

  anim = animation.FuncAnimation(fig, update_position, # type: ignore
                    fargs=(circle, intervals, u, theta),
                    frames=len(intervals), interval=1,
                    repeat=False)

  plt.title('Projectil Motion')
  plt.xlabel('X')
  plt.ylabel('Y')
  plt.show()


if __name__ == '__main__':
  try:
    u = float(input('Enter the initial velocity (m/s): '))
    theta = float(input('Enter the angle of projection (degrees): '))
  except ValueError:
    print('You entered an invalid input')
  else:
    theta = math.radians(theta)
    create_animation(u, theta)