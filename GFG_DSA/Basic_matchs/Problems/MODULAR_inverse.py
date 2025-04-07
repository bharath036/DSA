'''
Given two integers ‘a’ and ‘m’. The task is to find the smallest
modular multiplicative inverse of ‘a’ under modulo ‘m’. if it does not exist then return -1. 
'''

'''
To find the smallest modular multiplicative inverse of a under modulo m, we need to find an integer x such that:

(
𝑎
×
𝑥
)
m
o
d
 
 
𝑚
=
1
(a×x)modm=1
Conditions for Inverse to Exist
The modular inverse exists if and only if a and m are coprime, meaning:

gcd
⁡
(
𝑎
,
𝑚
)
=
1
gcd(a,m)=1
If gcd(a, m) ≠ 1, return -1 since no modular inverse exists.

Methods to Compute Modular Inverse
Brute Force Method (Slow, O(m) complexity)

Extended Euclidean Algorithm (Efficient, O(log m) complexity)

Fermat's Little Theorem (Only if m is prime)

1️⃣ Brute Force Method
This method checks all values from 1 to m-1 to find x.

Python Code
python
Copy
Edit
def modInverse_brute(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1  # If no inverse exists

# Example
print(modInverse_brute(3, 7))  # Output: 5
🔹 Time Complexity: O(m), not efficient for large m.

2️⃣ Extended Euclidean Algorithm
This method efficiently finds x using Extended Euclidean Algorithm, which also finds the solution to:

𝑎
𝑥
+
𝑚
𝑦
=
1
ax+my=1
Python Code
python
Copy
Edit
def gcd_extended(a, b):
    if b == 0:
        return a, 1, 0  # Base case: gcd(a, 0) = a
    gcd, x1, y1 = gcd_extended(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def modInverse_eea(a, m):
    gcd, x, _ = gcd_extended(a, m)
    if gcd != 1:
        return -1  # No modular inverse exists
    return x % m  # Ensure x is positive

# Example
print(modInverse_eea(3, 7))  # Output: 5
print(modInverse_eea(10, 17))  # Output: 12
print(modInverse_eea(15, 30))  # Output: -1 (since gcd(15,30) ≠ 1)
🔹 Time Complexity: O(log m), much faster than brute force.

3️⃣ Fermat’s Little Theorem (When m is Prime)
Fermat’s theorem states:

𝑎
𝑚
−
1
≡
1
m
o
d
 
 
𝑚
a 
m−1
 ≡1modm
which means:

𝑎
𝑚
−
2
≡
𝑎
−
1
m
o
d
 
 
𝑚
a 
m−2
 ≡a 
−1
 modm
Thus, the modular inverse is:

𝑎
𝑚
−
2
m
o
d
 
 
𝑚
a 
m−2
 modm
Python Code
python
Copy
Edit
def power_mod(a, b, m):
    result = 1
    a = a % m
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % m
        a = (a * a) % m
        b //= 2
    return result

def modInverse_fermat(a, m):
    if gcd_extended(a, m)[0] != 1:
        return -1  # No modular inverse exists
    return power_mod(a, m-2, m)

# Example (works only when m is prime)
print(modInverse_fermat(3, 7))  # Output: 5
print(modInverse_fermat(10, 17))  # Output: 12
🔹 Time Complexity: O(log m), same as Extended Euclidean Algorithm.
🔹 Note: This only works when m is prime.

Final Thoughts
Method	Time Complexity	Best Use Case
Brute Force	O(m)	Small values of m
Extended Euclidean Algorithm	O(log m)	Works for all cases
Fermat’s Theorem	O(log m)	Only when m is prime
📌 Recommended Approach: Use the Extended Euclidean Algorithm since it works for all values of m efficiently. 🚀
'''