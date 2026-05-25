'''
   assert statement:
   ->this is a debugging statement used to check or test
   whether a condition is true
   ->is condition is false it will throw an error (AssertError)


age=10

assert age>=18,"age must be greater than 18" #if its given like this it will print the statement with the error** 
print("eligible to vote")
'''
'''
********FUNCTIONS*****

--->a function is a block of code which only executed when it is called..
--> we can pass data, known as parameters into a function
-->to avoid repeated lines in code

syntax--->
def function_name(parameters):    #definition of the function
    -----------
    --------------
    ---------
function_name(arguments)   # calling the function


#the below code explains the definition we given to function
num=10
def even(num):  #if i give two here
    if num % 2 ==0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
even(num) #calling function should also have two
even(105)
even(2000)


ways to pass arguments:
----->a function must be called with the same number of arguments as the parameter
def even(num):  
    if num % 2 ==0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
even(109,90)   #it will throw an error


def even(num,num1,num2):  
    if num % 2 ==0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
even(109,90) #it will also throw error


----------> default arguments
by default values is defined at parameters but it will take the values from arguments onlyy

def info(name='siri',age=21):
    print(name)
    print(age)
info('saranya',22) #it will take these values only

--------->keyword argument
we can send arguments with key=value syntax. By this,the order of arguments does not matter....

def info(age,name):
    print(name)
    print(age)
info(name='siri',age=21)  #here the oder is reversed but it will not throw a error as it will print in argument order only

--------->variable length argument
'''
def info(*name):
    print(name[2])
info('siri','saranya','satya','kanakasri')



