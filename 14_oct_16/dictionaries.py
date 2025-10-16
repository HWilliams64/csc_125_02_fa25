my_dictionary = {True: "apple", "B": "beef", "C": "beef"}
print(my_dictionary)

my_dictionary["A"] = "pie"
my_dictionary.setdefault("A", "sauce")

# Below is the long way for `my_dictionary.setdefault("A", "sauce")`
if "A" not in my_dictionary:
    my_dictionary['A'] = "sauce"

my_dictionary['D'] = "dominos"
print(my_dictionary.get("D", "dog"))

# Below is the long way for `my_dictionary.get("D", "dog")`
if "D" in my_dictionary:
    value = my_dictionary['D']
else:
    value = "dog"
