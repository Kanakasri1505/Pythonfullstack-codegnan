
'''
   1.type conversions
    int----> can be converted into string,float
ex
an=78
us=str(an) #if we print type it will be give str
om=float(an) #same as above

    str-----> -can be converted to int if pure int characters are present
              #same as to float

              -can be converted to list and tuple to
ex
an=90
os=list(an)
print(os)---->['9','0']
on=tuple(an)
print(on)---->('9','0')

    float----->can be into int and into string
ex
car=90.58
print(int(car))

    list------->can be converted into string,tuple
ex
any=[6,7]
print(str(any))

    tuple------->can be converted into list and string
ex
how=(4,5)
print(list(how))

    input statement
    '''
'''
     int as a user input
num=int(input("enter a number:"))  #only takes integer input and throws error for evrything else
print(num + 65)


     string as a user input
     '''
'''
str1=input("enter a string:")    #considers anything as string only like list,tuple anything
print(str1)
   *why use map(list as a user input)
num=list(map(int,input("enter a number:").split())) #explanantion in notes

    tuple as a user input
num=tuple(map(int,input("enter a number:").split()))

***eval
   takes any form of input like int or list or tuple
   '''

num=eval(input("enter"))
print(type(num))

    

     

    
