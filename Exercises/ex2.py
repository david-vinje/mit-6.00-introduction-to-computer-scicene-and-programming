# Problem 1
# Show that it is possible to buy exactly 50, 51, 52, 53, 54, and 55 McNuggets,
# by finding solutions to the Diophantine equation.
# list the combinations of 6, 9 and 20 packs of McNuggets 
# you need to buy in order to get each of the exact amounts.
def diaphantine(a, b, c, x, y, z):
    return x*a + y*b + z*c

def nuggets(n, x=6, y=9, z=20):
    for a in range(0, n):
        sum = diaphantine(a, 0, 0, x, y, z)
        if (sum == n):
            return a, 0, 0
        if (sum > n):
            break
        for b in range(0, n):
            sum = diaphantine(a, b, 0, x, y, z)
            if (sum == n):
                return a, b, 0
            if (sum > n):
                break
            for c in range(0, n):
                sum = diaphantine(a, b, c, x, y, z)
                if (sum == n):
                    return a, b, c
                if (sum > n):
                    break
    return 0

for n in range(50,56):
    abc = nuggets(n)
    if abc == 0:
        print(f"{n} nuggets are not possible")
    else:
        print(f"6*{abc[0]} + 9*{abc[1]} + 20*{abc[2]} = {diaphantine(abc[0], abc[1], abc[2], 6, 9, 20)}")

# Problem 2
# Given that it is possible to buy sets of 50, 51, 52, 53, 54 or 55
# McNuggets by combinations of 6, 9 and 20 packs, 
# show that it is possible to buy 56, 57,..., 65 McNuggets. 
# Explain, in English, why this theorem is true.
# Solution: 56=50+6, 57=51+6, ...,  61=55+6, 62=53+9, ..., 65=56+9, 

# Problem 3
# Write an iterative program that finds the largest number
# of McNuggets that *cannot* be bought in exact quantity
n = 50
while (nuggets(n) != 0):
    n = n-1
print("Largest number of McNuggets that cannot be bought in exact quantity:", n)

# Problem 4
# Assume that the variable packages is bound to a tuple of length 3,
# the values of which specify the sizes of the packages, ordered from smallest to largest.
# Write a program that uses exhaustive search to find the largest number (less than 200)
# of McNuggets that cannot be bought in exact quantity
def packages(x, y, z):
    n = 199
    while (nuggets(n, x, y, z) != 0):
        n = n-1
    print(f"Given package sizes {x}, {y}, and {z}, "+
    f"the largest number of McNuggets that cannot be bought in exact quantity is: {n}")

import random
for i in range(1, 10):
    a = random.randrange(2, 10)
    b = random.randrange(a+1, a+10)
    c = random.randrange(b+1, b+10)
    packages(a, b, c)
packages(6, 9, 20)        