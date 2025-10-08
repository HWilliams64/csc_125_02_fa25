from typing import Callable

x = 2
y = 2
def minus(x: int, y:int) ->int:
    return x - y

def add(x: int, y: int) -> int:
    return x + y


def calc(x:int, y:int, op:Callable[[int, int], int]) -> int:
    value = op(x, y)
    return value


r = calc(x=6, y=7, op=minus)
r = calc(r, y, add)
print(f"Result = {r}")