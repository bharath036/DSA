#count number of digits in a number

def count1(num):
    res = 0
    while num>0:
        num = num//10
        res = res+1
    return res 

num = 343
print(count1(num))

##############################################
def sum_of_n_numbers(n):
    res = n*(n+1)/2
    return int(res)

print(sum_of_n_numbers(4))