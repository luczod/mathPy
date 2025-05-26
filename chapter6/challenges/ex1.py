# 1: Packing Circles into a Square

'''
Draw a square
'''
from matplotlib import pyplot as plt
import matplotlib.patches as patches

def draw_square():
  ax = plt.axes(xlim = (0, 6), ylim = (0, 6))
  square = patches.Polygon([(1, 1), (5, 1), (5, 5), (1, 5)], closed = True)
  ax.add_patch(square)

  for x in range(1,5):
    for y in range(1,5):
      circle = patches.Circle((x + 0.5, y + 0.5), fc="w",ec="b", radius=0.5)
      ax.add_patch(circle)


  ax.set_aspect('equal')
  plt.show()


if __name__ == '__main__':
  draw_square()