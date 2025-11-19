import json


user_input = input("Enter a JSON string: ")
py_dictionary = json.loads(user_input)
print("Python Dictionary:".center(80, "="))
print(py_dictionary)
