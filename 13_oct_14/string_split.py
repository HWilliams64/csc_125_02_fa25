my_str = "a,b,c,d"
my_list = ["a", "b", "c", "d"]
my_str_as_list = my_str.split(",")
print(f"my_str={my_str}")
print(f"my_list={my_list}")
print(f"my_str_as_list={my_str_as_list}")
print(my_list == my_str_as_list)
