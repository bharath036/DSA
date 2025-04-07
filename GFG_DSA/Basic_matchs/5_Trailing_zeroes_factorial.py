'''
Our Task: We are given a number. The task is to find the Number of 
Trailing Zeros in the factorial of the number.

The Trailing Zeros are the Zeros, which appear at the end of a 
number(factorial in that case)
'''

def trailing_zeroes(num):
    fact = 1
    for i in range(2,num+1):
        fact = fact*i 
    
    count = 0
    while fact>0:
        if fact%10 == 0:
            count = count+1
            fact=fact//10
        else:
            break
    return count 



num = 5
print(trailing_zeroes(num))

#The above method will cause overflow for slightly bigger numbers as the factorial
#of a number is a big number

#Effective approach

'''
# 🧮 How to count trailing zeros efficiently?

# For every multiple of 5, there’s at least one factor of 5.
# Example:

# Numbers like 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, etc., all contribute a 5.
# Multiples of 25 contribute an extra 5 because 25 = 5 × 5.
# Multiples of 125 contribute yet another 5.

# 📝 Formula:
# Trailing Zeros = ⌊ n/5 ⌋ + ⌊ n/25 ⌋ + ⌊ n/125 ⌋ + …

# 📖 Example Walkthrough: n = 100
# How many multiples of 5?
# ⌊100/5⌋ = 20

# How many multiples of 25?
# ⌊100/25⌋ = 4

# How many multiples of 125?
# ⌊100/125⌋ = 0

# Add them up:
# 20 + 4 + 0 = 24

# So, 100! has 24 trailing zeros.

# 🖨️ Code Implementation:
def find_trailing_zeros(n):
    count = 0
    i = 5
    while n // i >= 1:
        count += n // i
        i *= 5
    return count

# 🎬 Example Run:
n = 100
print(f"Count of trailing zeros in {n}! is {find_trailing_zeros(n)}")

# 🕰️ Output:
# Count of trailing zeros in 100! is 24

'''

def find_trailing_zeros(n):
    count = 0
    i = 5
    while n // i >= 1:
        count += n // i
        i *= 5
    return count

n = 100
print(find_trailing_zeros(n))