from itertools import permutations

def print_permutations(s):
    for perm in permutations(s):
        print("".join(perm))

#Example
print_permutations("abc")