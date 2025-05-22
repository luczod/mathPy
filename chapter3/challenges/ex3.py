# 3: Experiment with Other CSV Data

# 2: Statistics Calculator
import pathlib
import csv
from collections import Counter
from matplotlib import pyplot as plt
from numpy.typing import ArrayLike
current_dir = pathlib.Path(__file__).parent.resolve()


def draw_graph(x: ArrayLike, y: ArrayLike):
  plt.bar(x, y)
  plt.xlabel('years')
  plt.ylabel('population')
  plt.title('USA Population')
  plt.show()


def read_csv(filename: str) -> tuple[list[str], list[int]]:
  years = []
  population = []

  with open(filename, "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
      years.append(str(row[0])[:4])
      population.append(int(float(row[1])))

    return years, population

def calculate_mean(numbers: list[int]) -> float:
  s = sum(numbers)
  N = len(numbers)
  mean = s/N

  return mean


def calculate_median(numbers: list[int]) -> float:
    N = len(numbers)
    numbers.sort()

    # Find the median
    if N % 2 == 0:
        # if N is even
        m1 = N/2
        m2 = (N/2) + 1
        # Convert to integer, match position
        m1 = int(m1) - 1
        m2 = int(m2) - 1
        median = (numbers[m1] + numbers[m2])/2
    else:
        m = (N+1)/2
        # Convert to integer, match position
        m = int(m) - 1
        median = numbers[m]
    return median


def calculate_mode(numbers: list[int]) -> list[tuple[int]]:
    c = Counter(numbers)
    numbers_freq = c.most_common()
    max_count = numbers_freq[0][1]

    modes = []
    for num in numbers_freq:
        if num[1] == max_count:
            modes.append(num[0])
    return modes


def find_differences(numbers: list[int]) -> list[float]:
  # Find the mean
  mean = calculate_mean(numbers)
  # Find the differences from the mean
  diff = []
  for num in numbers:
    diff.append(num - mean)
  return diff

def calculate_variance(numbers: list[int]) -> float:
  # Find the list of differences
  diff = find_differences(numbers)
  # Find the squared differences
  squared_diff = []
  for d in diff:
    squared_diff.append(d**2)

  # Find the variance
  sum_squared_diff = sum(squared_diff)
  variance = sum_squared_diff/len(numbers)

  return variance

if __name__ == '__main__':
  year , population = read_csv(f'{current_dir}/USA_SP_POP_TOTL.csv')
  year = year[:-1]
  population = population[:-1]
  mean = calculate_mean(population)
  median = calculate_median(population)
  mode = calculate_mode(population)
  variance = calculate_variance(population)
  standard_deviation = variance**0.5
  print('mean: {0:.2f}\nmedian: {1:.2f}\nmode: {2:.2f}\nvariance: {3:.2f}\n' \
  'standard deviation: {4:.2f}'.format(mean,median,mode[0],variance,standard_deviation))
  draw_graph(year,population)
