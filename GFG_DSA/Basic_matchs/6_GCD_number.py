#GCD (Greatest Common Divisor) or HCF (Highest Common Factor) of two 
# numbers is the largest number that divides both of them. 
'''
EX: 36&60 
36 --> 2*2*3*3
60 --> 2*2*3*5

gcd = 2*2*3 =12
'''
#Using naive approch. iterate through it till min number and update gcd if the 
#condition satisfies
def gcd(a,b):
    gcd  = 1
    for i in range(1,min(a,b)+1):
        if a%i == 0 and b%i ==0:
            gcd = i 

    return gcd 

a = 36
b =60 
print(gcd(a,b))

#The above solution is insuffient for larger problems

#Eucidian Algorithm 
#If we take two numbers a &b. lets assume a is greater than b
# we will proceed when b!=0 
#then swap and calculate remainder
#and finally we return a 

def gcd_Eucidian(a,b):
    
    while b!=0:
        a,b = b, a%b 
    return a 

a = 36
b = 60 
print(gcd(a,b))
print(print())

'''
### 📝 **Euclidean Principle for GCD (Greatest Common Divisor)**

**Definition:**
The Euclidean algorithm finds the GCD of two numbers using division and remainders.

**Key Rule:**
👉 *GCD(a, b) = GCD(b, a % b)*  
👉 Repeat until remainder becomes **0**. The last non-zero remainder is the GCD.

**Steps:**
1. Take two numbers `a` and `b`.
2. Divide `a` by `b` and find the remainder `r` → `r = a % b`.
3. Replace `a` with `b` and `b` with `r`.
4. Repeat until `b = 0`.
5. The final value of `a` is the GCD.

**Example (56, 98):**
```
98 % 56 = 42
56 % 42 = 14
42 % 14 = 0
```
GCD = **14** (last non-zero remainder)

**Python Code:**
```python
# Euclidean Algorithm for GCD
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(gcd(56, 98))  # Output: 14
```

**Why It Works:**
The remainder reduces the problem size, ensuring logarithmic time complexity.

**Time Complexity:** `O(log(min(a, b)))`  
**Space Complexity:** `O(1)`

💡 *Remember: Keep dividing until remainder is 0!* 🚀


'''