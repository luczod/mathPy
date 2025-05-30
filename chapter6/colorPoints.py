import matplotlib.pyplot as plt
import random


def initialize_image(x_p: int, y_p: int) -> list[list[int]]:
  image = []
  for i in range(y_p):
    x_colors = []
    for j in range(x_p):
      x_colors.append(0)
    image.append(x_colors)

  return image


def color_points():
  x_p = 40
  y_p = 40
  image = initialize_image(x_p, y_p)

  for i in range(y_p):
    for j in range(x_p):
      image[i][j] = random.randint(0, 10)

  plt.imshow(image, origin='lower', extent=(0, 5, 0, 5),
              cmap=plt.get_cmap("Grays_r"), interpolation='nearest')
  plt.colorbar()

  plt.show()

if __name__ == '__main__':
  color_points()