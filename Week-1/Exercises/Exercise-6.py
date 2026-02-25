"""
Write a script that lists all the prime numbers between 1 and 10000.
(A prime number is an integer greater or equal to 2 which has no divisors except 1 and itself). 
Hint: Write an is_factor helper function.
"""
import math

def is_factor(d, n):
        if d !=0 and n % d == 0:
            return True
        else:
            return False

def is_prime(n):
    d = []
    for i in range (int(math.sqrt(n))+1):
        if is_factor(i, n):
            if i != n and i != 1:
                return False
            else:
                d.append(i)
    if len(d) == 1:
         return n

def main():
    list_of_primes = []
    for i in range(10001):
        if is_prime(i):
            list_of_primes.append(is_prime(i)) 
    print(list_of_primes)

main()

