my_text_file = open("example.txt", "r")

text = my_text_file.read()
print("1st Read:", text)
my_text_file.seek(10)
text = my_text_file.read()
print("2nd Read:", text)
