a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

print(f"intersection: {a.intersection(b)}") # what is found in both sets?
print(f"difference: {a.difference(b)}") # what is found in a not found in b?
print(f"isdisjoint: {a.isdisjoint(b)}") # do they not have any overlapping values?
print(f"issubset: {a.issubset(b)}")
print(f"issuperset: {a.issuperset(b)}")
print(f"symmetric_difference: {a.symmetric_difference(b)}")
