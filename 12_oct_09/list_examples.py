# Create
my_grocery_list = ["eggs", "wine", "fruits", "coffee", "bread"]

# Add
# print(my_grocery_list)
# my_grocery_list.append("water")
# print(my_grocery_list)
# my_grocery_list.insert(0,"chicken")
# print(my_grocery_list)
# other_stuff = ["candy"]
# new_list =  my_grocery_list[:3]+other_stuff+my_grocery_list[3:]
# Remove
# del my_grocery_list[-1]
# print(my_grocery_list)
# my_grocery_list.pop(0)
# print(my_grocery_list)
# my_grocery_list.remove("fruits")
# print(my_grocery_list)

# my_grocery_list_rev = my_grocery_list[::-1]
# my_grocery_list_rev.remove("fruits")
# my_grocery_list = my_grocery_list_rev[::-1]
# print(my_grocery_list)
# Iterate
# for index, element in enumerate(my_grocery_list):
#     print(f"'{element}' at {index} is a ", type(element))


def swap(v1, v2, l: list):
    index_value_1: int = l.index(v1)
    index_value_2 = l.index(v2)
    l.pop(index_value_1)
    l.pop(index_value_2-1)
    
    l.insert(index_value_1, v2)
    l.insert(index_value_2, v1)


swap("eggs", "fruits", my_grocery_list)
print(my_grocery_list)
