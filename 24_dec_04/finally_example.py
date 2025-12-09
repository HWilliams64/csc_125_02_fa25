def fun():
    try:
        print("Before dividing")
        1/0
        print("After dividing")
        return 0
    except BaseException as e:
        print(f"There was an error in the code, \"{e}\"")
        return 1
    finally:
        print("This is the final thing I am doing")
        return 2
r = fun()
print(f"returned value: {r}")
print("Outside of the try-except block")