
number = 0

while True:
    number += 1 # <== number = number + 1

    if number % 2 == 0:
        continue
    else:
        pass

    print(number)

    if number > 100_000:
        break

print(f"The final number is {number}")

