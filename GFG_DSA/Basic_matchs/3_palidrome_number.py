#palidrome number or not
#if we reverse a numbe it is same or not

def palidrome(num):
    rev = 0
    temp = num 
    while temp!=0:
        rem = temp%10
        rev = rev*10+ rem
        temp = temp//10
    
    if (rev==num):
        return True
    else:
        return False

num = 343
print(palidrome(num))

#here we are reversing the number and comparing to check whether it is 
#palidrome or not

#Factorial of a number

def fact(n):
    res = 1
    while n>0:
        res=res*n 
        n = n-1 

    return res 

print(fact(4))