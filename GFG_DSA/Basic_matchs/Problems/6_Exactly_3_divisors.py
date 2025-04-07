'''
Given a positive integer value n. The task is to find 
how many numbers less than or equal to n have numbers of divisors 
exactly equal to 3.
'''

'''
def exactly_3_divisors(n):
   
    count1 = 0
    for i in range(1,n+1):
        count = 0
        for j in range(1,i+1):
            if i%j == 0:
                count+=1
            else: 
                continue 
        if count == 3:
            count1+=1
            print("count1:",count1)
            print("i:",i) 
    
    return count1 


a = exactly_3_divisors(10)
print(a)
'''

#The above approach is more time taking O(N^2).
#Use logic as square of prime numbers has 3 divisors exactly
'''
import math

class Solution:
    def exactly3Divisors(self, N):
        def sieve(limit):
            is_prime = [True] * (limit + 1)
            is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
            
            for i in range(2, int(math.sqrt(limit)) + 1):
                if is_prime[i]:
                    for j in range(i * i, limit + 1, i):
                        is_prime[j] = False
            
            return [x for x in range(limit + 1) if is_prime[x]]
        
        # Find primes up to sqrt(N)
        primes = sieve(int(math.sqrt(N)))
        
        # Count squares of primes within N
        count = 0
        for prime in primes:
            if prime * prime <= N:
                count += 1
            else:
                break
        
        return count

# Example test
sol = Solution()
print(sol.exactly3Divisors(10))  # Output: 2 (4 and 9)
print(sol.exactly3Divisors(30))  # Output: 3 (4, 9, 25)
'''
'''
"""
# Understanding the Problem:

1. We need to find numbers ≤ N that have exactly **three divisors**.
2. Key Observation:
   - A number has exactly **3 divisors** if and only if it is the **square of a prime**.

# Why?
- A **prime number** (p) has only 2 divisors: (1, p).
- If we square it (p²), it gets exactly **3 divisors**: (1, p, p²).
  Example:
    - 4 (2²) → Divisors: [1, 2, 4] ✅ (Exactly 3)
    - 9 (3²) → Divisors: [1, 3, 9] ✅ (Exactly 3)
    - 25 (5²) → Divisors: [1, 5, 25] ✅ (Exactly 3)
    - 8 (2³) → Divisors: [1, 2, 4, 8] ❌ (More than 3)

# Optimized Approach:
1. **Find all prime numbers up to √N.**
   - We only need primes up to √N because their squares will be ≤ N.
   - Use the **Sieve of Eratosthenes** (Fast way to find primes).

2. **Count squares of those prime numbers ≤ N.**
   - If p is prime, check if p² ≤ N.
   - If true, increase the count.

# Time Complexity:
- **Sieve of Eratosthenes**: O(√N log log √N) [Very Efficient for small N]
- **Checking squares of primes**: O(√N)
- Overall: **O(√N log √N)**
"""

import math

class Solution:
    def exactly3Divisors(self, N):
        """
        Step 1: Use Sieve of Eratosthenes to find prime numbers up to sqrt(N)
        Step 2: Count how many squares of primes are ≤ N
        """
        
        def sieve(limit):
            """ Returns a list of prime numbers up to 'limit' using Sieve of Eratosthenes """
            is_prime = [True] * (limit + 1)  # Assume all numbers are prime initially
            is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
            
            # Mark multiples of each prime as False
            for i in range(2, int(math.sqrt(limit)) + 1):
                if is_prime[i]:  # If 'i' is prime, mark its multiples as non-prime
                    for j in range(i * i, limit + 1, i):
                        is_prime[j] = False
            
            # Collect all prime numbers
            return [x for x in range(limit + 1) if is_prime[x]]
        
        # Step 1: Find primes up to sqrt(N)
        primes = sieve(int(math.sqrt(N)))

        # Step 2: Count prime squares within N
        count = 0
        for prime in primes:
            if prime * prime <= N:  # Check if p² is within range
                count += 1
            else:
                break  # No need to check further if p² > N
        
        return count

# Example test cases:
sol = Solution()
print(sol.exactly3Divisors(10))  # Expected Output: 2 (Numbers: 4, 9)
print(sol.exactly3Divisors(30))  # Expected Output: 3 (Numbers: 4, 9, 25)
print(sol.exactly3Divisors(100)) # Expected Output: 4 (Numbers: 4, 9, 25, 49)

How to Think Like This?
If you're solving such a problem for the first time, follow these steps:

1️⃣ Brute Force First:

Try checking divisors for all numbers ≤ N (O(N²) approach).

Realize that it's too slow.

2️⃣ Look for a Pattern:

Think about what kind of numbers have exactly 3 divisors.

You’ll notice they are squares of prime numbers.

3️⃣ Optimize Step-by-Step:

Instead of checking divisors for every number, focus only on prime numbers.

Find primes efficiently using Sieve of Eratosthenes (which is very fast).

Only check their squares (reduces computation significantly).
'''

#Lets use other method and solve this problem 
#Time complexity of this is O(sqrt(N))
'''
def is_prime(N):
    if N == 1 :
        return False 
    if N== 2 or N==3:
        return True  
    if N%2 == 0 or N%3 ==0:
        return False 
    i=5 
    while i*i <= N:
        if N%i == 0 or N%(i+2) == 0:
            return False 
        i += 6 
    return True 

#print(is_prime(20))

def prime(N):
    primes = []
    for num in range(2,N+1):
        if is_prime(num):
            primes.append(num)
    return primes

#prime(28)
#print(prime(20))

def Exactly_3_divisors(N):
    b = []
    a = prime(N)
    count = 0
    for i in a:
        b.append(i*i)
    
    for i in b:
        if i <=N:
            count += 1

    return count
    
#Exactly_3_divisors(3)
print(Exactly_3_divisors(20))

'''

'''
#User function Template for python3
import math 
class Solution:
    def exactly3Divisors(self,N):
        # code here
        i = 2
        count = 0
        while i*i <= N:
            if self.isPrime(i):
                count+=1
            i+=1
            
        return count
        
    def isPrime(self, n):
        if n <= 1:
            return False
        if n == 2 or n == 3:
            return True
        
        if n%2 == 0 or n%3 == 0:
            return False
        
        i = 5
        while i <= math.sqrt(n):
            if n%i == 0 or n%(i+2) == 0:
                return False
            i+=6
        return True
        
'''


#User function Template for python3
import math 
class Solution:
    def exactly3Divisors(self,N):
        # code here
        def isPrime(n):
            if n < 2:
                return False
            for i in range(2,int(math.sqrt(n))+1):
                if n % i == 0:
                    return False
            return True
                
        count = 0
        for i in range(2,int(math.sqrt(N))+1):
            if isPrime(i):
                if i * i <= N:
                    count += 1
        return count