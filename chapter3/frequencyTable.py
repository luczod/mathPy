"""
Frequency table for a list of numbers
"""

from collections import Counter


def frequency_table(numbers: list[int]):
    table = Counter(numbers)
    print("Number\tFrequency")
    numbers_freq = table.most_common()
    numbers_freq.sort()

    for number in numbers_freq:
        print("{0}\t{1}".format(number[0], number[1]))


if __name__ == "__main__":
    scores = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
    frequency_table(scores)

