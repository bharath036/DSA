#Average of list 
'''
lst1 = [1,2,3,4,5,6]
sum_of_list = 0
for i in range(len(lst1)):
    sum_of_list +=  lst1[i]
    
Avg = sum_of_list/len(lst1)
print(Avg)
'''

#Gets even and odd lists from given lists 
'''
even = []
odd = []

list1 = [12,14,79,11,89,98]

for i in list1:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("even_list: ",even)
print('odd_list: ',odd)

'''


#Elements smaller than x
'''
list1 = [1,3,4,6,7,8,9]
x = 6

new_list = []

for i in list1:
    if i<x:
        new_list.append(i)

print(new_list)

'''

#Slicing(List,Tuple,String)
'''
l1 = [10, 20, 30]
l2 = l1[:]
t1 = (10, 20, 30)
t2 = t1[:]          # Tuple having same elements has same id
s1 = "geeks"
s2 = s1[:]          # String of same value has same id
print(l1 is l2)
print(t1 is t2)
print(s1 is s2)
'''

'''
When slicing a list, a new list is created, so l1 and l2 are different objects.
However, slicing a tuple or a string returns the same object since they are immutable.

Everything else is the same in the case of tuples and strings. 
The slicing syntax in the earlier examples is applied similarly to tuples and strings.
'''


#Comprehensions in python 

#LIST comprehension
'''
l = [1, 2, 3, 4, 5]

l1 = [x for x in l if x % 2 == 0]
print(l1)  # Output: [2, 4]

l2 = [x for x in l if x % 2 != 0]
print(l2)  # Output: [1, 3, 5]

l1 = [2,3,4,6,8,0,1,2]
l2 = [x for x in l1 if x%2 == 0]
print(l2)

'''

#Dictionary Comprehension

#Structure : --> output_dict = {key:value for (key, value) in iterable if (key, value satisfy this condition)}

'''
l1 = [1,3,4,2,5]

d1 = {x:x**3 for x in l1}

d2 = {x:f"ID{x}" for x in range(5)} # dictionary comprehension
print(d2)


l2 = [101,103,102]
l3 = ['gfg','ide','corse']

d3 = {l2[i]:l3[i] for i in range(len(l2)) }   # dictionary comprehension

print(d3)


d4 = dict(zip(l2,l3))

print(d4)

'''

#Set comprehensions

'''
l = {10,20,3,4,10,20,7,3}

s1 = {x for x in l if x%2==0 }
s2 = {x for x in l if x%2!=0 }  # set comprehension

print(s1)
print(s2)
'''


#Inverting Dictionary
'''
d1 = {101:'gfg',103:'practise','ide':102}
d2 = {val:key for key,val in d1.items()}
print(d2)

'''

#Generator Comprehensions
'''
input_list = [1,2,3,4,5,6,7,8,8]

output_gen = (var for var in input_list if var%2==0)
print("Output values using generator comprehension",end =" ")
for var in output_gen:
    print(var)

'''

#Largest Element in a List 
'''
def lar_ele(lst):
    lar = 0
    for i in range(len(lst)):
        if lst[i]>lar:
            lar = lst[i]

    return lar 
    
lst = [2,3,5,8,9,6,1]
print(lar_ele(lst))

'''

#Second larget element in a list
'''
def sec_lar(lst):
    sec_lar1 = lst[0]
    fir_lar = lst[0]

    for i in range(len(lst)):
        if lst[i]>fir_lar:
            fir_lar = lst[i]

  

    for i in range(len(lst)):
        if lst[i]<fir_lar:
            if sec_lar1==fir_lar or lst[i] > sec_lar1:
                sec_lar1 = lst[i]

    return sec_lar1 

lst = [2,3,4,5,6,3,5,7,4,6,9,8,8]
print(sec_lar(lst))
'''


#Check if a list is Sorted

def is_sort(lst):
    lst2 = sorted(lst)

    if lst == lst2:
        return True
    else:
        return False
    

lst = [1,2,3,4,5,6,7,8]
print(is_sort(lst))