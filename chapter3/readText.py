'''
Calculating the mean of numbers stored in a file
'''

import pathlib
current_dir = pathlib.Path(__file__).parent.resolve()

def sum_data(filename: str):
  s = 0
  with open(filename,'r') as file:
    for line in file.readlines():
      s = s + float(line)

    print('Sum of the numbers: {0}'.format(s))

def read_data(filename: str) -> list[float]:
  numbers = []

  with open(filename,'r') as file:
    for line in file:
      numbers.append(float(line))

  return numbers

def calculate_mean(numbers: list[float]) -> float:
  s = sum(numbers)
  N = len(numbers)
  mean = s/N

  return mean

if __name__ == '__main__':
  data = read_data(f'{current_dir}/mydata.txt')
  mean = calculate_mean(data)
  print('Mean: {0}'.format(mean))