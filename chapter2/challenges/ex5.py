# 5: Exploring the Relationship Between the Fibonacci Sequence and the Golden Ratio

import matplotlib.pyplot  as plt


def fibo(n: int) -> list[int]:
  if n == 1:
    return [1]
  if n == 2:
    return [1, 1]

  # n > 2
  a = 1
  b = 1

  # First two members of the series
  series = [a, b]
  for i in range(n):
    c = a + b
    series.append(c)
    a = b
    b = c
  return series

def ratio_fibo(fibo: list[int]) -> list[float]:
  if len(fibo) == 1:
    return [1]
  if len(fibo) == 2:
    return [1, 1]

  # n > 2
  series_ratio = []
  for i in range(len(fibo)):
    if i >= len(fibo) - 1:
      c = fibo[i] / fibo[i - 1]
      series_ratio.append(c)
      return series_ratio

    c = fibo[i + 1] / fibo[i]
    series_ratio.append(c)
  return series_ratio

x_numbers = range(0,102)
temp_fibo = fibo(100)
y_numbers = ratio_fibo(temp_fibo)
print(temp_fibo)
print()
print(y_numbers)

plt.plot(x_numbers,y_numbers)
plt.xlabel('No')
plt.ylabel('Ratio')
plt.show()
# 618033988749895