'''
Find the range
the dispersion tells us how far away the numbers in a set of data are from the mean of the
data set.
'''

def find_range(numbers: list[int]) -> tuple[int, int, int]:
    lowest = min(numbers)
    highest = max(numbers)
    # Find the range
    r = highest-lowest

    return lowest, highest, r

if __name__ == '__main__':
    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    lowest, highest, r = find_range(donations)
    print('Lowest: {0} Highest: {1} Range: {2}'.format(lowest, highest, r))