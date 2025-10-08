def number_input(prompt):
    user_input = input(prompt)
    while not user_input.isnumeric():
        print(f"The value {user_input} is not a proper number")
        user_input = input(prompt)

    number = int(user_input)
    return number

def get_two_numbers(prompt):
    number_1 = number_input(prompt)
    number_2 = number_input(prompt)
    return number_1, number_2


def add(x=0, y=0, z=0):
    return x + y - z


r = add(4, 5, z=1)
print(r)
def result(x, y, op=None, overdirer=None)
    pass

result(2, 1)
result(1, 2, 4)
