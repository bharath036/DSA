#https://www.geeksforgeeks.org/file-handling-python/
import os

def create_file(filename):
    if os.path.exists(filename):
        print("file already exists")
    else:
        with open(filename,'w') as f:
            f.write('Hello, world \n')
        print('File ' + filename + "created successfully.")
   

def read_file(filename):
    with open(filename,'r') as f:
        contents = f.read()
        print(contents)

def append_file(filename,text):
    with open(filename,'a') as f:
        f.write(text)

def rename_file(filename,new_filename):
    if os.path.exists(new_filename):
        os.remove(new_filename)
        print("Already existing file removed")
        os.rename(filename,new_filename)
        print("filename has changed from "+ filename + "to "+ new_filename)

def delete_file(new_filename):
    os.remove(new_filename)
    print('file deleted successfully')

if __name__ == '__main__':
    filename = 'example.txt'
    new_filename = 'new_example.txt'

    create_file(filename)
    read_file(filename)
    append_file(filename,"This is some additional text.\n")
    read_file(filename)
    rename_file(filename,new_filename)
    read_file(new_filename)
    #delete_file(new_filename)