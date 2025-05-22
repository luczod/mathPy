# 4: Finding the Percentile
# if a student obtained a 95 percentile score on an exam, this means that 95 percent of
# the students scored less than or equal to the student’s score.

from ex2 import read_data
# from math import modf

def calculate_percentile(data: list[int], p: int) -> float:
  if p < 0 or p > 100:
      ValueError("Out of range 100")

  data.sort()
  n = len(data)

  r = (p/100) * (n - 1) + 1

  if(isinstance(r, int)):
    return data[r]

  # frac, whole = modf(r)
  i = int(r)
  f = r - i
  # first element is 0 in a array but is 1 in mathematics
  real_idx = i - 1

  percentile = data[real_idx] + f * (data[real_idx + 1] - data[real_idx])

  return percentile


if __name__ == '__main__':
  filename = input("Enter the file name: ")
  data = read_data(filename)
  # data = [5, 1, 9, 3, 14, 9, 7]
  result = calculate_percentile(data, 50)
  print(result)