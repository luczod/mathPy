# 1: Even-Odd Vending Machine


def even_odd(a: float) -> None:
    if a % 2 == 0:
        print("the number is even")
        for i in range(int(a + 2), int(a + 20), 2):
            print(f"Followd by: {i}")
    else:
        print("the number is odd")
        for i in range(int(a + 2), int(a + 20), 2):
            print(f"Followd by: {i}")


if __name__ == "__main__":
    a = input("Enter a number: ")
    even_odd(float(a))
