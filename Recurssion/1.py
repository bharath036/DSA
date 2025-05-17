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

def printArrayRecur(arr,n):
    if n==0:
        return
    printArrayRecur(arr,n-1)
    print(arr[n-1]) 

arr = [1,2,3,4,5,6]
n=6
printArrayRecur(arr,n)