import csv
import pathlib
import matplotlib.pyplot as plt
from numpy.typing import ArrayLike

current_dir = pathlib.Path(__file__).parent.resolve()

def scatter_plot(x: ArrayLike, y: ArrayLike):
  plt.scatter(x, y)
  plt.xlabel('Number')
  plt.ylabel('Square')
  plt.show()


def read_csv(filename: str) -> tuple[list[int], list[int]]:
  numbers = []
  squared = []

  with open(filename, "r") as f:
    reader = csv.reader(f)
    next(reader)

    for row in reader:
      numbers.append(int(row[0]))
      squared.append(int(row[1]))

    return numbers, squared


if __name__ == '__main__':
  numbers, squared = read_csv(f'{current_dir}/numbers.csv')
  scatter_plot(numbers, squared)