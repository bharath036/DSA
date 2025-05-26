'''
def bin_search(arr,x):
    arr.sort()
    print("sorted array: ",arr)
    l = 0
    r = len(arr) - 1
    while l<=r:
        mid = l+ (r-l)//2 
        if arr[mid] == x:
            return mid
        
        elif arr[mid] < x:
            l = mid+1 
        else:
            r = mid-1 

    return -1 

arr = [1,2,4,34,78,90,12,11]
print(bin_search(arr,11))
'''

#Index of first Occurance and Last Occurance in a sorted array
#value of x is given , we need to find the duplicates of x first occurance and last occurance index in a sorted array 
'''
def firstAndLast(arr,n,x):
    first = -1
    last = -1
    for i in range(0,n):
        if x!=arr[i]:
            continue 
        if first==-1:
            first = i 
        last=i 

    if first!= -1 :
        print(first,last)
    else:
        print("Not found")

arr = [1,2,2,2,2,2,2,3,4,8,8]
n=len(arr)
x =2
firstAndLast(arr,n,x)

'''
'''
def bin_search(arr,key):
    l = 0 
    r = len(arr)-1 

    while l<=r:
        mid = l + (r-l)//2
        if arr[mid] == key:
            return mid 
        elif arr[mid] > key :
            r = mid -1 
        else :
            l = mid + 1 
    return -1 

arr = [1,2,3,4,4,8]
print(bin_search(arr,8))
'''

#first occurance and last occurance 

# First occurrence and last occurrence in a sorted array
'''
def findFirstAndLast(arr, n, x):
    first = -1   # Default value if x not found
    last = -1

    for i in range(0, n):       # Traverse the array
        if (x != arr[i]):       # If not x, skip
            continue

        if (first == -1):       # First time we see x
            first = i
            print("first:", first)
        else:
            last = i                # Keep updating last when x is seen
            print("last:", last)

    if (first != -1):           # If x was found
        print("First Occurrence =", first)
        print("Last Occurrence =", last)
    else:
        print("Not Found")

# Driver code
arr = [1, 2, 3, 4, 4, 4, 4, 4, 6, 7, 8]
n = len(arr)
findFirstAndLast(arr, n, 4)
'''


'''
# Function to find the first occurrence of x
def findFirst(arr, n, x):
    low = 0
    high = n - 1
    first = -1

    while low <= high:
        mid = low + (high - low) // 2  # To avoid overflow

        if arr[mid] == x:
            first = mid          # Potential first occurrence
            high = mid - 1       # Look on the left side for earlier occurrence
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return first

# Function to find the last occurrence of x
def findLast(arr, n, x):
    low = 0
    high = n - 1
    last = -1

    while low <= high:
        mid = low + (high - low) // 2  # To avoid overflow

        if arr[mid] == x:
            last = mid           # Potential last occurrence
            low = mid + 1        # Look on the right side for later occurrence
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return last

# Wrapper function to print results
def findFirstAndLast(arr, n, x):
    first = findFirst(arr, n, x)
    last = findLast(arr, n, x)

    if first != -1:
        print("First Occurrence =", first)
        print("Last Occurrence  =", last)
    else:
        print("Element not found")

# Driver code
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
n = len(arr)
x = 2
findFirstAndLast(arr, n, x)

'''



#Count occurrenxes in sorted array
'''
def search(arr, x):
    n = len(arr)
    count = 0
    for i in range(0,n):
        if arr[i] == x:
            count = count+1

    if  count> 0:
        return count 
    return -1 

arr = [1,2,3,4,4,4,6,8]
print(search(arr,4))

arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
print(search(arr,x = 2))
'''

#The time complexity is O(N).., we can reduce it to O(LOGN) using Binary Search


