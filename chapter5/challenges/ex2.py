# 2: Law of Large Numbers
'''
According to the law of large numbers, the average value of results over
multiple trials approaches the expected value or Expectation(E), as the number of trials
increases.
'''

import random


def roll(num_trials: int) -> float:
    rolls = []

    for t in range(num_trials):
        rolls.append(random.randint(1, 6))

    return sum(rolls)/num_trials


if __name__ == '__main__':
    expected_value = 1*(1/6) + 2*(1/6) + 3*(1/6) + 4*(1/6) + 5*(1/6) + 6*(1/6)
    print('Expected value: {0}'.format(expected_value))

    for trial in [100, 1000, 10000, 100000, 500000]:
        avg = roll(trial)
        print('Trials: {0} Trial average {1}'.format(trial, avg))