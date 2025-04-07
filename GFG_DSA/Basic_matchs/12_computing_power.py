#The task is to compute Power(x,n)  which means x to the power y.
'''
def pow(x,y):
    res = x**y
    print(res)

x = 7
y = 3
print(pow(x,y))

'''

#A simple solution to calculate pow(x, n) would multiply x exactly 
# n times. We can do that by using a simple for loop
#O(N),O(1)
#suppose 7 power 0 = 1 ., if we give 0.., then it wont enter into loop and
# returns 1 because 0 is the end point max in range as defined  
def pow(x,y):
    pow1 = 1

    for _ in range(y):
        pow1 = pow1*x 
    return pow1
    
x = 7 
y = 0
print(pow(x,y))


#Efficient approach 
'''
An optimized Divide and Conquer Solution: 
The problem can be recursively defined by:

power(x, n) = power(x, n / 2) * power(x, n / 2);  // if n is even

power(x, n) = x * power(x, n / 2) * power(x, n / 2);  // if n is odd
'''

