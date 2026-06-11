'''
   *****FILE-HANDLING:
   
   -->file handler is an object of file to maintain several functions of file such as creating,
   reading, updating and deleting the file..

   -->open a file:
      1.open()  #should close manually
      syntax:
      name=open('file',mode)
      ex:
so=open('demo.txt','r')
print(so.read())
so.close()
      
      2.with open() #closes automatically after the file is read

with open('d.txt','r') as so:
    print(so.read())

    ->modes:
     -'r'------>is used to read the file,error if file doesnot exist...
     
     -'a'---->is used to add the text into file at last index...
     
     -'w'-->is used to add text into file but it will override all the text inside file...(removes everything present before and writes new)
           if the file does not exist it will create a new file(no error is thrown)

     -'x'-->it is used to create an error( it will throw an error if u try to use 'r' mode )

    ->methods:
    1.write()
    -->used for both 'a' and 'w' mode

with open('d.txt','a') as so:
    print(so.write())

with open('d.txt','w') as so:
    print(so.write())

    
    2.read()
    -->this method can read file chunk by chunk where we can specify the size
    
with open('d.txt','r') as so:
    print(so.read())
    
    3.realine()
    -->can read only 1 line at a time in a file

with open('d.txt','r') as so:
    print(so.readline())
    
    4.readlines()
     -->it will read entire file and gives ina list where each line is each index in a list


with open('d.txt','r') as so:
    print(so.readlines())
'''




