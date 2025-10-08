from time import sleep


# print("Hello\n1\n2\n\t3")

# print("4", end="")
# print("\r5", end="")
# print("\r6", end="")
# print()

for i in range(0, 10):
    print(f"\r{i}", end="")
    sleep(1)
    