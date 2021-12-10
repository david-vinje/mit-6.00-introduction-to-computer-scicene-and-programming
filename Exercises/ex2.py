def perfect_sqrt(x):
    if x < 0:
        print("Invalid input, is negative")
        return
    i = 0
    while (i*i < x):
        i += 1
    if i*i > x:
        print("Invalid input, is not a perfect square")
    else:
        print("The square root of", x, "is", i)
perfect_sqrt(25)

def approx_sqrt(x):
    i = 0
    while (x-i*i > 0.001):
        i += 0.001
    print("The approx. square root of", x, "is", i)
approx_sqrt(10)


