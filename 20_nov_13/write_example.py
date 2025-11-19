file = open("example.txt", "a")
text = "something"

while text:
    text = input("Write: ")
    if text:
        file.write(f"{text}\n")
        file.flush()

file.close()
