import csv
import pathlib
import matplotlib.pyplot as plt
from numpy.typing import ArrayLike
from correlation import find_corr_x_y

current_dir = pathlib.Path(__file__).parent.resolve()

def scatter_plot(x: ArrayLike, y: ArrayLike):
  plt.scatter(x, y)
  plt.xlabel('Number')
  plt.ylabel('Square')
  plt.show()


def read_csv(filename: str) -> tuple[list[float], list[float]]:

  with open(filename, "r") as file:
    reader = csv.reader(file)
    next(reader)

    summer = []
    highest_correlated = []
    for row in reader:
      summer.append(float(row[1]))
      highest_correlated.append(float(row[2]))

    return summer, highest_correlated


if __name__ == '__main__':
  summer, highest_correlated = read_csv(f'{current_dir}/correlate-summer.csv')
  corr = find_corr_x_y(summer, highest_correlated)
  print('Highest correlation: {0}'.format(corr))
  scatter_plot(summer, highest_correlated)