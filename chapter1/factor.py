# When a nonzero integer, a, divides another integer, b, leaving a remainder
# 0, a is said to be a factor of b.


def is_factor(a: int, b: int) -> bool:
    if b % a == 0:
        return True
    else:
        return False


# Is 4 a factor of 1024?
result = is_factor(4, 1024)


# Find the factors of an integer
def factors(b: int) -> None:
    for i in range(1, b + 1):
        if b % i == 0:
            print(i)


if __name__ == "__main__":
    b = input("Your Number Please: ")
    b = float(b)

    if b > 0 and b.is_integer():
        factors(int(b))
    else:
        print("Please enter a positive integer")
