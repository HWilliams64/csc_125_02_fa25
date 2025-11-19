import json


my_dictionary = {
    "first_name": "tony",
    "last_name": "stark",
    "age": 48,
    "city": "new york",
    "email": "ironman@starkindustries.com",
    "is_hero": True,
}

# json.dumps - convert Python object to JSON string
json_str = json.dumps(my_dictionary)

print("Py Version".center(80, "="))
print(my_dictionary)
print("Json Version".center(80, "="))
print(json_str)

with open("data.json", "w") as json_file:
    # json.dump - write Python object as JSON to a file
    # NOTE: no 's' at the end of dump
    json.dump(my_dictionary, json_file)

with open("data.json", "r") as json_file:
    data = json_file.read()
    # json.loads - convert JSON string to Python object
    my_new_dictionary = json.loads(data)

    json_file.seek(0)  # Move the file pointer back to the beginning

    # OR use json.load to read JSON from a file directly
    # NOTE: no 's' at the end of load
    my_new_dictionary = json.load(json_file)

print("New Py Version".center(80, "="))
print(my_new_dictionary)

print("Are they equal?".center(80, "="))
print(my_dictionary == my_new_dictionary)
