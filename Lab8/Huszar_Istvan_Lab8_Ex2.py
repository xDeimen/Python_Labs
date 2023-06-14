def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def percentage(x):
    return x / 100


def negate(x):
    return -x


def cancel(x):
    return x[:-1]


def calculator():
    while True:
        print("Select operation.")
        print("1.+")
        print("2.-")
        print("3.x")
        print("4./")
        print("5.%")
        print("6.!")
        print("7.Cancel")
        print("8.Quit")

        pick = input("Enter choice(1/2/3/4/5/6/7/8): ")

        if pick in ('1', '2', '3', '4'):
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))

            if pick == '1':
                print(x, "+", y, "=", add(x, y))

            elif pick == '2':
                print(x, "-", y, "=", subtract(x, y))

            elif pick == '3':
                print(x, "*", y, "=", multiply(x, y))

            elif pick == '4':
                print(x, "/", y, "=", divide(x, y))

        elif pick == '5':
            x = float(input("Enter a number: "))
            print(x, "% =", percentage(x))

        elif pick == '6':
            x = float(input("Enter a number: "))
            print("-", x, "=", negate(x))

        elif pick == '7':
            x = input("Enter a number: ")
            print(cancel(x))

        elif pick == '8':
            break

        else:
            print("Invalid input")
calculator()

