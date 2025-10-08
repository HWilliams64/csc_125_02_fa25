from typing import Callable


def capitalize(x:str, y:str):
    full = x.upper()+" "+y.upper()
    return full


def lowercase(x: str, y: str):
    full = x.lower()+" "+y.lower()
    return full

def main(x:str, y:str, capFunc:Callable):
    print(f"capFunc(): {capFunc}")
    value:str = capFunc(x, y)

    if value.isupper():
        print("The function capitalized the text")
    else:
        print("The function lowercased the text")


print(f"capitalize(): {capitalize}")
print(f"lowercase(): {lowercase}")
main("AppLe", "pIe", capitalize)
