'''
-->We can open files and manipulate data or create a file.
Before we read the contents of the file, we must tell python
which file we are doing operations with the file.
--> Using open() function we can open a file.
handle = open(filename , mode)
mode can be w or r 
ex:- fhnad = open('mbox.txt','r')
-->filename is a string
-->returns a handle use to manipulate the file.
-->Handle is like our connection between our code and file
-->A text file has new lines at the end of each line.
'''

'''
counting lines in a file:-

-->open a file read only
--> use loop to go through each line read only
--> count and print the lines.
fhand = open('.txt','r')
count = 0
for line in fhand:
    count = count+1

print(count)
'''

'''
Reading the whole file:

We can read the whole file(newlines and all) into a single string.

fhand = open('.txt')
inp = fhand.read()
print(len(inp))
print(inp[:20])
'''

'''
Searching through a file:
We can use if statement and check it that line matches specific crieteria through a loop

fhand = open('.txt','w')
for line in fhand:
    if line.startswith('from :')
        print(line)
**-->If we print lines, we will get one more line space because
            -->each line from the file has a newline at the end.
            -->The print statement adds a new line to each line.

To fix this we use rstrip or lstrip ---> To fix white spaces.
fhand = open('.txt','r')
for line in fhand:
    line = line.rstrip()
    if line.startswith('from: '):
        print(line)
'''