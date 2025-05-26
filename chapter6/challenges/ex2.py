# 2: Drawing the Sierpiński Triangle
# transformations functions
# list of probability

import random
import matplotlib.pyplot as plt


def transformation_1(point: tuple[float,float]) ->  tuple[float,float]:
  x = point[0]
  y = point[1]

  x1 = 0.5*x
  y1 = 0.5*y

  return x1, y1


def transformation_2(point: tuple[float,float]) ->  tuple[float,float]:
  x = point[0]
  y = point[1]

  x1 = 0.5*x + 0.5
  y1 = 0.5*y + 0.5

  return x1, y1


def transformation_3(point: tuple[float,float]) ->  tuple[float,float]:
  x = point[0]
  y = point[1]

  x1 = 0.5*x + 1
  y1 = 0.5*y

  return x1, y1



def get_index(probability: list[float]) -> int:
  r = random.random()
  acum_probability = 0
  sum_probability = []

  for p in probability:
    acum_probability += p
    sum_probability.append(acum_probability)

  for item, sp in enumerate(sum_probability):
    if r <= sp:
      return item

  # fallback: if none of the conditions match due to floating-point, return the last index.
  return len(probability)-1


def transform(point: tuple[float,float]) ->  tuple[float,float]:
  # List of transformation functions
  transformations = [transformation_1, transformation_2,
                      transformation_3]
  probability = [1/3, 1/3, 1/3]

  # Pick a random transformation function and call it
  tindex = get_index(probability)
  transform_func = transformations[tindex]
  x, y = transform_func(point)

  return x, y


def draw_triangle(n: int) -> tuple[list[float],list[float]]:
  # We start with (0, 0)
  x = [0.0]
  y = [0.0]

  x1, y1 = 0, 0
  for i in range(n):
    x1, y1 = transform((x1, y1))
    x.append(x1)
    y.append(y1)

  return x, y


if __name__ == '__main__':
  n = int(input('Enter the number of points in the Sierpiński triangle: '))
  x, y = draw_triangle(n)

  # Plot the points
  plt.plot(x, y, 'o')
  plt.title('Sierpiński with {0} points'.format(n))
  plt.show()