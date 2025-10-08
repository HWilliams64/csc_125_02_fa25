def function(*args, **kwargs):
    first_value = args[0]
    apple = kwargs["apple"]
    print(f"1st value = {first_value} Apple = {apple}")



function(1,2,3,4,5,6,7, apple="pie", grape="wine")