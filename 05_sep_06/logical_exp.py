# 1 + 1 = 2 = True
# or    => +
# and   => x
# True  >= 1
# False == 0

# 1 * 1 = 1

result = True and True
#print(f"Result = {result}")

# 1 * 0 = 0
result = True and False
#print(f"Result = {result}")

# Testing Equality
# Equals Values are the same  ==
# Greater Than  >
# Less Than  <
# Greater Than or equals to >=
# Same identity `is` - same memory address

a = "happy" * 1000
b = "happy" * 1000

# print(f"Same value: {a == b}")
# print(f"Same identity: {a is None}")
# print(a)


ui = input("Please type a number:")
user_number = int(ui)
print(user_number % 2)

print(1 <= user_number <= 10 and user_number % 2 == 0)
# 1 <= 7 <= 10 and 7 % 2 == 0
# True and True and False
# 1 x 1 x 0 = 0