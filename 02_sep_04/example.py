from shlex import join
import textwrap

# This is a number
number = 673634784949320304984732556

# This is a string
apple = "Hello how are you"
my_string = 'the person said \n\t"I said \'hello\'"'

lines = textwrap.wrap("I was walking down the street and I fell into a hole and as I fell I wrote a python game becase I had nothing else to do...", width=20)
para = "\n".join(lines)
print(para)
