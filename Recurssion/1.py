#print 1 to N
'''
def print_1_N(num):
    if num==0:
        return 1
    print_1_N(num-1)
    print(num)

print_1_N(3)

'''

'''
#print N to 1 (Reverse order)
def N_to_1(num):
    if num==0:
        return 
    print(num)
    N_to_1(num-1)

N_to_1(3)
'''

#print Array elements using recurssion
'''
def printArrayRecur(arr,n):
    if n==0:
        return
    printArrayRecur(arr,n-1)
    print(arr[n-1]) 

arr = [1,2,3,4,5,6]
n=6
printArrayRecur(arr,n)

'''

#check palidrome
'''
class Solution:
    def isPalin(self, n):
        # Store original number to compare later
        self.original = n
        
        # Recursive function to reverse digits
        def reverse(num):
            if num == 0:
                return 0
            digits = int(len(str(num)))  # count digits
            return (num % 10) * (10 ** (digits - 1)) + reverse(num // 10)

        reversed_n = reverse(n)
        return reversed_n == self.original

sol = Solution()
print(sol.isPalin(101)) 


'''

'''
# ----------------------------------------------
# Problem: Check if a number is a Palindrome (Recursively)
# ----------------------------------------------
# A number is called a palindrome if it reads the same backward as forward.
# For example:
#     121 -> palindrome (same when reversed)
#     123 -> not a palindrome
#
# Goal:
#     Given a number N, check whether it is a palindrome or not using recursion.

# ----------------------------------------------
# ✅ Recursive Solution in Python
# ----------------------------------------------

class Solution:
    def isPalin(self, N):
        # Helper recursive function to reverse the number
        def reverse(n, rev):
            # Base case: when the number becomes 0, return the reversed number
            if n == 0:
                return rev
            
            # Recursively call reverse with updated number and reversed value
            return reverse(n // 10, rev * 10 + n % 10)

        # Call the helper function with initial rev = 0
        reversed_n = reverse(N, 0)

        # Compare reversed number with original
        return reversed_n == N


# ----------------------------------------------
# 🔍 Step-by-step Example:
# Input: N = 101
#
# reverse(101, 0)
#   -> reverse(10, 1)       [1 is last digit]
#       -> reverse(1, 10)   [0 is last digit]
#           -> reverse(0, 101)  [1 is last digit]
# => reversed_n = 101
# => reversed_n == N, so it's a palindrome
#
# Output: True (or 1 in GFG-style)

# ----------------------------------------------
# 📌 Time and Space Complexity:
#
# Time Complexity:     O(log₁₀N) 
#     - Because we divide the number by 10 in each step, the number of digits is log₁₀(N)
#
# Auxiliary Space:     O(log₁₀N) 
#     - Due to recursive function call stack (each digit leads to one call)

# ----------------------------------------------
# ⚠️ Common Mistakes:
# 1. Writing 'return x = y' — this is invalid syntax in Python.
# 2. Trying to reverse using power of 10 may lead to incorrect digit positioning.
# 3. Not handling base case `if n == 0` properly in recursion.

# ----------------------------------------------
# ✅ How to Run in VS Code:
#
# 1. Open VS Code
# 2. Save this code as `check_palindrome_recursive.py`
# 3. Add test cases at bottom (example shown below)
# 4. Run with: `python check_palindrome_recursive.py` in terminal

# ----------------------------------------------
# 🧪 Sample Test Case

if __name__ == "__main__":
    sol = Solution()
    n = 121
    print("Is Palindrome:" , sol.isPalin(n))  # Output: True

    n = 123
    print("Is Palindrome:" , sol.isPalin(n))  # Output: False

'''

#GCD 

# ----------------------------------------------
# Problem: Find the GCD of two numbers using recursion
# ----------------------------------------------

# GCD (Greatest Common Divisor) of two numbers a and b is the largest number 
# that divides both a and b completely (without leaving a remainder).
#
# Example:
#   GCD(8, 12) = 4
#   GCD(7, 8)  = 1
#   GCD(2, 4)  = 2

# ----------------------------------------------
# ✅ Euclid's Algorithm (Recursive)
# ----------------------------------------------

# Formula:
#     GCD(a, b) = GCD(b, a % b)
#     Base case: if b == 0 => return a

# ----------------------------------------------
# Python Recursive Code:

class Solution:
    def GCD(self, a, b):
        # Base case: if one number becomes 0, return the other
        if b == 0:
            return a
        # Recursive call
        return self.GCD(b, a % b)


# ----------------------------------------------
# 🧪 Test Examples:

if __name__ == "__main__":
    sol = Solution()
    
    print("GCD of 7 and 8:", sol.GCD(7, 8))   # Output: 1
    print("GCD of 2 and 4:", sol.GCD(2, 4))   # Output: 2
    print("GCD of 8 and 12:", sol.GCD(8, 12)) # Output: 4
    print("GCD of 100 and 10:", sol.GCD(100, 10)) # Output: 10

# ----------------------------------------------
# 💡 Explanation of how recursion works:
#
# Example: GCD(8, 12)
#    -> GCD(12, 8)
#    -> GCD(8, 4)
#    -> GCD(4, 0)
#    => Return 4
#
# Each step keeps reducing the problem size until one becomes 0.

# ----------------------------------------------
# 🧠 Time and Space Complexity:
#
# Time Complexity: O(log(min(a, b)))
#     - Because we are dividing the number in every recursive step
#
# Auxiliary Space: O(log(min(a, b)))
#     - Due to recursive call stack

# ----------------------------------------------
# ✅ How to Run in VS Code:
#
# 1. Open VS Code.
# 2. Save this as `gcd_recursive.py`.
# 3. Run using `python gcd_recursive.py` from terminal.

