'''
Example of selecting a transformation from two equally probable
transformations

A basic idea in creating fractals—starting from an initial point
and applying a transformation to that point repeatedly
'''
import matplotlib.pyplot as plt
import random


def transformation_1(p: tuple[int,int]) -> tuple[int,int]:
  x = p[0]
  y = p[1]

  return x + 1, y - 1


def transformation_2(p: tuple[int,int]) -> tuple[int,int]:
  x = p[0]
  y = p[1]

  return x + 1, y + 1


def transform(point: tuple[int,int]) -> tuple[int,int]:
  # List of transformation functions
  transformations = [transformation_1, transformation_2]

  # Pick a random transformation function and call it
  transform_func = random.choice(transformations)
  x, y = transform_func(point)

  return x, y


def build_trajectory(p: tuple[int,int], n: int) -> tuple[list[int],list[int]]:
  x = [p[0]]
  y = [p[1]]

  for i in range(n):
    p = transform(p)
    x.append(p[0])
    y.append(p[1])

  return x, y


if __name__ == '__main__':
  # Initial point
  p = (1, 1)
  n = int(input('Enter the number of iterations: '))
  x, y = build_trajectory(p, n)

  # Plot
  plt.plot(x, y)
  plt.xlabel('X')
  plt.ylabel('Y')
  plt.show()