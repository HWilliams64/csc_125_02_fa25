def a(x, y) -> int:
    try:
        x = int(x)
    except ValueError:
        print(f"Error: {x} cannot be converted to a number")
        x = 0
    try:
        y = int(y)
    except BaseException as e:
        print(f"Error: {e}")
        y = 0

    return x + y


def b(x, y):
    try:
        return a(x, y)
    except:
        return 0


def c(x, y):
    return b(x, y)


def d(x, y):
    return c(x, y)


def e(x, y):
    return d(x, y)


x = input("Please type a number:")
y = input("Please type a number:")
result = e(x, y)
print(f"Result: {result}")