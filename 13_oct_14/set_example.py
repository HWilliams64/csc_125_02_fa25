my_set:set[str] = set()

while True:
    print("Type operation")
    op = input(">")
    if op in ("add", "discard", "pop", "intersection", "difference"):
        # How to add elements
        if op == "add":
            print("Type element to add")
            user_input = input(">")
            my_set.add(user_input)
        # How to remove elements
        elif op == "pop":
            my_set.pop()
        elif op == "discard":
            print("Type element to remove")
            user_input = input(">")
            my_set.discard(user_input)
        # Observability
        elif op == "intersection":
            print("Type a list of elements separated by comma")
            user_input = input(">")
            list_of_elements = user_input.split(",")
            print(f"Intersection: {my_set.intersection(list_of_elements)}")
        elif op == "difference":
            print("Type a list of elements separated by comma")
            user_input = input(">")
            list_of_elements = user_input.split(",")
            print(f"difference: {my_set.difference(list_of_elements)}")
        # elif op == "difference":
        #     print("Type a list of elements separated by comma")
        #     user_input = input(">")
        #     list_of_elements = user_input.split(",")
        #     print(f"Intersection: {my_set.difference(list_of_elements)}")
            

    print(f"My set: {my_set}")
