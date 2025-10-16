# You have 2 lists, return a single list of the the elements that are found in
# the 2 lists you were given. Given list A and B make a list C with only the
# elements found in list A and B.
# A = [1, 2, 3, 4, 5]
# B = [3, 4, 5, 6, 7]
# C = [3, 4, 5]

A = [1, 2, 3, 4, 5]
B = [3, 4, 5, 6, 7]
C: list[int] = []

# look at every element in list A
for a_item in A:
    # Compare each element in list A to  every element in list B
    for b_item in B:
        # If element from list A equals element for list B 
        if a_item == b_item:
            # Add the element to list C
            C.append(a_item)

print(f"Result: {C}")

# Convert the sequence to a set
set_a = set(A)
# we use the intersection() to find the overlapping values between set A and
# list B
set_c = set_a.intersection(B)
# Convert set C into a list
C = list(set_c)

print(f"Result: {C}")
