# Multiplication table printer
# A multiplication table for a number lists all of that number’s multiples.


def multi_table(a: int) -> None:
    for i in range(1, 11):
        print("{0} x {1} = {2}".format(a, i, a * i))


if __name__ == "__main__":
    a = input("Enter a number: ")
    multi_table(float(a))
