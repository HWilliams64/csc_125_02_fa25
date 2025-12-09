class MyCustomException(Exception):
    pass


def a(x, y, op) -> int:
    if op not in ("+", "-", "*", "/"):
        raise ValueError(f"The operation \"{op}\" is not recognized")

    if op == "/" and y == "0":
        raise MyCustomException("You cannot divide by zero")

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

    return (x ** 3) + x * y


def b(x, y, op):
    try:
        return a(x, y, op)
    except Exception as e:
        print(f"Warning: a() failed because {e}")
        return 0


def c(x, y, op):
    return b(x, y, op)


def d(x, y, op):
    return c(x, y, op)


def e(x, y, op):
    return d(x, y, op)


x = input("Please type a number:")
y = input("Please type a number:")
op = input("Please type an operation:")
result = e(x, y, op)
print(f"Result: {result}")
