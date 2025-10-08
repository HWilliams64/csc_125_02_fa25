my_sentence = "The dog jumped over the car"

# index = 0
# for char in my_sentence:
#     print(f"Character: {char} at index: {index}")
#     index += 1


for index, char in enumerate(my_sentence[::-1]):
    print(f"Character: {char} at index: {index}")
