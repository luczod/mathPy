# 2: Enhanced Multiplication Table Generator
# Multiplication table printer


def multi_table(a: float, b: float) -> None:
    for i in range(1, int(b + 1)):
        print("{0} x {1} = {2}".format(int(a), i, int(a * i)))


if __name__ == "__main__":
    a = input("Enter a number: ")
    b = input("Amount of multiples: ")
    multi_table(float(a), float(b))
