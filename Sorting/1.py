#Using sorted 
'''
From below observations we can say that sorted function will created new variable to store sorted list
means in new object
'''
'''
lst1 = [2,4,8,6,4,9,1]
print(id(lst1))
#add= hex(id(lst1)) 
add = id(lst1)
print(add)
print(sorted(lst1))
#print(hex(id(sorted(lst1))))
print(id(sorted(lst1)))
'''

#Sort 
'''
sort function will create in place variable where the values will be stored in same variable 
'''
'''
lst1 = [1,3,2,4,6,8,6,9,2,1]
lst1.sort()
print(lst1)

'''

#Bubble sort
'''
In bubble sort in each pass it compares with adjacent elements and sorted
TC is O(N^2)
SC is O(1)
'''

'''
def bubble_sort(lst):
    n = len(lst)
    for i in range(n-1):
        for j in range(n-i-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
    
    return lst
    
lst = [2,1,3,6,4,8,9,7,4]
print(bubble_sort(lst))

'''

#SELECTION SORT
'''
In every pass it finds the minimun elements avoids many swaps
'''
'''
def selection_sort(lst):
    n= len(lst)
    for i in range(n-1):
        min_ele = i 
        for j in range(i+1,n):
            if lst[j] < lst[min_ele]:
                min_ele = j
        lst[min_ele], lst[i] = lst[i],lst[min_ele]
        
    return lst 

lst = [2,1,3,6,4,8,6,9,1]
print(selection_sort(lst))
'''


#Optimizied Bubble sort
'''
We use flagging condition here
'''

'''
def bubbleSort(l):
    n = len(l)

    for i in range(n-1):
        swapped = False

        for j in range(n-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]

                swapped = True

        if swapped == False:
            return

l = [10, 8, 20, 5]

bubbleSort(l)

print(*l)

'''