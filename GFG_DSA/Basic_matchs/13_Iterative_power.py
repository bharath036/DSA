'''
Given an integer x and a positive number y, write a function 
that computes xy under following conditions. 
a) Time complexity of the function should be O(Log y) 
b) Extra Space is O(1) 

Examples: 

Input: x = 3, y = 5
Output: 243

Input: x = 2, y = 5
Output: 32
The recursive solutions are generally not preferred as they 
require space on call stack and they involve function call overhead. 
'''

#Binary Exponentation
# 
'''
Why O(log y)?
Normally, raising x to the power y using a loop takes O(y) time, 
which is inefficient for large y.
Instead, we use Binary Exponentiation, which reduces the problem 
size by half in each step, leading to O(log y) time complexity.

How Does Binary Exponentiation Work?

The key idea is:
Instead of multiplying x y times, break y down into its binary form.
Use right shift (y // 2) and bitwise checks (y % 2) to 
selectively multiply values.

Only multiply res when the current bit in y is 1.

Square x at each step (x = x * x) and halve y (y = y // 2)--> here we
square x because this is how it proceed further 2^0,2^1,2^2, it doubles
2^2 means 4 (2*2)...not like this we are doing x^2(x*x)


Q.)How is This Related to Binary Concepts?
1.)Right Shift (>>)
--Every iteration, y is divided by 2 (y // 2).
--This is the same as right shifting (y >> 1).
2.)Checking the Last Bit (y % 2)
--If y is odd, its last bit is 1, so multiply res = res * x.
here we multiply because we get result here only as loop proceeds
and 1 indicate that 2^n is there.
--If y is even, skip multiplication.
3.)Bit Representation of Exponent (y)
--We process the binary representation of y from least
 significant bit (LSB) to most significant bit (MSB).
 we can also optimze the above solution while n&1: checks boolean
n=n//2 --> n>>1 right shift

Reason for n//2 and x=x*x  --> Try examples and solve it logically to 
get more understanding
Example problems
''' 


"""
Binary Exponentiation: Fast Power Calculation (x^n)
----------------------------------------------------
Instead of multiplying x by itself n times (O(n) time complexity),
we use a faster approach called **Binary Exponentiation**, which works in **O(log n) time**.

Key Concept:
- We repeatedly square the base (`x = x * x`) to jump ahead in powers.
  Example: Instead of calculating 2^8 as 2×2×2×2×2×2×2×2, we do:
  2^2 = 4, 2^4 = 16, 2^8 = 256 (only 3 multiplications instead of 7).

- We divide `n` by 2 (`n = n // 2`) to process each bit of `n`.
  Example: If n = 5 (binary `101`), we process it as:
  5 = 2^2 + 2^0 → Multiply when bit is 1, skip when 0.

- If a bit in `n` is `1`, we multiply `res` by `x`.
  Example: For 3^5 (binary `101`), compute:
  3^1 = 3, 3^4 = 81 → Multiply 3 × 81 = 243.

This method significantly reduces the number of multiplications needed,
making it much faster than the naive approach.
"""

