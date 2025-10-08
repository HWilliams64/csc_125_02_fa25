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


menu_options = ("a", "s", "q")
while True:
    user_input = input("Type:\na - add\ns - subtract\nq - to quit\n")
    clean_input = user_input.casefold().strip()

    if clean_input not in menu_options:
        print(f"The option '{user_input}' is not defined")
        continue

    if clean_input == "a":
        number_1, number_2 = get_two_numbers("Type a number for addition:")

        print(f"{number_1} + {number_2} = {add(number_1, number_2)}")

    elif clean_input == "s":
        number_1, number_2 = get_two_numbers("Type a number for subtraction:")

        print(f"{number_1} - {number_2} = {number_1 - number_2}")
    else:
        break
