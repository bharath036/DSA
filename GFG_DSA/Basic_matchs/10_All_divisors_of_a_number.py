#Given a natural number n, print all distinct divisors of it.

def all_div(num):
    for i in range(1,num+1):
        if num%i == 0:
            print(i,end=' ')
        else:
            continue 

print('The divisors are : ',end = "")
num = 100
all_div(num)

#We can solve this using while loop also while i<=n, every time i will increase by 1


'''
Can we improve the above solution? 
If we look carefully, all the divisors are present in pairs.
For example if n = 100, then the various pairs of divisors are: 
(1,100), (2,50), (4,25), (5,20), (10,10)

Using this fact we could speed up our program significantly. 
We, however, have to be careful if there are two equal divisors as in
the case of (10, 10). In such case, we’d print only one of them.
'''