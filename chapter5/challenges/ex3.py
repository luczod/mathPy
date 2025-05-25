# 3: How Many Tosses Before You Run Out of Money?

import random


def coin_toss(amount: float) -> tuple[float,int]:
    cash = amount
    trials = 0

    while cash > 0:
        toss = random.randint(0,1)
        trials += 1
        if toss == 0:
            print("Tails! Current amount: {0}".format(cash - 1.50))
            cash -= 1.50
        else:
            print("Heads! Current amount: {0}".format(cash + 1.0))
            cash += 1.0

    return cash, trials


if __name__ == '__main__':
    amount = input("Enter your starting amount: ")
    cash,trials = coin_toss(float(amount))
    print("Game over :( Current amount: {0}. Coin tosses: {1}".format(cash,trials))