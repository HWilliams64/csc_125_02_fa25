

text = "something"

with open("example.txt", "a") as file:
    while text:
        text = input("Write: ")
        int(text)
        if text:
            file.write(f"{text}\n")
