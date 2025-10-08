pie = "hello"

for apple in pie:
    print(apple)
print("="*40)

length = len(pie)
index = 0

while index < length:
    print(pie[index])
    index = index + 1
    #print(f"index: {index} length: {length}")
    # if index >= length:
    #    break