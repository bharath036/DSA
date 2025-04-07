''''
In a realm where numbers hold secrets, a captivating challenge awaits, 
which is to, Find all the Prime Numbers less than or equal to a given 
Number !!!

Our Task: Given a number n, print all primes smaller than or equal to n.
It is also given that n is a small number.

'''

def all_Prime(num):
    for i in range(2,num+1):
        #print("i:",i)
        for j in range(2,i):
            #print(j)
            if i%j == 0:
                break 
        else:
            print(i,end=" ") 


num = 10
all_Prime(num)

'''
In Python, the else block after a for loop runs only if the loop completes
normally without encountering a break statement.

for i in range(5):
    print(i)
else:
    print("Loop completed without break.")

Output:
0
1
2
3
4
Loop completed without break.

Ex:2 :-- 
for i in range(5):
    print(i)
    if i == 2:
        print("Breaking the loop.")
        break
else:
    print("Loop completed without break.")

Output:
0
1
2
Breaking the loop.

*******************************************************************
Why It Works:
The else block belongs to the for loop, not the if condition.
It runs only if the for loop completes normally (no break).
This feature is often used for search problems or validations.

'''
'''
def all_Prime(num):
    for i in range(2, num + 1):
        is_prime = True
        for j in range(2, int(i**0.5) + 1):  # Efficient check up to the square root of i
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            print(i)


num = 10
all_Prime(num)

'''
