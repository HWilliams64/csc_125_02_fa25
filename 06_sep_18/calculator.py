while True:
    user_input = input("Type:\na - add\ns - subtract\ne - to quit\n")
    clean_input = user_input.casefold().strip()
    
    if clean_input not in "ase":
        print(f"The option '{user_input}' is not defined")
        continue

    if clean_input == "a":
        number_1 = input("Please type a number:")
        if not number_1.isnumeric():
            print(f"The value {number_1} is not valid number")
            continue
        number_2 = input("Please type a number:")
        if not number_2.isnumeric():
            print(f"The value {number_2} is not valid number")
            continue

        print(f"{number_1} + {number_2} = {int(number_1) + int(number_2)}")

    elif clean_input == "s":
        number_1 = input("Please type a number:")
        if not number_1.isnumeric():
            print(f"The value {number_1} is not valid number")
            continue
        number_2 = input("Please type a number:")
        if not number_2.isnumeric():
            print(f"The value {number_2} is not valid number")
            continue

        print(f"{number_1} + {number_2} = {int(number_1) - int(number_2)}")
    else:
        break
