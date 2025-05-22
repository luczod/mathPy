# 5: Creating a Grouped Frequency Table
from collections import Counter

def create_classes(numbers: list[int], n: int) -> list[tuple[float, float]]:
  low = min(numbers)
  high = max(numbers)

  # Width of each class
  width = (high - low)/n
  classes = []
  a = low
  b = low + width
  classes = []

  while a < (high-width):
    classes.append((a, b))
    a = b
    b = a + width

  # The last class may be of a size that is less than width
  classes.append((a, high+1))
  print(classes)
  return classes

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

def frequency_table(numbers: list[int]):
    median = calculate_median(numbers)
    table = Counter(numbers)
    numbers_freq = table.most_common()
    numbers_freq.sort()
    grade1 = []
    grade2 = []

    for item in numbers_freq:
      if item[0] < median - 1:
        grade1.append(item[1])
        continue
      grade2.append(item[1])

    print('Grade\tFrequency')
    print("1-6\t{0}".format(sum(grade1)))
    print("6-11\t{0}".format(sum(grade2)))


if __name__=='__main__':
    scores = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
    frequency_table(scores)