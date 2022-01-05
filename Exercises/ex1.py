from math import *

# Problem 1.
# Write a program that computes and prints the 1000th prime number.
def is_prime(num):
    for i in range(3, int(sqrt(num))+1, 2):
        if (num % i == 0):
            return False
    return True
count = 1
prime = 3
while (count < 1000):
    if (is_prime(prime)):
        count += 1
    prime += 2
print(prime-2)

# Problem 2.
# Write a program that computes the sum of the logarithms of all the primes
# from 2 to some number n, and print out the sum of the logs of the primes, the number n,
# and the ratio of these two quantities. Test this for different values of n.
def logarithmic_prime_sum(n):
    sum1 = log(2)
    sum2 = 2
    for i in range(3, int(sqrt(n))+1, 2):
        if (n % i == 0):
            sum1 += log(i)
            sum2 += i
    print("The sum of logarithmic primes: ", sum1)
    print("The logarithm of prime summation: ", log(sum2))
n = int(input("n: "))
logarithmic_prime_sum(n)
