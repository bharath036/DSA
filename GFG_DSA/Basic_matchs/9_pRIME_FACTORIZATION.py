'''
Prime factorization is finding which prime numbers multiply
together to create the original number. This article'll discuss 
performing prime factorization in Python using a straightforward, 
beginner-friendly approach. We'll also provide a detailed explanation 
of the code and how it works.

What is Prime Factorization?
Prime factorization involves breaking down a number into its prime
number components. For example, the prime factors of 100 are 2 and 5. 
Here's how you get there:

Divide 100 by 2 (the smallest prime number) to get 50.
Divide 50 by 2 to get 25 (2 occurrences of 2).
Divide 25 by 5 to get 5.
Divide 5 by 5 to get 1 (2 occurrences of 5).
So, the prime factorization of 100 is 2^2×5^2.
'''
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_factors(n):
    for i in range(2, n + 1):
        if is_prime(i):
            while n % i == 0:
                print(i, end=' ')
                n = n// i
                print(n)

number = 100
print("Prime factors of", number, "are:", end=' ')
prime_factors(number)
