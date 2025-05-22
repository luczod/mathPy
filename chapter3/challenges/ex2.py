# 2: Statistics Calculator
import pathlib
from collections import Counter
current_dir = pathlib.Path(__file__).parent.resolve()


def read_data(filename: str) -> list[int]:
  numbers = []

  with open(filename,'r') as file:
    for line in file:
      numbers.append(float(line))

  return numbers

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
  filename = input("Enter the file name: ")
  data = read_data(filename)
  print(data)
  mean = calculate_mean(data)
  median = calculate_median(data)
  mode = calculate_mode(data)
  variance = calculate_variance(data)
  standard_deviation = variance**0.5

  print('\nmean\tmedian\tmode\tvariance\tstandard deviation')
  print('{0}\t{1}\t{2}\t{3:.4f}\t{4:.4f}'.format(mean,median,mode[0],variance,standard_deviation))