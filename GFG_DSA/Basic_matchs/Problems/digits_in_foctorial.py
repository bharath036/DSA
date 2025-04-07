import math 
#My solution is correct but time complexity is N*logN which is 
# more to reduce we use different approach using math module to reduce it to O(N)
def factorial(N):
    fact = 1
    while N>0:
        fact = fact*N
        N= N-1
    return fact
        
def digitsInFactorial(N):
        # code here
    res = factorial(N)
    count = 0
    while res>0:
        res = res // 10
        count +=1
    return count

def digitsInFactorial(N):
    if N==0 or N==1:
        return 1 
    logsum = sum(math.log10(i) for i in range(1,N+1))
    return math.floor(logsum)+1

N= 5 
print(digitsInFactorial(5))
