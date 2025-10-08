# Tuple

from typing import Tuple


my_grocery_list = ["milk", "cheese", "meat", "ice cream", "milk"]
my_grocery_list.append("grape")

def index(search, ds: Tuple):
    index = 0
    for value in ds:
        if value == search:
            return index
        index += 1

    return None


def count(search, ds: Tuple):
    count = 0
    for value in ds:
        if value == search:
            count += 1

    return count


while True:
    search = input("> ")
    # Count the number of occurrences of a value
    search_count = count(search,my_grocery_list)
    print(f"{search} was found {search_count} times")
    
    # If the number is anything other than zero then its considered true
    if search in my_grocery_list:
        # Where an item is located
        search_index = index(search, my_grocery_list)
        print(f"{search} was found at index {search_index}")
    else:
        print(f"{search} has no index")
