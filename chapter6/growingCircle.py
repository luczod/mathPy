'''
A growing circle
'''

from matplotlib import pyplot as plt
import matplotlib.patches as patches
from matplotlib import animation
from matplotlib.patches import Circle

def create_circle() -> Circle:
  circle = patches.Circle((0, 0), 0.05, fc="w", ec="b")
  return circle


def update_radius(i: int, circle: Circle) -> Circle:
  circle.radius = i*0.5
  return circle

def create_animation():
  fig = plt.gcf()
  ax = plt.axes(xlim=(-10, 10), ylim=(-10, 10))
  ax.set_aspect('equal')
  circle = create_circle()
  ax.add_patch(circle)

  anim = animation.FuncAnimation(
    fig, update_radius, fargs = (circle,), frames=30, interval=50) # type: ignore

  plt.title('Simple Circle Animation')
  plt.show()

if __name__ == '__main__':
  create_animation()