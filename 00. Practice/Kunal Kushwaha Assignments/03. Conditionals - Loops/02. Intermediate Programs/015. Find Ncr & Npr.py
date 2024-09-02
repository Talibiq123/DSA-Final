import math


def combinations(n, r):
    return math.comb(n, r)


def permutations(n, r):
    return math.perm(n, r)


n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))

print(f"The number of combinations (nCr) is: {combinations(n, r)}")
print(f"The number of permutations (nPr) is: {permutations(n, r)}")
