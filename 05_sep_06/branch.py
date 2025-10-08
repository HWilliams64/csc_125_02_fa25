ui = input("Please type a number:")
user_number = int(ui)


if 1 <= user_number <= 10 and user_number % 2 == 0:
    print(f"The number {user_number} is between 1-10 and is even")

    if user_number > 5:
        print(f"The {user_number} is larger than 5")

elif 1 > user_number or user_number > 10:
    print(f"The number {user_number} not between 1 and 10")

elif user_number % 2 != 0:
    print(f"The number {user_number} not even")

else:
    print(f"The number {user_number} is either not between 1-10 and or is odd")

print("default")


# not 3 % 2 == 0
# not False => True

# not True => False