import os

# Absolute Path: /home/developer/Documents/code/csc_125_02_fa25/19_nov_6/example.txt
# Relative Path: example.txt
while True:
    file_name = input("File name: ")
    os.system("clear")
    root_dir: str = os.path.dirname(__file__)
    example_file_path = os.path.join(root_dir, file_name)
    abs_example_file_path = os.path.abspath(example_file_path)

    if not abs_example_file_path.startswith(root_dir):
        print(f"You can only read files in {root_dir}")

    elif os.path.isfile(example_file_path):
        print(example_file_path)
        # 1) open the file to be read
        my_text_file = open(example_file_path, "r")

        # read from the file
        text = my_text_file.read()

        # print out the text
        print(" FILE TEXT ".center(40, "="))
        print(text)
        print("="*40)
    else:
        print(f"{example_file_path} is not a file.")