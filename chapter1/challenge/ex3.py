# 3: Enhanced Unit Converter
# Unit converter: Miles and Kilometers


def print_menu():
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    print("3. kilograms to pounds")
    print("4. Pounds to kilograms")
    print("5. Celsius to fahrenheit")
    print("6. Fahrenheit to celsius")


def km_miles():
    km = float(input("Enter distance in kilometers: "))
    miles = km / 1.609

    print("Distance in miles: {0}".format(miles))


def miles_km():
    miles = float(input("Enter distance in miles: "))
    km = miles * 1.609

    print("Distance in kilometers: {0}".format(km))


def kg_pounds():
    kg = float(input("Enter mass in kilograms: "))
    pounds = kg / 0.45359237

    print("Mass in pounds: {0}".format(pounds))


def pounds_kg():
    pounds = float(input("Enter mass in pounds: "))
    kg = pounds * 0.45359237

    print("Mass in kilograms: {0}".format(kg))


def celsius_fahrenheit():
    celsius = float(input("Enter temperature in celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32

    print("Temperature in fahrenheit: {0}".format(fahrenheit))


def fahrenheit_celsius():
    fahrenheit = float(input("Enter temperature in fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9

    print("Temperature in celsius: {0}".format(celsius))


if __name__ == "__main__":
    print_menu()
    try:
        choice = input("Which conversion would you like to do?: ")
    except KeyboardInterrupt:
        print("\nExiting program.")

    match choice:
        case "1":
            km_miles()
        case "2":
            miles_km()
        case "3":
            kg_pounds()
        case "4":
            pounds_kg()
        case "5":
            celsius_fahrenheit()
        case "6":
            fahrenheit_celsius()
