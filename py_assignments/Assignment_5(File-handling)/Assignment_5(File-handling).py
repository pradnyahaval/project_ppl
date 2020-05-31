'''Raise and handle exception in file handling'''

try:
    f=open("try.txt", "r") 
    print(f.read())
    f.close()
except:
    print("File can't be opened")


