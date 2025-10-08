def add(x: int | float | str, y: int | float | str) -> int | float | str:
    """
    This function accepts 2 numbers 
    and returns the sum of the the numbers

    x: int is a number
    y: int is a number to be added to x

    return int the sum of x and y
    """
    x = str(x)
    y = str(y)

    if x.isdigit() and y.isdigit():
        x = float(x)
        y = float(y)
    
    v = x + y # type: ignore
    return v


v = add("1", 1)

print(f"returned value = {v}")

def minus(x:int, y:int)