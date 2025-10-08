from content..helpers import get_two_numbers, add

while True:
    user_input = input("Type:\na - add\ns - subtract\ne - to quit\n")
    clean_input = user_input.casefold().strip()

    if clean_input not in "ase":
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
